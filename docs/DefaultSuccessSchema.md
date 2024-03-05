# DefaultSuccessSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**session_id** | **str** |  | [optional] 

## Example

```python
from endgrate.models.default_success_schema import DefaultSuccessSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultSuccessSchema from a JSON string
default_success_schema_instance = DefaultSuccessSchema.from_json(json)
# print the JSON string representation of the object
print DefaultSuccessSchema.to_json()

# convert the object into a dict
default_success_schema_dict = default_success_schema_instance.to_dict()
# create an instance of DefaultSuccessSchema from a dict
default_success_schema_form_dict = default_success_schema.from_dict(default_success_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


