---
url: https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.DatastoreAdminClient
title: Class DatastoreAdminClient (2.27.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:47:24.092840+00:00
---

# Class DatastoreAdminClient (2.27.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.DatastoreAdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DatastoreAdminClient (2.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.27.0 (latest)  2.26.1  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.0  2.16.1  2.15.2  2.14.0  2.13.2  2.12.0  2.11.1  2.10.0  2.9.0  2.8.3  2.7.2  2.6.2  2.5.1  2.4.0  2.3.0  2.2.0  2.1.6  2.0.1  1.15.5  1.14.0  1.13.2  1.12.0  1.11.0  1.10.0  1.9.0 
    
    
    DatastoreAdminClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.datastore_admin_v1.services.datastore_admin.transports.base.DatastoreAdminTransport,
                typing.Callable[
                    [...],
                    google.cloud.datastore_admin_v1.services.datastore_admin.transports.base.DatastoreAdminTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Google Cloud Datastore Admin API

The Datastore Admin API provides several admin services for Cloud Datastore.

Concepts: Project, namespace, kind, and entity as defined in the Google Cloud Datastore API.

Operation: An Operation represents work being performed in the background.

EntityFilter: Allows specifying a subset of entities in a project. This is specified as a combination of kinds and namespaces (either or both of which may be all).

Export/Import Service:

  * The Export/Import service provides the ability to copy all or a subset of entities to/from Google Cloud Storage.
  * Exported data may be imported into Cloud Datastore for any Google Cloud Platform project. It is not restricted to the export source project. It is possible to export from one project and then import into another.
  * Exported data can also be loaded into Google BigQuery for analysis.
  * Exports and imports are performed asynchronously. An Operation resource is created for each export/import. The state (including any errors encountered) of the export/import may be queried via the Operation resource.



Index Service:

  * The index service manages Cloud Datastore composite indexes.
  * Index creation and deletion are performed asynchronously. An Operation resource is created for each such asynchronous operation. The state of the operation (including any errors encountered) may be queried via the Operation resource.



Operation Service:

  * The Operations collection provides a record of actions performed for the specified project (including any operations in progress). Operations are not created directly but through calls on other collections or resources.
  * An operation that is not yet done may be cancelled. The request to cancel is asynchronous and the operation may continue to run for some time after the request to cancel is made.
  * An operation that is done may be deleted so that it is no longer listed as part of the Operation collection.
  * ListOperations returns all pending operations, but not completed operations.
  * Operations are created by service DatastoreAdmin, but are accessed via service google.longrunning.Operations.



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
`DatastoreAdminTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### DatastoreAdminClient
    
    
    DatastoreAdminClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.datastore_admin_v1.services.datastore_admin.transports.base.DatastoreAdminTransport,
                typing.Callable[
                    [...],
                    google.cloud.datastore_admin_v1.services.datastore_admin.transports.base.DatastoreAdminTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the datastore admin client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,DatastoreAdminTransport,Callable[..., DatastoreAdminTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the DatastoreAdminTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that the `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTLSChannelError` | If mutual TLS transport creation failed for any reason.  
  
### __exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

**Warning:** ONLY use as a context manager if the transport is NOT shared with other clients! Exiting the with block will CLOSE the transport and may cause errors in other clients! 

### cancel_operation
    
    
    cancel_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.CancelOperationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
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
`retry` |  `google.api_core.retry.Retry`   
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

### create_index
    
    
    create_index(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastore_admin_v1.types.datastore_admin.CreateIndexRequest,
                dict,
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates the specified index. A newly created index's initial state is `CREATING`. On completion of the returned `google.longrunning.Operation][google.longrunning.Operation]`, the state will be `READY`. If the index already exists, the call will return an `ALREADY_EXISTS` status.

During index creation, the process could result in an error, in which case the index will move to the `ERROR` state. The process can be recovered by fixing the data that caused the error, removing the index with `delete][google.datastore.admin.v1.DatastoreAdmin.DeleteIndex]`, then re-creating the index with [create] [google.datastore.admin.v1.DatastoreAdmin.CreateIndex].

Indexes with a single property cannot be created.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import datastore_admin_v1
    
    def sample_create_index():
        # Create a client
        client = datastore_admin_v1.[DatastoreAdminClient](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.DatastoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = datastore_admin_v1.CreateIndexRequest(
        )
    
        # Make the request
        operation = [client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.html).[create_index](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.DatastoreAdminClient.html#google_cloud_datastore_admin_v1_services_datastore_admin_client_DatastoreAdminClient_create_index)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.datastore_admin_v1.types.CreateIndexRequest, dict]`   
The request object. The request for `google.datastore.admin.v1.DatastoreAdmin.CreateIndex][google.datastore.admin.v1.DatastoreAdmin.CreateIndex]`.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be Index Datastore composite index definition.  
  
