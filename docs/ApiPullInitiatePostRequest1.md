# ApiPullInitiatePostRequest1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**pk** | **object** |  | [optional] 
**transfer_id** | **object** |  | [optional] 
**session_id** | **object** |  | [optional] 
**timestamp** | **object** |  | [optional] 
**error_resolve_text** | **object** |  | [optional] 
**error_type** | **object** | The &#x60;internal&#x60; error type indicates a problem with the internal server. The &#x60;integration&#x60; error type indicates a problem with the chosen integration. The &#x60;upstream&#x60; error type indicates a problem that arises from the integration provider. Errors classified as &#x60;authentication&#x60; are related to user authentication processes, including login issues or problems with access tokens. Lastly, &#x60;mapping&#x60; errors occur when there are discrepancies or issues in data mapping, such as invalid data points or incorrect alignments of data fields. | [optional] 
**resolved** | **object** |  | [optional] 
**endgrate** | [**ErrorListSchemaEndgrate**](ErrorListSchemaEndgrate.md) |  | [optional] 
**metadata** | **object** | The metadata from ${request.body#/error_webhook/metadata}. | [optional] 

## Example

```python
from openapi_client.models.api_pull_initiate_post_request1 import ApiPullInitiatePostRequest1

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPullInitiatePostRequest1 from a JSON string
api_pull_initiate_post_request1_instance = ApiPullInitiatePostRequest1.from_json(json)
# print the JSON string representation of the object
print ApiPullInitiatePostRequest1.to_json()

# convert the object into a dict
api_pull_initiate_post_request1_dict = api_pull_initiate_post_request1_instance.to_dict()
# create an instance of ApiPullInitiatePostRequest1 from a dict
api_pull_initiate_post_request1_form_dict = api_pull_initiate_post_request1.from_dict(api_pull_initiate_post_request1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


