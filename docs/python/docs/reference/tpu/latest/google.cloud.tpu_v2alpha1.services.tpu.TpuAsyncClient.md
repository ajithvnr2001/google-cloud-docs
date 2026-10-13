---
url: https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient
title: Class TpuAsyncClient (1.28.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:12:26.041365+00:00
---

# Class TpuAsyncClient (1.28.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TpuAsyncClient (1.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.28.0 (latest)  1.27.0  1.26.0  1.25.0  1.24.0  1.23.2  1.22.0  1.21.0  1.20.0  1.19.1  1.18.5  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.2  1.10.1  1.9.0  1.8.0  1.7.2  1.6.0  1.5.2  1.4.1  1.3.4  1.2.1  1.1.0  1.0.2  0.2.2  0.1.0 
    
    
    TpuAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.tpu_v2alpha1.services.tpu.transports.base.TpuTransport,
                typing.Callable[
                    [...],
                    google.cloud.tpu_v2alpha1.services.tpu.transports.base.TpuTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Manages TPU nodes and other resources

TPU API v2alpha1

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
`TpuTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### TpuAsyncClient
    
    
    TpuAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.tpu_v2alpha1.services.tpu.transports.base.TpuTransport,
                typing.Callable[
                    [...],
                    google.cloud.tpu_v2alpha1.services.tpu.transports.base.TpuTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the tpu async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,TpuTransport,Callable[..., TpuTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the TpuTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### accelerator_type_path
    
    
    accelerator_type_path(project: str, location: str, accelerator_type: str) -> str

Returns a fully-qualified accelerator_type string.

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

### create_node
    
    
    create_node(
        request: typing.Optional[
            typing.Union[google.cloud.tpu_v2alpha1.types.cloud_tpu.CreateNodeRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        node: typing.Optional[google.cloud.tpu_v2alpha1.types.cloud_tpu.Node] = None,
        node_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a node.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_create_node():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        node = tpu_v2alpha1.[Node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.Node.html)()
        node.runtime_version = "runtime_version_value"
    
        request = tpu_v2alpha1.[CreateNodeRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.CreateNodeRequest.html)(
            parent="parent_value",
            node=node,
        )
    
        # Make the request
        operation = await client.[create_node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_create_node)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.CreateNodeRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.CreateNodeRequest), dict]]`   
The request object. Request for CreateNode.  
`parent` |  ``str``   
Required. The parent resource name. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`node` |  `[Node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.Node)`   
Required. The node. This corresponds to the `node` field on the `request` instance; if `request` is provided, this should not be set.  
`node_id` |  ``str``   
The unqualified resource name. This corresponds to the `node_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.Node) A TPU instance.  
  
### create_queued_resource
    
    
    create_queued_resource(
        request: typing.Optional[
            typing.Union[
                google.cloud.tpu_v2alpha1.types.cloud_tpu.CreateQueuedResourceRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        queued_resource: typing.Optional[
            google.cloud.tpu_v2alpha1.types.cloud_tpu.QueuedResource
        ] = None,
        queued_resource_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a QueuedResource TPU instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_create_queued_resource():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[CreateQueuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.CreateQueuedResourceRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        operation = await client.[create_queued_resource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_create_queued_resource)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.CreateQueuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.CreateQueuedResourceRequest), dict]]`   
The request object. Request for CreateQueuedResource.  
`parent` |  ``str``   
Required. The parent resource name. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`queued_resource` |  `[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource)`   
Required. The queued resource. This corresponds to the `queued_resource` field on the `request` instance; if `request` is provided, this should not be set.  
`queued_resource_id` |  ``str``   
The unqualified resource name. Should follow the `^[A-Za-z0-9_.`+%-]+$` regex format. This corresponds to the `queued_resource_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource) A QueuedResource represents a request for resources that will be placed in a queue and fulfilled when the necessary resources are available.  
  
