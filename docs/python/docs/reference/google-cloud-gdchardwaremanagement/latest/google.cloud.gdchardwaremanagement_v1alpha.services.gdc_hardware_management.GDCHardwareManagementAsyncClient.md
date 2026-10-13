---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient
title: Class GDCHardwareManagementAsyncClient (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:16:41.608010+00:00
---

# Class GDCHardwareManagementAsyncClient (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GDCHardwareManagementAsyncClient (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.3.0  0.2.0  0.1.13 
    
    
    GDCHardwareManagementAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.transports.base.GDCHardwareManagementTransport,
                typing.Callable[
                    [...],
                    google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.transports.base.GDCHardwareManagementTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

The GDC Hardware Management service.

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
`GDCHardwareManagementTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### GDCHardwareManagementAsyncClient
    
    
    GDCHardwareManagementAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.transports.base.GDCHardwareManagementTransport,
                typing.Callable[
                    [...],
                    google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.transports.base.GDCHardwareManagementTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the gdc hardware management async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,GDCHardwareManagementTransport,Callable[..., GDCHardwareManagementTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the GDCHardwareManagementTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
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
  
### cancel_order
    
    
    cancel_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CancelOrderRequest,
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

Cancels an order.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_cancel_order():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[CancelOrderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CancelOrderRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[cancel_order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_cancel_order)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.CancelOrderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CancelOrderRequest), dict]]`   
The request object. A request to cancel an order.  
`name` |  ``str``   
Required. The name of the order. Format: `projects/{project}/locations/{location}/orders/{order}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Order) An order for GDC hardware.  
  
### change_log_entry_path
    
    
    change_log_entry_path(
        project: str, location: str, order: str, change_log_entry: str
    ) -> str

Returns a fully-qualified change_log_entry string.

### comment_path
    
    
    comment_path(project: str, location: str, order: str, comment: str) -> str

Returns a fully-qualified comment string.

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

### create_comment
    
    
    create_comment(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateCommentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        comment: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Comment
        ] = None,
        comment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new comment on an order.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_create_comment():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        comment = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[Comment](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Comment.html)()
        comment.text = "text_value"
    
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[CreateCommentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CreateCommentRequest.html)(
            parent="parent_value",
            comment=comment,
        )
    
        # Make the request
        operation = await client.[create_comment](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_create_comment)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.CreateCommentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CreateCommentRequest), dict]]`   
The request object. A request to create a comment.  
`parent` |  ``str``   
Required. The order to create the comment on. Format: `projects/{project}/locations/{location}/orders/{order}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`comment` |  `[Comment](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Comment)`   
Required. The comment to create. This corresponds to the `comment` field on the `request` instance; if `request` is provided, this should not be set.  
`comment_id` |  ``str``   
Optional. ID used to uniquely identify the Comment within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The comment.name field in the request will be ignored. This corresponds to the `comment_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Comment](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Comment) A comment on an order.  
  
### create_hardware
    
    
    create_hardware(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateHardwareRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        hardware: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Hardware
        ] = None,
        hardware_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates new hardware in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_create_hardware():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        hardware = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[Hardware](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Hardware.html)()
        hardware.order = "order_value"
        hardware.site = "site_value"
        hardware.config.sku = "sku_value"
        hardware.config.power_supply = "POWER_SUPPLY_DC"
        hardware.zone = "zone_value"
    
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[CreateHardwareRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CreateHardwareRequest.html)(
            parent="parent_value",
            hardware=hardware,
        )
    
        # Make the request
        operation = await client.[create_hardware](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_create_hardware)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.CreateHardwareRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CreateHardwareRequest), dict]]`   
The request object. A request to create hardware.  
`parent` |  ``str``   
Required. The project and location to create hardware in. Format: `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`hardware` |  `[Hardware](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Hardware)`   
Required. The resource to create. This corresponds to the `hardware` field on the `request` instance; if `request` is provided, this should not be set.  
`hardware_id` |  ``str``   
Optional. ID used to uniquely identify the Hardware within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The hardware.name field in the request will be ignored. This corresponds to the `hardware_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Hardware](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Hardware) An instance of hardware installed at a site.  
  
### create_hardware_group
    
    
    create_hardware_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateHardwareGroupRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        hardware_group: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.HardwareGroup
        ] = None,
        hardware_group_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new hardware group in a given order.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_create_hardware_group():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        hardware_group = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[HardwareGroup](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup.html)()
        hardware_group.hardware_count = 1494
        hardware_group.config.sku = "sku_value"
        hardware_group.config.power_supply = "POWER_SUPPLY_DC"
        hardware_group.site = "site_value"
    
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[CreateHardwareGroupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CreateHardwareGroupRequest.html)(
            parent="parent_value",
            hardware_group=hardware_group,
        )
    
        # Make the request
        operation = await client.[create_hardware_group](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_create_hardware_group)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.CreateHardwareGroupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CreateHardwareGroupRequest), dict]]`   
