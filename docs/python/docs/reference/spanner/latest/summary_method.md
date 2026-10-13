---
url: https://docs.cloud.google.com/python/docs/reference/spanner/latest/summary_method/
title: Package Methods (3.71.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:49:12.213902+00:00
---

# Package Methods (3.71.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/spanner/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (3.71.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.71.0 (latest)  3.70.0  3.69.1  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.1  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.0  3.23.0  3.22.2  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.1  3.14.1  3.13.0  3.12.1  3.11.1  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.1.1  2.0.0  1.19.3  1.18.0  1.17.1  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0 

Summary of entries of Methods for spanner.

## 

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient
    
    
    DatabaseAdminAsyncClient(
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
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the database admin async client.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_DatabaseAdminAsyncClient)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.add_split_points
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.spanner_admin_database_v1.types.spanner_database_admin.AddSplitPointsResponse
    )

Adds split points to specified tables, indexes of a database.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.add_split_points](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_add_split_points)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.backup_path
    
    
    backup_path(project: str, instance: str, backup: str) -> str

Returns a fully-qualified backup string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.backup_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_backup_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.backup_schedule_path
    
    
    backup_schedule_path(
        project: str, instance: str, database: str, schedule: str
    ) -> str

Returns a fully-qualified backup_schedule string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.backup_schedule_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_backup_schedule_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_cancel_operation)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_common_billing_account_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_common_folder_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_common_location_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_common_organization_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_common_project_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.copy_backup
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Starts copying a Cloud Spanner Backup.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.copy_backup](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_copy_backup)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.create_backup
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Starts creating a new Cloud Spanner Backup.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.create_backup](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_create_backup)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.create_backup_schedule
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.spanner_admin_database_v1.types.backup_schedule.BackupSchedule

Creates a new backup schedule.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.create_backup_schedule](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_create_backup_schedule)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.create_database
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Cloud Spanner database and starts to prepare it for serving.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.create_database](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_create_database)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.crypto_key_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_crypto_key_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.crypto_key_version_path
    
    
    crypto_key_version_path(
        project: str, location: str, key_ring: str, crypto_key: str, crypto_key_version: str
    ) -> str

Returns a fully-qualified crypto_key_version string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.crypto_key_version_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_crypto_key_version_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.database_path
    
    
    database_path(project: str, instance: str, database: str) -> str

Returns a fully-qualified database string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.database_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_database_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.database_role_path
    
    
    database_role_path(project: str, instance: str, database: str, role: str) -> str

Returns a fully-qualified database_role string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.database_role_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_database_role_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.delete_backup
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes a pending or completed `Backup][google.spanner.admin.database.v1.Backup]`.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.delete_backup](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_delete_backup)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.delete_backup_schedule
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes a backup schedule.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.delete_backup_schedule](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_delete_backup_schedule)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.delete_operation
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_delete_operation)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.drop_database
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Drops (aka deletes) a Cloud Spanner database.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.drop_database](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_drop_database)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_from_service_account_file)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_from_service_account_info)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_from_service_account_json)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.get_backup
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.spanner_admin_database_v1.types.backup.Backup

Gets metadata on a pending or completed `Backup][google.spanner.admin.database.v1.Backup]`.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.get_backup](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_get_backup)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.get_backup_schedule
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.spanner_admin_database_v1.types.backup_schedule.BackupSchedule

Gets backup schedule for the input schedule name.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.get_backup_schedule](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_get_backup_schedule)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.get_database
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.spanner_admin_database_v1.types.spanner_database_admin.Database

Gets the state of a Cloud Spanner database.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.get_database](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_get_database)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.get_database_ddl
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.spanner_admin_database_v1.types.spanner_database_admin.GetDatabaseDdlResponse
    )

Returns the schema of a Cloud Spanner database as a list of formatted DDL statements.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.get_database_ddl](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_get_database_ddl)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Gets the access control policy for a database or backup resource.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_get_iam_policy)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.get_operation
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_get_operation)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.spanner_admin_database_v1.services.database_admin.transports.base.DatabaseAdminTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_get_transport_class)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.instance_partition_path
    
    
    instance_partition_path(
        project: str, instance: str, instance_partition: str
    ) -> str

Returns a fully-qualified instance_partition string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.instance_partition_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_instance_partition_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.instance_path
    
    
    instance_path(project: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.instance_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_instance_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.internal_update_graph_operation
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.spanner_admin_database_v1.types.spanner_database_admin.InternalUpdateGraphOperationResponse
    )

This is an internal API called by Spanner Graph jobs.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.internal_update_graph_operation](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_internal_update_graph_operation)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.list_backup_operations
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupOperationsAsyncPager
    )

Lists the backup [long-running operations][google.longrunning.Operation] in the given instance.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.list_backup_operations](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_list_backup_operations)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.list_backup_schedules
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupSchedulesAsyncPager
    )

Lists all the backup schedules for the database.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.list_backup_schedules](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_list_backup_schedules)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.list_backups
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupsAsyncPager
    )

Lists completed and pending backups.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.list_backups](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_list_backups)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.list_database_operations
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseOperationsAsyncPager
    )

Lists database `longrunning-operations][google.longrunning.Operation]`.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.list_database_operations](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_list_database_operations)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.list_database_roles
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseRolesAsyncPager
    )

Lists Cloud Spanner database roles.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.list_database_roles](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_list_database_roles)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.list_databases
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabasesAsyncPager
    )

Lists Cloud Spanner databases.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.list_databases](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_list_databases)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.list_operations
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_list_operations)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_backup_path
    
    
    parse_backup_path(path: str) -> typing.Dict[str, str]

Parses a backup path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_backup_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_parse_backup_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_backup_schedule_path
    
    
    parse_backup_schedule_path(path: str) -> typing.Dict[str, str]

Parses a backup_schedule path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_backup_schedule_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_parse_backup_schedule_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_parse_common_billing_account_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_parse_common_folder_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_parse_common_location_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_parse_common_organization_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_parse_common_project_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_parse_crypto_key_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_crypto_key_version_path
    
    
    parse_crypto_key_version_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key_version path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_crypto_key_version_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_parse_crypto_key_version_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_database_path
    
    
    parse_database_path(path: str) -> typing.Dict[str, str]

Parses a database path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_database_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_parse_database_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_database_role_path
    
    
    parse_database_role_path(path: str) -> typing.Dict[str, str]

Parses a database_role path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_database_role_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_parse_database_role_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_instance_partition_path
    
    
    parse_instance_partition_path(path: str) -> typing.Dict[str, str]

Parses a instance_partition path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_instance_partition_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_parse_instance_partition_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.parse_instance_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_parse_instance_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.restore_database
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Create a new database by restoring from a completed backup.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.restore_database](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_restore_database)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Sets the access control policy on a database or backup resource.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_set_iam_policy)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        permissions: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Returns permissions that the caller has on the specified database or backup resource.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_test_iam_permissions)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.update_backup
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.spanner_admin_database_v1.types.backup.Backup

Updates a pending or completed `Backup][google.spanner.admin.database.v1.Backup]`.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.update_backup](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_update_backup)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.update_backup_schedule
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.spanner_admin_database_v1.types.backup_schedule.BackupSchedule

Updates a backup schedule.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.update_backup_schedule](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_update_backup_schedule)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.update_database
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Updates a Cloud Spanner database.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.update_database](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_update_database)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.update_database_ddl
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Updates the schema of a Cloud Spanner database by creating/altering/dropping tables, columns, indexes, etc.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient.update_database_ddl](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminAsyncClient_update_database_ddl)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_DatabaseAdminClient)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.**exit**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient___exit__)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.add_split_points
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.add_split_points](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_add_split_points)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.backup_path
    
    
    backup_path(project: str, instance: str, backup: str) -> str

Returns a fully-qualified backup string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.backup_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_backup_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.backup_schedule_path
    
    
    backup_schedule_path(
        project: str, instance: str, database: str, schedule: str
    ) -> str

Returns a fully-qualified backup_schedule string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.backup_schedule_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_backup_schedule_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.cancel_operation
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.cancel_operation](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_cancel_operation)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_common_billing_account_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.common_folder_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_common_folder_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.common_location_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_common_location_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.common_organization_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_common_organization_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.common_project_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_common_project_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.copy_backup
    
    
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

Starts copying a Cloud Spanner Backup.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.copy_backup](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_copy_backup)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.create_backup
    
    
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

Starts creating a new Cloud Spanner Backup.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.create_backup](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_create_backup)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.create_backup_schedule
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.create_backup_schedule](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_create_backup_schedule)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.create_database
    
    
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

Creates a new Cloud Spanner database and starts to prepare it for serving.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.create_database](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_create_database)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.crypto_key_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_crypto_key_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.crypto_key_version_path
    
    
    crypto_key_version_path(
        project: str, location: str, key_ring: str, crypto_key: str, crypto_key_version: str
    ) -> str

Returns a fully-qualified crypto_key_version string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.crypto_key_version_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_crypto_key_version_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.database_path
    
    
    database_path(project: str, instance: str, database: str) -> str

Returns a fully-qualified database string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.database_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_database_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.database_role_path
    
    
    database_role_path(project: str, instance: str, database: str, role: str) -> str

Returns a fully-qualified database_role string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.database_role_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_database_role_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.delete_backup
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.delete_backup](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_delete_backup)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.delete_backup_schedule
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.delete_backup_schedule](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_delete_backup_schedule)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.delete_operation
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.delete_operation](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_delete_operation)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.drop_database
    
    
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

Drops (aka deletes) a Cloud Spanner database.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.drop_database](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_drop_database)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.from_service_account_file](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_from_service_account_file)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.from_service_account_info](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_from_service_account_info)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.from_service_account_json](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_from_service_account_json)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.get_backup
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.get_backup](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_get_backup)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.get_backup_schedule
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.get_backup_schedule](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_get_backup_schedule)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.get_database
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.get_database](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_get_database)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.get_database_ddl
    
    
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

Returns the schema of a Cloud Spanner database as a list of formatted DDL statements.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.get_database_ddl](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_get_database_ddl)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.get_iam_policy
    
    
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

Gets the access control policy for a database or backup resource.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.get_iam_policy](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_get_iam_policy)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_get_mtls_endpoint_and_cert_source)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.get_operation
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.get_operation](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_get_operation)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.instance_partition_path
    
    
    instance_partition_path(
        project: str, instance: str, instance_partition: str
    ) -> str

Returns a fully-qualified instance_partition string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.instance_partition_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_instance_partition_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.instance_path
    
    
    instance_path(project: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.instance_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_instance_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.internal_update_graph_operation
    
    
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

This is an internal API called by Spanner Graph jobs.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.internal_update_graph_operation](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_internal_update_graph_operation)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.list_backup_operations
    
    
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

Lists the backup [long-running operations][google.longrunning.Operation] in the given instance.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.list_backup_operations](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_list_backup_operations)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.list_backup_schedules
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.list_backup_schedules](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_list_backup_schedules)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.list_backups
    
    
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

Lists completed and pending backups.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.list_backups](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_list_backups)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.list_database_operations
    
    
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

Lists database `longrunning-operations][google.longrunning.Operation]`.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.list_database_operations](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_list_database_operations)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.list_database_roles
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.list_database_roles](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_list_database_roles)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.list_databases
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.list_databases](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_list_databases)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.list_operations
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.list_operations](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_list_operations)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_backup_path
    
    
    parse_backup_path(path: str) -> typing.Dict[str, str]

Parses a backup path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_backup_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_parse_backup_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_backup_schedule_path
    
    
    parse_backup_schedule_path(path: str) -> typing.Dict[str, str]

Parses a backup_schedule path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_backup_schedule_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_parse_backup_schedule_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_parse_common_billing_account_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_parse_common_folder_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_parse_common_location_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_parse_common_organization_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_parse_common_project_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_parse_crypto_key_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_crypto_key_version_path
    
    
    parse_crypto_key_version_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key_version path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_crypto_key_version_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_parse_crypto_key_version_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_database_path
    
    
    parse_database_path(path: str) -> typing.Dict[str, str]

