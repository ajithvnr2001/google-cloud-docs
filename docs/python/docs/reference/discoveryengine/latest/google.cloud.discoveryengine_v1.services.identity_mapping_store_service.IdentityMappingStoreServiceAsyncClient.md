---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient
title: Class IdentityMappingStoreServiceAsyncClient (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:00:08.849331+00:00
---

# Class IdentityMappingStoreServiceAsyncClient (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class IdentityMappingStoreServiceAsyncClient (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    IdentityMappingStoreServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.discoveryengine_v1.services.identity_mapping_store_service.transports.base.IdentityMappingStoreServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.discoveryengine_v1.services.identity_mapping_store_service.transports.base.IdentityMappingStoreServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service for managing Identity Mapping Stores.

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
`IdentityMappingStoreServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### IdentityMappingStoreServiceAsyncClient
    
    
    IdentityMappingStoreServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.discoveryengine_v1.services.identity_mapping_store_service.transports.base.IdentityMappingStoreServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.discoveryengine_v1.services.identity_mapping_store_service.transports.base.IdentityMappingStoreServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the identity mapping store service async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,IdentityMappingStoreServiceTransport,Callable[..., IdentityMappingStoreServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the IdentityMappingStoreServiceTransport constructor. If set to None, a transport is chosen automatically.  
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
  
### cmek_config_path
    
    
    cmek_config_path(project: str, location: str) -> str

Returns a fully-qualified cmek_config string.

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

### create_identity_mapping_store
    
    
    create_identity_mapping_store(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.identity_mapping_store_service.CreateIdentityMappingStoreRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        identity_mapping_store: typing.Optional[
            google.cloud.discoveryengine_v1.types.identity_mapping_store.IdentityMappingStore
        ] = None,
        identity_mapping_store_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.discoveryengine_v1.types.identity_mapping_store.IdentityMappingStore

Creates a new Identity Mapping Store.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest)
    
    async def sample_create_identity_mapping_store():
        # Create a client
        client = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[IdentityMappingStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[CreateIdentityMappingStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateIdentityMappingStoreRequest.html)(
            cmek_config_name="cmek_config_name_value",
            parent="parent_value",
            identity_mapping_store_id="identity_mapping_store_id_value",
        )
    
        # Make the request
        response = await client.[create_identity_mapping_store](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient.html#google_cloud_discoveryengine_v1_services_identity_mapping_store_service_IdentityMappingStoreServiceAsyncClient_create_identity_mapping_store)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.discoveryengine_v1.types.CreateIdentityMappingStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateIdentityMappingStoreRequest), dict]]`   
The request object. Request message for IdentityMappingStoreService.CreateIdentityMappingStore  
`parent` |  ``str``   
Required. The parent collection resource name, such as `projects/{project}/locations/{location}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`identity_mapping_store` |  `[IdentityMappingStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.IdentityMappingStore)`   
Required. The Identity Mapping Store to create. This corresponds to the `identity_mapping_store` field on the `request` instance; if `request` is provided, this should not be set.  
`identity_mapping_store_id` |  ``str``   
Required. The ID of the Identity Mapping Store to create. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 63 characters. This corresponds to the `identity_mapping_store_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.types.IdentityMappingStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.IdentityMappingStore)` | Identity Mapping Store which contains Identity Mapping Entries.  
  
### crypto_key_versions_path
    
    
    crypto_key_versions_path(
        project: str, location: str, key_ring: str, crypto_key: str, crypto_key_version: str
    ) -> str

Returns a fully-qualified crypto_key_versions string.

### crypto_keys_path
    
    
    crypto_keys_path(
        project: str, location: str, key_ring: str, crypto_key: str
    ) -> str

Returns a fully-qualified crypto_keys string.

### delete_identity_mapping_store
    
    
    delete_identity_mapping_store(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.identity_mapping_store_service.DeleteIdentityMappingStoreRequest,
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

Deletes the Identity Mapping Store.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest)
    
    async def sample_delete_identity_mapping_store():
        # Create a client
        client = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[IdentityMappingStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[DeleteIdentityMappingStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteIdentityMappingStoreRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_identity_mapping_store](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient.html#google_cloud_discoveryengine_v1_services_identity_mapping_store_service_IdentityMappingStoreServiceAsyncClient_delete_identity_mapping_store)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.discoveryengine_v1.types.DeleteIdentityMappingStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteIdentityMappingStoreRequest), dict]]`   
The request object. Request message for IdentityMappingStoreService.DeleteIdentityMappingStore  
`name` |  ``str``   
Required. The name of the Identity Mapping Store to delete. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
`IdentityMappingStoreServiceAsyncClient` | The constructed client.  
  
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
`IdentityMappingStoreServiceAsyncClient` | The constructed client.  
  
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
`IdentityMappingStoreServiceAsyncClient` | The constructed client.  
  
### get_identity_mapping_store
    
    
    get_identity_mapping_store(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.identity_mapping_store_service.GetIdentityMappingStoreRequest,
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
    ) -> google.cloud.discoveryengine_v1.types.identity_mapping_store.IdentityMappingStore