### delete_node
    
    
    delete_node(
        request: typing.Optional[
            typing.Union[google.cloud.tpu_v2alpha1.types.cloud_tpu.DeleteNodeRequest, dict]
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

Deletes a node.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_delete_node():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[DeleteNodeRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.DeleteNodeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_delete_node)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.DeleteNodeRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.DeleteNodeRequest), dict]]`   
The request object. Request for DeleteNode.  
`name` |  ``str``   
Required. The resource name. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_queued_resource
    
    
    delete_queued_resource(
        request: typing.Optional[
            typing.Union[
                google.cloud.tpu_v2alpha1.types.cloud_tpu.DeleteQueuedResourceRequest, dict
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

Deletes a QueuedResource TPU instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_delete_queued_resource():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[DeleteQueuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.DeleteQueuedResourceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_queued_resource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_delete_queued_resource)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.DeleteQueuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.DeleteQueuedResourceRequest), dict]]`   
The request object. Request for DeleteQueuedResource.  
`name` |  ``str``   
Required. The resource name. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource) A QueuedResource represents a request for resources that will be placed in a queue and fulfilled when the necessary resources are available.  
  
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
`TpuAsyncClient` | The constructed client.  
  
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
`TpuAsyncClient` | The constructed client.  
  
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
`TpuAsyncClient` | The constructed client.  
  
### generate_service_identity
    
    
    generate_service_identity(
        request: typing.Optional[
            typing.Union[
                google.cloud.tpu_v2alpha1.types.cloud_tpu.GenerateServiceIdentityRequest,
                dict,
            ]
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
    ) -> google.cloud.tpu_v2alpha1.types.cloud_tpu.GenerateServiceIdentityResponse

Generates the Cloud TPU service identity for the project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_generate_service_identity():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[GenerateServiceIdentityRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.GenerateServiceIdentityRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[generate_service_identity](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_generate_service_identity)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.GenerateServiceIdentityRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.GenerateServiceIdentityRequest), dict]]`   
The request object. Request for GenerateServiceIdentity.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tpu_v2alpha1.types.GenerateServiceIdentityResponse](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.GenerateServiceIdentityResponse)` | Response for GenerateServiceIdentity.  
  
### get_accelerator_type
    
    
    get_accelerator_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.tpu_v2alpha1.types.cloud_tpu.GetAcceleratorTypeRequest, dict
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
    ) -> google.cloud.tpu_v2alpha1.types.cloud_tpu.AcceleratorType

Gets AcceleratorType.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_get_accelerator_type():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[GetAcceleratorTypeRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.GetAcceleratorTypeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_accelerator_type](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_get_accelerator_type)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.GetAcceleratorTypeRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.GetAcceleratorTypeRequest), dict]]`   
The request object. Request for GetAcceleratorType.  
`name` |  ``str``   
Required. The resource name. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tpu_v2alpha1.types.AcceleratorType](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.AcceleratorType)` | A accelerator type that a Node can be configured with.  
  
### get_guest_attributes
    
    
    get_guest_attributes(
        request: typing.Optional[
            typing.Union[
                google.cloud.tpu_v2alpha1.types.cloud_tpu.GetGuestAttributesRequest, dict
            ]
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
    ) -> google.cloud.tpu_v2alpha1.types.cloud_tpu.GetGuestAttributesResponse

Retrieves the guest attributes for the node.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_get_guest_attributes():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[GetGuestAttributesRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.GetGuestAttributesRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_guest_attributes](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_get_guest_attributes)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.GetGuestAttributesRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.GetGuestAttributesRequest), dict]]`   
The request object. Request for GetGuestAttributes.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tpu_v2alpha1.types.GetGuestAttributesResponse](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.GetGuestAttributesResponse)` | Response for GetGuestAttributes.  
  
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
  
### get_node
    
    
    get_node(
        request: typing.Optional[
            typing.Union[google.cloud.tpu_v2alpha1.types.cloud_tpu.GetNodeRequest, dict]
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
    ) -> google.cloud.tpu_v2alpha1.types.cloud_tpu.Node

Gets the details of a node.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_get_node():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[GetNodeRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.GetNodeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_get_node)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.GetNodeRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.GetNodeRequest), dict]]`   
The request object. Request for GetNode.  
`name` |  ``str``   
Required. The resource name. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tpu_v2alpha1.types.Node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.Node)` | A TPU instance.  
  
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
  
