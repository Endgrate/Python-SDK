# openapi_client.WebhooksApi

All URIs are relative to *https://endgrate.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**completed_webhook_post**](WebhooksApi.md#completed_webhook_post) | **POST** /completed_webhook | Completed Webhook
[**configuration_webhook_post**](WebhooksApi.md#configuration_webhook_post) | **POST** /configuration_webhook | Configuration Webhook
[**data_webhook_post**](WebhooksApi.md#data_webhook_post) | **POST** /data_webhook | Data Webhook
[**error_webhook_post**](WebhooksApi.md#error_webhook_post) | **POST** /error_webhook | Error Webhook


# **completed_webhook_post**
> completed_webhook_post(completed_callback_schema)

Completed Webhook

Endgrate will POST to this webhook whenever a transfer is completed. This is useful if you want to display a completion message to your users.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.WebhooksApi(api_client)
    completed_callback_schema = openapi_client.CompletedCallbackSchema() # CompletedCallbackSchema | 

    try:
        # Completed Webhook
        api_instance.completed_webhook_post(completed_callback_schema)
    except Exception as e:
        print("Exception when calling WebhooksApi->completed_webhook_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **completed_callback_schema** | [**CompletedCallbackSchema**](CompletedCallbackSchema.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Acknowledgement that the completion data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_webhook_post**
> configuration_webhook_post(configuration_callback_schema)

Configuration Webhook

Endgrate will POST to this webhook when the session is configured by the user. This is useful if you want to get the integration provider chosen, any passthrough schemas, or passthrough fields without polling the GET api/session/configuration endpoint.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.WebhooksApi(api_client)
    configuration_callback_schema = openapi_client.ConfigurationCallbackSchema() # ConfigurationCallbackSchema | 

    try:
        # Configuration Webhook
        api_instance.configuration_webhook_post(configuration_callback_schema)
    except Exception as e:
        print("Exception when calling WebhooksApi->configuration_webhook_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_callback_schema** | [**ConfigurationCallbackSchema**](ConfigurationCallbackSchema.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Acknowledgement that the configuration data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_webhook_post**
> data_webhook_post(data_callback_schema)

Data Webhook

Endgrate will POST to this webhook whenever new data is received. This is useful if you want to get transfer data without polling the GET api/pull/data endpoint.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.WebhooksApi(api_client)
    data_callback_schema = openapi_client.DataCallbackSchema() # DataCallbackSchema | 

    try:
        # Data Webhook
        api_instance.data_webhook_post(data_callback_schema)
    except Exception as e:
        print("Exception when calling WebhooksApi->data_webhook_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_callback_schema** | [**DataCallbackSchema**](DataCallbackSchema.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Acknowledgement that the data was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **error_webhook_post**
> error_webhook_post(error_callback_schema)

Error Webhook

Endgrate will POST to this webhook whenever an error occurs. This endpoint is useful if you want to get error information without polling the GET api/errors endpoint.

### Example


```python
import openapi_client
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
    api_instance = openapi_client.WebhooksApi(api_client)
    error_callback_schema = openapi_client.ErrorCallbackSchema() # ErrorCallbackSchema | 

    try:
        # Error Webhook
        api_instance.error_webhook_post(error_callback_schema)
    except Exception as e:
        print("Exception when calling WebhooksApi->error_webhook_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_callback_schema** | [**ErrorCallbackSchema**](ErrorCallbackSchema.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Acknowledgement that the error information was received successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

