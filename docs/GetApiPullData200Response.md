# GetApiPullData200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**meta** | [**GetApiPullData200ResponseMeta**](GetApiPullData200ResponseMeta.md) |  | [optional] 
**transfer_data** | [**List[TransferDataSchemaInner]**](TransferDataSchemaInner.md) | Returned transfer data. | [optional] 

## Example

```python
from endgrate.models.get_api_pull_data200_response import GetApiPullData200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiPullData200Response from a JSON string
get_api_pull_data200_response_instance = GetApiPullData200Response.from_json(json)
# print the JSON string representation of the object
print GetApiPullData200Response.to_json()

# convert the object into a dict
get_api_pull_data200_response_dict = get_api_pull_data200_response_instance.to_dict()
# create an instance of GetApiPullData200Response from a dict
get_api_pull_data200_response_form_dict = get_api_pull_data200_response.from_dict(get_api_pull_data200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


