---
url: https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient
title: Class DatabaseAdminClient (3.71.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:53.015401+00:00
---

# Class DatabaseAdminClient (3.71.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DatabaseAdminClient (3.71.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.71.0 (latest)  3.70.0  3.69.1  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.1  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.0  3.23.0  3.22.2  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.1  3.14.1  3.13.0  3.12.1  3.11.1  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.1.1  2.0.0  1.19.3  1.18.0  1.17.1  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0 
    
    
    DatabaseAdminClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.spanner_admin_database_v1.services.database_admin.transports.base.DatabaseAdminTransport,
                typing.Callable[
                    [...],
                    google.cloud.spanner_admin_database_v1.services.database_admin.transports.base.DatabaseAdminTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Cloud Spanner Database Admin API

The Cloud Spanner Database Admin API can be used to:

  * create, drop, and list databases
  * update the schema of pre-existing databases
  * create, delete, copy and list backups for a database
  * restore a database from an existing backup



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
`DatabaseAdminTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### DatabaseAdminClient
    
    
    DatabaseAdminClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.spanner_admin_database_v1.services.database_admin.transports.base.DatabaseAdminTransport,
                typing.Callable[
                    [...],
                    google.cloud.spanner_admin_database_v1.services.database_admin.transports.base.DatabaseAdminTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the database admin client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,DatabaseAdminTransport,Callable[..., DatabaseAdminTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the DatabaseAdminTransport constructor. If set to None, a transport is chosen automatically.  
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

### add_split_points
    
    
    add_split_points(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.spanner_database_admin.AddSplitPointsRequest,
                dict,
            ]
        ] = None,
        *,
        database: typing.Optional[str] = None,
        split_points: typing.Optional[
            typing.MutableSequence[
                google.cloud.spanner_admin_database_v1.types.spanner_database_admin.SplitPoints
            ]
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.spanner_admin_database_v1.types.spanner_database_admin.AddSplitPointsResponse
    )

Adds split points to specified tables, indexes of a database.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_add_split_points():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[AddSplitPointsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.AddSplitPointsRequest.html)(
            database="database_value",
        )
    
        # Make the request
        response = client.[add_split_points](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_add_split_points)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.AddSplitPointsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.AddSplitPointsRequest), dict]`   
The request object. The request for `AddSplitPoints][google.spanner.admin.database.v1.DatabaseAdmin.AddSplitPoints]`.  
`database` |  `str`   
Required. The database on whose tables/indexes split points are to be added. Values are of the form `projects/`. This corresponds to the `database` field on the `request` instance; if `request` is provided, this should not be set.  
`split_points` |  `MutableSequence[[google.cloud.spanner_admin_database_v1.types.SplitPoints](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.SplitPoints)]`   
Required. The split points to add. This corresponds to the `split_points` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.spanner_admin_database_v1.types.AddSplitPointsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.AddSplitPointsResponse)` | The response for `AddSplitPoints][google.spanner.admin.database.v1.DatabaseAdmin.AddSplitPoints]`.  
  
### backup_path
    
    
    backup_path(project: str, instance: str, backup: str) -> str

Returns a fully-qualified backup string.

### backup_schedule_path
    
    
    backup_schedule_path(
        project: str, instance: str, database: str, schedule: str
    ) -> str

Returns a fully-qualified backup_schedule string.

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

### copy_backup
    
    
    copy_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.backup.CopyBackupRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_id: typing.Optional[str] = None,
        source_backup: typing.Optional[str] = None,
        expire_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Starts copying a Cloud Spanner Backup. The returned backup `long-running operation][google.longrunning.Operation]` will have a name of the format `projects/<project>/instances/<instance>/backups/<backup>/operations/<operation_id>` and can be used to track copying of the backup. The operation is associated with the destination backup. The `metadata][google.longrunning.Operation.metadata]` field type is `CopyBackupMetadata][google.spanner.admin.database.v1.CopyBackupMetadata]`. The `response][google.longrunning.Operation.response]` field type is `Backup][google.spanner.admin.database.v1.Backup]`, if successful. Cancelling the returned operation will stop the copying and delete the destination backup. Concurrent CopyBackup requests can run on the same source backup.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_copy_backup():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[CopyBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CopyBackupRequest.html)(
            parent="parent_value",
            backup_id="backup_id_value",
            source_backup="source_backup_value",
        )
    
        # Make the request
        operation = client.[copy_backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_copy_backup)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.CopyBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CopyBackupRequest), dict]`   
