---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/summary_method/
title: Package Methods (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:37.738658+00:00
---

# Package Methods (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 

Summary of entries of Methods for backupdr.

## 

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient
    
    
    BackupDRAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.backupdr_v1.services.backup_dr.transports.base.BackupDRTransport,
                typing.Callable[
                    [...],
                    google.cloud.backupdr_v1.services.backup_dr.transports.base.BackupDRTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the backup dr async client.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_BackupDRAsyncClient)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.backup_path
    
    
    backup_path(
        project: str, location: str, backupvault: str, datasource: str, backup: str
    ) -> str

Returns a fully-qualified backup string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.backup_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_backup_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.backup_plan_association_path
    
    
    backup_plan_association_path(
        project: str, location: str, backup_plan_association: str
    ) -> str

Returns a fully-qualified backup_plan_association string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.backup_plan_association_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_backup_plan_association_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.backup_plan_path
    
    
    backup_plan_path(project: str, location: str, backup_plan: str) -> str

Returns a fully-qualified backup_plan string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.backup_plan_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_backup_plan_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.backup_plan_revision_path
    
    
    backup_plan_revision_path(
        project: str, location: str, backup_plan: str, revision: str
    ) -> str

Returns a fully-qualified backup_plan_revision string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.backup_plan_revision_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_backup_plan_revision_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.backup_vault_path
    
    
    backup_vault_path(project: str, location: str, backupvault: str) -> str

Returns a fully-qualified backup_vault string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.backup_vault_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_backup_vault_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_cancel_operation)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.cluster_path
    
    
    cluster_path(project: str, location: str, cluster: str) -> str

Returns a fully-qualified cluster string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.cluster_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_cluster_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_common_billing_account_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_common_folder_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_common_location_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_common_organization_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_common_project_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.create_backup_plan
    
    
    create_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.CreateBackupPlanRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_plan: typing.Optional[
            google.cloud.backupdr_v1.types.backupplan.BackupPlan
        ] = None,
        backup_plan_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Create a BackupPlan.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.create_backup_plan](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_create_backup_plan)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.create_backup_plan_association
    
    
    create_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.CreateBackupPlanAssociationRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_plan_association: typing.Optional[
            google.cloud.backupdr_v1.types.backupplanassociation.BackupPlanAssociation
        ] = None,
        backup_plan_association_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Create a BackupPlanAssociation.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.create_backup_plan_association](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_create_backup_plan_association)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.create_backup_vault
    
    
    create_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.CreateBackupVaultRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_vault: typing.Optional[
            google.cloud.backupdr_v1.types.backupvault.BackupVault
        ] = None,
        backup_vault_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new BackupVault in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.create_backup_vault](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_create_backup_vault)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.create_management_server
    
    
    create_management_server(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupdr.CreateManagementServerRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        management_server: typing.Optional[
            google.cloud.backupdr_v1.types.backupdr.ManagementServer
        ] = None,
        management_server_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new ManagementServer in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.create_management_server](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_create_management_server)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, ring: str, key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.crypto_key_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_crypto_key_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.crypto_key_version_path
    
    
    crypto_key_version_path(
        project: str, location: str, key_ring: str, crypto_key: str, crypto_key_version: str
    ) -> str

Returns a fully-qualified crypto_key_version string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.crypto_key_version_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_crypto_key_version_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.data_source_path
    
    
    data_source_path(
        project: str, location: str, backupvault: str, datasource: str
    ) -> str

Returns a fully-qualified data_source string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.data_source_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_data_source_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.data_source_reference_path
    
    
    data_source_reference_path(
        project: str, location: str, data_source_reference: str
    ) -> str

Returns a fully-qualified data_source_reference string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.data_source_reference_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_data_source_reference_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.delete_backup
    
    
    delete_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.DeleteBackupRequest, dict
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

Deletes a Backup.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.delete_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_delete_backup)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.delete_backup_plan
    
    
    delete_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.DeleteBackupPlanRequest, dict
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

Deletes a single BackupPlan.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.delete_backup_plan](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_delete_backup_plan)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.delete_backup_plan_association
    
    
    delete_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.DeleteBackupPlanAssociationRequest,
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

Deletes a single BackupPlanAssociation.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.delete_backup_plan_association](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_delete_backup_plan_association)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.delete_backup_vault
    
    
    delete_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.DeleteBackupVaultRequest, dict
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

Deletes a BackupVault.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.delete_backup_vault](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_delete_backup_vault)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.delete_management_server
    
    
    delete_management_server(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupdr.DeleteManagementServerRequest, dict
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

Deletes a single ManagementServer.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.delete_management_server](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_delete_management_server)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.delete_operation
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_delete_operation)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.fetch_backup_plan_associations_for_resource_type
    
    
    fetch_backup_plan_associations_for_resource_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypeAsyncPager
    )

List BackupPlanAssociations for a given resource type.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.fetch_backup_plan_associations_for_resource_type](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_fetch_backup_plan_associations_for_resource_type)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.fetch_backups_for_resource_type
    
    
    fetch_backups_for_resource_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypeAsyncPager
    )

Fetch Backups for a given resource type.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.fetch_backups_for_resource_type](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_fetch_backups_for_resource_type)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.fetch_data_source_references_for_resource_type
    
    
    fetch_data_source_references_for_resource_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.backupdr_v1.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypeAsyncPager
    )

Fetch DataSourceReferences for a given project, location and resource type.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.fetch_data_source_references_for_resource_type](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_fetch_data_source_references_for_resource_type)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.fetch_usable_backup_vaults
    
    
    fetch_usable_backup_vaults(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.FetchUsableBackupVaultsRequest,
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
        google.cloud.backupdr_v1.services.backup_dr.pagers.FetchUsableBackupVaultsAsyncPager
    )

FetchUsableBackupVaults lists usable BackupVaults in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.fetch_usable_backup_vaults](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_fetch_usable_backup_vaults)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_from_service_account_file)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_from_service_account_info)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_from_service_account_json)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_backup
    
    
    get_backup(
        request: typing.Optional[
            typing.Union[google.cloud.backupdr_v1.types.backupvault.GetBackupRequest, dict]
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
    ) -> google.cloud.backupdr_v1.types.backupvault.Backup

Gets details of a Backup.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_get_backup)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_backup_plan
    
    
    get_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.GetBackupPlanRequest, dict
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
    ) -> google.cloud.backupdr_v1.types.backupplan.BackupPlan

Gets details of a single BackupPlan.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_backup_plan](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_get_backup_plan)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_backup_plan_association
    
    
    get_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.GetBackupPlanAssociationRequest,
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
    ) -> google.cloud.backupdr_v1.types.backupplanassociation.BackupPlanAssociation

Gets details of a single BackupPlanAssociation.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_backup_plan_association](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_get_backup_plan_association)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_backup_plan_revision
    
    
    get_backup_plan_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.GetBackupPlanRevisionRequest, dict
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
    ) -> google.cloud.backupdr_v1.types.backupplan.BackupPlanRevision

Gets details of a single BackupPlanRevision.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_backup_plan_revision](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_get_backup_plan_revision)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_backup_vault
    
    
    get_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.GetBackupVaultRequest, dict
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
    ) -> google.cloud.backupdr_v1.types.backupvault.BackupVault

Gets details of a BackupVault.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_backup_vault](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_get_backup_vault)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_data_source
    
    
    get_data_source(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.GetDataSourceRequest, dict
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
    ) -> google.cloud.backupdr_v1.types.backupvault.DataSource

Gets details of a DataSource.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_data_source](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_get_data_source)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_data_source_reference
    
    
    get_data_source_reference(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.datasourcereference.GetDataSourceReferenceRequest,
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
    ) -> google.cloud.backupdr_v1.types.datasourcereference.DataSourceReference

Gets details of a single DataSourceReference.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_data_source_reference](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_get_data_source_reference)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_get_iam_policy)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_location
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_location](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_get_location)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_management_server
    
    
    get_management_server(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupdr.GetManagementServerRequest, dict
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
    ) -> google.cloud.backupdr_v1.types.backupdr.ManagementServer

Gets details of a single ManagementServer.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_management_server](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_get_management_server)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_operation
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_get_operation)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.backupdr_v1.services.backup_dr.transports.base.BackupDRTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_get_transport_class)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.initialize_service
    
    
    initialize_service(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupdr.InitializeServiceRequest, dict
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

Initializes the service related config for a project.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.initialize_service](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_initialize_service)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.instance_path
    
    
    instance_path(project: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.instance_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_instance_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_backup_plan_associations
    
    
    list_backup_plan_associations(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.ListBackupPlanAssociationsRequest,
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
        google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanAssociationsAsyncPager
    )

Lists BackupPlanAssociations in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_backup_plan_associations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_list_backup_plan_associations)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_backup_plan_revisions
    
    
    list_backup_plan_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.ListBackupPlanRevisionsRequest,
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
        google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanRevisionsAsyncPager
    )

Lists BackupPlanRevisions in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_backup_plan_revisions](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_list_backup_plan_revisions)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_backup_plans
    
    
    list_backup_plans(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.ListBackupPlansRequest, dict
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlansAsyncPager

Lists BackupPlans in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_backup_plans](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_list_backup_plans)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_backup_vaults
    
    
    list_backup_vaults(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.ListBackupVaultsRequest, dict
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupVaultsAsyncPager

Lists BackupVaults in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_backup_vaults](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_list_backup_vaults)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_backups
    
    
    list_backups(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.ListBackupsRequest, dict
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupsAsyncPager

Lists Backups in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_backups](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_list_backups)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_data_source_references
    
    
    list_data_source_references(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.datasourcereference.ListDataSourceReferencesRequest,
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
        google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourceReferencesAsyncPager
    )

Lists DataSourceReferences for a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_data_source_references](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_list_data_source_references)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_data_sources
    
    
    list_data_sources(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.ListDataSourcesRequest, dict
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourcesAsyncPager

Lists DataSources in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_data_sources](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_list_data_sources)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_locations
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_list_locations)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_management_servers
    
    
    list_management_servers(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupdr.ListManagementServersRequest, dict
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListManagementServersAsyncPager

Lists ManagementServers in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_management_servers](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_list_management_servers)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_operations
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_list_operations)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.management_server_path
    
    
    management_server_path(project: str, location: str, managementserver: str) -> str

Returns a fully-qualified management_server string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.management_server_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_management_server_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_backup_path
    
    
    parse_backup_path(path: str) -> typing.Dict[str, str]

Parses a backup path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_backup_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_backup_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_backup_plan_association_path
    
    
    parse_backup_plan_association_path(path: str) -> typing.Dict[str, str]

Parses a backup_plan_association path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_backup_plan_association_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_backup_plan_association_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_backup_plan_path
    
    
    parse_backup_plan_path(path: str) -> typing.Dict[str, str]

Parses a backup_plan path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_backup_plan_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_backup_plan_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_backup_plan_revision_path
    
    
    parse_backup_plan_revision_path(path: str) -> typing.Dict[str, str]

Parses a backup_plan_revision path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_backup_plan_revision_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_backup_plan_revision_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_backup_vault_path
    
    
    parse_backup_vault_path(path: str) -> typing.Dict[str, str]

Parses a backup_vault path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_backup_vault_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_backup_vault_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_cluster_path
    
    
    parse_cluster_path(path: str) -> typing.Dict[str, str]

Parses a cluster path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_cluster_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_cluster_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_common_billing_account_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_common_folder_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_common_location_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_common_organization_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_common_project_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_crypto_key_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_crypto_key_version_path
    
    
    parse_crypto_key_version_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key_version path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_crypto_key_version_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_crypto_key_version_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_data_source_path
    
    
    parse_data_source_path(path: str) -> typing.Dict[str, str]

Parses a data_source path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_data_source_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_data_source_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_data_source_reference_path
    
    
    parse_data_source_reference_path(path: str) -> typing.Dict[str, str]

Parses a data_source_reference path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_data_source_reference_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_data_source_reference_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_instance_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_instance_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_management_server_path
    
    
    parse_management_server_path(path: str) -> typing.Dict[str, str]

Parses a management_server path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_management_server_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_management_server_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_storage_pool_path
    
    
    parse_storage_pool_path(path: str) -> typing.Dict[str, str]

Parses a storage_pool path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.parse_storage_pool_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_parse_storage_pool_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.restore_backup
    
    
    restore_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.RestoreBackupRequest, dict
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

Restore from a Backup.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.restore_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_restore_backup)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_set_iam_policy)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.storage_pool_path
    
    
    storage_pool_path(project: str, zone: str, storage_pool: str) -> str

Returns a fully-qualified storage_pool string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.storage_pool_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_storage_pool_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_test_iam_permissions)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.trigger_backup
    
    
    trigger_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.TriggerBackupRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        rule_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Triggers a new Backup.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.trigger_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_trigger_backup)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.update_backup
    
    
    update_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.UpdateBackupRequest, dict
            ]
        ] = None,
        *,
        backup: typing.Optional[google.cloud.backupdr_v1.types.backupvault.Backup] = None,
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

