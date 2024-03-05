# ConfigurationCallbackSchemaSchemasValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_info** | [**ConfigurationCallbackSchemaSchemasValueIntegrationInfo**](ConfigurationCallbackSchemaSchemasValueIntegrationInfo.md) |  | [optional] 
**integration** | **str** |  | [optional] 
**var_schema** | [**ConfigurationCallbackSchemaSchemasValueSchema**](ConfigurationCallbackSchemaSchemasValueSchema.md) |  | [optional] 
**passthrough_fields** | [**ConfigurationCallbackSchemaSchemasValuePassthroughFields**](ConfigurationCallbackSchemaSchemasValuePassthroughFields.md) |  | [optional] 

## Example

```python
from openapi_client.models.configuration_callback_schema_schemas_value import ConfigurationCallbackSchemaSchemasValue

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationCallbackSchemaSchemasValue from a JSON string
configuration_callback_schema_schemas_value_instance = ConfigurationCallbackSchemaSchemasValue.from_json(json)
# print the JSON string representation of the object
print ConfigurationCallbackSchemaSchemasValue.to_json()

# convert the object into a dict
configuration_callback_schema_schemas_value_dict = configuration_callback_schema_schemas_value_instance.to_dict()
# create an instance of ConfigurationCallbackSchemaSchemasValue from a dict
configuration_callback_schema_schemas_value_form_dict = configuration_callback_schema_schemas_value.from_dict(configuration_callback_schema_schemas_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


