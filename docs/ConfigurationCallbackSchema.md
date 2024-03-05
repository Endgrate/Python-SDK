# ConfigurationCallbackSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**session_id** | **str** |  | [optional] 
**endgrate** | [**ConfigurationCallbackSchemaEndgrate**](ConfigurationCallbackSchemaEndgrate.md) |  | [optional] 
**schemas** | **object** | Schema information, keyed by endgrate type. | [optional] 
**passthrough_schemas** | **object** | Passthrough schema information, keyed by endgrate type. | [optional] 

## Example

```python
from endgrate.models.configuration_callback_schema import ConfigurationCallbackSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationCallbackSchema from a JSON string
configuration_callback_schema_instance = ConfigurationCallbackSchema.from_json(json)
# print the JSON string representation of the object
print ConfigurationCallbackSchema.to_json()

# convert the object into a dict
configuration_callback_schema_dict = configuration_callback_schema_instance.to_dict()
# create an instance of ConfigurationCallbackSchema from a dict
configuration_callback_schema_form_dict = configuration_callback_schema.from_dict(configuration_callback_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


