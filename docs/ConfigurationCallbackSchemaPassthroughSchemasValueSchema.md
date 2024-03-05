# ConfigurationCallbackSchemaPassthroughSchemasValueSchema

JSON schema of the endgrate type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**associations** | **bool** |  | [optional] 
**endgrate_type** | **str** |  | [optional] 
**properties** | **object** |  | [optional] 
**title** | **str** |  | [optional] 
**session_method** | **str** |  | [optional] 

## Example

```python
from endgrate.models.configuration_callback_schema_passthrough_schemas_value_schema import ConfigurationCallbackSchemaPassthroughSchemasValueSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationCallbackSchemaPassthroughSchemasValueSchema from a JSON string
configuration_callback_schema_passthrough_schemas_value_schema_instance = ConfigurationCallbackSchemaPassthroughSchemasValueSchema.from_json(json)
# print the JSON string representation of the object
print ConfigurationCallbackSchemaPassthroughSchemasValueSchema.to_json()

# convert the object into a dict
configuration_callback_schema_passthrough_schemas_value_schema_dict = configuration_callback_schema_passthrough_schemas_value_schema_instance.to_dict()
# create an instance of ConfigurationCallbackSchemaPassthroughSchemasValueSchema from a dict
configuration_callback_schema_passthrough_schemas_value_schema_form_dict = configuration_callback_schema_passthrough_schemas_value_schema.from_dict(configuration_callback_schema_passthrough_schemas_value_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


