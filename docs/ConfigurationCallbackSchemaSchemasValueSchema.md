# ConfigurationCallbackSchemaSchemasValueSchema

JSON schema of the endgrate type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**associations** | **bool** |  | [optional] 
**endgrate_type** | **str** | A valid &#x60;endgrate_type&#x60; for the session. If no &#x60;endgrate_type&#x60; was specified, the title of the schema can be used instead. | [optional] 
**properties** | **object** |  | [optional] 
**required** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**session_method** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.configuration_callback_schema_schemas_value_schema import ConfigurationCallbackSchemaSchemasValueSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationCallbackSchemaSchemasValueSchema from a JSON string
configuration_callback_schema_schemas_value_schema_instance = ConfigurationCallbackSchemaSchemasValueSchema.from_json(json)
# print the JSON string representation of the object
print ConfigurationCallbackSchemaSchemasValueSchema.to_json()

# convert the object into a dict
configuration_callback_schema_schemas_value_schema_dict = configuration_callback_schema_schemas_value_schema_instance.to_dict()
# create an instance of ConfigurationCallbackSchemaSchemasValueSchema from a dict
configuration_callback_schema_schemas_value_schema_form_dict = configuration_callback_schema_schemas_value_schema.from_dict(configuration_callback_schema_schemas_value_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


