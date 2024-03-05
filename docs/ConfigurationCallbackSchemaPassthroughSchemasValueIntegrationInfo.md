# ConfigurationCallbackSchemaPassthroughSchemasValueIntegrationInfo

Integration information.

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
from openapi_client.models.configuration_callback_schema_passthrough_schemas_value_integration_info import ConfigurationCallbackSchemaPassthroughSchemasValueIntegrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationCallbackSchemaPassthroughSchemasValueIntegrationInfo from a JSON string
configuration_callback_schema_passthrough_schemas_value_integration_info_instance = ConfigurationCallbackSchemaPassthroughSchemasValueIntegrationInfo.from_json(json)
# print the JSON string representation of the object
print ConfigurationCallbackSchemaPassthroughSchemasValueIntegrationInfo.to_json()

# convert the object into a dict
configuration_callback_schema_passthrough_schemas_value_integration_info_dict = configuration_callback_schema_passthrough_schemas_value_integration_info_instance.to_dict()
# create an instance of ConfigurationCallbackSchemaPassthroughSchemasValueIntegrationInfo from a dict
configuration_callback_schema_passthrough_schemas_value_integration_info_form_dict = configuration_callback_schema_passthrough_schemas_value_integration_info.from_dict(configuration_callback_schema_passthrough_schemas_value_integration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