The request object. The request for `CopyBackup][google.spanner.admin.database.v1.DatabaseAdmin.CopyBackup]`.  
`parent` |  `str`   
Required. The name of the destination instance that will contain the backup copy. Values are of the form: `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_id` |  `str`   
Required. The id of the backup copy. The `backup_id` appended to `parent` forms the full backup_uri of the form `projects/`. This corresponds to the `backup_id` field on the `request` instance; if `request` is provided, this should not be set.  
`source_backup` |  `str`   
Required. The source backup to be copied. The source backup needs to be in READY state for it to be copied. Once CopyBackup is in progress, the source backup cannot be deleted or cleaned up on expiration until CopyBackup is finished. Values are of the form: `projects/`. This corresponds to the `source_backup` field on the `request` instance; if `request` is provided, this should not be set.  
`expire_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Required. The expiration time of the backup in microsecond granularity. The expiration time must be at least 6 hours and at most 366 days from the `create_time` of the source backup. Once the `expire_time` has passed, the backup is eligible to be automatically deleted by Cloud Spanner to free the resources used by the backup. This corresponds to the `expire_time` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Backup) A backup of a Cloud Spanner database.  
  
### create_backup
    
    
    create_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.backup.CreateBackupRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup: typing.Optional[
            google.cloud.spanner_admin_database_v1.types.backup.Backup
        ] = None,
        backup_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Starts creating a new Cloud Spanner Backup. The returned backup `long-running operation][google.longrunning.Operation]` will have a name of the format `projects/<project>/instances/<instance>/backups/<backup>/operations/<operation_id>` and can be used to track creation of the backup. The `metadata][google.longrunning.Operation.metadata]` field type is `CreateBackupMetadata][google.spanner.admin.database.v1.CreateBackupMetadata]`. The `response][google.longrunning.Operation.response]` field type is `Backup][google.spanner.admin.database.v1.Backup]`, if successful. Cancelling the returned operation will stop the creation and delete the backup. There can be only one pending backup creation per database. Backup creation of different databases can run concurrently.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_create_backup():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[CreateBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupRequest.html)(
            parent="parent_value",
            backup_id="backup_id_value",
        )
    
        # Make the request
        operation = client.[create_backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_create_backup)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.CreateBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupRequest), dict]`   
The request object. The request for `CreateBackup][google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup]`.  
`parent` |  `str`   
Required. The name of the instance in which the backup will be created. This must be the same instance that contains the database the backup will be created from. The backup will be stored in the location(s) specified in the instance configuration of this instance. Values are of the form `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`backup` |  `[google.cloud.spanner_admin_database_v1.types.Backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Backup)`   
Required. The backup to create. This corresponds to the `backup` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_id` |  `str`   
Required. The id of the backup to be created. The `backup_id` appended to `parent` forms the full backup name of the form `projects/`. This corresponds to the `backup_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Backup) A backup of a Cloud Spanner database.  
  
### create_backup_schedule
    
    
    create_backup_schedule(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.backup_schedule.CreateBackupScheduleRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_schedule: typing.Optional[
            google.cloud.spanner_admin_database_v1.types.backup_schedule.BackupSchedule
        ] = None,
        backup_schedule_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.spanner_admin_database_v1.types.backup_schedule.BackupSchedule

Creates a new backup schedule.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_create_backup_schedule():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[CreateBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupScheduleRequest.html)(
            parent="parent_value",
            backup_schedule_id="backup_schedule_id_value",
        )
    
        # Make the request
        response = client.[create_backup_schedule](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_create_backup_schedule)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.CreateBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupScheduleRequest), dict]`   
The request object. The request for `CreateBackupSchedule][google.spanner.admin.database.v1.DatabaseAdmin.CreateBackupSchedule]`.  
`parent` |  `str`   
Required. The name of the database that this backup schedule applies to. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_schedule` |  `[google.cloud.spanner_admin_database_v1.types.BackupSchedule](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.BackupSchedule)`   
Required. The backup schedule to create. This corresponds to the `backup_schedule` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_schedule_id` |  `str`   
Required. The Id to use for the backup schedule. The `backup_schedule_id` appended to `parent` forms the full backup schedule name of the form `projects/`. This corresponds to the `backup_schedule_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.spanner_admin_database_v1.types.BackupSchedule](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.BackupSchedule)` | BackupSchedule expresses the automated backup creation specification for a Spanner database. Next ID: 10  
  
