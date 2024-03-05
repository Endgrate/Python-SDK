# EndgrateJsonSchema

full JSON schema of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**associations** | **bool** |  | [optional] 
**endgrate_type** | **str** | This field requires a valid &#x60;endgrate_type&#x60;. If you choose not to utilize a predefined &#x60;endgrate_type&#x60;, you must provide a &#x60;title&#x60;. | [optional] 
**properties** | **object** |  | [optional] 
**required** | **List[str]** |  | [optional] 
**title** | **str** | The &#x60;title&#x60; of this schema that will be displayed to the user. If no &#x60;endgrate_type&#x60; has been provided, &#x60;title&#x60; should be used as a substitute for &#x60;endgrate_type&#x60; in subsequent API calls. | [optional] 

## Example

```python
from endgrate.models.endgrate_json_schema import EndgrateJsonSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EndgrateJsonSchema from a JSON string
endgrate_json_schema_instance = EndgrateJsonSchema.from_json(json)
# print the JSON string representation of the object
print EndgrateJsonSchema.to_json()

# convert the object into a dict
endgrate_json_schema_dict = endgrate_json_schema_instance.to_dict()
# create an instance of EndgrateJsonSchema from a dict
endgrate_json_schema_form_dict = endgrate_json_schema.from_dict(endgrate_json_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


