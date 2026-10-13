---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient
title: Class DataObjectServiceAsyncClient (0.11.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:10:32.974441+00:00
---

# Class DataObjectServiceAsyncClient (0.11.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DataObjectServiceAsyncClient (0.11.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.5 (latest)  0.11.4  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    DataObjectServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.vectorsearch_v1.services.data_object_service.transports.base.DataObjectServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.vectorsearch_v1.services.data_object_service.transports.base.DataObjectServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service for creating and managing data objects.

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
`DataObjectServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### DataObjectServiceAsyncClient
    
    
    DataObjectServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.vectorsearch_v1.services.data_object_service.transports.base.DataObjectServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.vectorsearch_v1.services.data_object_service.transports.base.DataObjectServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data object service async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,DataObjectServiceTransport,Callable[..., DataObjectServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the DataObjectServiceTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### batch_create_data_objects
    
    
    batch_create_data_objects(
        request: typing.Optional[
            typing.Union[
                google.cloud.vectorsearch_v1.types.data_object_service.BatchCreateDataObjectsRequest,
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
        google.cloud.vectorsearch_v1.types.data_object_service.BatchCreateDataObjectsResponse
    )

Creates a batch of dataObjects.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest)
    
    async def sample_batch_create_data_objects():
        # Create a client
        client = [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest).[DataObjectServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        requests = [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest).[CreateDataObjectRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.CreateDataObjectRequest.html)()
        requests.parent = "parent_value"
        requests.data_object_id = "data_object_id_value"
    
        request = [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest).[BatchCreateDataObjectsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.BatchCreateDataObjectsRequest.html)(
            parent="parent_value",
            requests=requests,
        )
    
        # Make the request
        response = await client.[batch_create_data_objects](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient.html#google_cloud_vectorsearch_v1_services_data_object_service_DataObjectServiceAsyncClient_batch_create_data_objects)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vectorsearch_v1.types.BatchCreateDataObjectsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.BatchCreateDataObjectsRequest), dict]]`   
The request object. Request message for DataObjectService.BatchCreateDataObjects.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vectorsearch_v1.types.BatchCreateDataObjectsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.BatchCreateDataObjectsResponse)` | Response message for DataObjectService.BatchCreateDataObjects.  
  
### batch_delete_data_objects
    
    
    batch_delete_data_objects(
        request: typing.Optional[
            typing.Union[
                google.cloud.vectorsearch_v1.types.data_object_service.BatchDeleteDataObjectsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        requests: typing.Optional[
            typing.MutableSequence[
                google.cloud.vectorsearch_v1.types.data_object_service.DeleteDataObjectRequest
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
    ) -> None

Deletes dataObjects in a batch.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest)
    
    async def sample_batch_delete_data_objects():
        # Create a client
        client = [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest).[DataObjectServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        requests = [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest).[DeleteDataObjectRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.DeleteDataObjectRequest.html)()
        requests.name = "name_value"
    
        request = [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest).[BatchDeleteDataObjectsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.BatchDeleteDataObjectsRequest.html)(
            parent="parent_value",
            requests=requests,
        )
    
        # Make the request
        await client.[batch_delete_data_objects](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient.html#google_cloud_vectorsearch_v1_services_data_object_service_DataObjectServiceAsyncClient_batch_delete_data_objects)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vectorsearch_v1.types.BatchDeleteDataObjectsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.BatchDeleteDataObjectsRequest), dict]]`   
