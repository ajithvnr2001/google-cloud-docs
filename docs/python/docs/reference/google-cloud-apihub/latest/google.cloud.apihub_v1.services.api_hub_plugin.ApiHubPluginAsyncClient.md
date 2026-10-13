---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient
title: Class ApiHubPluginAsyncClient (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:22.267071+00:00
---

# Class ApiHubPluginAsyncClient (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ApiHubPluginAsyncClient (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    ApiHubPluginAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.api_hub_plugin.transports.base.ApiHubPluginTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.api_hub_plugin.transports.base.ApiHubPluginTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

This service is used for managing plugins inside the API Hub.

## Properties 

### api_endpoint

Return the API endpoint used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The API endpoint used by the client instance.  
  
### transport

Returns the transport used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`ApiHubPluginTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### ApiHubPluginAsyncClient
    
    
    ApiHubPluginAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.api_hub_plugin.transports.base.ApiHubPluginTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.api_hub_plugin.transports.base.ApiHubPluginTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the api hub plugin async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,ApiHubPluginTransport,Callable[..., ApiHubPluginTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the ApiHubPluginTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### attribute_path
    
    
    attribute_path(project: str, location: str, attribute: str) -> str

Returns a fully-qualified attribute string.

### cancel_operation
    
    
    cancel_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.CancelOperationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Starts asynchronous cancellation on a long-running operation.

The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.CancelOperationRequest``   
The request object. Request message for `CancelOperation` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

### common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

### common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

### common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

### common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

### create_plugin
    
    
    create_plugin(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.CreatePluginRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        plugin: typing.Optional[google.cloud.apihub_v1.types.plugin_service.Plugin] = None,
        plugin_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.plugin_service.Plugin

Create an API Hub plugin resource in the API hub. Once a plugin is created, it can be used to create plugin instances.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_create_plugin():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubPluginAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html)()
    
        # Initialize request argument(s)
        plugin = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[Plugin](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Plugin.html)()
        plugin.display_name = "display_name_value"
    
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[CreatePluginRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreatePluginRequest.html)(
            parent="parent_value",
            plugin=plugin,
        )
    
        # Make the request
        response = await client.[create_plugin](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_create_plugin)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.CreatePluginRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreatePluginRequest), dict]]`   
The request object. The CreatePlugin method's request.  
`parent` |  ``str``   
Required. The parent resource where this plugin will be created. Format: `projects/{project}/locations/{location}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`plugin` |  `[Plugin](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Plugin)`   
Required. The plugin to create. This corresponds to the `plugin` field on the `request` instance; if `request` is provided, this should not be set.  
`plugin_id` |  ``str``   
Optional. The ID to use for the Plugin resource, which will become the final component of the Plugin's resource name. This field is optional. - If provided, the same will be used. The service will throw an error if the specified id is already used by another Plugin resource in the API hub instance. - If not provided, a system generated id will be used. This value should be 4-63 characters, overall resource name which will be of format `projects/{project}/locations/{location}/plugins/{plugin}`, its length is limited to 1000 characters and valid characters are /`a-z][A-Z]`[0-9]-_/. This corresponds to the `plugin_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Plugin](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Plugin)` | A plugin resource in the API Hub.  
  
### create_plugin_instance
    
    
    create_plugin_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.CreatePluginInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        plugin_instance: typing.Optional[
            google.cloud.apihub_v1.types.plugin_service.PluginInstance
        ] = None,
        plugin_instance_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a Plugin instance in the API hub.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_create_plugin_instance():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubPluginAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html)()
    
        # Initialize request argument(s)
        plugin_instance = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[PluginInstance](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.PluginInstance.html)()
        plugin_instance.display_name = "display_name_value"
        plugin_instance.actions.action_id = "action_id_value"
    
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[CreatePluginInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreatePluginInstanceRequest.html)(
            parent="parent_value",
            plugin_instance=plugin_instance,
        )
    
        # Make the request
        operation = await client.[create_plugin_instance](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_create_plugin_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.CreatePluginInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreatePluginInstanceRequest), dict]]`   
The request object. The CreatePluginInstance method's request.  
`parent` |  ``str``   
Required. The parent of the plugin instance resource. Format: `projects/{project}/locations/{location}/plugins/{plugin}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`plugin_instance` |  `[PluginInstance](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.PluginInstance)`   
Required. The plugin instance to create. This corresponds to the `plugin_instance` field on the `request` instance; if `request` is provided, this should not be set.  
`plugin_instance_id` |  ``str``   
Optional. The ID to use for the plugin instance, which will become the final component of the plugin instance's resource name. This field is optional. - If provided, the same will be used. The service will throw an error if the specified id is already used by another plugin instance in the plugin resource. - If not provided, a system generated id will be used. This value should be 4-63 characters, and valid characters are /`a-z][A-Z]`[0-9]-_/. This corresponds to the `plugin_instance_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [PluginInstance](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.PluginInstance) Represents a plugin instance resource in the API Hub. A PluginInstance is a specific instance of a hub plugin with its own configuration, state, and execution details.  
  
