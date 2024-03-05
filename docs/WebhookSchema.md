# WebhookSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** |  | 
**metadata** | **object** | Any information to be passed back in the webhook call. | [optional] 

## Example

```python
from openapi_client.models.webhook_schema import WebhookSchema

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSchema from a JSON string
webhook_schema_instance = WebhookSchema.from_json(json)
# print the JSON string representation of the object
print WebhookSchema.to_json()

# convert the object into a dict
webhook_schema_dict = webhook_schema_instance.to_dict()
# create an instance of WebhookSchema from a dict
webhook_schema_form_dict = webhook_schema.from_dict(webhook_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


