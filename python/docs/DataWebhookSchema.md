# DataWebhookSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuous** | **object** | Whether or not to allow Endgrate to continuously trigger transfers on your behalf, polling for new data every 15 minutes. | [optional] 
**endpoint** | **object** |  | 
**metadata** | **object** | Any information to be passed back in the webhook call. | [optional] 

## Example

```python
from endgrate.models.data_webhook_schema import DataWebhookSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DataWebhookSchema from a JSON string
data_webhook_schema_instance = DataWebhookSchema.from_json(json)
# print the JSON string representation of the object
print DataWebhookSchema.to_json()

# convert the object into a dict
data_webhook_schema_dict = data_webhook_schema_instance.to_dict()
# create an instance of DataWebhookSchema from a dict
data_webhook_schema_form_dict = data_webhook_schema.from_dict(data_webhook_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