Updates the settings of a Backup.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.update_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_update_backup)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.update_backup_plan
    
    
    update_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.UpdateBackupPlanRequest, dict
            ]
        ] = None,
        *,
        backup_plan: typing.Optional[
            google.cloud.backupdr_v1.types.backupplan.BackupPlan
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

Update a BackupPlan.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.update_backup_plan](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_update_backup_plan)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.update_backup_plan_association
    
    
    update_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.UpdateBackupPlanAssociationRequest,
                dict,
            ]
        ] = None,
        *,
        backup_plan_association: typing.Optional[
            google.cloud.backupdr_v1.types.backupplanassociation.BackupPlanAssociation
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

Update a BackupPlanAssociation.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.update_backup_plan_association](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_update_backup_plan_association)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.update_backup_vault
    
    
    update_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.UpdateBackupVaultRequest, dict
            ]
        ] = None,
        *,
        backup_vault: typing.Optional[
            google.cloud.backupdr_v1.types.backupvault.BackupVault
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

Updates the settings of a BackupVault.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.update_backup_vault](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_update_backup_vault)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.update_data_source
    
    
    update_data_source(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.UpdateDataSourceRequest, dict
            ]
        ] = None,
        *,
        data_source: typing.Optional[
            google.cloud.backupdr_v1.types.backupvault.DataSource
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

Updates the settings of a DataSource.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient.update_data_source](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRAsyncClient_update_data_source)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient
    
    
    BackupDRClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.backupdr_v1.services.backup_dr.transports.base.BackupDRTransport,
                typing.Callable[
                    [...],
                    google.cloud.backupdr_v1.services.backup_dr.transports.base.BackupDRTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the backup dr client.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_BackupDRClient)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.**exit**](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient___exit__)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.backup_path
    
    
    backup_path(
        project: str, location: str, backupvault: str, datasource: str, backup: str
    ) -> str

Returns a fully-qualified backup string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.backup_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_backup_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.backup_plan_association_path
    
    
    backup_plan_association_path(
        project: str, location: str, backup_plan_association: str
    ) -> str

Returns a fully-qualified backup_plan_association string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.backup_plan_association_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_backup_plan_association_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.backup_plan_path
    
    
    backup_plan_path(project: str, location: str, backup_plan: str) -> str

Returns a fully-qualified backup_plan string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.backup_plan_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_backup_plan_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.backup_plan_revision_path
    
    
    backup_plan_revision_path(
        project: str, location: str, backup_plan: str, revision: str
    ) -> str

Returns a fully-qualified backup_plan_revision string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.backup_plan_revision_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_backup_plan_revision_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.backup_vault_path
    
    
    backup_vault_path(project: str, location: str, backupvault: str) -> str

Returns a fully-qualified backup_vault string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.backup_vault_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_backup_vault_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.cancel_operation
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.cancel_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_cancel_operation)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.cluster_path
    
    
    cluster_path(project: str, location: str, cluster: str) -> str

Returns a fully-qualified cluster string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.cluster_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_cluster_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_common_billing_account_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.common_folder_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_common_folder_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.common_location_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_common_location_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.common_organization_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_common_organization_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.common_project_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_common_project_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.create_backup_plan
    
    
    create_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.CreateBackupPlanRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_plan: typing.Optional[
            google.cloud.backupdr_v1.types.backupplan.BackupPlan
        ] = None,
        backup_plan_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Create a BackupPlan.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.create_backup_plan](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_create_backup_plan)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.create_backup_plan_association
    
    
    create_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.CreateBackupPlanAssociationRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_plan_association: typing.Optional[
            google.cloud.backupdr_v1.types.backupplanassociation.BackupPlanAssociation
        ] = None,
        backup_plan_association_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Create a BackupPlanAssociation.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.create_backup_plan_association](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_create_backup_plan_association)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.create_backup_vault
    
    
    create_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.CreateBackupVaultRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_vault: typing.Optional[
            google.cloud.backupdr_v1.types.backupvault.BackupVault
        ] = None,
        backup_vault_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new BackupVault in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.create_backup_vault](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_create_backup_vault)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.create_management_server
    
    
    create_management_server(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupdr.CreateManagementServerRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        management_server: typing.Optional[
            google.cloud.backupdr_v1.types.backupdr.ManagementServer
        ] = None,
        management_server_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new ManagementServer in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.create_management_server](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_create_management_server)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, ring: str, key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.crypto_key_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_crypto_key_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.crypto_key_version_path
    
    
    crypto_key_version_path(
        project: str, location: str, key_ring: str, crypto_key: str, crypto_key_version: str
    ) -> str

Returns a fully-qualified crypto_key_version string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.crypto_key_version_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_crypto_key_version_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.data_source_path
    
    
    data_source_path(
        project: str, location: str, backupvault: str, datasource: str
    ) -> str

Returns a fully-qualified data_source string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.data_source_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_data_source_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.data_source_reference_path
    
    
    data_source_reference_path(
        project: str, location: str, data_source_reference: str
    ) -> str

Returns a fully-qualified data_source_reference string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.data_source_reference_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_data_source_reference_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.delete_backup
    
    
    delete_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.DeleteBackupRequest, dict
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

Deletes a Backup.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.delete_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_delete_backup)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.delete_backup_plan
    
    
    delete_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.DeleteBackupPlanRequest, dict
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

Deletes a single BackupPlan.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.delete_backup_plan](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_delete_backup_plan)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.delete_backup_plan_association
    
    
    delete_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.DeleteBackupPlanAssociationRequest,
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

Deletes a single BackupPlanAssociation.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.delete_backup_plan_association](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_delete_backup_plan_association)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.delete_backup_vault
    
    
    delete_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.DeleteBackupVaultRequest, dict
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

Deletes a BackupVault.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.delete_backup_vault](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_delete_backup_vault)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.delete_management_server
    
    
    delete_management_server(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupdr.DeleteManagementServerRequest, dict
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

Deletes a single ManagementServer.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.delete_management_server](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_delete_management_server)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.delete_operation
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.delete_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_delete_operation)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.fetch_backup_plan_associations_for_resource_type
    
    
    fetch_backup_plan_associations_for_resource_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypePager
    )

List BackupPlanAssociations for a given resource type.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.fetch_backup_plan_associations_for_resource_type](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_fetch_backup_plan_associations_for_resource_type)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.fetch_backups_for_resource_type
    
    
    fetch_backups_for_resource_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypePager
    )

Fetch Backups for a given resource type.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.fetch_backups_for_resource_type](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_fetch_backups_for_resource_type)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.fetch_data_source_references_for_resource_type
    
    
    fetch_data_source_references_for_resource_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.backupdr_v1.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypePager
    )

Fetch DataSourceReferences for a given project, location and resource type.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.fetch_data_source_references_for_resource_type](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_fetch_data_source_references_for_resource_type)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.fetch_usable_backup_vaults
    
    
    fetch_usable_backup_vaults(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.FetchUsableBackupVaultsRequest,
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.FetchUsableBackupVaultsPager

FetchUsableBackupVaults lists usable BackupVaults in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.fetch_usable_backup_vaults](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_fetch_usable_backup_vaults)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.from_service_account_file](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_from_service_account_file)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.from_service_account_info](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_from_service_account_info)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.from_service_account_json](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_from_service_account_json)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_backup
    
    
    get_backup(
        request: typing.Optional[
            typing.Union[google.cloud.backupdr_v1.types.backupvault.GetBackupRequest, dict]
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
    ) -> google.cloud.backupdr_v1.types.backupvault.Backup

Gets details of a Backup.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_backup)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_backup_plan
    
    
    get_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.GetBackupPlanRequest, dict
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
    ) -> google.cloud.backupdr_v1.types.backupplan.BackupPlan

Gets details of a single BackupPlan.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_backup_plan](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_backup_plan)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_backup_plan_association
    
    
    get_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.GetBackupPlanAssociationRequest,
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
    ) -> google.cloud.backupdr_v1.types.backupplanassociation.BackupPlanAssociation

Gets details of a single BackupPlanAssociation.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_backup_plan_association](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_backup_plan_association)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_backup_plan_revision
    
    
    get_backup_plan_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.GetBackupPlanRevisionRequest, dict
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
    ) -> google.cloud.backupdr_v1.types.backupplan.BackupPlanRevision

Gets details of a single BackupPlanRevision.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_backup_plan_revision](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_backup_plan_revision)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_backup_vault
    
    
    get_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.GetBackupVaultRequest, dict
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
    ) -> google.cloud.backupdr_v1.types.backupvault.BackupVault

Gets details of a BackupVault.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_backup_vault](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_backup_vault)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_data_source
    
    
    get_data_source(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.GetDataSourceRequest, dict
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
    ) -> google.cloud.backupdr_v1.types.backupvault.DataSource

Gets details of a DataSource.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_data_source](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_data_source)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_data_source_reference
    
    
    get_data_source_reference(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.datasourcereference.GetDataSourceReferenceRequest,
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
    ) -> google.cloud.backupdr_v1.types.datasourcereference.DataSourceReference

Gets details of a single DataSourceReference.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_data_source_reference](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_data_source_reference)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_iam_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_iam_policy)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_location
    
    
    get_location(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.GetLocationRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.Location

Gets information about a location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_location](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_location)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_management_server
    
    
    get_management_server(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupdr.GetManagementServerRequest, dict
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
    ) -> google.cloud.backupdr_v1.types.backupdr.ManagementServer

Gets details of a single ManagementServer.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_management_server](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_management_server)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_mtls_endpoint_and_cert_source)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_operation
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.get_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_get_operation)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.initialize_service
    
    
    initialize_service(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupdr.InitializeServiceRequest, dict
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

Initializes the service related config for a project.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.initialize_service](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_initialize_service)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.instance_path
    
    
    instance_path(project: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.instance_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_instance_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_backup_plan_associations
    
    
    list_backup_plan_associations(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.ListBackupPlanAssociationsRequest,
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanAssociationsPager

Lists BackupPlanAssociations in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_backup_plan_associations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_backup_plan_associations)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_backup_plan_revisions
    
    
    list_backup_plan_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.ListBackupPlanRevisionsRequest,
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanRevisionsPager

Lists BackupPlanRevisions in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_backup_plan_revisions](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_backup_plan_revisions)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_backup_plans
    
    
    list_backup_plans(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.ListBackupPlansRequest, dict
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlansPager

Lists BackupPlans in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_backup_plans](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_backup_plans)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_backup_vaults
    
    
    list_backup_vaults(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.ListBackupVaultsRequest, dict
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupVaultsPager

Lists BackupVaults in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_backup_vaults](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_backup_vaults)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_backups
    
    
    list_backups(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.ListBackupsRequest, dict
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupsPager

Lists Backups in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_backups](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_backups)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_data_source_references
    
    
    list_data_source_references(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.datasourcereference.ListDataSourceReferencesRequest,
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourceReferencesPager

Lists DataSourceReferences for a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_data_source_references](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_data_source_references)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_data_sources
    
    
    list_data_sources(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.ListDataSourcesRequest, dict
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourcesPager

Lists DataSources in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_data_sources](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_data_sources)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_locations
    
    
    list_locations(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.ListLocationsRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.ListLocationsResponse

Lists information about the supported locations for this service.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_locations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_locations)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_management_servers
    
    
    list_management_servers(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupdr.ListManagementServersRequest, dict
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
    ) -> google.cloud.backupdr_v1.services.backup_dr.pagers.ListManagementServersPager

Lists ManagementServers in a given project and location.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_management_servers](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_management_servers)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_operations
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.list_operations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_list_operations)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.management_server_path
    
    
    management_server_path(project: str, location: str, managementserver: str) -> str

Returns a fully-qualified management_server string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.management_server_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_management_server_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_backup_path
    
    
    parse_backup_path(path: str) -> typing.Dict[str, str]

Parses a backup path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_backup_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_backup_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_backup_plan_association_path
    
    
    parse_backup_plan_association_path(path: str) -> typing.Dict[str, str]

Parses a backup_plan_association path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_backup_plan_association_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_backup_plan_association_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_backup_plan_path
    
    
    parse_backup_plan_path(path: str) -> typing.Dict[str, str]

Parses a backup_plan path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_backup_plan_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_backup_plan_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_backup_plan_revision_path
    
    
    parse_backup_plan_revision_path(path: str) -> typing.Dict[str, str]

Parses a backup_plan_revision path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_backup_plan_revision_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_backup_plan_revision_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_backup_vault_path
    
    
    parse_backup_vault_path(path: str) -> typing.Dict[str, str]

