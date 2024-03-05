# TransferResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**transfer_id** | **str** |  | [optional] 
**statistics** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.transfer_response_schema import TransferResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TransferResponseSchema from a JSON string
transfer_response_schema_instance = TransferResponseSchema.from_json(json)
# print the JSON string representation of the object
print TransferResponseSchema.to_json()

# convert the object into a dict
transfer_response_schema_dict = transfer_response_schema_instance.to_dict()
# create an instance of TransferResponseSchema from a dict
transfer_response_schema_form_dict = transfer_response_schema.from_dict(transfer_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