The request object. Request message for DataObjectService.BatchDeleteDataObjects.  
`parent` |  ``str``   
Required. The resource name of the Collection to delete the DataObjects in. Format: `projects/{project}/locations/{location}/collections/{collection}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`requests` |  `:class:`MutableSequence[[google.cloud.vectorsearch_v1.types.DeleteDataObjectRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.DeleteDataObjectRequest)]``   
Required. The request message specifying the resources to delete. A maximum of 1000 DataObjects can be deleted in a batch. This corresponds to the `requests` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### batch_update_data_objects
    
    
    batch_update_data_objects(
        request: typing.Optional[
            typing.Union[
                google.cloud.vectorsearch_v1.types.data_object_service.BatchUpdateDataObjectsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        requests: typing.Optional[
            typing.MutableSequence[
                google.cloud.vectorsearch_v1.types.data_object_service.UpdateDataObjectRequest
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
    ) -> (
        google.cloud.vectorsearch_v1.types.data_object_service.BatchUpdateDataObjectsResponse
    )

Updates dataObjects in a batch.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest)
    
    async def sample_batch_update_data_objects():
        # Create a client
        client = [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest).[DataObjectServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest).[BatchUpdateDataObjectsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.BatchUpdateDataObjectsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[batch_update_data_objects](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient.html#google_cloud_vectorsearch_v1_services_data_object_service_DataObjectServiceAsyncClient_batch_update_data_objects)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vectorsearch_v1.types.BatchUpdateDataObjectsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.BatchUpdateDataObjectsRequest), dict]]`   
The request object. Request message for DataObjectService.BatchUpdateDataObjects.  
`parent` |  ``str``   
Required. The resource name of the Collection to update the DataObjects in. Format: `projects/{project}/locations/{location}/collections/{collection}`. The parent field in the UpdateDataObjectRequest messages must match this field. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`requests` |  `:class:`MutableSequence[[google.cloud.vectorsearch_v1.types.UpdateDataObjectRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.UpdateDataObjectRequest)]``   
Required. The request message specifying the resources to update. A maximum of 1000 DataObjects can be updated in a batch. This corresponds to the `requests` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vectorsearch_v1.types.BatchUpdateDataObjectsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.BatchUpdateDataObjectsResponse)` | Response message for DataObjectService.BatchUpdateDataObjects.  
  
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

### create_data_object
    
    
    create_data_object(
        request: typing.Optional[
            typing.Union[
                google.cloud.vectorsearch_v1.types.data_object_service.CreateDataObjectRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_object: typing.Optional[
            google.cloud.vectorsearch_v1.types.data_object.DataObject
        ] = None,
        data_object_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.vectorsearch_v1.types.data_object.DataObject

Creates a dataObject.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest)
    
    async def sample_create_data_object():
        # Create a client
        client = [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest).[DataObjectServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest).[CreateDataObjectRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.CreateDataObjectRequest.html)(
            parent="parent_value",
            data_object_id="data_object_id_value",
        )
    
        # Make the request
        response = await client.[create_data_object](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient.html#google_cloud_vectorsearch_v1_services_data_object_service_DataObjectServiceAsyncClient_create_data_object)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vectorsearch_v1.types.CreateDataObjectRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.CreateDataObjectRequest), dict]]`   
The request object. Request message for DataObjectService.CreateDataObject.  
`parent` |  ``str``   
Required. The resource name of the Collection to create the DataObject in. Format: `projects/{project}/locations/{location}/collections/{collection}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`data_object` |  `[DataObject](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.DataObject)`   
Required. The DataObject to create. This corresponds to the `data_object` field on the `request` instance; if `request` is provided, this should not be set.  
`data_object_id` |  ``str``   
Required. The id of the dataObject to create. The id must be 1-63 characters long, and comply with `RFC1035 <https://www.ietf.org/rfc/rfc1035.txt>`__. Specifically, it must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient?:\[-a-z0-9\]{0,61}\[a-z0-9\])?`. This corresponds to the `data_object_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vectorsearch_v1.types.DataObject](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.DataObject)` | A dataObject resource in Vector Search.  
  
### data_object_path
    
    
    data_object_path(
        project: str, location: str, collection: str, dataObject: str
    ) -> str

Returns a fully-qualified data_object string.

