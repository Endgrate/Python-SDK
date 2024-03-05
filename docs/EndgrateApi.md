# openapi_client.EndgrateApi

All URIs are relative to *https://endgrate.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_errors**](EndgrateApi.md#get_api_errors) | **GET** /api/errors | Get Error Logs
[**get_api_integrations**](EndgrateApi.md#get_api_integrations) | **GET** /api/integrations | Get Integrations
[**get_api_pull_data**](EndgrateApi.md#get_api_pull_data) | **GET** /api/pull/data | Get Pull Data
[**get_api_session_configuration**](EndgrateApi.md#get_api_session_configuration) | **GET** /api/session/configuration | Get Session Configuration
[**get_api_session_delete**](EndgrateApi.md#get_api_session_delete) | **POST** /api/session/delete | Delete Session
[**get_api_statistics**](EndgrateApi.md#get_api_statistics) | **GET** /api/statistics | Get Statistics
[**get_session**](EndgrateApi.md#get_session) | **GET** /session | Session Redirect
[**get_session_edit**](EndgrateApi.md#get_session_edit) | **GET** /session/edit | Edit Session Redirect
[**get_session_reauthenticate**](EndgrateApi.md#get_session_reauthenticate) | **GET** /session/reauthenticate | Reauthenticate Session Redirect
[**post_api_pull_initiate**](EndgrateApi.md#post_api_pull_initiate) | **POST** /api/pull/initiate | Initiate Pull Session
[**post_api_pull_transfer**](EndgrateApi.md#post_api_pull_transfer) | **POST** /api/pull/transfer | Trigger Pull
[**post_api_push_initiate**](EndgrateApi.md#post_api_push_initiate) | **POST** /api/push/initiate | Initiate Push Session
[**post_api_push_transfer**](EndgrateApi.md#post_api_push_transfer) | **POST** /api/push/transfer | Trigger Push
[**post_api_schemas**](EndgrateApi.md#post_api_schemas) | **POST** /api/schemas | Set Schemas
[**post_api_session_initiate**](EndgrateApi.md#post_api_session_initiate) | **POST** /api/session/initiate | Initiate (Push + Pull) Session


# **get_api_errors**
> GetApiErrors200Response get_api_errors(limit=limit, offset=offset, session_id=session_id, transfer_id=transfer_id)

Get Error Logs

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_api_errors200_response import GetApiErrors200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://endgrate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://endgrate.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndgrateApi(api_client)
    limit = 250 # int |  (optional)
    offset = 500 # int |  (optional)
    session_id = '6566e85e7cf20dca9cef0c0a' # str |  (optional)
    transfer_id = '6566e87b7cf20dca9cef0c0d' # str |  (optional)

    try:
        # Get Error Logs
        api_response = api_instance.get_api_errors(limit=limit, offset=offset, session_id=session_id, transfer_id=transfer_id)
        print("The response of EndgrateApi->get_api_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndgrateApi->get_api_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **session_id** | **str**|  | [optional] 
 **transfer_id** | **str**|  | [optional] 

### Return type

[**GetApiErrors200Response**](GetApiErrors200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_integrations**
> GetApiIntegrations200Response get_api_integrations(provider=provider, category=category, session_id=session_id)

Get Integrations

### Example


```python
import openapi_client
from openapi_client.models.get_api_integrations200_response import GetApiIntegrations200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://endgrate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://endgrate.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndgrateApi(api_client)
    provider = 'hubspot' # str |  (optional)
    category = 'CRM' # str |  (optional)
    session_id = '6566e85e7cf20dca9cef0c0a' # str |  (optional)

    try:
        # Get Integrations
        api_response = api_instance.get_api_integrations(provider=provider, category=category, session_id=session_id)
        print("The response of EndgrateApi->get_api_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndgrateApi->get_api_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | [optional] 
 **category** | **str**|  | [optional] 
 **session_id** | **str**|  | [optional] 

### Return type

[**GetApiIntegrations200Response**](GetApiIntegrations200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_pull_data**
> GetApiPullData200Response get_api_pull_data(endgrate_type, transfer_id, limit=limit, offset=offset)

Get Pull Data

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.get_api_pull_data200_response import GetApiPullData200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://endgrate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://endgrate.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndgrateApi(api_client)
    endgrate_type = 'endgrate_type_example' # str | A valid `endgrate_type` for the session. If no `endgrate_type` was specified, the title of the schema can be used instead.
    transfer_id = '6566e89b7cf20dca9cef0c10' # str | 
    limit = 250 # int |  (optional)
    offset = 500 # int |  (optional)

    try:
        # Get Pull Data
        api_response = api_instance.get_api_pull_data(endgrate_type, transfer_id, limit=limit, offset=offset)
        print("The response of EndgrateApi->get_api_pull_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndgrateApi->get_api_pull_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endgrate_type** | **str**| A valid &#x60;endgrate_type&#x60; for the session. If no &#x60;endgrate_type&#x60; was specified, the title of the schema can be used instead. | 
 **transfer_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**GetApiPullData200Response**](GetApiPullData200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Transfer has not yet completed. |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_session_configuration**
> ConfigurationCallbackSchema get_api_session_configuration(session_id)

Get Session Configuration

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.configuration_callback_schema import ConfigurationCallbackSchema
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://endgrate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://endgrate.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndgrateApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Get Session Configuration
        api_response = api_instance.get_api_session_configuration(session_id)
        print("The response of EndgrateApi->get_api_session_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndgrateApi->get_api_session_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**ConfigurationCallbackSchema**](ConfigurationCallbackSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_session_delete**
> DefaultSuccessSchema get_api_session_delete(delete_schema)

Delete Session

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.default_success_schema import DefaultSuccessSchema
from openapi_client.models.delete_schema import DeleteSchema
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://endgrate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://endgrate.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndgrateApi(api_client)
    delete_schema = openapi_client.DeleteSchema() # DeleteSchema | 

    try:
        # Delete Session
        api_response = api_instance.get_api_session_delete(delete_schema)
        print("The response of EndgrateApi->get_api_session_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndgrateApi->get_api_session_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_schema** | [**DeleteSchema**](DeleteSchema.md)|  | 

### Return type

[**DefaultSuccessSchema**](DefaultSuccessSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_statistics**
> GetApiStatistics200Response get_api_statistics(method=method, session_id=session_id, transfer_id=transfer_id)

Get Statistics

### Example


```python
import openapi_client
from openapi_client.models.get_api_statistics200_response import GetApiStatistics200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://endgrate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://endgrate.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndgrateApi(api_client)
    method = 'method_example' # str |  (optional)
    session_id = 'session_id_example' # str |  (optional)
    transfer_id = 'transfer_id_example' # str |  (optional)

    try:
        # Get Statistics
        api_response = api_instance.get_api_statistics(method=method, session_id=session_id, transfer_id=transfer_id)
        print("The response of EndgrateApi->get_api_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndgrateApi->get_api_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method** | **str**|  | [optional] 
 **session_id** | **str**|  | [optional] 
 **transfer_id** | **str**|  | [optional] 

### Return type

[**GetApiStatistics200Response**](GetApiStatistics200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session**
> Error get_session(session_id, integration_provider_list_id=integration_provider_list_id)

Session Redirect

### Example


```python
import openapi_client
from openapi_client.models.error import Error
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://endgrate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://endgrate.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndgrateApi(api_client)
    session_id = 'session_id_example' # str | 
    integration_provider_list_id = 'integration_provider_list_id_example' # str |  (optional)

    try:
        # Session Redirect
        api_response = api_instance.get_session(session_id, integration_provider_list_id=integration_provider_list_id)
        print("The response of EndgrateApi->get_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndgrateApi->get_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **integration_provider_list_id** | **str**|  | [optional] 

### Return type

[**Error**](Error.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_edit**
> Error get_session_edit(session_id)

Edit Session Redirect

### Example


```python
import openapi_client
from openapi_client.models.error import Error
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://endgrate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://endgrate.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndgrateApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Edit Session Redirect
        api_response = api_instance.get_session_edit(session_id)
        print("The response of EndgrateApi->get_session_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndgrateApi->get_session_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**Error**](Error.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_reauthenticate**
> Error get_session_reauthenticate(session_id)

Reauthenticate Session Redirect

### Example


```python
import openapi_client
from openapi_client.models.error import Error
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://endgrate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://endgrate.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndgrateApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Reauthenticate Session Redirect
        api_response = api_instance.get_session_reauthenticate(session_id)
        print("The response of EndgrateApi->get_session_reauthenticate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndgrateApi->get_session_reauthenticate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**Error**](Error.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_pull_initiate**
> DefaultSuccessSchema post_api_pull_initiate(pull_initiate_schema)

Initiate Pull Session

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.default_success_schema import DefaultSuccessSchema
from openapi_client.models.pull_initiate_schema import PullInitiateSchema
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://endgrate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://endgrate.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndgrateApi(api_client)
    pull_initiate_schema = openapi_client.PullInitiateSchema() # PullInitiateSchema | 

    try:
        # Initiate Pull Session
        api_response = api_instance.post_api_pull_initiate(pull_initiate_schema)
        print("The response of EndgrateApi->post_api_pull_initiate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndgrateApi->post_api_pull_initiate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pull_initiate_schema** | [**PullInitiateSchema**](PullInitiateSchema.md)|  | 

### Return type

[**DefaultSuccessSchema**](DefaultSuccessSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_pull_transfer**
> TransferResponseSchema post_api_pull_transfer(pull_transfer_schema)

Trigger Pull

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.pull_transfer_schema import PullTransferSchema
from openapi_client.models.transfer_response_schema import TransferResponseSchema
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://endgrate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://endgrate.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndgrateApi(api_client)
    pull_transfer_schema = openapi_client.PullTransferSchema() # PullTransferSchema | 

    try:
        # Trigger Pull
        api_response = api_instance.post_api_pull_transfer(pull_transfer_schema)
        print("The response of EndgrateApi->post_api_pull_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndgrateApi->post_api_pull_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pull_transfer_schema** | [**PullTransferSchema**](PullTransferSchema.md)|  | 

### Return type

[**TransferResponseSchema**](TransferResponseSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_push_initiate**
> DefaultSuccessSchema post_api_push_initiate(push_initiate_schema)

Initiate Push Session

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.default_success_schema import DefaultSuccessSchema
from openapi_client.models.push_initiate_schema import PushInitiateSchema
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://endgrate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://endgrate.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndgrateApi(api_client)
    push_initiate_schema = openapi_client.PushInitiateSchema() # PushInitiateSchema | 

    try:
        # Initiate Push Session
        api_response = api_instance.post_api_push_initiate(push_initiate_schema)
        print("The response of EndgrateApi->post_api_push_initiate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndgrateApi->post_api_push_initiate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_initiate_schema** | [**PushInitiateSchema**](PushInitiateSchema.md)|  | 

### Return type

[**DefaultSuccessSchema**](DefaultSuccessSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_push_transfer**
> TransferResponseSchema post_api_push_transfer(push_transfer_schema)

Trigger Push

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.push_transfer_schema import PushTransferSchema
from openapi_client.models.transfer_response_schema import TransferResponseSchema
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://endgrate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://endgrate.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndgrateApi(api_client)
    push_transfer_schema = openapi_client.PushTransferSchema() # PushTransferSchema | 

    try:
        # Trigger Push
        api_response = api_instance.post_api_push_transfer(push_transfer_schema)
        print("The response of EndgrateApi->post_api_push_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndgrateApi->post_api_push_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_transfer_schema** | [**PushTransferSchema**](PushTransferSchema.md)|  | 

### Return type

[**TransferResponseSchema**](TransferResponseSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_schemas**
> DefaultSuccessSchema post_api_schemas(post_api_schemas_request=post_api_schemas_request)

Set Schemas

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.default_success_schema import DefaultSuccessSchema
from openapi_client.models.post_api_schemas_request import PostApiSchemasRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://endgrate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://endgrate.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndgrateApi(api_client)
    post_api_schemas_request = openapi_client.PostApiSchemasRequest() # PostApiSchemasRequest |  (optional)

    try:
        # Set Schemas
        api_response = api_instance.post_api_schemas(post_api_schemas_request=post_api_schemas_request)
        print("The response of EndgrateApi->post_api_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndgrateApi->post_api_schemas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_api_schemas_request** | [**PostApiSchemasRequest**](PostApiSchemasRequest.md)|  | [optional] 

### Return type

[**DefaultSuccessSchema**](DefaultSuccessSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_api_session_initiate**
> DefaultSuccessSchema post_api_session_initiate(session_initiate_schema)

Initiate (Push + Pull) Session

### Example

* Bearer Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.default_success_schema import DefaultSuccessSchema
from openapi_client.models.session_initiate_schema import SessionInitiateSchema
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://endgrate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://endgrate.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndgrateApi(api_client)
    session_initiate_schema = openapi_client.SessionInitiateSchema() # SessionInitiateSchema | 

    try:
        # Initiate (Push + Pull) Session
        api_response = api_instance.post_api_session_initiate(session_initiate_schema)
        print("The response of EndgrateApi->post_api_session_initiate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndgrateApi->post_api_session_initiate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_initiate_schema** | [**SessionInitiateSchema**](SessionInitiateSchema.md)|  | 

### Return type

[**DefaultSuccessSchema**](DefaultSuccessSchema.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

