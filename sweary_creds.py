"""
Pull through environment variables for creds
"""
import os

apiKey = os.environ.get('apiKey')
apiSecret = os.environ.get('apiSecret')
accessToken = os.environ.get('accessToken')
accessSecret = os.environ.get('accessSecret')
