# ConfigurationCallbackSchemaPassthroughSchemasValuePassthroughFields

JSON schema of passthrough fields. For passthough schemas, all properties are passthrough fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | **object** |  | [optional] 
**required** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.configuration_callback_schema_passthrough_schemas_value_passthrough_fields import ConfigurationCallbackSchemaPassthroughSchemasValuePassthroughFields

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationCallbackSchemaPassthroughSchemasValuePassthroughFields from a JSON string
configuration_callback_schema_passthrough_schemas_value_passthrough_fields_instance = ConfigurationCallbackSchemaPassthroughSchemasValuePassthroughFields.from_json(json)
# print the JSON string representation of the object
print ConfigurationCallbackSchemaPassthroughSchemasValuePassthroughFields.to_json()

# convert the object into a dict
configuration_callback_schema_passthrough_schemas_value_passthrough_fields_dict = configuration_callback_schema_passthrough_schemas_value_passthrough_fields_instance.to_dict()
# create an instance of ConfigurationCallbackSchemaPassthroughSchemasValuePassthroughFields from a dict
configuration_callback_schema_passthrough_schemas_value_passthrough_fields_form_dict = configuration_callback_schema_passthrough_schemas_value_passthrough_fields.from_dict(configuration_callback_schema_passthrough_schemas_value_passthrough_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