The request object. A request to create a hardware group.  
`parent` |  ``str``   
Required. The order to create the hardware group in. Format: `projects/{project}/locations/{location}/orders/{order}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`hardware_group` |  `[HardwareGroup](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup)`   
Required. The hardware group to create. This corresponds to the `hardware_group` field on the `request` instance; if `request` is provided, this should not be set.  
`hardware_group_id` |  ``str``   
Optional. ID used to uniquely identify the HardwareGroup within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The hardware_group.name field in the request will be ignored. This corresponds to the `hardware_group_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [HardwareGroup](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup) A group of hardware that is part of the same order, has the same SKU, and is delivered to the same site.  
  
### create_order
    
    
    create_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateOrderRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        order: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Order
        ] = None,
        order_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new order in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_create_order():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        order = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[Order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Order.html)()
        order.organization_contact.contacts.given_name = "given_name_value"
        order.organization_contact.contacts.email = "email_value"
        order.organization_contact.contacts.phone = "phone_value"
        order.customer_motivation = "customer_motivation_value"
        order.region_code = "region_code_value"
    
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[CreateOrderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CreateOrderRequest.html)(
            parent="parent_value",
            order=order,
        )
    
        # Make the request
        operation = await client.[create_order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_create_order)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.CreateOrderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CreateOrderRequest), dict]]`   
The request object. A request to create an order.  
`parent` |  ``str``   
Required. The project and location to create the order in. Format: `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`order` |  `[Order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Order)`   
Required. The order to create. This corresponds to the `order` field on the `request` instance; if `request` is provided, this should not be set.  
`order_id` |  ``str``   
Optional. ID used to uniquely identify the Order within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The order.name field in the request will be ignored. This corresponds to the `order_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Order) An order for GDC hardware.  
  
### create_site
    
    
    create_site(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateSiteRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        site: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Site
        ] = None,
        site_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new site in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_create_site():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        site = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[Site](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Site.html)()
        site.organization_contact.contacts.given_name = "given_name_value"
        site.organization_contact.contacts.email = "email_value"
        site.organization_contact.contacts.phone = "phone_value"
    
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[CreateSiteRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CreateSiteRequest.html)(
            parent="parent_value",
            site=site,
        )
    
        # Make the request
        operation = await client.[create_site](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_create_site)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.CreateSiteRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CreateSiteRequest), dict]]`   
The request object. A request to create a site.  
`parent` |  ``str``   
Required. The project and location to create the site in. Format: `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`site` |  `[Site](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Site)`   
Required. The site to create. This corresponds to the `site` field on the `request` instance; if `request` is provided, this should not be set.  
`site_id` |  ``str``   
Optional. ID used to uniquely identify the Site within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The site.name field in the request will be ignored. This corresponds to the `site_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Site](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Site) A physical site where hardware will be installed.  
  
