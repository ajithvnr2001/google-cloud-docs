---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient
title: Class ApiHubAsyncClient (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:15.362881+00:00
---

# Class ApiHubAsyncClient (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ApiHubAsyncClient (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    ApiHubAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.api_hub.transports.base.ApiHubTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.api_hub.transports.base.ApiHubTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

This service provides all methods related to the API hub.

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
`ApiHubTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### ApiHubAsyncClient
    
    
    ApiHubAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apihub_v1.services.api_hub.transports.base.ApiHubTransport,
                typing.Callable[
                    [...],
                    google.cloud.apihub_v1.services.api_hub.transports.base.ApiHubTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the api hub async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,ApiHubTransport,Callable[..., ApiHubTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the ApiHubTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### api_operation_path
    
    
    api_operation_path(
        project: str, location: str, api: str, version: str, operation: str
    ) -> str

Returns a fully-qualified api_operation string.

### api_path
    
    
    api_path(project: str, location: str, api: str) -> str

Returns a fully-qualified api string.

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

### create_api
    
    
    create_api(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.CreateApiRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api: typing.Optional[google.cloud.apihub_v1.types.common_fields.Api] = None,
        api_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Api

Create an API resource in the API hub. Once an API resource is created, versions can be added to it.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_create_api():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        api = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[Api](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Api.html)()
        api.display_name = "display_name_value"
    
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[CreateApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateApiRequest.html)(
            parent="parent_value",
            api=api,
        )
    
        # Make the request
        response = await client.[create_api](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_create_api)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.CreateApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateApiRequest), dict]]`   
The request object. The CreateApi method's request.  
`parent` |  ``str``   
Required. The parent resource for the API resource. Format: `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`api` |  `[Api](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Api)`   
Required. The API resource to create. This corresponds to the `api` field on the `request` instance; if `request` is provided, this should not be set.  
`api_id` |  ``str``   
Optional. The ID to use for the API resource, which will become the final component of the API's resource name. This field is optional. - If provided, the same will be used. The service will throw an error if the specified id is already used by another API resource in the API hub. - If not provided, a system generated id will be used. This value should be 4-500 characters, and valid characters are /`a-z][A-Z]`[0-9]-_/. This corresponds to the `api_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Api](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Api)` | An API resource in the API Hub.  
  
### create_api_operation
    
    
    create_api_operation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateApiOperationRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api_operation: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.ApiOperation
        ] = None,
        api_operation_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.ApiOperation

Create an apiOperation in an API version. An apiOperation can be created only if the version has no apiOperations which were created by parsing a spec.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_create_api_operation():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[CreateApiOperationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateApiOperationRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[create_api_operation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_create_api_operation)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.CreateApiOperationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateApiOperationRequest), dict]]`   
The request object. The CreateApiOperation method's request.  
`parent` |  ``str``   
Required. The parent resource for the operation resource. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`api_operation` |  `[ApiOperation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiOperation)`   
Required. The operation resource to create. This corresponds to the `api_operation` field on the `request` instance; if `request` is provided, this should not be set.  
`api_operation_id` |  ``str``   
Optional. The ID to use for the operation resource, which will become the final component of the operation's resource name. This field is optional. - If provided, the same will be used. The service will throw an error if the specified id is already used by another operation resource in the API hub. - If not provided, a system generated id will be used. This value should be 4-500 characters, overall resource name which will be of format `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}`, its length is limited to 700 characters, and valid characters are /`a-z][A-Z]`[0-9]-_/. This corresponds to the `api_operation_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.ApiOperation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiOperation)` | Represents an operation contained in an API version in the API Hub. An operation is added/updated/deleted in an API version when a new spec is added or an existing spec is updated/deleted in a version. Currently, an operation will be created only corresponding to OpenAPI spec as parsing is supported for OpenAPI spec. Alternatively operations can be managed via create,update and delete APIs, creation of apiOperation can be possible only for version with no parsed operations and update/delete can be possible only for operations created via create API.  
  
### create_attribute
    
    
    create_attribute(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateAttributeRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        attribute: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.Attribute
        ] = None,
        attribute_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Attribute

Create a user defined attribute.

Certain pre defined attributes are already created by the API hub. These attributes will have type as `SYSTEM_DEFINED` and can be listed via xref_ListAttributes method. Allowed values for the same can be updated via xref_UpdateAttribute method.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_create_attribute():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        attribute = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[Attribute](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Attribute.html)()
        attribute.display_name = "display_name_value"
        attribute.scope = "PLUGIN"
        attribute.data_type = "URI"
    
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[CreateAttributeRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateAttributeRequest.html)(
            parent="parent_value",
            attribute=attribute,
        )
    
        # Make the request
        response = await client.[create_attribute](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_create_attribute)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.CreateAttributeRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateAttributeRequest), dict]]`   
The request object. The CreateAttribute method's request.  
`parent` |  ``str``   
Required. The parent resource for Attribute. Format: `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`attribute` |  `[Attribute](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Attribute)`   
Required. The attribute to create. This corresponds to the `attribute` field on the `request` instance; if `request` is provided, this should not be set.  
`attribute_id` |  ``str``   
Optional. The ID to use for the attribute, which will become the final component of the attribute's resource name. This field is optional. - If provided, the same will be used. The service will throw an error if the specified id is already used by another attribute resource in the API hub. - If not provided, a system generated id will be used. This value should be 4-500 characters, and valid characters are /`a-z][A-Z]`[0-9]-_/. This corresponds to the `attribute_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Attribute](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Attribute)` | An attribute in the API Hub. An attribute is a name value pair which can be attached to different resources in the API hub based on the scope of the attribute. Attributes can either be pre-defined by the API Hub or created by users.  
  
