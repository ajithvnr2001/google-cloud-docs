---
url: https://docs.cloud.google.com/python/docs/reference/netapp/latest/summary_method/
title: Package Methods (0.10.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:07.169738+00:00
---

# Package Methods (0.10.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/netapp/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.10.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.2 (latest)  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.24  0.2.0  0.1.0 

Summary of entries of Methods for netapp.

## 

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient
    
    
    NetAppAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.netapp_v1.services.net_app.transports.base.NetAppTransport,
                typing.Callable[
                    [...],
                    google.cloud.netapp_v1.services.net_app.transports.base.NetAppTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the net app async client.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_NetAppAsyncClient)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.active_directory_path
    
    
    active_directory_path(project: str, location: str, active_directory: str) -> str

Returns a fully-qualified active_directory string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.active_directory_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_active_directory_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.backup_path
    
    
    backup_path(project: str, location: str, backup_vault: str, backup: str) -> str

Returns a fully-qualified backup string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.backup_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_backup_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.backup_policy_path
    
    
    backup_policy_path(project: str, location: str, backup_policy: str) -> str

Returns a fully-qualified backup_policy string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.backup_policy_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_backup_policy_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.backup_vault_path
    
    
    backup_vault_path(project: str, location: str, backup_vault: str) -> str

Returns a fully-qualified backup_vault string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.backup_vault_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_backup_vault_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_cancel_operation)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_common_billing_account_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_common_folder_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_common_location_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_common_organization_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_common_project_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_active_directory
    
    
    create_active_directory(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.active_directory.CreateActiveDirectoryRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        active_directory: typing.Optional[
            google.cloud.netapp_v1.types.active_directory.ActiveDirectory
        ] = None,
        active_directory_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

CreateActiveDirectory Creates the active directory specified in the request.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_active_directory](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_active_directory)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_backup
    
    
    create_backup(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.backup.CreateBackupRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup: typing.Optional[google.cloud.netapp_v1.types.backup.Backup] = None,
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

Creates a backup from the volume specified in the request The backup can be created from the given snapshot if specified in the request.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_backup](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_backup)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_backup_policy
    
    
    create_backup_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_policy.CreateBackupPolicyRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_policy: typing.Optional[
            google.cloud.netapp_v1.types.backup_policy.BackupPolicy
        ] = None,
        backup_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates new backup policy.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_backup_policy](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_backup_policy)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_backup_vault
    
    
    create_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_vault.CreateBackupVaultRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_vault: typing.Optional[
            google.cloud.netapp_v1.types.backup_vault.BackupVault
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

Creates new backup vault.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_backup_vault](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_backup_vault)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_host_group
    
    
    create_host_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.host_group.CreateHostGroupRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        host_group: typing.Optional[
            google.cloud.netapp_v1.types.host_group.HostGroup
        ] = None,
        host_group_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new host group.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_host_group](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_host_group)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_kms_config
    
    
    create_kms_config(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.CreateKmsConfigRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        kms_config: typing.Optional[google.cloud.netapp_v1.types.kms.KmsConfig] = None,
        kms_config_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new KMS config.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_kms_config](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_kms_config)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_quota_rule
    
    
    create_quota_rule(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.quota_rule.CreateQuotaRuleRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        quota_rule: typing.Optional[
            google.cloud.netapp_v1.types.quota_rule.QuotaRule
        ] = None,
        quota_rule_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new quota rule.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_quota_rule](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_quota_rule)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_replication
    
    
    create_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.CreateReplicationRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        replication: typing.Optional[
            google.cloud.netapp_v1.types.replication.Replication
        ] = None,
        replication_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Create a new replication for a volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_replication](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_replication)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_snapshot
    
    
    create_snapshot(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.snapshot.CreateSnapshotRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        snapshot: typing.Optional[google.cloud.netapp_v1.types.snapshot.Snapshot] = None,
        snapshot_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Create a new snapshot for a volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_snapshot](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_snapshot)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_storage_pool
    
    
    create_storage_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.CreateStoragePoolRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        storage_pool: typing.Optional[
            google.cloud.netapp_v1.types.storage_pool.StoragePool
        ] = None,
        storage_pool_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new storage pool.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_storage_pool](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_storage_pool)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_volume
    
    
    create_volume(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.CreateVolumeRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        volume: typing.Optional[google.cloud.netapp_v1.types.volume.Volume] = None,
        volume_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Volume in a given project and location.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.create_volume](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_create_volume)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_active_directory
    
    
    delete_active_directory(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.active_directory.DeleteActiveDirectoryRequest,
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

Delete the active directory specified in the request.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_active_directory](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_active_directory)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_backup
    
    
    delete_backup(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.backup.DeleteBackupRequest, dict]
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

Warning! This operation will permanently delete the backup.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_backup](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_backup)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_backup_policy
    
    
    delete_backup_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_policy.DeleteBackupPolicyRequest, dict
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

Warning! This operation will permanently delete the backup policy.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_backup_policy](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_backup_policy)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_backup_vault
    
    
    delete_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_vault.DeleteBackupVaultRequest, dict
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

Warning! This operation will permanently delete the backup vault.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_backup_vault](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_backup_vault)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_host_group
    
    
    delete_host_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.host_group.DeleteHostGroupRequest, dict
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

Deletes a host group.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_host_group](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_host_group)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_kms_config
    
    
    delete_kms_config(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.DeleteKmsConfigRequest, dict]
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

Warning! This operation will permanently delete the Kms config.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_kms_config](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_kms_config)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_operation
    
    
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

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_operation)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_quota_rule
    
    
    delete_quota_rule(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.quota_rule.DeleteQuotaRuleRequest, dict
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

Deletes a quota rule.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_quota_rule](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_quota_rule)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_replication
    
    
    delete_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.DeleteReplicationRequest, dict
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

Deletes a replication.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_replication](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_replication)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_snapshot
    
    
    delete_snapshot(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.snapshot.DeleteSnapshotRequest, dict]
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

Deletes a snapshot.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_snapshot](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_snapshot)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_storage_pool
    
    
    delete_storage_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.DeleteStoragePoolRequest, dict
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

Warning! This operation will permanently delete the storage pool.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_storage_pool](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_storage_pool)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_volume
    
    
    delete_volume(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.DeleteVolumeRequest, dict]
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

Deletes a single Volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.delete_volume](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_delete_volume)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.encrypt_volumes
    
    
    encrypt_volumes(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.EncryptVolumesRequest, dict]
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

Encrypt the existing volumes without CMEK encryption with the desired the KMS config for the whole region.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.encrypt_volumes](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_encrypt_volumes)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.establish_peering
    
    
    establish_peering(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.EstablishPeeringRequest, dict
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

Establish replication peering.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.establish_peering](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_establish_peering)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.establish_volume_peering
    
    
    establish_volume_peering(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.volume.EstablishVolumePeeringRequest, dict
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

Establish volume peering.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.establish_volume_peering](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_establish_volume_peering)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.execute_ontap_delete
    
    
    execute_ontap_delete(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.ontap.ExecuteOntapDeleteRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.ontap.ExecuteOntapDeleteResponse

`ExecuteOntapDelete` dispatches the ONTAP `DELETE` request to the `StoragePool` cluster.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.execute_ontap_delete](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_execute_ontap_delete)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.execute_ontap_get
    
    
    execute_ontap_get(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.ontap.ExecuteOntapGetRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.ontap.ExecuteOntapGetResponse

`ExecuteOntapGet` dispatches the ONTAP `GET` request to the `StoragePool` cluster.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.execute_ontap_get](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_execute_ontap_get)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.execute_ontap_patch
    
    
    execute_ontap_patch(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.ontap.ExecuteOntapPatchRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.ontap.ExecuteOntapPatchResponse

`ExecuteOntapPatch` dispatches the ONTAP `PATCH` request to the `StoragePool` cluster.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.execute_ontap_patch](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_execute_ontap_patch)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.execute_ontap_post
    
    
    execute_ontap_post(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.ontap.ExecuteOntapPostRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.ontap.ExecuteOntapPostResponse

`ExecuteOntapPost` dispatches the ONTAP `POST` request to the `StoragePool` cluster.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.execute_ontap_post](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_execute_ontap_post)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_from_service_account_file)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_from_service_account_info)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_from_service_account_json)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_active_directory
    
    
    get_active_directory(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.active_directory.GetActiveDirectoryRequest,
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
    ) -> google.cloud.netapp_v1.types.active_directory.ActiveDirectory