### create_zone
    
    
    create_zone(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateZoneRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        zone: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Zone
        ] = None,
        zone_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new zone in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_create_zone():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        zone = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[Zone](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Zone.html)()
        zone.contacts.given_name = "given_name_value"
        zone.contacts.email = "email_value"
        zone.contacts.phone = "phone_value"
    
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[CreateZoneRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CreateZoneRequest.html)(
            parent="parent_value",
            zone=zone,
        )
    
        # Make the request
        operation = await client.[create_zone](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_create_zone)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.CreateZoneRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CreateZoneRequest), dict]]`   
The request object. A request to create a zone.  
`parent` |  ``str``   
Required. The project and location to create the zone in. Format: `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`zone` |  `[Zone](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Zone)`   
Required. The zone to create. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`zone_id` |  ``str``   
Optional. ID used to uniquely identify the Zone within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and `-` are accepted. The `-` character cannot be the first or the last one. A system generated ID will be used if the field is not set. The zone.name field in the request will be ignored. This corresponds to the `zone_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Zone](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Zone) A zone holding a set of hardware.  
  
### delete_hardware
    
    
    delete_hardware(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.DeleteHardwareRequest,
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

Deletes hardware.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_delete_hardware():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[DeleteHardwareRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.DeleteHardwareRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_hardware](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_delete_hardware)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.DeleteHardwareRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.DeleteHardwareRequest), dict]]`   
The request object. A request to delete hardware.  
`name` |  ``str``   
Required. The name of the hardware. Format: `projects/{project}/locations/{location}/hardware/{hardware}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_hardware_group
    
    
    delete_hardware_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.DeleteHardwareGroupRequest,
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

Deletes a hardware group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_delete_hardware_group():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[DeleteHardwareGroupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.DeleteHardwareGroupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_hardware_group](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_delete_hardware_group)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.DeleteHardwareGroupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.DeleteHardwareGroupRequest), dict]]`   
The request object. A request to delete a hardware group.  
`name` |  ``str``   
Required. The name of the hardware group. Format: `projects/{project}/locations/{location}/orders/{order}/hardwareGroups/{hardware_group}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_order
    
    
    delete_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.DeleteOrderRequest,
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

Deletes an order.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_delete_order():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[DeleteOrderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.DeleteOrderRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_delete_order)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.DeleteOrderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.DeleteOrderRequest), dict]]`   
The request object. A request to delete an order.  
`name` |  ``str``   
Required. The name of the order. Format: `projects/{project}/locations/{location}/orders/{order}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_site
    
    
    delete_site(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.DeleteSiteRequest,
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

Deletes a site.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_delete_site():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[DeleteSiteRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.DeleteSiteRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_site](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_delete_site)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.DeleteSiteRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.DeleteSiteRequest), dict]]`   
The request object. A request to delete a site.  
`name` |  ``str``   
Required. The name of the site. Format: `projects/{project}/locations/{location}/sites/{site}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_zone
    
    
    delete_zone(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.DeleteZoneRequest,
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

Deletes a zone.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_delete_zone():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[DeleteZoneRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.DeleteZoneRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_zone](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_delete_zone)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.DeleteZoneRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.DeleteZoneRequest), dict]]`   
The request object. A request to delete a zone.  
`name` |  ``str``   
Required. The name of the zone. Format: `projects/{project}/locations/{location}/zones/{zone}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
`GDCHardwareManagementAsyncClient` | The constructed client.  
  
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
`GDCHardwareManagementAsyncClient` | The constructed client.  
  
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
`GDCHardwareManagementAsyncClient` | The constructed client.  
  
### get_change_log_entry
    
    
    get_change_log_entry(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetChangeLogEntryRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.ChangeLogEntry

Gets details of a change to an order.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_get_change_log_entry():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GetChangeLogEntryRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.GetChangeLogEntryRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_change_log_entry](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_change_log_entry)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.GetChangeLogEntryRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.GetChangeLogEntryRequest), dict]]`   
The request object. A request to get a change log entry.  
`name` |  ``str``   
Required. The name of the change log entry. Format: `projects/{project}/locations/{location}/orders/{order}/changeLogEntries/{change_log_entry}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.gdchardwaremanagement_v1alpha.types.ChangeLogEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ChangeLogEntry)` | A log entry of a change made to an order.  
  
