# PostApiSchemasRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | [optional] 
**data** | [**List[PostApiSchemasRequestDataInner]**](PostApiSchemasRequestDataInner.md) |  | [optional] 

## Example

```python
from endgrate.models.post_api_schemas_request import PostApiSchemasRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostApiSchemasRequest from a JSON string
post_api_schemas_request_instance = PostApiSchemasRequest.from_json(json)
# print the JSON string representation of the object
print PostApiSchemasRequest.to_json()

# convert the object into a dict
post_api_schemas_request_dict = post_api_schemas_request_instance.to_dict()
# create an instance of PostApiSchemasRequest from a dict
post_api_schemas_request_form_dict = post_api_schemas_request.from_dict(post_api_schemas_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