### create_deployment
    
    
    create_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateDeploymentRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deployment: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.Deployment
        ] = None,
        deployment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Deployment

Create a deployment resource in the API hub. Once a deployment resource is created, it can be associated with API versions.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_create_deployment():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        deployment = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[Deployment](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Deployment.html)()
        deployment.display_name = "display_name_value"
        deployment.deployment_type.enum_values.values.id = "id_value"
        deployment.deployment_type.enum_values.values.display_name = "display_name_value"
        deployment.resource_uri = "resource_uri_value"
        deployment.endpoints = ['endpoints_value1', 'endpoints_value2']
    
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[CreateDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateDeploymentRequest.html)(
            parent="parent_value",
            deployment=deployment,
        )
    
        # Make the request
        response = await client.[create_deployment](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_create_deployment)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.CreateDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateDeploymentRequest), dict]]`   
The request object. The CreateDeployment method's request.  
`parent` |  ``str``   
Required. The parent resource for the deployment resource. Format: `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`deployment` |  `[Deployment](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Deployment)`   
Required. The deployment resource to create. This corresponds to the `deployment` field on the `request` instance; if `request` is provided, this should not be set.  
`deployment_id` |  ``str``   
Optional. The ID to use for the deployment resource, which will become the final component of the deployment's resource name. This field is optional. - If provided, the same will be used. The service will throw an error if the specified id is already used by another deployment resource in the API hub. - If not provided, a system generated id will be used. This value should be 4-500 characters, and valid characters are /`a-z][A-Z]`[0-9]-_/. This corresponds to the `deployment_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Deployment](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Deployment)` | Details of the deployment where APIs are hosted. A deployment could represent an Apigee proxy, API gateway, other Google Cloud services or non-Google Cloud services as well. A deployment entity is a root level entity in the API hub and exists independent of any API.  
  
### create_external_api
    
    
    create_external_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateExternalApiRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        external_api: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.ExternalApi
        ] = None,
        external_api_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.ExternalApi

Create an External API resource in the API hub.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_create_external_api():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        external_api = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ExternalApi](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ExternalApi.html)()
        external_api.display_name = "display_name_value"
    
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[CreateExternalApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateExternalApiRequest.html)(
            parent="parent_value",
            external_api=external_api,
        )
    
        # Make the request
        response = await client.[create_external_api](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_create_external_api)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.CreateExternalApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateExternalApiRequest), dict]]`   
The request object. The CreateExternalApi method's request.  
`parent` |  ``str``   
Required. The parent resource for the External API resource. Format: `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`external_api` |  `[ExternalApi](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ExternalApi)`   
Required. The External API resource to create. This corresponds to the `external_api` field on the `request` instance; if `request` is provided, this should not be set.  
`external_api_id` |  ``str``   
Optional. The ID to use for the External API resource, which will become the final component of the External API's resource name. This field is optional. - If provided, the same will be used. The service will throw an error if the specified id is already used by another External API resource in the API hub. - If not provided, a system generated id will be used. This value should be 4-500 characters, and valid characters are /`a-z][A-Z]`[0-9]-_/. This corresponds to the `external_api_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.ExternalApi](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ExternalApi)` | An external API represents an API being provided by external sources. This can be used to model third-party APIs and can be used to define dependencies.  
  
### create_spec
    
    
    create_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateSpecRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        spec: typing.Optional[google.cloud.apihub_v1.types.common_fields.Spec] = None,
        spec_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Spec

Add a spec to an API version in the API hub. Multiple specs can be added to an API version. Note, while adding a spec, at least one of `contents` or `source_uri` must be provided. If `contents` is provided, then `spec_type` must also be provided.

On adding a spec with contents to the version, the operations present in it will be added to the version.Note that the file contents in the spec should be of the same type as defined in the `projects/{project}/locations/{location}/attributes/system-spec-type` attribute associated with spec resource. Note that specs of various types can be uploaded, however parsing of details is supported for OpenAPI spec currently.

