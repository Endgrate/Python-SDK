# PullTransferSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bypass_rate_limit** | **object** | Whether or not to bypass the integration/provider rate limit when transferring data. | [optional] 
**endgrate_type** | **str** | A valid &#x60;endgrate_type&#x60; for the session. If no &#x60;endgrate_type&#x60; was specified, the title of the schema can be used instead. | 
**params** | **object** |  | [optional] 
**session_id** | **str** |  | 
**synchronous** | **object** | Whether or not to make this API request synchronous. If true, Endgrate will poll the status of the transfer interally, and return only when the transfer is completed, with a 5 minute maximum polling time. | [optional] 

## Example

```python
from endgrate.models.pull_transfer_schema import PullTransferSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PullTransferSchema from a JSON string
pull_transfer_schema_instance = PullTransferSchema.from_json(json)
# print the JSON string representation of the object
print PullTransferSchema.to_json()

# convert the object into a dict
pull_transfer_schema_dict = pull_transfer_schema_instance.to_dict()
# create an instance of PullTransferSchema from a dict
pull_transfer_schema_form_dict = pull_transfer_schema.from_dict(pull_transfer_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