### create_database
    
    
    create_database(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.spanner_database_admin.CreateDatabaseRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        create_statement: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Cloud Spanner database and starts to prepare it for serving. The returned [long-running operation][google.longrunning.Operation] will have a name of the format `<database_name>/operations/<operation_id>` and can be used to track preparation of the database. The `metadata][google.longrunning.Operation.metadata]` field type is `CreateDatabaseMetadata][google.spanner.admin.database.v1.CreateDatabaseMetadata]`. The `response][google.longrunning.Operation.response]` field type is `Database][google.spanner.admin.database.v1.Database]`, if successful.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_create_database():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[CreateDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateDatabaseRequest.html)(
            parent="parent_value",
            create_statement="create_statement_value",
        )
    
        # Make the request
        operation = client.[create_database](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_create_database)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.CreateDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateDatabaseRequest), dict]`   
The request object. The request for `CreateDatabase][google.spanner.admin.database.v1.DatabaseAdmin.CreateDatabase]`.  
`parent` |  `str`   
Required. The name of the instance that will serve the new database. Values are of the form `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`create_statement` |  `str`   
Required. A `CREATE DATABASE` statement, which specifies the ID of the new database. The database ID must conform to the regular expression `[a-z][a-z0-9_-]*[a-z0-9]` and be between 2 and 30 characters in length. If the database ID is a reserved word or if it contains a hyphen, the database ID must be enclosed in backticks (:literal:`</code>). This corresponds to the `create_statement` field on the `request` instance; if `request` is provided, this should not be set.`` `  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Database](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Database) A Cloud Spanner database.  
  
### crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

### crypto_key_version_path
    
    
    crypto_key_version_path(
        project: str, location: str, key_ring: str, crypto_key: str, crypto_key_version: str
    ) -> str

Returns a fully-qualified crypto_key_version string.

### database_path
    
    
    database_path(project: str, instance: str, database: str) -> str

Returns a fully-qualified database string.

### database_role_path
    
    
    database_role_path(project: str, instance: str, database: str, role: str) -> str

Returns a fully-qualified database_role string.

### delete_backup
    
    
    delete_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.backup.DeleteBackupRequest,
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

Deletes a pending or completed `Backup][google.spanner.admin.database.v1.Backup]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_delete_backup():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.DeleteBackupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_delete_backup)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.DeleteBackupRequest), dict]`   
The request object. The request for `DeleteBackup][google.spanner.admin.database.v1.DatabaseAdmin.DeleteBackup]`.  
`name` |  `str`   
Required. Name of the backup to delete. Values are of the form `projects/`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
                google.cloud.spanner_admin_database_v1.types.backup_schedule.DeleteBackupScheduleRequest,
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
    from google.cloud import spanner_admin_database_v1
    
    def sample_delete_backup_schedule():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[DeleteBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.DeleteBackupScheduleRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_backup_schedule](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_delete_backup_schedule)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.DeleteBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.DeleteBackupScheduleRequest), dict]`   
The request object. The request for `DeleteBackupSchedule][google.spanner.admin.database.v1.DatabaseAdmin.DeleteBackupSchedule]`.  
`name` |  `str`   
Required. The name of the schedule to delete. Values are of the form `projects/`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### drop_database
    
    
    drop_database(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.spanner_database_admin.DropDatabaseRequest,
                dict,
            ]
        ] = None,
        *,
        database: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Drops (aka deletes) a Cloud Spanner database. Completed backups for the database will be retained according to their `expire_time`. Note: Cloud Spanner might continue to accept requests for a few seconds after the database has been deleted.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_drop_database():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[DropDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.DropDatabaseRequest.html)(
            database="database_value",
        )
    
        # Make the request
        client.[drop_database](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_drop_database)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.DropDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.DropDatabaseRequest), dict]`   
The request object. The request for `DropDatabase][google.spanner.admin.database.v1.DatabaseAdmin.DropDatabase]`.  
`database` |  `str`   
Required. The database to be dropped. This corresponds to the `database` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
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
`DatabaseAdminClient` | The constructed client.  
  
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
`DatabaseAdminClient` | The constructed client.  
  
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
`DatabaseAdminClient` | The constructed client.  
  
### get_backup
    
    
    get_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.backup.GetBackupRequest, dict
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
    ) -> google.cloud.spanner_admin_database_v1.types.backup.Backup