Gets the Identity Mapping Store.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest)
    
    async def sample_get_identity_mapping_store():
        # Create a client
        client = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[IdentityMappingStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[GetIdentityMappingStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetIdentityMappingStoreRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_identity_mapping_store](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient.html#google_cloud_discoveryengine_v1_services_identity_mapping_store_service_IdentityMappingStoreServiceAsyncClient_get_identity_mapping_store)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.discoveryengine_v1.types.GetIdentityMappingStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetIdentityMappingStoreRequest), dict]]`   
The request object. Request message for IdentityMappingStoreService.GetIdentityMappingStore  
`name` |  ``str``   
Required. The name of the Identity Mapping Store to get. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.types.IdentityMappingStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.IdentityMappingStore)` | Identity Mapping Store which contains Identity Mapping Entries.  
  
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
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.discoveryengine_v1.services.identity_mapping_store_service.transports.base.IdentityMappingStoreServiceTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### identity_mapping_store_path
    
    
    identity_mapping_store_path(
        project: str, location: str, identity_mapping_store: str
    ) -> str

Returns a fully-qualified identity_mapping_store string.

### import_identity_mappings
    
    
    import_identity_mappings(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.identity_mapping_store_service.ImportIdentityMappingsRequest,
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

Imports a list of Identity Mapping Entries to an Identity Mapping Store.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest)
    
    async def sample_import_identity_mappings():
        # Create a client
        client = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[IdentityMappingStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[ImportIdentityMappingsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportIdentityMappingsRequest.html)(
            identity_mapping_store="identity_mapping_store_value",
        )
    
        # Make the request
        operation = await client.[import_identity_mappings](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient.html#google_cloud_discoveryengine_v1_services_identity_mapping_store_service_IdentityMappingStoreServiceAsyncClient_import_identity_mappings)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.discoveryengine_v1.types.ImportIdentityMappingsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportIdentityMappingsRequest), dict]]`   
The request object. Request message for IdentityMappingStoreService.ImportIdentityMappings  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [ImportIdentityMappingsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportIdentityMappingsResponse) Response message for IdentityMappingStoreService.ImportIdentityMappings  
  
### list_identity_mapping_stores
    
    
    list_identity_mapping_stores(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.identity_mapping_store_service.ListIdentityMappingStoresRequest,
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
        google.cloud.discoveryengine_v1.services.identity_mapping_store_service.pagers.ListIdentityMappingStoresAsyncPager
    )

Lists all Identity Mapping Stores.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest)
    
    async def sample_list_identity_mapping_stores():
        # Create a client
        client = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[IdentityMappingStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[ListIdentityMappingStoresRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListIdentityMappingStoresRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_identity_mapping_stores](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient.html#google_cloud_discoveryengine_v1_services_identity_mapping_store_service_IdentityMappingStoreServiceAsyncClient_list_identity_mapping_stores)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.discoveryengine_v1.types.ListIdentityMappingStoresRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListIdentityMappingStoresRequest), dict]]`   
The request object. Request message for IdentityMappingStoreService.ListIdentityMappingStores  
`parent` |  ``str``   
Required. The parent of the Identity Mapping Stores to list. Format: `projects/{project}/locations/{location}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.services.identity_mapping_store_service.pagers.ListIdentityMappingStoresAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.pagers.ListIdentityMappingStoresAsyncPager)` | Response message for IdentityMappingStoreService.ListIdentityMappingStores Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_identity_mappings
    
    
    list_identity_mappings(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.identity_mapping_store_service.ListIdentityMappingsRequest,
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
    ) -> (
        google.cloud.discoveryengine_v1.services.identity_mapping_store_service.pagers.ListIdentityMappingsAsyncPager
    )

Lists Identity Mappings in an Identity Mapping Store.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest)
    
    async def sample_list_identity_mappings():
        # Create a client
        client = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[IdentityMappingStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[ListIdentityMappingsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListIdentityMappingsRequest.html)(
            identity_mapping_store="identity_mapping_store_value",
        )
    
        # Make the request
        page_result = client.[list_identity_mappings](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient.html#google_cloud_discoveryengine_v1_services_identity_mapping_store_service_IdentityMappingStoreServiceAsyncClient_list_identity_mappings)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.discoveryengine_v1.types.ListIdentityMappingsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListIdentityMappingsRequest), dict]]`   
The request object. Request message for IdentityMappingStoreService.ListIdentityMappings  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.services.identity_mapping_store_service.pagers.ListIdentityMappingsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.pagers.ListIdentityMappingsAsyncPager)` | Response message for IdentityMappingStoreService.ListIdentityMappings Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### location_path
    
    
    location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

### parse_cmek_config_path
    
    
    parse_cmek_config_path(path: str) -> typing.Dict[str, str]

Parses a cmek_config path into its component segments.

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

### parse_crypto_key_versions_path
    
    
    parse_crypto_key_versions_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key_versions path into its component segments.

### parse_crypto_keys_path
    
    
    parse_crypto_keys_path(path: str) -> typing.Dict[str, str]

Parses a crypto_keys path into its component segments.

### parse_identity_mapping_store_path
    
    
    parse_identity_mapping_store_path(path: str) -> typing.Dict[str, str]

Parses a identity_mapping_store path into its component segments.

### parse_location_path
    
    
    parse_location_path(path: str) -> typing.Dict[str, str]

Parses a location path into its component segments.

### purge_identity_mappings
    
    
    purge_identity_mappings(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.identity_mapping_store_service.PurgeIdentityMappingsRequest,
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

Purges specified or all Identity Mapping Entries from an Identity Mapping Store.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest)
    
    async def sample_purge_identity_mappings():
        # Create a client
        client = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[IdentityMappingStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [discoveryengine_v1](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest).[PurgeIdentityMappingsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeIdentityMappingsRequest.html)(
            identity_mapping_store="identity_mapping_store_value",
        )
    
        # Make the request
        operation = await client.[purge_identity_mappings](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient.html#google_cloud_discoveryengine_v1_services_identity_mapping_store_service_IdentityMappingStoreServiceAsyncClient_purge_identity_mappings)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.discoveryengine_v1.types.PurgeIdentityMappingsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeIdentityMappingsRequest), dict]]`   
The request object. Request message for IdentityMappingStoreService.PurgeIdentityMappings  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