Parses a database path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_database_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_parse_database_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_database_role_path
    
    
    parse_database_role_path(path: str) -> typing.Dict[str, str]

Parses a database_role path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_database_role_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_parse_database_role_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_instance_partition_path
    
    
    parse_instance_partition_path(path: str) -> typing.Dict[str, str]

Parses a instance_partition path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_instance_partition_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_parse_instance_partition_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.parse_instance_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_parse_instance_path)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.restore_database
    
    
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

Create a new database by restoring from a completed backup.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.restore_database](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_restore_database)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.set_iam_policy
    
    
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

Sets the access control policy on a database or backup resource.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.set_iam_policy](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_set_iam_policy)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.test_iam_permissions
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_test_iam_permissions)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.update_backup
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.update_backup](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_update_backup)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.update_backup_schedule
    
    
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

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.update_backup_schedule](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_update_backup_schedule)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.update_database
    
    
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

Updates a Cloud Spanner database.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.update_database](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_update_database)

### google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.update_database_ddl
    
    
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

Updates the schema of a Cloud Spanner database by creating/altering/dropping tables, columns, indexes, etc.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient.update_database_ddl](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient#google_cloud_spanner_admin_database_v1_services_database_admin_DatabaseAdminClient_update_database_ddl)

### google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupOperationsAsyncPager
    
    
    ListBackupOperationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.spanner_admin_database_v1.types.backup.ListBackupOperationsResponse
            ],
        ],
        request: google.cloud.spanner_admin_database_v1.types.backup.ListBackupOperationsRequest,
        response: google.cloud.spanner_admin_database_v1.types.backup.ListBackupOperationsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupOperationsAsyncPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupOperationsAsyncPager#google_cloud_spanner_admin_database_v1_services_database_admin_pagers_ListBackupOperationsAsyncPager_ListBackupOperationsAsyncPager)

### google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupOperationsPager
    
    
    ListBackupOperationsPager(
        method: typing.Callable[
            [...],
            google.cloud.spanner_admin_database_v1.types.backup.ListBackupOperationsResponse,
        ],
        request: google.cloud.spanner_admin_database_v1.types.backup.ListBackupOperationsRequest,
        response: google.cloud.spanner_admin_database_v1.types.backup.ListBackupOperationsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupOperationsPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupOperationsPager#google_cloud_spanner_admin_database_v1_services_database_admin_pagers_ListBackupOperationsPager_ListBackupOperationsPager)

### google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupSchedulesAsyncPager
    
    
    ListBackupSchedulesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.spanner_admin_database_v1.types.backup_schedule.ListBackupSchedulesResponse
            ],
        ],
        request: google.cloud.spanner_admin_database_v1.types.backup_schedule.ListBackupSchedulesRequest,
        response: google.cloud.spanner_admin_database_v1.types.backup_schedule.ListBackupSchedulesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupSchedulesAsyncPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupSchedulesAsyncPager#google_cloud_spanner_admin_database_v1_services_database_admin_pagers_ListBackupSchedulesAsyncPager_ListBackupSchedulesAsyncPager)

### google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupSchedulesPager
    
    
    ListBackupSchedulesPager(
        method: typing.Callable[
            [...],
            google.cloud.spanner_admin_database_v1.types.backup_schedule.ListBackupSchedulesResponse,
        ],
        request: google.cloud.spanner_admin_database_v1.types.backup_schedule.ListBackupSchedulesRequest,
        response: google.cloud.spanner_admin_database_v1.types.backup_schedule.ListBackupSchedulesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupSchedulesPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupSchedulesPager#google_cloud_spanner_admin_database_v1_services_database_admin_pagers_ListBackupSchedulesPager_ListBackupSchedulesPager)

### google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupsAsyncPager
    
    
    ListBackupsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.spanner_admin_database_v1.types.backup.ListBackupsResponse
            ],
        ],
        request: google.cloud.spanner_admin_database_v1.types.backup.ListBackupsRequest,
        response: google.cloud.spanner_admin_database_v1.types.backup.ListBackupsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupsAsyncPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupsAsyncPager#google_cloud_spanner_admin_database_v1_services_database_admin_pagers_ListBackupsAsyncPager_ListBackupsAsyncPager)

### google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupsPager
    
    
    ListBackupsPager(
        method: typing.Callable[
            [...], google.cloud.spanner_admin_database_v1.types.backup.ListBackupsResponse
        ],
        request: google.cloud.spanner_admin_database_v1.types.backup.ListBackupsRequest,
        response: google.cloud.spanner_admin_database_v1.types.backup.ListBackupsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupsPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupsPager#google_cloud_spanner_admin_database_v1_services_database_admin_pagers_ListBackupsPager_ListBackupsPager)

### google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseOperationsAsyncPager
    
    
    ListDatabaseOperationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabaseOperationsResponse
            ],
        ],
        request: google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabaseOperationsRequest,
        response: google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabaseOperationsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseOperationsAsyncPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseOperationsAsyncPager#google_cloud_spanner_admin_database_v1_services_database_admin_pagers_ListDatabaseOperationsAsyncPager_ListDatabaseOperationsAsyncPager)

### google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseOperationsPager
    
    
    ListDatabaseOperationsPager(
        method: typing.Callable[
            [...],
            google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabaseOperationsResponse,
        ],
        request: google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabaseOperationsRequest,
        response: google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabaseOperationsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseOperationsPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseOperationsPager#google_cloud_spanner_admin_database_v1_services_database_admin_pagers_ListDatabaseOperationsPager_ListDatabaseOperationsPager)

### google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseRolesAsyncPager
    
    
    ListDatabaseRolesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabaseRolesResponse
            ],
        ],
        request: google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabaseRolesRequest,
        response: google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabaseRolesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseRolesAsyncPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseRolesAsyncPager#google_cloud_spanner_admin_database_v1_services_database_admin_pagers_ListDatabaseRolesAsyncPager_ListDatabaseRolesAsyncPager)

### google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseRolesPager
    
    
    ListDatabaseRolesPager(
        method: typing.Callable[
            [...],
            google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabaseRolesResponse,
        ],
        request: google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabaseRolesRequest,
        response: google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabaseRolesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseRolesPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseRolesPager#google_cloud_spanner_admin_database_v1_services_database_admin_pagers_ListDatabaseRolesPager_ListDatabaseRolesPager)

### google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabasesAsyncPager
    
    
    ListDatabasesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabasesResponse
            ],
        ],
        request: google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabasesRequest,
        response: google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabasesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabasesAsyncPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabasesAsyncPager#google_cloud_spanner_admin_database_v1_services_database_admin_pagers_ListDatabasesAsyncPager_ListDatabasesAsyncPager)

### google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabasesPager
    
    
    ListDatabasesPager(
        method: typing.Callable[
            [...],
            google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabasesResponse,
        ],
        request: google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabasesRequest,
        response: google.cloud.spanner_admin_database_v1.types.spanner_database_admin.ListDatabasesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabasesPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabasesPager#google_cloud_spanner_admin_database_v1_services_database_admin_pagers_ListDatabasesPager_ListDatabasesPager)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient
    
    
    InstanceAdminAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.spanner_admin_instance_v1.services.instance_admin.transports.base.InstanceAdminTransport,
                typing.Callable[
                    [...],
                    google.cloud.spanner_admin_instance_v1.services.instance_admin.transports.base.InstanceAdminTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the instance admin async client.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_InstanceAdminAsyncClient)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_cancel_operation)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_common_billing_account_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_common_folder_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_common_location_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_common_organization_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_common_project_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.create_instance
    
    
    create_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.CreateInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        instance_id: typing.Optional[str] = None,
        instance: typing.Optional[
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.Instance
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

Creates an instance and begins preparing it to begin serving.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.create_instance](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_create_instance)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.create_instance_config
    
    
    create_instance_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.CreateInstanceConfigRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        instance_config: typing.Optional[
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.InstanceConfig
        ] = None,
        instance_config_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates an instance configuration and begins preparing it to be used.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.create_instance_config](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_create_instance_config)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.create_instance_partition
    
    
    create_instance_partition(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.CreateInstancePartitionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        instance_partition: typing.Optional[
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.InstancePartition
        ] = None,
        instance_partition_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates an instance partition and begins preparing it to be used.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.create_instance_partition](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_create_instance_partition)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.delete_instance
    
    
    delete_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.DeleteInstanceRequest,
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

Deletes an instance.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.delete_instance](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_delete_instance)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.delete_instance_config
    
    
    delete_instance_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.DeleteInstanceConfigRequest,
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

Deletes the instance configuration.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.delete_instance_config](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_delete_instance_config)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.delete_instance_partition
    
    
    delete_instance_partition(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.DeleteInstancePartitionRequest,
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

Deletes an existing instance partition.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.delete_instance_partition](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_delete_instance_partition)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.delete_operation
    
    
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

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_delete_operation)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_from_service_account_file)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_from_service_account_info)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_from_service_account_json)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Gets the access control policy for an instance resource.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_get_iam_policy)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.get_instance
    
    
    get_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.GetInstanceRequest,
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
    ) -> google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.Instance

Gets information about a particular instance.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.get_instance](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_get_instance)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.get_instance_config
    
    
    get_instance_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.GetInstanceConfigRequest,
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
    ) -> google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.InstanceConfig

Gets information about a particular instance configuration.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.get_instance_config](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_get_instance_config)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.get_instance_partition
    
    
    get_instance_partition(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.GetInstancePartitionRequest,
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
    ) -> (
        google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.InstancePartition
    )

Gets information about a particular instance partition.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.get_instance_partition](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_get_instance_partition)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.get_operation
    
    
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

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_get_operation)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.spanner_admin_instance_v1.services.instance_admin.transports.base.InstanceAdminTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_get_transport_class)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.instance_config_path
    
    
    instance_config_path(project: str, instance_config: str) -> str

Returns a fully-qualified instance_config string.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.instance_config_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_instance_config_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.instance_partition_path
    
    
    instance_partition_path(
        project: str, instance: str, instance_partition: str
    ) -> str

Returns a fully-qualified instance_partition string.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.instance_partition_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_instance_partition_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.instance_path
    
    
    instance_path(project: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.instance_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_instance_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.list_instance_config_operations
    
    
    list_instance_config_operations(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstanceConfigOperationsRequest,
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
        google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigOperationsAsyncPager
    )

Lists the user-managed instance configuration long-running operations in the given project.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.list_instance_config_operations](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_list_instance_config_operations)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.list_instance_configs
    
    
    list_instance_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstanceConfigsRequest,
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
        google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigsAsyncPager
    )

Lists the supported instance configurations for a given project.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.list_instance_configs](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_list_instance_configs)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.list_instance_partition_operations
    
    
    list_instance_partition_operations(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancePartitionOperationsRequest,
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
        google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionOperationsAsyncPager
    )

Lists instance partition long-running operations in the given instance.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.list_instance_partition_operations](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_list_instance_partition_operations)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.list_instance_partitions
    
    
    list_instance_partitions(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancePartitionsRequest,
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
        google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionsAsyncPager
    )

Lists all instance partitions for the given instance.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.list_instance_partitions](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_list_instance_partitions)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.list_instances
    
    
    list_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancesRequest,
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
        google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancesAsyncPager
    )

Lists all instances in the given project.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.list_instances](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_list_instances)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.list_operations
    
    
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

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_list_operations)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.move_instance
    
    
    move_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.MoveInstanceRequest,
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

Moves an instance to the target instance configuration.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.move_instance](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_move_instance)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_parse_common_billing_account_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_parse_common_folder_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_parse_common_location_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_parse_common_organization_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_parse_common_project_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.parse_instance_config_path
    
    
    parse_instance_config_path(path: str) -> typing.Dict[str, str]

Parses a instance_config path into its component segments.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.parse_instance_config_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_parse_instance_config_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.parse_instance_partition_path
    
    
    parse_instance_partition_path(path: str) -> typing.Dict[str, str]