Parses a backup_vault path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_backup_vault_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_backup_vault_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_cluster_path
    
    
    parse_cluster_path(path: str) -> typing.Dict[str, str]

Parses a cluster path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_cluster_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_cluster_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_common_billing_account_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_common_folder_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_common_location_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_common_organization_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_common_project_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_crypto_key_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_crypto_key_version_path
    
    
    parse_crypto_key_version_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key_version path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_crypto_key_version_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_crypto_key_version_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_data_source_path
    
    
    parse_data_source_path(path: str) -> typing.Dict[str, str]

Parses a data_source path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_data_source_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_data_source_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_data_source_reference_path
    
    
    parse_data_source_reference_path(path: str) -> typing.Dict[str, str]

Parses a data_source_reference path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_data_source_reference_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_data_source_reference_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_instance_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_instance_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_management_server_path
    
    
    parse_management_server_path(path: str) -> typing.Dict[str, str]

Parses a management_server path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_management_server_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_management_server_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_storage_pool_path
    
    
    parse_storage_pool_path(path: str) -> typing.Dict[str, str]

Parses a storage_pool path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.parse_storage_pool_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_parse_storage_pool_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.restore_backup
    
    
    restore_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.RestoreBackupRequest, dict
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

Restore from a Backup.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.restore_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_restore_backup)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.set_iam_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_set_iam_policy)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.storage_pool_path
    
    
    storage_pool_path(project: str, zone: str, storage_pool: str) -> str

Returns a fully-qualified storage_pool string.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.storage_pool_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_storage_pool_path)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_test_iam_permissions)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.trigger_backup
    
    
    trigger_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.TriggerBackupRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        rule_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Triggers a new Backup.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.trigger_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_trigger_backup)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.update_backup
    
    
    update_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.UpdateBackupRequest, dict
            ]
        ] = None,
        *,
        backup: typing.Optional[google.cloud.backupdr_v1.types.backupvault.Backup] = None,
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

Updates the settings of a Backup.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.update_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_update_backup)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.update_backup_plan
    
    
    update_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplan.UpdateBackupPlanRequest, dict
            ]
        ] = None,
        *,
        backup_plan: typing.Optional[
            google.cloud.backupdr_v1.types.backupplan.BackupPlan
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

Update a BackupPlan.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.update_backup_plan](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_update_backup_plan)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.update_backup_plan_association
    
    
    update_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupplanassociation.UpdateBackupPlanAssociationRequest,
                dict,
            ]
        ] = None,
        *,
        backup_plan_association: typing.Optional[
            google.cloud.backupdr_v1.types.backupplanassociation.BackupPlanAssociation
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

Update a BackupPlanAssociation.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.update_backup_plan_association](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_update_backup_plan_association)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.update_backup_vault
    
    
    update_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.UpdateBackupVaultRequest, dict
            ]
        ] = None,
        *,
        backup_vault: typing.Optional[
            google.cloud.backupdr_v1.types.backupvault.BackupVault
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

Updates the settings of a BackupVault.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.update_backup_vault](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_update_backup_vault)

### google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.update_data_source
    
    
    update_data_source(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.backupvault.UpdateDataSourceRequest, dict
            ]
        ] = None,
        *,
        data_source: typing.Optional[
            google.cloud.backupdr_v1.types.backupvault.DataSource
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

Updates the settings of a DataSource.

See more: [google.cloud.backupdr_v1.services.backup_dr.BackupDRClient.update_data_source](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1_services_backup_dr_BackupDRClient_update_data_source)

### google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypeAsyncPager
    
    
    FetchBackupPlanAssociationsForResourceTypeAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
        response: google.cloud.backupdr_v1.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypeAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypeAsyncPager#google_cloud_backupdr_v1_services_backup_dr_pagers_FetchBackupPlanAssociationsForResourceTypeAsyncPager_FetchBackupPlanAssociationsForResourceTypeAsyncPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypePager
    
    
    FetchBackupPlanAssociationsForResourceTypePager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
        ],
        request: google.cloud.backupdr_v1.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
        response: google.cloud.backupdr_v1.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypePager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypePager#google_cloud_backupdr_v1_services_backup_dr_pagers_FetchBackupPlanAssociationsForResourceTypePager_FetchBackupPlanAssociationsForResourceTypePager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypeAsyncPager
    
    
    FetchBackupsForResourceTypeAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeRequest,
        response: google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypeAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypeAsyncPager#google_cloud_backupdr_v1_services_backup_dr_pagers_FetchBackupsForResourceTypeAsyncPager_FetchBackupsForResourceTypeAsyncPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypePager
    
    
    FetchBackupsForResourceTypePager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeResponse,
        ],
        request: google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeRequest,
        response: google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypePager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypePager#google_cloud_backupdr_v1_services_backup_dr_pagers_FetchBackupsForResourceTypePager_FetchBackupsForResourceTypePager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypeAsyncPager
    
    
    FetchDataSourceReferencesForResourceTypeAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.datasourcereference.FetchDataSourceReferencesForResourceTypeResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
        response: google.cloud.backupdr_v1.types.datasourcereference.FetchDataSourceReferencesForResourceTypeResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypeAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypeAsyncPager#google_cloud_backupdr_v1_services_backup_dr_pagers_FetchDataSourceReferencesForResourceTypeAsyncPager_FetchDataSourceReferencesForResourceTypeAsyncPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypePager
    
    
    FetchDataSourceReferencesForResourceTypePager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1.types.datasourcereference.FetchDataSourceReferencesForResourceTypeResponse,
        ],
        request: google.cloud.backupdr_v1.types.datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
        response: google.cloud.backupdr_v1.types.datasourcereference.FetchDataSourceReferencesForResourceTypeResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypePager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypePager#google_cloud_backupdr_v1_services_backup_dr_pagers_FetchDataSourceReferencesForResourceTypePager_FetchDataSourceReferencesForResourceTypePager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.FetchUsableBackupVaultsAsyncPager
    
    
    FetchUsableBackupVaultsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupvault.FetchUsableBackupVaultsResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupvault.FetchUsableBackupVaultsRequest,
        response: google.cloud.backupdr_v1.types.backupvault.FetchUsableBackupVaultsResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.FetchUsableBackupVaultsAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchUsableBackupVaultsAsyncPager#google_cloud_backupdr_v1_services_backup_dr_pagers_FetchUsableBackupVaultsAsyncPager_FetchUsableBackupVaultsAsyncPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.FetchUsableBackupVaultsPager
    
    
    FetchUsableBackupVaultsPager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1.types.backupvault.FetchUsableBackupVaultsResponse,
        ],
        request: google.cloud.backupdr_v1.types.backupvault.FetchUsableBackupVaultsRequest,
        response: google.cloud.backupdr_v1.types.backupvault.FetchUsableBackupVaultsResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.FetchUsableBackupVaultsPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchUsableBackupVaultsPager#google_cloud_backupdr_v1_services_backup_dr_pagers_FetchUsableBackupVaultsPager_FetchUsableBackupVaultsPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanAssociationsAsyncPager
    
    
    ListBackupPlanAssociationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupplanassociation.ListBackupPlanAssociationsResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupplanassociation.ListBackupPlanAssociationsRequest,
        response: google.cloud.backupdr_v1.types.backupplanassociation.ListBackupPlanAssociationsResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanAssociationsAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanAssociationsAsyncPager#google_cloud_backupdr_v1_services_backup_dr_pagers_ListBackupPlanAssociationsAsyncPager_ListBackupPlanAssociationsAsyncPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanAssociationsPager
    
    
    ListBackupPlanAssociationsPager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1.types.backupplanassociation.ListBackupPlanAssociationsResponse,
        ],
        request: google.cloud.backupdr_v1.types.backupplanassociation.ListBackupPlanAssociationsRequest,
        response: google.cloud.backupdr_v1.types.backupplanassociation.ListBackupPlanAssociationsResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanAssociationsPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanAssociationsPager#google_cloud_backupdr_v1_services_backup_dr_pagers_ListBackupPlanAssociationsPager_ListBackupPlanAssociationsPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanRevisionsAsyncPager
    
    
    ListBackupPlanRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupplan.ListBackupPlanRevisionsResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupplan.ListBackupPlanRevisionsRequest,
        response: google.cloud.backupdr_v1.types.backupplan.ListBackupPlanRevisionsResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanRevisionsAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanRevisionsAsyncPager#google_cloud_backupdr_v1_services_backup_dr_pagers_ListBackupPlanRevisionsAsyncPager_ListBackupPlanRevisionsAsyncPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanRevisionsPager
    
    
    ListBackupPlanRevisionsPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1.types.backupplan.ListBackupPlanRevisionsResponse
        ],
        request: google.cloud.backupdr_v1.types.backupplan.ListBackupPlanRevisionsRequest,
        response: google.cloud.backupdr_v1.types.backupplan.ListBackupPlanRevisionsResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanRevisionsPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanRevisionsPager#google_cloud_backupdr_v1_services_backup_dr_pagers_ListBackupPlanRevisionsPager_ListBackupPlanRevisionsPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlansAsyncPager
    
    
    ListBackupPlansAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupplan.ListBackupPlansResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupplan.ListBackupPlansRequest,
        response: google.cloud.backupdr_v1.types.backupplan.ListBackupPlansResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlansAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlansAsyncPager#google_cloud_backupdr_v1_services_backup_dr_pagers_ListBackupPlansAsyncPager_ListBackupPlansAsyncPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlansPager
    
    
    ListBackupPlansPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1.types.backupplan.ListBackupPlansResponse
        ],
        request: google.cloud.backupdr_v1.types.backupplan.ListBackupPlansRequest,
        response: google.cloud.backupdr_v1.types.backupplan.ListBackupPlansResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlansPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlansPager#google_cloud_backupdr_v1_services_backup_dr_pagers_ListBackupPlansPager_ListBackupPlansPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupVaultsAsyncPager
    
    
    ListBackupVaultsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupvault.ListBackupVaultsResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupvault.ListBackupVaultsRequest,
        response: google.cloud.backupdr_v1.types.backupvault.ListBackupVaultsResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupVaultsAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupVaultsAsyncPager#google_cloud_backupdr_v1_services_backup_dr_pagers_ListBackupVaultsAsyncPager_ListBackupVaultsAsyncPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupVaultsPager
    
    
    ListBackupVaultsPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1.types.backupvault.ListBackupVaultsResponse
        ],
        request: google.cloud.backupdr_v1.types.backupvault.ListBackupVaultsRequest,
        response: google.cloud.backupdr_v1.types.backupvault.ListBackupVaultsResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupVaultsPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupVaultsPager#google_cloud_backupdr_v1_services_backup_dr_pagers_ListBackupVaultsPager_ListBackupVaultsPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupsAsyncPager
    
    
    ListBackupsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupvault.ListBackupsResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupvault.ListBackupsRequest,
        response: google.cloud.backupdr_v1.types.backupvault.ListBackupsResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupsAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupsAsyncPager#google_cloud_backupdr_v1_services_backup_dr_pagers_ListBackupsAsyncPager_ListBackupsAsyncPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupsPager
    
    
    ListBackupsPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1.types.backupvault.ListBackupsResponse
        ],
        request: google.cloud.backupdr_v1.types.backupvault.ListBackupsRequest,
        response: google.cloud.backupdr_v1.types.backupvault.ListBackupsResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupsPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupsPager#google_cloud_backupdr_v1_services_backup_dr_pagers_ListBackupsPager_ListBackupsPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourceReferencesAsyncPager
    
    
    ListDataSourceReferencesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.datasourcereference.ListDataSourceReferencesResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.datasourcereference.ListDataSourceReferencesRequest,
        response: google.cloud.backupdr_v1.types.datasourcereference.ListDataSourceReferencesResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourceReferencesAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourceReferencesAsyncPager#google_cloud_backupdr_v1_services_backup_dr_pagers_ListDataSourceReferencesAsyncPager_ListDataSourceReferencesAsyncPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourceReferencesPager
    
    
    ListDataSourceReferencesPager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1.types.datasourcereference.ListDataSourceReferencesResponse,
        ],
        request: google.cloud.backupdr_v1.types.datasourcereference.ListDataSourceReferencesRequest,
        response: google.cloud.backupdr_v1.types.datasourcereference.ListDataSourceReferencesResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourceReferencesPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourceReferencesPager#google_cloud_backupdr_v1_services_backup_dr_pagers_ListDataSourceReferencesPager_ListDataSourceReferencesPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourcesAsyncPager
    
    
    ListDataSourcesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupvault.ListDataSourcesResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupvault.ListDataSourcesRequest,
        response: google.cloud.backupdr_v1.types.backupvault.ListDataSourcesResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourcesAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourcesAsyncPager#google_cloud_backupdr_v1_services_backup_dr_pagers_ListDataSourcesAsyncPager_ListDataSourcesAsyncPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourcesPager
    
    
    ListDataSourcesPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1.types.backupvault.ListDataSourcesResponse
        ],
        request: google.cloud.backupdr_v1.types.backupvault.ListDataSourcesRequest,
        response: google.cloud.backupdr_v1.types.backupvault.ListDataSourcesResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourcesPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourcesPager#google_cloud_backupdr_v1_services_backup_dr_pagers_ListDataSourcesPager_ListDataSourcesPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.ListManagementServersAsyncPager
    
    
    ListManagementServersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupdr.ListManagementServersResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupdr.ListManagementServersRequest,
        response: google.cloud.backupdr_v1.types.backupdr.ListManagementServersResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.ListManagementServersAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListManagementServersAsyncPager#google_cloud_backupdr_v1_services_backup_dr_pagers_ListManagementServersAsyncPager_ListManagementServersAsyncPager)

