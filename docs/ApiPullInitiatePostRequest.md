# ApiPullInitiatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **object** |  | [optional] 
**session_id** | **object** |  | [optional] 
**endgrate** | [**ConfigurationCallbackSchemaEndgrate**](ConfigurationCallbackSchemaEndgrate.md) |  | [optional] 
**schemas** | [**Dict[str, ConfigurationCallbackSchemaSchemasValue]**](ConfigurationCallbackSchemaSchemasValue.md) | Schema information, keyed by endgrate type. | [optional] 
**passthrough_schemas** | [**Dict[str, ConfigurationCallbackSchemaPassthroughSchemasValue]**](ConfigurationCallbackSchemaPassthroughSchemasValue.md) | Passthrough schema information, keyed by endgrate type. | [optional] 
**metadata** | **object** | The metadata from ${request.body#/data_webhook/metadata}. | [optional] 

## Example

```python
from endgrate.models.api_pull_initiate_post_request import ApiPullInitiatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPullInitiatePostRequest from a JSON string
api_pull_initiate_post_request_instance = ApiPullInitiatePostRequest.from_json(json)
# print the JSON string representation of the object
print ApiPullInitiatePostRequest.to_json()

# convert the object into a dict
api_pull_initiate_post_request_dict = api_pull_initiate_post_request_instance.to_dict()
# create an instance of ApiPullInitiatePostRequest from a dict
api_pull_initiate_post_request_form_dict = api_pull_initiate_post_request.from_dict(api_pull_initiate_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