Describes a specified active directory.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_active_directory](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_active_directory)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_backup
    
    
    get_backup(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.backup.GetBackupRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.backup.Backup

Returns the description of the specified backup.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_backup](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_backup)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_backup_policy
    
    
    get_backup_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_policy.GetBackupPolicyRequest, dict
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
    ) -> google.cloud.netapp_v1.types.backup_policy.BackupPolicy

Returns the description of the specified backup policy by backup_policy_id.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_backup_policy](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_backup_policy)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_backup_vault
    
    
    get_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_vault.GetBackupVaultRequest, dict
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
    ) -> google.cloud.netapp_v1.types.backup_vault.BackupVault

Returns the description of the specified backup vault.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_backup_vault](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_backup_vault)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_host_group
    
    
    get_host_group(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.host_group.GetHostGroupRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.host_group.HostGroup

Returns details of the specified host group.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_host_group](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_host_group)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_kms_config
    
    
    get_kms_config(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.GetKmsConfigRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.kms.KmsConfig

Returns the description of the specified KMS config by kms_config_id.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_kms_config](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_kms_config)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_location
    
    
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

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_location](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_location)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_operation
    
    
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

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_operation)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_quota_rule
    
    
    get_quota_rule(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.quota_rule.GetQuotaRuleRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.quota_rule.QuotaRule

Returns details of the specified quota rule.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_quota_rule](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_quota_rule)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_replication
    
    
    get_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.GetReplicationRequest, dict
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
    ) -> google.cloud.netapp_v1.types.replication.Replication

Describe a replication for a volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_replication](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_replication)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_snapshot
    
    
    get_snapshot(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.snapshot.GetSnapshotRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.snapshot.Snapshot

Describe a snapshot for a volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_snapshot](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_snapshot)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_storage_pool
    
    
    get_storage_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.GetStoragePoolRequest, dict
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
    ) -> google.cloud.netapp_v1.types.storage_pool.StoragePool

Returns the description of the specified storage pool by poolId.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_storage_pool](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_storage_pool)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.netapp_v1.services.net_app.transports.base.NetAppTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_transport_class)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_volume
    
    
    get_volume(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.GetVolumeRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.volume.Volume

Gets details of a single Volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.get_volume](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_get_volume)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.host_group_path
    
    
    host_group_path(project: str, location: str, host_group: str) -> str

Returns a fully-qualified host_group string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.host_group_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_host_group_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.kms_config_path
    
    
    kms_config_path(project: str, location: str, kms_config: str) -> str

Returns a fully-qualified kms_config string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.kms_config_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_kms_config_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_active_directories
    
    
    list_active_directories(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.active_directory.ListActiveDirectoriesRequest,
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListActiveDirectoriesAsyncPager

Lists active directories.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_active_directories](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_active_directories)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_backup_policies
    
    
    list_backup_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_policy.ListBackupPoliciesRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListBackupPoliciesAsyncPager

Returns list of all available backup policies.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_backup_policies](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_backup_policies)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_backup_vaults
    
    
    list_backup_vaults(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_vault.ListBackupVaultsRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListBackupVaultsAsyncPager

Returns list of all available backup vaults.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_backup_vaults](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_backup_vaults)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_backups
    
    
    list_backups(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.backup.ListBackupsRequest, dict]
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListBackupsAsyncPager

Returns descriptions of all backups for a backupVault.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_backups](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_backups)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_host_groups
    
    
    list_host_groups(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.host_group.ListHostGroupsRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListHostGroupsAsyncPager

Returns a list of host groups in a `location`.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_host_groups](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_host_groups)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_kms_configs
    
    
    list_kms_configs(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.ListKmsConfigsRequest, dict]
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListKmsConfigsAsyncPager

Returns descriptions of all KMS configs owned by the caller.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_kms_configs](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_kms_configs)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_locations
    
    
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

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_locations)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_operations
    
    
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

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_operations)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_quota_rules
    
    
    list_quota_rules(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.quota_rule.ListQuotaRulesRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListQuotaRulesAsyncPager

Returns list of all quota rules in a location.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_quota_rules](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_quota_rules)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_replications
    
    
    list_replications(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.ListReplicationsRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListReplicationsAsyncPager

Returns descriptions of all replications for a volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_replications](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_replications)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_snapshots
    
    
    list_snapshots(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.snapshot.ListSnapshotsRequest, dict]
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListSnapshotsAsyncPager

Returns descriptions of all snapshots for a volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_snapshots](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_snapshots)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_storage_pools
    
    
    list_storage_pools(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.ListStoragePoolsRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListStoragePoolsAsyncPager

Returns descriptions of all storage pools owned by the caller.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_storage_pools](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_storage_pools)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_volumes
    
    
    list_volumes(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.ListVolumesRequest, dict]
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListVolumesAsyncPager

Lists Volumes in a given project.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.list_volumes](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_list_volumes)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.network_path
    
    
    network_path(project: str, network: str) -> str

Returns a fully-qualified network string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.network_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_network_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_active_directory_path
    
    
    parse_active_directory_path(path: str) -> typing.Dict[str, str]

Parses a active_directory path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_active_directory_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_active_directory_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_backup_path
    
    
    parse_backup_path(path: str) -> typing.Dict[str, str]

Parses a backup path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_backup_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_backup_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_backup_policy_path
    
    
    parse_backup_policy_path(path: str) -> typing.Dict[str, str]

Parses a backup_policy path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_backup_policy_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_backup_policy_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_backup_vault_path
    
    
    parse_backup_vault_path(path: str) -> typing.Dict[str, str]

Parses a backup_vault path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_backup_vault_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_backup_vault_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_common_billing_account_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_common_folder_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_common_location_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_common_organization_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_common_project_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_host_group_path
    
    
    parse_host_group_path(path: str) -> typing.Dict[str, str]

Parses a host_group path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_host_group_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_host_group_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_kms_config_path
    
    
    parse_kms_config_path(path: str) -> typing.Dict[str, str]

Parses a kms_config path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_kms_config_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_kms_config_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_network_path
    
    
    parse_network_path(path: str) -> typing.Dict[str, str]

Parses a network path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_network_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_network_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_quota_rule_path
    
    
    parse_quota_rule_path(path: str) -> typing.Dict[str, str]

Parses a quota_rule path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_quota_rule_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_quota_rule_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_replication_path
    
    
    parse_replication_path(path: str) -> typing.Dict[str, str]

Parses a replication path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_replication_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_replication_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_snapshot_path
    
    
    parse_snapshot_path(path: str) -> typing.Dict[str, str]

Parses a snapshot path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_snapshot_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_snapshot_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_storage_pool_path
    
    
    parse_storage_pool_path(path: str) -> typing.Dict[str, str]