### google.cloud.backupdr_v1.services.backup_dr.pagers.ListManagementServersPager
    
    
    ListManagementServersPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1.types.backupdr.ListManagementServersResponse
        ],
        request: google.cloud.backupdr_v1.types.backupdr.ListManagementServersRequest,
        response: google.cloud.backupdr_v1.types.backupdr.ListManagementServersResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr.pagers.ListManagementServersPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListManagementServersPager#google_cloud_backupdr_v1_services_backup_dr_pagers_ListManagementServersPager_ListManagementServersPager)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient
    
    
    BackupDrProtectionSummaryAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.backupdr_v1.services.backup_dr_protection_summary.transports.base.BackupDrProtectionSummaryTransport,
                typing.Callable[
                    [...],
                    google.cloud.backupdr_v1.services.backup_dr_protection_summary.transports.base.BackupDrProtectionSummaryTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the backup dr protection summary async client.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_BackupDrProtectionSummaryAsyncClient)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_cancel_operation)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_common_billing_account_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_common_folder_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_common_location_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_common_organization_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_common_project_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.delete_operation
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_delete_operation)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_from_service_account_file)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_from_service_account_info)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_from_service_account_json)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_get_iam_policy)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_location
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_location](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_get_location)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_operation
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_get_operation)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.backupdr_v1.services.backup_dr_protection_summary.transports.base.BackupDrProtectionSummaryTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_get_transport_class)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.list_locations
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_list_locations)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.list_operations
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_list_operations)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.list_resource_backup_configs
    
    
    list_resource_backup_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.protection_summary.ListResourceBackupConfigsRequest,
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
        google.cloud.backupdr_v1.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsAsyncPager
    )

Lists ResourceBackupConfigs.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.list_resource_backup_configs](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_list_resource_backup_configs)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_parse_common_billing_account_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_parse_common_folder_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_parse_common_location_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_parse_common_organization_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_parse_common_project_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_resource_backup_config_path
    
    
    parse_resource_backup_config_path(path: str) -> typing.Dict[str, str]

Parses a resource_backup_config path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_resource_backup_config_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_parse_resource_backup_config_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.resource_backup_config_path
    
    
    resource_backup_config_path(
        project: str, location: str, resource_backup_config: str
    ) -> str

Returns a fully-qualified resource_backup_config string.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.resource_backup_config_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_resource_backup_config_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_set_iam_policy)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_test_iam_permissions)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient
    
    
    BackupDrProtectionSummaryClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.backupdr_v1.services.backup_dr_protection_summary.transports.base.BackupDrProtectionSummaryTransport,
                typing.Callable[
                    [...],
                    google.cloud.backupdr_v1.services.backup_dr_protection_summary.transports.base.BackupDrProtectionSummaryTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the backup dr protection summary client.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_BackupDrProtectionSummaryClient)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.**exit**](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient___exit__)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.cancel_operation
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.cancel_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_cancel_operation)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_common_billing_account_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_folder_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_common_folder_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_location_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_common_location_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_organization_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_common_organization_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_project_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_common_project_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.delete_operation
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.delete_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_delete_operation)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.from_service_account_file](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_from_service_account_file)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.from_service_account_info](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_from_service_account_info)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.from_service_account_json](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_from_service_account_json)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.get_iam_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_get_iam_policy)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.get_location
    
    
    get_location(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.GetLocationRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.Location

Gets information about a location.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.get_location](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_get_location)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_get_mtls_endpoint_and_cert_source)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.get_operation
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.get_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_get_operation)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.list_locations
    
    
    list_locations(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.ListLocationsRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.ListLocationsResponse

Lists information about the supported locations for this service.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.list_locations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_list_locations)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.list_operations
    
    
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

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.list_operations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_list_operations)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.list_resource_backup_configs
    
    
    list_resource_backup_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1.types.protection_summary.ListResourceBackupConfigsRequest,
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
        google.cloud.backupdr_v1.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsPager
    )

Lists ResourceBackupConfigs.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.list_resource_backup_configs](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_list_resource_backup_configs)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_parse_common_billing_account_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_parse_common_folder_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_parse_common_location_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_parse_common_organization_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_parse_common_project_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_resource_backup_config_path
    
    
    parse_resource_backup_config_path(path: str) -> typing.Dict[str, str]

Parses a resource_backup_config path into its component segments.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_resource_backup_config_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_parse_resource_backup_config_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.resource_backup_config_path
    
    
    resource_backup_config_path(
        project: str, location: str, resource_backup_config: str
    ) -> str

Returns a fully-qualified resource_backup_config string.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.resource_backup_config_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_resource_backup_config_path)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.set_iam_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_set_iam_policy)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_test_iam_permissions)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsAsyncPager
    
    
    ListResourceBackupConfigsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.protection_summary.ListResourceBackupConfigsResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.protection_summary.ListResourceBackupConfigsRequest,
        response: google.cloud.backupdr_v1.types.protection_summary.ListResourceBackupConfigsResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsAsyncPager#google_cloud_backupdr_v1_services_backup_dr_protection_summary_pagers_ListResourceBackupConfigsAsyncPager_ListResourceBackupConfigsAsyncPager)

### google.cloud.backupdr_v1.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsPager
    
    
    ListResourceBackupConfigsPager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1.types.protection_summary.ListResourceBackupConfigsResponse,
        ],
        request: google.cloud.backupdr_v1.types.protection_summary.ListResourceBackupConfigsRequest,
        response: google.cloud.backupdr_v1.types.protection_summary.ListResourceBackupConfigsResponse,
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

See more: [google.cloud.backupdr_v1.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsPager#google_cloud_backupdr_v1_services_backup_dr_protection_summary_pagers_ListResourceBackupConfigsPager_ListResourceBackupConfigsPager)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient
    
    
    BackupDRAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.backupdr_v1beta.services.backup_dr.transports.base.BackupDRTransport,
                typing.Callable[
                    [...],
                    google.cloud.backupdr_v1beta.services.backup_dr.transports.base.BackupDRTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the backup dr async client.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_BackupDRAsyncClient)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.applied_auto_protection_policy_path
    
    
    applied_auto_protection_policy_path(
        project: str, location: str, applied_auto_protection_policy: str
    ) -> str

Returns a fully-qualified applied_auto_protection_policy string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.applied_auto_protection_policy_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_applied_auto_protection_policy_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.auto_protection_policy_binding_path
    
    
    auto_protection_policy_binding_path(
        project: str, location: str, auto_protection_policy: str, binding: str
    ) -> str

Returns a fully-qualified auto_protection_policy_binding string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.auto_protection_policy_binding_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_auto_protection_policy_binding_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.auto_protection_policy_path
    
    
    auto_protection_policy_path(
        project: str, location: str, auto_protection_policy: str
    ) -> str

Returns a fully-qualified auto_protection_policy string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.auto_protection_policy_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_auto_protection_policy_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.backup_path
    
    
    backup_path(
        project: str, location: str, backupvault: str, datasource: str, backup: str
    ) -> str

Returns a fully-qualified backup string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.backup_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_backup_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.backup_plan_association_path
    
    
    backup_plan_association_path(
        project: str, location: str, backup_plan_association: str
    ) -> str

Returns a fully-qualified backup_plan_association string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.backup_plan_association_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_backup_plan_association_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.backup_plan_path
    
    
    backup_plan_path(project: str, location: str, backup_plan: str) -> str

Returns a fully-qualified backup_plan string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.backup_plan_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_backup_plan_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.backup_plan_revision_path
    
    
    backup_plan_revision_path(
        project: str, location: str, backup_plan: str, revision: str
    ) -> str

Returns a fully-qualified backup_plan_revision string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.backup_plan_revision_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_backup_plan_revision_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.backup_vault_path
    
    
    backup_vault_path(project: str, location: str, backupvault: str) -> str

Returns a fully-qualified backup_vault string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.backup_vault_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_backup_vault_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.binding_matching_resource_path
    
    
    binding_matching_resource_path(
        project: str,
        location: str,
        auto_protection_policy: str,
        binding: str,
        matching_resource: str,
    ) -> str

Returns a fully-qualified binding_matching_resource string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.binding_matching_resource_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_binding_matching_resource_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_cancel_operation)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.cluster_path
    
    
    cluster_path(project: str, location: str, cluster: str) -> str

Returns a fully-qualified cluster string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.cluster_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_cluster_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_common_billing_account_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_common_folder_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_common_location_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_common_organization_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_common_project_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.create_auto_protection_policy
    
    
    create_auto_protection_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicy.CreateAutoProtectionPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        auto_protection_policy: typing.Optional[
            google.cloud.backupdr_v1beta.types.autoprotectionpolicy.AutoProtectionPolicy
        ] = None,
        auto_protection_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new AutoProtectionPolicy in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.create_auto_protection_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_create_auto_protection_policy)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.create_auto_protection_policy_binding
    
    
    create_auto_protection_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.CreateAutoProtectionPolicyBindingRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        auto_protection_policy_binding: typing.Optional[
            google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.AutoProtectionPolicyBinding
        ] = None,
        auto_protection_policy_binding_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new AutoProtectionPolicyBinding in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.create_auto_protection_policy_binding](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_create_auto_protection_policy_binding)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.create_backup_plan
    
    
    create_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplan.CreateBackupPlanRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_plan: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupplan.BackupPlan
        ] = None,
        backup_plan_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Create a BackupPlan.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.create_backup_plan](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_create_backup_plan)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.create_backup_plan_association
    
    
    create_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplanassociation.CreateBackupPlanAssociationRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_plan_association: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupplanassociation.BackupPlanAssociation
        ] = None,
        backup_plan_association_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Create a BackupPlanAssociation.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.create_backup_plan_association](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_create_backup_plan_association)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.create_backup_vault
    
    
    create_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.CreateBackupVaultRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_vault: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupvault.BackupVault
        ] = None,
        backup_vault_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new BackupVault in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.create_backup_vault](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_create_backup_vault)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.create_management_server
    
    
    create_management_server(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupdr.CreateManagementServerRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        management_server: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupdr.ManagementServer
        ] = None,
        management_server_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new ManagementServer in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.create_management_server](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_create_management_server)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, ring: str, key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.crypto_key_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_crypto_key_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.crypto_key_version_path
    
    
    crypto_key_version_path(
        project: str, location: str, key_ring: str, crypto_key: str, crypto_key_version: str
    ) -> str

Returns a fully-qualified crypto_key_version string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.crypto_key_version_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_crypto_key_version_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.data_source_path
    
    
    data_source_path(
        project: str, location: str, backupvault: str, datasource: str
    ) -> str

Returns a fully-qualified data_source string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.data_source_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_data_source_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.data_source_reference_path
    
    
    data_source_reference_path(
        project: str, location: str, data_source_reference: str
    ) -> str

Returns a fully-qualified data_source_reference string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.data_source_reference_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_data_source_reference_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.delete_auto_protection_policy
    
    
    delete_auto_protection_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicy.DeleteAutoProtectionPolicyRequest,
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

Deletes a single AutoProtectionPolicy.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.delete_auto_protection_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_delete_auto_protection_policy)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.delete_backup
    
    
    delete_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.DeleteBackupRequest, dict
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

Deletes a Backup.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.delete_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_delete_backup)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.delete_backup_plan
    
    
    delete_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplan.DeleteBackupPlanRequest, dict
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

Deletes a single BackupPlan.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.delete_backup_plan](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_delete_backup_plan)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.delete_backup_plan_association
    
    
    delete_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplanassociation.DeleteBackupPlanAssociationRequest,
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

Deletes a single BackupPlanAssociation.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.delete_backup_plan_association](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_delete_backup_plan_association)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.delete_backup_vault
    
    
    delete_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.DeleteBackupVaultRequest,
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