### get_comment
    
    
    get_comment(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetCommentRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Comment

Gets the content of a comment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_get_comment():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GetCommentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.GetCommentRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_comment](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_comment)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.GetCommentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.GetCommentRequest), dict]]`   
The request object. A request to get a comment.  
`name` |  ``str``   
Required. The name of the comment. Format: `projects/{project}/locations/{location}/orders/{order}/comments/{comment}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.gdchardwaremanagement_v1alpha.types.Comment](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Comment)` | A comment on an order.  
  
### get_hardware
    
    
    get_hardware(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetHardwareRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Hardware

Gets hardware details.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_get_hardware():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GetHardwareRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.GetHardwareRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_hardware](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_hardware)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.GetHardwareRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.GetHardwareRequest), dict]]`   
The request object. A request to get hardware.  
`name` |  ``str``   
Required. The name of the hardware. Format: `projects/{project}/locations/{location}/hardware/{hardware}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.gdchardwaremanagement_v1alpha.types.Hardware](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Hardware)` | An instance of hardware installed at a site.  
  
### get_hardware_group
    
    
    get_hardware_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetHardwareGroupRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.HardwareGroup

Gets details of a hardware group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_get_hardware_group():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GetHardwareGroupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.GetHardwareGroupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_hardware_group](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_hardware_group)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.GetHardwareGroupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.GetHardwareGroupRequest), dict]]`   
The request object. A request to get a hardware group.  
`name` |  ``str``   
Required. The name of the hardware group. Format: `projects/{project}/locations/{location}/orders/{order}/hardwareGroups/{hardware_group}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup)` | A group of hardware that is part of the same order, has the same SKU, and is delivered to the same site.  
  
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
  
### get_order
    
    
    get_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetOrderRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Order

Gets details of an order.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_get_order():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GetOrderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.GetOrderRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_order)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.GetOrderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.GetOrderRequest), dict]]`   
The request object. A request to get an order.  
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
`[google.cloud.gdchardwaremanagement_v1alpha.types.Order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Order)` | An order for GDC hardware.  
  
### get_site
    
    
    get_site(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetSiteRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Site

Gets details of a site.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_get_site():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GetSiteRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.GetSiteRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_site](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_site)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.GetSiteRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.GetSiteRequest), dict]]`   
The request object. A request to get a site.  
`name` |  ``str``   
Required. The name of the site. Format: `projects/{project}/locations/{location}/sites/{site}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.gdchardwaremanagement_v1alpha.types.Site](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Site)` | A physical site where hardware will be installed.  
  
### get_sku
    
    
    get_sku(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetSkuRequest, dict
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Sku

Gets details of an SKU.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_get_sku():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GetSkuRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.GetSkuRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_sku](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_sku)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.GetSkuRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.GetSkuRequest), dict]]`   
The request object. A request to get an SKU.  
`name` |  ``str``   
Required. The name of the SKU. Format: `projects/{project}/locations/{location}/skus/{sku}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.gdchardwaremanagement_v1alpha.types.Sku](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Sku)` | A stock keeping unit (SKU) of GDC hardware.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.transports.base.GDCHardwareManagementTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### get_zone
    
    
    get_zone(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetZoneRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Zone

Gets details of a zone.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_get_zone():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GetZoneRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.GetZoneRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_zone](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_zone)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.GetZoneRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.GetZoneRequest), dict]]`   
The request object. A request to get a zone.  
`name` |  ``str``   
Required. The name of the zone. Format: `projects/{project}/locations/{location}/zones/{zone}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.gdchardwaremanagement_v1alpha.types.Zone](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Zone)` | A zone holding a set of hardware.  
  
### hardware_group_path
    
    
    hardware_group_path(
        project: str, location: str, order: str, hardware_group: str
    ) -> str

Returns a fully-qualified hardware_group string.

### hardware_path
    
    
    hardware_path(project: str, location: str, hardware: str) -> str

Returns a fully-qualified hardware string.

### list_change_log_entries
    
    
    list_change_log_entries(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListChangeLogEntriesRequest,
                dict,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListChangeLogEntriesAsyncPager
    )

Lists the changes made to an order.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_list_change_log_entries():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[ListChangeLogEntriesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ListChangeLogEntriesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_change_log_entries](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_change_log_entries)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.ListChangeLogEntriesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ListChangeLogEntriesRequest), dict]]`   
The request object. A request to list change log entries.  
`parent` |  ``str``   
Required. The order to list change log entries for. Format: `projects/{project}/locations/{location}/orders/{order}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListChangeLogEntriesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListChangeLogEntriesAsyncPager)` | A list of change log entries. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_comments
    
    
    list_comments(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListCommentsRequest,
                dict,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListCommentsAsyncPager
    )