Parses a storage_pool path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_storage_pool_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_storage_pool_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_volume_path
    
    
    parse_volume_path(path: str) -> typing.Dict[str, str]

Parses a volume path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.parse_volume_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_parse_volume_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.quota_rule_path
    
    
    quota_rule_path(project: str, location: str, volume: str, quota_rule: str) -> str

Returns a fully-qualified quota_rule string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.quota_rule_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_quota_rule_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.replication_path
    
    
    replication_path(project: str, location: str, volume: str, replication: str) -> str

Returns a fully-qualified replication string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.replication_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_replication_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.restore_backup_files
    
    
    restore_backup_files(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.volume.RestoreBackupFilesRequest, dict
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

Restore files from a backup to a volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.restore_backup_files](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_restore_backup_files)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.resume_replication
    
    
    resume_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.ResumeReplicationRequest, dict
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

Resume Cross Region Replication.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.resume_replication](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_resume_replication)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.reverse_replication_direction
    
    
    reverse_replication_direction(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.ReverseReplicationDirectionRequest,
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

Reverses direction of replication.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.reverse_replication_direction](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_reverse_replication_direction)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.revert_volume
    
    
    revert_volume(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.RevertVolumeRequest, dict]
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

Revert an existing volume to a specified snapshot.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.revert_volume](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_revert_volume)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.snapshot_path
    
    
    snapshot_path(project: str, location: str, volume: str, snapshot: str) -> str

Returns a fully-qualified snapshot string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.snapshot_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_snapshot_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.stop_replication
    
    
    stop_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.StopReplicationRequest, dict
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

Stop Cross Region Replication.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.stop_replication](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_stop_replication)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.storage_pool_path
    
    
    storage_pool_path(project: str, location: str, storage_pool: str) -> str

Returns a fully-qualified storage_pool string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.storage_pool_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_storage_pool_path)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.switch_active_replica_zone
    
    
    switch_active_replica_zone(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.SwitchActiveReplicaZoneRequest,
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

This operation will switch the active/replica zone for a regional storagePool.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.switch_active_replica_zone](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_switch_active_replica_zone)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.sync_replication
    
    
    sync_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.SyncReplicationRequest, dict
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

Syncs the replication.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.sync_replication](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_sync_replication)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_active_directory
    
    
    update_active_directory(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.active_directory.UpdateActiveDirectoryRequest,
                dict,
            ]
        ] = None,
        *,
        active_directory: typing.Optional[
            google.cloud.netapp_v1.types.active_directory.ActiveDirectory
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

Update the parameters of an active directories.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_active_directory](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_active_directory)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_backup
    
    
    update_backup(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.backup.UpdateBackupRequest, dict]
        ] = None,
        *,
        backup: typing.Optional[google.cloud.netapp_v1.types.backup.Backup] = None,
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

Update backup with full spec.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_backup](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_backup)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_backup_policy
    
    
    update_backup_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_policy.UpdateBackupPolicyRequest, dict
            ]
        ] = None,
        *,
        backup_policy: typing.Optional[
            google.cloud.netapp_v1.types.backup_policy.BackupPolicy
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

Updates settings of a specific backup policy.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_backup_policy](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_backup_policy)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_backup_vault
    
    
    update_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_vault.UpdateBackupVaultRequest, dict
            ]
        ] = None,
        *,
        backup_vault: typing.Optional[
            google.cloud.netapp_v1.types.backup_vault.BackupVault
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

Updates the settings of a specific backup vault.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_backup_vault](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_backup_vault)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_host_group
    
    
    update_host_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.host_group.UpdateHostGroupRequest, dict
            ]
        ] = None,
        *,
        host_group: typing.Optional[
            google.cloud.netapp_v1.types.host_group.HostGroup
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

Updates an existing host group.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_host_group](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_host_group)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_kms_config
    
    
    update_kms_config(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.UpdateKmsConfigRequest, dict]
        ] = None,
        *,
        kms_config: typing.Optional[google.cloud.netapp_v1.types.kms.KmsConfig] = None,
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

Updates the Kms config properties with the full spec.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_kms_config](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_kms_config)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_quota_rule
    
    
    update_quota_rule(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.quota_rule.UpdateQuotaRuleRequest, dict
            ]
        ] = None,
        *,
        quota_rule: typing.Optional[
            google.cloud.netapp_v1.types.quota_rule.QuotaRule
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

Updates a quota rule.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_quota_rule](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_quota_rule)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_replication
    
    
    update_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.UpdateReplicationRequest, dict
            ]
        ] = None,
        *,
        replication: typing.Optional[
            google.cloud.netapp_v1.types.replication.Replication
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

Updates the settings of a specific replication.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_replication](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_replication)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_snapshot
    
    
    update_snapshot(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.snapshot.UpdateSnapshotRequest, dict]
        ] = None,
        *,
        snapshot: typing.Optional[google.cloud.netapp_v1.types.snapshot.Snapshot] = None,
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

Updates the settings of a specific snapshot.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_snapshot](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_snapshot)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_storage_pool
    
    
    update_storage_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.UpdateStoragePoolRequest, dict
            ]
        ] = None,
        *,
        storage_pool: typing.Optional[
            google.cloud.netapp_v1.types.storage_pool.StoragePool
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

Updates the storage pool properties with the full spec.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_storage_pool](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_storage_pool)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_volume
    
    
    update_volume(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.UpdateVolumeRequest, dict]
        ] = None,
        *,
        volume: typing.Optional[google.cloud.netapp_v1.types.volume.Volume] = None,
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

Updates the parameters of a single Volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.update_volume](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_update_volume)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.validate_directory_service
    
    
    validate_directory_service(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.ValidateDirectoryServiceRequest,
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

ValidateDirectoryService does a connectivity check for a directory service policy attached to the storage pool.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.validate_directory_service](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_validate_directory_service)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.verify_kms_config
    
    
    verify_kms_config(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.VerifyKmsConfigRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.kms.VerifyKmsConfigResponse

Verifies KMS config reachability.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.verify_kms_config](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_verify_kms_config)

### google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.volume_path
    
    
    volume_path(project: str, location: str, volume: str) -> str

Returns a fully-qualified volume string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppAsyncClient.volume_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppAsyncClient#google_cloud_netapp_v1_services_net_app_NetAppAsyncClient_volume_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient
    
    
    NetAppClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.netapp_v1.services.net_app.transports.base.NetAppTransport,
                typing.Callable[
                    [...],
                    google.cloud.netapp_v1.services.net_app.transports.base.NetAppTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the net app client.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_NetAppClient)

### google.cloud.netapp_v1.services.net_app.NetAppClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.**exit**](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient___exit__)

### google.cloud.netapp_v1.services.net_app.NetAppClient.active_directory_path
    
    
    active_directory_path(project: str, location: str, active_directory: str) -> str

Returns a fully-qualified active_directory string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.active_directory_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_active_directory_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.backup_path
    
    
    backup_path(project: str, location: str, backup_vault: str, backup: str) -> str

Returns a fully-qualified backup string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.backup_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_backup_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.backup_policy_path
    
    
    backup_policy_path(project: str, location: str, backup_policy: str) -> str

Returns a fully-qualified backup_policy string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.backup_policy_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_backup_policy_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.backup_vault_path
    
    
    backup_vault_path(project: str, location: str, backup_vault: str) -> str

Returns a fully-qualified backup_vault string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.backup_vault_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_backup_vault_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.cancel_operation
    
    
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

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.cancel_operation](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_cancel_operation)

