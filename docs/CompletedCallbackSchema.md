# CompletedCallbackSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**transfer_id** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**metadata** | **object** | The metadata from ${request.body#/completed_webhook/metadata}. | [optional] 
**endgrate** | [**CompletedCallbackSchemaEndgrate**](CompletedCallbackSchemaEndgrate.md) |  | [optional] 
**completed** | **bool** | Success flag indicating the transfer has completed. | [optional] 

## Example

```python
from openapi_client.models.completed_callback_schema import CompletedCallbackSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CompletedCallbackSchema from a JSON string
completed_callback_schema_instance = CompletedCallbackSchema.from_json(json)
# print the JSON string representation of the object
print CompletedCallbackSchema.to_json()

# convert the object into a dict
completed_callback_schema_dict = completed_callback_schema_instance.to_dict()
# create an instance of CompletedCallbackSchema from a dict
completed_callback_schema_form_dict = completed_callback_schema.from_dict(completed_callback_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