Gets metadata on a pending or completed `Backup][google.spanner.admin.database.v1.Backup]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_get_backup():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.GetBackupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_get_backup)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.GetBackupRequest), dict]`   
The request object. The request for `GetBackup][google.spanner.admin.database.v1.DatabaseAdmin.GetBackup]`.  
`name` |  `str`   
Required. Name of the backup. Values are of the form `projects/`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.spanner_admin_database_v1.types.Backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Backup)` | A backup of a Cloud Spanner database.  
  
### get_backup_schedule
    
    
    get_backup_schedule(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.backup_schedule.GetBackupScheduleRequest,
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
    ) -> google.cloud.spanner_admin_database_v1.types.backup_schedule.BackupSchedule

Gets backup schedule for the input schedule name.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_get_backup_schedule():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[GetBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.GetBackupScheduleRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_backup_schedule](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_get_backup_schedule)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.GetBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.GetBackupScheduleRequest), dict]`   
The request object. The request for `GetBackupSchedule][google.spanner.admin.database.v1.DatabaseAdmin.GetBackupSchedule]`.  
`name` |  `str`   
Required. The name of the schedule to retrieve. Values are of the form `projects/`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.spanner_admin_database_v1.types.BackupSchedule](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.BackupSchedule)` | BackupSchedule expresses the automated backup creation specification for a Spanner database. Next ID: 10  
  
### get_database
    
    
    get_database(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.spanner_database_admin.GetDatabaseRequest,
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
    ) -> google.cloud.spanner_admin_database_v1.types.spanner_database_admin.Database

Gets the state of a Cloud Spanner database.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_get_database():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[GetDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.GetDatabaseRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_database](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_get_database)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.GetDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.GetDatabaseRequest), dict]`   
The request object. The request for `GetDatabase][google.spanner.admin.database.v1.DatabaseAdmin.GetDatabase]`.  
`name` |  `str`   
Required. The name of the requested database. Values are of the form `projects/`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.spanner_admin_database_v1.types.Database](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Database)` | A Cloud Spanner database.  
  
### get_database_ddl
    
    
    get_database_ddl(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.spanner_database_admin.GetDatabaseDdlRequest,
                dict,
            ]
        ] = None,
        *,
        database: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.spanner_admin_database_v1.types.spanner_database_admin.GetDatabaseDdlResponse
    )

Returns the schema of a Cloud Spanner database as a list of formatted DDL statements. This method does not show pending schema updates, those may be queried using the `Operations][google.longrunning.Operations]` API.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_get_database_ddl():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[GetDatabaseDdlRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.GetDatabaseDdlRequest.html)(
            database="database_value",
        )
    
        # Make the request
        response = client.[get_database_ddl](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_get_database_ddl)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.GetDatabaseDdlRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.GetDatabaseDdlRequest), dict]`   
The request object. The request for `GetDatabaseDdl][google.spanner.admin.database.v1.DatabaseAdmin.GetDatabaseDdl]`.  
`database` |  `str`   
Required. The database whose schema we wish to get. Values are of the form `projects/` This corresponds to the `database` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.spanner_admin_database_v1.types.GetDatabaseDdlResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.GetDatabaseDdlResponse)` | The response for `GetDatabaseDdl][google.spanner.admin.database.v1.DatabaseAdmin.GetDatabaseDdl]`.  
  
### get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Gets the access control policy for a database or backup resource. Returns an empty policy if a database or backup exists but does not have a policy set.

Authorization requires `spanner.databases.getIamPolicy` permission on `resource][google.iam.v1.GetIamPolicyRequest.resource]`. For backups, authorization requires `spanner.backups.getIamPolicy` permission on `resource][google.iam.v1.GetIamPolicyRequest.resource]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    def sample_get_iam_policy():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.GetIamPolicyRequest(
            resource="resource_value",
        )
    
        # Make the request
        response = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_get_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L111-L118), dict]`   
The request object. Request message for `GetIamPolicy` method.  
`resource` |  `str`   
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.iam.v1.policy_pb2.Policy` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
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
  
### instance_partition_path
    
    
    instance_partition_path(
        project: str, instance: str, instance_partition: str
    ) -> str

Returns a fully-qualified instance_partition string.

### instance_path
    
    
    instance_path(project: str, instance: str) -> str

Returns a fully-qualified instance string.

### internal_update_graph_operation
    
    
    internal_update_graph_operation(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.spanner_database_admin.InternalUpdateGraphOperationRequest,
                dict,
            ]
        ] = None,
        *,
        database: typing.Optional[str] = None,
        operation_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.spanner_admin_database_v1.types.spanner_database_admin.InternalUpdateGraphOperationResponse
    )

