# GetApiStatistics200ResponseStatisticsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_size** | **int** |  | [optional] 
**records** | **int** |  | [optional] 
**batches** | **int** |  | [optional] 
**batches_queued** | **int** |  | [optional] 
**batches_success** | **int** |  | [optional] 
**batches_fail** | **int** |  | [optional] 
**records_transferred** | **int** |  | [optional] 
**completed** | **bool** |  | [optional] 
**provider** | **str** |  | [optional] 
**integration** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_api_statistics200_response_statistics_value import GetApiStatistics200ResponseStatisticsValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiStatistics200ResponseStatisticsValue from a JSON string
get_api_statistics200_response_statistics_value_instance = GetApiStatistics200ResponseStatisticsValue.from_json(json)
# print the JSON string representation of the object
print GetApiStatistics200ResponseStatisticsValue.to_json()

# convert the object into a dict
get_api_statistics200_response_statistics_value_dict = get_api_statistics200_response_statistics_value_instance.to_dict()
# create an instance of GetApiStatistics200ResponseStatisticsValue from a dict
get_api_statistics200_response_statistics_value_form_dict = get_api_statistics200_response_statistics_value.from_dict(get_api_statistics200_response_statistics_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


