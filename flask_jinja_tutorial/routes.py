"""Route declaration."""
from flask import current_app as app
from flask import render_template
from flask import jsonify

nav = [
        {"name": "Home", "url": "/"},
        {"name": "About", "url": "about"},
        {"name": "Contact Us", "url": "/contact-us"},
    ]


@app.route("/")
def home():
    """Landing page route."""
    return render_template(
        "home.html",
        nav=nav,
        title="Jinja Demo Site",
        description="Smarter page templates with Flask & Jinja.",
    )


@app.route("/about")
def about():
    """Landing page route."""
    return render_template(
        "about.html",
        nav=nav,
        title="Jinja Demo Site",
        description="Smarter page templates with Flask & Jinja.",
    )


@app.route("/contact-us")
def contact_us():
    """Landing page route."""
    return render_template(
        "contact-us.html",
        nav=nav,
        title="Jinja Demo Site",
        description="Smarter page templates with Flask & Jinja.",
    )


@app.route("/temperature")
def temp():
    """Show the temperature"""
    return jsonify({'name': 'Jimit',
                    'address': 'India'})

