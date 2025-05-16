from finnhub_python import Configuration, ApiClient, DefaultApi
from pprint import pprint

# 🔐 Replace this with your actual API key
API_KEY = "your_finnhub_api_key"

# Configure API key authorization
configuration = Configuration()
configuration.api_key['token'] = API_KEY

# Create API client and instance
with ApiClient(configuration) as api_client:
    api_instance = DefaultApi(api_client)

    # Replace 'AAPL' with any stock symbol you want
    symbol = "AAPL"

    try:
        response = api_instance.quote_get(symbol=symbol)
        pprint(response)
    except Exception as e:
        print(f"Exception when calling DefaultApi->quote_get: {e}")
