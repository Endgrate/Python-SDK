# GetApiPullData200ResponseMeta

Paging metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**previous** | [**GetApiPullData200ResponseMetaPrevious**](GetApiPullData200ResponseMetaPrevious.md) |  | [optional] 
**next** | [**GetApiPullData200ResponseMetaPrevious**](GetApiPullData200ResponseMetaPrevious.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_api_pull_data200_response_meta import GetApiPullData200ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiPullData200ResponseMeta from a JSON string
get_api_pull_data200_response_meta_instance = GetApiPullData200ResponseMeta.from_json(json)
# print the JSON string representation of the object
print GetApiPullData200ResponseMeta.to_json()

# convert the object into a dict
get_api_pull_data200_response_meta_dict = get_api_pull_data200_response_meta_instance.to_dict()
# create an instance of GetApiPullData200ResponseMeta from a dict
get_api_pull_data200_response_meta_form_dict = get_api_pull_data200_response_meta.from_dict(get_api_pull_data200_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