This is an internal API called by Spanner Graph jobs. You should never need to call this API directly.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_internal_update_graph_operation():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[InternalUpdateGraphOperationRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.InternalUpdateGraphOperationRequest.html)(
            database="database_value",
            operation_id="operation_id_value",
            vm_identity_token="vm_identity_token_value",
        )
    
        # Make the request
        response = client.[internal_update_graph_operation](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_internal_update_graph_operation)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.InternalUpdateGraphOperationRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.InternalUpdateGraphOperationRequest), dict]`   
The request object. Internal request proto, do not use directly.  
`database` |  `str`   
Internal field, do not use directly. This corresponds to the `database` field on the `request` instance; if `request` is provided, this should not be set.  
`operation_id` |  `str`   
Internal field, do not use directly. This corresponds to the `operation_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.spanner_admin_database_v1.types.InternalUpdateGraphOperationResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.InternalUpdateGraphOperationResponse)` | Internal response proto, do not use directly.  
  
### list_backup_operations
    
    
    list_backup_operations(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.backup.ListBackupOperationsRequest,
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
    ) -> (
        google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupOperationsPager
    )

Lists the backup [long-running operations][google.longrunning.Operation] in the given instance. A backup operation has a name of the form `projects/<project>/instances/<instance>/backups/<backup>/operations/<operation>`. The long-running operation `metadata][google.longrunning.Operation.metadata]` field type `metadata.type_url` describes the type of the metadata. Operations returned include those that have completed/failed/canceled within the last 7 days, and pending operations. Operations returned are ordered by `operation.metadata.value.progress.start_time` in descending order starting from the most recently started operation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_list_backup_operations():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[ListBackupOperationsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupOperationsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_backup_operations](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_list_backup_operations)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.ListBackupOperationsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupOperationsRequest), dict]`   
The request object. The request for `ListBackupOperations][google.spanner.admin.database.v1.DatabaseAdmin.ListBackupOperations]`.  
`parent` |  `str`   
Required. The instance of the backup operations. Values are of the form `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupOperationsPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupOperationsPager)` | The response for `ListBackupOperations][google.spanner.admin.database.v1.DatabaseAdmin.ListBackupOperations]`. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_backup_schedules
    
    
    list_backup_schedules(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.backup_schedule.ListBackupSchedulesRequest,
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
    ) -> (
        google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupSchedulesPager
    )

Lists all the backup schedules for the database.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_list_backup_schedules():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[ListBackupSchedulesRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupSchedulesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_backup_schedules](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_list_backup_schedules)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.ListBackupSchedulesRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupSchedulesRequest), dict]`   
The request object. The request for `ListBackupSchedules][google.spanner.admin.database.v1.DatabaseAdmin.ListBackupSchedules]`.  
`parent` |  `str`   
Required. Database is the parent resource whose backup schedules should be listed. Values are of the form projects/  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupSchedulesPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupSchedulesPager)` | The response for `ListBackupSchedules][google.spanner.admin.database.v1.DatabaseAdmin.ListBackupSchedules]`. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_backups
    
    
    list_backups(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.backup.ListBackupsRequest, dict
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
    ) -> (
        google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupsPager
    )

Lists completed and pending backups. Backups returned are ordered by `create_time` in descending order, starting from the most recent `create_time`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_list_backups():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_backups](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_list_backups)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupsRequest), dict]`   
The request object. The request for `ListBackups][google.spanner.admin.database.v1.DatabaseAdmin.ListBackups]`.  
`parent` |  `str`   
Required. The instance to list backups from. Values are of the form `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupsPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupsPager)` | The response for `ListBackups][google.spanner.admin.database.v1.DatabaseAdmin.ListBackups]`. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_database_operations
    
    
    list_database_operations(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabaseOperationsRequest,
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
    ) -> (
        google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseOperationsPager
    )

Lists database `longrunning-operations][google.longrunning.Operation]`. A database operation has a name of the form `projects/<project>/instances/<instance>/databases/<database>/operations/<operation>`. The long-running operation `metadata][google.longrunning.Operation.metadata]` field type `metadata.type_url` describes the type of the metadata. Operations returned include those that have completed/failed/canceled within the last 7 days, and pending operations.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_list_database_operations():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[ListDatabaseOperationsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabaseOperationsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_database_operations](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_list_database_operations)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.ListDatabaseOperationsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabaseOperationsRequest), dict]`   
The request object. The request for `ListDatabaseOperations][google.spanner.admin.database.v1.DatabaseAdmin.ListDatabaseOperations]`.  
`parent` |  `str`   
Required. The instance of the database operations. Values are of the form `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseOperationsPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseOperationsPager)` | The response for `ListDatabaseOperations][google.spanner.admin.database.v1.DatabaseAdmin.ListDatabaseOperations]`. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_database_roles
    
    
    list_database_roles(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabaseRolesRequest,
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
    ) -> (
        google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseRolesPager
    )

