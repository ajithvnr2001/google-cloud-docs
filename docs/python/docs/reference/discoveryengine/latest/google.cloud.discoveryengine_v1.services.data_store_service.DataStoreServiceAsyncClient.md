---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceAsyncClient
title: Class DataStoreServiceAsyncClient (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:59:57.876343+00:00
---

# Class DataStoreServiceAsyncClient (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DataStoreServiceAsyncClient (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    DataStoreServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.discoveryengine_v1.services.data_store_service.transports.base.DataStoreServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.discoveryengine_v1.services.data_store_service.transports.base.DataStoreServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service for managing DataStore configuration.

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
`DataStoreServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### DataStoreServiceAsyncClient
    
    
    DataStoreServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.discoveryengine_v1.services.data_store_service.transports.base.DataStoreServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.discoveryengine_v1.services.data_store_service.transports.base.DataStoreServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data store service async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,DataStoreServiceTransport,Callable[..., DataStoreServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the DataStoreServiceTransport constructor. If set to None, a transport is chosen automatically.  
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

### collection_path
    
    
    collection_path(project: str, location: str, collection: str) -> str

Returns a fully-qualified collection string.

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

### create_data_store
    
    
    create_data_store(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.data_store_service.CreateDataStoreRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_store: typing.Optional[
            google.cloud.discoveryengine_v1.types.data_store.DataStore
        ] = None,
        data_store_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a xref_DataStore.

DataStore is for storing xref_Documents. To serve these documents for Search, or Recommendation use case, an xref_Engine needs to be created separately.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    async def sample_create_data_store():
        # Create a client
        client = discoveryengine_v1.[DataStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        data_store = discoveryengine_v1.[DataStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DataStore.html)()
        data_store.display_name = "display_name_value"
    
        request = discoveryengine_v1.[CreateDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateDataStoreRequest.html)(
            cmek_config_name="cmek_config_name_value",
            parent="parent_value",
            data_store=data_store,
            data_store_id="data_store_id_value",
        )
    
        # Make the request
        operation = await client.[create_data_store](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceAsyncClient.html#google_cloud_discoveryengine_v1_services_data_store_service_DataStoreServiceAsyncClient_create_data_store)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.discoveryengine_v1.types.CreateDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateDataStoreRequest), dict]]`   
The request object. Request for DataStoreService.CreateDataStore method.  
`parent` |  ``str``   
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`data_store` |  `DataStore`   
Required. The DataStore to create. This corresponds to the `data_store` field on the `request` instance; if `request` is provided, this should not be set.  
`data_store_id` |  ``str``   
Required. The ID to use for the DataStore, which will become the final component of the DataStore's resource name. This field must conform to `RFC-1034 <https://tools.ietf.org/html/rfc1034>`__ standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned. This corresponds to the `data_store_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be DataStore DataStore captures global settings and configs at the DataStore level.  
  
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

### data_store_path
    
    
    data_store_path(project: str, location: str, data_store: str) -> str

Returns a fully-qualified data_store string.

### delete_data_store
    
    
    delete_data_store(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.data_store_service.DeleteDataStoreRequest,
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

Deletes a xref_DataStore.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    async def sample_delete_data_store():
        # Create a client
        client = discoveryengine_v1.[DataStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[DeleteDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteDataStoreRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_data_store](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceAsyncClient.html#google_cloud_discoveryengine_v1_services_data_store_service_DataStoreServiceAsyncClient_delete_data_store)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.discoveryengine_v1.types.DeleteDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteDataStoreRequest), dict]]`   
The request object. Request message for DataStoreService.DeleteDataStore method.  
`name` |  ``str``   
Required. Full resource name of DataStore, such as `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}`. If the caller does not have permission to delete the DataStore, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the DataStore to delete does not exist, a NOT_FOUND error is returned. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### document_processing_config_path
    
    
    document_processing_config_path(
        project: str, location: str, data_store: str
    ) -> str

Returns a fully-qualified document_processing_config string.

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
`DataStoreServiceAsyncClient` | The constructed client.  
  
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
`DataStoreServiceAsyncClient` | The constructed client.  
  
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
`DataStoreServiceAsyncClient` | The constructed client.  
  
### get_data_store
    
    
    get_data_store(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.data_store_service.GetDataStoreRequest,
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
    ) -> google.cloud.discoveryengine_v1.types.data_store.DataStore

Gets a xref_DataStore.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    async def sample_get_data_store():
        # Create a client
        client = discoveryengine_v1.[DataStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[GetDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetDataStoreRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_data_store](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceAsyncClient.html#google_cloud_discoveryengine_v1_services_data_store_service_DataStoreServiceAsyncClient_get_data_store)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.discoveryengine_v1.types.GetDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetDataStoreRequest), dict]]`   
The request object. Request message for DataStoreService.GetDataStore method.  
`name` |  ``str``   
Required. Full resource name of DataStore, such as `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}`. If the caller does not have permission to access the DataStore, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the requested DataStore does not exist, a NOT_FOUND error is returned. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.types.DataStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DataStore)` | DataStore captures global settings and configs at the DataStore level.  
  
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
        google.cloud.discoveryengine_v1.services.data_store_service.transports.base.DataStoreServiceTransport
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

### list_data_stores
    
    
    list_data_stores(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.data_store_service.ListDataStoresRequest,
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
        google.cloud.discoveryengine_v1.services.data_store_service.pagers.ListDataStoresAsyncPager
    )

Lists all the xref_DataStores associated with the project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    async def sample_list_data_stores():
        # Create a client
        client = discoveryengine_v1.[DataStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = discoveryengine_v1.[ListDataStoresRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListDataStoresRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_data_stores](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceAsyncClient.html#google_cloud_discoveryengine_v1_services_data_store_service_DataStoreServiceAsyncClient_list_data_stores)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.discoveryengine_v1.types.ListDataStoresRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListDataStoresRequest), dict]]`   
The request object. Request message for DataStoreService.ListDataStores method.  
`parent` |  ``str``   
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection_id}`. If the caller does not have permission to list DataStores under this location, regardless of whether or not this data store exists, a PERMISSION_DENIED error is returned. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.services.data_store_service.pagers.ListDataStoresAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.pagers.ListDataStoresAsyncPager)` | Response message for DataStoreService.ListDataStores method. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### parse_cmek_config_path
    
    
    parse_cmek_config_path(path: str) -> typing.Dict[str, str]

Parses a cmek_config path into its component segments.

### parse_collection_path
    
    
    parse_collection_path(path: str) -> typing.Dict[str, str]

Parses a collection path into its component segments.

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

### parse_data_store_path
    
    
    parse_data_store_path(path: str) -> typing.Dict[str, str]

Parses a data_store path into its component segments.

### parse_document_processing_config_path
    
    
    parse_document_processing_config_path(path: str) -> typing.Dict[str, str]

Parses a document_processing_config path into its component segments.

### parse_identity_mapping_store_path
    
    
    parse_identity_mapping_store_path(path: str) -> typing.Dict[str, str]

Parses a identity_mapping_store path into its component segments.

### parse_schema_path
    
    
    parse_schema_path(path: str) -> typing.Dict[str, str]

Parses a schema path into its component segments.

### schema_path
    
    
    schema_path(project: str, location: str, data_store: str, schema: str) -> str

Returns a fully-qualified schema string.

### update_data_store
    
    
    update_data_store(
        request: typing.Optional[
            typing.Union[
                google.cloud.discoveryengine_v1.types.data_store_service.UpdateDataStoreRequest,
                dict,
            ]
        ] = None,
        *,
        data_store: typing.Optional[
            google.cloud.discoveryengine_v1.types.data_store.DataStore
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
    ) -> google.cloud.discoveryengine_v1.types.data_store.DataStore

Updates a xref_DataStore
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import discoveryengine_v1
    
    async def sample_update_data_store():
        # Create a client
        client = discoveryengine_v1.[DataStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        data_store = discoveryengine_v1.[DataStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DataStore.html)()
        data_store.display_name = "display_name_value"
    
        request = discoveryengine_v1.[UpdateDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateDataStoreRequest.html)(
            data_store=data_store,
        )
    
        # Make the request
        response = await client.[update_data_store](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceAsyncClient.html#google_cloud_discoveryengine_v1_services_data_store_service_DataStoreServiceAsyncClient_update_data_store)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.discoveryengine_v1.types.UpdateDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateDataStoreRequest), dict]]`   
The request object. Request message for DataStoreService.UpdateDataStore method.  
`data_store` |  `DataStore`   
Required. The DataStore to update. If the caller does not have permission to update the DataStore, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the DataStore to update does not exist, a NOT_FOUND error is returned. This corresponds to the `data_store` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Indicates which fields in the provided DataStore to update. If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.discoveryengine_v1.types.DataStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DataStore)` | DataStore captures global settings and configs at the DataStore level.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
