import sys
print("Python executable:", sys.executable)
print("Python sys.path:", sys.path)

from openapi_client import Configuration, ApiClient, DefaultApi
from pprint import pprint

# 🔐 Replace this with your actual API key
API_KEY = "d0hhgqhr01qv1u37h420d0hhgqhr01qv1u37h42g"

# Configure API key authorization
configuration = Configuration()
configuration.api_key['token'] = API_KEY

# Create API client and instance
with ApiClient(configuration) as api_client:
    api_instance = DefaultApi(api_client)

    # Replace 'AAPL' with any stock symbol you want
    symbol = "AAPL"

    try:
        # Use get_quote and pass both symbol and token
        response = api_instance.get_quote(symbol=symbol, token=API_KEY)
        pprint(response)
    except Exception as e:
        print(f"Exception when calling DefaultApi->get_quote: {e}")
