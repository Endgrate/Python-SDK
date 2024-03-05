# DataCallbackSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**transfer_id** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**metadata** | **object** | The metadata from ${request.body#/data_webhook/metadata}. | [optional] 
**endgrate** | [**CompletedCallbackSchemaEndgrate**](CompletedCallbackSchemaEndgrate.md) |  | [optional] 
**completed** | **bool** | Whether or not the transfer has completed. | [optional] 
**transfer_data** | [**List[TransferDataSchemaInner]**](TransferDataSchemaInner.md) | Returned transfer data. | [optional] 

## Example

```python
from endgrate.models.data_callback_schema import DataCallbackSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DataCallbackSchema from a JSON string
data_callback_schema_instance = DataCallbackSchema.from_json(json)
# print the JSON string representation of the object
print DataCallbackSchema.to_json()

# convert the object into a dict
data_callback_schema_dict = data_callback_schema_instance.to_dict()
# create an instance of DataCallbackSchema from a dict
data_callback_schema_form_dict = data_callback_schema.from_dict(data_callback_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


