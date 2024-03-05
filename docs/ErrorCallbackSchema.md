# ErrorCallbackSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**pk** | **str** |  | [optional] 
**transfer_id** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**error_resolve_text** | **str** |  | [optional] 
**error_type** | **str** | The &#x60;internal&#x60; error type indicates a problem with the internal server. The &#x60;integration&#x60; error type indicates a problem with the chosen integration. The &#x60;upstream&#x60; error type indicates a problem that arises from the integration provider. Errors classified as &#x60;authentication&#x60; are related to user authentication processes, including login issues or problems with access tokens. Lastly, &#x60;mapping&#x60; errors occur when there are discrepancies or issues in data mapping, such as invalid data points or incorrect alignments of data fields. | [optional] 
**resolved** | **bool** |  | [optional] 
**endgrate** | [**ErrorListSchemaEndgrate**](ErrorListSchemaEndgrate.md) |  | [optional] 

## Example

```python
from openapi_client.models.error_callback_schema import ErrorCallbackSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorCallbackSchema from a JSON string
error_callback_schema_instance = ErrorCallbackSchema.from_json(json)
# print the JSON string representation of the object
print ErrorCallbackSchema.to_json()

# convert the object into a dict
error_callback_schema_dict = error_callback_schema_instance.to_dict()
# create an instance of ErrorCallbackSchema from a dict
error_callback_schema_form_dict = error_callback_schema.from_dict(error_callback_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