### delete_data_object
    
    
    delete_data_object(
        request: typing.Optional[
            typing.Union[
                google.cloud.vectorsearch_v1.types.data_object_service.DeleteDataObjectRequest,
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
    ) -> None

Deletes a dataObject.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest)
    
    async def sample_delete_data_object():
        # Create a client
        client = [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest).[DataObjectServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest).[DeleteDataObjectRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.DeleteDataObjectRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_data_object](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient.html#google_cloud_vectorsearch_v1_services_data_object_service_DataObjectServiceAsyncClient_delete_data_object)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vectorsearch_v1.types.DeleteDataObjectRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.DeleteDataObjectRequest), dict]]`   
The request object. Request message for DataObjectService.DeleteDataObject.  
`name` |  ``str``   
Required. The name of the DataObject resource to be deleted. Format: `projects/{project}/locations/{location}/collections/{collection}/dataObjects/{dataObject}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
`DataObjectServiceAsyncClient` | The constructed client.  
  
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
`DataObjectServiceAsyncClient` | The constructed client.  
  
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
`DataObjectServiceAsyncClient` | The constructed client.  
  
### get_data_object
    
    
    get_data_object(
        request: typing.Optional[
            typing.Union[
                google.cloud.vectorsearch_v1.types.data_object_service.GetDataObjectRequest,
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
    ) -> google.cloud.vectorsearch_v1.types.data_object.DataObject

Gets a data object.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest)
    
    async def sample_get_data_object():
        # Create a client
        client = [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest).[DataObjectServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest).[GetDataObjectRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.GetDataObjectRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_data_object](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient.html#google_cloud_vectorsearch_v1_services_data_object_service_DataObjectServiceAsyncClient_get_data_object)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vectorsearch_v1.types.GetDataObjectRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.GetDataObjectRequest), dict]]`   
The request object. Request message for DataObjectService.GetDataObject.  
`name` |  ``str``   
Required. The name of the DataObject resource. Format: `projects/{project}/locations/{location}/collections/{collection}/dataObjects/{dataObject}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vectorsearch_v1.types.DataObject](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.DataObject)` | A dataObject resource in Vector Search.  
  
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
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.vectorsearch_v1.services.data_object_service.transports.base.DataObjectServiceTransport
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

### parse_data_object_path
    
    
    parse_data_object_path(path: str) -> typing.Dict[str, str]

Parses a data_object path into its component segments.

### update_data_object
    
    
    update_data_object(
        request: typing.Optional[
            typing.Union[
                google.cloud.vectorsearch_v1.types.data_object_service.UpdateDataObjectRequest,
                dict,
            ]
        ] = None,
        *,
        data_object: typing.Optional[
            google.cloud.vectorsearch_v1.types.data_object.DataObject
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
    ) -> google.cloud.vectorsearch_v1.types.data_object.DataObject

Updates a dataObject.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest)
    
    async def sample_update_data_object():
        # Create a client
        client = [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest).[DataObjectServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [vectorsearch_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest).[UpdateDataObjectRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.UpdateDataObjectRequest.html)(
        )
    
        # Make the request
        response = await client.[update_data_object](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.services.data_object_service.DataObjectServiceAsyncClient.html#google_cloud_vectorsearch_v1_services_data_object_service_DataObjectServiceAsyncClient_update_data_object)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.vectorsearch_v1.types.UpdateDataObjectRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.UpdateDataObjectRequest), dict]]`   
The request object. Request message for DataObjectService.UpdateDataObject.  
`data_object` |  `[DataObject](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.DataObject)`   
Required. The DataObject which replaces the resource on the server. This corresponds to the `data_object` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. The update mask applies to the resource. See `google.protobuf.FieldMask][google.protobuf.FieldMask]`. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.vectorsearch_v1.types.DataObject](https://docs.cloud.google.com/python/docs/reference/google-cloud-vectorsearch/latest/google.cloud.vectorsearch_v1.types.DataObject)` | A dataObject resource in Vector Search.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