### google.cloud.netapp_v1.services.net_app.NetAppClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_common_billing_account_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.common_folder_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_common_folder_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.common_location_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_common_location_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.common_organization_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_common_organization_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.common_project_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_common_project_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.create_active_directory
    
    
    create_active_directory(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.active_directory.CreateActiveDirectoryRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        active_directory: typing.Optional[
            google.cloud.netapp_v1.types.active_directory.ActiveDirectory
        ] = None,
        active_directory_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

CreateActiveDirectory Creates the active directory specified in the request.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.create_active_directory](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_create_active_directory)

### google.cloud.netapp_v1.services.net_app.NetAppClient.create_backup
    
    
    create_backup(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.backup.CreateBackupRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup: typing.Optional[google.cloud.netapp_v1.types.backup.Backup] = None,
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

Creates a backup from the volume specified in the request The backup can be created from the given snapshot if specified in the request.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.create_backup](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_create_backup)

### google.cloud.netapp_v1.services.net_app.NetAppClient.create_backup_policy
    
    
    create_backup_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_policy.CreateBackupPolicyRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_policy: typing.Optional[
            google.cloud.netapp_v1.types.backup_policy.BackupPolicy
        ] = None,
        backup_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates new backup policy.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.create_backup_policy](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_create_backup_policy)

### google.cloud.netapp_v1.services.net_app.NetAppClient.create_backup_vault
    
    
    create_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_vault.CreateBackupVaultRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup_vault: typing.Optional[
            google.cloud.netapp_v1.types.backup_vault.BackupVault
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

Creates new backup vault.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.create_backup_vault](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_create_backup_vault)

### google.cloud.netapp_v1.services.net_app.NetAppClient.create_host_group
    
    
    create_host_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.host_group.CreateHostGroupRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        host_group: typing.Optional[
            google.cloud.netapp_v1.types.host_group.HostGroup
        ] = None,
        host_group_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new host group.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.create_host_group](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_create_host_group)

### google.cloud.netapp_v1.services.net_app.NetAppClient.create_kms_config
    
    
    create_kms_config(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.CreateKmsConfigRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        kms_config: typing.Optional[google.cloud.netapp_v1.types.kms.KmsConfig] = None,
        kms_config_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new KMS config.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.create_kms_config](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_create_kms_config)

### google.cloud.netapp_v1.services.net_app.NetAppClient.create_quota_rule
    
    
    create_quota_rule(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.quota_rule.CreateQuotaRuleRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        quota_rule: typing.Optional[
            google.cloud.netapp_v1.types.quota_rule.QuotaRule
        ] = None,
        quota_rule_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new quota rule.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.create_quota_rule](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_create_quota_rule)

### google.cloud.netapp_v1.services.net_app.NetAppClient.create_replication
    
    
    create_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.CreateReplicationRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        replication: typing.Optional[
            google.cloud.netapp_v1.types.replication.Replication
        ] = None,
        replication_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Create a new replication for a volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.create_replication](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_create_replication)

### google.cloud.netapp_v1.services.net_app.NetAppClient.create_snapshot
    
    
    create_snapshot(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.snapshot.CreateSnapshotRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        snapshot: typing.Optional[google.cloud.netapp_v1.types.snapshot.Snapshot] = None,
        snapshot_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Create a new snapshot for a volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.create_snapshot](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_create_snapshot)

### google.cloud.netapp_v1.services.net_app.NetAppClient.create_storage_pool
    
    
    create_storage_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.CreateStoragePoolRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        storage_pool: typing.Optional[
            google.cloud.netapp_v1.types.storage_pool.StoragePool
        ] = None,
        storage_pool_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new storage pool.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.create_storage_pool](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_create_storage_pool)

### google.cloud.netapp_v1.services.net_app.NetAppClient.create_volume
    
    
    create_volume(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.CreateVolumeRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        volume: typing.Optional[google.cloud.netapp_v1.types.volume.Volume] = None,
        volume_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Volume in a given project and location.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.create_volume](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_create_volume)

### google.cloud.netapp_v1.services.net_app.NetAppClient.delete_active_directory
    
    
    delete_active_directory(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.active_directory.DeleteActiveDirectoryRequest,
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

Delete the active directory specified in the request.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.delete_active_directory](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_delete_active_directory)

### google.cloud.netapp_v1.services.net_app.NetAppClient.delete_backup
    
    
    delete_backup(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.backup.DeleteBackupRequest, dict]
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

Warning! This operation will permanently delete the backup.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.delete_backup](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_delete_backup)

### google.cloud.netapp_v1.services.net_app.NetAppClient.delete_backup_policy
    
    
    delete_backup_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_policy.DeleteBackupPolicyRequest, dict
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

Warning! This operation will permanently delete the backup policy.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.delete_backup_policy](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_delete_backup_policy)

### google.cloud.netapp_v1.services.net_app.NetAppClient.delete_backup_vault
    
    
    delete_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_vault.DeleteBackupVaultRequest, dict
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

Warning! This operation will permanently delete the backup vault.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.delete_backup_vault](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_delete_backup_vault)

### google.cloud.netapp_v1.services.net_app.NetAppClient.delete_host_group
    
    
    delete_host_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.host_group.DeleteHostGroupRequest, dict
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

Deletes a host group.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.delete_host_group](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_delete_host_group)

### google.cloud.netapp_v1.services.net_app.NetAppClient.delete_kms_config
    
    
    delete_kms_config(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.DeleteKmsConfigRequest, dict]
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

Warning! This operation will permanently delete the Kms config.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.delete_kms_config](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_delete_kms_config)

### google.cloud.netapp_v1.services.net_app.NetAppClient.delete_operation
    
    
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

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.delete_operation](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_delete_operation)

### google.cloud.netapp_v1.services.net_app.NetAppClient.delete_quota_rule
    
    
    delete_quota_rule(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.quota_rule.DeleteQuotaRuleRequest, dict
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

Deletes a quota rule.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.delete_quota_rule](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_delete_quota_rule)

### google.cloud.netapp_v1.services.net_app.NetAppClient.delete_replication
    
    
    delete_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.DeleteReplicationRequest, dict
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

Deletes a replication.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.delete_replication](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_delete_replication)

### google.cloud.netapp_v1.services.net_app.NetAppClient.delete_snapshot
    
    
    delete_snapshot(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.snapshot.DeleteSnapshotRequest, dict]
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

Deletes a snapshot.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.delete_snapshot](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_delete_snapshot)

### google.cloud.netapp_v1.services.net_app.NetAppClient.delete_storage_pool
    
    
    delete_storage_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.DeleteStoragePoolRequest, dict
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

Warning! This operation will permanently delete the storage pool.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.delete_storage_pool](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_delete_storage_pool)

### google.cloud.netapp_v1.services.net_app.NetAppClient.delete_volume
    
    
    delete_volume(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.DeleteVolumeRequest, dict]
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

Deletes a single Volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.delete_volume](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_delete_volume)

### google.cloud.netapp_v1.services.net_app.NetAppClient.encrypt_volumes
    
    
    encrypt_volumes(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.EncryptVolumesRequest, dict]
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

Encrypt the existing volumes without CMEK encryption with the desired the KMS config for the whole region.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.encrypt_volumes](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_encrypt_volumes)

### google.cloud.netapp_v1.services.net_app.NetAppClient.establish_peering
    
    
    establish_peering(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.EstablishPeeringRequest, dict
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

Establish replication peering.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.establish_peering](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_establish_peering)

### google.cloud.netapp_v1.services.net_app.NetAppClient.establish_volume_peering
    
    
    establish_volume_peering(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.volume.EstablishVolumePeeringRequest, dict
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

Establish volume peering.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.establish_volume_peering](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_establish_volume_peering)

