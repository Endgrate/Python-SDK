# ErrorListSchemaEndgrateIntegrationInfo

Integration information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**endgrate_type** | **str** |  | [optional] 
**supports_associations** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.error_list_schema_endgrate_integration_info import ErrorListSchemaEndgrateIntegrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorListSchemaEndgrateIntegrationInfo from a JSON string
error_list_schema_endgrate_integration_info_instance = ErrorListSchemaEndgrateIntegrationInfo.from_json(json)
# print the JSON string representation of the object
print ErrorListSchemaEndgrateIntegrationInfo.to_json()

# convert the object into a dict
error_list_schema_endgrate_integration_info_dict = error_list_schema_endgrate_integration_info_instance.to_dict()
# create an instance of ErrorListSchemaEndgrateIntegrationInfo from a dict
error_list_schema_endgrate_integration_info_form_dict = error_list_schema_endgrate_integration_info.from_dict(error_list_schema_endgrate_integration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


