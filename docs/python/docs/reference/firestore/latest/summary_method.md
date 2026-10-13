---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/summary_method/
title: Package Methods (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:29.556900+00:00
---

# Package Methods (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 

Summary of entries of Methods for firestore.

## 

### google.cloud.firestore_v1.async_transaction.async_transactional
    
    
    async_transactional(
        to_wrap: typing.Callable[
            [
                typing.Concatenate[
                    google.cloud.firestore_v1.async_transaction.AsyncTransaction, ~P
                ]
            ],
            typing.Awaitable[google.cloud.firestore_v1.async_transaction.T],
        ],
    ) -> typing.Callable[
        [
            typing.Concatenate[
                google.cloud.firestore_v1.async_transaction.AsyncTransaction, ~P
            ]
        ],
        typing.Awaitable[google.cloud.firestore_v1.async_transaction.T],
    ]

Decorate a callable so that it runs in a transaction.

See more: [google.cloud.firestore_v1.async_transaction.async_transactional](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_transaction#google_cloud_firestore_v1_async_transaction_async_transactional)

### google.cloud.firestore_v1.field_path.get_field_path
    
    
    get_field_path(field_names: typing.Iterable[str])

Create a **field path** from a list of nested field names.

See more: [google.cloud.firestore_v1.field_path.get_field_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path#google_cloud_firestore_v1_field_path_get_field_path)

### google.cloud.firestore_v1.field_path.get_nested_value
    
    
    get_nested_value(field_path: str, data: typing.MutableMapping[str, typing.Any])

Get a (potentially nested) value from a dictionary.

See more: [google.cloud.firestore_v1.field_path.get_nested_value](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path#google_cloud_firestore_v1_field_path_get_nested_value)

### google.cloud.firestore_v1.field_path.parse_field_path
    
    
    parse_field_path(api_repr: str)

Parse a **field path** from into a list of nested field names.

See more: [google.cloud.firestore_v1.field_path.parse_field_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path#google_cloud_firestore_v1_field_path_parse_field_path)

### google.cloud.firestore_v1.field_path.render_field_path
    
    
    render_field_path(field_names: typing.Iterable[str])

Create a **field path** from a list of nested field names.

See more: [google.cloud.firestore_v1.field_path.render_field_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path#google_cloud_firestore_v1_field_path_render_field_path)

### google.cloud.firestore_v1.field_path.split_field_path
    
    
    split_field_path(path: str | None)

Split a field path into valid elements (without dots).

See more: [google.cloud.firestore_v1.field_path.split_field_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path#google_cloud_firestore_v1_field_path_split_field_path)

### google.cloud.firestore_v1.transaction.transactional
    
    
    transactional(
        to_wrap: typing.Callable,
    ) -> google.cloud.firestore_v1.transaction._Transactional

Decorate a callable so that it runs in a transaction.

See more: [google.cloud.firestore_v1.transaction.transactional](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transaction#google_cloud_firestore_v1_transaction_transactional)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_FirestoreAdminClient)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.**exit**](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient___exit__)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.backup_path
    
    
    backup_path(project: str, location: str, backup: str) -> str

Returns a fully-qualified backup string.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.backup_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_backup_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.backup_schedule_path
    
    
    backup_schedule_path(project: str, database: str, backup_schedule: str) -> str

Returns a fully-qualified backup_schedule string.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.backup_schedule_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_backup_schedule_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.bulk_delete_documents
    
    
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

Bulk deletes a subset of documents from Google Cloud Firestore.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.bulk_delete_documents](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_bulk_delete_documents)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.cancel_operation
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.cancel_operation](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_cancel_operation)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.clone_database
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.clone_database](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_clone_database)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.collection_group_path
    
    
    collection_group_path(project: str, database: str, collection: str) -> str

Returns a fully-qualified collection_group string.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.collection_group_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_collection_group_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_common_billing_account_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.common_folder_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_common_folder_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.common_location_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_common_location_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.common_organization_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_common_organization_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.common_project_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_common_project_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.create_backup_schedule
    
    
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

Creates a backup schedule on a database.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.create_backup_schedule](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_create_backup_schedule)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.create_database
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.create_database](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_create_database)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.create_index
    
    
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

Creates a composite index.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.create_index](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_create_index)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.create_user_creds
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.create_user_creds](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_create_user_creds)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.database_path
    
    
    database_path(project: str, database: str) -> str

Returns a fully-qualified database string.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.database_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_database_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.delete_backup
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.delete_backup](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_delete_backup)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.delete_backup_schedule
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.delete_backup_schedule](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_delete_backup_schedule)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.delete_database
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.delete_database](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_delete_database)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.delete_index
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.delete_index](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_delete_index)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.delete_operation
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.delete_operation](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_delete_operation)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.delete_user_creds
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.delete_user_creds](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_delete_user_creds)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.disable_user_creds
    
    
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

Disables a user creds.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.disable_user_creds](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_disable_user_creds)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.enable_user_creds
    
    
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

Enables a user creds.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.enable_user_creds](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_enable_user_creds)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.export_documents
    
    
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

Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.export_documents](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_export_documents)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.field_path
    
    
    field_path(project: str, database: str, collection: str, field: str) -> str

Returns a fully-qualified field string.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.field_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_field_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.from_service_account_file](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_from_service_account_file)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.from_service_account_info](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_from_service_account_info)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.from_service_account_json](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_from_service_account_json)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.get_backup
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.get_backup](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_get_backup)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.get_backup_schedule
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.get_backup_schedule](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_get_backup_schedule)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.get_database
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.get_database](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_get_database)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.get_field
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.get_field](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_get_field)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.get_index
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.get_index](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_get_index)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_get_mtls_endpoint_and_cert_source)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.get_operation
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.get_operation](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_get_operation)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.get_user_creds
    
    
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

Gets a user creds resource.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.get_user_creds](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_get_user_creds)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.import_documents
    
    
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

Imports documents into Google Cloud Firestore.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.import_documents](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_import_documents)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.index_path
    
    
    index_path(project: str, database: str, collection: str, index: str) -> str

Returns a fully-qualified index string.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.index_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_index_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.list_backup_schedules
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.list_backup_schedules](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_list_backup_schedules)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.list_backups
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.list_backups](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_list_backups)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.list_databases
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.list_databases](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_list_databases)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.list_fields
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.list_fields](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_list_fields)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.list_indexes
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.list_indexes](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_list_indexes)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.list_operations
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.list_operations](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_list_operations)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.list_user_creds
    
    
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

List all user creds in the database.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.list_user_creds](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_list_user_creds)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.location_path
    
    
    location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.location_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_location_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.operation_path
    
    
    operation_path(project: str, database: str, operation: str) -> str

Returns a fully-qualified operation string.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.operation_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_operation_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_backup_path
    
    
    parse_backup_path(path: str) -> typing.Dict[str, str]

Parses a backup path into its component segments.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_backup_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_parse_backup_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_backup_schedule_path
    
    
    parse_backup_schedule_path(path: str) -> typing.Dict[str, str]

Parses a backup_schedule path into its component segments.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_backup_schedule_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_parse_backup_schedule_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_collection_group_path
    
    
    parse_collection_group_path(path: str) -> typing.Dict[str, str]

Parses a collection_group path into its component segments.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_collection_group_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_parse_collection_group_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_parse_common_billing_account_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_parse_common_folder_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_parse_common_location_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_parse_common_organization_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_parse_common_project_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_database_path
    
    
    parse_database_path(path: str) -> typing.Dict[str, str]

Parses a database path into its component segments.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_database_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_parse_database_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_field_path
    
    
    parse_field_path(path: str) -> typing.Dict[str, str]

Parses a field path into its component segments.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_field_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_parse_field_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_index_path
    
    
    parse_index_path(path: str) -> typing.Dict[str, str]

Parses a index path into its component segments.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_index_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_parse_index_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_location_path
    
    
    parse_location_path(path: str) -> typing.Dict[str, str]

Parses a location path into its component segments.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_location_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_parse_location_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_operation_path
    
    
    parse_operation_path(path: str) -> typing.Dict[str, str]

Parses a operation path into its component segments.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_operation_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_parse_operation_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_user_creds_path
    
    
    parse_user_creds_path(path: str) -> typing.Dict[str, str]

Parses a user_creds path into its component segments.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.parse_user_creds_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_parse_user_creds_path)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.reset_user_password
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.reset_user_password](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_reset_user_password)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.restore_database
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.restore_database](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_restore_database)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.update_backup_schedule
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.update_backup_schedule](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_update_backup_schedule)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.update_database
    
    
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

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.update_database](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_update_database)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.update_field
    
    
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

Updates a field configuration.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.update_field](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_update_field)

### google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.user_creds_path
    
    
    user_creds_path(project: str, database: str, user_creds: str) -> str

Returns a fully-qualified user_creds string.