### google.cloud.netapp_v1.services.net_app.NetAppClient.execute_ontap_delete
    
    
    execute_ontap_delete(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.ontap.ExecuteOntapDeleteRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.ontap.ExecuteOntapDeleteResponse

`ExecuteOntapDelete` dispatches the ONTAP `DELETE` request to the `StoragePool` cluster.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.execute_ontap_delete](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_execute_ontap_delete)

### google.cloud.netapp_v1.services.net_app.NetAppClient.execute_ontap_get
    
    
    execute_ontap_get(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.ontap.ExecuteOntapGetRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.ontap.ExecuteOntapGetResponse

`ExecuteOntapGet` dispatches the ONTAP `GET` request to the `StoragePool` cluster.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.execute_ontap_get](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_execute_ontap_get)

### google.cloud.netapp_v1.services.net_app.NetAppClient.execute_ontap_patch
    
    
    execute_ontap_patch(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.ontap.ExecuteOntapPatchRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.ontap.ExecuteOntapPatchResponse

`ExecuteOntapPatch` dispatches the ONTAP `PATCH` request to the `StoragePool` cluster.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.execute_ontap_patch](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_execute_ontap_patch)

### google.cloud.netapp_v1.services.net_app.NetAppClient.execute_ontap_post
    
    
    execute_ontap_post(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.ontap.ExecuteOntapPostRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.ontap.ExecuteOntapPostResponse

`ExecuteOntapPost` dispatches the ONTAP `POST` request to the `StoragePool` cluster.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.execute_ontap_post](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_execute_ontap_post)

### google.cloud.netapp_v1.services.net_app.NetAppClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.from_service_account_file](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_from_service_account_file)

### google.cloud.netapp_v1.services.net_app.NetAppClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.from_service_account_info](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_from_service_account_info)

### google.cloud.netapp_v1.services.net_app.NetAppClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.from_service_account_json](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_from_service_account_json)

### google.cloud.netapp_v1.services.net_app.NetAppClient.get_active_directory
    
    
    get_active_directory(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.active_directory.GetActiveDirectoryRequest,
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
    ) -> google.cloud.netapp_v1.types.active_directory.ActiveDirectory

Describes a specified active directory.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.get_active_directory](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_get_active_directory)

### google.cloud.netapp_v1.services.net_app.NetAppClient.get_backup
    
    
    get_backup(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.backup.GetBackupRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.backup.Backup

Returns the description of the specified backup.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.get_backup](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_get_backup)

### google.cloud.netapp_v1.services.net_app.NetAppClient.get_backup_policy
    
    
    get_backup_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_policy.GetBackupPolicyRequest, dict
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
    ) -> google.cloud.netapp_v1.types.backup_policy.BackupPolicy

Returns the description of the specified backup policy by backup_policy_id.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.get_backup_policy](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_get_backup_policy)

### google.cloud.netapp_v1.services.net_app.NetAppClient.get_backup_vault
    
    
    get_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_vault.GetBackupVaultRequest, dict
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
    ) -> google.cloud.netapp_v1.types.backup_vault.BackupVault

Returns the description of the specified backup vault.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.get_backup_vault](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_get_backup_vault)

### google.cloud.netapp_v1.services.net_app.NetAppClient.get_host_group
    
    
    get_host_group(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.host_group.GetHostGroupRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.host_group.HostGroup

Returns details of the specified host group.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.get_host_group](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_get_host_group)

### google.cloud.netapp_v1.services.net_app.NetAppClient.get_kms_config
    
    
    get_kms_config(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.GetKmsConfigRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.kms.KmsConfig

Returns the description of the specified KMS config by kms_config_id.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.get_kms_config](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_get_kms_config)

### google.cloud.netapp_v1.services.net_app.NetAppClient.get_location
    
    
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

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.get_location](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_get_location)

### google.cloud.netapp_v1.services.net_app.NetAppClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_get_mtls_endpoint_and_cert_source)

### google.cloud.netapp_v1.services.net_app.NetAppClient.get_operation
    
    
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

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.get_operation](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_get_operation)

### google.cloud.netapp_v1.services.net_app.NetAppClient.get_quota_rule
    
    
    get_quota_rule(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.quota_rule.GetQuotaRuleRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.quota_rule.QuotaRule

Returns details of the specified quota rule.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.get_quota_rule](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_get_quota_rule)

### google.cloud.netapp_v1.services.net_app.NetAppClient.get_replication
    
    
    get_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.GetReplicationRequest, dict
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
    ) -> google.cloud.netapp_v1.types.replication.Replication

Describe a replication for a volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.get_replication](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_get_replication)

### google.cloud.netapp_v1.services.net_app.NetAppClient.get_snapshot
    
    
    get_snapshot(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.snapshot.GetSnapshotRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.snapshot.Snapshot

Describe a snapshot for a volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.get_snapshot](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_get_snapshot)

### google.cloud.netapp_v1.services.net_app.NetAppClient.get_storage_pool
    
    
    get_storage_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.GetStoragePoolRequest, dict
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
    ) -> google.cloud.netapp_v1.types.storage_pool.StoragePool

Returns the description of the specified storage pool by poolId.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.get_storage_pool](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_get_storage_pool)

### google.cloud.netapp_v1.services.net_app.NetAppClient.get_volume
    
    
    get_volume(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.GetVolumeRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.volume.Volume

Gets details of a single Volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.get_volume](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_get_volume)

### google.cloud.netapp_v1.services.net_app.NetAppClient.host_group_path
    
    
    host_group_path(project: str, location: str, host_group: str) -> str

Returns a fully-qualified host_group string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.host_group_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_host_group_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.kms_config_path
    
    
    kms_config_path(project: str, location: str, kms_config: str) -> str

Returns a fully-qualified kms_config string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.kms_config_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_kms_config_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.list_active_directories
    
    
    list_active_directories(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.active_directory.ListActiveDirectoriesRequest,
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListActiveDirectoriesPager

Lists active directories.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.list_active_directories](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_list_active_directories)

### google.cloud.netapp_v1.services.net_app.NetAppClient.list_backup_policies
    
    
    list_backup_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_policy.ListBackupPoliciesRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListBackupPoliciesPager

Returns list of all available backup policies.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.list_backup_policies](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_list_backup_policies)

### google.cloud.netapp_v1.services.net_app.NetAppClient.list_backup_vaults
    
    
    list_backup_vaults(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_vault.ListBackupVaultsRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListBackupVaultsPager

Returns list of all available backup vaults.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.list_backup_vaults](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_list_backup_vaults)

### google.cloud.netapp_v1.services.net_app.NetAppClient.list_backups
    
    
    list_backups(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.backup.ListBackupsRequest, dict]
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListBackupsPager

Returns descriptions of all backups for a backupVault.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.list_backups](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_list_backups)

### google.cloud.netapp_v1.services.net_app.NetAppClient.list_host_groups
    
    
    list_host_groups(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.host_group.ListHostGroupsRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListHostGroupsPager

Returns a list of host groups in a `location`.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.list_host_groups](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_list_host_groups)

### google.cloud.netapp_v1.services.net_app.NetAppClient.list_kms_configs
    
    
    list_kms_configs(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.ListKmsConfigsRequest, dict]
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListKmsConfigsPager

Returns descriptions of all KMS configs owned by the caller.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.list_kms_configs](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_list_kms_configs)

### google.cloud.netapp_v1.services.net_app.NetAppClient.list_locations
    
    
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

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.list_locations](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_list_locations)

### google.cloud.netapp_v1.services.net_app.NetAppClient.list_operations
    
    
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

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.list_operations](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_list_operations)