Lists Cloud Spanner database roles.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_list_database_roles():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[ListDatabaseRolesRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabaseRolesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_database_roles](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_list_database_roles)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.ListDatabaseRolesRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabaseRolesRequest), dict]`   
The request object. The request for `ListDatabaseRoles][google.spanner.admin.database.v1.DatabaseAdmin.ListDatabaseRoles]`.  
`parent` |  `str`   
Required. The database whose roles should be listed. Values are of the form `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseRolesPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseRolesPager)` | The response for `ListDatabaseRoles][google.spanner.admin.database.v1.DatabaseAdmin.ListDatabaseRoles]`. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_databases
    
    
    list_databases(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabasesRequest,
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
    ) -> (
        google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabasesPager
    )

Lists Cloud Spanner databases.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_list_databases():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[ListDatabasesRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabasesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_databases](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_list_databases)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.ListDatabasesRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabasesRequest), dict]`   
The request object. The request for `ListDatabases][google.spanner.admin.database.v1.DatabaseAdmin.ListDatabases]`.  
`parent` |  `str`   
Required. The instance whose databases should be listed. Values are of the form `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabasesPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabasesPager)` | The response for `ListDatabases][google.spanner.admin.database.v1.DatabaseAdmin.ListDatabases]`. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### parse_backup_path
    
    
    parse_backup_path(path: str) -> typing.Dict[str, str]

Parses a backup path into its component segments.

### parse_backup_schedule_path
    
    
    parse_backup_schedule_path(path: str) -> typing.Dict[str, str]

Parses a backup_schedule path into its component segments.

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

### parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

### parse_crypto_key_version_path
    
    
    parse_crypto_key_version_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key_version path into its component segments.

### parse_database_path
    
    
    parse_database_path(path: str) -> typing.Dict[str, str]

Parses a database path into its component segments.

### parse_database_role_path
    
    
    parse_database_role_path(path: str) -> typing.Dict[str, str]

Parses a database_role path into its component segments.

### parse_instance_partition_path
    
    
    parse_instance_partition_path(path: str) -> typing.Dict[str, str]

Parses a instance_partition path into its component segments.

### parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

### restore_database
    
    
    restore_database(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.spanner_database_admin.RestoreDatabaseRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        database_id: typing.Optional[str] = None,
        backup: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Create a new database by restoring from a completed backup. The new database must be in the same project and in an instance with the same instance configuration as the instance containing the backup. The returned database [long-running operation][google.longrunning.Operation] has a name of the format `projects/<project>/instances/<instance>/databases/<database>/operations/<operation_id>`, and can be used to track the progress of the operation, and to cancel it. The `metadata][google.longrunning.Operation.metadata]` field type is `RestoreDatabaseMetadata][google.spanner.admin.database.v1.RestoreDatabaseMetadata]`. The `response][google.longrunning.Operation.response]` type is `Database][google.spanner.admin.database.v1.Database]`, if successful. Cancelling the returned operation will stop the restore and delete the database. There can be only one database being restored into an instance at a time. Once the restore operation completes, a new restore operation can be initiated, without waiting for the optimize operation associated with the first restore to complete.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_restore_database():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[RestoreDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.RestoreDatabaseRequest.html)(
            backup="backup_value",
            parent="parent_value",
            database_id="database_id_value",
        )
    
        # Make the request
        operation = client.[restore_database](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_restore_database)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.RestoreDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.RestoreDatabaseRequest), dict]`   
The request object. The request for `RestoreDatabase][google.spanner.admin.database.v1.DatabaseAdmin.RestoreDatabase]`.  
`parent` |  `str`   
Required. The name of the instance in which to create the restored database. This instance must be in the same project and have the same instance configuration as the instance containing the source backup. Values are of the form `projects/`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`database_id` |  `str`   
Required. The id of the database to create and restore to. This database must not already exist. The `database_id` appended to `parent` forms the full database name of the form `projects/`. This corresponds to the `database_id` field on the `request` instance; if `request` is provided, this should not be set.  
`backup` |  `str`   
Name of the backup from which to restore. Values are of the form `projects/`. This corresponds to the `backup` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Database](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Database) A Cloud Spanner database.  
  
### set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Sets the access control policy on a database or backup resource. Replaces any existing policy.

Authorization requires `spanner.databases.setIamPolicy` permission on `resource][google.iam.v1.SetIamPolicyRequest.resource]`. For backups, authorization requires `spanner.backups.setIamPolicy` permission on `resource][google.iam.v1.SetIamPolicyRequest.resource]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    def sample_set_iam_policy():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.SetIamPolicyRequest(
            resource="resource_value",
        )
    
        # Make the request
        response = client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_set_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L103-L109), dict]`   
The request object. Request message for `SetIamPolicy` method.  
`resource` |  `str`   
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.iam.v1.policy_pb2.Policy` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
### test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        permissions: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Returns permissions that the caller has on the specified database or backup resource.

