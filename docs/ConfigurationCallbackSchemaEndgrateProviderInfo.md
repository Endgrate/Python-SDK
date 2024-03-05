# ConfigurationCallbackSchemaEndgrateProviderInfo

Provider information.

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
from endgrate.models.configuration_callback_schema_endgrate_provider_info import ConfigurationCallbackSchemaEndgrateProviderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationCallbackSchemaEndgrateProviderInfo from a JSON string
configuration_callback_schema_endgrate_provider_info_instance = ConfigurationCallbackSchemaEndgrateProviderInfo.from_json(json)
# print the JSON string representation of the object
print ConfigurationCallbackSchemaEndgrateProviderInfo.to_json()

# convert the object into a dict
configuration_callback_schema_endgrate_provider_info_dict = configuration_callback_schema_endgrate_provider_info_instance.to_dict()
# create an instance of ConfigurationCallbackSchemaEndgrateProviderInfo from a dict
configuration_callback_schema_endgrate_provider_info_form_dict = configuration_callback_schema_endgrate_provider_info.from_dict(configuration_callback_schema_endgrate_provider_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


