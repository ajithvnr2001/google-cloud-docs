---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient
title: Class FirestoreAdminClient (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:03.599483+00:00
---

# Class FirestoreAdminClient (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class FirestoreAdminClient (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    FirestoreAdminClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.firestore_admin_v1.services.firestore_admin.transports.base.FirestoreAdminTransport,
                typing.Callable[
                    [...],
                    google.cloud.firestore_admin_v1.services.firestore_admin.transports.base.FirestoreAdminTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

The Cloud Firestore Admin API.

This API provides several administrative services for Cloud Firestore.

Project, Database, Namespace, Collection, Collection Group, and Document are used as defined in the Google Cloud Firestore API.

Operation: An Operation represents work being performed in the background.

The index service manages Cloud Firestore indexes.

Index creation is performed asynchronously. An Operation resource is created for each such asynchronous operation. The state of the operation (including any errors encountered) may be queried via the Operation resource.

The Operations collection provides a record of actions performed for the specified Project (including any Operations in progress). Operations are not created directly but through calls on other collections or resources.

An Operation that is done may be deleted so that it is no longer listed as part of the Operation collection. Operations are garbage collected after 30 days. By default, ListOperations will only return in progress and failed operations. To list completed operation, issue a ListOperations request with the filter `done: true`.

Operations are created by service `FirestoreAdmin`, but are accessed via service `google.longrunning.Operations`.

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
`FirestoreAdminTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### FirestoreAdminClient
    
    
    FirestoreAdminClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.firestore_admin_v1.services.firestore_admin.transports.base.FirestoreAdminTransport,
                typing.Callable[
                    [...],
                    google.cloud.firestore_admin_v1.services.firestore_admin.transports.base.FirestoreAdminTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the firestore admin client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,FirestoreAdminTransport,Callable[..., FirestoreAdminTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the FirestoreAdminTransport constructor. If set to None, a transport is chosen automatically.  
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

### backup_path
    
    
    backup_path(project: str, location: str, backup: str) -> str

Returns a fully-qualified backup string.

### backup_schedule_path
    
    
    backup_schedule_path(project: str, database: str, backup_schedule: str) -> str

Returns a fully-qualified backup_schedule string.

### bulk_delete_documents
    
    
    bulk_delete_documents(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.BulkDeleteDocumentsRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Bulk deletes a subset of documents from Google Cloud Firestore. Documents created or updated after the underlying system starts to process the request will not be deleted. The bulk delete occurs in the background and its progress can be monitored and managed via the Operation resource that is created.

For more details on bulk delete behavior, refer to:

<https://cloud.google.com/firestore/docs/manage-data/bulk-delete>
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_bulk_delete_documents():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.BulkDeleteDocumentsRequest(
            name="name_value",
        )
    
        # Make the request
        operation = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[bulk_delete_documents](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_bulk_delete_documents)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.BulkDeleteDocumentsRequest, dict]`   
The request object. The request for `FirestoreAdmin.BulkDeleteDocuments][google.firestore.admin.v1.FirestoreAdmin.BulkDeleteDocuments]`. When both collection_ids and namespace_ids are set, only documents satisfying both conditions will be deleted. Requests with namespace_ids and collection_ids both empty will be rejected. Please use `FirestoreAdmin.DeleteDatabase][google.firestore.admin.v1.FirestoreAdmin.DeleteDatabase]` instead.  
`name` |  `str`   
Required. Database to operate. Should be of the form: `projects/{project_id}/databases/{database_id}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be BulkDeleteDocumentsResponse The response for `FirestoreAdmin.BulkDeleteDocuments][google.firestore.admin.v1.FirestoreAdmin.BulkDeleteDocuments]`.  
  
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
  
### clone_database
    
    
    clone_database(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.CloneDatabaseRequest,
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

Creates a new database by cloning an existing one.

The new database must be in the same cloud region or multi-region location as the existing database. This behaves similar to `FirestoreAdmin.CreateDatabase][google.firestore.admin.v1.FirestoreAdmin.CreateDatabase]` except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing database.

The `long-running operation][google.longrunning.Operation]` can be used to track the progress of the clone, with the Operation's `metadata][google.longrunning.Operation.metadata]` field type being the `CloneDatabaseMetadata][google.firestore.admin.v1.CloneDatabaseMetadata]`. The `response][google.longrunning.Operation.response]` type is the `Database][google.firestore.admin.v1.Database]` if the clone was successful. The new database is not readable or writeable until the LRO has completed.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_clone_database():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        pitr_snapshot = firestore_admin_v1.PitrSnapshot()
        pitr_snapshot.database = "database_value"
    
        request = firestore_admin_v1.CloneDatabaseRequest(
            parent="parent_value",
            database_id="database_id_value",
            pitr_snapshot=pitr_snapshot,
        )
    
        # Make the request
        operation = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[clone_database](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_clone_database)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.CloneDatabaseRequest, dict]`   
