# ConfigurationCallbackSchemaPassthroughSchemasValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_info** | [**ConfigurationCallbackSchemaPassthroughSchemasValueIntegrationInfo**](ConfigurationCallbackSchemaPassthroughSchemasValueIntegrationInfo.md) |  | [optional] 
**var_schema** | [**ConfigurationCallbackSchemaPassthroughSchemasValueSchema**](ConfigurationCallbackSchemaPassthroughSchemasValueSchema.md) |  | [optional] 
**passthrough_fields** | [**ConfigurationCallbackSchemaPassthroughSchemasValuePassthroughFields**](ConfigurationCallbackSchemaPassthroughSchemasValuePassthroughFields.md) |  | [optional] 

## Example

```python
from endgrate.models.configuration_callback_schema_passthrough_schemas_value import ConfigurationCallbackSchemaPassthroughSchemasValue

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationCallbackSchemaPassthroughSchemasValue from a JSON string
configuration_callback_schema_passthrough_schemas_value_instance = ConfigurationCallbackSchemaPassthroughSchemasValue.from_json(json)
# print the JSON string representation of the object
print ConfigurationCallbackSchemaPassthroughSchemasValue.to_json()

# convert the object into a dict
configuration_callback_schema_passthrough_schemas_value_dict = configuration_callback_schema_passthrough_schemas_value_instance.to_dict()
# create an instance of ConfigurationCallbackSchemaPassthroughSchemasValue from a dict
configuration_callback_schema_passthrough_schemas_value_form_dict = configuration_callback_schema_passthrough_schemas_value.from_dict(configuration_callback_schema_passthrough_schemas_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