Lists the comments on an order.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_list_comments():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[ListCommentsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ListCommentsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_comments](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_comments)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.ListCommentsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ListCommentsRequest), dict]]`   
The request object. A request to list comments.  
`parent` |  ``str``   
Required. The order to list comments on. Format: `projects/{project}/locations/{location}/orders/{order}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListCommentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListCommentsAsyncPager)` | A request to list comments. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_hardware
    
    
    list_hardware(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareRequest,
                dict,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareAsyncPager
    )

Lists hardware in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_list_hardware():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[ListHardwareRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_hardware](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_hardware)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareRequest), dict]]`   
The request object. A request to list hardware.  
`parent` |  ``str``   
Required. The project and location to list hardware in. Format: `projects/{project}/locations/{location}` To list hardware across all locations, substitute `-` (the hyphen or dash character) for the location and check the unreachable field in the response message. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareAsyncPager)` | A list of hardware. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_hardware_groups
    
    
    list_hardware_groups(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareGroupsRequest,
                dict,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareGroupsAsyncPager
    )

Lists hardware groups in a given order.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_list_hardware_groups():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[ListHardwareGroupsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareGroupsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_hardware_groups](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_hardware_groups)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareGroupsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ListHardwareGroupsRequest), dict]]`   
The request object. A request to list hardware groups.  
`parent` |  ``str``   
Required. The order to list hardware groups in. Format: `projects/{project}/locations/{location}/orders/{order}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareGroupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareGroupsAsyncPager)` | A list of hardware groups. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### list_orders
    
    
    list_orders(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListOrdersRequest,
                dict,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListOrdersAsyncPager
    )

Lists orders in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_list_orders():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[ListOrdersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ListOrdersRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_orders](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_orders)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.ListOrdersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ListOrdersRequest), dict]]`   
The request object. A request to list orders.  
`parent` |  ``str``   
Required. The project and location to list orders in. Format: `projects/{project}/locations/{location}` To list orders across all locations, substitute `-` (the hyphen or dash character) for the location and check the unreachable field in the response message. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListOrdersAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListOrdersAsyncPager)` | A list of orders. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_sites
    
    
    list_sites(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSitesRequest,
                dict,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSitesAsyncPager
    )

Lists sites in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_list_sites():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[ListSitesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ListSitesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_sites](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_sites)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.ListSitesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ListSitesRequest), dict]]`   
The request object. A request to list sites.  
`parent` |  ``str``   
Required. The project and location to list sites in. Format: `projects/{project}/locations/{location}` To list sites across all locations, substitute `-` (the hyphen or dash character) for the location and check the unreachable field in the response message. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSitesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSitesAsyncPager)` | A list of sites. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_skus
    
    
    list_skus(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSkusRequest,
                dict,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSkusAsyncPager
    )