See more: [google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient.user_creds_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient#google_cloud_firestore_admin_v1_services_firestore_admin_client_FirestoreAdminClient_user_creds_path)

### google.cloud.firestore_bundle.bundle.FirestoreBundle.add_document
    
    
    add_document(
        snapshot: google.cloud.firestore_v1.base_document.DocumentSnapshot,
    ) -> google.cloud.firestore_bundle.bundle.FirestoreBundle

Adds a document to the bundle.

See more: [google.cloud.firestore_bundle.bundle.FirestoreBundle.add_document](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_bundle.bundle.FirestoreBundle#google_cloud_firestore_bundle_bundle_FirestoreBundle_add_document)

### google.cloud.firestore_bundle.bundle.FirestoreBundle.add_named_query
    
    
    add_named_query(
        name: str, query: google.cloud.firestore_v1.base_query.BaseQuery
    ) -> google.cloud.firestore_bundle.bundle.FirestoreBundle

Adds a query to the bundle, referenced by the provided name.

See more: [google.cloud.firestore_bundle.bundle.FirestoreBundle.add_named_query](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_bundle.bundle.FirestoreBundle#google_cloud_firestore_bundle_bundle_FirestoreBundle_add_named_query)

### google.cloud.firestore_bundle.bundle.FirestoreBundle.build
    
    
    build() -> str

Iterates over the bundle's stored documents and queries and produces a single length-prefixed json string suitable for long-term storage.

See more: [google.cloud.firestore_bundle.bundle.FirestoreBundle.build](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_bundle.bundle.FirestoreBundle#google_cloud_firestore_bundle_bundle_FirestoreBundle_build)

### google.cloud.firestore_v1.aggregation.AggregationQuery.get
    
    
    get(
        transaction=None,
        retry: Union[retries.Retry, None, object] = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> QueryResultsList[AggregationResult]

Runs the aggregation query.

See more: [google.cloud.firestore_v1.aggregation.AggregationQuery.get](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.aggregation.AggregationQuery#google_cloud_firestore_v1_aggregation_AggregationQuery_get)

### google.cloud.firestore_v1.aggregation.AggregationQuery.stream
    
    
    stream(
        transaction: Optional["transaction.Transaction"] = None,
        retry: Union[retries.Retry, None, object] = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> StreamGenerator[List[AggregationResult]]

Runs the aggregation query.

See more: [google.cloud.firestore_v1.aggregation.AggregationQuery.stream](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.aggregation.AggregationQuery#google_cloud_firestore_v1_aggregation_AggregationQuery_stream)

### google.cloud.firestore_v1.async_aggregation.AsyncAggregationQuery.get
    
    
    get(
        transaction=None,
        retry: Union[retries.AsyncRetry, None, object] = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> QueryResultsList[List[AggregationResult]]

Runs the aggregation query.

See more: [google.cloud.firestore_v1.async_aggregation.AsyncAggregationQuery.get](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_aggregation.AsyncAggregationQuery#google_cloud_firestore_v1_async_aggregation_AsyncAggregationQuery_get)

### google.cloud.firestore_v1.async_aggregation.AsyncAggregationQuery.stream
    
    
    stream(
        transaction: Optional[transaction.Transaction] = None,
        retry: retries.AsyncRetry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> AsyncStreamGenerator[List[AggregationResult]]

Runs the aggregation query.

See more: [google.cloud.firestore_v1.async_aggregation.AsyncAggregationQuery.stream](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_aggregation.AsyncAggregationQuery#google_cloud_firestore_v1_async_aggregation_AsyncAggregationQuery_stream)

### google.cloud.firestore_v1.async_batch.AsyncWriteBatch.commit
    
    
    commit(
        retry: (
            google.api_core.retry.retry_unary_async.AsyncRetry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> list[google.cloud.firestore_v1.types.write.WriteResult]

Commit the changes accumulated in this batch.

See more: [google.cloud.firestore_v1.async_batch.AsyncWriteBatch.commit](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_batch.AsyncWriteBatch#google_cloud_firestore_v1_async_batch_AsyncWriteBatch_commit)

### google.cloud.firestore_v1.async_client.AsyncClient.batch
    
    
    batch() -> google.cloud.firestore_v1.async_batch.AsyncWriteBatch

Get a batch instance from this client.

See more: [google.cloud.firestore_v1.async_client.AsyncClient.batch](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_client.AsyncClient#google_cloud_firestore_v1_async_client_AsyncClient_batch)

### google.cloud.firestore_v1.async_client.AsyncClient.collection
    
    
    collection(
        *collection_path: str,
    ) -> google.cloud.firestore_v1.async_collection.AsyncCollectionReference

Get a reference to a collection.

See more: [google.cloud.firestore_v1.async_client.AsyncClient.collection](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_client.AsyncClient#google_cloud_firestore_v1_async_client_AsyncClient_collection)

### google.cloud.firestore_v1.async_client.AsyncClient.collection_group
    
    
    collection_group(
        collection_id: str,
    ) -> google.cloud.firestore_v1.async_query.AsyncCollectionGroup

Creates and returns a new AsyncQuery that includes all documents in the database that are contained in a collection or subcollection with the given collection_id.

See more: [google.cloud.firestore_v1.async_client.AsyncClient.collection_group](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_client.AsyncClient#google_cloud_firestore_v1_async_client_AsyncClient_collection_group)

### google.cloud.firestore_v1.async_client.AsyncClient.collections
    
    
    collections(
        retry: retries.AsyncRetry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        read_time: datetime.datetime | None = None
    ) -> AsyncGenerator[AsyncCollectionReference, Any]

List top-level collections of the client's database.

See more: [google.cloud.firestore_v1.async_client.AsyncClient.collections](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_client.AsyncClient#google_cloud_firestore_v1_async_client_AsyncClient_collections)

### google.cloud.firestore_v1.async_client.AsyncClient.document
    
    
    document(
        *document_path: str,
    ) -> google.cloud.firestore_v1.async_document.AsyncDocumentReference

Get a reference to a document in a collection.

See more: [google.cloud.firestore_v1.async_client.AsyncClient.document](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_client.AsyncClient#google_cloud_firestore_v1_async_client_AsyncClient_document)

### google.cloud.firestore_v1.async_client.AsyncClient.get_all
    
    
    get_all(
        references: List[AsyncDocumentReference],
        field_paths: Iterable[str] | None = None,
        transaction: AsyncTransaction | None = None,
        retry: retries.AsyncRetry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        read_time: datetime.datetime | None = None
    ) -> AsyncGenerator[DocumentSnapshot, Any]

Retrieve a batch of documents.

See more: [google.cloud.firestore_v1.async_client.AsyncClient.get_all](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_client.AsyncClient#google_cloud_firestore_v1_async_client_AsyncClient_get_all)

### google.cloud.firestore_v1.async_client.AsyncClient.pipeline
    
    
    pipeline() -> google.cloud.firestore_v1.pipeline_source.PipelineSource

Start a pipeline with this client.

See more: [google.cloud.firestore_v1.async_client.AsyncClient.pipeline](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_client.AsyncClient#google_cloud_firestore_v1_async_client_AsyncClient_pipeline)

### google.cloud.firestore_v1.async_client.AsyncClient.recursive_delete
    
    
    recursive_delete(
        reference: Union[AsyncCollectionReference, AsyncDocumentReference],
        *,
        bulk_writer: Optional["BulkWriter"] = None,
        chunk_size: int = 5000
    ) -> int

Deletes documents and their subcollections, regardless of collection name.

See more: [google.cloud.firestore_v1.async_client.AsyncClient.recursive_delete](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_client.AsyncClient#google_cloud_firestore_v1_async_client_AsyncClient_recursive_delete)

### google.cloud.firestore_v1.async_client.AsyncClient.transaction
    
    
    transaction(
        max_attempts: int = 5, read_only: bool = False
    ) -> google.cloud.firestore_v1.async_transaction.AsyncTransaction

Get a transaction that uses this client.

See more: [google.cloud.firestore_v1.async_client.AsyncClient.transaction](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_client.AsyncClient#google_cloud_firestore_v1_async_client_AsyncClient_transaction)

### google.cloud.firestore_v1.async_collection.AsyncCollectionReference.add
    
    
    add(
        document_data: dict,
        document_id: typing.Optional[str] = None,
        retry: (
            google.api_core.retry.retry_unary_async.AsyncRetry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> typing.Tuple[typing.Any, typing.Any]

Create a document in the Firestore database with the provided data.

See more: [google.cloud.firestore_v1.async_collection.AsyncCollectionReference.add](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_collection.AsyncCollectionReference#google_cloud_firestore_v1_async_collection_AsyncCollectionReference_add)

### google.cloud.firestore_v1.async_collection.AsyncCollectionReference.document
    
    
    document(document_id: str | None = None) -> AsyncDocumentReference

Create a sub-document underneath the current collection.

See more: [google.cloud.firestore_v1.async_collection.AsyncCollectionReference.document](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_collection.AsyncCollectionReference#google_cloud_firestore_v1_async_collection_AsyncCollectionReference_document)

### google.cloud.firestore_v1.async_collection.AsyncCollectionReference.get
    
    
    get(
        transaction: Optional[transaction.Transaction] = None,
        retry: retries.AsyncRetry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> QueryResultsList[DocumentSnapshot]

Read the documents in this collection.

See more: [google.cloud.firestore_v1.async_collection.AsyncCollectionReference.get](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_collection.AsyncCollectionReference#google_cloud_firestore_v1_async_collection_AsyncCollectionReference_get)

### google.cloud.firestore_v1.async_collection.AsyncCollectionReference.list_documents
    
    
    list_documents(
        page_size: int | None = None,
        retry: retries.AsyncRetry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        read_time: datetime.datetime | None = None
    ) -> AsyncGenerator[AsyncDocumentReference, None]

List all subdocuments of the current collection.

See more: [google.cloud.firestore_v1.async_collection.AsyncCollectionReference.list_documents](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_collection.AsyncCollectionReference#google_cloud_firestore_v1_async_collection_AsyncCollectionReference_list_documents)

### google.cloud.firestore_v1.async_collection.AsyncCollectionReference.stream
    
    
    stream(
        transaction: Optional[transaction.Transaction] = None,
        retry: retries.AsyncRetry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> AsyncStreamGenerator[DocumentSnapshot]

Read the documents in this collection.

See more: [google.cloud.firestore_v1.async_collection.AsyncCollectionReference.stream](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_collection.AsyncCollectionReference#google_cloud_firestore_v1_async_collection_AsyncCollectionReference_stream)

### google.cloud.firestore_v1.async_document.AsyncDocumentReference.collections
    
    
    collections(
        page_size: typing.Optional[int] = None,
        retry: (
            google.api_core.retry.retry_unary_async.AsyncRetry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
        *,
        read_time: typing.Optional[datetime.datetime] = None
    ) -> typing.AsyncGenerator

List subcollections of the current document.

See more: [google.cloud.firestore_v1.async_document.AsyncDocumentReference.collections](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_document.AsyncDocumentReference#google_cloud_firestore_v1_async_document_AsyncDocumentReference_collections)

### google.cloud.firestore_v1.async_document.AsyncDocumentReference.create
    
    
    create(
        document_data: dict,
        retry: (
            google.api_core.retry.retry_unary_async.AsyncRetry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> google.cloud.firestore_v1.types.write.WriteResult

Create the current document in the Firestore database.

See more: [google.cloud.firestore_v1.async_document.AsyncDocumentReference.create](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_document.AsyncDocumentReference#google_cloud_firestore_v1_async_document_AsyncDocumentReference_create)

### google.cloud.firestore_v1.async_document.AsyncDocumentReference.delete
    
    
    delete(
        option: typing.Optional[google.cloud.firestore_v1._helpers.WriteOption] = None,
        retry: (
            google.api_core.retry.retry_unary_async.AsyncRetry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> google.protobuf.timestamp_pb2.Timestamp

Delete the current document in the Firestore database.

See more: [google.cloud.firestore_v1.async_document.AsyncDocumentReference.delete](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_document.AsyncDocumentReference#google_cloud_firestore_v1_async_document_AsyncDocumentReference_delete)

### google.cloud.firestore_v1.async_document.AsyncDocumentReference.get
    
    
    get(
        field_paths: typing.Optional[typing.Iterable[str]] = None,
        transaction=None,
        retry: (
            google.api_core.retry.retry_unary_async.AsyncRetry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
        *,
        read_time: typing.Optional[datetime.datetime] = None
    ) -> google.cloud.firestore_v1.base_document.DocumentSnapshot

Retrieve a snapshot of the current document.

See more: [google.cloud.firestore_v1.async_document.AsyncDocumentReference.get](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_document.AsyncDocumentReference#google_cloud_firestore_v1_async_document_AsyncDocumentReference_get)

### google.cloud.firestore_v1.async_document.AsyncDocumentReference.set
    
    
    set(
        document_data: dict,
        merge: bool = False,
        retry: (
            google.api_core.retry.retry_unary_async.AsyncRetry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> google.cloud.firestore_v1.types.write.WriteResult

Replace the current document in the Firestore database.

See more: [google.cloud.firestore_v1.async_document.AsyncDocumentReference.set](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_document.AsyncDocumentReference#google_cloud_firestore_v1_async_document_AsyncDocumentReference_set)

### google.cloud.firestore_v1.async_document.AsyncDocumentReference.update
    
    
    update(
        field_updates: dict,
        option: typing.Optional[google.cloud.firestore_v1._helpers.WriteOption] = None,
        retry: (
            google.api_core.retry.retry_unary_async.AsyncRetry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> google.cloud.firestore_v1.types.write.WriteResult

Update an existing document in the Firestore database.

See more: [google.cloud.firestore_v1.async_document.AsyncDocumentReference.update](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_document.AsyncDocumentReference#google_cloud_firestore_v1_async_document_AsyncDocumentReference_update)

### google.cloud.firestore_v1.async_query.AsyncCollectionGroup.get_partitions
    
    
    get_partitions(
        partition_count,
        retry: retries.AsyncRetry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        read_time: Optional[datetime.datetime] = None
    ) -> AsyncGenerator[QueryPartition, None]

Partition a query for parallelization.

See more: [google.cloud.firestore_v1.async_query.AsyncCollectionGroup.get_partitions](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_query.AsyncCollectionGroup#google_cloud_firestore_v1_async_query_AsyncCollectionGroup_get_partitions)

### google.cloud.firestore_v1.async_query.AsyncQuery.avg
    
    
    avg(
        field_ref: str | FieldPath, alias: str | None = None
    ) -> Type["firestore_v1.async_aggregation.AsyncAggregationQuery"]

Adds an avg over the nested query.

See more: [google.cloud.firestore_v1.async_query.AsyncQuery.avg](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_query.AsyncQuery#google_cloud_firestore_v1_async_query_AsyncQuery_avg)

### google.cloud.firestore_v1.async_query.AsyncQuery.count
    
    
    count(
        alias: typing.Optional[str] = None,
    ) -> typing.Type[google.cloud.firestore_v1.async_aggregation.AsyncAggregationQuery]

Adds a count over the nested query.

See more: [google.cloud.firestore_v1.async_query.AsyncQuery.count](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_query.AsyncQuery#google_cloud_firestore_v1_async_query_AsyncQuery_count)

### google.cloud.firestore_v1.async_query.AsyncQuery.find_nearest
    
    
    find_nearest(
        vector_field: str,
        query_vector: Union[Vector, Sequence[float]],
        limit: int,
        distance_measure: DistanceMeasure,
        *,
        distance_result_field: Optional[str] = None,
        distance_threshold: Optional[float] = None
    ) -> AsyncVectorQuery

Finds the closest vector embeddings to the given query vector.

See more: [google.cloud.firestore_v1.async_query.AsyncQuery.find_nearest](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_query.AsyncQuery#google_cloud_firestore_v1_async_query_AsyncQuery_find_nearest)

### google.cloud.firestore_v1.async_query.AsyncQuery.get
    
    
    get(
        transaction: Optional[AsyncTransaction] = None,
        retry: retries.AsyncRetry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> QueryResultsList[DocumentSnapshot]

Read the documents in the collection that match this query.

See more: [google.cloud.firestore_v1.async_query.AsyncQuery.get](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_query.AsyncQuery#google_cloud_firestore_v1_async_query_AsyncQuery_get)

### google.cloud.firestore_v1.async_query.AsyncQuery.stream
    
    
    stream(
        transaction: Optional[AsyncTransaction] = None,
        retry: retries.AsyncRetry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> AsyncStreamGenerator[DocumentSnapshot]

Read the documents in the collection that match this query.

See more: [google.cloud.firestore_v1.async_query.AsyncQuery.stream](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_query.AsyncQuery#google_cloud_firestore_v1_async_query_AsyncQuery_stream)

### google.cloud.firestore_v1.async_query.AsyncQuery.sum
    
    
    sum(
        field_ref: str | FieldPath, alias: str | None = None
    ) -> Type["firestore_v1.async_aggregation.AsyncAggregationQuery"]

Adds a sum over the nested query.

See more: [google.cloud.firestore_v1.async_query.AsyncQuery.sum](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_query.AsyncQuery#google_cloud_firestore_v1_async_query_AsyncQuery_sum)

### google.cloud.firestore_v1.async_transaction.AsyncTransaction.commit
    
    
    commit(
        retry: (
            google.api_core.retry.retry_unary_async.AsyncRetry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> list[google.cloud.firestore_v1.types.write.WriteResult]

Commit the changes accumulated in this batch.

See more: [google.cloud.firestore_v1.async_transaction.AsyncTransaction.commit](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_transaction.AsyncTransaction#google_cloud_firestore_v1_async_transaction_AsyncTransaction_commit)

### google.cloud.firestore_v1.async_transaction.AsyncTransaction.create
    
    
    create(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        document_data: dict[str, typing.Any],
    ) -> None

Add a "change" to this batch to create a document.

See more: [google.cloud.firestore_v1.async_transaction.AsyncTransaction.create](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_transaction.AsyncTransaction#google_cloud_firestore_v1_async_transaction_AsyncTransaction_create)

### google.cloud.firestore_v1.async_transaction.AsyncTransaction.delete
    
    
    delete(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        option: typing.Optional[google.cloud.firestore_v1._helpers.WriteOption] = None,
    ) -> None

Add a "change" to delete a document.

See more: [google.cloud.firestore_v1.async_transaction.AsyncTransaction.delete](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_transaction.AsyncTransaction#google_cloud_firestore_v1_async_transaction_AsyncTransaction_delete)

### google.cloud.firestore_v1.async_transaction.AsyncTransaction.get
    
    
    get(
        ref_or_query: AsyncDocumentReference | AsyncQuery,
        retry: retries.AsyncRetry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> AsyncGenerator[DocumentSnapshot, Any] | AsyncStreamGenerator[DocumentSnapshot]

Retrieve a document or a query result from the database.

See more: [google.cloud.firestore_v1.async_transaction.AsyncTransaction.get](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_transaction.AsyncTransaction#google_cloud_firestore_v1_async_transaction_AsyncTransaction_get)

### google.cloud.firestore_v1.async_transaction.AsyncTransaction.get_all
    
    
    get_all(
        references: list,
        retry: retries.AsyncRetry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        read_time: datetime.datetime | None = None
    ) -> AsyncGenerator[DocumentSnapshot, Any]

Retrieves multiple documents from Firestore.

See more: [google.cloud.firestore_v1.async_transaction.AsyncTransaction.get_all](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_transaction.AsyncTransaction#google_cloud_firestore_v1_async_transaction_AsyncTransaction_get_all)

### google.cloud.firestore_v1.async_transaction.AsyncTransaction.set
    
    
    set(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        document_data: dict,
        merge: typing.Union[bool, list] = False,
    ) -> None

Add a "change" to replace a document.

See more: [google.cloud.firestore_v1.async_transaction.AsyncTransaction.set](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_transaction.AsyncTransaction#google_cloud_firestore_v1_async_transaction_AsyncTransaction_set)

### google.cloud.firestore_v1.async_transaction.AsyncTransaction.update
    
    
    update(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        field_updates: dict[str, typing.Any],
        option: typing.Optional[google.cloud.firestore_v1._helpers.WriteOption] = None,
    ) -> None

Add a "change" to update a document.

See more: [google.cloud.firestore_v1.async_transaction.AsyncTransaction.update](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_transaction.AsyncTransaction#google_cloud_firestore_v1_async_transaction_AsyncTransaction_update)

### google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery.add_aggregation
    
    
    add_aggregation(
        aggregation: google.cloud.firestore_v1.base_aggregation.BaseAggregation,
    ) -> None

Adds an aggregation operation to the nested query .

See more: [google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery.add_aggregation](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery#google_cloud_firestore_v1_base_aggregation_BaseAggregationQuery_add_aggregation)

### google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery.add_aggregations
    
    
    add_aggregations(
        aggregations: typing.List[
            google.cloud.firestore_v1.base_aggregation.BaseAggregation
        ],
    ) -> None

Adds a list of aggregations to the nested query .

See more: [google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery.add_aggregations](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery#google_cloud_firestore_v1_base_aggregation_BaseAggregationQuery_add_aggregations)

### google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery.avg
    
    
    avg(
        field_ref: str | google.cloud.firestore_v1.field_path.FieldPath,
        alias: typing.Optional[str] = None,
    )

Adds an avg over the nested query.

See more: [google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery.avg](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery#google_cloud_firestore_v1_base_aggregation_BaseAggregationQuery_avg)

### google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery.count
    
    
    count(alias: typing.Optional[str] = None)

Adds a count over the nested query.

See more: [google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery.count](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery#google_cloud_firestore_v1_base_aggregation_BaseAggregationQuery_count)

### google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery.get
    
    
    get(
        transaction=None,
        retry: Union[
            retries.Retry, retries.AsyncRetry, None, object
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> (
        QueryResultsList[AggregationResult]
        | Coroutine[Any, Any, List[List[AggregationResult]]]
    )

Runs the aggregation query.

See more: [google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery.get](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery#google_cloud_firestore_v1_base_aggregation_BaseAggregationQuery_get)

### google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery.stream
    
    
    stream(
        transaction: Optional[transaction.Transaction] = None,
        retry: (
            retries.Retry | retries.AsyncRetry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> (
        StreamGenerator[List[AggregationResult]]
        | AsyncStreamGenerator[List[AggregationResult]]
    )

Runs the aggregation query.

See more: [google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery.stream](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery#google_cloud_firestore_v1_base_aggregation_BaseAggregationQuery_stream)

### google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery.sum
    
    
    sum(
        field_ref: str | google.cloud.firestore_v1.field_path.FieldPath,
        alias: typing.Optional[str] = None,
    )

Adds a sum over the nested query.

See more: [google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery.sum](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery#google_cloud_firestore_v1_base_aggregation_BaseAggregationQuery_sum)

### google.cloud.firestore_v1.base_batch.BaseBatch.commit
    
    
    commit()

Sends all accumulated write operations to the server.

See more: [google.cloud.firestore_v1.base_batch.BaseBatch.commit](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_batch.BaseBatch#google_cloud_firestore_v1_base_batch_BaseBatch_commit)

### google.cloud.firestore_v1.base_batch.BaseBatch.create
    
    
    create(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        document_data: dict[str, typing.Any],
    ) -> None

Add a "change" to this batch to create a document.

See more: [google.cloud.firestore_v1.base_batch.BaseBatch.create](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_batch.BaseBatch#google_cloud_firestore_v1_base_batch_BaseBatch_create)

### google.cloud.firestore_v1.base_batch.BaseBatch.delete
    
    
    delete(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        option: typing.Optional[google.cloud.firestore_v1._helpers.WriteOption] = None,
    ) -> None

Add a "change" to delete a document.

See more: [google.cloud.firestore_v1.base_batch.BaseBatch.delete](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_batch.BaseBatch#google_cloud_firestore_v1_base_batch_BaseBatch_delete)

### google.cloud.firestore_v1.base_batch.BaseBatch.set
    
    
    set(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        document_data: dict,
        merge: typing.Union[bool, list] = False,
    ) -> None

Add a "change" to replace a document.

See more: [google.cloud.firestore_v1.base_batch.BaseBatch.set](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_batch.BaseBatch#google_cloud_firestore_v1_base_batch_BaseBatch_set)

### google.cloud.firestore_v1.base_batch.BaseBatch.update
    
    
    update(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        field_updates: dict[str, typing.Any],
        option: typing.Optional[google.cloud.firestore_v1._helpers.WriteOption] = None,
    ) -> None

Add a "change" to update a document.

See more: [google.cloud.firestore_v1.base_batch.BaseBatch.update](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_batch.BaseBatch#google_cloud_firestore_v1_base_batch_BaseBatch_update)

### google.cloud.firestore_v1.base_client.BaseClient.bulk_writer
    
    
    bulk_writer(
        options: typing.Optional[
            google.cloud.firestore_v1.bulk_writer.BulkWriterOptions
        ] = None,
    ) -> google.cloud.firestore_v1.bulk_writer.BulkWriter

Get a BulkWriter instance from this client.

See more: [google.cloud.firestore_v1.base_client.BaseClient.bulk_writer](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_client.BaseClient#google_cloud_firestore_v1_base_client_BaseClient_bulk_writer)

### google.cloud.firestore_v1.base_client.BaseClient.field_path
    
    
    field_path(*field_names: str) -> str

Create a **field path** from a list of nested field names.

See more: [google.cloud.firestore_v1.base_client.BaseClient.field_path](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_client.BaseClient#google_cloud_firestore_v1_base_client_BaseClient_field_path)

### google.cloud.firestore_v1.base_client.BaseClient.pipeline
    
    
    pipeline() -> google.cloud.firestore_v1.pipeline_source.PipelineSource

Start a pipeline with this client.

See more: [google.cloud.firestore_v1.base_client.BaseClient.pipeline](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_client.BaseClient#google_cloud_firestore_v1_base_client_BaseClient_pipeline)

### google.cloud.firestore_v1.base_client.BaseClient.write_option
    
    
    write_option(
        **kwargs,
    ) -> typing.Union[
        google.cloud.firestore_v1._helpers.ExistsOption,
        google.cloud.firestore_v1._helpers.LastUpdateOption,
    ]

Create a write option for write operations.

See more: [google.cloud.firestore_v1.base_client.BaseClient.write_option](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_client.BaseClient#google_cloud_firestore_v1_base_client_BaseClient_write_option)

### google.cloud.firestore_v1.base_collection.BaseCollectionReference.avg
    
    
    avg(field_ref: str | FieldPath, alias=None)

Adds an avg over the nested query.

See more: [google.cloud.firestore_v1.base_collection.BaseCollectionReference.avg](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference#google_cloud_firestore_v1_base_collection_BaseCollectionReference_avg)

### google.cloud.firestore_v1.base_collection.BaseCollectionReference.count
    
    
    count(alias=None)

Adds a count over the nested query.

See more: [google.cloud.firestore_v1.base_collection.BaseCollectionReference.count](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference#google_cloud_firestore_v1_base_collection_BaseCollectionReference_count)

### google.cloud.firestore_v1.base_collection.BaseCollectionReference.document
    
    
    document(
        document_id: typing.Optional[str] = None,
    ) -> google.cloud.firestore_v1.base_document.BaseDocumentReference

Create a sub-document underneath the current collection.

See more: [google.cloud.firestore_v1.base_collection.BaseCollectionReference.document](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference#google_cloud_firestore_v1_base_collection_BaseCollectionReference_document)

### google.cloud.firestore_v1.base_collection.BaseCollectionReference.end_at
    
    
    end_at(document_fields: Union[DocumentSnapshot, dict, list, tuple]) -> QueryType

End query at a cursor with this collection as parent.

See more: [google.cloud.firestore_v1.base_collection.BaseCollectionReference.end_at](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference#google_cloud_firestore_v1_base_collection_BaseCollectionReference_end_at)

### google.cloud.firestore_v1.base_collection.BaseCollectionReference.end_before
    
    
    end_before(
        document_fields: Union[DocumentSnapshot, dict, list, tuple],
    ) -> QueryType

End query before a cursor with this collection as parent.

See more: [google.cloud.firestore_v1.base_collection.BaseCollectionReference.end_before](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference#google_cloud_firestore_v1_base_collection_BaseCollectionReference_end_before)

### google.cloud.firestore_v1.base_collection.BaseCollectionReference.find_nearest
    
    
    find_nearest(
        vector_field: str,
        query_vector: Union[Vector, Sequence[float]],
        limit: int,
        distance_measure: DistanceMeasure,
        *,
        distance_result_field: Optional[str] = None,
        distance_threshold: Optional[float] = None
    ) -> VectorQuery

Finds the closest vector embeddings to the given query vector.

See more: [google.cloud.firestore_v1.base_collection.BaseCollectionReference.find_nearest](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference#google_cloud_firestore_v1_base_collection_BaseCollectionReference_find_nearest)

### google.cloud.firestore_v1.base_collection.BaseCollectionReference.limit
    
    
    limit(count: int) -> google.cloud.firestore_v1.base_query.QueryType

Create a limited query with this collection as parent.

See more: [google.cloud.firestore_v1.base_collection.BaseCollectionReference.limit](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference#google_cloud_firestore_v1_base_collection_BaseCollectionReference_limit)

### google.cloud.firestore_v1.base_collection.BaseCollectionReference.limit_to_last
    
    
    limit_to_last(count: int)

Create a limited to last query with this collection as parent.

See more: [google.cloud.firestore_v1.base_collection.BaseCollectionReference.limit_to_last](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference#google_cloud_firestore_v1_base_collection_BaseCollectionReference_limit_to_last)

### google.cloud.firestore_v1.base_collection.BaseCollectionReference.offset
    
    
    offset(num_to_skip: int) -> google.cloud.firestore_v1.base_query.QueryType

Skip to an offset in a query with this collection as parent.

See more: [google.cloud.firestore_v1.base_collection.BaseCollectionReference.offset](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference#google_cloud_firestore_v1_base_collection_BaseCollectionReference_offset)

### google.cloud.firestore_v1.base_collection.BaseCollectionReference.order_by
    
    
    order_by(
        field_path: str, **kwargs
    ) -> google.cloud.firestore_v1.base_query.QueryType

Create an "order by" query with this collection as parent.

See more: [google.cloud.firestore_v1.base_collection.BaseCollectionReference.order_by](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference#google_cloud_firestore_v1_base_collection_BaseCollectionReference_order_by)

### google.cloud.firestore_v1.base_collection.BaseCollectionReference.select
    
    
    select(
        field_paths: typing.Iterable[str],
    ) -> google.cloud.firestore_v1.base_query.QueryType

Create a "select" query with this collection as parent.

See more: [google.cloud.firestore_v1.base_collection.BaseCollectionReference.select](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference#google_cloud_firestore_v1_base_collection_BaseCollectionReference_select)

### google.cloud.firestore_v1.base_collection.BaseCollectionReference.start_after
    
    
    start_after(
        document_fields: Union[DocumentSnapshot, dict, list, tuple],
    ) -> QueryType

Start query after a cursor with this collection as parent.

See more: [google.cloud.firestore_v1.base_collection.BaseCollectionReference.start_after](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference#google_cloud_firestore_v1_base_collection_BaseCollectionReference_start_after)

### google.cloud.firestore_v1.base_collection.BaseCollectionReference.start_at
    
    
    start_at(document_fields: Union[DocumentSnapshot, dict, list, tuple]) -> QueryType

Start query at a cursor with this collection as parent.

See more: [google.cloud.firestore_v1.base_collection.BaseCollectionReference.start_at](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference#google_cloud_firestore_v1_base_collection_BaseCollectionReference_start_at)

### google.cloud.firestore_v1.base_collection.BaseCollectionReference.sum
    
    
    sum(field_ref: str | FieldPath, alias=None)

Adds a sum over the nested query.

See more: [google.cloud.firestore_v1.base_collection.BaseCollectionReference.sum](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference#google_cloud_firestore_v1_base_collection_BaseCollectionReference_sum)

### google.cloud.firestore_v1.base_collection.BaseCollectionReference.where
    
    
    where(
        field_path: typing.Optional[str] = None,
        op_string: typing.Optional[str] = None,
        value=None,
        *,
        filter=None
    ) -> google.cloud.firestore_v1.base_query.QueryType

Create a "where" query with this collection as parent.

See more: [google.cloud.firestore_v1.base_collection.BaseCollectionReference.where](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference#google_cloud_firestore_v1_base_collection_BaseCollectionReference_where)

### google.cloud.firestore_v1.base_document.BaseDocumentReference.__copy__
    
    
    __copy__()

Shallow copy the instance.

See more: [google.cloud.firestore_v1.base_document.BaseDocumentReference.**copy**](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.BaseDocumentReference#google_cloud_firestore_v1_base_document_BaseDocumentReference___copy__)

### google.cloud.firestore_v1.base_document.BaseDocumentReference.__deepcopy__
    
    
    __deepcopy__(unused_memo)

Deep copy the instance.

See more: [google.cloud.firestore_v1.base_document.BaseDocumentReference.**deepcopy**](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.BaseDocumentReference#google_cloud_firestore_v1_base_document_BaseDocumentReference___deepcopy__)

### google.cloud.firestore_v1.base_document.BaseDocumentReference.__eq__
    
    
    __eq__(other)

Equality check against another instance.

See more: [google.cloud.firestore_v1.base_document.BaseDocumentReference.**eq**](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.BaseDocumentReference#google_cloud_firestore_v1_base_document_BaseDocumentReference___eq__)

### google.cloud.firestore_v1.base_document.BaseDocumentReference.__ne__
    
    
    __ne__(other)

Inequality check against another instance.

See more: [google.cloud.firestore_v1.base_document.BaseDocumentReference.**ne**](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.BaseDocumentReference#google_cloud_firestore_v1_base_document_BaseDocumentReference___ne__)

### google.cloud.firestore_v1.base_document.BaseDocumentReference.collection
    
    
    collection(collection_id: str)

Create a sub-collection underneath the current document.

See more: [google.cloud.firestore_v1.base_document.BaseDocumentReference.collection](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.BaseDocumentReference#google_cloud_firestore_v1_base_document_BaseDocumentReference_collection)

### google.cloud.firestore_v1.base_document.DocumentSnapshot.get
    
    
    get(field_path: str) -> typing.Any

Get a value from the snapshot data.

See more: [google.cloud.firestore_v1.base_document.DocumentSnapshot.get](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.DocumentSnapshot#google_cloud_firestore_v1_base_document_DocumentSnapshot_get)

### google.cloud.firestore_v1.base_document.DocumentSnapshot.to_dict
    
    
    to_dict() -> typing.Optional[typing.Dict[str, typing.Any]]

Retrieve the data contained in this snapshot.

See more: [google.cloud.firestore_v1.base_document.DocumentSnapshot.to_dict](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.DocumentSnapshot#google_cloud_firestore_v1_base_document_DocumentSnapshot_to_dict)

### google.cloud.firestore_v1.base_query.BaseQuery.end_at
    
    
    end_at(
        document_fields_or_snapshot: typing.Optional[
            typing.Union[
                google.cloud.firestore_v1.base_document.DocumentSnapshot, dict, list, tuple
            ]
        ],
    ) -> google.cloud.firestore_v1.base_query.QueryType

End query results at a particular document value.

See more: [google.cloud.firestore_v1.base_query.BaseQuery.end_at](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseQuery#google_cloud_firestore_v1_base_query_BaseQuery_end_at)

### google.cloud.firestore_v1.base_query.BaseQuery.end_before
    
    
    end_before(
        document_fields_or_snapshot: typing.Optional[
            typing.Union[
                google.cloud.firestore_v1.base_document.DocumentSnapshot, dict, list, tuple
            ]
        ],
    ) -> google.cloud.firestore_v1.base_query.QueryType

End query results before a particular document value.

See more: [google.cloud.firestore_v1.base_query.BaseQuery.end_before](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseQuery#google_cloud_firestore_v1_base_query_BaseQuery_end_before)

### google.cloud.firestore_v1.base_query.BaseQuery.limit
    
    
    limit(count: int) -> google.cloud.firestore_v1.base_query.QueryType

Limit a query to return at most `count` matching results.

See more: [google.cloud.firestore_v1.base_query.BaseQuery.limit](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseQuery#google_cloud_firestore_v1_base_query_BaseQuery_limit)

### google.cloud.firestore_v1.base_query.BaseQuery.limit_to_last
    
    
    limit_to_last(count: int) -> google.cloud.firestore_v1.base_query.QueryType

Limit a query to return the last `count` matching results.

See more: [google.cloud.firestore_v1.base_query.BaseQuery.limit_to_last](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseQuery#google_cloud_firestore_v1_base_query_BaseQuery_limit_to_last)

### google.cloud.firestore_v1.base_query.BaseQuery.offset
    
    
    offset(num_to_skip: int) -> google.cloud.firestore_v1.base_query.QueryType

Skip to an offset in a query.

See more: [google.cloud.firestore_v1.base_query.BaseQuery.offset](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseQuery#google_cloud_firestore_v1_base_query_BaseQuery_offset)

### google.cloud.firestore_v1.base_query.BaseQuery.order_by
    
    
    order_by(
        field_path: str, direction: str = "ASCENDING"
    ) -> google.cloud.firestore_v1.base_query.QueryType

Modify the query to add an order clause on a specific field.

See more: [google.cloud.firestore_v1.base_query.BaseQuery.order_by](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseQuery#google_cloud_firestore_v1_base_query_BaseQuery_order_by)

### google.cloud.firestore_v1.base_query.BaseQuery.recursive
    
    
    recursive() -> google.cloud.firestore_v1.base_query.QueryType

Returns a copy of this query whose iterator will yield all matching documents as well as each of their descendent subcollections and documents.

See more: [google.cloud.firestore_v1.base_query.BaseQuery.recursive](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseQuery#google_cloud_firestore_v1_base_query_BaseQuery_recursive)

### google.cloud.firestore_v1.base_query.BaseQuery.select
    
    
    select(
        field_paths: typing.Iterable[str],
    ) -> google.cloud.firestore_v1.base_query.QueryType

Project documents matching query to a limited set of fields.

See more: [google.cloud.firestore_v1.base_query.BaseQuery.select](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseQuery#google_cloud_firestore_v1_base_query_BaseQuery_select)

### google.cloud.firestore_v1.base_query.BaseQuery.start_after
    
    
    start_after(
        document_fields_or_snapshot: typing.Optional[
            typing.Union[
                google.cloud.firestore_v1.base_document.DocumentSnapshot, dict, list, tuple
            ]
        ],
    ) -> google.cloud.firestore_v1.base_query.QueryType

Start query results after a particular document value.

See more: [google.cloud.firestore_v1.base_query.BaseQuery.start_after](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseQuery#google_cloud_firestore_v1_base_query_BaseQuery_start_after)

### google.cloud.firestore_v1.base_query.BaseQuery.start_at
    
    
    start_at(
        document_fields_or_snapshot: typing.Optional[
            typing.Union[
                google.cloud.firestore_v1.base_document.DocumentSnapshot, dict, list, tuple
            ]
        ],
    ) -> google.cloud.firestore_v1.base_query.QueryType

Start query results at a particular document value.

See more: [google.cloud.firestore_v1.base_query.BaseQuery.start_at](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseQuery#google_cloud_firestore_v1_base_query_BaseQuery_start_at)

### google.cloud.firestore_v1.base_query.BaseQuery.where
    
    
    where(
        field_path: typing.Optional[str] = None,
        op_string: typing.Optional[str] = None,
        value=None,
        *,
        filter=None
    ) -> google.cloud.firestore_v1.base_query.QueryType

Filter the query on a field.

See more: [google.cloud.firestore_v1.base_query.BaseQuery.where](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseQuery#google_cloud_firestore_v1_base_query_BaseQuery_where)

### google.cloud.firestore_v1.base_query.QueryPartition.query
    
    
    query()

Generate a new query using this partition's bounds.

See more: [google.cloud.firestore_v1.base_query.QueryPartition.query](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.QueryPartition#google_cloud_firestore_v1_base_query_QueryPartition_query)

### google.cloud.firestore_v1.batch.WriteBatch.commit
    
    
    commit(
        retry: (
            google.api_core.retry.retry_unary.Retry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> list

Commit the changes accumulated in this batch.

See more: [google.cloud.firestore_v1.batch.WriteBatch.commit](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.batch.WriteBatch#google_cloud_firestore_v1_batch_WriteBatch_commit)

### google.cloud.firestore_v1.bulk_writer.BulkWriter.close
    
    
    close()

Block until all pooled write operations are complete and then reject any further write operations.

See more: [google.cloud.firestore_v1.bulk_writer.BulkWriter.close](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.bulk_writer.BulkWriter#google_cloud_firestore_v1_bulk_writer_BulkWriter_close)

### google.cloud.firestore_v1.bulk_writer.BulkWriter.create
    
    
    create(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        document_data: typing.Dict,
        attempts: int = 0,
    ) -> None

Adds a `create` pb to the in-progress batch.

See more: [google.cloud.firestore_v1.bulk_writer.BulkWriter.create](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.bulk_writer.BulkWriter#google_cloud_firestore_v1_bulk_writer_BulkWriter_create)

### google.cloud.firestore_v1.bulk_writer.BulkWriter.delete
    
    
    delete(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        option: typing.Optional[google.cloud.firestore_v1._helpers.WriteOption] = None,
        attempts: int = 0,
    ) -> None

Adds a `delete` pb to the in-progress batch.

See more: [google.cloud.firestore_v1.bulk_writer.BulkWriter.delete](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.bulk_writer.BulkWriter#google_cloud_firestore_v1_bulk_writer_BulkWriter_delete)

### google.cloud.firestore_v1.bulk_writer.BulkWriter.flush
    
    
    flush()

Block until all pooled write operations are complete and then resume accepting new write operations.

See more: [google.cloud.firestore_v1.bulk_writer.BulkWriter.flush](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.bulk_writer.BulkWriter#google_cloud_firestore_v1_bulk_writer_BulkWriter_flush)

### google.cloud.firestore_v1.bulk_writer.BulkWriter.on_batch_result
    
    
    on_batch_result(
        callback: typing.Optional[
            typing.Callable[
                [
                    google.cloud.firestore_v1.bulk_batch.BulkWriteBatch,
                    google.cloud.firestore_v1.types.firestore.BatchWriteResponse,
                    google.cloud.firestore_v1.bulk_writer.BulkWriter,
                ],
                None,
            ]
        ],
    ) -> None

Sets a callback that will be invoked once for every successful batch.

See more: [google.cloud.firestore_v1.bulk_writer.BulkWriter.on_batch_result](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.bulk_writer.BulkWriter#google_cloud_firestore_v1_bulk_writer_BulkWriter_on_batch_result)

### google.cloud.firestore_v1.bulk_writer.BulkWriter.on_write_error
    
    
    on_write_error(
        callback: typing.Optional[
            typing.Callable[
                [
                    google.cloud.firestore_v1.bulk_writer.BulkWriteFailure,
                    google.cloud.firestore_v1.bulk_writer.BulkWriter,
                ],
                bool,
            ]
        ],
    ) -> None

Sets a callback that will be invoked once for every batch that contains an error.

See more: [google.cloud.firestore_v1.bulk_writer.BulkWriter.on_write_error](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.bulk_writer.BulkWriter#google_cloud_firestore_v1_bulk_writer_BulkWriter_on_write_error)

### google.cloud.firestore_v1.bulk_writer.BulkWriter.on_write_result
    
    
    on_write_result(
        callback: typing.Optional[
            typing.Callable[
                [
                    google.cloud.firestore_v1.base_document.BaseDocumentReference,
                    google.cloud.firestore_v1.types.write.WriteResult,
                    google.cloud.firestore_v1.bulk_writer.BulkWriter,
                ],
                None,
            ]
        ],
    ) -> None

Sets a callback that will be invoked once for every successful operation.

See more: [google.cloud.firestore_v1.bulk_writer.BulkWriter.on_write_result](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.bulk_writer.BulkWriter#google_cloud_firestore_v1_bulk_writer_BulkWriter_on_write_result)

### google.cloud.firestore_v1.bulk_writer.BulkWriter.set
    
    
    set(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        document_data: typing.Dict,
        merge: typing.Union[bool, list] = False,
        attempts: int = 0,
    ) -> None

Adds a `set` pb to the in-progress batch.

See more: [google.cloud.firestore_v1.bulk_writer.BulkWriter.set](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.bulk_writer.BulkWriter#google_cloud_firestore_v1_bulk_writer_BulkWriter_set)

### google.cloud.firestore_v1.bulk_writer.BulkWriter.update
    
    
    update(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        field_updates: dict,
        option: typing.Optional[google.cloud.firestore_v1._helpers.WriteOption] = None,
        attempts: int = 0,
    ) -> None

Adds an `update` pb to the in-progress batch.

See more: [google.cloud.firestore_v1.bulk_writer.BulkWriter.update](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.bulk_writer.BulkWriter#google_cloud_firestore_v1_bulk_writer_BulkWriter_update)

### google.cloud.firestore_v1.client.Client.batch
    
    
    batch() -> google.cloud.firestore_v1.batch.WriteBatch

Get a batch instance from this client.

See more: [google.cloud.firestore_v1.client.Client.batch](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client#google_cloud_firestore_v1_client_Client_batch)

### google.cloud.firestore_v1.client.Client.collection
    
    
    collection(
        *collection_path: str,
    ) -> google.cloud.firestore_v1.collection.CollectionReference

Get a reference to a collection.

See more: [google.cloud.firestore_v1.client.Client.collection](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client#google_cloud_firestore_v1_client_Client_collection)

### google.cloud.firestore_v1.client.Client.collection_group
    
    
    collection_group(
        collection_id: str,
    ) -> google.cloud.firestore_v1.query.CollectionGroup

Creates and returns a new Query that includes all documents in the database that are contained in a collection or subcollection with the given collection_id.

See more: [google.cloud.firestore_v1.client.Client.collection_group](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client#google_cloud_firestore_v1_client_Client_collection_group)

### google.cloud.firestore_v1.client.Client.collections
    
    
    collections(
        retry: retries.Retry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        read_time: datetime.datetime | None = None
    ) -> Generator[Any, Any, None]

List top-level collections of the client's database.

See more: [google.cloud.firestore_v1.client.Client.collections](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client#google_cloud_firestore_v1_client_Client_collections)

### google.cloud.firestore_v1.client.Client.document
    
    
    document(
        *document_path: str,
    ) -> google.cloud.firestore_v1.document.DocumentReference

Get a reference to a document in a collection.

See more: [google.cloud.firestore_v1.client.Client.document](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client#google_cloud_firestore_v1_client_Client_document)

### google.cloud.firestore_v1.client.Client.get_all
    
    
    get_all(
        references: list,
        field_paths: Iterable[str] | None = None,
        transaction: Transaction | None = None,
        retry: retries.Retry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        read_time: datetime.datetime | None = None
    ) -> Generator[DocumentSnapshot, Any, None]

Retrieve a batch of documents.

See more: [google.cloud.firestore_v1.client.Client.get_all](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client#google_cloud_firestore_v1_client_Client_get_all)

### google.cloud.firestore_v1.client.Client.pipeline
    
    
    pipeline() -> google.cloud.firestore_v1.pipeline_source.PipelineSource

Start a pipeline with this client.

See more: [google.cloud.firestore_v1.client.Client.pipeline](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client#google_cloud_firestore_v1_client_Client_pipeline)

### google.cloud.firestore_v1.client.Client.recursive_delete
    
    
    recursive_delete(
        reference: Union[CollectionReference, DocumentReference],
        *,
        bulk_writer: Optional["BulkWriter"] = None,
        chunk_size: int = 5000
    ) -> int

Deletes documents and their subcollections, regardless of collection name.

See more: [google.cloud.firestore_v1.client.Client.recursive_delete](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client#google_cloud_firestore_v1_client_Client_recursive_delete)

### google.cloud.firestore_v1.client.Client.transaction
    
    
    transaction(
        max_attempts: int = 5, read_only: bool = False
    ) -> google.cloud.firestore_v1.transaction.Transaction

Get a transaction that uses this client.

See more: [google.cloud.firestore_v1.client.Client.transaction](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client#google_cloud_firestore_v1_client_Client_transaction)

### google.cloud.firestore_v1.collection.CollectionReference.add
    
    
    add(
        document_data: dict,
        document_id: typing.Optional[str] = None,
        retry: (
            google.api_core.retry.retry_unary.Retry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> typing.Tuple[typing.Any, typing.Any]

Create a document in the Firestore database with the provided data.

See more: [google.cloud.firestore_v1.collection.CollectionReference.add](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.collection.CollectionReference#google_cloud_firestore_v1_collection_CollectionReference_add)

### google.cloud.firestore_v1.collection.CollectionReference.document
    
    
    document(document_id: Union[str, None] = None) -> DocumentReference

Create a sub-document underneath the current collection.

See more: [google.cloud.firestore_v1.collection.CollectionReference.document](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.collection.CollectionReference#google_cloud_firestore_v1_collection_CollectionReference_document)

### google.cloud.firestore_v1.collection.CollectionReference.get
    
    
    get(
        transaction: Union[transaction.Transaction, None] = None,
        retry: retries.Retry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: Union[float, None] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> QueryResultsList[DocumentSnapshot]

Read the documents in this collection.

See more: [google.cloud.firestore_v1.collection.CollectionReference.get](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.collection.CollectionReference#google_cloud_firestore_v1_collection_CollectionReference_get)

### google.cloud.firestore_v1.collection.CollectionReference.list_documents
    
    
    list_documents(
        page_size: Union[int, None] = None,
        retry: retries.Retry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: Union[float, None] = None,
        *,
        read_time: Optional[datetime.datetime] = None
    ) -> Generator[Any, Any, None]

List all subdocuments of the current collection.

See more: [google.cloud.firestore_v1.collection.CollectionReference.list_documents](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.collection.CollectionReference#google_cloud_firestore_v1_collection_CollectionReference_list_documents)

### google.cloud.firestore_v1.collection.CollectionReference.on_snapshot
    
    
    on_snapshot(callback: typing.Callable) -> google.cloud.firestore_v1.watch.Watch

Monitor the documents in this collection.

See more: [google.cloud.firestore_v1.collection.CollectionReference.on_snapshot](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.collection.CollectionReference#google_cloud_firestore_v1_collection_CollectionReference_on_snapshot)

### google.cloud.firestore_v1.collection.CollectionReference.stream
    
    
    stream(
        transaction: Optional[transaction.Transaction] = None,
        retry: retries.Retry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> StreamGenerator[DocumentSnapshot]

Read the documents in this collection.

See more: [google.cloud.firestore_v1.collection.CollectionReference.stream](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.collection.CollectionReference#google_cloud_firestore_v1_collection_CollectionReference_stream)

### google.cloud.firestore_v1.document.DocumentReference.collections
    
    
    collections(
        page_size: typing.Optional[int] = None,
        retry: (
            google.api_core.retry.retry_unary.Retry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
        *,
        read_time: typing.Optional[datetime.datetime] = None
    ) -> typing.Generator[typing.Any, typing.Any, None]

List subcollections of the current document.

See more: [google.cloud.firestore_v1.document.DocumentReference.collections](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference#google_cloud_firestore_v1_document_DocumentReference_collections)

### google.cloud.firestore_v1.document.DocumentReference.create
    
    
    create(
        document_data: dict,
        retry: (
            google.api_core.retry.retry_unary.Retry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> google.cloud.firestore_v1.types.write.WriteResult

Create a document in the Firestore database.

See more: [google.cloud.firestore_v1.document.DocumentReference.create](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference#google_cloud_firestore_v1_document_DocumentReference_create)

### google.cloud.firestore_v1.document.DocumentReference.delete
    
    
    delete(
        option: typing.Optional[google.cloud.firestore_v1._helpers.WriteOption] = None,
        retry: (
            google.api_core.retry.retry_unary.Retry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> google.protobuf.timestamp_pb2.Timestamp

Delete the current document in the Firestore database.

See more: [google.cloud.firestore_v1.document.DocumentReference.delete](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference#google_cloud_firestore_v1_document_DocumentReference_delete)

### google.cloud.firestore_v1.document.DocumentReference.get
    
    
    get(
        field_paths: typing.Optional[typing.Iterable[str]] = None,
        transaction=None,
        retry: (
            google.api_core.retry.retry_unary.Retry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
        *,
        read_time: typing.Optional[datetime.datetime] = None
    ) -> google.cloud.firestore_v1.base_document.DocumentSnapshot

Retrieve a snapshot of the current document.

See more: [google.cloud.firestore_v1.document.DocumentReference.get](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference#google_cloud_firestore_v1_document_DocumentReference_get)

### google.cloud.firestore_v1.document.DocumentReference.on_snapshot
    
    
    on_snapshot(callback: typing.Callable) -> google.cloud.firestore_v1.watch.Watch

Watch this document.

See more: [google.cloud.firestore_v1.document.DocumentReference.on_snapshot](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference#google_cloud_firestore_v1_document_DocumentReference_on_snapshot)

### google.cloud.firestore_v1.document.DocumentReference.set
    
    
    set(
        document_data: dict,
        merge: bool = False,
        retry: (
            google.api_core.retry.retry_unary.Retry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> google.cloud.firestore_v1.types.write.WriteResult

Create / replace / merge a document in the Firestore database.

See more: [google.cloud.firestore_v1.document.DocumentReference.set](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference#google_cloud_firestore_v1_document_DocumentReference_set)

### google.cloud.firestore_v1.document.DocumentReference.update
    
    
    update(
        field_updates: dict[str, typing.Any],
        option: typing.Optional[google.cloud.firestore_v1._helpers.WriteOption] = None,
        retry: (
            google.api_core.retry.retry_unary.Retry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> google.cloud.firestore_v1.types.write.WriteResult

Update an existing document in the Firestore database.

See more: [google.cloud.firestore_v1.document.DocumentReference.update](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference#google_cloud_firestore_v1_document_DocumentReference_update)

### google.cloud.firestore_v1.field_path.FieldPath.__add__
    
    
    __add__(other)

Adds `other` field path to end of this field path.

See more: [google.cloud.firestore_v1.field_path.FieldPath.**add**](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path.FieldPath#google_cloud_firestore_v1_field_path_FieldPath___add__)

### google.cloud.firestore_v1.field_path.FieldPath.document_id
    
    
    document_id() -> str

A special FieldPath value to refer to the ID of a document.

See more: [google.cloud.firestore_v1.field_path.FieldPath.document_id](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path.FieldPath#google_cloud_firestore_v1_field_path_FieldPath_document_id)

### google.cloud.firestore_v1.field_path.FieldPath.eq_or_parent
    
    
    eq_or_parent(other) -> bool

Check whether `other` is an ancestor.

See more: [google.cloud.firestore_v1.field_path.FieldPath.eq_or_parent](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path.FieldPath#google_cloud_firestore_v1_field_path_FieldPath_eq_or_parent)

### google.cloud.firestore_v1.field_path.FieldPath.from_api_repr
    
    
    from_api_repr(api_repr: str) -> google.cloud.firestore_v1.field_path.FieldPath

Factory: create a FieldPath from the string formatted per the API.

See more: [google.cloud.firestore_v1.field_path.FieldPath.from_api_repr](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path.FieldPath#google_cloud_firestore_v1_field_path_FieldPath_from_api_repr)

### google.cloud.firestore_v1.field_path.FieldPath.from_string
    
    
    from_string(path_string: str) -> google.cloud.firestore_v1.field_path.FieldPath

Factory: create a FieldPath from a unicode string representation.

See more: [google.cloud.firestore_v1.field_path.FieldPath.from_string](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path.FieldPath#google_cloud_firestore_v1_field_path_FieldPath_from_string)

### google.cloud.firestore_v1.field_path.FieldPath.lineage
    
    
    lineage() -> set["FieldPath"]

Return field paths for all parents.

See more: [google.cloud.firestore_v1.field_path.FieldPath.lineage](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path.FieldPath#google_cloud_firestore_v1_field_path_FieldPath_lineage)

### google.cloud.firestore_v1.field_path.FieldPath.to_api_repr
    
    
    to_api_repr() -> str

Render a quoted string representation of the FieldPath .

See more: [google.cloud.firestore_v1.field_path.FieldPath.to_api_repr](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path.FieldPath#google_cloud_firestore_v1_field_path_FieldPath_to_api_repr)

### google.cloud.firestore_v1.query.CollectionGroup.get_partitions
    
    
    get_partitions(
        partition_count,
        retry: retries.Retry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        read_time: Optional[datetime.datetime] = None
    ) -> Generator[QueryPartition, None, None]

Partition a query for parallelization.

See more: [google.cloud.firestore_v1.query.CollectionGroup.get_partitions](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.CollectionGroup#google_cloud_firestore_v1_query_CollectionGroup_get_partitions)

### google.cloud.firestore_v1.query.Query.avg
    
    
    avg(
        field_ref: str | FieldPath, alias: str | None = None
    ) -> Type["firestore_v1.aggregation.AggregationQuery"]

Adds an avg over the query.

See more: [google.cloud.firestore_v1.query.Query.avg](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query#google_cloud_firestore_v1_query_Query_avg)

### google.cloud.firestore_v1.query.Query.count
    
    
    count(
        alias: typing.Optional[str] = None,
    ) -> typing.Type[google.cloud.firestore_v1.aggregation.AggregationQuery]

Adds a count over the query.

See more: [google.cloud.firestore_v1.query.Query.count](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query#google_cloud_firestore_v1_query_Query_count)

### google.cloud.firestore_v1.query.Query.find_nearest
    
    
    find_nearest(
        vector_field: str,
        query_vector: Union[Vector, Sequence[float]],
        limit: int,
        distance_measure: DistanceMeasure,
        *,
        distance_result_field: Optional[str] = None,
        distance_threshold: Optional[float] = None
    ) -> Type["firestore_v1.vector_query.VectorQuery"]

Finds the closest vector embeddings to the given query vector.

See more: [google.cloud.firestore_v1.query.Query.find_nearest](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query#google_cloud_firestore_v1_query_Query_find_nearest)

### google.cloud.firestore_v1.query.Query.get
    
    
    get(
        transaction=None,
        retry: retries.Retry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> QueryResultsList[DocumentSnapshot]

Read the documents in the collection that match this query.

See more: [google.cloud.firestore_v1.query.Query.get](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query#google_cloud_firestore_v1_query_Query_get)

### google.cloud.firestore_v1.query.Query.on_snapshot
    
    
    on_snapshot(callback: typing.Callable) -> google.cloud.firestore_v1.watch.Watch

Monitor the documents in this collection that match this query.

See more: [google.cloud.firestore_v1.query.Query.on_snapshot](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query#google_cloud_firestore_v1_query_Query_on_snapshot)

### google.cloud.firestore_v1.query.Query.stream
    
    
    stream(
        transaction: transaction.Transaction | None = None,
        retry: retries.Retry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> StreamGenerator[DocumentSnapshot]

Read the documents in the collection that match this query.

See more: [google.cloud.firestore_v1.query.Query.stream](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query#google_cloud_firestore_v1_query_Query_stream)

### google.cloud.firestore_v1.query.Query.sum
    
    
    sum(
        field_ref: str | FieldPath, alias: str | None = None
    ) -> Type["firestore_v1.aggregation.AggregationQuery"]

Adds a sum over the query.

See more: [google.cloud.firestore_v1.query.Query.sum](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query#google_cloud_firestore_v1_query_Query_sum)

### google.cloud.firestore_v1.transaction.Transaction.commit
    
    
    commit(
        retry: (
            google.api_core.retry.retry_unary.Retry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> list

Commit the changes accumulated in this batch.

See more: [google.cloud.firestore_v1.transaction.Transaction.commit](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transaction.Transaction#google_cloud_firestore_v1_transaction_Transaction_commit)

### google.cloud.firestore_v1.transaction.Transaction.create
    
    
    create(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        document_data: dict[str, typing.Any],
    ) -> None

Add a "change" to this batch to create a document.

See more: [google.cloud.firestore_v1.transaction.Transaction.create](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transaction.Transaction#google_cloud_firestore_v1_transaction_Transaction_create)

### google.cloud.firestore_v1.transaction.Transaction.delete
    
    
    delete(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        option: typing.Optional[google.cloud.firestore_v1._helpers.WriteOption] = None,
    ) -> None

Add a "change" to delete a document.

See more: [google.cloud.firestore_v1.transaction.Transaction.delete](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transaction.Transaction#google_cloud_firestore_v1_transaction_Transaction_delete)

### google.cloud.firestore_v1.transaction.Transaction.get
    
    
    get(
        ref_or_query: DocumentReference | Query,
        retry: retries.Retry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> StreamGenerator[DocumentSnapshot] | Generator[DocumentSnapshot, Any, None]

Retrieve a document or a query result from the database.

See more: [google.cloud.firestore_v1.transaction.Transaction.get](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transaction.Transaction#google_cloud_firestore_v1_transaction_Transaction_get)

### google.cloud.firestore_v1.transaction.Transaction.get_all
    
    
    get_all(
        references: list,
        retry: retries.Retry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        read_time: datetime.datetime | None = None
    ) -> Generator[DocumentSnapshot, Any, None]

Retrieves multiple documents from Firestore.

See more: [google.cloud.firestore_v1.transaction.Transaction.get_all](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transaction.Transaction#google_cloud_firestore_v1_transaction_Transaction_get_all)

### google.cloud.firestore_v1.transaction.Transaction.set
    
    
    set(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        document_data: dict,
        merge: typing.Union[bool, list] = False,
    ) -> None

Add a "change" to replace a document.

See more: [google.cloud.firestore_v1.transaction.Transaction.set](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transaction.Transaction#google_cloud_firestore_v1_transaction_Transaction_set)

### google.cloud.firestore_v1.transaction.Transaction.update
    
    
    update(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        field_updates: dict[str, typing.Any],
        option: typing.Optional[google.cloud.firestore_v1._helpers.WriteOption] = None,
    ) -> None

Add a "change" to update a document.

See more: [google.cloud.firestore_v1.transaction.Transaction.update](https://cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transaction.Transaction#google_cloud_firestore_v1_transaction_Transaction_update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
