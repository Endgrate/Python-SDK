# GetApiErrors200ResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**previous** | [**GetApiErrors200ResponseMetaPrevious**](GetApiErrors200ResponseMetaPrevious.md) |  | [optional] 
**next** | [**GetApiErrors200ResponseMetaPrevious**](GetApiErrors200ResponseMetaPrevious.md) |  | [optional] 

## Example

```python
from endgrate.models.get_api_errors200_response_meta import GetApiErrors200ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiErrors200ResponseMeta from a JSON string
get_api_errors200_response_meta_instance = GetApiErrors200ResponseMeta.from_json(json)
# print the JSON string representation of the object
print GetApiErrors200ResponseMeta.to_json()

# convert the object into a dict
get_api_errors200_response_meta_dict = get_api_errors200_response_meta_instance.to_dict()
# create an instance of GetApiErrors200ResponseMeta from a dict
get_api_errors200_response_meta_form_dict = get_api_errors200_response_meta.from_dict(get_api_errors200_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