Lists SKUs for a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_list_skus():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[ListSkusRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ListSkusRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_skus](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_skus)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.ListSkusRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ListSkusRequest), dict]]`   
The request object. A request to list SKUs.  
`parent` |  ``str``   
Required. The project and location to list SKUs in. Format: `projects/{project}/locations/{location}` To list SKUs across all locations, substitute `-` (the hyphen or dash character) for the location and check the unreachable field in the response message. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSkusAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSkusAsyncPager)` | A list of SKUs. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_zones
    
    
    list_zones(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListZonesRequest,
                dict,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListZonesAsyncPager
    )

Lists zones in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_list_zones():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[ListZonesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ListZonesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_zones](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_zones)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.ListZonesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ListZonesRequest), dict]]`   
The request object. A request to list zones.  
`parent` |  ``str``   
Required. The project and location to list zones in. Format: `projects/{project}/locations/{location}` To list zones across all locations, substitute `-` (the hyphen or dash character) for the location and check the unreachable field in the response message. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListZonesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListZonesAsyncPager)` | A list of zones. Iterating over this object will yield results and resolve additional pages automatically.  
  
### order_path
    
    
    order_path(project: str, location: str, order: str) -> str

Returns a fully-qualified order string.

### parse_change_log_entry_path
    
    
    parse_change_log_entry_path(path: str) -> typing.Dict[str, str]

Parses a change_log_entry path into its component segments.

### parse_comment_path
    
    
    parse_comment_path(path: str) -> typing.Dict[str, str]

Parses a comment path into its component segments.

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

### parse_hardware_group_path
    
    
    parse_hardware_group_path(path: str) -> typing.Dict[str, str]

Parses a hardware_group path into its component segments.

### parse_hardware_path
    
    
    parse_hardware_path(path: str) -> typing.Dict[str, str]

Parses a hardware path into its component segments.

### parse_order_path
    
    
    parse_order_path(path: str) -> typing.Dict[str, str]

Parses a order path into its component segments.

### parse_site_path
    
    
    parse_site_path(path: str) -> typing.Dict[str, str]

Parses a site path into its component segments.

### parse_sku_path
    
    
    parse_sku_path(path: str) -> typing.Dict[str, str]

Parses a sku path into its component segments.

### parse_zone_path
    
    
    parse_zone_path(path: str) -> typing.Dict[str, str]

Parses a zone path into its component segments.

### record_action_on_comment
    
    
    record_action_on_comment(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.RecordActionOnCommentRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        action_type: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.service.RecordActionOnCommentRequest.ActionType
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Comment

Record Action on a Comment. If the Action specified in the request is READ, the viewed time in the comment is set to the time the request was received. If the comment is already marked as read, subsequent calls will be ignored. If the Action is UNREAD, the viewed time is cleared from the comment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_record_action_on_comment():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[RecordActionOnCommentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.RecordActionOnCommentRequest.html)(
            name="name_value",
            action_type="UNREAD",
        )
    
        # Make the request
        response = await client.[record_action_on_comment](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_record_action_on_comment)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.RecordActionOnCommentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.RecordActionOnCommentRequest), dict]]`   
The request object. A request to record an action on a comment.  
`name` |  ``str``   
Required. The name of the comment. Format: `projects/{project}/locations/{location}/orders/{order}/comments/{comment}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`action_type` |  `[ActionType](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.RecordActionOnCommentRequest.ActionType)`   
Required. The action type of the recorded action. This corresponds to the `action_type` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.gdchardwaremanagement_v1alpha.types.Comment](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Comment)` | A comment on an order.  
  
### request_order_date_change
    
    
    request_order_date_change(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.RequestOrderDateChangeRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        requested_date: typing.Optional[google.type.date_pb2.Date] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Updates the requested date change of a single Order.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_request_order_date_change():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[RequestOrderDateChangeRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.RequestOrderDateChangeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[request_order_date_change](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_request_order_date_change)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.RequestOrderDateChangeRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.RequestOrderDateChangeRequest), dict]]`   
