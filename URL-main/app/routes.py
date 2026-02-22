from flask import Blueprint, request, jsonify, redirect, current_app, render_template
from .utils import generate_short_code
from .models import (
    insert_url,
    find_original_url,
    find_existing_short_code,
    is_short_code_taken,
    increment_clicks,
    get_clicks
)

url_shortener_routes = Blueprint('url_shortener', __name__)

@url_shortener_routes.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@url_shortener_routes.route('/shorten', methods=['POST'])
def shorten_url():
    try:
        data = request.get_json()
        original_url = data.get("url")
        custom_code = data.get("custom_code")
        expires_in = data.get("expires_in")  # in hours

        if not original_url:
            return jsonify({"error": "URL is required"}), 400

        db = current_app.db

        # Use custom code if given
        if custom_code:
            if is_short_code_taken(db, custom_code):
                return jsonify({"error": "Custom code already taken"}), 409
            short_code = custom_code
        else:
            existing = find_existing_short_code(db, original_url)
            if existing:
                short_code = existing["short_code"]
            else:
                short_code = generate_short_code(original_url)

        insert_url(db, original_url, short_code, expires_in)

        short_url = f"{current_app.config['BASE_URL']}/{short_code}"
        return jsonify({
            "short_url": short_url,
            "custom_code": custom_code,
            "expires_in": expires_in
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@url_shortener_routes.route('/<short_code>', methods=['GET'])
def redirect_to_original(short_code):
    db = current_app.db
    original_url = find_original_url(db, short_code)

    if original_url:
        increment_clicks(db, short_code)
        return redirect(original_url)

    return render_template("404.html"), 404

@url_shortener_routes.route('/<short_code>/stats', methods=['GET'])
def get_stats(short_code):
    db = current_app.db
    clicks = get_clicks(db, short_code)
    return jsonify({
        "short_code": short_code,
        "clicks": clicks
    })