In order to access the information parsed from the spec, use the xref_GetSpec method. In order to access the raw contents for a particular spec, use the xref_GetSpecContents method. In order to access the operations parsed from the spec, use the xref_ListAPIOperations method.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_create_spec():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        spec = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[Spec](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Spec.html)()
        spec.display_name = "display_name_value"
        spec.spec_type.enum_values.values.id = "id_value"
        spec.spec_type.enum_values.values.display_name = "display_name_value"
    
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[CreateSpecRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateSpecRequest.html)(
            parent="parent_value",
            spec=spec,
        )
    
        # Make the request
        response = await client.[create_spec](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_create_spec)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.CreateSpecRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateSpecRequest), dict]]`   
The request object. The CreateSpec method's request.  
`parent` |  ``str``   
Required. The parent resource for Spec. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`spec` |  `[Spec](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Spec)`   
Required. The spec to create. This corresponds to the `spec` field on the `request` instance; if `request` is provided, this should not be set.  
`spec_id` |  ``str``   
Optional. The ID to use for the spec, which will become the final component of the spec's resource name. This field is optional. - If provided, the same will be used. The service will throw an error if the specified id is already used by another spec in the API resource. - If not provided, a system generated id will be used. This value should be 4-500 characters, overall resource name which will be of format `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}`, its length is limited to 1000 characters and valid characters are /`a-z][A-Z]`[0-9]-_/. This corresponds to the `spec_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Spec](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Spec)` | Represents a spec associated with an API version in the API Hub. Note that specs of various types can be uploaded, however parsing of details is supported for OpenAPI spec currently.  
  
### create_version
    
    
    create_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.CreateVersionRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        version: typing.Optional[google.cloud.apihub_v1.types.common_fields.Version] = None,
        version_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Version

Create an API version for an API resource in the API hub.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_create_version():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        version = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[Version](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Version.html)()
        version.display_name = "display_name_value"
    
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[CreateVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateVersionRequest.html)(
            parent="parent_value",
            version=version,
        )
    
        # Make the request
        response = await client.[create_version](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_create_version)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.CreateVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.CreateVersionRequest), dict]]`   
The request object. The CreateVersion method's request.  
`parent` |  ``str``   
Required. The parent resource for API version. Format: `projects/{project}/locations/{location}/apis/{api}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`version` |  `[Version](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Version)`   
Required. The version to create. This corresponds to the `version` field on the `request` instance; if `request` is provided, this should not be set.  
`version_id` |  ``str``   
Optional. The ID to use for the API version, which will become the final component of the version's resource name. This field is optional. - If provided, the same will be used. The service will throw an error if the specified id is already used by another version in the API resource. - If not provided, a system generated id will be used. This value should be 4-500 characters, overall resource name which will be of format `projects/{project}/locations/{location}/apis/{api}/versions/{version}`, its length is limited to 700 characters and valid characters are /`a-z][A-Z]`[0-9]-_/. This corresponds to the `version_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Version](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Version)` | Represents a version of the API resource in API hub. This is also referred to as the API version.  
  
### definition_path
    
    
    definition_path(
        project: str, location: str, api: str, version: str, definition: str
    ) -> str

Returns a fully-qualified definition string.

### delete_api
    
    
    delete_api(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.DeleteApiRequest, dict]
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
    ) -> None

Delete an API resource in the API hub. API can only be deleted if all underlying versions are deleted.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_delete_api():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[DeleteApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteApiRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_api](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_delete_api)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.DeleteApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteApiRequest), dict]]`   
The request object. The DeleteApi method's request.  
`name` |  ``str``   
Required. The name of the API resource to delete. Format: `projects/{project}/locations/{location}/apis/{api}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_api_operation
    
    
    delete_api_operation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteApiOperationRequest, dict
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
    ) -> None

Delete an operation in an API version and we can delete only the operations created via create API. If the operation was created by parsing the spec, then it can be deleted by editing or deleting the spec.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_delete_api_operation():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[DeleteApiOperationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteApiOperationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_api_operation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_delete_api_operation)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.DeleteApiOperationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteApiOperationRequest), dict]]`   
The request object. The DeleteApiOperation method's request.  
`name` |  ``str``   
Required. The name of the operation resource to delete. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_attribute
    
    
    delete_attribute(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteAttributeRequest, dict
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
    ) -> None

Delete an attribute.

Note: System defined attributes cannot be deleted. All associations of the attribute being deleted with any API hub resource will also get deleted.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_delete_attribute():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[DeleteAttributeRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteAttributeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_attribute](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_delete_attribute)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.DeleteAttributeRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteAttributeRequest), dict]]`   
The request object. The DeleteAttribute method's request.  
`name` |  ``str``   
Required. The name of the attribute to delete. Format: `projects/{project}/locations/{location}/attributes/{attribute}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_deployment
    
    
    delete_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteDeploymentRequest, dict
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
    ) -> None

Delete a deployment resource in the API hub.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_delete_deployment():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[DeleteDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteDeploymentRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_deployment](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_delete_deployment)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.DeleteDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteDeploymentRequest), dict]]`   
The request object. The DeleteDeployment method's request.  
`name` |  ``str``   
Required. The name of the deployment resource to delete. Format: `projects/{project}/locations/{location}/deployments/{deployment}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_external_api
    
    
    delete_external_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteExternalApiRequest, dict
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
    ) -> None

Delete an External API resource in the API hub.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_delete_external_api():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[DeleteExternalApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteExternalApiRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_external_api](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_delete_external_api)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.DeleteExternalApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteExternalApiRequest), dict]]`   
The request object. The DeleteExternalApi method's request.  
`name` |  ``str``   
Required. The name of the External API resource to delete. Format: `projects/{project}/locations/{location}/externalApis/{externalApi}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
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
  
