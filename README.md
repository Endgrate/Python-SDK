# Endgrate
Endgrate API Reference

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Endgrate/SDK.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Endgrate/SDK.git`)

Then import the package:
```python
import endgrate
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import endgrate
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import endgrate
from endgrate.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://endgrate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = endgrate.Configuration(
    host = "https://endgrate.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = endgrate.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with endgrate.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = endgrate.EndgrateApi(api_client)
    limit = 250 # int |  (optional)
    offset = 500 # int |  (optional)
    session_id = '6566e85e7cf20dca9cef0c0a' # str |  (optional)
    transfer_id = '6566e87b7cf20dca9cef0c0d' # str |  (optional)

    try:
        # Get Error Logs
        api_response = api_instance.get_api_errors(limit=limit, offset=offset, session_id=session_id, transfer_id=transfer_id)
        print("The response of EndgrateApi->get_api_errors:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EndgrateApi->get_api_errors: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://endgrate.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EndgrateApi* | [**get_api_errors**](docs/EndgrateApi.md#get_api_errors) | **GET** /api/errors | Get Error Logs
*EndgrateApi* | [**get_api_integrations**](docs/EndgrateApi.md#get_api_integrations) | **GET** /api/integrations | Get Integrations
*EndgrateApi* | [**get_api_pull_data**](docs/EndgrateApi.md#get_api_pull_data) | **GET** /api/pull/data | Get Pull Data
*EndgrateApi* | [**get_api_session_configuration**](docs/EndgrateApi.md#get_api_session_configuration) | **GET** /api/session/configuration | Get Session Configuration
*EndgrateApi* | [**get_api_session_delete**](docs/EndgrateApi.md#get_api_session_delete) | **POST** /api/session/delete | Delete Session
*EndgrateApi* | [**get_api_statistics**](docs/EndgrateApi.md#get_api_statistics) | **GET** /api/statistics | Get Statistics
*EndgrateApi* | [**get_session**](docs/EndgrateApi.md#get_session) | **GET** /session | Session Redirect
*EndgrateApi* | [**get_session_edit**](docs/EndgrateApi.md#get_session_edit) | **GET** /session/edit | Edit Session Redirect
*EndgrateApi* | [**get_session_reauthenticate**](docs/EndgrateApi.md#get_session_reauthenticate) | **GET** /session/reauthenticate | Reauthenticate Session Redirect
*EndgrateApi* | [**post_api_pull_initiate**](docs/EndgrateApi.md#post_api_pull_initiate) | **POST** /api/pull/initiate | Initiate Pull Session
*EndgrateApi* | [**post_api_pull_transfer**](docs/EndgrateApi.md#post_api_pull_transfer) | **POST** /api/pull/transfer | Trigger Pull
*EndgrateApi* | [**post_api_push_initiate**](docs/EndgrateApi.md#post_api_push_initiate) | **POST** /api/push/initiate | Initiate Push Session
*EndgrateApi* | [**post_api_push_transfer**](docs/EndgrateApi.md#post_api_push_transfer) | **POST** /api/push/transfer | Trigger Push
*EndgrateApi* | [**post_api_schemas**](docs/EndgrateApi.md#post_api_schemas) | **POST** /api/schemas | Set Schemas
*EndgrateApi* | [**post_api_session_initiate**](docs/EndgrateApi.md#post_api_session_initiate) | **POST** /api/session/initiate | Initiate (Push + Pull) Session


## Documentation For Models

 - [ApiPullInitiatePostRequest](docs/ApiPullInitiatePostRequest.md)
 - [ApiPullInitiatePostRequest1](docs/ApiPullInitiatePostRequest1.md)
 - [CompletedCallbackSchema](docs/CompletedCallbackSchema.md)
 - [CompletedCallbackSchemaEndgrate](docs/CompletedCallbackSchemaEndgrate.md)
 - [ConfigurationCallbackSchema](docs/ConfigurationCallbackSchema.md)
 - [ConfigurationCallbackSchemaEndgrate](docs/ConfigurationCallbackSchemaEndgrate.md)
 - [ConfigurationCallbackSchemaEndgrateProviderInfo](docs/ConfigurationCallbackSchemaEndgrateProviderInfo.md)
 - [ConfigurationCallbackSchemaPassthroughSchemasValue](docs/ConfigurationCallbackSchemaPassthroughSchemasValue.md)
 - [ConfigurationCallbackSchemaPassthroughSchemasValueIntegrationInfo](docs/ConfigurationCallbackSchemaPassthroughSchemasValueIntegrationInfo.md)
 - [ConfigurationCallbackSchemaPassthroughSchemasValuePassthroughFields](docs/ConfigurationCallbackSchemaPassthroughSchemasValuePassthroughFields.md)
 - [ConfigurationCallbackSchemaPassthroughSchemasValueSchema](docs/ConfigurationCallbackSchemaPassthroughSchemasValueSchema.md)
 - [ConfigurationCallbackSchemaSchemasValue](docs/ConfigurationCallbackSchemaSchemasValue.md)
 - [ConfigurationCallbackSchemaSchemasValueIntegrationInfo](docs/ConfigurationCallbackSchemaSchemasValueIntegrationInfo.md)
 - [ConfigurationCallbackSchemaSchemasValuePassthroughFields](docs/ConfigurationCallbackSchemaSchemasValuePassthroughFields.md)
 - [ConfigurationCallbackSchemaSchemasValuePassthroughFieldsPropertiesValue](docs/ConfigurationCallbackSchemaSchemasValuePassthroughFieldsPropertiesValue.md)
 - [ConfigurationCallbackSchemaSchemasValueSchema](docs/ConfigurationCallbackSchemaSchemasValueSchema.md)
 - [ConfigurationCallbackSchemaSchemasValueSchemaPropertiesValue](docs/ConfigurationCallbackSchemaSchemasValueSchemaPropertiesValue.md)
 - [DataCallbackSchema](docs/DataCallbackSchema.md)
 - [DataWebhookSchema](docs/DataWebhookSchema.md)
 - [DefaultSuccessSchema](docs/DefaultSuccessSchema.md)
 - [DeleteSchema](docs/DeleteSchema.md)
 - [EndgrateJsonSchema](docs/EndgrateJsonSchema.md)
 - [Error](docs/Error.md)
 - [ErrorCallbackSchema](docs/ErrorCallbackSchema.md)
 - [ErrorListSchema](docs/ErrorListSchema.md)
 - [ErrorListSchemaEndgrate](docs/ErrorListSchemaEndgrate.md)
 - [ErrorListSchemaEndgrateIntegrationInfo](docs/ErrorListSchemaEndgrateIntegrationInfo.md)
 - [GetApiErrors200Response](docs/GetApiErrors200Response.md)
 - [GetApiErrors200ResponseMeta](docs/GetApiErrors200ResponseMeta.md)
 - [GetApiErrors200ResponseMetaPrevious](docs/GetApiErrors200ResponseMetaPrevious.md)
 - [GetApiIntegrations200Response](docs/GetApiIntegrations200Response.md)
 - [GetApiIntegrations200ResponseProvidersInner](docs/GetApiIntegrations200ResponseProvidersInner.md)
 - [GetApiIntegrations200ResponseProvidersInnerIntegrationsInner](docs/GetApiIntegrations200ResponseProvidersInnerIntegrationsInner.md)
 - [GetApiIntegrations200ResponseProvidersInnerProvider](docs/GetApiIntegrations200ResponseProvidersInnerProvider.md)
 - [GetApiPullData200Response](docs/GetApiPullData200Response.md)
 - [GetApiPullData200ResponseMeta](docs/GetApiPullData200ResponseMeta.md)
 - [GetApiPullData200ResponseMetaPrevious](docs/GetApiPullData200ResponseMetaPrevious.md)
 - [GetApiStatistics200Response](docs/GetApiStatistics200Response.md)
 - [GetApiStatistics200ResponseStatisticsValue](docs/GetApiStatistics200ResponseStatisticsValue.md)
 - [PostApiSchemasRequest](docs/PostApiSchemasRequest.md)
 - [PostApiSchemasRequestDataInner](docs/PostApiSchemasRequestDataInner.md)
 - [PullInitiateSchema](docs/PullInitiateSchema.md)
 - [PullTransferSchema](docs/PullTransferSchema.md)
 - [PushInitiateSchema](docs/PushInitiateSchema.md)
 - [PushTransferSchema](docs/PushTransferSchema.md)
 - [SessionInitiateSchema](docs/SessionInitiateSchema.md)
 - [TransferDataSchemaInner](docs/TransferDataSchemaInner.md)
 - [TransferResponseSchema](docs/TransferResponseSchema.md)
 - [WebhookSchema](docs/WebhookSchema.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
### BearerAuth

- **Type**: Bearer authentication


## Author

team@endgrate.com


