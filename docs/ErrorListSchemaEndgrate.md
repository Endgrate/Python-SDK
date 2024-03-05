# ErrorListSchemaEndgrate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_info** | [**ConfigurationCallbackSchemaEndgrateProviderInfo**](ConfigurationCallbackSchemaEndgrateProviderInfo.md) |  | [optional] 
**integration_info** | [**ErrorListSchemaEndgrateIntegrationInfo**](ErrorListSchemaEndgrateIntegrationInfo.md) |  | [optional] 

## Example

```python
from endgrate.models.error_list_schema_endgrate import ErrorListSchemaEndgrate

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorListSchemaEndgrate from a JSON string
error_list_schema_endgrate_instance = ErrorListSchemaEndgrate.from_json(json)
# print the JSON string representation of the object
print ErrorListSchemaEndgrate.to_json()

# convert the object into a dict
error_list_schema_endgrate_dict = error_list_schema_endgrate_instance.to_dict()
# create an instance of ErrorListSchemaEndgrate from a dict
error_list_schema_endgrate_form_dict = error_list_schema_endgrate.from_dict(error_list_schema_endgrate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


