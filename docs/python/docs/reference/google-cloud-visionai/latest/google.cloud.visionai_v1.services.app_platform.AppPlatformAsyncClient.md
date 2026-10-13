---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient
title: Class AppPlatformAsyncClient (0.5.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:39:38.243778+00:00
---

# Class AppPlatformAsyncClient (0.5.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AppPlatformAsyncClient (0.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.3 (latest)  0.5.2  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    AppPlatformAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.visionai_v1.services.app_platform.transports.base.AppPlatformTransport,
                typing.Callable[
                    [...],
                    google.cloud.visionai_v1.services.app_platform.transports.base.AppPlatformTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service describing handlers for resources

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
`AppPlatformTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### AppPlatformAsyncClient
    
    
    AppPlatformAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.visionai_v1.services.app_platform.transports.base.AppPlatformTransport,
                typing.Callable[
                    [...],
                    google.cloud.visionai_v1.services.app_platform.transports.base.AppPlatformTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the app platform async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,AppPlatformTransport,Callable[..., AppPlatformTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the AppPlatformTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### add_application_stream_input
    
    
    add_application_stream_input(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.AddApplicationStreamInputRequest,
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

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_add_application_stream_input():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AddApplicationStreamInputRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.AddApplicationStreamInputRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[add_application_stream_input](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_add_application_stream_input)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.AddApplicationStreamInputRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.AddApplicationStreamInputRequest), dict]]`   
The request object. Message for adding stream input to an Application.  
`name` |  ``str``   
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}" This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [AddApplicationStreamInputResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.AddApplicationStreamInputResponse) Message for AddApplicationStreamInput Response.  
  
### application_path
    
    
    application_path(project: str, location: str, application: str) -> str

Returns a fully-qualified application string.

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

### create_application
    
    
    create_application(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.CreateApplicationRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        application: typing.Optional[
            google.cloud.visionai_v1.types.platform.Application
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

Creates a new Application in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_create_application():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        application = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[Application](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Application.html)()
        application.display_name = "display_name_value"
    
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[CreateApplicationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.CreateApplicationRequest.html)(
            parent="parent_value",
            application_id="application_id_value",
            application=application,
        )
    
        # Make the request
        operation = await client.[create_application](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_create_application)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.CreateApplicationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.CreateApplicationRequest), dict]]`   
The request object. Message for creating a Application.  
`parent` |  ``str``   
Required. Value for parent. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`application` |  `[Application](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Application)`   
Required. The resource being created. This corresponds to the `application` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Application](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Application) Message describing Application object  
  
### create_application_instances
    
    
    create_application_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.CreateApplicationInstancesRequest,
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

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_create_application_instances():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        application_instances = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[ApplicationInstance](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.ApplicationInstance.html)()
        application_instances.instance_id = "instance_id_value"
        application_instances.instance.display_name = "display_name_value"
    
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[CreateApplicationInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.CreateApplicationInstancesRequest.html)(
            name="name_value",
            application_instances=application_instances,
        )
    
        # Make the request
        operation = await client.[create_application_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_create_application_instances)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.CreateApplicationInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.CreateApplicationInstancesRequest), dict]]`   
The request object. Message for adding stream input to an Application.  
`name` |  ``str``   
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}" This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [CreateApplicationInstancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.CreateApplicationInstancesResponse) Message for CreateApplicationInstance Response.  
  
### create_draft
    
    
    create_draft(
        request: typing.Optional[
            typing.Union[google.cloud.visionai_v1.types.platform.CreateDraftRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        draft: typing.Optional[google.cloud.visionai_v1.types.platform.Draft] = None,
        draft_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Draft in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_create_draft():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        draft = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[Draft](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Draft.html)()
        draft.display_name = "display_name_value"
    
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[CreateDraftRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.CreateDraftRequest.html)(
            parent="parent_value",
            draft_id="draft_id_value",
            draft=draft,
        )
    
        # Make the request
        operation = await client.[create_draft](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_create_draft)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.CreateDraftRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.CreateDraftRequest), dict]]`   
The request object. Message for creating a Draft.  
`parent` |  ``str``   
Required. Value for parent. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`draft` |  `[Draft](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Draft)`   
Required. The resource being created. This corresponds to the `draft` field on the `request` instance; if `request` is provided, this should not be set.  
`draft_id` |  ``str``   
Required. Id of the requesting object. This corresponds to the `draft_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Draft](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Draft) Message describing Draft object  
  