Parses a instance_partition path into its component segments.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.parse_instance_partition_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_parse_instance_partition_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.parse_instance_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_parse_instance_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Sets the access control policy on an instance resource.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_set_iam_policy)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        permissions: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Returns permissions that the caller has on the specified instance resource.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_test_iam_permissions)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.update_instance
    
    
    update_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.UpdateInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        instance: typing.Optional[
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.Instance
        ] = None,
        field_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Updates an instance, and begins allocating or releasing resources as requested.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.update_instance](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_update_instance)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.update_instance_config
    
    
    update_instance_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.UpdateInstanceConfigRequest,
                dict,
            ]
        ] = None,
        *,
        instance_config: typing.Optional[
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.InstanceConfig
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

Updates an instance configuration.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.update_instance_config](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_update_instance_config)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.update_instance_partition
    
    
    update_instance_partition(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.UpdateInstancePartitionRequest,
                dict,
            ]
        ] = None,
        *,
        instance_partition: typing.Optional[
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.InstancePartition
        ] = None,
        field_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Updates an instance partition, and begins allocating or releasing resources as requested.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient.update_instance_partition](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminAsyncClient_update_instance_partition)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient
    
    
    InstanceAdminClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.spanner_admin_instance_v1.services.instance_admin.transports.base.InstanceAdminTransport,
                typing.Callable[
                    [...],
                    google.cloud.spanner_admin_instance_v1.services.instance_admin.transports.base.InstanceAdminTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the instance admin client.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_InstanceAdminClient)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.**exit**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient___exit__)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.cancel_operation
    
    
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

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.cancel_operation](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_cancel_operation)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_common_billing_account_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.common_folder_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_common_folder_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.common_location_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_common_location_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.common_organization_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_common_organization_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.common_project_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_common_project_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.create_instance
    
    
    create_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.CreateInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        instance_id: typing.Optional[str] = None,
        instance: typing.Optional[
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.Instance
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

Creates an instance and begins preparing it to begin serving.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.create_instance](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_create_instance)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.create_instance_config
    
    
    create_instance_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.CreateInstanceConfigRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        instance_config: typing.Optional[
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.InstanceConfig
        ] = None,
        instance_config_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates an instance configuration and begins preparing it to be used.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.create_instance_config](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_create_instance_config)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.create_instance_partition
    
    
    create_instance_partition(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.CreateInstancePartitionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        instance_partition: typing.Optional[
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.InstancePartition
        ] = None,
        instance_partition_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates an instance partition and begins preparing it to be used.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.create_instance_partition](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_create_instance_partition)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.delete_instance
    
    
    delete_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.DeleteInstanceRequest,
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

Deletes an instance.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.delete_instance](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_delete_instance)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.delete_instance_config
    
    
    delete_instance_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.DeleteInstanceConfigRequest,
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

Deletes the instance configuration.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.delete_instance_config](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_delete_instance_config)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.delete_instance_partition
    
    
    delete_instance_partition(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.DeleteInstancePartitionRequest,
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

Deletes an existing instance partition.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.delete_instance_partition](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_delete_instance_partition)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.delete_operation
    
    
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

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.delete_operation](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_delete_operation)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.from_service_account_file](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_from_service_account_file)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.from_service_account_info](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_from_service_account_info)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.from_service_account_json](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_from_service_account_json)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.get_iam_policy
    
    
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

Gets the access control policy for an instance resource.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.get_iam_policy](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_get_iam_policy)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.get_instance
    
    
    get_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.GetInstanceRequest,
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
    ) -> google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.Instance

Gets information about a particular instance.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.get_instance](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_get_instance)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.get_instance_config
    
    
    get_instance_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.GetInstanceConfigRequest,
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
    ) -> google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.InstanceConfig

Gets information about a particular instance configuration.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.get_instance_config](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_get_instance_config)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.get_instance_partition
    
    
    get_instance_partition(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.GetInstancePartitionRequest,
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
    ) -> (
        google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.InstancePartition
    )

Gets information about a particular instance partition.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.get_instance_partition](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_get_instance_partition)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_get_mtls_endpoint_and_cert_source)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.get_operation
    
    
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

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.get_operation](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_get_operation)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.instance_config_path
    
    
    instance_config_path(project: str, instance_config: str) -> str

Returns a fully-qualified instance_config string.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.instance_config_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_instance_config_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.instance_partition_path
    
    
    instance_partition_path(
        project: str, instance: str, instance_partition: str
    ) -> str

Returns a fully-qualified instance_partition string.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.instance_partition_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_instance_partition_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.instance_path
    
    
    instance_path(project: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.instance_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_instance_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.list_instance_config_operations
    
    
    list_instance_config_operations(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstanceConfigOperationsRequest,
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
        google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigOperationsPager
    )

Lists the user-managed instance configuration long-running operations in the given project.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.list_instance_config_operations](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_list_instance_config_operations)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.list_instance_configs
    
    
    list_instance_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstanceConfigsRequest,
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
        google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigsPager
    )

Lists the supported instance configurations for a given project.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.list_instance_configs](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_list_instance_configs)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.list_instance_partition_operations
    
    
    list_instance_partition_operations(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancePartitionOperationsRequest,
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
        google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionOperationsPager
    )

Lists instance partition long-running operations in the given instance.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.list_instance_partition_operations](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_list_instance_partition_operations)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.list_instance_partitions
    
    
    list_instance_partitions(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancePartitionsRequest,
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
        google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionsPager
    )

Lists all instance partitions for the given instance.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.list_instance_partitions](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_list_instance_partitions)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.list_instances
    
    
    list_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancesRequest,
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
        google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancesPager
    )

Lists all instances in the given project.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.list_instances](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_list_instances)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.list_operations
    
    
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

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.list_operations](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_list_operations)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.move_instance
    
    
    move_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.MoveInstanceRequest,
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

Moves an instance to the target instance configuration.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.move_instance](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_move_instance)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_parse_common_billing_account_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_parse_common_folder_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_parse_common_location_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_parse_common_organization_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_parse_common_project_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.parse_instance_config_path
    
    
    parse_instance_config_path(path: str) -> typing.Dict[str, str]

Parses a instance_config path into its component segments.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.parse_instance_config_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_parse_instance_config_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.parse_instance_partition_path
    
    
    parse_instance_partition_path(path: str) -> typing.Dict[str, str]

Parses a instance_partition path into its component segments.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.parse_instance_partition_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_parse_instance_partition_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.parse_instance_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_parse_instance_path)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.set_iam_policy
    
    
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

Sets the access control policy on an instance resource.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.set_iam_policy](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_set_iam_policy)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.test_iam_permissions
    
    
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

Returns permissions that the caller has on the specified instance resource.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_test_iam_permissions)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.update_instance
    
    
    update_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.UpdateInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        instance: typing.Optional[
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.Instance
        ] = None,
        field_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Updates an instance, and begins allocating or releasing resources as requested.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.update_instance](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_update_instance)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.update_instance_config
    
    
    update_instance_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.UpdateInstanceConfigRequest,
                dict,
            ]
        ] = None,
        *,
        instance_config: typing.Optional[
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.InstanceConfig
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

Updates an instance configuration.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.update_instance_config](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_update_instance_config)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.update_instance_partition
    
    
    update_instance_partition(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.UpdateInstancePartitionRequest,
                dict,
            ]
        ] = None,
        *,
        instance_partition: typing.Optional[
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.InstancePartition
        ] = None,
        field_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Updates an instance partition, and begins allocating or releasing resources as requested.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient.update_instance_partition](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient#google_cloud_spanner_admin_instance_v1_services_instance_admin_InstanceAdminClient_update_instance_partition)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigOperationsAsyncPager
    
    
    ListInstanceConfigOperationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstanceConfigOperationsResponse
            ],
        ],
        request: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstanceConfigOperationsRequest,
        response: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstanceConfigOperationsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigOperationsAsyncPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigOperationsAsyncPager#google_cloud_spanner_admin_instance_v1_services_instance_admin_pagers_ListInstanceConfigOperationsAsyncPager_ListInstanceConfigOperationsAsyncPager)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigOperationsPager
    
    
    ListInstanceConfigOperationsPager(
        method: typing.Callable[
            [...],
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstanceConfigOperationsResponse,
        ],
        request: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstanceConfigOperationsRequest,
        response: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstanceConfigOperationsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigOperationsPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigOperationsPager#google_cloud_spanner_admin_instance_v1_services_instance_admin_pagers_ListInstanceConfigOperationsPager_ListInstanceConfigOperationsPager)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigsAsyncPager
    
    
    ListInstanceConfigsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstanceConfigsResponse
            ],
        ],
        request: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstanceConfigsRequest,
        response: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstanceConfigsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigsAsyncPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigsAsyncPager#google_cloud_spanner_admin_instance_v1_services_instance_admin_pagers_ListInstanceConfigsAsyncPager_ListInstanceConfigsAsyncPager)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigsPager
    
    
    ListInstanceConfigsPager(
        method: typing.Callable[
            [...],
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstanceConfigsResponse,
        ],
        request: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstanceConfigsRequest,
        response: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstanceConfigsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigsPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigsPager#google_cloud_spanner_admin_instance_v1_services_instance_admin_pagers_ListInstanceConfigsPager_ListInstanceConfigsPager)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionOperationsAsyncPager
    
    
    ListInstancePartitionOperationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancePartitionOperationsResponse
            ],
        ],
        request: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancePartitionOperationsRequest,
        response: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancePartitionOperationsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionOperationsAsyncPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionOperationsAsyncPager#google_cloud_spanner_admin_instance_v1_services_instance_admin_pagers_ListInstancePartitionOperationsAsyncPager_ListInstancePartitionOperationsAsyncPager)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionOperationsPager
    
    
    ListInstancePartitionOperationsPager(
        method: typing.Callable[
            [...],
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancePartitionOperationsResponse,
        ],
        request: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancePartitionOperationsRequest,
        response: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancePartitionOperationsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionOperationsPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionOperationsPager#google_cloud_spanner_admin_instance_v1_services_instance_admin_pagers_ListInstancePartitionOperationsPager_ListInstancePartitionOperationsPager)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionsAsyncPager
    
    
    ListInstancePartitionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancePartitionsResponse
            ],
        ],
        request: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancePartitionsRequest,
        response: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancePartitionsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionsAsyncPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionsAsyncPager#google_cloud_spanner_admin_instance_v1_services_instance_admin_pagers_ListInstancePartitionsAsyncPager_ListInstancePartitionsAsyncPager)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionsPager
    
    
    ListInstancePartitionsPager(
        method: typing.Callable[
            [...],
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancePartitionsResponse,
        ],
        request: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancePartitionsRequest,
        response: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancePartitionsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionsPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionsPager#google_cloud_spanner_admin_instance_v1_services_instance_admin_pagers_ListInstancePartitionsPager_ListInstancePartitionsPager)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancesAsyncPager
    
    
    ListInstancesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancesResponse
            ],
        ],
        request: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancesRequest,
        response: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancesAsyncPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancesAsyncPager#google_cloud_spanner_admin_instance_v1_services_instance_admin_pagers_ListInstancesAsyncPager_ListInstancesAsyncPager)

