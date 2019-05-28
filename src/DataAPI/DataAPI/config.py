import os


class Config:
    """
    Global application configuration
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my super secret key'