### create_processor
    
    
    create_processor(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.CreateProcessorRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        processor: typing.Optional[
            google.cloud.visionai_v1.types.platform.Processor
        ] = None,
        processor_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Processor in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_create_processor():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        processor = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[Processor](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Processor.html)()
        processor.display_name = "display_name_value"
    
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[CreateProcessorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.CreateProcessorRequest.html)(
            parent="parent_value",
            processor_id="processor_id_value",
            processor=processor,
        )
    
        # Make the request
        operation = await client.[create_processor](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_create_processor)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.CreateProcessorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.CreateProcessorRequest), dict]]`   
The request object. Message for creating a Processor.  
`parent` |  ``str``   
Required. Value for parent. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`processor` |  `[Processor](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Processor)`   
Required. The resource being created. This corresponds to the `processor` field on the `request` instance; if `request` is provided, this should not be set.  
`processor_id` |  ``str``   
Required. Id of the requesting object. This corresponds to the `processor_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Processor](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Processor) Message describing Processor object. Next ID: 19  
  
### delete_application
    
    
    delete_application(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.DeleteApplicationRequest, dict
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

Deletes a single Application.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_delete_application():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[DeleteApplicationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.DeleteApplicationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_application](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_delete_application)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.DeleteApplicationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.DeleteApplicationRequest), dict]]`   
The request object. Message for deleting an Application.  
`name` |  ``str``   
Required. Name of the resource. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_application_instances
    
    
    delete_application_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.DeleteApplicationInstancesRequest,
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

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_delete_application_instances():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[DeleteApplicationInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.DeleteApplicationInstancesRequest.html)(
            name="name_value",
            instance_ids=['instance_ids_value1', 'instance_ids_value2'],
        )
    
        # Make the request
        operation = await client.[delete_application_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_delete_application_instances)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.DeleteApplicationInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.DeleteApplicationInstancesRequest), dict]]`   
The request object. Message for removing stream input from an Application.  
`name` |  ``str``   
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}" This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Instance) Message describing Instance object Next ID: 12  
  
