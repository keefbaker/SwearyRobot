"""
Pull through environment variables for creds
"""
import os

API_KEY = os.environ.get('apiKey')
API_SECRET = os.environ.get('apiSecret')
ACCESS_TOKEN = os.environ.get('accessToken')
ACCESS_SECRET = os.environ.get('accessSecret')