The request object. The request message for `FirestoreAdmin.CloneDatabase][google.firestore.admin.v1.FirestoreAdmin.CloneDatabase]`.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be Database A Cloud Firestore Database.  
  
### collection_group_path
    
    
    collection_group_path(project: str, database: str, collection: str) -> str

Returns a fully-qualified collection_group string.

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

### create_backup_schedule
    
    
    create_backup_schedule(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.CreateBackupScheduleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_schedule: typing.Optional[
            google.cloud.firestore_admin_v1.types.schedule.BackupSchedule
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.types.schedule.BackupSchedule

Creates a backup schedule on a database. At most two backup schedules can be configured on a database, one daily backup schedule and one weekly backup schedule.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_create_backup_schedule():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.CreateBackupScheduleRequest(
            parent="parent_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[create_backup_schedule](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_create_backup_schedule)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.CreateBackupScheduleRequest, dict]`   
The request object. The request for `FirestoreAdmin.CreateBackupSchedule][google.firestore.admin.v1.FirestoreAdmin.CreateBackupSchedule]`.  
`parent` |  `str`   
Required. The parent database. Format `projects/{project}/databases/{database}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_schedule` |  `google.cloud.firestore_admin_v1.types.BackupSchedule`   
Required. The backup schedule to create. This corresponds to the `backup_schedule` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.types.BackupSchedule` | A backup schedule for a Cloud Firestore Database. This resource is owned by the database it is backing up, and is deleted along with the database. The actual backups are not though.  
  
### create_database
    
    
    create_database(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.CreateDatabaseRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        database: typing.Optional[
            google.cloud.firestore_admin_v1.types.database.Database
        ] = None,
        database_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Create a database.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_create_database():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.CreateDatabaseRequest(
            parent="parent_value",
            database_id="database_id_value",
        )
    
        # Make the request
        operation = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[create_database](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_create_database)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.CreateDatabaseRequest, dict]`   
The request object. The request for `FirestoreAdmin.CreateDatabase][google.firestore.admin.v1.FirestoreAdmin.CreateDatabase]`.  
`parent` |  `str`   
Required. A parent name of the form `projects/{project_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`database` |  `google.cloud.firestore_admin_v1.types.Database`   
Required. The Database to create. This corresponds to the `database` field on the `request` instance; if `request` is provided, this should not be set.  
`database_id` |  `str`   
Required. The ID to use for the database, which will become the final component of the database's resource name. This value should be 4-63 characters. Valid characters are /`a-z][0-9]`-/ with first character a letter and the last a letter or a number. Must not be UUID-like /[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}/. "(default)" database ID is also valid if the database is Standard edition. This corresponds to the `database_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be Database A Cloud Firestore Database.  
  
### create_index
    
    
    create_index(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.CreateIndexRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        index: typing.Optional[google.cloud.firestore_admin_v1.types.index.Index] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a composite index. This returns a `google.longrunning.Operation][google.longrunning.Operation]` which may be used to track the status of the creation. The metadata for the operation will be the type `IndexOperationMetadata][google.firestore.admin.v1.IndexOperationMetadata]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_create_index():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.CreateIndexRequest(
            parent="parent_value",
        )
    
        # Make the request
        operation = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[create_index](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_create_index)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.CreateIndexRequest, dict]`   
The request object. The request for `FirestoreAdmin.CreateIndex][google.firestore.admin.v1.FirestoreAdmin.CreateIndex]`.  
`parent` |  `str`   
Required. A parent name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`index` |  `google.cloud.firestore_admin_v1.types.Index`   
Required. The composite index to create. This corresponds to the `index` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be Index Cloud Firestore indexes enable simple and complex queries against documents in a database.  
  
### create_user_creds
    
    
    create_user_creds(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.CreateUserCredsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        user_creds: typing.Optional[
            google.cloud.firestore_admin_v1.types.user_creds.UserCreds
        ] = None,
        user_creds_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.types.user_creds.UserCreds

Create a user creds.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_create_user_creds():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.CreateUserCredsRequest(
            parent="parent_value",
            user_creds_id="user_creds_id_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[create_user_creds](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_create_user_creds)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.CreateUserCredsRequest, dict]`   
The request object. The request for `FirestoreAdmin.CreateUserCreds][google.firestore.admin.v1.FirestoreAdmin.CreateUserCreds]`.  
`parent` |  `str`   
Required. A parent name of the form `projects/{project_id}/databases/{database_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`user_creds` |  `google.cloud.firestore_admin_v1.types.UserCreds`   
Required. The user creds to create. This corresponds to the `user_creds` field on the `request` instance; if `request` is provided, this should not be set.  
`user_creds_id` |  `str`   
Required. The ID to use for the user creds, which will become the final component of the user creds's resource name. This value should be 4-63 characters. Valid characters are /`a-z][0-9]`-/ with first character a letter and the last a letter or a number. Must not be UUID-like /[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}/. This corresponds to the `user_creds_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.types.UserCreds` | A Cloud Firestore User Creds.  
  
### database_path
    
    
    database_path(project: str, database: str) -> str

Returns a fully-qualified database string.

### delete_backup
    
    
    delete_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.DeleteBackupRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes a backup.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_delete_backup():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.DeleteBackupRequest(
            name="name_value",
        )
    
        # Make the request
        [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[delete_backup](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_delete_backup)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.DeleteBackupRequest, dict]`   
The request object. The request for `FirestoreAdmin.DeleteBackup][google.firestore.admin.v1.FirestoreAdmin.DeleteBackup]`.  
`name` |  `str`   
Required. Name of the backup to delete. format is `projects/{project}/locations/{location}/backups/{backup}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_backup_schedule
    
    
    delete_backup_schedule(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.DeleteBackupScheduleRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes a backup schedule.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_delete_backup_schedule():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.DeleteBackupScheduleRequest(
            name="name_value",
        )
    
        # Make the request
        [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[delete_backup_schedule](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_delete_backup_schedule)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.DeleteBackupScheduleRequest, dict]`   
The request object. The request for [FirestoreAdmin.DeleteBackupSchedules][].  
`name` |  `str`   
Required. The name of the backup schedule. Format `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_database
    
    
    delete_database(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.DeleteDatabaseRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Deletes a database.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_delete_database():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.DeleteDatabaseRequest(
            name="name_value",
        )
    
        # Make the request
        operation = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[delete_database](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_delete_database)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.DeleteDatabaseRequest, dict]`   
The request object. The request for `FirestoreAdmin.DeleteDatabase][google.firestore.admin.v1.FirestoreAdmin.DeleteDatabase]`.  
`name` |  `str`   
Required. A name of the form `projects/{project_id}/databases/{database_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be Database A Cloud Firestore Database.  
  
### delete_index
    
    
    delete_index(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.DeleteIndexRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes a composite index.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_delete_index():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.DeleteIndexRequest(
            name="name_value",
        )
    
        # Make the request
        [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[delete_index](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_delete_index)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.DeleteIndexRequest, dict]`   
The request object. The request for `FirestoreAdmin.DeleteIndex][google.firestore.admin.v1.FirestoreAdmin.DeleteIndex]`.  
`name` |  `str`   
Required. A name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{index_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
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
  
### delete_user_creds
    
    
    delete_user_creds(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.DeleteUserCredsRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes a user creds.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_delete_user_creds():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.DeleteUserCredsRequest(
            name="name_value",
        )
    
        # Make the request
        [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[delete_user_creds](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_delete_user_creds)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.DeleteUserCredsRequest, dict]`   
The request object. The request for `FirestoreAdmin.DeleteUserCreds][google.firestore.admin.v1.FirestoreAdmin.DeleteUserCreds]`.  
`name` |  `str`   
Required. A name of the form `projects/{project_id}/databases/{database_id}/userCreds/{user_creds_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### disable_user_creds
    
    
    disable_user_creds(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.DisableUserCredsRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.types.user_creds.UserCreds

Disables a user creds. No-op if the user creds are already disabled.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_disable_user_creds():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.DisableUserCredsRequest(
            name="name_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[disable_user_creds](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_disable_user_creds)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.DisableUserCredsRequest, dict]`   
The request object. The request for `FirestoreAdmin.DisableUserCreds][google.firestore.admin.v1.FirestoreAdmin.DisableUserCreds]`.  
`name` |  `str`   
Required. A name of the form `projects/{project_id}/databases/{database_id}/userCreds/{user_creds_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.types.UserCreds` | A Cloud Firestore User Creds.  
  
### enable_user_creds
    
    
    enable_user_creds(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.EnableUserCredsRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.types.user_creds.UserCreds

Enables a user creds. No-op if the user creds are already enabled.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_enable_user_creds():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.EnableUserCredsRequest(
            name="name_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[enable_user_creds](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_enable_user_creds)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.EnableUserCredsRequest, dict]`   
The request object. The request for `FirestoreAdmin.EnableUserCreds][google.firestore.admin.v1.FirestoreAdmin.EnableUserCreds]`.  
`name` |  `str`   
Required. A name of the form `projects/{project_id}/databases/{database_id}/userCreds/{user_creds_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.types.UserCreds` | A Cloud Firestore User Creds.  
  
### export_documents
    
    
    export_documents(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.ExportDocumentsRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. Recent updates to documents may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage.

For more details on export behavior and output format, refer to:

<https://cloud.google.com/firestore/docs/manage-data/export-import>
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_export_documents():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.ExportDocumentsRequest(
            name="name_value",
        )
    
        # Make the request
        operation = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[export_documents](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_export_documents)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.ExportDocumentsRequest, dict]`   
The request object. The request for `FirestoreAdmin.ExportDocuments][google.firestore.admin.v1.FirestoreAdmin.ExportDocuments]`.  
`name` |  `str`   
Required. Database to export. Should be of the form: `projects/{project_id}/databases/{database_id}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be ExportDocumentsResponse Returned in the `google.longrunning.Operation][google.longrunning.Operation]` response field.  
  
### field_path
    
    
    field_path(project: str, database: str, collection: str, field: str) -> str

Returns a fully-qualified field string.

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
`FirestoreAdminClient` | The constructed client.  
  
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
`FirestoreAdminClient` | The constructed client.  
  
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
`FirestoreAdminClient` | The constructed client.  
  
### get_backup
    
    
    get_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.GetBackupRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.types.backup.Backup

Gets information about a backup.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_get_backup():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.GetBackupRequest(
            name="name_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[get_backup](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_get_backup)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.GetBackupRequest, dict]`   
The request object. The request for `FirestoreAdmin.GetBackup][google.firestore.admin.v1.FirestoreAdmin.GetBackup]`.  
`name` |  `str`   
Required. Name of the backup to fetch. Format is `projects/{project}/locations/{location}/backups/{backup}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.types.Backup` | A Backup of a Cloud Firestore Database. The backup contains all documents and index configurations for the given database at a specific point in time.  
  
### get_backup_schedule
    
    
    get_backup_schedule(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.GetBackupScheduleRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.types.schedule.BackupSchedule

Gets information about a backup schedule.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_get_backup_schedule():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.GetBackupScheduleRequest(
            name="name_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[get_backup_schedule](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_get_backup_schedule)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.GetBackupScheduleRequest, dict]`   
The request object. The request for `FirestoreAdmin.GetBackupSchedule][google.firestore.admin.v1.FirestoreAdmin.GetBackupSchedule]`.  
`name` |  `str`   
Required. The name of the backup schedule. Format `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.types.BackupSchedule` | A backup schedule for a Cloud Firestore Database. This resource is owned by the database it is backing up, and is deleted along with the database. The actual backups are not though.  
  
### get_database
    
    
    get_database(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.GetDatabaseRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.types.database.Database

Gets information about a database.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_get_database():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.GetDatabaseRequest(
            name="name_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[get_database](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_get_database)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.GetDatabaseRequest, dict]`   
The request object. The request for `FirestoreAdmin.GetDatabase][google.firestore.admin.v1.FirestoreAdmin.GetDatabase]`.  
`name` |  `str`   
Required. A name of the form `projects/{project_id}/databases/{database_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.types.Database` | A Cloud Firestore Database.  
  
### get_field
    
    
    get_field(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.GetFieldRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.types.field.Field

Gets the metadata and configuration for a Field.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_get_field():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.GetFieldRequest(
            name="name_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[get_field](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_get_field)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.GetFieldRequest, dict]`   
The request object. The request for `FirestoreAdmin.GetField][google.firestore.admin.v1.FirestoreAdmin.GetField]`.  
`name` |  `str`   
Required. A name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/fields/{field_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.types.Field` | Represents a single field in the database. Fields are grouped by their "Collection Group", which represent all collections in the database with the same ID.  
  
### get_index
    
    
    get_index(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.GetIndexRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.types.index.Index

Gets a composite index.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_get_index():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.GetIndexRequest(
            name="name_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[get_index](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_get_index)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.GetIndexRequest, dict]`   
The request object. The request for `FirestoreAdmin.GetIndex][google.firestore.admin.v1.FirestoreAdmin.GetIndex]`.  
`name` |  `str`   
Required. A name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{index_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.types.Index` | Cloud Firestore indexes enable simple and complex queries against documents in a database.  
  
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
  
### get_user_creds
    
    
    get_user_creds(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.GetUserCredsRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.types.user_creds.UserCreds

Gets a user creds resource. Note that the returned resource does not contain the secret value itself.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_get_user_creds():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.GetUserCredsRequest(
            name="name_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[get_user_creds](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_get_user_creds)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.GetUserCredsRequest, dict]`   
The request object. The request for `FirestoreAdmin.GetUserCreds][google.firestore.admin.v1.FirestoreAdmin.GetUserCreds]`.  
`name` |  `str`   
Required. A name of the form `projects/{project_id}/databases/{database_id}/userCreds/{user_creds_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.types.UserCreds` | A Cloud Firestore User Creds.  
  
### import_documents
    
    
    import_documents(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.ImportDocumentsRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Imports documents into Google Cloud Firestore. Existing documents with the same name are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportDocuments operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Firestore.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_import_documents():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.ImportDocumentsRequest(
            name="name_value",
        )
    
        # Make the request
        operation = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[import_documents](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_import_documents)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.ImportDocumentsRequest, dict]`   
The request object. The request for `FirestoreAdmin.ImportDocuments][google.firestore.admin.v1.FirestoreAdmin.ImportDocuments]`.  
`name` |  `str`   
Required. Database to import into. Should be of the form: `projects/{project_id}/databases/{database_id}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### index_path
    
    
    index_path(project: str, database: str, collection: str, index: str) -> str

Returns a fully-qualified index string.

### list_backup_schedules
    
    
    list_backup_schedules(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.ListBackupSchedulesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.types.firestore_admin.ListBackupSchedulesResponse

List backup schedules.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_list_backup_schedules():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.ListBackupSchedulesRequest(
            parent="parent_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[list_backup_schedules](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_list_backup_schedules)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.ListBackupSchedulesRequest, dict]`   
The request object. The request for `FirestoreAdmin.ListBackupSchedules][google.firestore.admin.v1.FirestoreAdmin.ListBackupSchedules]`.  
`parent` |  `str`   
Required. The parent database. Format is `projects/{project}/databases/{database}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.types.ListBackupSchedulesResponse` | The response for `FirestoreAdmin.ListBackupSchedules][google.firestore.admin.v1.FirestoreAdmin.ListBackupSchedules]`.  
  
### list_backups
    
    
    list_backups(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.ListBackupsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.types.firestore_admin.ListBackupsResponse

Lists all the backups.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_list_backups():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.ListBackupsRequest(
            parent="parent_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[list_backups](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_list_backups)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.ListBackupsRequest, dict]`   
The request object. The request for `FirestoreAdmin.ListBackups][google.firestore.admin.v1.FirestoreAdmin.ListBackups]`.  
`parent` |  `str`   
Required. The location to list backups from. Format is `projects/{project}/locations/{location}`. Use `{location} = '-'` to list backups from all locations for the given project. This allows listing backups from a single location or from all locations. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.types.ListBackupsResponse` | The response for `FirestoreAdmin.ListBackups][google.firestore.admin.v1.FirestoreAdmin.ListBackups]`.  
  
### list_databases
    
    
    list_databases(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.ListDatabasesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.types.firestore_admin.ListDatabasesResponse

List all the databases in the project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_list_databases():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.ListDatabasesRequest(
            parent="parent_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[list_databases](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_list_databases)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.ListDatabasesRequest, dict]`   
The request object. A request to list the Firestore Databases in all locations for a project.  
`parent` |  `str`   
Required. A parent name of the form `projects/{project_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.types.ListDatabasesResponse` | The list of databases for a project.  
  
### list_fields
    
    
    list_fields(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.ListFieldsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.services.firestore_admin.pagers.ListFieldsPager

Lists the field configuration and metadata for this database.

Currently, `FirestoreAdmin.ListFields][google.firestore.admin.v1.FirestoreAdmin.ListFields]` only supports listing fields that have been explicitly overridden. To issue this query, call `FirestoreAdmin.ListFields][google.firestore.admin.v1.FirestoreAdmin.ListFields]` with the filter set to `indexConfig.usesAncestorConfig:false` or `ttlConfig:*`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_list_fields():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.ListFieldsRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[list_fields](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_list_fields)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.ListFieldsRequest, dict]`   
The request object. The request for `FirestoreAdmin.ListFields][google.firestore.admin.v1.FirestoreAdmin.ListFields]`.  
`parent` |  `str`   
Required. A parent name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.services.firestore_admin.pagers.ListFieldsPager` | The response for `FirestoreAdmin.ListFields][google.firestore.admin.v1.FirestoreAdmin.ListFields]`. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_indexes
    
    
    list_indexes(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.ListIndexesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.services.firestore_admin.pagers.ListIndexesPager

Lists composite indexes.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_list_indexes():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.ListIndexesRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[list_indexes](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_list_indexes)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.ListIndexesRequest, dict]`   
The request object. The request for `FirestoreAdmin.ListIndexes][google.firestore.admin.v1.FirestoreAdmin.ListIndexes]`.  
`parent` |  `str`   
Required. A parent name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.services.firestore_admin.pagers.ListIndexesPager` | The response for `FirestoreAdmin.ListIndexes][google.firestore.admin.v1.FirestoreAdmin.ListIndexes]`. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### list_user_creds
    
    
    list_user_creds(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.ListUserCredsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.types.firestore_admin.ListUserCredsResponse

List all user creds in the database. Note that the returned resource does not contain the secret value itself.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_list_user_creds():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.ListUserCredsRequest(
            parent="parent_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[list_user_creds](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_list_user_creds)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.ListUserCredsRequest, dict]`   
The request object. The request for `FirestoreAdmin.ListUserCreds][google.firestore.admin.v1.FirestoreAdmin.ListUserCreds]`.  
`parent` |  `str`   
Required. A parent database name of the form `projects/{project_id}/databases/{database_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.types.ListUserCredsResponse` | The response for `FirestoreAdmin.ListUserCreds][google.firestore.admin.v1.FirestoreAdmin.ListUserCreds]`.  
  
### location_path
    
    
    location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

### operation_path
    
    
    operation_path(project: str, database: str, operation: str) -> str

Returns a fully-qualified operation string.

### parse_backup_path
    
    
    parse_backup_path(path: str) -> typing.Dict[str, str]

Parses a backup path into its component segments.

### parse_backup_schedule_path
    
    
    parse_backup_schedule_path(path: str) -> typing.Dict[str, str]

Parses a backup_schedule path into its component segments.

### parse_collection_group_path
    
    
    parse_collection_group_path(path: str) -> typing.Dict[str, str]

Parses a collection_group path into its component segments.

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

### parse_database_path
    
    
    parse_database_path(path: str) -> typing.Dict[str, str]

Parses a database path into its component segments.

### parse_field_path
    
    
    parse_field_path(path: str) -> typing.Dict[str, str]

Parses a field path into its component segments.

### parse_index_path
    
    
    parse_index_path(path: str) -> typing.Dict[str, str]

Parses a index path into its component segments.

### parse_location_path
    
    
    parse_location_path(path: str) -> typing.Dict[str, str]

Parses a location path into its component segments.

### parse_operation_path
    
    
    parse_operation_path(path: str) -> typing.Dict[str, str]

Parses a operation path into its component segments.

### parse_user_creds_path
    
    
    parse_user_creds_path(path: str) -> typing.Dict[str, str]

Parses a user_creds path into its component segments.

### reset_user_password
    
    
    reset_user_password(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.ResetUserPasswordRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.types.user_creds.UserCreds

Resets the password of a user creds.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_reset_user_password():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.ResetUserPasswordRequest(
            name="name_value",
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[reset_user_password](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_reset_user_password)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.ResetUserPasswordRequest, dict]`   
The request object. The request for `FirestoreAdmin.ResetUserPassword][google.firestore.admin.v1.FirestoreAdmin.ResetUserPassword]`.  
`name` |  `str`   
Required. A name of the form `projects/{project_id}/databases/{database_id}/userCreds/{user_creds_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.types.UserCreds` | A Cloud Firestore User Creds.  
  
### restore_database
    
    
    restore_database(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.RestoreDatabaseRequest,
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

Creates a new database by restoring from an existing backup.

The new database must be in the same cloud region or multi-region location as the existing backup. This behaves similar to `FirestoreAdmin.CreateDatabase][google.firestore.admin.v1.FirestoreAdmin.CreateDatabase]` except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing backup.

The `long-running operation][google.longrunning.Operation]` can be used to track the progress of the restore, with the Operation's `metadata][google.longrunning.Operation.metadata]` field type being the `RestoreDatabaseMetadata][google.firestore.admin.v1.RestoreDatabaseMetadata]`. The `response][google.longrunning.Operation.response]` type is the `Database][google.firestore.admin.v1.Database]` if the restore was successful. The new database is not readable or writeable until the LRO has completed.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_restore_database():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.RestoreDatabaseRequest(
            parent="parent_value",
            database_id="database_id_value",
            backup="backup_value",
        )
    
        # Make the request
        operation = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[restore_database](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_restore_database)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.RestoreDatabaseRequest, dict]`   
The request object. The request message for `FirestoreAdmin.RestoreDatabase][google.firestore.admin.v1.FirestoreAdmin.RestoreDatabase]`.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be Database A Cloud Firestore Database.  
  
### update_backup_schedule
    
    
    update_backup_schedule(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.UpdateBackupScheduleRequest,
                dict,
            ]
        ] = None,
        *,
        backup_schedule: typing.Optional[
            google.cloud.firestore_admin_v1.types.schedule.BackupSchedule
        ] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.firestore_admin_v1.types.schedule.BackupSchedule

Updates a backup schedule.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_update_backup_schedule():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.UpdateBackupScheduleRequest(
        )
    
        # Make the request
        response = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[update_backup_schedule](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_update_backup_schedule)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.UpdateBackupScheduleRequest, dict]`   
The request object. The request for `FirestoreAdmin.UpdateBackupSchedule][google.firestore.admin.v1.FirestoreAdmin.UpdateBackupSchedule]`.  
`backup_schedule` |  `google.cloud.firestore_admin_v1.types.BackupSchedule`   
Required. The backup schedule to update. This corresponds to the `backup_schedule` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
The list of fields to be updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.firestore_admin_v1.types.BackupSchedule` | A backup schedule for a Cloud Firestore Database. This resource is owned by the database it is backing up, and is deleted along with the database. The actual backups are not though.  
  
### update_database
    
    
    update_database(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.UpdateDatabaseRequest,
                dict,
            ]
        ] = None,
        *,
        database: typing.Optional[
            google.cloud.firestore_admin_v1.types.database.Database
        ] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Updates a database.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_update_database():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        request = firestore_admin_v1.UpdateDatabaseRequest(
        )
    
        # Make the request
        operation = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[update_database](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_update_database)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.UpdateDatabaseRequest, dict]`   
The request object. The request for `FirestoreAdmin.UpdateDatabase][google.firestore.admin.v1.FirestoreAdmin.UpdateDatabase]`.  
`database` |  `google.cloud.firestore_admin_v1.types.Database`   
Required. The database to update. This corresponds to the `database` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
The list of fields to be updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be Database A Cloud Firestore Database.  
  
### update_field
    
    
    update_field(
        request: typing.Optional[
            typing.Union[
                google.cloud.firestore_admin_v1.types.firestore_admin.UpdateFieldRequest,
                dict,
            ]
        ] = None,
        *,
        field: typing.Optional[google.cloud.firestore_admin_v1.types.field.Field] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Updates a field configuration. Currently, field updates apply only to single field index configuration. However, calls to `FirestoreAdmin.UpdateField][google.firestore.admin.v1.FirestoreAdmin.UpdateField]` should provide a field mask to avoid changing any configuration that the caller isn't aware of. The field mask should be specified as: `{ paths: "index_config" }`.

This call returns a `google.longrunning.Operation][google.longrunning.Operation]` which may be used to track the status of the field update. The metadata for the operation will be the type `FieldOperationMetadata][google.firestore.admin.v1.FieldOperationMetadata]`.

To configure the default field settings for the database, use the special `Field` with resource name: `projects/{project_id}/databases/{database_id}/collectionGroups/__default__/fields/*`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import firestore_admin_v1
    
    def sample_update_field():
        # Create a client
        client = firestore_admin_v1.[FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html)()
    
        # Initialize request argument(s)
        field = firestore_admin_v1.Field()
        field.name = "name_value"
    
        request = firestore_admin_v1.UpdateFieldRequest(
            field=field,
        )
    
        # Make the request
        operation = [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.html).[update_field](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.html#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_update_field)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[google.cloud.firestore_admin_v1.types.UpdateFieldRequest, dict]`   
The request object. The request for `FirestoreAdmin.UpdateField][google.firestore.admin.v1.FirestoreAdmin.UpdateField]`.  
`field` |  `google.cloud.firestore_admin_v1.types.Field`   
Required. The field to be updated. This corresponds to the `field` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be Field Represents a single field in the database. Fields are grouped by their "Collection Group", which represent all collections in the database with the same ID.  
  
### user_creds_path
    
    
    user_creds_path(project: str, database: str, user_creds: str) -> str

Returns a fully-qualified user_creds string.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