### google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancesPager
    
    
    ListInstancesPager(
        method: typing.Callable[
            [...],
            google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancesResponse,
        ],
        request: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancesRequest,
        response: google.cloud.spanner_admin_instance_v1.types.spanner_instance_admin.ListInstancesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancesPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancesPager#google_cloud_spanner_admin_instance_v1_services_instance_admin_pagers_ListInstancesPager_ListInstancesPager)

### google.cloud.spanner_v1.batch.Batch.__enter__
    
    
    __enter__()

Begin `with` block.

See more: [google.cloud.spanner_v1.batch.Batch.**enter**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.batch.Batch#google_cloud_spanner_v1_batch_Batch___enter__)

### google.cloud.spanner_v1.batch.Batch.__exit__
    
    
    __exit__(exc_type, exc_val, exc_tb)

End `with` block.

See more: [google.cloud.spanner_v1.batch.Batch.**exit**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.batch.Batch#google_cloud_spanner_v1_batch_Batch___exit__)

### google.cloud.spanner_v1.batch.Batch.commit
    
    
    commit(
        return_commit_stats=False,
        request_options=None,
        max_commit_delay=None,
        exclude_txn_from_change_streams=False,
        isolation_level=IsolationLevel.ISOLATION_LEVEL_UNSPECIFIED,
        read_lock_mode=ReadLockMode.READ_LOCK_MODE_UNSPECIFIED,
        timeout_secs=30,
        default_retry_delay=None,
    )

Commit mutations to the database.

See more: [google.cloud.spanner_v1.batch.Batch.commit](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.batch.Batch#google_cloud_spanner_v1_batch_Batch_commit)

### google.cloud.spanner_v1.batch.MutationGroups.batch_write
    
    
    batch_write(request_options=None, exclude_txn_from_change_streams=False)

Executes batch_write.

See more: [google.cloud.spanner_v1.batch.MutationGroups.batch_write](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.batch.MutationGroups#google_cloud_spanner_v1_batch_MutationGroups_batch_write)

### google.cloud.spanner_v1.batch.MutationGroups.group
    
    
    group()

Returns a new `MutationGroup` to which mutations can be added.

See more: [google.cloud.spanner_v1.batch.MutationGroups.group](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.batch.MutationGroups#google_cloud_spanner_v1_batch_MutationGroups_group)

### google.cloud.spanner_v1.client.Client.copy
    
    
    copy()

Make a copy of this client.

See more: [google.cloud.spanner_v1.client.Client.copy](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client#google_cloud_spanner_v1_client_Client_copy)

### google.cloud.spanner_v1.client.Client.instance
    
    
    instance(
        instance_id,
        configuration_name=None,
        display_name=None,
        node_count=None,
        labels=None,
        processing_units=None,
    )

Factory to create a instance associated with this client.

See more: [google.cloud.spanner_v1.client.Client.instance](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client#google_cloud_spanner_v1_client_Client_instance)

### google.cloud.spanner_v1.client.Client.list_instance_configs
    
    
    list_instance_configs(page_size=None)

List available instance configurations for the client's project.

See more: [google.cloud.spanner_v1.client.Client.list_instance_configs](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client#google_cloud_spanner_v1_client_Client_list_instance_configs)

### google.cloud.spanner_v1.client.Client.list_instances
    
    
    list_instances(filter_="", page_size=None)

List instances for the client's project.

See more: [google.cloud.spanner_v1.client.Client.list_instances](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client#google_cloud_spanner_v1_client_Client_list_instances)

### google.cloud.spanner_v1.database.BatchCheckout.__enter__
    
    
    __enter__()

Begin `with` block.

See more: [google.cloud.spanner_v1.database.BatchCheckout.**enter**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchCheckout#google_cloud_spanner_v1_database_BatchCheckout___enter__)

### google.cloud.spanner_v1.database.BatchCheckout.__exit__
    
    
    __exit__(exc_type, exc_val, exc_tb)

End `with` block.

See more: [google.cloud.spanner_v1.database.BatchCheckout.**exit**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchCheckout#google_cloud_spanner_v1_database_BatchCheckout___exit__)

### google.cloud.spanner_v1.database.BatchSnapshot.__enter__
    
    
    __enter__()

Begin `with` block.

See more: [google.cloud.spanner_v1.database.BatchSnapshot.**enter**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchSnapshot#google_cloud_spanner_v1_database_BatchSnapshot___enter__)

### google.cloud.spanner_v1.database.BatchSnapshot.__exit__
    
    
    __exit__(exc_type, exc_val, exc_tb)

End `with` block.

See more: [google.cloud.spanner_v1.database.BatchSnapshot.**exit**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchSnapshot#google_cloud_spanner_v1_database_BatchSnapshot___exit__)

### google.cloud.spanner_v1.database.BatchSnapshot.close
    
    
    close()

Clean up underlying session.

See more: [google.cloud.spanner_v1.database.BatchSnapshot.close](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchSnapshot#google_cloud_spanner_v1_database_BatchSnapshot_close)

### google.cloud.spanner_v1.database.BatchSnapshot.execute_sql
    
    
    execute_sql(*args, **kw)

Convenience method: perform query operation via snapshot.

See more: [google.cloud.spanner_v1.database.BatchSnapshot.execute_sql](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchSnapshot#google_cloud_spanner_v1_database_BatchSnapshot_execute_sql)

### google.cloud.spanner_v1.database.BatchSnapshot.from_dict
    
    
    from_dict(database, mapping)

Reconstruct an instance from a mapping.

See more: [google.cloud.spanner_v1.database.BatchSnapshot.from_dict](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchSnapshot#google_cloud_spanner_v1_database_BatchSnapshot_from_dict)

### google.cloud.spanner_v1.database.BatchSnapshot.generate_query_batches
    
    
    generate_query_batches(
        sql,
        params=None,
        param_types=None,
        partition_size_bytes=None,
        max_partitions=None,
        query_options=None,
        data_boost_enabled=False,
        directed_read_options=None,
        *,
        retry=_MethodDefault._DEFAULT_VALUE,
        timeout=_MethodDefault._DEFAULT_VALUE
    )

Start a partitioned query operation.

See more: [google.cloud.spanner_v1.database.BatchSnapshot.generate_query_batches](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchSnapshot#google_cloud_spanner_v1_database_BatchSnapshot_generate_query_batches)

### google.cloud.spanner_v1.database.BatchSnapshot.generate_read_batches
    
    
    generate_read_batches(
        table,
        columns,
        keyset,
        index="",
        partition_size_bytes=None,
        max_partitions=None,
        data_boost_enabled=False,
        directed_read_options=None,
        *,
        retry=_MethodDefault._DEFAULT_VALUE,
        timeout=_MethodDefault._DEFAULT_VALUE
    )

Start a partitioned batch read operation.

See more: [google.cloud.spanner_v1.database.BatchSnapshot.generate_read_batches](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchSnapshot#google_cloud_spanner_v1_database_BatchSnapshot_generate_read_batches)

### google.cloud.spanner_v1.database.BatchSnapshot.process
    
    
    process(batch)

Process a single, partitioned query or read.

See more: [google.cloud.spanner_v1.database.BatchSnapshot.process](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchSnapshot#google_cloud_spanner_v1_database_BatchSnapshot_process)

### google.cloud.spanner_v1.database.BatchSnapshot.process_query_batch
    
    
    process_query_batch(
        batch,
        *,
        lazy_decode: bool = False,
        retry=_MethodDefault._DEFAULT_VALUE,
        timeout=_MethodDefault._DEFAULT_VALUE
    )

Process a single, partitioned query.

See more: [google.cloud.spanner_v1.database.BatchSnapshot.process_query_batch](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchSnapshot#google_cloud_spanner_v1_database_BatchSnapshot_process_query_batch)

### google.cloud.spanner_v1.database.BatchSnapshot.process_read_batch
    
    
    process_read_batch(
        batch,
        *,
        retry=_MethodDefault._DEFAULT_VALUE,
        timeout=_MethodDefault._DEFAULT_VALUE,
        lazy_decode=False
    )

Process a single, partitioned read.

See more: [google.cloud.spanner_v1.database.BatchSnapshot.process_read_batch](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchSnapshot#google_cloud_spanner_v1_database_BatchSnapshot_process_read_batch)

### google.cloud.spanner_v1.database.BatchSnapshot.read
    
    
    read(*args, **kw)

Convenience method: perform read operation via snapshot.

See more: [google.cloud.spanner_v1.database.BatchSnapshot.read](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchSnapshot#google_cloud_spanner_v1_database_BatchSnapshot_read)

### google.cloud.spanner_v1.database.BatchSnapshot.run_partitioned_query
    
    
    run_partitioned_query(
        sql,
        params=None,
        param_types=None,
        partition_size_bytes=None,
        max_partitions=None,
        query_options=None,
        data_boost_enabled=False,
        lazy_decode=False,
    )

Start a partitioned query operation to get list of partitions and then executes each partition on a separate thread.

See more: [google.cloud.spanner_v1.database.BatchSnapshot.run_partitioned_query](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchSnapshot#google_cloud_spanner_v1_database_BatchSnapshot_run_partitioned_query)

### google.cloud.spanner_v1.database.BatchSnapshot.to_dict
    
    
    to_dict()

Return state as a dictionary.

See more: [google.cloud.spanner_v1.database.BatchSnapshot.to_dict](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchSnapshot#google_cloud_spanner_v1_database_BatchSnapshot_to_dict)

### google.cloud.spanner_v1.database.Database.batch
    
    
    batch(
        request_options=None,
        max_commit_delay=None,
        exclude_txn_from_change_streams=False,
        isolation_level=IsolationLevel.ISOLATION_LEVEL_UNSPECIFIED,
        read_lock_mode=ReadLockMode.READ_LOCK_MODE_UNSPECIFIED,
        client_context=None,
        **kw
    )

Return an object which wraps a batch.

See more: [google.cloud.spanner_v1.database.Database.batch](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_batch)

### google.cloud.spanner_v1.database.Database.batch_snapshot
    
    
    batch_snapshot(
        read_timestamp=None,
        exact_staleness=None,
        session_id=None,
        transaction_id=None,
        client_context=None,
    )

Return an object which wraps a batch read / query.

See more: [google.cloud.spanner_v1.database.Database.batch_snapshot](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_batch_snapshot)

### google.cloud.spanner_v1.database.Database.close
    
    
    close()

Clean up underlying session manager and background tasks.

See more: [google.cloud.spanner_v1.database.Database.close](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_close)

### google.cloud.spanner_v1.database.Database.create
    
    
    create()

Create this database within its instance.

See more: [google.cloud.spanner_v1.database.Database.create](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_create)

### google.cloud.spanner_v1.database.Database.drop
    
    
    drop()

Drop this database.

See more: [google.cloud.spanner_v1.database.Database.drop](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_drop)

### google.cloud.spanner_v1.database.Database.execute_partitioned_dml
    
    
    execute_partitioned_dml(
        dml,
        params=None,
        param_types=None,
        query_options=None,
        request_options=None,
        exclude_txn_from_change_streams=False,
    )

Execute a partitionable DML statement.

See more: [google.cloud.spanner_v1.database.Database.execute_partitioned_dml](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_execute_partitioned_dml)

### google.cloud.spanner_v1.database.Database.exists
    
    
    exists()

Test whether this database exists.

See more: [google.cloud.spanner_v1.database.Database.exists](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_exists)

### google.cloud.spanner_v1.database.Database.from_pb
    
    
    from_pb(database_pb, instance, pool=None)

Creates an instance of this class from a protobuf.

See more: [google.cloud.spanner_v1.database.Database.from_pb](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_from_pb)

### google.cloud.spanner_v1.database.Database.get_iam_policy
    
    
    get_iam_policy(policy_version=None)

Gets the access control policy for a database resource.

See more: [google.cloud.spanner_v1.database.Database.get_iam_policy](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_get_iam_policy)

### google.cloud.spanner_v1.database.Database.is_optimized
    
    
    is_optimized()

Test whether this database has finished optimizing.

See more: [google.cloud.spanner_v1.database.Database.is_optimized](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_is_optimized)

### google.cloud.spanner_v1.database.Database.is_ready
    
    
    is_ready()

Test whether this database is ready for use.

See more: [google.cloud.spanner_v1.database.Database.is_ready](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_is_ready)

### google.cloud.spanner_v1.database.Database.list_database_operations
    
    
    list_database_operations(filter_="", page_size=None)

List database operations for the database.

See more: [google.cloud.spanner_v1.database.Database.list_database_operations](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_list_database_operations)

### google.cloud.spanner_v1.database.Database.list_database_roles
    
    
    list_database_roles(page_size=None)

Lists Cloud Spanner database roles.

See more: [google.cloud.spanner_v1.database.Database.list_database_roles](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_list_database_roles)

### google.cloud.spanner_v1.database.Database.list_tables
    
    
    list_tables(schema="_default")

List tables within the database.

See more: [google.cloud.spanner_v1.database.Database.list_tables](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_list_tables)

### google.cloud.spanner_v1.database.Database.metadata_and_request_id
    
    
    metadata_and_request_id(nth_request, nth_attempt, prior_metadata=[], span=None)

Return metadata and request ID string.

See more: [google.cloud.spanner_v1.database.Database.metadata_and_request_id](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_metadata_and_request_id)

### google.cloud.spanner_v1.database.Database.mutation_groups
    
    
    mutation_groups(client_context=None)

Return an object which wraps a mutation_group.

See more: [google.cloud.spanner_v1.database.Database.mutation_groups](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_mutation_groups)

### google.cloud.spanner_v1.database.Database.reload
    
    
    reload()

Reload this database.

See more: [google.cloud.spanner_v1.database.Database.reload](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_reload)

### google.cloud.spanner_v1.database.Database.restore
    
    
    restore(source)

Restore from a backup to this database.

See more: [google.cloud.spanner_v1.database.Database.restore](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_restore)

### google.cloud.spanner_v1.database.Database.run_in_transaction
    
    
    run_in_transaction(func, *args, **kw)

Perform a unit of work in a transaction, retrying on abort.

See more: [google.cloud.spanner_v1.database.Database.run_in_transaction](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_run_in_transaction)

### google.cloud.spanner_v1.database.Database.session
    
    
    session(labels=None, database_role=None)

Factory to create a session for this database.

See more: [google.cloud.spanner_v1.database.Database.session](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_session)

### google.cloud.spanner_v1.database.Database.set_iam_policy
    
    
    set_iam_policy(policy)

Sets the access control policy on a database resource.

See more: [google.cloud.spanner_v1.database.Database.set_iam_policy](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_set_iam_policy)

### google.cloud.spanner_v1.database.Database.snapshot
    
    
    snapshot(**kw)

Return an object which wraps a snapshot.

See more: [google.cloud.spanner_v1.database.Database.snapshot](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_snapshot)

### google.cloud.spanner_v1.database.Database.table
    
    
    table(table_id)

Factory to create a table object within this database.

See more: [google.cloud.spanner_v1.database.Database.table](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_table)

### google.cloud.spanner_v1.database.Database.update
    
    
    update(fields)

Update this database.

See more: [google.cloud.spanner_v1.database.Database.update](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_update)

### google.cloud.spanner_v1.database.Database.update_ddl
    
    
    update_ddl(ddl_statements, operation_id="", proto_descriptors=None)

Update DDL for this database.

See more: [google.cloud.spanner_v1.database.Database.update_ddl](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_update_ddl)

### google.cloud.spanner_v1.database.Database.with_error_augmentation
    
    
    with_error_augmentation(nth_request, nth_attempt, prior_metadata=[], span=None)

Context manager for gRPC calls with error augmentation.

See more: [google.cloud.spanner_v1.database.Database.with_error_augmentation](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database#google_cloud_spanner_v1_database_Database_with_error_augmentation)

### google.cloud.spanner_v1.database.MutationGroupsCheckout.__enter__
    
    
    __enter__()

Begin `with` block.

See more: [google.cloud.spanner_v1.database.MutationGroupsCheckout.**enter**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.MutationGroupsCheckout#google_cloud_spanner_v1_database_MutationGroupsCheckout___enter__)

### google.cloud.spanner_v1.database.MutationGroupsCheckout.__exit__
    
    
    __exit__(exc_type, exc_val, exc_tb)

End `with` block.

See more: [google.cloud.spanner_v1.database.MutationGroupsCheckout.**exit**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.MutationGroupsCheckout#google_cloud_spanner_v1_database_MutationGroupsCheckout___exit__)

### google.cloud.spanner_v1.database.SnapshotCheckout.__enter__
    
    
    __enter__()

Begin `with` block.

See more: [google.cloud.spanner_v1.database.SnapshotCheckout.**enter**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.SnapshotCheckout#google_cloud_spanner_v1_database_SnapshotCheckout___enter__)

### google.cloud.spanner_v1.database.SnapshotCheckout.__exit__
    
    
    __exit__(exc_type, exc_val, exc_tb)

End `with` block.

See more: [google.cloud.spanner_v1.database.SnapshotCheckout.**exit**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.SnapshotCheckout#google_cloud_spanner_v1_database_SnapshotCheckout___exit__)

### google.cloud.spanner_v1.instance.Instance.backup
    
    
    backup(
        backup_id, database="", expire_time=None, version_time=None, encryption_config=None
    )

Factory to create a backup within this instance.

See more: [google.cloud.spanner_v1.instance.Instance.backup](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance#google_cloud_spanner_v1_instance_Instance_backup)

### google.cloud.spanner_v1.instance.Instance.copy
    
    
    copy()

Make a copy of this instance.

See more: [google.cloud.spanner_v1.instance.Instance.copy](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance#google_cloud_spanner_v1_instance_Instance_copy)

### google.cloud.spanner_v1.instance.Instance.copy_backup
    
    
    copy_backup(backup_id, source_backup, expire_time=None, encryption_config=None)

Factory to create a copy backup within this instance.

See more: [google.cloud.spanner_v1.instance.Instance.copy_backup](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance#google_cloud_spanner_v1_instance_Instance_copy_backup)

### google.cloud.spanner_v1.instance.Instance.create
    
    
    create()

Create this instance.

See more: [google.cloud.spanner_v1.instance.Instance.create](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance#google_cloud_spanner_v1_instance_Instance_create)

### google.cloud.spanner_v1.instance.Instance.database
    
    
    database(
        database_id,
        ddl_statements=(),
        pool=None,
        logger=None,
        encryption_config=None,
        database_dialect=DatabaseDialect.DATABASE_DIALECT_UNSPECIFIED,
        database_role=None,
        enable_drop_protection=False,
        enable_interceptors_in_tests=False,
        proto_descriptors=None,
    )

Factory to create a database within this instance.

See more: [google.cloud.spanner_v1.instance.Instance.database](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance#google_cloud_spanner_v1_instance_Instance_database)

### google.cloud.spanner_v1.instance.Instance.delete
    
    
    delete()

Mark an instance and all of its databases for permanent deletion.

See more: [google.cloud.spanner_v1.instance.Instance.delete](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance#google_cloud_spanner_v1_instance_Instance_delete)

### google.cloud.spanner_v1.instance.Instance.exists
    
    
    exists()

Test whether this instance exists.

See more: [google.cloud.spanner_v1.instance.Instance.exists](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance#google_cloud_spanner_v1_instance_Instance_exists)

### google.cloud.spanner_v1.instance.Instance.from_pb
    
    
    from_pb(instance_pb, client)

Creates an instance from a protobuf.

See more: [google.cloud.spanner_v1.instance.Instance.from_pb](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance#google_cloud_spanner_v1_instance_Instance_from_pb)

### google.cloud.spanner_v1.instance.Instance.list_backup_operations
    
    
    list_backup_operations(filter_="", page_size=None)

List backup operations for the instance.

See more: [google.cloud.spanner_v1.instance.Instance.list_backup_operations](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance#google_cloud_spanner_v1_instance_Instance_list_backup_operations)

### google.cloud.spanner_v1.instance.Instance.list_backups
    
    
    list_backups(filter_="", page_size=None)

List backups for the instance.

See more: [google.cloud.spanner_v1.instance.Instance.list_backups](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance#google_cloud_spanner_v1_instance_Instance_list_backups)

### google.cloud.spanner_v1.instance.Instance.list_database_operations
    
    
    list_database_operations(filter_="", page_size=None)

List database operations for the instance.

See more: [google.cloud.spanner_v1.instance.Instance.list_database_operations](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance#google_cloud_spanner_v1_instance_Instance_list_database_operations)

### google.cloud.spanner_v1.instance.Instance.list_databases
    
    
    list_databases(page_size=None)

List databases for the instance.

See more: [google.cloud.spanner_v1.instance.Instance.list_databases](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance#google_cloud_spanner_v1_instance_Instance_list_databases)

### google.cloud.spanner_v1.instance.Instance.reload
    
    
    reload()

Reload the metadata for this instance.

See more: [google.cloud.spanner_v1.instance.Instance.reload](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance#google_cloud_spanner_v1_instance_Instance_reload)

### google.cloud.spanner_v1.instance.Instance.update
    
    
    update()

Update this instance.

See more: [google.cloud.spanner_v1.instance.Instance.update](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance#google_cloud_spanner_v1_instance_Instance_update)

### google.cloud.spanner_v1.keyset.KeyRange.__eq__
    
    
    __eq__(other)

Compare by serialized state.

See more: [google.cloud.spanner_v1.keyset.KeyRange.**eq**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.keyset.KeyRange#google_cloud_spanner_v1_keyset_KeyRange___eq__)

### google.cloud.spanner_v1.keyset.KeySet.__eq__
    
    
    __eq__(other)

Compare by serialized state.

See more: [google.cloud.spanner_v1.keyset.KeySet.**eq**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.keyset.KeySet#google_cloud_spanner_v1_keyset_KeySet___eq__)

### google.cloud.spanner_v1.pool.AbstractSessionPool.bind
    
    
    bind(database)

Associate the pool with a database.

See more: [google.cloud.spanner_v1.pool.AbstractSessionPool.bind](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.AbstractSessionPool#google_cloud_spanner_v1_pool_AbstractSessionPool_bind)

### google.cloud.spanner_v1.pool.AbstractSessionPool.clear
    
    
    clear()

Delete all sessions in the pool.

See more: [google.cloud.spanner_v1.pool.AbstractSessionPool.clear](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.AbstractSessionPool#google_cloud_spanner_v1_pool_AbstractSessionPool_clear)

### google.cloud.spanner_v1.pool.AbstractSessionPool.get
    
    
    get()

Check a session out from the pool.

See more: [google.cloud.spanner_v1.pool.AbstractSessionPool.get](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.AbstractSessionPool#google_cloud_spanner_v1_pool_AbstractSessionPool_get)

### google.cloud.spanner_v1.pool.AbstractSessionPool.put
    
    
    put(session)

Return a session to the pool.

See more: [google.cloud.spanner_v1.pool.AbstractSessionPool.put](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.AbstractSessionPool#google_cloud_spanner_v1_pool_AbstractSessionPool_put)

### google.cloud.spanner_v1.pool.AbstractSessionPool.session
    
    
    session(**kwargs)

Check out a session from the pool.

See more: [google.cloud.spanner_v1.pool.AbstractSessionPool.session](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.AbstractSessionPool#google_cloud_spanner_v1_pool_AbstractSessionPool_session)

### google.cloud.spanner_v1.pool.BurstyPool.bind
    
    
    bind(database)

Associate the pool with a database.

See more: [google.cloud.spanner_v1.pool.BurstyPool.bind](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.BurstyPool#google_cloud_spanner_v1_pool_BurstyPool_bind)

### google.cloud.spanner_v1.pool.BurstyPool.clear
    
    
    clear()

Delete all sessions in the pool.

See more: [google.cloud.spanner_v1.pool.BurstyPool.clear](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.BurstyPool#google_cloud_spanner_v1_pool_BurstyPool_clear)

### google.cloud.spanner_v1.pool.BurstyPool.get
    
    
    get()

Check a session out from the pool.

See more: [google.cloud.spanner_v1.pool.BurstyPool.get](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.BurstyPool#google_cloud_spanner_v1_pool_BurstyPool_get)

### google.cloud.spanner_v1.pool.BurstyPool.put
    
    
    put(session)

Return a session to the pool.

See more: [google.cloud.spanner_v1.pool.BurstyPool.put](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.BurstyPool#google_cloud_spanner_v1_pool_BurstyPool_put)

### google.cloud.spanner_v1.pool.FixedSizePool.bind
    
    
    bind(database)

Associate the pool with a database.

See more: [google.cloud.spanner_v1.pool.FixedSizePool.bind](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.FixedSizePool#google_cloud_spanner_v1_pool_FixedSizePool_bind)

### google.cloud.spanner_v1.pool.FixedSizePool.clear
    
    
    clear()

Delete all sessions in the pool.

See more: [google.cloud.spanner_v1.pool.FixedSizePool.clear](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.FixedSizePool#google_cloud_spanner_v1_pool_FixedSizePool_clear)

### google.cloud.spanner_v1.pool.FixedSizePool.get
    
    
    get(timeout=None)

Check a session out from the pool.

See more: [google.cloud.spanner_v1.pool.FixedSizePool.get](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.FixedSizePool#google_cloud_spanner_v1_pool_FixedSizePool_get)

### google.cloud.spanner_v1.pool.FixedSizePool.ping
    
    
    ping()

Check all sessions in the pool.

See more: [google.cloud.spanner_v1.pool.FixedSizePool.ping](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.FixedSizePool#google_cloud_spanner_v1_pool_FixedSizePool_ping)

### google.cloud.spanner_v1.pool.FixedSizePool.put
    
    
    put(session)

Return a session to the pool.

See more: [google.cloud.spanner_v1.pool.FixedSizePool.put](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.FixedSizePool#google_cloud_spanner_v1_pool_FixedSizePool_put)

### google.cloud.spanner_v1.pool.PingingPool.bind
    
    
    bind(database)

Associate the pool with a database.

See more: [google.cloud.spanner_v1.pool.PingingPool.bind](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.PingingPool#google_cloud_spanner_v1_pool_PingingPool_bind)

### google.cloud.spanner_v1.pool.PingingPool.clear
    
    
    clear()

Delete all sessions in the pool.

See more: [google.cloud.spanner_v1.pool.PingingPool.clear](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.PingingPool#google_cloud_spanner_v1_pool_PingingPool_clear)

### google.cloud.spanner_v1.pool.PingingPool.get
    
    
    get(timeout=None)

Check a session out from the pool.

See more: [google.cloud.spanner_v1.pool.PingingPool.get](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.PingingPool#google_cloud_spanner_v1_pool_PingingPool_get)

### google.cloud.spanner_v1.pool.PingingPool.ping
    
    
    ping()

Refresh maybe-expired sessions in the pool.

See more: [google.cloud.spanner_v1.pool.PingingPool.ping](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.PingingPool#google_cloud_spanner_v1_pool_PingingPool_ping)

### google.cloud.spanner_v1.pool.PingingPool.put
    
    
    put(session)

Return a session to the pool.

See more: [google.cloud.spanner_v1.pool.PingingPool.put](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.PingingPool#google_cloud_spanner_v1_pool_PingingPool_put)

### google.cloud.spanner_v1.pool.TransactionPingingPool
    
    
    TransactionPingingPool(
        size=10, default_timeout=10, ping_interval=3000, labels=None, database_role=None
    )

This throws a deprecation warning on initialization.

See more: [google.cloud.spanner_v1.pool.TransactionPingingPool](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.TransactionPingingPool#google_cloud_spanner_v1_pool_TransactionPingingPool_TransactionPingingPool)

### google.cloud.spanner_v1.pool.TransactionPingingPool.begin_pending_transactions
    
    
    begin_pending_transactions()

Begin all transactions for sessions added to the pool.

See more: [google.cloud.spanner_v1.pool.TransactionPingingPool.begin_pending_transactions](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.TransactionPingingPool#google_cloud_spanner_v1_pool_TransactionPingingPool_begin_pending_transactions)

### google.cloud.spanner_v1.pool.TransactionPingingPool.bind
    
    
    bind(database)

Associate the pool with a database.

See more: [google.cloud.spanner_v1.pool.TransactionPingingPool.bind](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.TransactionPingingPool#google_cloud_spanner_v1_pool_TransactionPingingPool_bind)

### google.cloud.spanner_v1.pool.TransactionPingingPool.put
    
    
    put(session)

Return a session to the pool.

See more: [google.cloud.spanner_v1.pool.TransactionPingingPool.put](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.TransactionPingingPool#google_cloud_spanner_v1_pool_TransactionPingingPool_put)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient
    
    
    SpannerAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.spanner_v1.services.spanner.transports.base.SpannerTransport,
                typing.Callable[
                    [...],
                    google.cloud.spanner_v1.services.spanner.transports.base.SpannerTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the spanner async client.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_SpannerAsyncClient)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.batch_create_sessions
    
    
    batch_create_sessions(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_v1.types.spanner.BatchCreateSessionsRequest, dict
            ]
        ] = None,
        *,
        database: typing.Optional[str] = None,
        session_count: typing.Optional[int] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.spanner_v1.types.spanner.BatchCreateSessionsResponse

Creates multiple new sessions.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.batch_create_sessions](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_batch_create_sessions)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.batch_write
    
    
    batch_write(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.BatchWriteRequest, dict]
        ] = None,
        *,
        session: typing.Optional[str] = None,
        mutation_groups: typing.Optional[
            typing.MutableSequence[
                google.cloud.spanner_v1.types.spanner.BatchWriteRequest.MutationGroup
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
    ) -> typing.Awaitable[
        typing.AsyncIterable[google.cloud.spanner_v1.types.spanner.BatchWriteResponse]
    ]

Batches the supplied mutation groups in a collection of efficient transactions.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.batch_write](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_batch_write)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.begin_transaction
    
    
    begin_transaction(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_v1.types.spanner.BeginTransactionRequest, dict
            ]
        ] = None,
        *,
        session: typing.Optional[str] = None,
        options: typing.Optional[
            google.cloud.spanner_v1.types.transaction.TransactionOptions
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.spanner_v1.types.transaction.Transaction

Begins a new transaction.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.begin_transaction](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_begin_transaction)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.commit
    
    
    commit(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.CommitRequest, dict]
        ] = None,
        *,
        session: typing.Optional[str] = None,
        transaction_id: typing.Optional[bytes] = None,
        mutations: typing.Optional[
            typing.MutableSequence[google.cloud.spanner_v1.types.mutation.Mutation]
        ] = None,
        single_use_transaction: typing.Optional[
            google.cloud.spanner_v1.types.transaction.TransactionOptions
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.spanner_v1.types.commit_response.CommitResponse

Commits a transaction.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.commit](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_commit)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_common_billing_account_path)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_common_folder_path)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_common_location_path)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_common_organization_path)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_common_project_path)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.create_session
    
    
    create_session(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.CreateSessionRequest, dict]
        ] = None,
        *,
        database: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.spanner_v1.types.spanner.Session

Creates a new session.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.create_session](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_create_session)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.database_path
    
    
    database_path(project: str, instance: str, database: str) -> str

Returns a fully-qualified database string.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.database_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_database_path)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.delete_session
    
    
    delete_session(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.DeleteSessionRequest, dict]
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

Ends a session, releasing server resources associated with it.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.delete_session](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_delete_session)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.execute_batch_dml
    
    
    execute_batch_dml(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.ExecuteBatchDmlRequest, dict]
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
    ) -> google.cloud.spanner_v1.types.spanner.ExecuteBatchDmlResponse

Executes a batch of SQL DML statements.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.execute_batch_dml](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_execute_batch_dml)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.execute_sql
    
    
    execute_sql(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.ExecuteSqlRequest, dict]
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
    ) -> google.cloud.spanner_v1.types.result_set.ResultSet

Executes an SQL statement, returning all results in a single reply.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.execute_sql](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_execute_sql)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.execute_streaming_sql
    
    
    execute_streaming_sql(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.ExecuteSqlRequest, dict]
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
    ) -> typing.Awaitable[
        typing.AsyncIterable[google.cloud.spanner_v1.types.result_set.PartialResultSet]
    ]

Like `ExecuteSql][google.spanner.v1.Spanner.ExecuteSql]`, except returns the result set as a stream.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.execute_streaming_sql](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_execute_streaming_sql)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.fetch_cache_update
    
    
    fetch_cache_update(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_v1.types.spanner.FetchCacheUpdateRequest, dict
            ]
        ] = None,
        *,
        database: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> typing.Awaitable[
        typing.AsyncIterable[google.cloud.spanner_v1.types.location.CacheUpdate]
    ]

Retrieves a cache update for a given database.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.fetch_cache_update](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_fetch_cache_update)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_from_service_account_file)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_from_service_account_info)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_from_service_account_json)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.get_session
    
    
    get_session(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.GetSessionRequest, dict]
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
    ) -> google.cloud.spanner_v1.types.spanner.Session

Gets a session.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.get_session](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_get_session)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.spanner_v1.services.spanner.transports.base.SpannerTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_get_transport_class)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.list_sessions
    
    
    list_sessions(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.ListSessionsRequest, dict]
        ] = None,
        *,
        database: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.spanner_v1.services.spanner.pagers.ListSessionsAsyncPager

Lists all sessions in a given database.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.list_sessions](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_list_sessions)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_parse_common_billing_account_path)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_parse_common_folder_path)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_parse_common_location_path)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_parse_common_organization_path)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_parse_common_project_path)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.parse_database_path
    
    
    parse_database_path(path: str) -> typing.Dict[str, str]

Parses a database path into its component segments.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.parse_database_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_parse_database_path)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.parse_session_path
    
    
    parse_session_path(path: str) -> typing.Dict[str, str]

Parses a session path into its component segments.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.parse_session_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_parse_session_path)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.partition_query
    
    
    partition_query(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.PartitionQueryRequest, dict]
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
    ) -> google.cloud.spanner_v1.types.spanner.PartitionResponse

Creates a set of partition tokens that can be used to execute a query operation in parallel.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.partition_query](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_partition_query)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.partition_read
    
    
    partition_read(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.PartitionReadRequest, dict]
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
    ) -> google.cloud.spanner_v1.types.spanner.PartitionResponse

Creates a set of partition tokens that can be used to execute a read operation in parallel.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.partition_read](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_partition_read)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.read
    
    
    read(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.ReadRequest, dict]
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
    ) -> google.cloud.spanner_v1.types.result_set.ResultSet

Reads rows from the database using key lookups and scans, as a simple key/value style alternative to `ExecuteSql][google.spanner.v1.Spanner.ExecuteSql]`.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.read](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_read)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.rollback
    
    
    rollback(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.RollbackRequest, dict]
        ] = None,
        *,
        session: typing.Optional[str] = None,
        transaction_id: typing.Optional[bytes] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Rolls back a transaction, releasing any locks it holds.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.rollback](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_rollback)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.session_path
    
    
    session_path(project: str, instance: str, database: str, session: str) -> str

Returns a fully-qualified session string.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.session_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_session_path)

### google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.streaming_read
    
    
    streaming_read(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.ReadRequest, dict]
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
    ) -> typing.Awaitable[
        typing.AsyncIterable[google.cloud.spanner_v1.types.result_set.PartialResultSet]
    ]

Like `Read][google.spanner.v1.Spanner.Read]`, except returns the result set as a stream.

See more: [google.cloud.spanner_v1.services.spanner.SpannerAsyncClient.streaming_read](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient#google_cloud_spanner_v1_services_spanner_SpannerAsyncClient_streaming_read)

### google.cloud.spanner_v1.services.spanner.SpannerClient
    
    
    SpannerClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.spanner_v1.services.spanner.transports.base.SpannerTransport,
                typing.Callable[
                    [...],
                    google.cloud.spanner_v1.services.spanner.transports.base.SpannerTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the spanner client.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_SpannerClient)

### google.cloud.spanner_v1.services.spanner.SpannerClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.**exit**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient___exit__)

### google.cloud.spanner_v1.services.spanner.SpannerClient.batch_create_sessions
    
    
    batch_create_sessions(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_v1.types.spanner.BatchCreateSessionsRequest, dict
            ]
        ] = None,
        *,
        database: typing.Optional[str] = None,
        session_count: typing.Optional[int] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.spanner_v1.types.spanner.BatchCreateSessionsResponse

Creates multiple new sessions.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.batch_create_sessions](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_batch_create_sessions)

### google.cloud.spanner_v1.services.spanner.SpannerClient.batch_write
    
    
    batch_write(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.BatchWriteRequest, dict]
        ] = None,
        *,
        session: typing.Optional[str] = None,
        mutation_groups: typing.Optional[
            typing.MutableSequence[
                google.cloud.spanner_v1.types.spanner.BatchWriteRequest.MutationGroup
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
    ) -> typing.Iterable[google.cloud.spanner_v1.types.spanner.BatchWriteResponse]

Batches the supplied mutation groups in a collection of efficient transactions.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.batch_write](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_batch_write)

### google.cloud.spanner_v1.services.spanner.SpannerClient.begin_transaction
    
    
    begin_transaction(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_v1.types.spanner.BeginTransactionRequest, dict
            ]
        ] = None,
        *,
        session: typing.Optional[str] = None,
        options: typing.Optional[
            google.cloud.spanner_v1.types.transaction.TransactionOptions
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.spanner_v1.types.transaction.Transaction

Begins a new transaction.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.begin_transaction](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_begin_transaction)

### google.cloud.spanner_v1.services.spanner.SpannerClient.commit
    
    
    commit(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.CommitRequest, dict]
        ] = None,
        *,
        session: typing.Optional[str] = None,
        transaction_id: typing.Optional[bytes] = None,
        mutations: typing.Optional[
            typing.MutableSequence[google.cloud.spanner_v1.types.mutation.Mutation]
        ] = None,
        single_use_transaction: typing.Optional[
            google.cloud.spanner_v1.types.transaction.TransactionOptions
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.spanner_v1.types.commit_response.CommitResponse

Commits a transaction.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.commit](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_commit)

### google.cloud.spanner_v1.services.spanner.SpannerClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_common_billing_account_path)

### google.cloud.spanner_v1.services.spanner.SpannerClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.common_folder_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_common_folder_path)

### google.cloud.spanner_v1.services.spanner.SpannerClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.common_location_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_common_location_path)

### google.cloud.spanner_v1.services.spanner.SpannerClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.common_organization_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_common_organization_path)

### google.cloud.spanner_v1.services.spanner.SpannerClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.common_project_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_common_project_path)

### google.cloud.spanner_v1.services.spanner.SpannerClient.create_session
    
    
    create_session(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.CreateSessionRequest, dict]
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
    ) -> google.cloud.spanner_v1.types.spanner.Session

Creates a new session.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.create_session](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_create_session)

### google.cloud.spanner_v1.services.spanner.SpannerClient.database_path
    
    
    database_path(project: str, instance: str, database: str) -> str

Returns a fully-qualified database string.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.database_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_database_path)

### google.cloud.spanner_v1.services.spanner.SpannerClient.delete_session
    
    
    delete_session(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.DeleteSessionRequest, dict]
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

Ends a session, releasing server resources associated with it.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.delete_session](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_delete_session)

### google.cloud.spanner_v1.services.spanner.SpannerClient.execute_batch_dml
    
    
    execute_batch_dml(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.ExecuteBatchDmlRequest, dict]
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
    ) -> google.cloud.spanner_v1.types.spanner.ExecuteBatchDmlResponse

Executes a batch of SQL DML statements.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.execute_batch_dml](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_execute_batch_dml)

### google.cloud.spanner_v1.services.spanner.SpannerClient.execute_sql
    
    
    execute_sql(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.ExecuteSqlRequest, dict]
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
    ) -> google.cloud.spanner_v1.types.result_set.ResultSet

Executes an SQL statement, returning all results in a single reply.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.execute_sql](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_execute_sql)

### google.cloud.spanner_v1.services.spanner.SpannerClient.execute_streaming_sql
    
    
    execute_streaming_sql(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.ExecuteSqlRequest, dict]
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
    ) -> typing.Iterable[google.cloud.spanner_v1.types.result_set.PartialResultSet]

Like `ExecuteSql][google.spanner.v1.Spanner.ExecuteSql]`, except returns the result set as a stream.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.execute_streaming_sql](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_execute_streaming_sql)

### google.cloud.spanner_v1.services.spanner.SpannerClient.fetch_cache_update
    
    
    fetch_cache_update(
        request: typing.Optional[
            typing.Union[
                google.cloud.spanner_v1.types.spanner.FetchCacheUpdateRequest, dict
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
    ) -> typing.Iterable[google.cloud.spanner_v1.types.location.CacheUpdate]

Retrieves a cache update for a given database.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.fetch_cache_update](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_fetch_cache_update)

### google.cloud.spanner_v1.services.spanner.SpannerClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.from_service_account_file](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_from_service_account_file)

### google.cloud.spanner_v1.services.spanner.SpannerClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.from_service_account_info](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_from_service_account_info)

### google.cloud.spanner_v1.services.spanner.SpannerClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.from_service_account_json](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_from_service_account_json)

### google.cloud.spanner_v1.services.spanner.SpannerClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_get_mtls_endpoint_and_cert_source)

### google.cloud.spanner_v1.services.spanner.SpannerClient.get_session
    
    
    get_session(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.GetSessionRequest, dict]
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
    ) -> google.cloud.spanner_v1.types.spanner.Session

Gets a session.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.get_session](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_get_session)

### google.cloud.spanner_v1.services.spanner.SpannerClient.list_sessions
    
    
    list_sessions(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.ListSessionsRequest, dict]
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
    ) -> google.cloud.spanner_v1.services.spanner.pagers.ListSessionsPager

Lists all sessions in a given database.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.list_sessions](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_list_sessions)

### google.cloud.spanner_v1.services.spanner.SpannerClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_parse_common_billing_account_path)

### google.cloud.spanner_v1.services.spanner.SpannerClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_parse_common_folder_path)

### google.cloud.spanner_v1.services.spanner.SpannerClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_parse_common_location_path)

### google.cloud.spanner_v1.services.spanner.SpannerClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_parse_common_organization_path)

### google.cloud.spanner_v1.services.spanner.SpannerClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_parse_common_project_path)

### google.cloud.spanner_v1.services.spanner.SpannerClient.parse_database_path
    
    
    parse_database_path(path: str) -> typing.Dict[str, str]

Parses a database path into its component segments.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.parse_database_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_parse_database_path)

### google.cloud.spanner_v1.services.spanner.SpannerClient.parse_session_path
    
    
    parse_session_path(path: str) -> typing.Dict[str, str]

Parses a session path into its component segments.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.parse_session_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_parse_session_path)

### google.cloud.spanner_v1.services.spanner.SpannerClient.partition_query
    
    
    partition_query(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.PartitionQueryRequest, dict]
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
    ) -> google.cloud.spanner_v1.types.spanner.PartitionResponse

Creates a set of partition tokens that can be used to execute a query operation in parallel.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.partition_query](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_partition_query)

### google.cloud.spanner_v1.services.spanner.SpannerClient.partition_read
    
    
    partition_read(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.PartitionReadRequest, dict]
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
    ) -> google.cloud.spanner_v1.types.spanner.PartitionResponse