### delete_spec
    
    
    delete_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteSpecRequest, dict
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
    ) -> None

Delete a spec. Deleting a spec will also delete the associated operations from the version.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_delete_spec():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[DeleteSpecRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteSpecRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_spec](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_delete_spec)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.DeleteSpecRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteSpecRequest), dict]]`   
The request object. The DeleteSpec method's request.  
`name` |  ``str``   
Required. The name of the spec to delete. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_version
    
    
    delete_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.DeleteVersionRequest, dict
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
    ) -> None

Delete an API version. Version can only be deleted if all underlying specs, operations, definitions and linked deployments are deleted.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_delete_version():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[DeleteVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteVersionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_version](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_delete_version)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.DeleteVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.DeleteVersionRequest), dict]]`   
The request object. The DeleteVersion method's request.  
`name` |  ``str``   
Required. The name of the version to delete. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### deployment_path
    
    
    deployment_path(project: str, location: str, deployment: str) -> str

Returns a fully-qualified deployment string.

### external_api_path
    
    
    external_api_path(project: str, location: str, external_api: str) -> str

Returns a fully-qualified external_api string.

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
`ApiHubAsyncClient` | The constructed client.  
  
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
`ApiHubAsyncClient` | The constructed client.  
  
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
`ApiHubAsyncClient` | The constructed client.  
  
### get_api
    
    
    get_api(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.GetApiRequest, dict]
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
    ) -> google.cloud.apihub_v1.types.common_fields.Api

Get API resource details including the API versions contained in it.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_get_api():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[GetApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetApiRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_api](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_api)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.GetApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetApiRequest), dict]]`   
The request object. The GetApi method's request.  
`name` |  ``str``   
Required. The name of the API resource to retrieve. Format: `projects/{project}/locations/{location}/apis/{api}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Api](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Api)` | An API resource in the API Hub.  
  
### get_api_operation
    
    
    get_api_operation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetApiOperationRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.ApiOperation

Get details about a particular operation in API version.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_get_api_operation():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[GetApiOperationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetApiOperationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_api_operation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_api_operation)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.GetApiOperationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetApiOperationRequest), dict]]`   
The request object. The GetApiOperation method's request.  
`name` |  ``str``   
Required. The name of the operation to retrieve. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.ApiOperation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiOperation)` | Represents an operation contained in an API version in the API Hub. An operation is added/updated/deleted in an API version when a new spec is added or an existing spec is updated/deleted in a version. Currently, an operation will be created only corresponding to OpenAPI spec as parsing is supported for OpenAPI spec. Alternatively operations can be managed via create,update and delete APIs, creation of apiOperation can be possible only for version with no parsed operations and update/delete can be possible only for operations created via create API.  
  
### get_attribute
    
    
    get_attribute(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetAttributeRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.Attribute

Get details about the attribute.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_get_attribute():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[GetAttributeRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetAttributeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_attribute](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_attribute)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.GetAttributeRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetAttributeRequest), dict]]`   
The request object. The GetAttribute method's request.  
`name` |  ``str``   
Required. The name of the attribute to retrieve. Format: `projects/{project}/locations/{location}/attributes/{attribute}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Attribute](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Attribute)` | An attribute in the API Hub. An attribute is a name value pair which can be attached to different resources in the API hub based on the scope of the attribute. Attributes can either be pre-defined by the API Hub or created by users.  
  
### get_definition
    
    
    get_definition(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetDefinitionRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.Definition

Get details about a definition in an API version.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_get_definition():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[GetDefinitionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetDefinitionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_definition](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_definition)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.GetDefinitionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetDefinitionRequest), dict]]`   
The request object. The GetDefinition method's request.  
`name` |  ``str``   
Required. The name of the definition to retrieve. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/definitions/{definition}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Definition](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Definition)` | Represents a definition for example schema, request, response definitions contained in an API version. A definition is added/updated/deleted in an API version when a new spec is added or an existing spec is updated/deleted in a version. Currently, definition will be created only corresponding to OpenAPI spec as parsing is supported for OpenAPI spec. Also, within OpenAPI spec, only schema object is supported.  
  
### get_deployment
    
    
    get_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetDeploymentRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.Deployment

Get details about a deployment and the API versions linked to it.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_get_deployment():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[GetDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetDeploymentRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_deployment](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_deployment)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.GetDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetDeploymentRequest), dict]]`   
The request object. The GetDeployment method's request.  
`name` |  ``str``   
Required. The name of the deployment resource to retrieve. Format: `projects/{project}/locations/{location}/deployments/{deployment}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Deployment](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Deployment)` | Details of the deployment where APIs are hosted. A deployment could represent an Apigee proxy, API gateway, other Google Cloud services or non-Google Cloud services as well. A deployment entity is a root level entity in the API hub and exists independent of any API.  
  
### get_external_api
    
    
    get_external_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetExternalApiRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.ExternalApi

Get details about an External API resource in the API hub.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_get_external_api():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[GetExternalApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetExternalApiRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_external_api](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_external_api)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.GetExternalApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetExternalApiRequest), dict]]`   
The request object. The GetExternalApi method's request.  
`name` |  ``str``   
Required. The name of the External API resource to retrieve. Format: `projects/{project}/locations/{location}/externalApis/{externalApi}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.ExternalApi](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ExternalApi)` | An external API represents an API being provided by external sources. This can be used to model third-party APIs and can be used to define dependencies.  
  
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
  