### delete_index
    
    
    delete_index(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastore_admin_v1.types.datastore_admin.DeleteIndexRequest,
                dict,
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Deletes an existing index. An index can only be deleted if it is in a `READY` or `ERROR` state. On successful execution of the request, the index will be in a `DELETING` `state][google.datastore.admin.v1.Index.State]`. And on completion of the returned `google.longrunning.Operation][google.longrunning.Operation]`, the index will be removed.

During index deletion, the process could result in an error, in which case the index will move to the `ERROR` state. The process can be recovered by fixing the data that caused the error, followed by calling `delete][google.datastore.admin.v1.DatastoreAdmin.DeleteIndex]` again.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import datastore_admin_v1
    
    def sample_delete_index():
        # Create a client
        client = datastore_admin_v1.[DatastoreAdminClient](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.DatastoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = datastore_admin_v1.DeleteIndexRequest(
        )
    
        # Make the request
        operation = [client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.html).[delete_index](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.DatastoreAdminClient.html#google_cloud_datastore_admin_v1_services_datastore_admin_client_DatastoreAdminClient_delete_index)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.datastore_admin_v1.types.DeleteIndexRequest, dict]`   
The request object. The request for `google.datastore.admin.v1.DatastoreAdmin.DeleteIndex][google.datastore.admin.v1.DatastoreAdmin.DeleteIndex]`.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be Index Datastore composite index definition.  
  
### delete_operation
    
    
    delete_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.DeleteOperationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
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
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### export_entities
    
    
    export_entities(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastore_admin_v1.types.datastore_admin.ExportEntitiesRequest,
                dict,
            ]
        ] = None,
        *,
        project_id: typing.Optional[str] = None,
        labels: typing.Optional[typing.MutableMapping[str, str]] = None,
        entity_filter: typing.Optional[
            google.cloud.datastore_admin_v1.types.datastore_admin.EntityFilter
        ] = None,
        output_url_prefix: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Exports a copy of all or a subset of entities from Google Cloud Datastore to another storage system, such as Google Cloud Storage. Recent updates to entities may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import datastore_admin_v1
    
    def sample_export_entities():
        # Create a client
        client = datastore_admin_v1.[DatastoreAdminClient](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.DatastoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = datastore_admin_v1.ExportEntitiesRequest(
            project_id="project_id_value",
            output_url_prefix="output_url_prefix_value",
        )
    
        # Make the request
        operation = [client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.html).[export_entities](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.DatastoreAdminClient.html#google_cloud_datastore_admin_v1_services_datastore_admin_client_DatastoreAdminClient_export_entities)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.datastore_admin_v1.types.ExportEntitiesRequest, dict]`   
The request object. The request for `google.datastore.admin.v1.DatastoreAdmin.ExportEntities][google.datastore.admin.v1.DatastoreAdmin.ExportEntities]`.  
`project_id` |  `str`   
Required. Project ID against which to make the request. This corresponds to the `project_id` field on the `request` instance; if `request` is provided, this should not be set.  
`labels` |  `MutableMapping[str, str]`   
Client-assigned labels. This corresponds to the `labels` field on the `request` instance; if `request` is provided, this should not be set.  
`entity_filter` |  `google.cloud.datastore_admin_v1.types.EntityFilter`   
Description of what data from the project is included in the export. This corresponds to the `entity_filter` field on the `request` instance; if `request` is provided, this should not be set.  
`output_url_prefix` |  `str`   
Required. Location for the export metadata and data files. The full resource URL of the external storage location. Currently, only Google Cloud Storage is supported. So output_url_prefix should be of the form: `gs://BUCKET_NAME[/NAMESPACE_PATH]`, where `BUCKET_NAME` is the name of the Cloud Storage bucket and `NAMESPACE_PATH` is an optional Cloud Storage namespace path (this is not a Cloud Datastore namespace). For more information about Cloud Storage namespace paths, see `Object name considerations <https://cloud.google.com/storage/docs/naming#object-considerations>`__. The resulting files will be nested deeper than the specified URL prefix. The final output URL will be provided in the `google.datastore.admin.v1.ExportEntitiesResponse.output_url][google.datastore.admin.v1.ExportEntitiesResponse.output_url]` field. That value should be used for subsequent ImportEntities operations. By nesting the data files deeper, the same Cloud Storage bucket can be used in multiple ExportEntities operations without conflict. This corresponds to the `output_url_prefix` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be ExportEntitiesResponse The response for `google.datastore.admin.v1.DatastoreAdmin.ExportEntities][google.datastore.admin.v1.DatastoreAdmin.ExportEntities]`.  
  
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
`DatastoreAdminClient` | The constructed client.  
  
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
`DatastoreAdminClient` | The constructed client.  
  
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
`DatastoreAdminClient` | The constructed client.  
  
### get_index
    
    
    get_index(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastore_admin_v1.types.datastore_admin.GetIndexRequest, dict
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.datastore_admin_v1.types.index.Index

Gets an index.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import datastore_admin_v1
    
    def sample_get_index():
        # Create a client
        client = datastore_admin_v1.[DatastoreAdminClient](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.DatastoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = datastore_admin_v1.GetIndexRequest(
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.html).[get_index](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.DatastoreAdminClient.html#google_cloud_datastore_admin_v1_services_datastore_admin_client_DatastoreAdminClient_get_index)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.datastore_admin_v1.types.GetIndexRequest, dict]`   
The request object. The request for `google.datastore.admin.v1.DatastoreAdmin.GetIndex][google.datastore.admin.v1.DatastoreAdmin.GetIndex]`.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.datastore_admin_v1.types.Index` | Datastore composite index definition.  
  
### get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated. Return the API endpoint and client cert source for mutual TLS.

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
                google.api_core.retry.retry_unary.Retry,
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
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.Operation`` | An `Operation` object.  
  
### import_entities
    
    
    import_entities(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastore_admin_v1.types.datastore_admin.ImportEntitiesRequest,
                dict,
            ]
        ] = None,
        *,
        project_id: typing.Optional[str] = None,
        labels: typing.Optional[typing.MutableMapping[str, str]] = None,
        input_url: typing.Optional[str] = None,
        entity_filter: typing.Optional[
            google.cloud.datastore_admin_v1.types.datastore_admin.EntityFilter
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Imports entities into Google Cloud Datastore. Existing entities with the same key are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportEntities operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Datastore.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import datastore_admin_v1
    
    def sample_import_entities():
        # Create a client
        client = datastore_admin_v1.[DatastoreAdminClient](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.DatastoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = datastore_admin_v1.ImportEntitiesRequest(
            project_id="project_id_value",
            input_url="input_url_value",
        )
    
        # Make the request
        operation = [client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.html).[import_entities](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.DatastoreAdminClient.html#google_cloud_datastore_admin_v1_services_datastore_admin_client_DatastoreAdminClient_import_entities)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.datastore_admin_v1.types.ImportEntitiesRequest, dict]`   
The request object. The request for `google.datastore.admin.v1.DatastoreAdmin.ImportEntities][google.datastore.admin.v1.DatastoreAdmin.ImportEntities]`.  
`project_id` |  `str`   
Required. Project ID against which to make the request. This corresponds to the `project_id` field on the `request` instance; if `request` is provided, this should not be set.  
`labels` |  `MutableMapping[str, str]`   
Client-assigned labels. This corresponds to the `labels` field on the `request` instance; if `request` is provided, this should not be set.  
`input_url` |  `str`   
Required. The full resource URL of the external storage location. Currently, only Google Cloud Storage is supported. So input_url should be of the form: `gs://BUCKET_NAME[/NAMESPACE_PATH]/OVERALL_EXPORT_METADATA_FILE`, where `BUCKET_NAME` is the name of the Cloud Storage bucket, `NAMESPACE_PATH` is an optional Cloud Storage namespace path (this is not a Cloud Datastore namespace), and `OVERALL_EXPORT_METADATA_FILE` is the metadata file written by the ExportEntities operation. For more information about Cloud Storage namespace paths, see `Object name considerations <https://cloud.google.com/storage/docs/naming#object-considerations>`__. For more information, see `google.datastore.admin.v1.ExportEntitiesResponse.output_url][google.datastore.admin.v1.ExportEntitiesResponse.output_url]`. This corresponds to the `input_url` field on the `request` instance; if `request` is provided, this should not be set.  
`entity_filter` |  `google.cloud.datastore_admin_v1.types.EntityFilter`   
Optionally specify which kinds/namespaces are to be imported. If provided, the list must be a subset of the EntityFilter used in creating the export, otherwise a FAILED_PRECONDITION error will be returned. If no filter is specified then all entities from the export are imported. This corresponds to the `entity_filter` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### list_indexes
    
    
    list_indexes(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastore_admin_v1.types.datastore_admin.ListIndexesRequest,
                dict,
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.datastore_admin_v1.services.datastore_admin.pagers.ListIndexesPager

Lists the indexes that match the specified filters. Datastore uses an eventually consistent query to fetch the list of indexes and may occasionally return stale results.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import datastore_admin_v1
    
    def sample_list_indexes():
        # Create a client
        client = datastore_admin_v1.[DatastoreAdminClient](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.DatastoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = datastore_admin_v1.ListIndexesRequest(
        )
    
        # Make the request
        page_result = [client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.html).[list_indexes](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore_admin_v1.services.datastore_admin.client.DatastoreAdminClient.html#google_cloud_datastore_admin_v1_services_datastore_admin_client_DatastoreAdminClient_list_indexes)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.datastore_admin_v1.types.ListIndexesRequest, dict]`   
The request object. The request for `google.datastore.admin.v1.DatastoreAdmin.ListIndexes][google.datastore.admin.v1.DatastoreAdmin.ListIndexes]`.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.datastore_admin_v1.services.datastore_admin.pagers.ListIndexesPager` | The response for `google.datastore.admin.v1.DatastoreAdmin.ListIndexes][google.datastore.admin.v1.DatastoreAdmin.ListIndexes]`. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_operations
    
    
    list_operations(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.ListOperationsRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
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
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.ListOperationsResponse`` | Response message for `ListOperations` method.  
  
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