Deletes a BackupVault.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.delete_backup_vault](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_delete_backup_vault)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.delete_management_server
    
    
    delete_management_server(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupdr.DeleteManagementServerRequest,
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

Deletes a single ManagementServer.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.delete_management_server](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_delete_management_server)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.delete_operation
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_delete_operation)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.fetch_backup_plan_associations_for_resource_type
    
    
    fetch_backup_plan_associations_for_resource_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypeAsyncPager
    )

List BackupPlanAssociations for a given resource type.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.fetch_backup_plan_associations_for_resource_type](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_fetch_backup_plan_associations_for_resource_type)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.fetch_backups_for_resource_type
    
    
    fetch_backups_for_resource_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.FetchBackupsForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupsForResourceTypeAsyncPager
    )

Fetch Backups for a given resource type.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.fetch_backups_for_resource_type](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_fetch_backups_for_resource_type)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.fetch_data_source_references_for_resource_type
    
    
    fetch_data_source_references_for_resource_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypeAsyncPager
    )

Fetch DataSourceReferences for a given project, location and resource type.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.fetch_data_source_references_for_resource_type](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_fetch_data_source_references_for_resource_type)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.fetch_usable_backup_vaults
    
    
    fetch_usable_backup_vaults(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.FetchUsableBackupVaultsRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchUsableBackupVaultsAsyncPager
    )

FetchUsableBackupVaults lists usable BackupVaults in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.fetch_usable_backup_vaults](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_fetch_usable_backup_vaults)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_from_service_account_file)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_from_service_account_info)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_from_service_account_json)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_auto_protection_policy
    
    
    get_auto_protection_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicy.GetAutoProtectionPolicyRequest,
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
    ) -> google.cloud.backupdr_v1beta.types.autoprotectionpolicy.AutoProtectionPolicy

Gets details of a single AutoProtectionPolicy.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_auto_protection_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_get_auto_protection_policy)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_auto_protection_policy_binding
    
    
    get_auto_protection_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.GetAutoProtectionPolicyBindingRequest,
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
        google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.AutoProtectionPolicyBinding
    )

Returns the auto protection policy binding read from the CCFE tables.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_auto_protection_policy_binding](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_get_auto_protection_policy_binding)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_backup
    
    
    get_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.GetBackupRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.types.backupvault.Backup

Gets details of a Backup.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_get_backup)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_backup_plan
    
    
    get_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplan.GetBackupPlanRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.types.backupplan.BackupPlan

Gets details of a single BackupPlan.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_backup_plan](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_get_backup_plan)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_backup_plan_association
    
    
    get_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplanassociation.GetBackupPlanAssociationRequest,
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
    ) -> google.cloud.backupdr_v1beta.types.backupplanassociation.BackupPlanAssociation

Gets details of a single BackupPlanAssociation.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_backup_plan_association](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_get_backup_plan_association)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_backup_plan_revision
    
    
    get_backup_plan_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplan.GetBackupPlanRevisionRequest,
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
    ) -> google.cloud.backupdr_v1beta.types.backupplan.BackupPlanRevision

Gets details of a single BackupPlanRevision.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_backup_plan_revision](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_get_backup_plan_revision)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_backup_vault
    
    
    get_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.GetBackupVaultRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.types.backupvault.BackupVault

Gets details of a BackupVault.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_backup_vault](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_get_backup_vault)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_binding_matching_resource
    
    
    get_binding_matching_resource(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.bindingmatchingresource.GetBindingMatchingResourceRequest,
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
    ) -> google.cloud.backupdr_v1beta.types.bindingmatchingresource.BindingMatchingResource

Gets details of a single Binding Matching Resource.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_binding_matching_resource](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_get_binding_matching_resource)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_data_source
    
    
    get_data_source(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.GetDataSourceRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.types.backupvault.DataSource

Gets details of a DataSource.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_data_source](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_get_data_source)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_data_source_reference
    
    
    get_data_source_reference(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.datasourcereference.GetDataSourceReferenceRequest,
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
    ) -> google.cloud.backupdr_v1beta.types.datasourcereference.DataSourceReference

Gets details of a single DataSourceReference.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_data_source_reference](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_get_data_source_reference)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_get_iam_policy)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_location
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_location](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_get_location)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_management_server
    
    
    get_management_server(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupdr.GetManagementServerRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.types.backupdr.ManagementServer

Gets details of a single ManagementServer.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_management_server](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_get_management_server)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_operation
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_get_operation)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.backupdr_v1beta.services.backup_dr.transports.base.BackupDRTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_get_transport_class)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.initialize_service
    
    
    initialize_service(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupdr.InitializeServiceRequest, dict
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

Initializes the service related config for a project.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.initialize_service](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_initialize_service)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.initiate_delete_auto_protection_policy_binding
    
    
    initiate_delete_auto_protection_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.InitiateDeleteAutoProtectionPolicyBindingRequest,
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

InitiateDeleteAutoProtectionPolicyBinding initiates delete for AutoProtectionPolicy Binding.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.initiate_delete_auto_protection_policy_binding](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_initiate_delete_auto_protection_policy_binding)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.instance_path
    
    
    instance_path(project: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.instance_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_instance_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_applied_auto_protection_policies
    
    
    list_applied_auto_protection_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAppliedAutoProtectionPoliciesAsyncPager
    )

Lists AppliedAutoProtectionPolicies in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_applied_auto_protection_policies](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_list_applied_auto_protection_policies)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_auto_protection_policies
    
    
    list_auto_protection_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicy.ListAutoProtectionPoliciesRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPoliciesAsyncPager
    )

Lists AutoProtectionPolicies for a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_auto_protection_policies](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_list_auto_protection_policies)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_auto_protection_policy_bindings
    
    
    list_auto_protection_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPolicyBindingsAsyncPager
    )

Returns the auto protection policy bindings read from the CCFE tables.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_auto_protection_policy_bindings](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_list_auto_protection_policy_bindings)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_backup_plan_associations
    
    
    list_backup_plan_associations(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplanassociation.ListBackupPlanAssociationsRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanAssociationsAsyncPager
    )

Lists BackupPlanAssociations in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_backup_plan_associations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_list_backup_plan_associations)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_backup_plan_revisions
    
    
    list_backup_plan_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplan.ListBackupPlanRevisionsRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanRevisionsAsyncPager
    )

Lists BackupPlanRevisions in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_backup_plan_revisions](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_list_backup_plan_revisions)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_backup_plans
    
    
    list_backup_plans(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplan.ListBackupPlansRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlansAsyncPager

Lists BackupPlans in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_backup_plans](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_list_backup_plans)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_backup_vaults
    
    
    list_backup_vaults(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.ListBackupVaultsRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupVaultsAsyncPager

Lists BackupVaults in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_backup_vaults](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_list_backup_vaults)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_backups
    
    
    list_backups(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.ListBackupsRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupsAsyncPager

Lists Backups in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_backups](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_list_backups)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_binding_matching_resources
    
    
    list_binding_matching_resources(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.bindingmatchingresource.ListBindingMatchingResourcesRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBindingMatchingResourcesAsyncPager
    )

Lists Binding Matching Resources for a given AutoProtectionPolicyBinding.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_binding_matching_resources](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_list_binding_matching_resources)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_data_source_references
    
    
    list_data_source_references(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.datasourcereference.ListDataSourceReferencesRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourceReferencesAsyncPager
    )

Lists DataSourceReferences for a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_data_source_references](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_list_data_source_references)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_data_sources
    
    
    list_data_sources(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.ListDataSourcesRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourcesAsyncPager

Lists DataSources in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_data_sources](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_list_data_sources)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_locations
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_list_locations)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_management_servers
    
    
    list_management_servers(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupdr.ListManagementServersRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListManagementServersAsyncPager
    )

Lists ManagementServers in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_management_servers](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_list_management_servers)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_operations
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_list_operations)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.management_server_path
    
    
    management_server_path(project: str, location: str, managementserver: str) -> str

Returns a fully-qualified management_server string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.management_server_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_management_server_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_applied_auto_protection_policy_path
    
    
    parse_applied_auto_protection_policy_path(path: str) -> typing.Dict[str, str]

Parses a applied_auto_protection_policy path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_applied_auto_protection_policy_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_applied_auto_protection_policy_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_auto_protection_policy_binding_path
    
    
    parse_auto_protection_policy_binding_path(path: str) -> typing.Dict[str, str]

Parses a auto_protection_policy_binding path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_auto_protection_policy_binding_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_auto_protection_policy_binding_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_auto_protection_policy_path
    
    
    parse_auto_protection_policy_path(path: str) -> typing.Dict[str, str]

Parses a auto_protection_policy path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_auto_protection_policy_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_auto_protection_policy_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_backup_path
    
    
    parse_backup_path(path: str) -> typing.Dict[str, str]

Parses a backup path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_backup_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_backup_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_backup_plan_association_path
    
    
    parse_backup_plan_association_path(path: str) -> typing.Dict[str, str]

Parses a backup_plan_association path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_backup_plan_association_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_backup_plan_association_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_backup_plan_path
    
    
    parse_backup_plan_path(path: str) -> typing.Dict[str, str]

Parses a backup_plan path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_backup_plan_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_backup_plan_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_backup_plan_revision_path
    
    
    parse_backup_plan_revision_path(path: str) -> typing.Dict[str, str]

Parses a backup_plan_revision path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_backup_plan_revision_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_backup_plan_revision_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_backup_vault_path
    
    
    parse_backup_vault_path(path: str) -> typing.Dict[str, str]

Parses a backup_vault path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_backup_vault_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_backup_vault_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_binding_matching_resource_path
    
    
    parse_binding_matching_resource_path(path: str) -> typing.Dict[str, str]

Parses a binding_matching_resource path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_binding_matching_resource_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_binding_matching_resource_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_cluster_path
    
    
    parse_cluster_path(path: str) -> typing.Dict[str, str]

Parses a cluster path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_cluster_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_cluster_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_common_billing_account_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_common_folder_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_common_location_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_common_organization_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_common_project_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_crypto_key_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_crypto_key_version_path
    
    
    parse_crypto_key_version_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key_version path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_crypto_key_version_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_crypto_key_version_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_data_source_path
    
    
    parse_data_source_path(path: str) -> typing.Dict[str, str]

Parses a data_source path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_data_source_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_data_source_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_data_source_reference_path
    
    
    parse_data_source_reference_path(path: str) -> typing.Dict[str, str]

Parses a data_source_reference path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_data_source_reference_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_data_source_reference_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_instance_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_instance_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_management_server_path
    
    
    parse_management_server_path(path: str) -> typing.Dict[str, str]

Parses a management_server path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_management_server_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_management_server_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_storage_pool_path
    
    
    parse_storage_pool_path(path: str) -> typing.Dict[str, str]

Parses a storage_pool path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.parse_storage_pool_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_parse_storage_pool_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.restore_backup
    
    
    restore_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.RestoreBackupRequest, dict
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

Restore from a Backup.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.restore_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_restore_backup)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_set_iam_policy)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.storage_pool_path
    
    
    storage_pool_path(project: str, zone: str, storage_pool: str) -> str

Returns a fully-qualified storage_pool string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.storage_pool_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_storage_pool_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_test_iam_permissions)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.trigger_backup
    
    
    trigger_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplanassociation.TriggerBackupRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        rule_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Triggers a new Backup.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.trigger_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_trigger_backup)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.update_auto_protection_policy
    
    
    update_auto_protection_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicy.UpdateAutoProtectionPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        auto_protection_policy: typing.Optional[
            google.cloud.backupdr_v1beta.types.autoprotectionpolicy.AutoProtectionPolicy
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

Updates the parameters of a single AutoProtectionPolicy.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.update_auto_protection_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_update_auto_protection_policy)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.update_backup
    
    
    update_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.UpdateBackupRequest, dict
            ]
        ] = None,
        *,
        backup: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupvault.Backup
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

Updates the settings of a Backup.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.update_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_update_backup)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.update_backup_plan
    
    
    update_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplan.UpdateBackupPlanRequest, dict
            ]
        ] = None,
        *,
        backup_plan: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupplan.BackupPlan
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

Update a BackupPlan.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.update_backup_plan](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_update_backup_plan)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.update_backup_plan_association
    
    
    update_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplanassociation.UpdateBackupPlanAssociationRequest,
                dict,
            ]
        ] = None,
        *,
        backup_plan_association: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupplanassociation.BackupPlanAssociation
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

Update a BackupPlanAssociation.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.update_backup_plan_association](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_update_backup_plan_association)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.update_backup_vault
    
    
    update_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.UpdateBackupVaultRequest,
                dict,
            ]
        ] = None,
        *,
        backup_vault: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupvault.BackupVault
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

Updates the settings of a BackupVault.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.update_backup_vault](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_update_backup_vault)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.update_data_source
    
    
    update_data_source(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.UpdateDataSourceRequest, dict
            ]
        ] = None,
        *,
        data_source: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupvault.DataSource
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

