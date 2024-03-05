# PullInitiateSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_webhook** | [**WebhookSchema**](WebhookSchema.md) | Endgrate will POST to this webhook whenever a transfer is completed. | [optional] 
**configuration_webhook** | [**WebhookSchema**](WebhookSchema.md) | Endgrate will POST to this webhook when the session is configured by the user. | [optional] 
**data_webhook** | [**DataWebhookSchema**](DataWebhookSchema.md) | Endgrate will POST to this webhook whenever new data is received. | [optional] 
**error_webhook** | [**WebhookSchema**](WebhookSchema.md) | Endgrate will POST to this webhook whenever an error occurs. | [optional] 
**field_selection** | **object** | Whether or not to allow the user to configure field mapping. | [optional] 
**passthrough_fields** | **object** | Whether or not passthrough fields are allowed. | [optional] 
**passthrough_schemas** | **object** | Whether or not passthrough schemas are allowed. | [optional] 
**sync** | **object** | Whether or not to return only updated (new) data when pulling data. | [optional] 
**prepopulate** | **object** |  | [optional] 
**provider** | **object** | A pre-selected integration provider. If specified, the user will be directly redirected to the specific authentication page. | [optional] 
**redirect_url** | **object** | A URL that users will be redirected to after setting up the session. | [optional] 
**resource_selection** | **object** | Whether or not to allow the user to choose the integrations for a given schema (e.g. choosing \&quot;Get Contacts\&quot; for a contact schema). | [optional] 
**save_session** | **object** | Whether or not the session should be persisted permanently. If false, sessions will expire after 72 hours. | [optional] 
**var_schema** | **object** | An array of schemas to be pulled in. | [optional] 
**schema_selection** | **object** | Whether or not to allow the user to choose which schemas to pull in. | [optional] 
**statistics** | **object** | Whether or not to allow the user to see transfer statistics. | [optional] 
**webhook_concurrency** | **object** | Whether or not to execute POST requests to webhooks concurrently. | [optional] 
**bypass_ui** | **object** | Whether or not the Endgrate UI should be bypassed (Beta). | [optional] 

## Example

```python
from openapi_client.models.pull_initiate_schema import PullInitiateSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PullInitiateSchema from a JSON string
pull_initiate_schema_instance = PullInitiateSchema.from_json(json)
# print the JSON string representation of the object
print PullInitiateSchema.to_json()

# convert the object into a dict
pull_initiate_schema_dict = pull_initiate_schema_instance.to_dict()
# create an instance of PullInitiateSchema from a dict
pull_initiate_schema_form_dict = pull_initiate_schema.from_dict(pull_initiate_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