### get_queued_resource
    
    
    get_queued_resource(
        request: typing.Optional[
            typing.Union[
                google.cloud.tpu_v2alpha1.types.cloud_tpu.GetQueuedResourceRequest, dict
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
    ) -> google.cloud.tpu_v2alpha1.types.cloud_tpu.QueuedResource

Gets details of a queued resource.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_get_queued_resource():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[GetQueuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.GetQueuedResourceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_queued_resource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_get_queued_resource)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.GetQueuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.GetQueuedResourceRequest), dict]]`   
The request object. Request for GetQueuedResource  
`name` |  ``str``   
Required. The resource name. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tpu_v2alpha1.types.QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource)` | A QueuedResource represents a request for resources that will be placed in a queue and fulfilled when the necessary resources are available.  
  
### get_runtime_version
    
    
    get_runtime_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.tpu_v2alpha1.types.cloud_tpu.GetRuntimeVersionRequest, dict
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
    ) -> google.cloud.tpu_v2alpha1.types.cloud_tpu.RuntimeVersion

Gets a runtime version.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_get_runtime_version():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[GetRuntimeVersionRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.GetRuntimeVersionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_runtime_version](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_get_runtime_version)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.GetRuntimeVersionRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.GetRuntimeVersionRequest), dict]]`   
The request object. Request for GetRuntimeVersion.  
`name` |  ``str``   
Required. The resource name. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tpu_v2alpha1.types.RuntimeVersion](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.RuntimeVersion)` | A runtime version that a Node can be configured with.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[google.cloud.tpu_v2alpha1.services.tpu.transports.base.TpuTransport]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### list_accelerator_types
    
    
    list_accelerator_types(
        request: typing.Optional[
            typing.Union[
                google.cloud.tpu_v2alpha1.types.cloud_tpu.ListAcceleratorTypesRequest, dict
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
    ) -> google.cloud.tpu_v2alpha1.services.tpu.pagers.ListAcceleratorTypesAsyncPager

Lists accelerator types supported by this API.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_list_accelerator_types():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[ListAcceleratorTypesRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.ListAcceleratorTypesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_accelerator_types](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_list_accelerator_types)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.ListAcceleratorTypesRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.ListAcceleratorTypesRequest), dict]]`   
The request object. Request for ListAcceleratorTypes.  
`parent` |  ``str``   
Required. The parent resource name. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tpu_v2alpha1.services.tpu.pagers.ListAcceleratorTypesAsyncPager](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.pagers.ListAcceleratorTypesAsyncPager)` | Response for ListAcceleratorTypes. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### list_nodes
    
    
    list_nodes(
        request: typing.Optional[
            typing.Union[google.cloud.tpu_v2alpha1.types.cloud_tpu.ListNodesRequest, dict]
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
    ) -> google.cloud.tpu_v2alpha1.services.tpu.pagers.ListNodesAsyncPager

Lists nodes.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_list_nodes():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[ListNodesRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.ListNodesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_nodes](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_list_nodes)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.ListNodesRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.ListNodesRequest), dict]]`   
The request object. Request for ListNodes.  
`parent` |  ``str``   
Required. The parent resource name. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tpu_v2alpha1.services.tpu.pagers.ListNodesAsyncPager](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.pagers.ListNodesAsyncPager)` | Response for ListNodes. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### list_queued_resources
    
    
    list_queued_resources(
        request: typing.Optional[
            typing.Union[
                google.cloud.tpu_v2alpha1.types.cloud_tpu.ListQueuedResourcesRequest, dict
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
    ) -> google.cloud.tpu_v2alpha1.services.tpu.pagers.ListQueuedResourcesAsyncPager

Lists queued resources.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_list_queued_resources():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[ListQueuedResourcesRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.ListQueuedResourcesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_queued_resources](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_list_queued_resources)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.ListQueuedResourcesRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.ListQueuedResourcesRequest), dict]]`   
The request object. Request for ListQueuedResources.  
`parent` |  ``str``   
Required. The parent resource name. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tpu_v2alpha1.services.tpu.pagers.ListQueuedResourcesAsyncPager](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.pagers.ListQueuedResourcesAsyncPager)` | Response for ListQueuedResources. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_reservations
    
    
    list_reservations(
        request: typing.Optional[
            typing.Union[
                google.cloud.tpu_v2alpha1.types.cloud_tpu.ListReservationsRequest, dict
            ]
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
    ) -> google.cloud.tpu_v2alpha1.services.tpu.pagers.ListReservationsAsyncPager

Retrieves the reservations for the given project in the given location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_list_reservations():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[ListReservationsRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.ListReservationsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_reservations](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_list_reservations)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.ListReservationsRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.ListReservationsRequest), dict]]`   
The request object. Request for ListReservations.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tpu_v2alpha1.services.tpu.pagers.ListReservationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.pagers.ListReservationsAsyncPager)` | Response for ListReservations. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_runtime_versions
    
    
    list_runtime_versions(
        request: typing.Optional[
            typing.Union[
                google.cloud.tpu_v2alpha1.types.cloud_tpu.ListRuntimeVersionsRequest, dict
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
    ) -> google.cloud.tpu_v2alpha1.services.tpu.pagers.ListRuntimeVersionsAsyncPager

Lists runtime versions supported by this API.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_list_runtime_versions():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[ListRuntimeVersionsRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.ListRuntimeVersionsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_runtime_versions](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_list_runtime_versions)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.ListRuntimeVersionsRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.ListRuntimeVersionsRequest), dict]]`   
The request object. Request for ListRuntimeVersions.  
`parent` |  ``str``   
Required. The parent resource name. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tpu_v2alpha1.services.tpu.pagers.ListRuntimeVersionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.pagers.ListRuntimeVersionsAsyncPager)` | Response for ListRuntimeVersions. Iterating over this object will yield results and resolve additional pages automatically.  
  