### delete_draft
    
    
    delete_draft(
        request: typing.Optional[
            typing.Union[google.cloud.visionai_v1.types.platform.DeleteDraftRequest, dict]
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

Deletes a single Draft.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_delete_draft():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[DeleteDraftRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.DeleteDraftRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_draft](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_delete_draft)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.DeleteDraftRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.DeleteDraftRequest), dict]]`   
The request object. Message for deleting a Draft.  
`name` |  ``str``   
Required. Name of the resource. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_processor
    
    
    delete_processor(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.DeleteProcessorRequest, dict
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

Deletes a single Processor.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_delete_processor():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[DeleteProcessorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.DeleteProcessorRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_processor](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_delete_processor)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.DeleteProcessorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.DeleteProcessorRequest), dict]]`   
The request object. Message for deleting a Processor.  
`name` |  ``str``   
Required. Name of the resource This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### deploy_application
    
    
    deploy_application(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.DeployApplicationRequest, dict
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

Deploys a single Application.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_deploy_application():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[DeployApplicationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.DeployApplicationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[deploy_application](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_deploy_application)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.DeployApplicationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.DeployApplicationRequest), dict]]`   
The request object. Message for deploying an Application.  
`name` |  ``str``   
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}" This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [DeployApplicationResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.DeployApplicationResponse) RPC Request Messages. Message for DeployApplication Response.  
  
### draft_path
    
    
    draft_path(project: str, location: str, application: str, draft: str) -> str

Returns a fully-qualified draft string.

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
`AppPlatformAsyncClient` | The constructed client.  
  
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
`AppPlatformAsyncClient` | The constructed client.  
  
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
`AppPlatformAsyncClient` | The constructed client.  
  
### get_application
    
    
    get_application(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.GetApplicationRequest, dict
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
    ) -> google.cloud.visionai_v1.types.platform.Application

Gets details of a single Application.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_get_application():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[GetApplicationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.GetApplicationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_application](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_get_application)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.GetApplicationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.GetApplicationRequest), dict]]`   
The request object. Message for getting a Application.  
`name` |  ``str``   
Required. Name of the resource. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.visionai_v1.types.Application](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Application)` | Message describing Application object  
  
### get_draft
    
    
    get_draft(
        request: typing.Optional[
            typing.Union[google.cloud.visionai_v1.types.platform.GetDraftRequest, dict]
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
    ) -> google.cloud.visionai_v1.types.platform.Draft

Gets details of a single Draft.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_get_draft():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[GetDraftRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.GetDraftRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_draft](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_get_draft)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.GetDraftRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.GetDraftRequest), dict]]`   
The request object. Message for getting a Draft.  
`name` |  ``str``   
Required. Name of the resource. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.visionai_v1.types.Draft](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Draft)` | Message describing Draft object  
  
### get_instance
    
    
    get_instance(
        request: typing.Optional[
            typing.Union[google.cloud.visionai_v1.types.platform.GetInstanceRequest, dict]
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
    ) -> google.cloud.visionai_v1.types.platform.Instance

Gets details of a single Instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_get_instance():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[GetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.GetInstanceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_instance](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_get_instance)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.GetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.GetInstanceRequest), dict]]`   
The request object. Message for getting a Instance.  
`name` |  ``str``   
Required. Name of the resource. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.visionai_v1.types.Instance](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Instance)` | Message describing Instance object Next ID: 12  
  
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
  
### get_processor
    
    
    get_processor(
        request: typing.Optional[
            typing.Union[google.cloud.visionai_v1.types.platform.GetProcessorRequest, dict]
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
    ) -> google.cloud.visionai_v1.types.platform.Processor

Gets details of a single Processor.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_get_processor():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[GetProcessorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.GetProcessorRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_processor](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_get_processor)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.GetProcessorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.GetProcessorRequest), dict]]`   
The request object. Message for getting a Processor.  
`name` |  ``str``   
Required. Name of the resource. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.visionai_v1.types.Processor](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Processor)` | Message describing Processor object. Next ID: 19  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.visionai_v1.services.app_platform.transports.base.AppPlatformTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### instance_path
    
    
    instance_path(project: str, location: str, application: str, instance: str) -> str

Returns a fully-qualified instance string.

### list_applications
    
    
    list_applications(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.ListApplicationsRequest, dict
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
    ) -> google.cloud.visionai_v1.services.app_platform.pagers.ListApplicationsAsyncPager

Lists Applications in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_list_applications():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[ListApplicationsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.ListApplicationsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_applications](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_list_applications)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.ListApplicationsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.ListApplicationsRequest), dict]]`   
The request object. Message for requesting list of Applications.  
`parent` |  ``str``   
Required. Parent value for ListApplicationsRequest. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.visionai_v1.services.app_platform.pagers.ListApplicationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.pagers.ListApplicationsAsyncPager)` | Message for response to listing Applications. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_drafts
    
    
    list_drafts(
        request: typing.Optional[
            typing.Union[google.cloud.visionai_v1.types.platform.ListDraftsRequest, dict]
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
    ) -> google.cloud.visionai_v1.services.app_platform.pagers.ListDraftsAsyncPager

Lists Drafts in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_list_drafts():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[ListDraftsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.ListDraftsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_drafts](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_list_drafts)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.ListDraftsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.ListDraftsRequest), dict]]`   
The request object. Message for requesting list of Drafts.  
`parent` |  ``str``   
Required. Parent value for ListDraftsRequest. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.visionai_v1.services.app_platform.pagers.ListDraftsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.pagers.ListDraftsAsyncPager)` | Message for response to listing Drafts. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_instances
    
    
    list_instances(
        request: typing.Optional[
            typing.Union[google.cloud.visionai_v1.types.platform.ListInstancesRequest, dict]
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
    ) -> google.cloud.visionai_v1.services.app_platform.pagers.ListInstancesAsyncPager

Lists Instances in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_list_instances():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[ListInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.ListInstancesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_list_instances)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.ListInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.ListInstancesRequest), dict]]`   
The request object. Message for requesting list of Instances.  
`parent` |  ``str``   
Required. Parent value for ListInstancesRequest. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.visionai_v1.services.app_platform.pagers.ListInstancesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.pagers.ListInstancesAsyncPager)` | Message for response to listing Instances. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### list_prebuilt_processors
    
    
    list_prebuilt_processors(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.ListPrebuiltProcessorsRequest, dict
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
    ) -> google.cloud.visionai_v1.types.platform.ListPrebuiltProcessorsResponse

ListPrebuiltProcessors is a custom pass-through verb that Lists Prebuilt Processors.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_list_prebuilt_processors():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[ListPrebuiltProcessorsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.ListPrebuiltProcessorsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[list_prebuilt_processors](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_list_prebuilt_processors)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.ListPrebuiltProcessorsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.ListPrebuiltProcessorsRequest), dict]]`   
The request object. Request Message for listing Prebuilt Processors.  
`parent` |  ``str``   
Required. Parent path. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.visionai_v1.types.ListPrebuiltProcessorsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.ListPrebuiltProcessorsResponse)` | Response Message for listing Prebuilt Processors.  
  
### list_processors
    
    
    list_processors(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.ListProcessorsRequest, dict
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
    ) -> google.cloud.visionai_v1.services.app_platform.pagers.ListProcessorsAsyncPager

Lists Processors in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_list_processors():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[ListProcessorsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.ListProcessorsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_processors](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_list_processors)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.ListProcessorsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.ListProcessorsRequest), dict]]`   
The request object. Message for requesting list of Processors.  
`parent` |  ``str``   
Required. Parent value for ListProcessorsRequest. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.visionai_v1.services.app_platform.pagers.ListProcessorsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.pagers.ListProcessorsAsyncPager)` | Message for response to listing Processors. Iterating over this object will yield results and resolve additional pages automatically.  
  
### parse_application_path
    
    
    parse_application_path(path: str) -> typing.Dict[str, str]

Parses a application path into its component segments.

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

### parse_draft_path
    
    
    parse_draft_path(path: str) -> typing.Dict[str, str]

Parses a draft path into its component segments.

### parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

### parse_processor_path
    
    
    parse_processor_path(path: str) -> typing.Dict[str, str]

Parses a processor path into its component segments.

### parse_stream_path
    
    
    parse_stream_path(path: str) -> typing.Dict[str, str]

Parses a stream path into its component segments.

### processor_path
    
    
    processor_path(project: str, location: str, processor: str) -> str

Returns a fully-qualified processor string.

### remove_application_stream_input
    
    
    remove_application_stream_input(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.RemoveApplicationStreamInputRequest,
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

Remove target stream input to the Application, if the Application is deployed, the corresponding instance based will be deleted. If the stream is not in the Application, the RPC will fail.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_remove_application_stream_input():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[RemoveApplicationStreamInputRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.RemoveApplicationStreamInputRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[remove_application_stream_input](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_remove_application_stream_input)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.RemoveApplicationStreamInputRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.RemoveApplicationStreamInputRequest), dict]]`   
The request object. Message for removing stream input from an Application.  
`name` |  ``str``   
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}" This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [RemoveApplicationStreamInputResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.RemoveApplicationStreamInputResponse) Message for RemoveApplicationStreamInput Response.  
  
