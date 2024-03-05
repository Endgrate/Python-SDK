# GetApiIntegrations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | [**List[GetApiIntegrations200ResponseProvidersInner]**](GetApiIntegrations200ResponseProvidersInner.md) |  | [optional] 

## Example

```python
from endgrate.models.get_api_integrations200_response import GetApiIntegrations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiIntegrations200Response from a JSON string
get_api_integrations200_response_instance = GetApiIntegrations200Response.from_json(json)
# print the JSON string representation of the object
print GetApiIntegrations200Response.to_json()

# convert the object into a dict
get_api_integrations200_response_dict = get_api_integrations200_response_instance.to_dict()
# create an instance of GetApiIntegrations200Response from a dict
get_api_integrations200_response_form_dict = get_api_integrations200_response.from_dict(get_api_integrations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


