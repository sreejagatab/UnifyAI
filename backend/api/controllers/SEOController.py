# SEOController.py
from flask import jsonify
from ..services.SEOService import optimize_seo

@app.route('/api/seo/optimize', methods=['POST'])
def optimize_page_seo():
    try:
        optimize_seo()
        return jsonify({"status": "SEO optimization success"}), 200
    except Exception as e:
        print(f"SEO optimization failed: {e}")
        return jsonify({"error": "Failed to optimize SEO"}), 500
