# GetApiIntegrations200ResponseProvidersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**GetApiIntegrations200ResponseProvidersInnerProvider**](GetApiIntegrations200ResponseProvidersInnerProvider.md) |  | [optional] 
**integrations** | [**List[GetApiIntegrations200ResponseProvidersInnerIntegrationsInner]**](GetApiIntegrations200ResponseProvidersInnerIntegrationsInner.md) |  | [optional] 

## Example

```python
from endgrate.models.get_api_integrations200_response_providers_inner import GetApiIntegrations200ResponseProvidersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiIntegrations200ResponseProvidersInner from a JSON string
get_api_integrations200_response_providers_inner_instance = GetApiIntegrations200ResponseProvidersInner.from_json(json)
# print the JSON string representation of the object
print GetApiIntegrations200ResponseProvidersInner.to_json()

# convert the object into a dict
get_api_integrations200_response_providers_inner_dict = get_api_integrations200_response_providers_inner_instance.to_dict()
# create an instance of GetApiIntegrations200ResponseProvidersInner from a dict
get_api_integrations200_response_providers_inner_form_dict = get_api_integrations200_response_providers_inner.from_dict(get_api_integrations200_response_providers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