### get_spec
    
    
    get_spec(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.GetSpecRequest, dict]
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
    ) -> google.cloud.apihub_v1.types.common_fields.Spec

Get details about the information parsed from a spec. Note that this method does not return the raw spec contents. Use xref_GetSpecContents method to retrieve the same.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_get_spec():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[GetSpecRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetSpecRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_spec](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_spec)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.GetSpecRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetSpecRequest), dict]]`   
The request object. The GetSpec method's request.  
`name` |  ``str``   
Required. The name of the spec to retrieve. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Spec](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Spec)` | Represents a spec associated with an API version in the API Hub. Note that specs of various types can be uploaded, however parsing of details is supported for OpenAPI spec currently.  
  
### get_spec_contents
    
    
    get_spec_contents(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetSpecContentsRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.SpecContents

Get spec contents.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_get_spec_contents():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[GetSpecContentsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetSpecContentsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_spec_contents](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_spec_contents)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.GetSpecContentsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetSpecContentsRequest), dict]]`   
The request object. The GetSpecContents method's request.  
`name` |  ``str``   
Required. The name of the spec whose contents need to be retrieved. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.SpecContents](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SpecContents)` | The spec contents.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.apihub_v1.services.api_hub.transports.base.ApiHubTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### get_version
    
    
    get_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.GetVersionRequest, dict
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
    ) -> google.cloud.apihub_v1.types.common_fields.Version

Get details about the API version of an API resource. This will include information about the specs and operations present in the API version as well as the deployments linked to it.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_get_version():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[GetVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetVersionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_version](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_get_version)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.GetVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.GetVersionRequest), dict]]`   
The request object. The GetVersion method's request.  
`name` |  ``str``   
Required. The name of the API version to retrieve. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Version](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Version)` | Represents a version of the API resource in API hub. This is also referred to as the API version.  
  
### list_api_operations
    
    
    list_api_operations(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListApiOperationsRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListApiOperationsAsyncPager

List operations in an API version.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_list_api_operations():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ListApiOperationsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApiOperationsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_api_operations](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_list_api_operations)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.ListApiOperationsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApiOperationsRequest), dict]]`   
The request object. The ListApiOperations method's request.  
`parent` |  ``str``   
Required. The parent which owns this collection of operations i.e., the API version. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.services.api_hub.pagers.ListApiOperationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListApiOperationsAsyncPager)` | The ListApiOperations method's response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_apis
    
    
    list_apis(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.ListApisRequest, dict]
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListApisAsyncPager

List API resources in the API hub.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_list_apis():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ListApisRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApisRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_apis](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_list_apis)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.ListApisRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApisRequest), dict]]`   
The request object. The ListApis method's request.  
`parent` |  ``str``   
Required. The parent, which owns this collection of API resources. Format: `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.services.api_hub.pagers.ListApisAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListApisAsyncPager)` | The ListApis method's response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_attributes
    
    
    list_attributes(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListAttributesRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListAttributesAsyncPager

List all attributes.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_list_attributes():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ListAttributesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListAttributesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_attributes](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_list_attributes)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.ListAttributesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListAttributesRequest), dict]]`   
The request object. The ListAttributes method's request.  
`parent` |  ``str``   
Required. The parent resource for Attribute. Format: `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.services.api_hub.pagers.ListAttributesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListAttributesAsyncPager)` | The ListAttributes method's response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_deployments
    
    
    list_deployments(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListDeploymentsRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListDeploymentsAsyncPager

List deployment resources in the API hub.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_list_deployments():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ListDeploymentsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListDeploymentsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_deployments](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_list_deployments)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.ListDeploymentsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListDeploymentsRequest), dict]]`   
The request object. The ListDeployments method's request.  
`parent` |  ``str``   
Required. The parent, which owns this collection of deployment resources. Format: `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.services.api_hub.pagers.ListDeploymentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListDeploymentsAsyncPager)` | The ListDeployments method's response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_external_apis
    
    
    list_external_apis(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListExternalApisRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListExternalApisAsyncPager

List External API resources in the API hub.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_list_external_apis():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ListExternalApisRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListExternalApisRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_external_apis](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_list_external_apis)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.ListExternalApisRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListExternalApisRequest), dict]]`   
The request object. The ListExternalApis method's request.  
`parent` |  ``str``   
Required. The parent, which owns this collection of External API resources. Format: `projects/{project}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.services.api_hub.pagers.ListExternalApisAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListExternalApisAsyncPager)` | The ListExternalApis method's response. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### list_specs
    
    
    list_specs(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.ListSpecsRequest, dict]
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListSpecsAsyncPager

List specs corresponding to a particular API resource.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_list_specs():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ListSpecsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListSpecsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_specs](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_list_specs)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.ListSpecsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListSpecsRequest), dict]]`   
The request object. The `ListSpecs][ListSpecs]` method's request.  
`parent` |  ``str``   
Required. The parent, which owns this collection of specs. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.services.api_hub.pagers.ListSpecsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListSpecsAsyncPager)` | The ListSpecs method's response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_versions
    
    
    list_versions(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.ListVersionsRequest, dict
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
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.ListVersionsAsyncPager

List API versions of an API resource in the API hub.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_list_versions():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ListVersionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListVersionsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_versions](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_list_versions)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.ListVersionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListVersionsRequest), dict]]`   
The request object. The ListVersions method's request.  
`parent` |  ``str``   
Required. The parent which owns this collection of API versions i.e., the API resource Format: `projects/{project}/locations/{location}/apis/{api}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.services.api_hub.pagers.ListVersionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListVersionsAsyncPager)` | The ListVersions method's response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### parse_api_operation_path
    
    
    parse_api_operation_path(path: str) -> typing.Dict[str, str]

Parses a api_operation path into its component segments.

### parse_api_path
    
    
    parse_api_path(path: str) -> typing.Dict[str, str]

Parses a api path into its component segments.

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

### parse_definition_path
    
    
    parse_definition_path(path: str) -> typing.Dict[str, str]

Parses a definition path into its component segments.

### parse_deployment_path
    
    
    parse_deployment_path(path: str) -> typing.Dict[str, str]

Parses a deployment path into its component segments.

### parse_external_api_path
    
    
    parse_external_api_path(path: str) -> typing.Dict[str, str]

Parses a external_api path into its component segments.

### parse_plugin_instance_path
    
    
    parse_plugin_instance_path(path: str) -> typing.Dict[str, str]

Parses a plugin_instance path into its component segments.

### parse_spec_path
    
    
    parse_spec_path(path: str) -> typing.Dict[str, str]

Parses a spec path into its component segments.

### parse_version_path
    
    
    parse_version_path(path: str) -> typing.Dict[str, str]

Parses a version path into its component segments.

### plugin_instance_path
    
    
    plugin_instance_path(
        project: str, location: str, plugin: str, instance: str
    ) -> str

Returns a fully-qualified plugin_instance string.

### search_resources
    
    
    search_resources(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.SearchResourcesRequest, dict
            ]
        ] = None,
        *,
        location: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.services.api_hub.pagers.SearchResourcesAsyncPager

Search across API-Hub resources.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_search_resources():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[SearchResourcesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SearchResourcesRequest.html)(
            location="location_value",
            query="query_value",
        )
    
        # Make the request
        page_result = client.[search_resources](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_search_resources)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.SearchResourcesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SearchResourcesRequest), dict]]`   
The request object. The SearchResources method's request.  
`location` |  ``str``   
Required. The resource name of the location which will be of the type `projects/{project_id}/locations/{location_id}`. This field is used to identify the instance of API-Hub in which resources should be searched. This corresponds to the `location` field on the `request` instance; if `request` is provided, this should not be set.  
`query` |  ``str``   
Required. The free text search query. This query can contain keywords which could be related to any detail of the API-Hub resources such display names, descriptions, attributes etc. This corresponds to the `query` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.services.api_hub.pagers.SearchResourcesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.SearchResourcesAsyncPager)` | Response for the SearchResources method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### spec_path
    
    
    spec_path(project: str, location: str, api: str, version: str, spec: str) -> str

Returns a fully-qualified spec string.

### update_api
    
    
    update_api(
        request: typing.Optional[
            typing.Union[google.cloud.apihub_v1.types.apihub_service.UpdateApiRequest, dict]
        ] = None,
        *,
        api: typing.Optional[google.cloud.apihub_v1.types.common_fields.Api] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Api

Update an API resource in the API hub. The following fields in the xref_API can be updated:

  * xref_display_name
  * xref_description
  * xref_owner
  * xref_documentation
  * xref_target_user
  * xref_team
  * xref_business_unit
  * xref_maturity_level
  * xref_api_style
  * xref_attributes



The xref_update_mask should be used to specify the fields being updated.

Updating the owner field requires complete owner message and updates both owner and email fields.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_update_api():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        api = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[Api](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Api.html)()
        api.display_name = "display_name_value"
    
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[UpdateApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateApiRequest.html)(
            api=api,
        )
    
        # Make the request
        response = await client.[update_api](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_update_api)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.UpdateApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateApiRequest), dict]]`   
The request object. The UpdateApi method's request.  
`api` |  `[Api](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Api)`   
Required. The API resource to update. The API resource's `name` field is used to identify the API resource to update. Format: `projects/{project}/locations/{location}/apis/{api}` This corresponds to the `api` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. The list of fields to update. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Api](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Api)` | An API resource in the API Hub.  
  
### update_api_operation
    
    
    update_api_operation(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateApiOperationRequest, dict
            ]
        ] = None,
        *,
        api_operation: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.ApiOperation
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
    ) -> google.cloud.apihub_v1.types.common_fields.ApiOperation