### delete_operation
    
    
    delete_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.DeleteOperationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes a long-running operation.

This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.DeleteOperationRequest``   
The request object. Request message for `DeleteOperation` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_plugin
    
    
    delete_plugin(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.DeletePluginRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Delete a Plugin in API hub. Note, only user owned plugins can be deleted via this method.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_delete_plugin():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubPluginAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[DeletePluginRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeletePluginRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_plugin](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_delete_plugin)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.DeletePluginRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeletePluginRequest), dict]]`   
The request object. The `DeletePlugin][ApiHub.DeletePlugin]` method's request.  
`name` |  ``str``   
Required. The name of the Plugin resource to delete. Format: `projects/{project}/locations/{location}/plugins/{plugin}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### delete_plugin_instance
    
    
    delete_plugin_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.DeletePluginInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Deletes a plugin instance in the API hub.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_delete_plugin_instance():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubPluginAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[DeletePluginInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeletePluginInstanceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_plugin_instance](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_delete_plugin_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.DeletePluginInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeletePluginInstanceRequest), dict]]`   
The request object. The DeletePluginInstance method's request.  
`name` |  ``str``   
Required. The name of the plugin instance to delete. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### disable_plugin
    
    
    disable_plugin(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.DisablePluginRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.plugin_service.Plugin

Disables a plugin. The `state` of the plugin after disabling is `DISABLED`
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_disable_plugin():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubPluginAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[DisablePluginRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DisablePluginRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[disable_plugin](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_disable_plugin)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.DisablePluginRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DisablePluginRequest), dict]]`   
The request object. The DisablePlugin method's request.  
`name` |  ``str``   
Required. The name of the plugin to disable. Format: `projects/{project}/locations/{location}/plugins/{plugin}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Plugin](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Plugin)` | A plugin resource in the API Hub.  
  
### disable_plugin_instance_action
    
    
    disable_plugin_instance_action(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.DisablePluginInstanceActionRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        action_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Disables a plugin instance in the API hub.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_disable_plugin_instance_action():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubPluginAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[DisablePluginInstanceActionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DisablePluginInstanceActionRequest.html)(
            name="name_value",
            action_id="action_id_value",
        )
    
        # Make the request
        operation = await client.[disable_plugin_instance_action](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_disable_plugin_instance_action)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.DisablePluginInstanceActionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DisablePluginInstanceActionRequest), dict]]`   
The request object. The DisablePluginInstanceAction method's request.  
`name` |  ``str``   
Required. The name of the plugin instance to disable. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`action_id` |  ``str``   
Required. The action id to disable. This corresponds to the `action_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be DisablePluginInstanceActionResponse The DisablePluginInstanceAction method's response.  
  
### enable_plugin
    
    
    enable_plugin(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.EnablePluginRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.plugin_service.Plugin

Enables a plugin. The `state` of the plugin after enabling is `ENABLED`
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_enable_plugin():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubPluginAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[EnablePluginRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.EnablePluginRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[enable_plugin](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_enable_plugin)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.EnablePluginRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.EnablePluginRequest), dict]]`   
The request object. The EnablePlugin method's request.  
`name` |  ``str``   
Required. The name of the plugin to enable. Format: `projects/{project}/locations/{location}/plugins/{plugin}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Plugin](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Plugin)` | A plugin resource in the API Hub.  
  
### enable_plugin_instance_action
    
    
    enable_plugin_instance_action(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.EnablePluginInstanceActionRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        action_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Enables a plugin instance in the API hub.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_enable_plugin_instance_action():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubPluginAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[EnablePluginInstanceActionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.EnablePluginInstanceActionRequest.html)(
            name="name_value",
            action_id="action_id_value",
        )
    
        # Make the request
        operation = await client.[enable_plugin_instance_action](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_enable_plugin_instance_action)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.EnablePluginInstanceActionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.EnablePluginInstanceActionRequest), dict]]`   
