# GetApiStatistics200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | [optional] 
**completed** | **bool** |  | [optional] 
**initiated** | **str** |  | [optional] 
**statistics** | **object** |  | [optional] 

## Example

```python
from endgrate.models.get_api_statistics200_response import GetApiStatistics200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiStatistics200Response from a JSON string
get_api_statistics200_response_instance = GetApiStatistics200Response.from_json(json)
# print the JSON string representation of the object
print GetApiStatistics200Response.to_json()

# convert the object into a dict
get_api_statistics200_response_dict = get_api_statistics200_response_instance.to_dict()
# create an instance of GetApiStatistics200Response from a dict
get_api_statistics200_response_form_dict = get_api_statistics200_response.from_dict(get_api_statistics200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


