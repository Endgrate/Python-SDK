# PushInitiateSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_webhook** | [**WebhookSchema**](WebhookSchema.md) | Endgrate will POST to this webhook whenever a transfer is completed. | [optional] 
**configuration_webhook** | [**WebhookSchema**](WebhookSchema.md) | Endgrate will POST to this webhook when the session is configured by the user. | [optional] 
**error_webhook** | [**WebhookSchema**](WebhookSchema.md) | Endgrate will POST to this webhook whenever an error occurs. | [optional] 
**field_selection** | **bool** | Whether or not to allow the user to configure field mapping. | [optional] 
**prepopulate** | **object** |  | [optional] 
**provider** | **str** | A pre-selected integration provider. If specified, the user will be directly redirected to the specific authentication page. | [optional] 
**redirect_url** | **str** | A URL that users will be redirected to after setting up the session. | [optional] 
**resource_selection** | **bool** | Whether or not to allow the user to choose the integrations for a given schema (e.g. choosing \&quot;Get Contacts\&quot; for a contact schema). | [optional] 
**save_session** | **bool** | Whether or not the session should be persisted permanently. If false, sessions will expire after 72 hours. | [optional] 
**var_schema** | [**List[EndgrateJsonSchema]**](EndgrateJsonSchema.md) | An array of schemas to be pushed out. | [optional] 
**schema_selection** | **bool** | Whether or not to allow the user to choose which schemas to pull in. | [optional] 
**statistics** | **bool** | Whether or not to allow the user to see transfer statistics. | [optional] 
**webhook_concurrency** | **bool** | Whether or not to execute POST requests to webhooks concurrently. | [optional] 
**bypass_ui** | **bool** | Whether or not the Endgrate UI should be bypassed (Beta). | [optional] 

## Example

```python
from endgrate.models.push_initiate_schema import PushInitiateSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PushInitiateSchema from a JSON string
push_initiate_schema_instance = PushInitiateSchema.from_json(json)
# print the JSON string representation of the object
print PushInitiateSchema.to_json()

# convert the object into a dict
push_initiate_schema_dict = push_initiate_schema_instance.to_dict()
# create an instance of PushInitiateSchema from a dict
push_initiate_schema_form_dict = push_initiate_schema.from_dict(push_initiate_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