Updates the settings of a DataSource.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient.update_data_source](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRAsyncClient_update_data_source)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient
    
    
    BackupDRClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.backupdr_v1beta.services.backup_dr.transports.base.BackupDRTransport,
                typing.Callable[
                    [...],
                    google.cloud.backupdr_v1beta.services.backup_dr.transports.base.BackupDRTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the backup dr client.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_BackupDRClient)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.**exit**](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient___exit__)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.applied_auto_protection_policy_path
    
    
    applied_auto_protection_policy_path(
        project: str, location: str, applied_auto_protection_policy: str
    ) -> str

Returns a fully-qualified applied_auto_protection_policy string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.applied_auto_protection_policy_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_applied_auto_protection_policy_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.auto_protection_policy_binding_path
    
    
    auto_protection_policy_binding_path(
        project: str, location: str, auto_protection_policy: str, binding: str
    ) -> str

Returns a fully-qualified auto_protection_policy_binding string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.auto_protection_policy_binding_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_auto_protection_policy_binding_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.auto_protection_policy_path
    
    
    auto_protection_policy_path(
        project: str, location: str, auto_protection_policy: str
    ) -> str

Returns a fully-qualified auto_protection_policy string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.auto_protection_policy_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_auto_protection_policy_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.backup_path
    
    
    backup_path(
        project: str, location: str, backupvault: str, datasource: str, backup: str
    ) -> str

Returns a fully-qualified backup string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.backup_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_backup_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.backup_plan_association_path
    
    
    backup_plan_association_path(
        project: str, location: str, backup_plan_association: str
    ) -> str

Returns a fully-qualified backup_plan_association string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.backup_plan_association_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_backup_plan_association_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.backup_plan_path
    
    
    backup_plan_path(project: str, location: str, backup_plan: str) -> str

Returns a fully-qualified backup_plan string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.backup_plan_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_backup_plan_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.backup_plan_revision_path
    
    
    backup_plan_revision_path(
        project: str, location: str, backup_plan: str, revision: str
    ) -> str

Returns a fully-qualified backup_plan_revision string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.backup_plan_revision_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_backup_plan_revision_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.backup_vault_path
    
    
    backup_vault_path(project: str, location: str, backupvault: str) -> str

Returns a fully-qualified backup_vault string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.backup_vault_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_backup_vault_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.binding_matching_resource_path
    
    
    binding_matching_resource_path(
        project: str,
        location: str,
        auto_protection_policy: str,
        binding: str,
        matching_resource: str,
    ) -> str

Returns a fully-qualified binding_matching_resource string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.binding_matching_resource_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_binding_matching_resource_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.cancel_operation
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.cancel_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_cancel_operation)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.cluster_path
    
    
    cluster_path(project: str, location: str, cluster: str) -> str

Returns a fully-qualified cluster string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.cluster_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_cluster_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_common_billing_account_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.common_folder_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_common_folder_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.common_location_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_common_location_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.common_organization_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_common_organization_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.common_project_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_common_project_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.create_auto_protection_policy
    
    
    create_auto_protection_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicy.CreateAutoProtectionPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        auto_protection_policy: typing.Optional[
            google.cloud.backupdr_v1beta.types.autoprotectionpolicy.AutoProtectionPolicy
        ] = None,
        auto_protection_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new AutoProtectionPolicy in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.create_auto_protection_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_create_auto_protection_policy)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.create_auto_protection_policy_binding
    
    
    create_auto_protection_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.CreateAutoProtectionPolicyBindingRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        auto_protection_policy_binding: typing.Optional[
            google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.AutoProtectionPolicyBinding
        ] = None,
        auto_protection_policy_binding_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new AutoProtectionPolicyBinding in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.create_auto_protection_policy_binding](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_create_auto_protection_policy_binding)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.create_backup_plan
    
    
    create_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplan.CreateBackupPlanRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_plan: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupplan.BackupPlan
        ] = None,
        backup_plan_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Create a BackupPlan.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.create_backup_plan](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_create_backup_plan)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.create_backup_plan_association
    
    
    create_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplanassociation.CreateBackupPlanAssociationRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_plan_association: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupplanassociation.BackupPlanAssociation
        ] = None,
        backup_plan_association_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Create a BackupPlanAssociation.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.create_backup_plan_association](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_create_backup_plan_association)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.create_backup_vault
    
    
    create_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.CreateBackupVaultRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_vault: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupvault.BackupVault
        ] = None,
        backup_vault_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new BackupVault in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.create_backup_vault](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_create_backup_vault)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.create_management_server
    
    
    create_management_server(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupdr.CreateManagementServerRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        management_server: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupdr.ManagementServer
        ] = None,
        management_server_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new ManagementServer in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.create_management_server](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_create_management_server)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, ring: str, key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.crypto_key_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_crypto_key_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.crypto_key_version_path
    
    
    crypto_key_version_path(
        project: str, location: str, key_ring: str, crypto_key: str, crypto_key_version: str
    ) -> str

Returns a fully-qualified crypto_key_version string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.crypto_key_version_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_crypto_key_version_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.data_source_path
    
    
    data_source_path(
        project: str, location: str, backupvault: str, datasource: str
    ) -> str

Returns a fully-qualified data_source string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.data_source_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_data_source_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.data_source_reference_path
    
    
    data_source_reference_path(
        project: str, location: str, data_source_reference: str
    ) -> str

Returns a fully-qualified data_source_reference string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.data_source_reference_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_data_source_reference_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.delete_auto_protection_policy
    
    
    delete_auto_protection_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicy.DeleteAutoProtectionPolicyRequest,
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

Deletes a single AutoProtectionPolicy.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.delete_auto_protection_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_delete_auto_protection_policy)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.delete_backup
    
    
    delete_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.DeleteBackupRequest, dict
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

Deletes a Backup.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.delete_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_delete_backup)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.delete_backup_plan
    
    
    delete_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplan.DeleteBackupPlanRequest, dict
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

Deletes a single BackupPlan.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.delete_backup_plan](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_delete_backup_plan)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.delete_backup_plan_association
    
    
    delete_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplanassociation.DeleteBackupPlanAssociationRequest,
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

Deletes a single BackupPlanAssociation.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.delete_backup_plan_association](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_delete_backup_plan_association)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.delete_backup_vault
    
    
    delete_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.DeleteBackupVaultRequest,
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

Deletes a BackupVault.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.delete_backup_vault](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_delete_backup_vault)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.delete_management_server
    
    
    delete_management_server(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupdr.DeleteManagementServerRequest,
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

Deletes a single ManagementServer.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.delete_management_server](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_delete_management_server)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.delete_operation
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.delete_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_delete_operation)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.fetch_backup_plan_associations_for_resource_type
    
    
    fetch_backup_plan_associations_for_resource_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypePager
    )

List BackupPlanAssociations for a given resource type.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.fetch_backup_plan_associations_for_resource_type](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_fetch_backup_plan_associations_for_resource_type)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.fetch_backups_for_resource_type
    
    
    fetch_backups_for_resource_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.FetchBackupsForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupsForResourceTypePager
    )

Fetch Backups for a given resource type.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.fetch_backups_for_resource_type](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_fetch_backups_for_resource_type)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.fetch_data_source_references_for_resource_type
    
    
    fetch_data_source_references_for_resource_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypePager
    )

Fetch DataSourceReferences for a given project, location and resource type.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.fetch_data_source_references_for_resource_type](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_fetch_data_source_references_for_resource_type)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.fetch_usable_backup_vaults
    
    
    fetch_usable_backup_vaults(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.FetchUsableBackupVaultsRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchUsableBackupVaultsPager
    )

FetchUsableBackupVaults lists usable BackupVaults in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.fetch_usable_backup_vaults](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_fetch_usable_backup_vaults)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.from_service_account_file](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_from_service_account_file)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.from_service_account_info](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_from_service_account_info)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.from_service_account_json](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_from_service_account_json)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_auto_protection_policy
    
    
    get_auto_protection_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicy.GetAutoProtectionPolicyRequest,
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
    ) -> google.cloud.backupdr_v1beta.types.autoprotectionpolicy.AutoProtectionPolicy

Gets details of a single AutoProtectionPolicy.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_auto_protection_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_get_auto_protection_policy)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_auto_protection_policy_binding
    
    
    get_auto_protection_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.GetAutoProtectionPolicyBindingRequest,
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
        google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.AutoProtectionPolicyBinding
    )

Returns the auto protection policy binding read from the CCFE tables.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_auto_protection_policy_binding](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_get_auto_protection_policy_binding)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_backup
    
    
    get_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.GetBackupRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.types.backupvault.Backup

Gets details of a Backup.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_get_backup)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_backup_plan
    
    
    get_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplan.GetBackupPlanRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.types.backupplan.BackupPlan

Gets details of a single BackupPlan.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_backup_plan](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_get_backup_plan)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_backup_plan_association
    
    
    get_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplanassociation.GetBackupPlanAssociationRequest,
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
    ) -> google.cloud.backupdr_v1beta.types.backupplanassociation.BackupPlanAssociation

Gets details of a single BackupPlanAssociation.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_backup_plan_association](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_get_backup_plan_association)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_backup_plan_revision
    
    
    get_backup_plan_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplan.GetBackupPlanRevisionRequest,
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
    ) -> google.cloud.backupdr_v1beta.types.backupplan.BackupPlanRevision

Gets details of a single BackupPlanRevision.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_backup_plan_revision](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_get_backup_plan_revision)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_backup_vault
    
    
    get_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.GetBackupVaultRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.types.backupvault.BackupVault

Gets details of a BackupVault.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_backup_vault](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_get_backup_vault)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_binding_matching_resource
    
    
    get_binding_matching_resource(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.bindingmatchingresource.GetBindingMatchingResourceRequest,
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
    ) -> google.cloud.backupdr_v1beta.types.bindingmatchingresource.BindingMatchingResource

Gets details of a single Binding Matching Resource.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_binding_matching_resource](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_get_binding_matching_resource)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_data_source
    
    
    get_data_source(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.GetDataSourceRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.types.backupvault.DataSource

Gets details of a DataSource.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_data_source](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_get_data_source)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_data_source_reference
    
    
    get_data_source_reference(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.datasourcereference.GetDataSourceReferenceRequest,
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
    ) -> google.cloud.backupdr_v1beta.types.datasourcereference.DataSourceReference

Gets details of a single DataSourceReference.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_data_source_reference](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_get_data_source_reference)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_iam_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_get_iam_policy)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_location
    
    
    get_location(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.GetLocationRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.Location

Gets information about a location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_location](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_get_location)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_management_server
    
    
    get_management_server(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupdr.GetManagementServerRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.types.backupdr.ManagementServer

Gets details of a single ManagementServer.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_management_server](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_get_management_server)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_get_mtls_endpoint_and_cert_source)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_operation
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.get_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_get_operation)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.initialize_service
    
    
    initialize_service(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupdr.InitializeServiceRequest, dict
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

Initializes the service related config for a project.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.initialize_service](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_initialize_service)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.initiate_delete_auto_protection_policy_binding
    
    
    initiate_delete_auto_protection_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.InitiateDeleteAutoProtectionPolicyBindingRequest,
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

InitiateDeleteAutoProtectionPolicyBinding initiates delete for AutoProtectionPolicy Binding.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.initiate_delete_auto_protection_policy_binding](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_initiate_delete_auto_protection_policy_binding)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.instance_path
    
    
    instance_path(project: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.instance_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_instance_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_applied_auto_protection_policies
    
    
    list_applied_auto_protection_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAppliedAutoProtectionPoliciesPager
    )

Lists AppliedAutoProtectionPolicies in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_applied_auto_protection_policies](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_list_applied_auto_protection_policies)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_auto_protection_policies
    
    
    list_auto_protection_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicy.ListAutoProtectionPoliciesRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPoliciesPager
    )

Lists AutoProtectionPolicies for a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_auto_protection_policies](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_list_auto_protection_policies)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_auto_protection_policy_bindings
    
    
    list_auto_protection_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPolicyBindingsPager
    )

Returns the auto protection policy bindings read from the CCFE tables.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_auto_protection_policy_bindings](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_list_auto_protection_policy_bindings)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_backup_plan_associations
    
    
    list_backup_plan_associations(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplanassociation.ListBackupPlanAssociationsRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanAssociationsPager
    )

Lists BackupPlanAssociations in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_backup_plan_associations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_list_backup_plan_associations)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_backup_plan_revisions
    
    
    list_backup_plan_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplan.ListBackupPlanRevisionsRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanRevisionsPager
    )