Creates a set of partition tokens that can be used to execute a read operation in parallel.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.partition_read](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_partition_read)

### google.cloud.spanner_v1.services.spanner.SpannerClient.read
    
    
    read(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.ReadRequest, dict]
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
    ) -> google.cloud.spanner_v1.types.result_set.ResultSet

Reads rows from the database using key lookups and scans, as a simple key/value style alternative to `ExecuteSql][google.spanner.v1.Spanner.ExecuteSql]`.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.read](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_read)

### google.cloud.spanner_v1.services.spanner.SpannerClient.rollback
    
    
    rollback(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.RollbackRequest, dict]
        ] = None,
        *,
        session: typing.Optional[str] = None,
        transaction_id: typing.Optional[bytes] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Rolls back a transaction, releasing any locks it holds.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.rollback](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_rollback)

### google.cloud.spanner_v1.services.spanner.SpannerClient.session_path
    
    
    session_path(project: str, instance: str, database: str, session: str) -> str

Returns a fully-qualified session string.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.session_path](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_session_path)

### google.cloud.spanner_v1.services.spanner.SpannerClient.streaming_read
    
    
    streaming_read(
        request: typing.Optional[
            typing.Union[google.cloud.spanner_v1.types.spanner.ReadRequest, dict]
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
    ) -> typing.Iterable[google.cloud.spanner_v1.types.result_set.PartialResultSet]

Like `Read][google.spanner.v1.Spanner.Read]`, except returns the result set as a stream.

See more: [google.cloud.spanner_v1.services.spanner.SpannerClient.streaming_read](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient#google_cloud_spanner_v1_services_spanner_SpannerClient_streaming_read)

### google.cloud.spanner_v1.services.spanner.pagers.ListSessionsAsyncPager
    
    
    ListSessionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.spanner_v1.types.spanner.ListSessionsResponse],
        ],
        request: google.cloud.spanner_v1.types.spanner.ListSessionsRequest,
        response: google.cloud.spanner_v1.types.spanner.ListSessionsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.spanner_v1.services.spanner.pagers.ListSessionsAsyncPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.pagers.ListSessionsAsyncPager#google_cloud_spanner_v1_services_spanner_pagers_ListSessionsAsyncPager_ListSessionsAsyncPager)