### google.cloud.netapp_v1.services.net_app.NetAppClient.list_quota_rules
    
    
    list_quota_rules(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.quota_rule.ListQuotaRulesRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListQuotaRulesPager

Returns list of all quota rules in a location.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.list_quota_rules](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_list_quota_rules)

### google.cloud.netapp_v1.services.net_app.NetAppClient.list_replications
    
    
    list_replications(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.ListReplicationsRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListReplicationsPager

Returns descriptions of all replications for a volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.list_replications](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_list_replications)

### google.cloud.netapp_v1.services.net_app.NetAppClient.list_snapshots
    
    
    list_snapshots(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.snapshot.ListSnapshotsRequest, dict]
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListSnapshotsPager

Returns descriptions of all snapshots for a volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.list_snapshots](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_list_snapshots)

### google.cloud.netapp_v1.services.net_app.NetAppClient.list_storage_pools
    
    
    list_storage_pools(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.ListStoragePoolsRequest, dict
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListStoragePoolsPager

Returns descriptions of all storage pools owned by the caller.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.list_storage_pools](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_list_storage_pools)

### google.cloud.netapp_v1.services.net_app.NetAppClient.list_volumes
    
    
    list_volumes(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.ListVolumesRequest, dict]
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
    ) -> google.cloud.netapp_v1.services.net_app.pagers.ListVolumesPager

Lists Volumes in a given project.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.list_volumes](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_list_volumes)

### google.cloud.netapp_v1.services.net_app.NetAppClient.network_path
    
    
    network_path(project: str, network: str) -> str

Returns a fully-qualified network string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.network_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_network_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_active_directory_path
    
    
    parse_active_directory_path(path: str) -> typing.Dict[str, str]

Parses a active_directory path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_active_directory_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_active_directory_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_backup_path
    
    
    parse_backup_path(path: str) -> typing.Dict[str, str]

Parses a backup path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_backup_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_backup_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_backup_policy_path
    
    
    parse_backup_policy_path(path: str) -> typing.Dict[str, str]

Parses a backup_policy path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_backup_policy_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_backup_policy_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_backup_vault_path
    
    
    parse_backup_vault_path(path: str) -> typing.Dict[str, str]

Parses a backup_vault path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_backup_vault_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_backup_vault_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_common_billing_account_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_common_folder_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_common_location_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_common_organization_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_common_project_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_host_group_path
    
    
    parse_host_group_path(path: str) -> typing.Dict[str, str]

Parses a host_group path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_host_group_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_host_group_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_kms_config_path
    
    
    parse_kms_config_path(path: str) -> typing.Dict[str, str]

Parses a kms_config path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_kms_config_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_kms_config_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_network_path
    
    
    parse_network_path(path: str) -> typing.Dict[str, str]

Parses a network path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_network_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_network_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_quota_rule_path
    
    
    parse_quota_rule_path(path: str) -> typing.Dict[str, str]

Parses a quota_rule path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_quota_rule_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_quota_rule_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_replication_path
    
    
    parse_replication_path(path: str) -> typing.Dict[str, str]

Parses a replication path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_replication_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_replication_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_snapshot_path
    
    
    parse_snapshot_path(path: str) -> typing.Dict[str, str]

Parses a snapshot path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_snapshot_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_snapshot_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_storage_pool_path
    
    
    parse_storage_pool_path(path: str) -> typing.Dict[str, str]

Parses a storage_pool path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_storage_pool_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_storage_pool_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.parse_volume_path
    
    
    parse_volume_path(path: str) -> typing.Dict[str, str]

Parses a volume path into its component segments.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.parse_volume_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_parse_volume_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.quota_rule_path
    
    
    quota_rule_path(project: str, location: str, volume: str, quota_rule: str) -> str

Returns a fully-qualified quota_rule string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.quota_rule_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_quota_rule_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.replication_path
    
    
    replication_path(project: str, location: str, volume: str, replication: str) -> str

Returns a fully-qualified replication string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.replication_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_replication_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.restore_backup_files
    
    
    restore_backup_files(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.volume.RestoreBackupFilesRequest, dict
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

Restore files from a backup to a volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.restore_backup_files](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_restore_backup_files)

### google.cloud.netapp_v1.services.net_app.NetAppClient.resume_replication
    
    
    resume_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.ResumeReplicationRequest, dict
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

Resume Cross Region Replication.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.resume_replication](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_resume_replication)

### google.cloud.netapp_v1.services.net_app.NetAppClient.reverse_replication_direction
    
    
    reverse_replication_direction(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.ReverseReplicationDirectionRequest,
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

Reverses direction of replication.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.reverse_replication_direction](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_reverse_replication_direction)

### google.cloud.netapp_v1.services.net_app.NetAppClient.revert_volume
    
    
    revert_volume(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.RevertVolumeRequest, dict]
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

Revert an existing volume to a specified snapshot.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.revert_volume](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_revert_volume)

### google.cloud.netapp_v1.services.net_app.NetAppClient.snapshot_path
    
    
    snapshot_path(project: str, location: str, volume: str, snapshot: str) -> str

Returns a fully-qualified snapshot string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.snapshot_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_snapshot_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.stop_replication
    
    
    stop_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.StopReplicationRequest, dict
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

Stop Cross Region Replication.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.stop_replication](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_stop_replication)

### google.cloud.netapp_v1.services.net_app.NetAppClient.storage_pool_path
    
    
    storage_pool_path(project: str, location: str, storage_pool: str) -> str

Returns a fully-qualified storage_pool string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.storage_pool_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_storage_pool_path)

### google.cloud.netapp_v1.services.net_app.NetAppClient.switch_active_replica_zone
    
    
    switch_active_replica_zone(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.SwitchActiveReplicaZoneRequest,
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

This operation will switch the active/replica zone for a regional storagePool.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.switch_active_replica_zone](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_switch_active_replica_zone)

### google.cloud.netapp_v1.services.net_app.NetAppClient.sync_replication
    
    
    sync_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.SyncReplicationRequest, dict
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

Syncs the replication.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.sync_replication](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_sync_replication)

### google.cloud.netapp_v1.services.net_app.NetAppClient.update_active_directory
    
    
    update_active_directory(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.active_directory.UpdateActiveDirectoryRequest,
                dict,
            ]
        ] = None,
        *,
        active_directory: typing.Optional[
            google.cloud.netapp_v1.types.active_directory.ActiveDirectory
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

Update the parameters of an active directories.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.update_active_directory](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_update_active_directory)

### google.cloud.netapp_v1.services.net_app.NetAppClient.update_backup
    
    
    update_backup(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.backup.UpdateBackupRequest, dict]
        ] = None,
        *,
        backup: typing.Optional[google.cloud.netapp_v1.types.backup.Backup] = None,
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

Update backup with full spec.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.update_backup](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_update_backup)

### google.cloud.netapp_v1.services.net_app.NetAppClient.update_backup_policy
    
    
    update_backup_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_policy.UpdateBackupPolicyRequest, dict
            ]
        ] = None,
        *,
        backup_policy: typing.Optional[
            google.cloud.netapp_v1.types.backup_policy.BackupPolicy
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

Updates settings of a specific backup policy.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.update_backup_policy](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_update_backup_policy)

### google.cloud.netapp_v1.services.net_app.NetAppClient.update_backup_vault
    
    
    update_backup_vault(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.backup_vault.UpdateBackupVaultRequest, dict
            ]
        ] = None,
        *,
        backup_vault: typing.Optional[
            google.cloud.netapp_v1.types.backup_vault.BackupVault
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

Updates the settings of a specific backup vault.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.update_backup_vault](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_update_backup_vault)