### node_path
    
    
    node_path(project: str, location: str, node: str) -> str

Returns a fully-qualified node string.

### parse_accelerator_type_path
    
    
    parse_accelerator_type_path(path: str) -> typing.Dict[str, str]

Parses a accelerator_type path into its component segments.

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

### parse_node_path
    
    
    parse_node_path(path: str) -> typing.Dict[str, str]

Parses a node path into its component segments.

### parse_queued_resource_path
    
    
    parse_queued_resource_path(path: str) -> typing.Dict[str, str]

Parses a queued_resource path into its component segments.

### parse_reservation_path
    
    
    parse_reservation_path(path: str) -> typing.Dict[str, str]

Parses a reservation path into its component segments.

### parse_runtime_version_path
    
    
    parse_runtime_version_path(path: str) -> typing.Dict[str, str]

Parses a runtime_version path into its component segments.

### perform_maintenance
    
    
    perform_maintenance(
        request: typing.Optional[
            typing.Union[
                google.cloud.tpu_v2alpha1.types.cloud_tpu.PerformMaintenanceRequest, dict
            ]
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
    ) -> google.api_core.operation_async.AsyncOperation

Perform manual maintenance on a node.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_perform_maintenance():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[PerformMaintenanceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.PerformMaintenanceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[perform_maintenance](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_perform_maintenance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.PerformMaintenanceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.PerformMaintenanceRequest), dict]]`   
The request object. Request for PerformMaintenance.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.Node) A TPU instance.  
  
### perform_maintenance_queued_resource
    
    
    perform_maintenance_queued_resource(
        request: typing.Optional[
            typing.Union[
                google.cloud.tpu_v2alpha1.types.cloud_tpu.PerformMaintenanceQueuedResourceRequest,
                dict,
            ]
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
    ) -> google.api_core.operation_async.AsyncOperation

Perform manual maintenance on specific nodes of a QueuedResource.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_perform_maintenance_queued_resource():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[PerformMaintenanceQueuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.PerformMaintenanceQueuedResourceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[perform_maintenance_queued_resource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_perform_maintenance_queued_resource)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.PerformMaintenanceQueuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.PerformMaintenanceQueuedResourceRequest), dict]]`   
The request object. Request for PerformMaintenanceQueuedResource.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource) A QueuedResource represents a request for resources that will be placed in a queue and fulfilled when the necessary resources are available.  
  