The request object. The EnablePluginInstanceAction method's request.  
`name` |  ``str``   
Required. The name of the plugin instance to enable. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`action_id` |  ``str``   
Required. The action id to enable. This corresponds to the `action_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be EnablePluginInstanceActionResponse The EnablePluginInstanceAction method's response.  
  
### execute_plugin_instance_action
    
    
    execute_plugin_instance_action(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.ExecutePluginInstanceActionRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        action_execution_detail: typing.Optional[
            google.cloud.apihub_v1.types.plugin_service.ActionExecutionDetail
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Executes a plugin instance in the API hub.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_execute_plugin_instance_action():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubPluginAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html)()
    
        # Initialize request argument(s)
        action_execution_detail = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ActionExecutionDetail](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ActionExecutionDetail.html)()
        action_execution_detail.action_id = "action_id_value"
    
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ExecutePluginInstanceActionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ExecutePluginInstanceActionRequest.html)(
            name="name_value",
            action_execution_detail=action_execution_detail,
        )
    
        # Make the request
        operation = await client.[execute_plugin_instance_action](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_execute_plugin_instance_action)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.ExecutePluginInstanceActionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ExecutePluginInstanceActionRequest), dict]]`   
The request object. The ExecutePluginInstanceAction method's request.  
`name` |  ``str``   
Required. The name of the plugin instance to execute. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`action_execution_detail` |  `[ActionExecutionDetail](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ActionExecutionDetail)`   
Required. The execution details for the action to execute. This corresponds to the `action_execution_detail` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be ExecutePluginInstanceActionResponse The ExecutePluginInstanceAction method's response.  
  
### from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

**Parameter**  
---  
**Name** | **Description**  
`filename` |  `str`   
The path to the service account private key json file.  
**Returns**  
---  
**Type** | **Description**  
`ApiHubPluginAsyncClient` | The constructed client.  
  
### from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

**Parameter**  
---  
**Name** | **Description**  
`info` |  `dict`   
The service account private key info.  
**Returns**  
---  
**Type** | **Description**  
`ApiHubPluginAsyncClient` | The constructed client.  
  
### from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

**Parameter**  
---  
**Name** | **Description**  
`filename` |  `str`   
The path to the service account private key json file.  
**Returns**  
---  
**Type** | **Description**  
`ApiHubPluginAsyncClient` | The constructed client.  
  