### stream_path
    
    
    stream_path(project: str, location: str, cluster: str, stream: str) -> str

Returns a fully-qualified stream string.

### undeploy_application
    
    
    undeploy_application(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.UndeployApplicationRequest, dict
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

Undeploys a single Application.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_undeploy_application():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[UndeployApplicationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.UndeployApplicationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[undeploy_application](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_undeploy_application)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.UndeployApplicationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.UndeployApplicationRequest), dict]]`   
The request object. Message for undeploying an Application.  
`name` |  ``str``   
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}" This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [UndeployApplicationResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.UndeployApplicationResponse) Message for UndeployApplication Response.  
  
### update_application
    
    
    update_application(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.UpdateApplicationRequest, dict
            ]
        ] = None,
        *,
        application: typing.Optional[
            google.cloud.visionai_v1.types.platform.Application
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
    ) -> google.api_core.operation_async.AsyncOperation

Updates the parameters of a single Application.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_update_application():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        application = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[Application](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Application.html)()
        application.display_name = "display_name_value"
    
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[UpdateApplicationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.UpdateApplicationRequest.html)(
            application=application,
        )
    
        # Make the request
        operation = await client.[update_application](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_update_application)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.UpdateApplicationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.UpdateApplicationRequest), dict]]`   
The request object. Message for updating an Application.  
`application` |  `[Application](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Application)`   
Required. The resource being updated. This corresponds to the `application` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. Field mask is used to specify the fields to be overwritten in the Application resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Application](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Application) Message describing Application object  
  
