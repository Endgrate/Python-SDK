# CompletedCallbackSchemaEndgrate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endgrate_type** | **str** | A valid &#x60;endgrate_type&#x60; for the session. If no &#x60;endgrate_type&#x60; was specified, the title of the schema can be used instead. | [optional] 

## Example

```python
from endgrate.models.completed_callback_schema_endgrate import CompletedCallbackSchemaEndgrate

# TODO update the JSON string below
json = "{}"
# create an instance of CompletedCallbackSchemaEndgrate from a JSON string
completed_callback_schema_endgrate_instance = CompletedCallbackSchemaEndgrate.from_json(json)
# print the JSON string representation of the object
print CompletedCallbackSchemaEndgrate.to_json()

# convert the object into a dict
completed_callback_schema_endgrate_dict = completed_callback_schema_endgrate_instance.to_dict()
# create an instance of CompletedCallbackSchemaEndgrate from a dict
completed_callback_schema_endgrate_form_dict = completed_callback_schema_endgrate.from_dict(completed_callback_schema_endgrate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


