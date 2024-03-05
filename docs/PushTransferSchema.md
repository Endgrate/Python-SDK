# PushTransferSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bypass_rate_limit** | **object** | Whether or not to bypass the integration/provider rate limit when transferring data. | [optional] 
**endgrate_type** | **str** | A valid &#x60;endgrate_type&#x60; for the session. If no &#x60;endgrate_type&#x60; was specified, the title of the schema can be used instead. | 
**session_id** | **str** |  | 
**synchronous** | **object** | Whether or not to make this API request synchronous. If true, If true, Endgrate will poll the status of the transfer interally, and return only when the transfer is completed, with a 5 minute maximum polling time. | [optional] 
**transfer_data** | **object** | An array of transfer data to be pushed out. | 

## Example

```python
from openapi_client.models.push_transfer_schema import PushTransferSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PushTransferSchema from a JSON string
push_transfer_schema_instance = PushTransferSchema.from_json(json)
# print the JSON string representation of the object
print PushTransferSchema.to_json()

# convert the object into a dict
push_transfer_schema_dict = push_transfer_schema_instance.to_dict()
# create an instance of PushTransferSchema from a dict
push_transfer_schema_form_dict = push_transfer_schema.from_dict(push_transfer_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