Lists BackupPlanRevisions in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_backup_plan_revisions](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_list_backup_plan_revisions)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_backup_plans
    
    
    list_backup_plans(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplan.ListBackupPlansRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlansPager

Lists BackupPlans in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_backup_plans](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_list_backup_plans)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_backup_vaults
    
    
    list_backup_vaults(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.ListBackupVaultsRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupVaultsPager

Lists BackupVaults in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_backup_vaults](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_list_backup_vaults)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_backups
    
    
    list_backups(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.ListBackupsRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupsPager

Lists Backups in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_backups](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_list_backups)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_binding_matching_resources
    
    
    list_binding_matching_resources(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.bindingmatchingresource.ListBindingMatchingResourcesRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBindingMatchingResourcesPager
    )

Lists Binding Matching Resources for a given AutoProtectionPolicyBinding.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_binding_matching_resources](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_list_binding_matching_resources)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_data_source_references
    
    
    list_data_source_references(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.datasourcereference.ListDataSourceReferencesRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourceReferencesPager
    )

Lists DataSourceReferences for a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_data_source_references](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_list_data_source_references)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_data_sources
    
    
    list_data_sources(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.ListDataSourcesRequest, dict
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
    ) -> google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourcesPager

Lists DataSources in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_data_sources](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_list_data_sources)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_locations
    
    
    list_locations(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.ListLocationsRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.ListLocationsResponse

Lists information about the supported locations for this service.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_locations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_list_locations)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_management_servers
    
    
    list_management_servers(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupdr.ListManagementServersRequest,
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
    ) -> google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListManagementServersPager

Lists ManagementServers in a given project and location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_management_servers](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_list_management_servers)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_operations
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.list_operations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_list_operations)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.management_server_path
    
    
    management_server_path(project: str, location: str, managementserver: str) -> str

Returns a fully-qualified management_server string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.management_server_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_management_server_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_applied_auto_protection_policy_path
    
    
    parse_applied_auto_protection_policy_path(path: str) -> typing.Dict[str, str]

Parses a applied_auto_protection_policy path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_applied_auto_protection_policy_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_applied_auto_protection_policy_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_auto_protection_policy_binding_path
    
    
    parse_auto_protection_policy_binding_path(path: str) -> typing.Dict[str, str]

Parses a auto_protection_policy_binding path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_auto_protection_policy_binding_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_auto_protection_policy_binding_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_auto_protection_policy_path
    
    
    parse_auto_protection_policy_path(path: str) -> typing.Dict[str, str]

Parses a auto_protection_policy path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_auto_protection_policy_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_auto_protection_policy_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_backup_path
    
    
    parse_backup_path(path: str) -> typing.Dict[str, str]

Parses a backup path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_backup_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_backup_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_backup_plan_association_path
    
    
    parse_backup_plan_association_path(path: str) -> typing.Dict[str, str]

Parses a backup_plan_association path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_backup_plan_association_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_backup_plan_association_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_backup_plan_path
    
    
    parse_backup_plan_path(path: str) -> typing.Dict[str, str]

Parses a backup_plan path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_backup_plan_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_backup_plan_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_backup_plan_revision_path
    
    
    parse_backup_plan_revision_path(path: str) -> typing.Dict[str, str]

Parses a backup_plan_revision path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_backup_plan_revision_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_backup_plan_revision_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_backup_vault_path
    
    
    parse_backup_vault_path(path: str) -> typing.Dict[str, str]

Parses a backup_vault path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_backup_vault_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_backup_vault_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_binding_matching_resource_path
    
    
    parse_binding_matching_resource_path(path: str) -> typing.Dict[str, str]

Parses a binding_matching_resource path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_binding_matching_resource_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_binding_matching_resource_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_cluster_path
    
    
    parse_cluster_path(path: str) -> typing.Dict[str, str]

Parses a cluster path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_cluster_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_cluster_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_common_billing_account_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_common_folder_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_common_location_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_common_organization_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_common_project_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_crypto_key_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_crypto_key_version_path
    
    
    parse_crypto_key_version_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key_version path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_crypto_key_version_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_crypto_key_version_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_data_source_path
    
    
    parse_data_source_path(path: str) -> typing.Dict[str, str]

Parses a data_source path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_data_source_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_data_source_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_data_source_reference_path
    
    
    parse_data_source_reference_path(path: str) -> typing.Dict[str, str]

Parses a data_source_reference path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_data_source_reference_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_data_source_reference_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_instance_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_instance_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_management_server_path
    
    
    parse_management_server_path(path: str) -> typing.Dict[str, str]

Parses a management_server path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_management_server_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_management_server_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_storage_pool_path
    
    
    parse_storage_pool_path(path: str) -> typing.Dict[str, str]

Parses a storage_pool path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.parse_storage_pool_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_parse_storage_pool_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.restore_backup
    
    
    restore_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.RestoreBackupRequest, dict
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

Restore from a Backup.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.restore_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_restore_backup)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.set_iam_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_set_iam_policy)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.storage_pool_path
    
    
    storage_pool_path(project: str, zone: str, storage_pool: str) -> str

Returns a fully-qualified storage_pool string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.storage_pool_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_storage_pool_path)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_test_iam_permissions)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.trigger_backup
    
    
    trigger_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplanassociation.TriggerBackupRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        rule_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Triggers a new Backup.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.trigger_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_trigger_backup)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.update_auto_protection_policy
    
    
    update_auto_protection_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicy.UpdateAutoProtectionPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        auto_protection_policy: typing.Optional[
            google.cloud.backupdr_v1beta.types.autoprotectionpolicy.AutoProtectionPolicy
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

Updates the parameters of a single AutoProtectionPolicy.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.update_auto_protection_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_update_auto_protection_policy)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.update_backup
    
    
    update_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.UpdateBackupRequest, dict
            ]
        ] = None,
        *,
        backup: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupvault.Backup
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

Updates the settings of a Backup.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.update_backup](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_update_backup)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.update_backup_plan
    
    
    update_backup_plan(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplan.UpdateBackupPlanRequest, dict
            ]
        ] = None,
        *,
        backup_plan: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupplan.BackupPlan
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

Update a BackupPlan.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.update_backup_plan](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_update_backup_plan)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.update_backup_plan_association
    
    
    update_backup_plan_association(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupplanassociation.UpdateBackupPlanAssociationRequest,
                dict,
            ]
        ] = None,
        *,
        backup_plan_association: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupplanassociation.BackupPlanAssociation
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

Update a BackupPlanAssociation.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.update_backup_plan_association](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_update_backup_plan_association)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.update_backup_vault
    
    
    update_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.UpdateBackupVaultRequest,
                dict,
            ]
        ] = None,
        *,
        backup_vault: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupvault.BackupVault
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

Updates the settings of a BackupVault.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.update_backup_vault](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_update_backup_vault)