### google.cloud.netapp_v1.services.net_app.NetAppClient.update_host_group
    
    
    update_host_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.host_group.UpdateHostGroupRequest, dict
            ]
        ] = None,
        *,
        host_group: typing.Optional[
            google.cloud.netapp_v1.types.host_group.HostGroup
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

Updates an existing host group.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.update_host_group](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_update_host_group)

### google.cloud.netapp_v1.services.net_app.NetAppClient.update_kms_config
    
    
    update_kms_config(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.UpdateKmsConfigRequest, dict]
        ] = None,
        *,
        kms_config: typing.Optional[google.cloud.netapp_v1.types.kms.KmsConfig] = None,
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

Updates the Kms config properties with the full spec.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.update_kms_config](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_update_kms_config)

### google.cloud.netapp_v1.services.net_app.NetAppClient.update_quota_rule
    
    
    update_quota_rule(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.quota_rule.UpdateQuotaRuleRequest, dict
            ]
        ] = None,
        *,
        quota_rule: typing.Optional[
            google.cloud.netapp_v1.types.quota_rule.QuotaRule
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

Updates a quota rule.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.update_quota_rule](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_update_quota_rule)

### google.cloud.netapp_v1.services.net_app.NetAppClient.update_replication
    
    
    update_replication(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.replication.UpdateReplicationRequest, dict
            ]
        ] = None,
        *,
        replication: typing.Optional[
            google.cloud.netapp_v1.types.replication.Replication
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

Updates the settings of a specific replication.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.update_replication](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_update_replication)

### google.cloud.netapp_v1.services.net_app.NetAppClient.update_snapshot
    
    
    update_snapshot(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.snapshot.UpdateSnapshotRequest, dict]
        ] = None,
        *,
        snapshot: typing.Optional[google.cloud.netapp_v1.types.snapshot.Snapshot] = None,
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

Updates the settings of a specific snapshot.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.update_snapshot](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_update_snapshot)

### google.cloud.netapp_v1.services.net_app.NetAppClient.update_storage_pool
    
    
    update_storage_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.UpdateStoragePoolRequest, dict
            ]
        ] = None,
        *,
        storage_pool: typing.Optional[
            google.cloud.netapp_v1.types.storage_pool.StoragePool
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

Updates the storage pool properties with the full spec.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.update_storage_pool](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_update_storage_pool)

### google.cloud.netapp_v1.services.net_app.NetAppClient.update_volume
    
    
    update_volume(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.volume.UpdateVolumeRequest, dict]
        ] = None,
        *,
        volume: typing.Optional[google.cloud.netapp_v1.types.volume.Volume] = None,
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

Updates the parameters of a single Volume.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.update_volume](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_update_volume)

