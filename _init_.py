"""
Application factory for the Simple Blog app.

This module creates and configures the Flask application.
"""

from flask import Flask
import os

def create_app(test_config=None):
    """
    Create and configure the Flask app.

    Args:
        test_config (dict, optional): Configuration dictionary for testing.

    Returns:
        Flask: The configured Flask application.
    """
    # Create the Flask app instance
    app = Flask(__name__, instance_relative_config=True)
    
    # Set default configuration
    app.config.from_mapping(
        SECRET_KEY='dev',  # Use a secure key in production!
        DATABASE=os.path.join(app.instance_path, 'blog.sqlite')
    )

    # Override config if test_config is provided
    if test_config:
        app.config.update(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize the database
    from . import db
    db.init_app(app)

    # Register the blueprint for blog routes
    from . import routes
    app.register_blueprint(routes.bp)

    return app