### get_location
    
    
    get_location(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.GetLocationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.location.locations_pb2.Location

Gets information about a location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.GetLocationRequest``   
The request object. Request message for `GetLocation` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.location_pb2.Location`` | Location object.  
  
### get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

The client cert source is determined in the following order: (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the client cert source is None. (2) if `client_options.client_cert_source` is provided, use the provided one; if the default client cert source exists, use the default one; otherwise the client cert source is None.

The API endpoint is determined in the following order: (1) if `client_options.api_endpoint` if provided, use the provided one. (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the default mTLS endpoint; if the environment variable is "never", use the default API endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise use the default API endpoint.

More details can be found at <https://google.aip.dev/auth/4114>.

**Parameter**  
---  
**Name** | **Description**  
`client_options` |  `google.api_core.client_options.ClientOptions`   
Custom options for the client. Only the `api_endpoint` and `client_cert_source` properties may be used in this method.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTLSChannelError` | If any errors happen.  
**Returns**  
---  
**Type** | **Description**  
`Tuple[str, Callable[[], Tuple[bytes, bytes]]]` | returns the API endpoint and the client cert source to use.  
  
### get_operation
    
    
    get_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.GetOperationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.longrunning.operations_pb2.Operation

Gets the latest state of a long-running operation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.GetOperationRequest``   
The request object. Request message for `GetOperation` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.Operation`` | An `Operation` object.  
  
### get_plugin
    
    
    get_plugin(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.plugin_service.GetPluginRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.plugin_service.Plugin

Get an API Hub plugin.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_get_plugin():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubPluginAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[GetPluginRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetPluginRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_plugin](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_get_plugin)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.GetPluginRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetPluginRequest), dict]]`   
The request object. The GetPlugin method's request.  
`name` |  ``str``   
Required. The name of the plugin to retrieve. Format: `projects/{project}/locations/{location}/plugins/{plugin}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Plugin](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Plugin)` | A plugin resource in the API Hub.  
  
### get_plugin_instance
    
    
    get_plugin_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.GetPluginInstanceRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.plugin_service.PluginInstance

Get an API Hub plugin instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_get_plugin_instance():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubPluginAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[GetPluginInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetPluginInstanceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_plugin_instance](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_get_plugin_instance)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.GetPluginInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetPluginInstanceRequest), dict]]`   
The request object. The GetPluginInstance method's request.  
`name` |  ``str``   
Required. The name of the plugin instance to retrieve. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.PluginInstance](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.PluginInstance)` | Represents a plugin instance resource in the API Hub. A PluginInstance is a specific instance of a hub plugin with its own configuration, state, and execution details.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.apihub_v1.services.api_hub_plugin.transports.base.ApiHubPluginTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### list_locations
    
    
    list_locations(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.ListLocationsRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.location.locations_pb2.ListLocationsResponse

Lists information about the supported locations for this service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.ListLocationsRequest``   
The request object. Request message for `ListLocations` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.location_pb2.ListLocationsResponse`` | Response message for `ListLocations` method.  
  
### list_operations
    
    
    list_operations(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.ListOperationsRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.longrunning.operations_pb2.ListOperationsResponse

Lists operations that match the specified filter in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.ListOperationsRequest``   
The request object. Request message for `ListOperations` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.ListOperationsResponse`` | Response message for `ListOperations` method.  
  
### list_plugin_instances
    
    
    list_plugin_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.ListPluginInstancesRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginInstancesAsyncPager
    )

List all the plugins in a given project and location. `-` can be used as wildcard value for {plugin_id}
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_list_plugin_instances():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubPluginAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ListPluginInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListPluginInstancesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_plugin_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_list_plugin_instances)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.ListPluginInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListPluginInstancesRequest), dict]]`   
The request object. The ListPluginInstances method's request.  
`parent` |  ``str``   
Required. The parent resource where this plugin will be created. Format: `projects/{project}/locations/{location}/plugins/{plugin}`. To list plugin instances for multiple plugins, use the - character instead of the plugin ID. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginInstancesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginInstancesAsyncPager)` | The ListPluginInstances method's response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_plugins
    
    
    list_plugins(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.ListPluginsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginsAsyncPager

List all the plugins in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_list_plugins():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubPluginAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ListPluginsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListPluginsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_plugins](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_list_plugins)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.ListPluginsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListPluginsRequest), dict]]`   
The request object. The ListPlugins method's request.  
`parent` |  ``str``   
Required. The parent resource where this plugin will be created. Format: `projects/{project}/locations/{location}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginsAsyncPager)` | The ListPlugins method's response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### parse_attribute_path
    
    
    parse_attribute_path(path: str) -> typing.Dict[str, str]

Parses a attribute path into its component segments.

### parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

### parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

### parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

### parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

### parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

### parse_plugin_instance_path
    
    
    parse_plugin_instance_path(path: str) -> typing.Dict[str, str]

Parses a plugin_instance path into its component segments.

### parse_plugin_path
    
    
    parse_plugin_path(path: str) -> typing.Dict[str, str]

Parses a plugin path into its component segments.

### parse_service_account_path
    
    
    parse_service_account_path(path: str) -> typing.Dict[str, str]

Parses a service_account path into its component segments.

### plugin_instance_path
    
    
    plugin_instance_path(
        project: str, location: str, plugin: str, instance: str
    ) -> str

Returns a fully-qualified plugin_instance string.

### plugin_path
    
    
    plugin_path(project: str, location: str, plugin: str) -> str

Returns a fully-qualified plugin string.

### service_account_path
    
    
    service_account_path(project: str, service_account: str) -> str

Returns a fully-qualified service_account string.

### update_plugin_instance
    
    
    update_plugin_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.plugin_service.UpdatePluginInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        plugin_instance: typing.Optional[
            google.cloud.apihub_v1.types.plugin_service.PluginInstance
        ] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.plugin_service.PluginInstance

Updates a plugin instance in the API hub. The following fields in the xref_plugin_instance can be updated currently:

  * xref_display_name
  * `schedule_cron_expression][PluginInstance.actions.schedule_cron_expression]`



The xref_update_mask should be used to specify the fields being updated.

To update the xref_auth_config and xref_additional_config of the plugin instance, use the xref_ApplyPluginInstanceConfig method.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_update_plugin_instance():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubPluginAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html)()
    
        # Initialize request argument(s)
        plugin_instance = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[PluginInstance](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.PluginInstance.html)()
        plugin_instance.display_name = "display_name_value"
        plugin_instance.actions.action_id = "action_id_value"
    
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[UpdatePluginInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdatePluginInstanceRequest.html)(
            plugin_instance=plugin_instance,
        )
    
        # Make the request
        response = await client.[update_plugin_instance](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.ApiHubPluginAsyncClient.html#google_cloud_apihub_v1_services_api_hub_plugin_ApiHubPluginAsyncClient_update_plugin_instance)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.UpdatePluginInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdatePluginInstanceRequest), dict]]`   
The request object. The UpdatePluginInstance method's request.  
`plugin_instance` |  `[PluginInstance](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.PluginInstance)`   
Required. The plugin instance to update. This corresponds to the `plugin_instance` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. The list of fields to update. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.PluginInstance](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.PluginInstance)` | Represents a plugin instance resource in the API Hub. A PluginInstance is a specific instance of a hub plugin with its own configuration, state, and execution details.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