### update_application_instances
    
    
    update_application_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.UpdateApplicationInstancesRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        application_instances: typing.Optional[
            typing.MutableSequence[
                google.cloud.visionai_v1.types.platform.UpdateApplicationInstancesRequest.UpdateApplicationInstance
            ]
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

Adds target stream input to the Application. If the Application is deployed, the corresponding new Application instance will be created. If the stream has already been in the Application, the RPC will fail.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_update_application_instances():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[UpdateApplicationInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.UpdateApplicationInstancesRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[update_application_instances](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_update_application_instances)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.UpdateApplicationInstancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.UpdateApplicationInstancesRequest), dict]]`   
The request object. Message for updating an ApplicationInstance.  
`name` |  ``str``   
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}" This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`application_instances` |  `:class:`MutableSequence[[google.cloud.visionai_v1.types.UpdateApplicationInstancesRequest.UpdateApplicationInstance](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.UpdateApplicationInstancesRequest.UpdateApplicationInstance)]``   
This corresponds to the `application_instances` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [UpdateApplicationInstancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.UpdateApplicationInstancesResponse) Message for UpdateApplicationInstances Response.  
  
### update_application_stream_input
    
    
    update_application_stream_input(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.UpdateApplicationStreamInputRequest,
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

Update target stream input to the Application, if the Application is deployed, the corresponding instance based will be deployed. For CreateOrUpdate behavior, set allow_missing to true.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_update_application_stream_input():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[UpdateApplicationStreamInputRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.UpdateApplicationStreamInputRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[update_application_stream_input](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_update_application_stream_input)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.UpdateApplicationStreamInputRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.UpdateApplicationStreamInputRequest), dict]]`   
The request object. Message for updating stream input to an Application.  
`name` |  ``str``   
Required. the name of the application to retrieve. Format: "projects/{project}/locations/{location}/applications/{application}" This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [UpdateApplicationStreamInputResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.UpdateApplicationStreamInputResponse) Message for AddApplicationStreamInput Response.  
  
### update_draft
    
    
    update_draft(
        request: typing.Optional[
            typing.Union[google.cloud.visionai_v1.types.platform.UpdateDraftRequest, dict]
        ] = None,
        *,
        draft: typing.Optional[google.cloud.visionai_v1.types.platform.Draft] = None,
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

Updates the parameters of a single Draft.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_update_draft():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        draft = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[Draft](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Draft.html)()
        draft.display_name = "display_name_value"
    
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[UpdateDraftRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.UpdateDraftRequest.html)(
            draft=draft,
        )
    
        # Make the request
        operation = await client.[update_draft](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_update_draft)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.UpdateDraftRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.UpdateDraftRequest), dict]]`   
The request object. Message for updating a Draft.  
`draft` |  `[Draft](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Draft)`   
Required. The resource being updated. This corresponds to the `draft` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. Field mask is used to specify the fields to be overwritten in the Draft resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Draft](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Draft) Message describing Draft object  
  
### update_processor
    
    
    update_processor(
        request: typing.Optional[
            typing.Union[
                google.cloud.visionai_v1.types.platform.UpdateProcessorRequest, dict
            ]
        ] = None,
        *,
        processor: typing.Optional[
            google.cloud.visionai_v1.types.platform.Processor
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
    ) -> google.api_core.operation_async.AsyncOperation

Updates the parameters of a single Processor.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest)
    
    async def sample_update_processor():
        # Create a client
        client = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[AppPlatformAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html)()
    
        # Initialize request argument(s)
        processor = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[Processor](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Processor.html)()
        processor.display_name = "display_name_value"
    
        request = [visionai_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest).[UpdateProcessorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.UpdateProcessorRequest.html)(
            processor=processor,
        )
    
        # Make the request
        operation = await client.[update_processor](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.services.app_platform.AppPlatformAsyncClient.html#google_cloud_visionai_v1_services_app_platform_AppPlatformAsyncClient_update_processor)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.visionai_v1.types.UpdateProcessorRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.UpdateProcessorRequest), dict]]`   
The request object. Message for updating a Processor.  
`processor` |  `[Processor](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Processor)`   
Required. The resource being updated. This corresponds to the `processor` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. Field mask is used to specify the fields to be overwritten in the Processor resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Processor](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1.types.Processor) Message describing Processor object. Next ID: 19  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
