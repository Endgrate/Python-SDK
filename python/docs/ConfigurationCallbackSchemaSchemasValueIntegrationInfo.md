# ConfigurationCallbackSchemaSchemasValueIntegrationInfo

integration information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**endgrate_type** | **str** | A valid &#x60;endgrate_type&#x60; for the session. If no &#x60;endgrate_type&#x60; was specified, the title of the schema can be used instead. | [optional] 
**supports_associations** | **bool** |  | [optional] 

## Example

```python
from endgrate.models.configuration_callback_schema_schemas_value_integration_info import ConfigurationCallbackSchemaSchemasValueIntegrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationCallbackSchemaSchemasValueIntegrationInfo from a JSON string
configuration_callback_schema_schemas_value_integration_info_instance = ConfigurationCallbackSchemaSchemasValueIntegrationInfo.from_json(json)
# print the JSON string representation of the object
print ConfigurationCallbackSchemaSchemasValueIntegrationInfo.to_json()

# convert the object into a dict
configuration_callback_schema_schemas_value_integration_info_dict = configuration_callback_schema_schemas_value_integration_info_instance.to_dict()
# create an instance of ConfigurationCallbackSchemaSchemasValueIntegrationInfo from a dict
configuration_callback_schema_schemas_value_integration_info_form_dict = configuration_callback_schema_schemas_value_integration_info.from_dict(configuration_callback_schema_schemas_value_integration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


