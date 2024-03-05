# GetApiIntegrations200ResponseProvidersInnerProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**auth_type** | **str** |  | [optional] 
**specific** | **object** |  | [optional] 
**endgrate_provider_type** | **str** |  | [optional] 

## Example

```python
from endgrate.models.get_api_integrations200_response_providers_inner_provider import GetApiIntegrations200ResponseProvidersInnerProvider

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiIntegrations200ResponseProvidersInnerProvider from a JSON string
get_api_integrations200_response_providers_inner_provider_instance = GetApiIntegrations200ResponseProvidersInnerProvider.from_json(json)
# print the JSON string representation of the object
print GetApiIntegrations200ResponseProvidersInnerProvider.to_json()

# convert the object into a dict
get_api_integrations200_response_providers_inner_provider_dict = get_api_integrations200_response_providers_inner_provider_instance.to_dict()
# create an instance of GetApiIntegrations200ResponseProvidersInnerProvider from a dict
get_api_integrations200_response_providers_inner_provider_form_dict = get_api_integrations200_response_providers_inner_provider.from_dict(get_api_integrations200_response_providers_inner_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