Attempting this RPC on a non-existent Cloud Spanner database will result in a NOT_FOUND error if the user has `spanner.databases.list` permission on the containing Cloud Spanner instance. Otherwise returns an empty set of permissions. Calling this method on a backup that does not exist will result in a NOT_FOUND error if the user has `spanner.backups.list` permission on the containing instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    def sample_test_iam_permissions():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.TestIamPermissionsRequest(
            resource="resource_value",
            permissions=['permissions_value1', 'permissions_value2'],
        )
    
        # Make the request
        response = client.[test_iam_permissions](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_test_iam_permissions)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L120-L131), dict]`   
The request object. Request message for `TestIamPermissions` method.  
`resource` |  `str`   
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`permissions` |  `MutableSequence[str]`   
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see `IAM Overview <https://cloud.google.com/iam/docs/overview#permissions>`__. This corresponds to the `permissions` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L120-L131)` | Response message for TestIamPermissions method.  
  
### update_backup
    
    
    update_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.backup.UpdateBackupRequest,
                dict,
            ]
        ] = None,
        *,
        backup: typing.Optional[
            google.cloud.spanner_admin_database_v1.types.backup.Backup
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
    ) -> google.cloud.spanner_admin_database_v1.types.backup.Backup

Updates a pending or completed `Backup][google.spanner.admin.database.v1.Backup]`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_update_backup():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[UpdateBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.UpdateBackupRequest.html)(
        )
    
        # Make the request
        response = client.[update_backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_update_backup)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.UpdateBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.UpdateBackupRequest), dict]`   
The request object. The request for `UpdateBackup][google.spanner.admin.database.v1.DatabaseAdmin.UpdateBackup]`.  
`backup` |  `[google.cloud.spanner_admin_database_v1.types.Backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Backup)`   
Required. The backup to update. `backup.name`, and the fields to be updated as specified by `update_mask` are required. Other fields are ignored. Update is only supported for the following fields: - `backup.expire_time`. This corresponds to the `backup` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. A mask specifying which fields (e.g. `expire_time`) in the Backup resource should be updated. This mask is relative to the Backup resource, not to the request message. The field mask must always be specified; this prevents any future fields from being erased accidentally by clients that do not know about them. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.spanner_admin_database_v1.types.Backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Backup)` | A backup of a Cloud Spanner database.  
  
### update_backup_schedule
    
    
    update_backup_schedule(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.backup_schedule.UpdateBackupScheduleRequest,
                dict,
            ]
        ] = None,
        *,
        backup_schedule: typing.Optional[
            google.cloud.spanner_admin_database_v1.types.backup_schedule.BackupSchedule
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
    ) -> google.cloud.spanner_admin_database_v1.types.backup_schedule.BackupSchedule

Updates a backup schedule.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_update_backup_schedule():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[UpdateBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.UpdateBackupScheduleRequest.html)(
        )
    
        # Make the request
        response = client.[update_backup_schedule](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_update_backup_schedule)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.UpdateBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.UpdateBackupScheduleRequest), dict]`   
The request object. The request for `UpdateBackupScheduleRequest][google.spanner.admin.database.v1.DatabaseAdmin.UpdateBackupSchedule]`.  
`backup_schedule` |  `[google.cloud.spanner_admin_database_v1.types.BackupSchedule](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.BackupSchedule)`   
Required. The backup schedule to update. `backup_schedule.name`, and the fields to be updated as specified by `update_mask` are required. Other fields are ignored. This corresponds to the `backup_schedule` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. A mask specifying which fields in the BackupSchedule resource should be updated. This mask is relative to the BackupSchedule resource, not to the request message. The field mask must always be specified; this prevents any future fields from being erased accidentally. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.spanner_admin_database_v1.types.BackupSchedule](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.BackupSchedule)` | BackupSchedule expresses the automated backup creation specification for a Spanner database. Next ID: 10  
  
