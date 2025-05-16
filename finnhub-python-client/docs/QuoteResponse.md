# QuoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**c** | **float** | Current price | 
**d** | **float** | Absolute change from previous close | [optional] 
**dp** | **float** | Percent change from previous close | [optional] 
**h** | **float** | High price of the day | 
**l** | **float** | Low price of the day | 
**o** | **float** | Open price of the day | 
**pc** | **float** | Previous close price | 
**t** | **int** | Timestamp (Unix) | 

## Example

```python
from openapi_client.models.quote_response import QuoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteResponse from a JSON string
quote_response_instance = QuoteResponse.from_json(json)
# print the JSON string representation of the object
print(QuoteResponse.to_json())

# convert the object into a dict
quote_response_dict = quote_response_instance.to_dict()
# create an instance of QuoteResponse from a dict
quote_response_from_dict = QuoteResponse.from_dict(quote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