Update an operation in an API version. The following fields in the xref_ApiOperation resource can be updated:

  * `details.description][ApiOperation.details.description]`
  * `details.documentation][ApiOperation.details.documentation]`
  * `details.http_operation.path][ApiOperation.details.http_operation.path.path]`
  * `details.http_operation.method][ApiOperation.details.http_operation.method]`
  * `details.deprecated][ApiOperation.details.deprecated]`
  * xref_attributes



The xref_update_mask should be used to specify the fields being updated.

An operation can be updated only if the operation was created via xref_CreateApiOperation API. If the operation was created by parsing the spec, then it can be edited by updating the spec.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_update_api_operation():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[UpdateApiOperationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateApiOperationRequest.html)(
        )
    
        # Make the request
        response = await client.[update_api_operation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_update_api_operation)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.UpdateApiOperationRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateApiOperationRequest), dict]]`   
The request object. The UpdateApiOperation method's request.  
`api_operation` |  `[ApiOperation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiOperation)`   
Required. The apiOperation resource to update. The operation resource's `name` field is used to identify the operation resource to update. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}` This corresponds to the `api_operation` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. The list of fields to update. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.ApiOperation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiOperation)` | Represents an operation contained in an API version in the API Hub. An operation is added/updated/deleted in an API version when a new spec is added or an existing spec is updated/deleted in a version. Currently, an operation will be created only corresponding to OpenAPI spec as parsing is supported for OpenAPI spec. Alternatively operations can be managed via create,update and delete APIs, creation of apiOperation can be possible only for version with no parsed operations and update/delete can be possible only for operations created via create API.  
  
### update_attribute
    
    
    update_attribute(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateAttributeRequest, dict
            ]
        ] = None,
        *,
        attribute: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.Attribute
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
    ) -> google.cloud.apihub_v1.types.common_fields.Attribute

Update the attribute. The following fields in the [Attribute resource][google.cloud.apihub.v1.Attribute] can be updated:

  * xref_display_name The display name can be updated for user defined attributes only.
  * xref_description The description can be updated for user defined attributes only.
  * xref_allowed_values To update the list of allowed values, clients need to use the fetched list of allowed values and add or remove values to or from the same list. The mutable allowed values can be updated for both user defined and System defined attributes. The immutable allowed values cannot be updated or deleted. The updated list of allowed values cannot be empty. If an allowed value that is already used by some resource's attribute is deleted, then the association between the resource and the attribute value will also be deleted.
  * xref_cardinality The cardinality can be updated for user defined attributes only. Cardinality can only be increased during an update.



The xref_update_mask should be used to specify the fields being updated.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_update_attribute():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        attribute = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[Attribute](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Attribute.html)()
        attribute.display_name = "display_name_value"
        attribute.scope = "PLUGIN"
        attribute.data_type = "URI"
    
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[UpdateAttributeRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateAttributeRequest.html)(
            attribute=attribute,
        )
    
        # Make the request
        response = await client.[update_attribute](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_update_attribute)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.UpdateAttributeRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateAttributeRequest), dict]]`   
The request object. The UpdateAttribute method's request.  
`attribute` |  `[Attribute](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Attribute)`   
Required. The attribute to update. The attribute's `name` field is used to identify the attribute to update. Format: `projects/{project}/locations/{location}/attributes/{attribute}` This corresponds to the `attribute` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. The list of fields to update. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Attribute](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Attribute)` | An attribute in the API Hub. An attribute is a name value pair which can be attached to different resources in the API hub based on the scope of the attribute. Attributes can either be pre-defined by the API Hub or created by users.  
  
### update_deployment
    
    
    update_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateDeploymentRequest, dict
            ]
        ] = None,
        *,
        deployment: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.Deployment
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
    ) -> google.cloud.apihub_v1.types.common_fields.Deployment

Update a deployment resource in the API hub. The following fields in the [deployment resource][google.cloud.apihub.v1.Deployment] can be updated:

  * xref_display_name
  * xref_description
  * xref_documentation
  * xref_deployment_type
  * xref_resource_uri
  * xref_endpoints
  * xref_slo
  * xref_environment
  * xref_attributes
  * [source_project] [google.cloud.apihub.v1.Deployment.source_project]
  * [source_environment] [google.cloud.apihub.v1.Deployment.source_environment]
  * xref_management_url
  * xref_source_uri The xref_update_mask should be used to specify the fields being updated.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_update_deployment():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        deployment = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[Deployment](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Deployment.html)()
        deployment.display_name = "display_name_value"
        deployment.deployment_type.enum_values.values.id = "id_value"
        deployment.deployment_type.enum_values.values.display_name = "display_name_value"
        deployment.resource_uri = "resource_uri_value"
        deployment.endpoints = ['endpoints_value1', 'endpoints_value2']
    
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[UpdateDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateDeploymentRequest.html)(
            deployment=deployment,
        )
    
        # Make the request
        response = await client.[update_deployment](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_update_deployment)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.UpdateDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateDeploymentRequest), dict]]`   
The request object. The UpdateDeployment method's request.  
`deployment` |  `[Deployment](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Deployment)`   
Required. The deployment resource to update. The deployment resource's `name` field is used to identify the deployment resource to update. Format: `projects/{project}/locations/{location}/deployments/{deployment}` This corresponds to the `deployment` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. The list of fields to update. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Deployment](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Deployment)` | Details of the deployment where APIs are hosted. A deployment could represent an Apigee proxy, API gateway, other Google Cloud services or non-Google Cloud services as well. A deployment entity is a root level entity in the API hub and exists independent of any API.  
  