### google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.update_data_source
    
    
    update_data_source(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.backupvault.UpdateDataSourceRequest, dict
            ]
        ] = None,
        *,
        data_source: typing.Optional[
            google.cloud.backupdr_v1beta.types.backupvault.DataSource
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

Updates the settings of a DataSource.

See more: [google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient.update_data_source](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.BackupDRClient#google_cloud_backupdr_v1beta_services_backup_dr_BackupDRClient_update_data_source)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypeAsyncPager
    
    
    FetchBackupPlanAssociationsForResourceTypeAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
        response: google.cloud.backupdr_v1beta.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypeAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypeAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_FetchBackupPlanAssociationsForResourceTypeAsyncPager_FetchBackupPlanAssociationsForResourceTypeAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypePager
    
    
    FetchBackupPlanAssociationsForResourceTypePager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1beta.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
        ],
        request: google.cloud.backupdr_v1beta.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
        response: google.cloud.backupdr_v1beta.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypePager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypePager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_FetchBackupPlanAssociationsForResourceTypePager_FetchBackupPlanAssociationsForResourceTypePager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupsForResourceTypeAsyncPager
    
    
    FetchBackupsForResourceTypeAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.backupvault.FetchBackupsForResourceTypeResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.backupvault.FetchBackupsForResourceTypeRequest,
        response: google.cloud.backupdr_v1beta.types.backupvault.FetchBackupsForResourceTypeResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupsForResourceTypeAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupsForResourceTypeAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_FetchBackupsForResourceTypeAsyncPager_FetchBackupsForResourceTypeAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupsForResourceTypePager
    
    
    FetchBackupsForResourceTypePager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1beta.types.backupvault.FetchBackupsForResourceTypeResponse,
        ],
        request: google.cloud.backupdr_v1beta.types.backupvault.FetchBackupsForResourceTypeRequest,
        response: google.cloud.backupdr_v1beta.types.backupvault.FetchBackupsForResourceTypeResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupsForResourceTypePager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchBackupsForResourceTypePager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_FetchBackupsForResourceTypePager_FetchBackupsForResourceTypePager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypeAsyncPager
    
    
    FetchDataSourceReferencesForResourceTypeAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.datasourcereference.FetchDataSourceReferencesForResourceTypeResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
        response: google.cloud.backupdr_v1beta.types.datasourcereference.FetchDataSourceReferencesForResourceTypeResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypeAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypeAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_FetchDataSourceReferencesForResourceTypeAsyncPager_FetchDataSourceReferencesForResourceTypeAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypePager
    
    
    FetchDataSourceReferencesForResourceTypePager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1beta.types.datasourcereference.FetchDataSourceReferencesForResourceTypeResponse,
        ],
        request: google.cloud.backupdr_v1beta.types.datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
        response: google.cloud.backupdr_v1beta.types.datasourcereference.FetchDataSourceReferencesForResourceTypeResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypePager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypePager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_FetchDataSourceReferencesForResourceTypePager_FetchDataSourceReferencesForResourceTypePager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchUsableBackupVaultsAsyncPager
    
    
    FetchUsableBackupVaultsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.backupvault.FetchUsableBackupVaultsResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.backupvault.FetchUsableBackupVaultsRequest,
        response: google.cloud.backupdr_v1beta.types.backupvault.FetchUsableBackupVaultsResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchUsableBackupVaultsAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchUsableBackupVaultsAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_FetchUsableBackupVaultsAsyncPager_FetchUsableBackupVaultsAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchUsableBackupVaultsPager
    
    
    FetchUsableBackupVaultsPager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1beta.types.backupvault.FetchUsableBackupVaultsResponse,
        ],
        request: google.cloud.backupdr_v1beta.types.backupvault.FetchUsableBackupVaultsRequest,
        response: google.cloud.backupdr_v1beta.types.backupvault.FetchUsableBackupVaultsResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchUsableBackupVaultsPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.FetchUsableBackupVaultsPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_FetchUsableBackupVaultsPager_FetchUsableBackupVaultsPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAppliedAutoProtectionPoliciesAsyncPager
    
    
    ListAppliedAutoProtectionPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesRequest,
        response: google.cloud.backupdr_v1beta.types.appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAppliedAutoProtectionPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAppliedAutoProtectionPoliciesAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListAppliedAutoProtectionPoliciesAsyncPager_ListAppliedAutoProtectionPoliciesAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAppliedAutoProtectionPoliciesPager
    
    
    ListAppliedAutoProtectionPoliciesPager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1beta.types.appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesResponse,
        ],
        request: google.cloud.backupdr_v1beta.types.appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesRequest,
        response: google.cloud.backupdr_v1beta.types.appliedautoprotectionpolicy.ListAppliedAutoProtectionPoliciesResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAppliedAutoProtectionPoliciesPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAppliedAutoProtectionPoliciesPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListAppliedAutoProtectionPoliciesPager_ListAppliedAutoProtectionPoliciesPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPoliciesAsyncPager
    
    
    ListAutoProtectionPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicy.ListAutoProtectionPoliciesResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.autoprotectionpolicy.ListAutoProtectionPoliciesRequest,
        response: google.cloud.backupdr_v1beta.types.autoprotectionpolicy.ListAutoProtectionPoliciesResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPoliciesAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListAutoProtectionPoliciesAsyncPager_ListAutoProtectionPoliciesAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPoliciesPager
    
    
    ListAutoProtectionPoliciesPager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1beta.types.autoprotectionpolicy.ListAutoProtectionPoliciesResponse,
        ],
        request: google.cloud.backupdr_v1beta.types.autoprotectionpolicy.ListAutoProtectionPoliciesRequest,
        response: google.cloud.backupdr_v1beta.types.autoprotectionpolicy.ListAutoProtectionPoliciesResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPoliciesPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPoliciesPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListAutoProtectionPoliciesPager_ListAutoProtectionPoliciesPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPolicyBindingsAsyncPager
    
    
    ListAutoProtectionPolicyBindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsRequest,
        response: google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPolicyBindingsAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPolicyBindingsAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListAutoProtectionPolicyBindingsAsyncPager_ListAutoProtectionPolicyBindingsAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPolicyBindingsPager
    
    
    ListAutoProtectionPolicyBindingsPager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsResponse,
        ],
        request: google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsRequest,
        response: google.cloud.backupdr_v1beta.types.autoprotectionpolicybinding.ListAutoProtectionPolicyBindingsResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPolicyBindingsPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListAutoProtectionPolicyBindingsPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListAutoProtectionPolicyBindingsPager_ListAutoProtectionPolicyBindingsPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanAssociationsAsyncPager
    
    
    ListBackupPlanAssociationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.backupplanassociation.ListBackupPlanAssociationsResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.backupplanassociation.ListBackupPlanAssociationsRequest,
        response: google.cloud.backupdr_v1beta.types.backupplanassociation.ListBackupPlanAssociationsResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanAssociationsAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanAssociationsAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListBackupPlanAssociationsAsyncPager_ListBackupPlanAssociationsAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanAssociationsPager
    
    
    ListBackupPlanAssociationsPager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1beta.types.backupplanassociation.ListBackupPlanAssociationsResponse,
        ],
        request: google.cloud.backupdr_v1beta.types.backupplanassociation.ListBackupPlanAssociationsRequest,
        response: google.cloud.backupdr_v1beta.types.backupplanassociation.ListBackupPlanAssociationsResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanAssociationsPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanAssociationsPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListBackupPlanAssociationsPager_ListBackupPlanAssociationsPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanRevisionsAsyncPager
    
    
    ListBackupPlanRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.backupplan.ListBackupPlanRevisionsResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.backupplan.ListBackupPlanRevisionsRequest,
        response: google.cloud.backupdr_v1beta.types.backupplan.ListBackupPlanRevisionsResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanRevisionsAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanRevisionsAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListBackupPlanRevisionsAsyncPager_ListBackupPlanRevisionsAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanRevisionsPager
    
    
    ListBackupPlanRevisionsPager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1beta.types.backupplan.ListBackupPlanRevisionsResponse,
        ],
        request: google.cloud.backupdr_v1beta.types.backupplan.ListBackupPlanRevisionsRequest,
        response: google.cloud.backupdr_v1beta.types.backupplan.ListBackupPlanRevisionsResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanRevisionsPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlanRevisionsPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListBackupPlanRevisionsPager_ListBackupPlanRevisionsPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlansAsyncPager
    
    
    ListBackupPlansAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.backupplan.ListBackupPlansResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.backupplan.ListBackupPlansRequest,
        response: google.cloud.backupdr_v1beta.types.backupplan.ListBackupPlansResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlansAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlansAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListBackupPlansAsyncPager_ListBackupPlansAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlansPager
    
    
    ListBackupPlansPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1beta.types.backupplan.ListBackupPlansResponse
        ],
        request: google.cloud.backupdr_v1beta.types.backupplan.ListBackupPlansRequest,
        response: google.cloud.backupdr_v1beta.types.backupplan.ListBackupPlansResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlansPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupPlansPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListBackupPlansPager_ListBackupPlansPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupVaultsAsyncPager
    
    
    ListBackupVaultsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.backupvault.ListBackupVaultsResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.backupvault.ListBackupVaultsRequest,
        response: google.cloud.backupdr_v1beta.types.backupvault.ListBackupVaultsResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupVaultsAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupVaultsAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListBackupVaultsAsyncPager_ListBackupVaultsAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupVaultsPager
    
    
    ListBackupVaultsPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1beta.types.backupvault.ListBackupVaultsResponse
        ],
        request: google.cloud.backupdr_v1beta.types.backupvault.ListBackupVaultsRequest,
        response: google.cloud.backupdr_v1beta.types.backupvault.ListBackupVaultsResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupVaultsPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupVaultsPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListBackupVaultsPager_ListBackupVaultsPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupsAsyncPager
    
    
    ListBackupsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.backupvault.ListBackupsResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.backupvault.ListBackupsRequest,
        response: google.cloud.backupdr_v1beta.types.backupvault.ListBackupsResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupsAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupsAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListBackupsAsyncPager_ListBackupsAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupsPager
    
    
    ListBackupsPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1beta.types.backupvault.ListBackupsResponse
        ],
        request: google.cloud.backupdr_v1beta.types.backupvault.ListBackupsRequest,
        response: google.cloud.backupdr_v1beta.types.backupvault.ListBackupsResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupsPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBackupsPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListBackupsPager_ListBackupsPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBindingMatchingResourcesAsyncPager
    
    
    ListBindingMatchingResourcesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.bindingmatchingresource.ListBindingMatchingResourcesResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.bindingmatchingresource.ListBindingMatchingResourcesRequest,
        response: google.cloud.backupdr_v1beta.types.bindingmatchingresource.ListBindingMatchingResourcesResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBindingMatchingResourcesAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBindingMatchingResourcesAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListBindingMatchingResourcesAsyncPager_ListBindingMatchingResourcesAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBindingMatchingResourcesPager
    
    
    ListBindingMatchingResourcesPager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1beta.types.bindingmatchingresource.ListBindingMatchingResourcesResponse,
        ],
        request: google.cloud.backupdr_v1beta.types.bindingmatchingresource.ListBindingMatchingResourcesRequest,
        response: google.cloud.backupdr_v1beta.types.bindingmatchingresource.ListBindingMatchingResourcesResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBindingMatchingResourcesPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListBindingMatchingResourcesPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListBindingMatchingResourcesPager_ListBindingMatchingResourcesPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourceReferencesAsyncPager
    
    
    ListDataSourceReferencesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.datasourcereference.ListDataSourceReferencesResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.datasourcereference.ListDataSourceReferencesRequest,
        response: google.cloud.backupdr_v1beta.types.datasourcereference.ListDataSourceReferencesResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourceReferencesAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourceReferencesAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListDataSourceReferencesAsyncPager_ListDataSourceReferencesAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourceReferencesPager
    
    
    ListDataSourceReferencesPager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1beta.types.datasourcereference.ListDataSourceReferencesResponse,
        ],
        request: google.cloud.backupdr_v1beta.types.datasourcereference.ListDataSourceReferencesRequest,
        response: google.cloud.backupdr_v1beta.types.datasourcereference.ListDataSourceReferencesResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourceReferencesPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourceReferencesPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListDataSourceReferencesPager_ListDataSourceReferencesPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourcesAsyncPager
    
    
    ListDataSourcesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.backupvault.ListDataSourcesResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.backupvault.ListDataSourcesRequest,
        response: google.cloud.backupdr_v1beta.types.backupvault.ListDataSourcesResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourcesAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourcesAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListDataSourcesAsyncPager_ListDataSourcesAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourcesPager
    
    
    ListDataSourcesPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1beta.types.backupvault.ListDataSourcesResponse
        ],
        request: google.cloud.backupdr_v1beta.types.backupvault.ListDataSourcesRequest,
        response: google.cloud.backupdr_v1beta.types.backupvault.ListDataSourcesResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourcesPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListDataSourcesPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListDataSourcesPager_ListDataSourcesPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListManagementServersAsyncPager
    
    
    ListManagementServersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.backupdr.ListManagementServersResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.backupdr.ListManagementServersRequest,
        response: google.cloud.backupdr_v1beta.types.backupdr.ListManagementServersResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListManagementServersAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListManagementServersAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListManagementServersAsyncPager_ListManagementServersAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListManagementServersPager
    
    
    ListManagementServersPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1beta.types.backupdr.ListManagementServersResponse
        ],
        request: google.cloud.backupdr_v1beta.types.backupdr.ListManagementServersRequest,
        response: google.cloud.backupdr_v1beta.types.backupdr.ListManagementServersResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListManagementServersPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr.pagers.ListManagementServersPager#google_cloud_backupdr_v1beta_services_backup_dr_pagers_ListManagementServersPager_ListManagementServersPager)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient
    
    
    BackupDrProtectionSummaryAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.transports.base.BackupDrProtectionSummaryTransport,
                typing.Callable[
                    [...],
                    google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.transports.base.BackupDrProtectionSummaryTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the backup dr protection summary async client.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_BackupDrProtectionSummaryAsyncClient)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_cancel_operation)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_common_billing_account_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_common_folder_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_common_location_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_common_organization_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_common_project_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.delete_operation
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_delete_operation)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_from_service_account_file)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_from_service_account_info)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_from_service_account_json)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_get_iam_policy)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_location
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_location](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_get_location)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_operation
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_get_operation)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.transports.base.BackupDrProtectionSummaryTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_get_transport_class)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.list_locations
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_list_locations)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.list_operations
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_list_operations)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.list_resource_backup_configs
    
    
    list_resource_backup_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.protection_summary.ListResourceBackupConfigsRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsAsyncPager
    )

Lists ResourceBackupConfigs.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.list_resource_backup_configs](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_list_resource_backup_configs)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_parse_common_billing_account_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_parse_common_folder_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_parse_common_location_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_parse_common_organization_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_parse_common_project_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_resource_backup_config_path
    
    
    parse_resource_backup_config_path(path: str) -> typing.Dict[str, str]

Parses a resource_backup_config path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.parse_resource_backup_config_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_parse_resource_backup_config_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.resource_backup_config_path
    
    
    resource_backup_config_path(
        project: str, location: str, resource_backup_config: str
    ) -> str

Returns a fully-qualified resource_backup_config string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.resource_backup_config_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_resource_backup_config_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_set_iam_policy)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryAsyncClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryAsyncClient_test_iam_permissions)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient
    
    
    BackupDrProtectionSummaryClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.transports.base.BackupDrProtectionSummaryTransport,
                typing.Callable[
                    [...],
                    google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.transports.base.BackupDrProtectionSummaryTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the backup dr protection summary client.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_BackupDrProtectionSummaryClient)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.**exit**](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient___exit__)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.cancel_operation
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.cancel_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_cancel_operation)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_common_billing_account_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_folder_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_common_folder_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_location_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_common_location_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_organization_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_common_organization_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.common_project_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_common_project_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.delete_operation
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.delete_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_delete_operation)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.from_service_account_file](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_from_service_account_file)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.from_service_account_info](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_from_service_account_info)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.from_service_account_json](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_from_service_account_json)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.get_iam_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_get_iam_policy)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.get_location
    
    
    get_location(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.GetLocationRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.Location

Gets information about a location.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.get_location](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_get_location)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_get_mtls_endpoint_and_cert_source)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.get_operation
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.get_operation](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_get_operation)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.list_locations
    
    
    list_locations(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.ListLocationsRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.ListLocationsResponse

Lists information about the supported locations for this service.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.list_locations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_list_locations)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.list_operations
    
    
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.list_operations](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_list_operations)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.list_resource_backup_configs
    
    
    list_resource_backup_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.backupdr_v1beta.types.protection_summary.ListResourceBackupConfigsRequest,
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
        google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsPager
    )

Lists ResourceBackupConfigs.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.list_resource_backup_configs](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_list_resource_backup_configs)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_parse_common_billing_account_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_parse_common_folder_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_parse_common_location_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_parse_common_organization_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_parse_common_project_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_resource_backup_config_path
    
    
    parse_resource_backup_config_path(path: str) -> typing.Dict[str, str]

Parses a resource_backup_config path into its component segments.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.parse_resource_backup_config_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_parse_resource_backup_config_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.resource_backup_config_path
    
    
    resource_backup_config_path(
        project: str, location: str, resource_backup_config: str
    ) -> str

Returns a fully-qualified resource_backup_config string.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.resource_backup_config_path](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_resource_backup_config_path)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.set_iam_policy](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_set_iam_policy)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.BackupDrProtectionSummaryClient#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_BackupDrProtectionSummaryClient_test_iam_permissions)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsAsyncPager
    
    
    ListResourceBackupConfigsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1beta.types.protection_summary.ListResourceBackupConfigsResponse
            ],
        ],
        request: google.cloud.backupdr_v1beta.types.protection_summary.ListResourceBackupConfigsRequest,
        response: google.cloud.backupdr_v1beta.types.protection_summary.ListResourceBackupConfigsResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsAsyncPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsAsyncPager#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_pagers_ListResourceBackupConfigsAsyncPager_ListResourceBackupConfigsAsyncPager)

### google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsPager
    
    
    ListResourceBackupConfigsPager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1beta.types.protection_summary.ListResourceBackupConfigsResponse,
        ],
        request: google.cloud.backupdr_v1beta.types.protection_summary.ListResourceBackupConfigsRequest,
        response: google.cloud.backupdr_v1beta.types.protection_summary.ListResourceBackupConfigsResponse,
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

See more: [google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsPager](https://cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.services.backup_dr_protection_summary.pagers.ListResourceBackupConfigsPager#google_cloud_backupdr_v1beta_services_backup_dr_protection_summary_pagers_ListResourceBackupConfigsPager_ListResourceBackupConfigsPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
