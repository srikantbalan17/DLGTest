import os


class Config:
    """ Global config for storing app related details, can be expanded """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my super secret key'