### update_external_api
    
    
    update_external_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateExternalApiRequest, dict
            ]
        ] = None,
        *,
        external_api: typing.Optional[
            google.cloud.apihub_v1.types.common_fields.ExternalApi
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
    ) -> google.cloud.apihub_v1.types.common_fields.ExternalApi

Update an External API resource in the API hub. The following fields can be updated:

  * xref_display_name
  * xref_description
  * xref_documentation
  * xref_endpoints
  * xref_paths



The xref_update_mask should be used to specify the fields being updated.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_update_external_api():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        external_api = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ExternalApi](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ExternalApi.html)()
        external_api.display_name = "display_name_value"
    
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[UpdateExternalApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateExternalApiRequest.html)(
            external_api=external_api,
        )
    
        # Make the request
        response = await client.[update_external_api](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_update_external_api)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.UpdateExternalApiRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateExternalApiRequest), dict]]`   
The request object. The UpdateExternalApi method's request.  
`external_api` |  `[ExternalApi](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ExternalApi)`   
Required. The External API resource to update. The External API resource's `name` field is used to identify the External API resource to update. Format: `projects/{project}/locations/{location}/externalApis/{externalApi}` This corresponds to the `external_api` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. The list of fields to update. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.ExternalApi](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ExternalApi)` | An external API represents an API being provided by external sources. This can be used to model third-party APIs and can be used to define dependencies.  
  
### update_spec
    
    
    update_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateSpecRequest, dict
            ]
        ] = None,
        *,
        spec: typing.Optional[google.cloud.apihub_v1.types.common_fields.Spec] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Spec

Update spec. The following fields in the xref_spec can be updated:

  * xref_display_name
  * xref_source_uri
  * xref_lint_response
  * xref_attributes
  * xref_contents
  * xref_spec_type



In case of an OAS spec, updating spec contents can lead to:

  1. Creation, deletion and update of operations.
  2. Creation, deletion and update of definitions.
  3. Update of other info parsed out from the new spec.



In case of contents or source_uri being present in update mask, spec_type must also be present. Also, spec_type can not be present in update mask if contents or source_uri is not present.

The xref_update_mask should be used to specify the fields being updated.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_update_spec():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        spec = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[Spec](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Spec.html)()
        spec.display_name = "display_name_value"
        spec.spec_type.enum_values.values.id = "id_value"
        spec.spec_type.enum_values.values.display_name = "display_name_value"
    
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[UpdateSpecRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateSpecRequest.html)(
            spec=spec,
        )
    
        # Make the request
        response = await client.[update_spec](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_update_spec)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.UpdateSpecRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateSpecRequest), dict]]`   
The request object. The UpdateSpec method's request.  
`spec` |  `[Spec](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Spec)`   
Required. The spec to update. The spec's `name` field is used to identify the spec to update. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}` This corresponds to the `spec` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. The list of fields to update. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Spec](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Spec)` | Represents a spec associated with an API version in the API Hub. Note that specs of various types can be uploaded, however parsing of details is supported for OpenAPI spec currently.  
  
### update_version
    
    
    update_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apihub_v1.types.apihub_service.UpdateVersionRequest, dict
            ]
        ] = None,
        *,
        version: typing.Optional[google.cloud.apihub_v1.types.common_fields.Version] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apihub_v1.types.common_fields.Version

Update API version. The following fields in the xref_version can be updated currently:

  * xref_display_name
  * xref_description
  * xref_documentation
  * xref_deployments
  * xref_lifecycle
  * xref_compliance
  * xref_accreditation
  * xref_attributes



The xref_update_mask should be used to specify the fields being updated.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest)
    
    async def sample_update_version():
        # Create a client
        client = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[ApiHubAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html)()
    
        # Initialize request argument(s)
        version = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[Version](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Version.html)()
        version.display_name = "display_name_value"
    
        request = [apihub_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest).[UpdateVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateVersionRequest.html)(
            version=version,
        )
    
        # Make the request
        response = await client.[update_version](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.ApiHubAsyncClient.html#google_cloud_apihub_v1_services_api_hub_ApiHubAsyncClient_update_version)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.apihub_v1.types.UpdateVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.UpdateVersionRequest), dict]]`   
The request object. The UpdateVersion method's request.  
`version` |  `[Version](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Version)`   
Required. The API version to update. The version's `name` field is used to identify the API version to update. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}` This corresponds to the `version` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. The list of fields to update. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.apihub_v1.types.Version](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Version)` | Represents a version of the API resource in API hub. This is also referred to as the API version.  
  
### version_path
    
    
    version_path(project: str, location: str, api: str, version: str) -> str

Returns a fully-qualified version string.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