### update_database
    
    
    update_database(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.spanner_database_admin.UpdateDatabaseRequest,
                dict,
            ]
        ] = None,
        *,
        database: typing.Optional[
            google.cloud.spanner_admin_database_v1.types.spanner_database_admin.Database
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

Updates a Cloud Spanner database. The returned [long-running operation][google.longrunning.Operation] can be used to track the progress of updating the database. If the named database does not exist, returns `NOT_FOUND`.

While the operation is pending:

  * The database's `reconciling][google.spanner.admin.database.v1.Database.reconciling]` field is set to true.
  * Cancelling the operation is best-effort. If the cancellation succeeds, the operation metadata's `cancel_time][google.spanner.admin.database.v1.UpdateDatabaseMetadata.cancel_time]` is set, the updates are reverted, and the operation terminates with a `CANCELLED` status.
  * New UpdateDatabase requests will return a `FAILED_PRECONDITION` error until the pending operation is done (returns successfully or with error).
  * Reading the database via the API continues to give the pre-request values.



Upon completion of the returned operation:

  * The new values are in effect and readable via the API.
  * The database's `reconciling][google.spanner.admin.database.v1.Database.reconciling]` field becomes false.



The returned [long-running operation][google.longrunning.Operation] will have a name of the format `projects/<project>/instances/<instance>/databases/<database>/operations/<operation_id>` and can be used to track the database modification. The `metadata][google.longrunning.Operation.metadata]` field type is `UpdateDatabaseMetadata][google.spanner.admin.database.v1.UpdateDatabaseMetadata]`. The `response][google.longrunning.Operation.response]` field type is `Database][google.spanner.admin.database.v1.Database]`, if successful.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_update_database():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        database = spanner_admin_database_v1.[Database](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Database.html)()
        database.name = "name_value"
    
        request = spanner_admin_database_v1.[UpdateDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.UpdateDatabaseRequest.html)(
            database=database,
        )
    
        # Make the request
        operation = client.[update_database](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_update_database)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.UpdateDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.UpdateDatabaseRequest), dict]`   
The request object. The request for `UpdateDatabase][google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabase]`.  
`database` |  `[google.cloud.spanner_admin_database_v1.types.Database](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Database)`   
Required. The database to update. The `name` field of the database is of the form `projects/`. This corresponds to the `database` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. The list of fields to update. Currently, only `enable_drop_protection` field can be updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Database](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Database) A Cloud Spanner database.  
  
### update_database_ddl
    
    
    update_database_ddl(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_database_v1.types.spanner_database_admin.UpdateDatabaseDdlRequest,
                dict,
            ]
        ] = None,
        *,
        database: typing.Optional[str] = None,
        statements: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Updates the schema of a Cloud Spanner database by creating/altering/dropping tables, columns, indexes, etc. The returned `long-running operation][google.longrunning.Operation]` will have a name of the format `<database_name>/operations/<operation_id>` and can be used to track execution of the schema change(s). The `metadata][google.longrunning.Operation.metadata]` field type is `UpdateDatabaseDdlMetadata][google.spanner.admin.database.v1.UpdateDatabaseDdlMetadata]`. The operation has no response.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import spanner_admin_database_v1
    
    def sample_update_database_ddl():
        # Create a client
        client = spanner_admin_database_v1.[DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html)()
    
        # Initialize request argument(s)
        request = spanner_admin_database_v1.[UpdateDatabaseDdlRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.UpdateDatabaseDdlRequest.html)(
            database="database_value",
            statements=['statements_value1', 'statements_value2'],
        )
    
        # Make the request
        operation = client.[update_database_ddl](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.html#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_update_database_ddl)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.spanner_admin_database_v1.types.UpdateDatabaseDdlRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.UpdateDatabaseDdlRequest), dict]`   
The request object. Enqueues the given DDL statements to be applied, in order but not necessarily all at once, to the database schema at some point (or points) in the future. The server checks that the statements are executable (syntactically valid, name tables that exist, etc.) before enqueueing them, but they may still fail upon later execution (e.g., if a statement from another batch of statements is applied first and it conflicts in some way, or if there is some data-related problem like a `NULL` value in a column to which `NOT NULL` would be added). If a statement fails, all subsequent statements in the batch are automatically cancelled. Each batch of statements is assigned a name which can be used with the `Operations][google.longrunning.Operations]` API to monitor progress. See the `operation_id][google.spanner.admin.database.v1.UpdateDatabaseDdlRequest.operation_id]` field for more details.  
`database` |  `str`   
Required. The database to update. This corresponds to the `database` field on the `request` instance; if `request` is provided, this should not be set.  
`statements` |  `MutableSequence[str]`   
Required. DDL statements to be applied to the database. This corresponds to the `statements` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