### queued_resource_path
    
    
    queued_resource_path(project: str, location: str, queued_resource: str) -> str

Returns a fully-qualified queued_resource string.

### reservation_path
    
    
    reservation_path(project: str, location: str, reservation: str) -> str

Returns a fully-qualified reservation string.

### reset_queued_resource
    
    
    reset_queued_resource(
        request: typing.Optional[
            typing.Union[
                google.cloud.tpu_v2alpha1.types.cloud_tpu.ResetQueuedResourceRequest, dict
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

Resets a QueuedResource TPU instance
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_reset_queued_resource():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[ResetQueuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.ResetQueuedResourceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[reset_queued_resource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_reset_queued_resource)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.ResetQueuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.ResetQueuedResourceRequest), dict]]`   
The request object. Request for ResetQueuedResource.  
`name` |  ``str``   
Required. The name of the queued resource. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource) A QueuedResource represents a request for resources that will be placed in a queue and fulfilled when the necessary resources are available.  
  
### runtime_version_path
    
    
    runtime_version_path(project: str, location: str, runtime_version: str) -> str

Returns a fully-qualified runtime_version string.

### simulate_maintenance_event
    
    
    simulate_maintenance_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.tpu_v2alpha1.types.cloud_tpu.SimulateMaintenanceEventRequest,
                dict,
            ]
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
    ) -> google.api_core.operation_async.AsyncOperation

Simulates a maintenance event.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_simulate_maintenance_event():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[SimulateMaintenanceEventRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.SimulateMaintenanceEventRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[simulate_maintenance_event](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_simulate_maintenance_event)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.SimulateMaintenanceEventRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.SimulateMaintenanceEventRequest), dict]]`   
The request object. Request for SimulateMaintenanceEvent.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.Node) A TPU instance.  
  
### start_node
    
    
    start_node(
        request: typing.Optional[
            typing.Union[google.cloud.tpu_v2alpha1.types.cloud_tpu.StartNodeRequest, dict]
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
    ) -> google.api_core.operation_async.AsyncOperation

Starts a node.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_start_node():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[StartNodeRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.StartNodeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[start_node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_start_node)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.StartNodeRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.StartNodeRequest), dict]]`   
The request object. Request for StartNode.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.Node) A TPU instance.  
  
### stop_node
    
    
    stop_node(
        request: typing.Optional[
            typing.Union[google.cloud.tpu_v2alpha1.types.cloud_tpu.StopNodeRequest, dict]
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
    ) -> google.api_core.operation_async.AsyncOperation

Stops a node. This operation is only available with single TPU nodes.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_stop_node():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        request = tpu_v2alpha1.[StopNodeRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.StopNodeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[stop_node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_stop_node)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.StopNodeRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.StopNodeRequest), dict]]`   
The request object. Request for StopNode.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.Node) A TPU instance.  
  
### update_node
    
    
    update_node(
        request: typing.Optional[
            typing.Union[google.cloud.tpu_v2alpha1.types.cloud_tpu.UpdateNodeRequest, dict]
        ] = None,
        *,
        node: typing.Optional[google.cloud.tpu_v2alpha1.types.cloud_tpu.Node] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Updates the configurations of a node.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tpu_v2alpha1
    
    async def sample_update_node():
        # Create a client
        client = tpu_v2alpha1.[TpuAsyncClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html)()
    
        # Initialize request argument(s)
        node = tpu_v2alpha1.[Node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.Node.html)()
        node.runtime_version = "runtime_version_value"
    
        request = tpu_v2alpha1.[UpdateNodeRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.UpdateNodeRequest.html)(
            node=node,
        )
    
        # Make the request
        operation = await client.[update_node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuAsyncClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuAsyncClient_update_node)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.tpu_v2alpha1.types.UpdateNodeRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.UpdateNodeRequest), dict]]`   
The request object. Request for UpdateNode.  
`node` |  `[Node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.Node)`   
Required. The node. Only fields specified in update_mask are updated. This corresponds to the `node` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Mask of fields from `Node][Tpu.Node]` to update. Supported fields: [description, tags, labels, metadata, network_config.enable_external_ips]. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.Node) A TPU instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