The request object. A request to change the requested date of an order.  
`name` |  ``str``   
Required. The name of the order to update. Format: projects/{project}/locations/{location}/orders/{order} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`requested_date` |  ``google.type.date_pb2.Date``   
Required. The date to which the customer or Google wants to set the scheduled installation date. This corresponds to the `requested_date` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Order) An order for GDC hardware.  
  
### signal_zone_state
    
    
    signal_zone_state(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.SignalZoneStateRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        state_signal: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.service.SignalZoneStateRequest.StateSignal
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

Signals the state of a zone.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_signal_zone_state():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[SignalZoneStateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.SignalZoneStateRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[signal_zone_state](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_signal_zone_state)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.SignalZoneStateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.SignalZoneStateRequest), dict]]`   
The request object. A request to signal the state of a zone.  
`name` |  ``str``   
Required. The name of the zone. Format: `projects/{project}/locations/{location}/zones/{zone}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`state_signal` |  `[StateSignal](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.SignalZoneStateRequest.StateSignal)`   
Optional. The state signal to send for this zone. Either state_signal or provisioning_state_signal must be set, but not both. This corresponds to the `state_signal` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Zone](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Zone) A zone holding a set of hardware.  
  
### site_path
    
    
    site_path(project: str, location: str, site: str) -> str

Returns a fully-qualified site string.

### sku_path
    
    
    sku_path(project: str, location: str, sku: str) -> str

Returns a fully-qualified sku string.

### submit_order
    
    
    submit_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.SubmitOrderRequest,
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

Submits an order.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_submit_order():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[SubmitOrderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.SubmitOrderRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[submit_order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_submit_order)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.SubmitOrderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.SubmitOrderRequest), dict]]`   
The request object. A request to submit an order.  
`name` |  ``str``   
Required. The name of the order. Format: `projects/{project}/locations/{location}/orders/{order}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Order) An order for GDC hardware.  
  
### update_hardware
    
    
    update_hardware(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.UpdateHardwareRequest,
                dict,
            ]
        ] = None,
        *,
        hardware: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Hardware
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

Updates hardware parameters.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_update_hardware():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        hardware = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[Hardware](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Hardware.html)()
        hardware.order = "order_value"
        hardware.site = "site_value"
        hardware.config.sku = "sku_value"
        hardware.config.power_supply = "POWER_SUPPLY_DC"
        hardware.zone = "zone_value"
    
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[UpdateHardwareRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.UpdateHardwareRequest.html)(
            hardware=hardware,
        )
    
        # Make the request
        operation = await client.[update_hardware](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_update_hardware)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.UpdateHardwareRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.UpdateHardwareRequest), dict]]`   
The request object. A request to update hardware.  
`hardware` |  `[Hardware](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Hardware)`   
Required. The hardware to update. This corresponds to the `hardware` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. A mask to specify the fields in the Hardware to overwrite with this update. The fields specified in the update_mask are relative to the hardware, not the full request. A field will be overwritten if it is in the mask. If you don't provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Hardware](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Hardware) An instance of hardware installed at a site.  
  
### update_hardware_group
    
    
    update_hardware_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.UpdateHardwareGroupRequest,
                dict,
            ]
        ] = None,
        *,
        hardware_group: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.HardwareGroup
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

Updates the parameters of a hardware group.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_update_hardware_group():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        hardware_group = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[HardwareGroup](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup.html)()
        hardware_group.hardware_count = 1494
        hardware_group.config.sku = "sku_value"
        hardware_group.config.power_supply = "POWER_SUPPLY_DC"
        hardware_group.site = "site_value"
    
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[UpdateHardwareGroupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.UpdateHardwareGroupRequest.html)(
            hardware_group=hardware_group,
        )
    
        # Make the request
        operation = await client.[update_hardware_group](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_update_hardware_group)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.UpdateHardwareGroupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.UpdateHardwareGroupRequest), dict]]`   
