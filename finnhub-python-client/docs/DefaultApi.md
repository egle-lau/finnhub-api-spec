# openapi_client.DefaultApi

All URIs are relative to *https://finnhub.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_quote**](DefaultApi.md#get_quote) | **GET** /quote | Get real-time quote


# **get_quote**
> QuoteResponse get_quote(symbol, token)

Get real-time quote

Returns real-time price quote for a given stock symbol.

### Example


```python
import openapi_client
from openapi_client.models.quote_response import QuoteResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://finnhub.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://finnhub.io/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    symbol = 'symbol_example' # str | Stock symbol (e.g. AAPL, TSLA)
    token = 'token_example' # str | Your API key from Finnhub

    try:
        # Get real-time quote
        api_response = api_instance.get_quote(symbol, token)
        print("The response of DefaultApi->get_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Stock symbol (e.g. AAPL, TSLA) | 
 **token** | **str**| Your API key from Finnhub | 

### Return type

[**QuoteResponse**](QuoteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with quote data |  -  |
**401** | Unauthorized – invalid or missing API key |  -  |
**429** | Too Many Requests – rate limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