### google.cloud.spanner_v1.services.spanner.pagers.ListSessionsPager
    
    
    ListSessionsPager(
        method: typing.Callable[
            [...], google.cloud.spanner_v1.types.spanner.ListSessionsResponse
        ],
        request: google.cloud.spanner_v1.types.spanner.ListSessionsRequest,
        response: google.cloud.spanner_v1.types.spanner.ListSessionsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.spanner_v1.services.spanner.pagers.ListSessionsPager](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.pagers.ListSessionsPager#google_cloud_spanner_v1_services_spanner_pagers_ListSessionsPager_ListSessionsPager)

### google.cloud.spanner_v1.session.Session.batch
    
    
    batch()

Factory to create a batch for this session.

See more: [google.cloud.spanner_v1.session.Session.batch](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.session.Session#google_cloud_spanner_v1_session_Session_batch)

### google.cloud.spanner_v1.session.Session.create
    
    
    create()

Create this session, bound to its database.

See more: [google.cloud.spanner_v1.session.Session.create](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.session.Session#google_cloud_spanner_v1_session_Session_create)

### google.cloud.spanner_v1.session.Session.delete
    
    
    delete()

Delete this session.

See more: [google.cloud.spanner_v1.session.Session.delete](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.session.Session#google_cloud_spanner_v1_session_Session_delete)

### google.cloud.spanner_v1.session.Session.execute_sql
    
    
    execute_sql(
        sql,
        params=None,
        param_types=None,
        query_mode=None,
        query_options=None,
        request_options=None,
        retry=_MethodDefault._DEFAULT_VALUE,
        timeout=_MethodDefault._DEFAULT_VALUE,
        column_info=None,
    )

Perform an `ExecuteStreamingSql` API request.

See more: [google.cloud.spanner_v1.session.Session.execute_sql](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.session.Session#google_cloud_spanner_v1_session_Session_execute_sql)

### google.cloud.spanner_v1.session.Session.exists
    
    
    exists()

Test for the existence of this session.

See more: [google.cloud.spanner_v1.session.Session.exists](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.session.Session#google_cloud_spanner_v1_session_Session_exists)

### google.cloud.spanner_v1.session.Session.ping
    
    
    ping()

Ping the session to keep it alive by executing "SELECT 1".

See more: [google.cloud.spanner_v1.session.Session.ping](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.session.Session#google_cloud_spanner_v1_session_Session_ping)

### google.cloud.spanner_v1.session.Session.read
    
    
    read(table, columns, keyset, index="", limit=0, column_info=None)

Perform a `StreamingRead` API request for rows in a table.

See more: [google.cloud.spanner_v1.session.Session.read](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.session.Session#google_cloud_spanner_v1_session_Session_read)

### google.cloud.spanner_v1.session.Session.run_in_transaction
    
    
    run_in_transaction(func, *args, **kw)

Perform a unit of work in a transaction, retrying on abort.

See more: [google.cloud.spanner_v1.session.Session.run_in_transaction](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.session.Session#google_cloud_spanner_v1_session_Session_run_in_transaction)

### google.cloud.spanner_v1.session.Session.snapshot
    
    
    snapshot(**kw)

Create a snapshot to perform a set of reads with shared staleness.

See more: [google.cloud.spanner_v1.session.Session.snapshot](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.session.Session#google_cloud_spanner_v1_session_Session_snapshot)

### google.cloud.spanner_v1.session.Session.transaction
    
    
    transaction(client_context=None) -> google.cloud.spanner_v1.transaction.Transaction

Create a transaction to perform a set of reads with shared staleness.

See more: [google.cloud.spanner_v1.session.Session.transaction](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.session.Session#google_cloud_spanner_v1_session_Session_transaction)

### google.cloud.spanner_v1.snapshot.Snapshot.begin
    
    
    begin() -> bytes

Begins a transaction on the database.

See more: [google.cloud.spanner_v1.snapshot.Snapshot.begin](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.snapshot.Snapshot#google_cloud_spanner_v1_snapshot_Snapshot_begin)

### google.cloud.spanner_v1.snapshot.Snapshot.execute_sql
    
    
    execute_sql(
        sql,
        params=None,
        param_types=None,
        query_mode=None,
        query_options=None,
        request_options=None,
        last_statement=False,
        partition=None,
        retry=_MethodDefault._DEFAULT_VALUE,
        timeout=_MethodDefault._DEFAULT_VALUE,
        data_boost_enabled=False,
        directed_read_options=None,
        column_info=None,
        lazy_decode=False,
    )

Perform an `ExecuteStreamingSql` API request.

See more: [google.cloud.spanner_v1.snapshot.Snapshot.execute_sql](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.snapshot.Snapshot#google_cloud_spanner_v1_snapshot_Snapshot_execute_sql)

### google.cloud.spanner_v1.snapshot.Snapshot.partition_query
    
    
    partition_query(
        sql,
        params=None,
        param_types=None,
        partition_size_bytes=None,
        max_partitions=None,
        *,
        retry=_MethodDefault._DEFAULT_VALUE,
        timeout=_MethodDefault._DEFAULT_VALUE
    )

Perform a `PartitionQuery` API request.

See more: [google.cloud.spanner_v1.snapshot.Snapshot.partition_query](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.snapshot.Snapshot#google_cloud_spanner_v1_snapshot_Snapshot_partition_query)

### google.cloud.spanner_v1.snapshot.Snapshot.partition_read
    
    
    partition_read(
        table,
        columns,
        keyset,
        index="",
        partition_size_bytes=None,
        max_partitions=None,
        *,
        retry=_MethodDefault._DEFAULT_VALUE,
        timeout=_MethodDefault._DEFAULT_VALUE
    )

Perform a `PartitionRead` API request for rows in a table.

See more: [google.cloud.spanner_v1.snapshot.Snapshot.partition_read](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.snapshot.Snapshot#google_cloud_spanner_v1_snapshot_Snapshot_partition_read)

### google.cloud.spanner_v1.snapshot.Snapshot.read
    
    
    read(
        table,
        columns,
        keyset,
        index="",
        limit=0,
        partition=None,
        request_options=None,
        data_boost_enabled=False,
        directed_read_options=None,
        *,
        retry=_MethodDefault._DEFAULT_VALUE,
        timeout=_MethodDefault._DEFAULT_VALUE,
        column_info=None,
        lazy_decode=False
    )

Perform a `StreamingRead` API request for rows in a table.

See more: [google.cloud.spanner_v1.snapshot.Snapshot.read](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.snapshot.Snapshot#google_cloud_spanner_v1_snapshot_Snapshot_read)

### google.cloud.spanner_v1.streamed.StreamedResultSet.decode_column
    
    
    decode_column(row: [], column_index: int)

Decodes a column from a protobuf value to a Python object.

See more: [google.cloud.spanner_v1.streamed.StreamedResultSet.decode_column](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.streamed.StreamedResultSet#google_cloud_spanner_v1_streamed_StreamedResultSet_decode_column)

### google.cloud.spanner_v1.streamed.StreamedResultSet.decode_row
    
    
    decode_row(row: []) -> []

Decodes a row from protobuf values to Python objects.

See more: [google.cloud.spanner_v1.streamed.StreamedResultSet.decode_row](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.streamed.StreamedResultSet#google_cloud_spanner_v1_streamed_StreamedResultSet_decode_row)

### google.cloud.spanner_v1.streamed.StreamedResultSet.one
    
    
    one()

Return exactly one result, or raise an exception.

See more: [google.cloud.spanner_v1.streamed.StreamedResultSet.one](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.streamed.StreamedResultSet#google_cloud_spanner_v1_streamed_StreamedResultSet_one)

### google.cloud.spanner_v1.streamed.StreamedResultSet.one_or_none
    
    
    one_or_none()

Return exactly one result, or None if there are no results.

See more: [google.cloud.spanner_v1.streamed.StreamedResultSet.one_or_none](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.streamed.StreamedResultSet#google_cloud_spanner_v1_streamed_StreamedResultSet_one_or_none)

### google.cloud.spanner_v1.streamed.StreamedResultSet.to_dict_list
    
    
    to_dict_list()

Return the result of a query as a list of dictionaries.

See more: [google.cloud.spanner_v1.streamed.StreamedResultSet.to_dict_list](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.streamed.StreamedResultSet#google_cloud_spanner_v1_streamed_StreamedResultSet_to_dict_list)

### google.cloud.spanner_v1.table.Table.exists
    
    
    exists()

Test whether this table exists.

See more: [google.cloud.spanner_v1.table.Table.exists](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.table.Table#google_cloud_spanner_v1_table_Table_exists)

### google.cloud.spanner_v1.table.Table.reload
    
    
    reload()

Reload this table.

See more: [google.cloud.spanner_v1.table.Table.reload](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.table.Table#google_cloud_spanner_v1_table_Table_reload)

### google.cloud.spanner_v1.transaction.DefaultTransactionOptions.__post_init__
    
    
    __post_init__()

Initialize _defaultReadWriteTransactionOptions automatically.

See more: [google.cloud.spanner_v1.transaction.DefaultTransactionOptions.**post_init**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.DefaultTransactionOptions#google_cloud_spanner_v1_transaction_DefaultTransactionOptions___post_init__)

### google.cloud.spanner_v1.transaction.Transaction.__enter__
    
    
    __enter__()

Begin `with` block.

See more: [google.cloud.spanner_v1.transaction.Transaction.**enter**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction___enter__)

### google.cloud.spanner_v1.transaction.Transaction.__exit__
    
    
    __exit__(exc_type, exc_val, exc_tb)

End `with` block.

See more: [google.cloud.spanner_v1.transaction.Transaction.**exit**](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction___exit__)

### google.cloud.spanner_v1.transaction.Transaction.ack
    
    
    ack(queue, key, ignore_not_found=None)

Acknowledge a message in a Cloud Spanner queue.

See more: [google.cloud.spanner_v1.transaction.Transaction.ack](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction_ack)

### google.cloud.spanner_v1.transaction.Transaction.batch_update
    
    
    batch_update(
        statements,
        request_options=None,
        last_statement=False,
        *,
        retry=_MethodDefault._DEFAULT_VALUE,
        timeout=_MethodDefault._DEFAULT_VALUE
    )

Perform a batch of DML statements via an `ExecuteBatchDml` request.

See more: [google.cloud.spanner_v1.transaction.Transaction.batch_update](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction_batch_update)

### google.cloud.spanner_v1.transaction.Transaction.begin
    
    
    begin() -> bytes

Begins a transaction on the database.

See more: [google.cloud.spanner_v1.transaction.Transaction.begin](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction_begin)

### google.cloud.spanner_v1.transaction.Transaction.commit
    
    
    commit(return_commit_stats=False, request_options=None, max_commit_delay=None)

Commit mutations to the database.

See more: [google.cloud.spanner_v1.transaction.Transaction.commit](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction_commit)

### google.cloud.spanner_v1.transaction.Transaction.delete
    
    
    delete(table, keyset)

Delete one or more table rows.

See more: [google.cloud.spanner_v1.transaction.Transaction.delete](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction_delete)

### google.cloud.spanner_v1.transaction.Transaction.execute_sql
    
    
    execute_sql(
        sql,
        params=None,
        param_types=None,
        query_mode=None,
        query_options=None,
        request_options=None,
        last_statement=False,
        partition=None,
        retry=_MethodDefault._DEFAULT_VALUE,
        timeout=_MethodDefault._DEFAULT_VALUE,
        data_boost_enabled=False,
        directed_read_options=None,
        column_info=None,
        lazy_decode=False,
    )

Perform an `ExecuteStreamingSql` API request.

See more: [google.cloud.spanner_v1.transaction.Transaction.execute_sql](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction_execute_sql)

### google.cloud.spanner_v1.transaction.Transaction.execute_update
    
    
    execute_update(
        dml,
        params=None,
        param_types=None,
        query_mode=None,
        query_options=None,
        request_options=None,
        last_statement=False,
        *,
        retry=_MethodDefault._DEFAULT_VALUE,
        timeout=_MethodDefault._DEFAULT_VALUE
    )

Perform an `ExecuteSql` API request with DML.

See more: [google.cloud.spanner_v1.transaction.Transaction.execute_update](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction_execute_update)

### google.cloud.spanner_v1.transaction.Transaction.insert
    
    
    insert(table, columns, values)

Insert one or more new table rows.

See more: [google.cloud.spanner_v1.transaction.Transaction.insert](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction_insert)

### google.cloud.spanner_v1.transaction.Transaction.insert_or_update
    
    
    insert_or_update(table, columns, values)

Insert/update one or more table rows.

See more: [google.cloud.spanner_v1.transaction.Transaction.insert_or_update](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction_insert_or_update)

### google.cloud.spanner_v1.transaction.Transaction.partition_query
    
    
    partition_query(
        sql,
        params=None,
        param_types=None,
        partition_size_bytes=None,
        max_partitions=None,
        *,
        retry=_MethodDefault._DEFAULT_VALUE,
        timeout=_MethodDefault._DEFAULT_VALUE
    )

Perform a `PartitionQuery` API request.

See more: [google.cloud.spanner_v1.transaction.Transaction.partition_query](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction_partition_query)

### google.cloud.spanner_v1.transaction.Transaction.partition_read
    
    
    partition_read(
        table,
        columns,
        keyset,
        index="",
        partition_size_bytes=None,
        max_partitions=None,
        *,
        retry=_MethodDefault._DEFAULT_VALUE,
        timeout=_MethodDefault._DEFAULT_VALUE
    )

Perform a `PartitionRead` API request for rows in a table.

See more: [google.cloud.spanner_v1.transaction.Transaction.partition_read](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction_partition_read)

### google.cloud.spanner_v1.transaction.Transaction.read
    
    
    read(
        table,
        columns,
        keyset,
        index="",
        limit=0,
        partition=None,
        request_options=None,
        data_boost_enabled=False,
        directed_read_options=None,
        *,
        retry=_MethodDefault._DEFAULT_VALUE,
        timeout=_MethodDefault._DEFAULT_VALUE,
        column_info=None,
        lazy_decode=False
    )

Perform a `StreamingRead` API request for rows in a table.

See more: [google.cloud.spanner_v1.transaction.Transaction.read](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction_read)

### google.cloud.spanner_v1.transaction.Transaction.replace
    
    
    replace(table, columns, values)

Replace one or more table rows.

See more: [google.cloud.spanner_v1.transaction.Transaction.replace](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction_replace)

### google.cloud.spanner_v1.transaction.Transaction.rollback
    
    
    rollback() -> None

Roll back a transaction on the database.

See more: [google.cloud.spanner_v1.transaction.Transaction.rollback](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction_rollback)

### google.cloud.spanner_v1.transaction.Transaction.send
    
    
    send(queue, key, payload=None, deliver_time=None)

Send a message to a Cloud Spanner queue.

See more: [google.cloud.spanner_v1.transaction.Transaction.send](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction_send)

### google.cloud.spanner_v1.transaction.Transaction.update
    
    
    update(table, columns, values)

Update one or more existing table rows.

See more: [google.cloud.spanner_v1.transaction.Transaction.update](https://cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction#google_cloud_spanner_v1_transaction_Transaction_update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
