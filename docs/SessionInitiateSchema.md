# SessionInitiateSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_webhook** | [**WebhookSchema**](WebhookSchema.md) | Endgrate will POST to this webhook whenever a transfer is completed. | [optional] 
**configuration_webhook** | [**WebhookSchema**](WebhookSchema.md) | Endgrate will POST to this webhook when the session is configured by the user. | [optional] 
**data_webhook** | [**DataWebhookSchema**](DataWebhookSchema.md) | Endgrate will POST to this webhook whenever new data is received. | [optional] 
**error_webhook** | [**WebhookSchema**](WebhookSchema.md) | Endgrate will POST to this webhook whenever an error occurs. | [optional] 
**field_selection** | **bool** | Whether or not to allow the user to configure field mapping. | [optional] 
**passthrough_fields** | **bool** | Whether or not passthrough fields are allowed. | [optional] 
**passthrough_schemas** | **bool** | Whether or not passthrough schemas are allowed. | [optional] 
**sync** | **bool** | Whether or not to return only updated (new) data when pulling data. | [optional] 
**prepopulate** | **object** |  | [optional] 
**provider** | **str** | A pre-selected integration provider. If specified, the user will be directly redirected to the specific authentication page. | [optional] 
**redirect_url** | **str** | A URL that users will be redirected to after setting up the session.. | [optional] 
**resource_selection** | **bool** | Whether or not to allow the user to choose the integrations for a given schema (e.g. choosing \&quot;Get Contacts\&quot; for a contact schema). | [optional] 
**save_session** | **bool** | Whether or not the session should be persisted permanently. If false, sessions will expire after 72 hours. | [optional] 
**var_schema** | [**List[EndgrateJsonSchema]**](EndgrateJsonSchema.md) | An array of schemas. | [optional] 
**schema_selection** | **bool** | Whether or not to allow the user to choose which schemas to pull in. | [optional] 
**statistics** | **bool** | Whether or not to allow the user to see transfer statistics. | [optional] 
**webhook_concurrency** | **bool** | Whether or not to execute POST requests to webhooks concurrently. | [optional] 
**bypass_ui** | **bool** | Whether or not the Endgrate UI should be bypassed (Beta). | [optional] 

## Example

```python
from openapi_client.models.session_initiate_schema import SessionInitiateSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SessionInitiateSchema from a JSON string
session_initiate_schema_instance = SessionInitiateSchema.from_json(json)
# print the JSON string representation of the object
print SessionInitiateSchema.to_json()

# convert the object into a dict
session_initiate_schema_dict = session_initiate_schema_instance.to_dict()
# create an instance of SessionInitiateSchema from a dict
session_initiate_schema_form_dict = session_initiate_schema.from_dict(session_initiate_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