The request object. A request to update a hardware group.  
`hardware_group` |  `[HardwareGroup](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup)`   
Required. The hardware group to update. This corresponds to the `hardware_group` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. A mask to specify the fields in the HardwareGroup to overwrite with this update. The fields specified in the update_mask are relative to the hardware group, not the full request. A field will be overwritten if it is in the mask. If you don't provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [HardwareGroup](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup) A group of hardware that is part of the same order, has the same SKU, and is delivered to the same site.  
  
### update_order
    
    
    update_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.UpdateOrderRequest,
                dict,
            ]
        ] = None,
        *,
        order: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Order
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

Updates the parameters of an order.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_update_order():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        order = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[Order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Order.html)()
        order.organization_contact.contacts.given_name = "given_name_value"
        order.organization_contact.contacts.email = "email_value"
        order.organization_contact.contacts.phone = "phone_value"
        order.customer_motivation = "customer_motivation_value"
        order.region_code = "region_code_value"
    
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[UpdateOrderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.UpdateOrderRequest.html)(
            order=order,
        )
    
        # Make the request
        operation = await client.[update_order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_update_order)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.UpdateOrderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.UpdateOrderRequest), dict]]`   
The request object. A request to update an order.  
`order` |  `[Order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Order)`   
Required. The order to update. This corresponds to the `order` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. A mask to specify the fields in the Order to overwrite with this update. The fields specified in the update_mask are relative to the order, not the full request. A field will be overwritten if it is in the mask. If you don't provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Order) An order for GDC hardware.  
  
### update_site
    
    
    update_site(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.UpdateSiteRequest,
                dict,
            ]
        ] = None,
        *,
        site: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Site
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

Updates the parameters of a site.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_update_site():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        site = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[Site](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Site.html)()
        site.organization_contact.contacts.given_name = "given_name_value"
        site.organization_contact.contacts.email = "email_value"
        site.organization_contact.contacts.phone = "phone_value"
    
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[UpdateSiteRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.UpdateSiteRequest.html)(
            site=site,
        )
    
        # Make the request
        operation = await client.[update_site](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_update_site)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.UpdateSiteRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.UpdateSiteRequest), dict]]`   
The request object. A request to update a site.  
`site` |  `[Site](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Site)`   
Required. The site to update. This corresponds to the `site` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. A mask to specify the fields in the Site to overwrite with this update. The fields specified in the update_mask are relative to the site, not the full request. A field will be overwritten if it is in the mask. If you don't provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Site](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Site) A physical site where hardware will be installed.  
  
### update_zone
    
    
    update_zone(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.UpdateZoneRequest,
                dict,
            ]
        ] = None,
        *,
        zone: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Zone
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

Updates the parameters of a zone.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
    
    async def sample_update_zone():
        # Create a client
        client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html)()
    
        # Initialize request argument(s)
        zone = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[Zone](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Zone.html)()
        zone.contacts.given_name = "given_name_value"
        zone.contacts.email = "email_value"
        zone.contacts.phone = "phone_value"
    
        request = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[UpdateZoneRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.UpdateZoneRequest.html)(
            zone=zone,
        )
    
        # Make the request
        operation = await client.[update_zone](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_update_zone)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.gdchardwaremanagement_v1alpha.types.UpdateZoneRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.UpdateZoneRequest), dict]]`   
The request object. A request to update a zone.  
`zone` |  `[Zone](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Zone)`   
Required. The zone to update. This corresponds to the `zone` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. A mask to specify the fields in the Zone to overwrite with this update. The fields specified in the update_mask are relative to the zone, not the full request. A field will be overwritten if it is in the mask. If you don't provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Zone](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Zone) A zone holding a set of hardware.  
  
### zone_path
    
    
    zone_path(project: str, location: str, zone: str) -> str

Returns a fully-qualified zone string.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