### google.cloud.netapp_v1.services.net_app.NetAppClient.validate_directory_service
    
    
    validate_directory_service(
        request: typing.Optional[
            typing.Union[
                google.cloud.netapp_v1.types.storage_pool.ValidateDirectoryServiceRequest,
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

ValidateDirectoryService does a connectivity check for a directory service policy attached to the storage pool.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.validate_directory_service](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_validate_directory_service)

### google.cloud.netapp_v1.services.net_app.NetAppClient.verify_kms_config
    
    
    verify_kms_config(
        request: typing.Optional[
            typing.Union[google.cloud.netapp_v1.types.kms.VerifyKmsConfigRequest, dict]
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
    ) -> google.cloud.netapp_v1.types.kms.VerifyKmsConfigResponse

Verifies KMS config reachability.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.verify_kms_config](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_verify_kms_config)

### google.cloud.netapp_v1.services.net_app.NetAppClient.volume_path
    
    
    volume_path(project: str, location: str, volume: str) -> str

Returns a fully-qualified volume string.

See more: [google.cloud.netapp_v1.services.net_app.NetAppClient.volume_path](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.NetAppClient#google_cloud_netapp_v1_services_net_app_NetAppClient_volume_path)

### google.cloud.netapp_v1.services.net_app.pagers.ListActiveDirectoriesAsyncPager
    
    
    ListActiveDirectoriesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.netapp_v1.types.active_directory.ListActiveDirectoriesResponse
            ],
        ],
        request: google.cloud.netapp_v1.types.active_directory.ListActiveDirectoriesRequest,
        response: google.cloud.netapp_v1.types.active_directory.ListActiveDirectoriesResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListActiveDirectoriesAsyncPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListActiveDirectoriesAsyncPager#google_cloud_netapp_v1_services_net_app_pagers_ListActiveDirectoriesAsyncPager_ListActiveDirectoriesAsyncPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListActiveDirectoriesPager
    
    
    ListActiveDirectoriesPager(
        method: typing.Callable[
            [...],
            google.cloud.netapp_v1.types.active_directory.ListActiveDirectoriesResponse,
        ],
        request: google.cloud.netapp_v1.types.active_directory.ListActiveDirectoriesRequest,
        response: google.cloud.netapp_v1.types.active_directory.ListActiveDirectoriesResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListActiveDirectoriesPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListActiveDirectoriesPager#google_cloud_netapp_v1_services_net_app_pagers_ListActiveDirectoriesPager_ListActiveDirectoriesPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListBackupPoliciesAsyncPager
    
    
    ListBackupPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.netapp_v1.types.backup_policy.ListBackupPoliciesResponse
            ],
        ],
        request: google.cloud.netapp_v1.types.backup_policy.ListBackupPoliciesRequest,
        response: google.cloud.netapp_v1.types.backup_policy.ListBackupPoliciesResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListBackupPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListBackupPoliciesAsyncPager#google_cloud_netapp_v1_services_net_app_pagers_ListBackupPoliciesAsyncPager_ListBackupPoliciesAsyncPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListBackupPoliciesPager
    
    
    ListBackupPoliciesPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.backup_policy.ListBackupPoliciesResponse
        ],
        request: google.cloud.netapp_v1.types.backup_policy.ListBackupPoliciesRequest,
        response: google.cloud.netapp_v1.types.backup_policy.ListBackupPoliciesResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListBackupPoliciesPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListBackupPoliciesPager#google_cloud_netapp_v1_services_net_app_pagers_ListBackupPoliciesPager_ListBackupPoliciesPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListBackupVaultsAsyncPager
    
    
    ListBackupVaultsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.netapp_v1.types.backup_vault.ListBackupVaultsResponse
            ],
        ],
        request: google.cloud.netapp_v1.types.backup_vault.ListBackupVaultsRequest,
        response: google.cloud.netapp_v1.types.backup_vault.ListBackupVaultsResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListBackupVaultsAsyncPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListBackupVaultsAsyncPager#google_cloud_netapp_v1_services_net_app_pagers_ListBackupVaultsAsyncPager_ListBackupVaultsAsyncPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListBackupVaultsPager
    
    
    ListBackupVaultsPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.backup_vault.ListBackupVaultsResponse
        ],
        request: google.cloud.netapp_v1.types.backup_vault.ListBackupVaultsRequest,
        response: google.cloud.netapp_v1.types.backup_vault.ListBackupVaultsResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListBackupVaultsPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListBackupVaultsPager#google_cloud_netapp_v1_services_net_app_pagers_ListBackupVaultsPager_ListBackupVaultsPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListBackupsAsyncPager
    
    
    ListBackupsAsyncPager(
        method: typing.Callable[
            [...], typing.Awaitable[google.cloud.netapp_v1.types.backup.ListBackupsResponse]
        ],
        request: google.cloud.netapp_v1.types.backup.ListBackupsRequest,
        response: google.cloud.netapp_v1.types.backup.ListBackupsResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListBackupsAsyncPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListBackupsAsyncPager#google_cloud_netapp_v1_services_net_app_pagers_ListBackupsAsyncPager_ListBackupsAsyncPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListBackupsPager
    
    
    ListBackupsPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.backup.ListBackupsResponse
        ],
        request: google.cloud.netapp_v1.types.backup.ListBackupsRequest,
        response: google.cloud.netapp_v1.types.backup.ListBackupsResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListBackupsPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListBackupsPager#google_cloud_netapp_v1_services_net_app_pagers_ListBackupsPager_ListBackupsPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListHostGroupsAsyncPager
    
    
    ListHostGroupsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.netapp_v1.types.host_group.ListHostGroupsResponse
            ],
        ],
        request: google.cloud.netapp_v1.types.host_group.ListHostGroupsRequest,
        response: google.cloud.netapp_v1.types.host_group.ListHostGroupsResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListHostGroupsAsyncPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListHostGroupsAsyncPager#google_cloud_netapp_v1_services_net_app_pagers_ListHostGroupsAsyncPager_ListHostGroupsAsyncPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListHostGroupsPager
    
    
    ListHostGroupsPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.host_group.ListHostGroupsResponse
        ],
        request: google.cloud.netapp_v1.types.host_group.ListHostGroupsRequest,
        response: google.cloud.netapp_v1.types.host_group.ListHostGroupsResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListHostGroupsPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListHostGroupsPager#google_cloud_netapp_v1_services_net_app_pagers_ListHostGroupsPager_ListHostGroupsPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListKmsConfigsAsyncPager
    
    
    ListKmsConfigsAsyncPager(
        method: typing.Callable[
            [...], typing.Awaitable[google.cloud.netapp_v1.types.kms.ListKmsConfigsResponse]
        ],
        request: google.cloud.netapp_v1.types.kms.ListKmsConfigsRequest,
        response: google.cloud.netapp_v1.types.kms.ListKmsConfigsResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListKmsConfigsAsyncPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListKmsConfigsAsyncPager#google_cloud_netapp_v1_services_net_app_pagers_ListKmsConfigsAsyncPager_ListKmsConfigsAsyncPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListKmsConfigsPager
    
    
    ListKmsConfigsPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.kms.ListKmsConfigsResponse
        ],
        request: google.cloud.netapp_v1.types.kms.ListKmsConfigsRequest,
        response: google.cloud.netapp_v1.types.kms.ListKmsConfigsResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListKmsConfigsPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListKmsConfigsPager#google_cloud_netapp_v1_services_net_app_pagers_ListKmsConfigsPager_ListKmsConfigsPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListQuotaRulesAsyncPager
    
    
    ListQuotaRulesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.netapp_v1.types.quota_rule.ListQuotaRulesResponse
            ],
        ],
        request: google.cloud.netapp_v1.types.quota_rule.ListQuotaRulesRequest,
        response: google.cloud.netapp_v1.types.quota_rule.ListQuotaRulesResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListQuotaRulesAsyncPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListQuotaRulesAsyncPager#google_cloud_netapp_v1_services_net_app_pagers_ListQuotaRulesAsyncPager_ListQuotaRulesAsyncPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListQuotaRulesPager
    
    
    ListQuotaRulesPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.quota_rule.ListQuotaRulesResponse
        ],
        request: google.cloud.netapp_v1.types.quota_rule.ListQuotaRulesRequest,
        response: google.cloud.netapp_v1.types.quota_rule.ListQuotaRulesResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListQuotaRulesPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListQuotaRulesPager#google_cloud_netapp_v1_services_net_app_pagers_ListQuotaRulesPager_ListQuotaRulesPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListReplicationsAsyncPager
    
    
    ListReplicationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.netapp_v1.types.replication.ListReplicationsResponse
            ],
        ],
        request: google.cloud.netapp_v1.types.replication.ListReplicationsRequest,
        response: google.cloud.netapp_v1.types.replication.ListReplicationsResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListReplicationsAsyncPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListReplicationsAsyncPager#google_cloud_netapp_v1_services_net_app_pagers_ListReplicationsAsyncPager_ListReplicationsAsyncPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListReplicationsPager
    
    
    ListReplicationsPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.replication.ListReplicationsResponse
        ],
        request: google.cloud.netapp_v1.types.replication.ListReplicationsRequest,
        response: google.cloud.netapp_v1.types.replication.ListReplicationsResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListReplicationsPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListReplicationsPager#google_cloud_netapp_v1_services_net_app_pagers_ListReplicationsPager_ListReplicationsPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListSnapshotsAsyncPager
    
    
    ListSnapshotsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.netapp_v1.types.snapshot.ListSnapshotsResponse],
        ],
        request: google.cloud.netapp_v1.types.snapshot.ListSnapshotsRequest,
        response: google.cloud.netapp_v1.types.snapshot.ListSnapshotsResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListSnapshotsAsyncPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListSnapshotsAsyncPager#google_cloud_netapp_v1_services_net_app_pagers_ListSnapshotsAsyncPager_ListSnapshotsAsyncPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListSnapshotsPager
    
    
    ListSnapshotsPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.snapshot.ListSnapshotsResponse
        ],
        request: google.cloud.netapp_v1.types.snapshot.ListSnapshotsRequest,
        response: google.cloud.netapp_v1.types.snapshot.ListSnapshotsResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListSnapshotsPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListSnapshotsPager#google_cloud_netapp_v1_services_net_app_pagers_ListSnapshotsPager_ListSnapshotsPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListStoragePoolsAsyncPager
    
    
    ListStoragePoolsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.netapp_v1.types.storage_pool.ListStoragePoolsResponse
            ],
        ],
        request: google.cloud.netapp_v1.types.storage_pool.ListStoragePoolsRequest,
        response: google.cloud.netapp_v1.types.storage_pool.ListStoragePoolsResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListStoragePoolsAsyncPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListStoragePoolsAsyncPager#google_cloud_netapp_v1_services_net_app_pagers_ListStoragePoolsAsyncPager_ListStoragePoolsAsyncPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListStoragePoolsPager
    
    
    ListStoragePoolsPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.storage_pool.ListStoragePoolsResponse
        ],
        request: google.cloud.netapp_v1.types.storage_pool.ListStoragePoolsRequest,
        response: google.cloud.netapp_v1.types.storage_pool.ListStoragePoolsResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListStoragePoolsPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListStoragePoolsPager#google_cloud_netapp_v1_services_net_app_pagers_ListStoragePoolsPager_ListStoragePoolsPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListVolumesAsyncPager
    
    
    ListVolumesAsyncPager(
        method: typing.Callable[
            [...], typing.Awaitable[google.cloud.netapp_v1.types.volume.ListVolumesResponse]
        ],
        request: google.cloud.netapp_v1.types.volume.ListVolumesRequest,
        response: google.cloud.netapp_v1.types.volume.ListVolumesResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListVolumesAsyncPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListVolumesAsyncPager#google_cloud_netapp_v1_services_net_app_pagers_ListVolumesAsyncPager_ListVolumesAsyncPager)

### google.cloud.netapp_v1.services.net_app.pagers.ListVolumesPager
    
    
    ListVolumesPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.volume.ListVolumesResponse
        ],
        request: google.cloud.netapp_v1.types.volume.ListVolumesRequest,
        response: google.cloud.netapp_v1.types.volume.ListVolumesResponse,
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

See more: [google.cloud.netapp_v1.services.net_app.pagers.ListVolumesPager](https://cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListVolumesPager#google_cloud_netapp_v1_services_net_app_pagers_ListVolumesPager_ListVolumesPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
