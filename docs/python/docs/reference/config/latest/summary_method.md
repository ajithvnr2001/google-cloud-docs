---
url: https://docs.cloud.google.com/python/docs/reference/config/latest/summary_method/
title: Package Methods (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:32.966614+00:00
---

# Package Methods (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/config/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.21 

Summary of entries of Methods for config.

## 

### google.cloud.config_v1.services.config.ConfigAsyncClient
    
    
    ConfigAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.config_v1.services.config.transports.base.ConfigTransport,
                typing.Callable[
                    [...],
                    google.cloud.config_v1.services.config.transports.base.ConfigTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the config async client.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_ConfigAsyncClient)

### google.cloud.config_v1.services.config.ConfigAsyncClient.auto_migration_config_path
    
    
    auto_migration_config_path(project: str, location: str) -> str

Returns a fully-qualified auto_migration_config string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.auto_migration_config_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_auto_migration_config_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_cancel_operation)

### google.cloud.config_v1.services.config.ConfigAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_common_billing_account_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_common_folder_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_common_location_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_common_organization_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_common_project_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.create_deployment
    
    
    create_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.CreateDeploymentRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deployment: typing.Optional[google.cloud.config_v1.types.config.Deployment] = None,
        deployment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a xref_Deployment.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.create_deployment](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_create_deployment)

### google.cloud.config_v1.services.config.ConfigAsyncClient.create_deployment_group
    
    
    create_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.CreateDeploymentGroupRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deployment_group: typing.Optional[
            google.cloud.config_v1.types.config.DeploymentGroup
        ] = None,
        deployment_group_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a xref_DeploymentGroup The newly created DeploymentGroup will be in the `CREATING` state and can be retrieved via Get and List calls.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.create_deployment_group](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_create_deployment_group)

### google.cloud.config_v1.services.config.ConfigAsyncClient.create_preview
    
    
    create_preview(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.CreatePreviewRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        preview: typing.Optional[google.cloud.config_v1.types.config.Preview] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a xref_Preview.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.create_preview](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_create_preview)

### google.cloud.config_v1.services.config.ConfigAsyncClient.delete_deployment
    
    
    delete_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.DeleteDeploymentRequest, dict]
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

Deletes a xref_Deployment.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.delete_deployment](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_delete_deployment)

### google.cloud.config_v1.services.config.ConfigAsyncClient.delete_deployment_group
    
    
    delete_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.DeleteDeploymentGroupRequest, dict
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

Deletes a xref_DeploymentGroup.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.delete_deployment_group](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_delete_deployment_group)

### google.cloud.config_v1.services.config.ConfigAsyncClient.delete_operation
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_delete_operation)

### google.cloud.config_v1.services.config.ConfigAsyncClient.delete_preview
    
    
    delete_preview(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.DeletePreviewRequest, dict]
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

Deletes a xref_Preview.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.delete_preview](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_delete_preview)

### google.cloud.config_v1.services.config.ConfigAsyncClient.delete_statefile
    
    
    delete_statefile(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.DeleteStatefileRequest, dict]
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

Deletes Terraform state file in a given deployment.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.delete_statefile](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_delete_statefile)

### google.cloud.config_v1.services.config.ConfigAsyncClient.deployment_group_path
    
    
    deployment_group_path(project: str, location: str, deployment_group: str) -> str

Returns a fully-qualified deployment_group string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.deployment_group_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_deployment_group_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.deployment_group_revision_path
    
    
    deployment_group_revision_path(
        project: str, location: str, deployment_group: str, revision: str
    ) -> str

Returns a fully-qualified deployment_group_revision string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.deployment_group_revision_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_deployment_group_revision_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.deployment_path
    
    
    deployment_path(project: str, location: str, deployment: str) -> str

Returns a fully-qualified deployment string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.deployment_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_deployment_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.deprovision_deployment_group
    
    
    deprovision_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.DeprovisionDeploymentGroupRequest, dict
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

Deprovisions a deployment group.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.deprovision_deployment_group](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_deprovision_deployment_group)

### google.cloud.config_v1.services.config.ConfigAsyncClient.export_deployment_statefile
    
    
    export_deployment_statefile(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ExportDeploymentStatefileRequest, dict
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
    ) -> google.cloud.config_v1.types.config.Statefile

Exports Terraform state file from a given deployment.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.export_deployment_statefile](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_export_deployment_statefile)

### google.cloud.config_v1.services.config.ConfigAsyncClient.export_lock_info
    
    
    export_lock_info(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ExportLockInfoRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.LockInfo

Exports the lock info on a locked deployment.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.export_lock_info](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_export_lock_info)

### google.cloud.config_v1.services.config.ConfigAsyncClient.export_preview_result
    
    
    export_preview_result(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ExportPreviewResultRequest, dict
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
    ) -> google.cloud.config_v1.types.config.ExportPreviewResultResponse

Export xref_Preview results.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.export_preview_result](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_export_preview_result)

### google.cloud.config_v1.services.config.ConfigAsyncClient.export_revision_statefile
    
    
    export_revision_statefile(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ExportRevisionStatefileRequest, dict
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
    ) -> google.cloud.config_v1.types.config.Statefile

Exports Terraform state file from a given revision.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.export_revision_statefile](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_export_revision_statefile)

### google.cloud.config_v1.services.config.ConfigAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_from_service_account_file)

### google.cloud.config_v1.services.config.ConfigAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_from_service_account_info)

### google.cloud.config_v1.services.config.ConfigAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_from_service_account_json)

### google.cloud.config_v1.services.config.ConfigAsyncClient.get_auto_migration_config
    
    
    get_auto_migration_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.GetAutoMigrationConfigRequest, dict
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
    ) -> google.cloud.config_v1.types.config.AutoMigrationConfig

Get the AutoMigrationConfig for a given project and location.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.get_auto_migration_config](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_get_auto_migration_config)

### google.cloud.config_v1.services.config.ConfigAsyncClient.get_deployment
    
    
    get_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetDeploymentRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.Deployment

Gets details about a xref_Deployment.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.get_deployment](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_get_deployment)

### google.cloud.config_v1.services.config.ConfigAsyncClient.get_deployment_group
    
    
    get_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.GetDeploymentGroupRequest, dict
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
    ) -> google.cloud.config_v1.types.config.DeploymentGroup

Get a DeploymentGroup for a given project and location.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.get_deployment_group](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_get_deployment_group)

### google.cloud.config_v1.services.config.ConfigAsyncClient.get_deployment_group_revision
    
    
    get_deployment_group_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.GetDeploymentGroupRevisionRequest, dict
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
    ) -> google.cloud.config_v1.types.config.DeploymentGroupRevision

Gets details about a xref_DeploymentGroupRevision.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.get_deployment_group_revision](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_get_deployment_group_revision)

### google.cloud.config_v1.services.config.ConfigAsyncClient.get_iam_policy
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_get_iam_policy)

### google.cloud.config_v1.services.config.ConfigAsyncClient.get_location
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.get_location](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_get_location)

### google.cloud.config_v1.services.config.ConfigAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.config_v1.services.config.ConfigAsyncClient.get_operation
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_get_operation)

### google.cloud.config_v1.services.config.ConfigAsyncClient.get_preview
    
    
    get_preview(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetPreviewRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.Preview

Gets details about a xref_Preview.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.get_preview](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_get_preview)

### google.cloud.config_v1.services.config.ConfigAsyncClient.get_resource
    
    
    get_resource(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetResourceRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.Resource

Gets details about a xref_Resource deployed by Infra Manager.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.get_resource](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_get_resource)

### google.cloud.config_v1.services.config.ConfigAsyncClient.get_resource_change
    
    
    get_resource_change(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetResourceChangeRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.ResourceChange

Get a ResourceChange for a given preview.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.get_resource_change](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_get_resource_change)

### google.cloud.config_v1.services.config.ConfigAsyncClient.get_resource_drift
    
    
    get_resource_drift(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetResourceDriftRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.ResourceDrift

Get a ResourceDrift for a given preview.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.get_resource_drift](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_get_resource_drift)

### google.cloud.config_v1.services.config.ConfigAsyncClient.get_revision
    
    
    get_revision(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetRevisionRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.Revision

Gets details about a xref_Revision.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.get_revision](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_get_revision)

### google.cloud.config_v1.services.config.ConfigAsyncClient.get_terraform_version
    
    
    get_terraform_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.GetTerraformVersionRequest, dict
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
    ) -> google.cloud.config_v1.types.config.TerraformVersion

Gets details about a xref_TerraformVersion.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.get_terraform_version](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_get_terraform_version)

### google.cloud.config_v1.services.config.ConfigAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.config_v1.services.config.transports.base.ConfigTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_get_transport_class)

### google.cloud.config_v1.services.config.ConfigAsyncClient.import_statefile
    
    
    import_statefile(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ImportStatefileRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        lock_id: typing.Optional[int] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.config_v1.types.config.Statefile

Imports Terraform state file in a given deployment.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.import_statefile](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_import_statefile)

### google.cloud.config_v1.services.config.ConfigAsyncClient.list_deployment_group_revisions
    
    
    list_deployment_group_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ListDeploymentGroupRevisionsRequest,
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
        google.cloud.config_v1.services.config.pagers.ListDeploymentGroupRevisionsAsyncPager
    )

Lists xref_DeploymentGroupRevisions in a given xref_DeploymentGroup.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.list_deployment_group_revisions](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_list_deployment_group_revisions)

### google.cloud.config_v1.services.config.ConfigAsyncClient.list_deployment_groups
    
    
    list_deployment_groups(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ListDeploymentGroupsRequest, dict
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
    ) -> google.cloud.config_v1.services.config.pagers.ListDeploymentGroupsAsyncPager

List DeploymentGroups for a given project and location.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.list_deployment_groups](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_list_deployment_groups)

### google.cloud.config_v1.services.config.ConfigAsyncClient.list_deployments
    
    
    list_deployments(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ListDeploymentsRequest, dict]
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
    ) -> google.cloud.config_v1.services.config.pagers.ListDeploymentsAsyncPager

Lists xref_Deployments in a given project and location.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.list_deployments](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_list_deployments)

### google.cloud.config_v1.services.config.ConfigAsyncClient.list_locations
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_list_locations)

### google.cloud.config_v1.services.config.ConfigAsyncClient.list_operations
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_list_operations)

### google.cloud.config_v1.services.config.ConfigAsyncClient.list_previews
    
    
    list_previews(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ListPreviewsRequest, dict]
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
    ) -> google.cloud.config_v1.services.config.pagers.ListPreviewsAsyncPager

Lists xref_Previews in a given project and location.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.list_previews](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_list_previews)

### google.cloud.config_v1.services.config.ConfigAsyncClient.list_resource_changes
    
    
    list_resource_changes(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ListResourceChangesRequest, dict
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
    ) -> google.cloud.config_v1.services.config.pagers.ListResourceChangesAsyncPager

Lists ResourceChanges for a given preview.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.list_resource_changes](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_list_resource_changes)

### google.cloud.config_v1.services.config.ConfigAsyncClient.list_resource_drifts
    
    
    list_resource_drifts(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ListResourceDriftsRequest, dict
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
    ) -> google.cloud.config_v1.services.config.pagers.ListResourceDriftsAsyncPager

List ResourceDrifts for a given preview.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.list_resource_drifts](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_list_resource_drifts)

### google.cloud.config_v1.services.config.ConfigAsyncClient.list_resources
    
    
    list_resources(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ListResourcesRequest, dict]
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
    ) -> google.cloud.config_v1.services.config.pagers.ListResourcesAsyncPager

Lists xref_Resources in a given revision.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.list_resources](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_list_resources)

### google.cloud.config_v1.services.config.ConfigAsyncClient.list_revisions
    
    
    list_revisions(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ListRevisionsRequest, dict]
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
    ) -> google.cloud.config_v1.services.config.pagers.ListRevisionsAsyncPager

Lists xref_Revisions of a deployment.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.list_revisions](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_list_revisions)

### google.cloud.config_v1.services.config.ConfigAsyncClient.list_terraform_versions
    
    
    list_terraform_versions(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ListTerraformVersionsRequest, dict
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
    ) -> google.cloud.config_v1.services.config.pagers.ListTerraformVersionsAsyncPager

Lists xref_TerraformVersions in a given project and location.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.list_terraform_versions](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_list_terraform_versions)

### google.cloud.config_v1.services.config.ConfigAsyncClient.lock_deployment
    
    
    lock_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.LockDeploymentRequest, dict]
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

Locks a deployment.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.lock_deployment](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_lock_deployment)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_auto_migration_config_path
    
    
    parse_auto_migration_config_path(path: str) -> typing.Dict[str, str]

Parses a auto_migration_config path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_auto_migration_config_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_auto_migration_config_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_common_billing_account_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_common_folder_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_common_location_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_common_organization_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_common_project_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_deployment_group_path
    
    
    parse_deployment_group_path(path: str) -> typing.Dict[str, str]

Parses a deployment_group path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_deployment_group_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_deployment_group_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_deployment_group_revision_path
    
    
    parse_deployment_group_revision_path(path: str) -> typing.Dict[str, str]

Parses a deployment_group_revision path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_deployment_group_revision_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_deployment_group_revision_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_deployment_path
    
    
    parse_deployment_path(path: str) -> typing.Dict[str, str]

Parses a deployment path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_deployment_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_deployment_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_preview_path
    
    
    parse_preview_path(path: str) -> typing.Dict[str, str]

Parses a preview path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_preview_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_preview_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_resource_change_path
    
    
    parse_resource_change_path(path: str) -> typing.Dict[str, str]

Parses a resource_change path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_resource_change_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_resource_change_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_resource_drift_path
    
    
    parse_resource_drift_path(path: str) -> typing.Dict[str, str]

Parses a resource_drift path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_resource_drift_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_resource_drift_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_resource_path
    
    
    parse_resource_path(path: str) -> typing.Dict[str, str]

Parses a resource path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_resource_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_resource_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_revision_path
    
    
    parse_revision_path(path: str) -> typing.Dict[str, str]

Parses a revision path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_revision_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_revision_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_service_account_path
    
    
    parse_service_account_path(path: str) -> typing.Dict[str, str]

Parses a service_account path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_service_account_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_service_account_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_terraform_version_path
    
    
    parse_terraform_version_path(path: str) -> typing.Dict[str, str]

Parses a terraform_version path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_terraform_version_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_terraform_version_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.parse_worker_pool_path
    
    
    parse_worker_pool_path(path: str) -> typing.Dict[str, str]

Parses a worker_pool path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.parse_worker_pool_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_parse_worker_pool_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.preview_path
    
    
    preview_path(project: str, location: str, preview: str) -> str

Returns a fully-qualified preview string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.preview_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_preview_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.provision_deployment_group
    
    
    provision_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ProvisionDeploymentGroupRequest, dict
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

Provisions a deployment group.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.provision_deployment_group](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_provision_deployment_group)

### google.cloud.config_v1.services.config.ConfigAsyncClient.resource_change_path
    
    
    resource_change_path(
        project: str, location: str, preview: str, resource_change: str
    ) -> str

Returns a fully-qualified resource_change string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.resource_change_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_resource_change_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.resource_drift_path
    
    
    resource_drift_path(
        project: str, location: str, preview: str, resource_drift: str
    ) -> str

Returns a fully-qualified resource_drift string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.resource_drift_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_resource_drift_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.resource_path
    
    
    resource_path(
        project: str, location: str, deployment: str, revision: str, resource: str
    ) -> str

Returns a fully-qualified resource string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.resource_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_resource_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.revision_path
    
    
    revision_path(project: str, location: str, deployment: str, revision: str) -> str

Returns a fully-qualified revision string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.revision_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_revision_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.service_account_path
    
    
    service_account_path(project: str, service_account: str) -> str

Returns a fully-qualified service_account string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.service_account_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_service_account_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.set_iam_policy
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_set_iam_policy)

### google.cloud.config_v1.services.config.ConfigAsyncClient.terraform_version_path
    
    
    terraform_version_path(project: str, location: str, terraform_version: str) -> str

Returns a fully-qualified terraform_version string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.terraform_version_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_terraform_version_path)

### google.cloud.config_v1.services.config.ConfigAsyncClient.test_iam_permissions
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_test_iam_permissions)

### google.cloud.config_v1.services.config.ConfigAsyncClient.unlock_deployment
    
    
    unlock_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.UnlockDeploymentRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        lock_id: typing.Optional[int] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Unlocks a locked deployment.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.unlock_deployment](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_unlock_deployment)

### google.cloud.config_v1.services.config.ConfigAsyncClient.update_auto_migration_config
    
    
    update_auto_migration_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.UpdateAutoMigrationConfigRequest, dict
            ]
        ] = None,
        *,
        auto_migration_config: typing.Optional[
            google.cloud.config_v1.types.config.AutoMigrationConfig
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

Updates the AutoMigrationConfig for a given project and location.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.update_auto_migration_config](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_update_auto_migration_config)

### google.cloud.config_v1.services.config.ConfigAsyncClient.update_deployment
    
    
    update_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.UpdateDeploymentRequest, dict]
        ] = None,
        *,
        deployment: typing.Optional[google.cloud.config_v1.types.config.Deployment] = None,
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

Updates a xref_Deployment.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.update_deployment](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_update_deployment)

### google.cloud.config_v1.services.config.ConfigAsyncClient.update_deployment_group
    
    
    update_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.UpdateDeploymentGroupRequest, dict
            ]
        ] = None,
        *,
        deployment_group: typing.Optional[
            google.cloud.config_v1.types.config.DeploymentGroup
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

Updates a xref_DeploymentGroup.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.update_deployment_group](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_update_deployment_group)

### google.cloud.config_v1.services.config.ConfigAsyncClient.worker_pool_path
    
    
    worker_pool_path(project: str, location: str, worker_pool: str) -> str

Returns a fully-qualified worker_pool string.

See more: [google.cloud.config_v1.services.config.ConfigAsyncClient.worker_pool_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigAsyncClient#google_cloud_config_v1_services_config_ConfigAsyncClient_worker_pool_path)

### google.cloud.config_v1.services.config.ConfigClient
    
    
    ConfigClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.config_v1.services.config.transports.base.ConfigTransport,
                typing.Callable[
                    [...],
                    google.cloud.config_v1.services.config.transports.base.ConfigTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the config client.

See more: [google.cloud.config_v1.services.config.ConfigClient](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_ConfigClient)

### google.cloud.config_v1.services.config.ConfigClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.config_v1.services.config.ConfigClient.**exit**](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient___exit__)

### google.cloud.config_v1.services.config.ConfigClient.auto_migration_config_path
    
    
    auto_migration_config_path(project: str, location: str) -> str

Returns a fully-qualified auto_migration_config string.

See more: [google.cloud.config_v1.services.config.ConfigClient.auto_migration_config_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_auto_migration_config_path)

### google.cloud.config_v1.services.config.ConfigClient.cancel_operation
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigClient.cancel_operation](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_cancel_operation)

### google.cloud.config_v1.services.config.ConfigClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.config_v1.services.config.ConfigClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_common_billing_account_path)

### google.cloud.config_v1.services.config.ConfigClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.config_v1.services.config.ConfigClient.common_folder_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_common_folder_path)

### google.cloud.config_v1.services.config.ConfigClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.config_v1.services.config.ConfigClient.common_location_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_common_location_path)

### google.cloud.config_v1.services.config.ConfigClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.config_v1.services.config.ConfigClient.common_organization_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_common_organization_path)

### google.cloud.config_v1.services.config.ConfigClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.config_v1.services.config.ConfigClient.common_project_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_common_project_path)

### google.cloud.config_v1.services.config.ConfigClient.create_deployment
    
    
    create_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.CreateDeploymentRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deployment: typing.Optional[google.cloud.config_v1.types.config.Deployment] = None,
        deployment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a xref_Deployment.

See more: [google.cloud.config_v1.services.config.ConfigClient.create_deployment](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_create_deployment)

### google.cloud.config_v1.services.config.ConfigClient.create_deployment_group
    
    
    create_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.CreateDeploymentGroupRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deployment_group: typing.Optional[
            google.cloud.config_v1.types.config.DeploymentGroup
        ] = None,
        deployment_group_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a xref_DeploymentGroup The newly created DeploymentGroup will be in the `CREATING` state and can be retrieved via Get and List calls.

See more: [google.cloud.config_v1.services.config.ConfigClient.create_deployment_group](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_create_deployment_group)

### google.cloud.config_v1.services.config.ConfigClient.create_preview
    
    
    create_preview(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.CreatePreviewRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        preview: typing.Optional[google.cloud.config_v1.types.config.Preview] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a xref_Preview.

See more: [google.cloud.config_v1.services.config.ConfigClient.create_preview](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_create_preview)

### google.cloud.config_v1.services.config.ConfigClient.delete_deployment
    
    
    delete_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.DeleteDeploymentRequest, dict]
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

Deletes a xref_Deployment.

See more: [google.cloud.config_v1.services.config.ConfigClient.delete_deployment](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_delete_deployment)

### google.cloud.config_v1.services.config.ConfigClient.delete_deployment_group
    
    
    delete_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.DeleteDeploymentGroupRequest, dict
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

Deletes a xref_DeploymentGroup.

See more: [google.cloud.config_v1.services.config.ConfigClient.delete_deployment_group](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_delete_deployment_group)

### google.cloud.config_v1.services.config.ConfigClient.delete_operation
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigClient.delete_operation](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_delete_operation)

### google.cloud.config_v1.services.config.ConfigClient.delete_preview
    
    
    delete_preview(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.DeletePreviewRequest, dict]
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

Deletes a xref_Preview.

See more: [google.cloud.config_v1.services.config.ConfigClient.delete_preview](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_delete_preview)

### google.cloud.config_v1.services.config.ConfigClient.delete_statefile
    
    
    delete_statefile(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.DeleteStatefileRequest, dict]
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

Deletes Terraform state file in a given deployment.

See more: [google.cloud.config_v1.services.config.ConfigClient.delete_statefile](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_delete_statefile)

### google.cloud.config_v1.services.config.ConfigClient.deployment_group_path
    
    
    deployment_group_path(project: str, location: str, deployment_group: str) -> str

Returns a fully-qualified deployment_group string.

See more: [google.cloud.config_v1.services.config.ConfigClient.deployment_group_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_deployment_group_path)

### google.cloud.config_v1.services.config.ConfigClient.deployment_group_revision_path
    
    
    deployment_group_revision_path(
        project: str, location: str, deployment_group: str, revision: str
    ) -> str

Returns a fully-qualified deployment_group_revision string.

See more: [google.cloud.config_v1.services.config.ConfigClient.deployment_group_revision_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_deployment_group_revision_path)

### google.cloud.config_v1.services.config.ConfigClient.deployment_path
    
    
    deployment_path(project: str, location: str, deployment: str) -> str

Returns a fully-qualified deployment string.

See more: [google.cloud.config_v1.services.config.ConfigClient.deployment_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_deployment_path)

### google.cloud.config_v1.services.config.ConfigClient.deprovision_deployment_group
    
    
    deprovision_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.DeprovisionDeploymentGroupRequest, dict
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

Deprovisions a deployment group.

See more: [google.cloud.config_v1.services.config.ConfigClient.deprovision_deployment_group](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_deprovision_deployment_group)

### google.cloud.config_v1.services.config.ConfigClient.export_deployment_statefile
    
    
    export_deployment_statefile(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ExportDeploymentStatefileRequest, dict
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
    ) -> google.cloud.config_v1.types.config.Statefile

Exports Terraform state file from a given deployment.

See more: [google.cloud.config_v1.services.config.ConfigClient.export_deployment_statefile](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_export_deployment_statefile)

### google.cloud.config_v1.services.config.ConfigClient.export_lock_info
    
    
    export_lock_info(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ExportLockInfoRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.LockInfo

Exports the lock info on a locked deployment.

See more: [google.cloud.config_v1.services.config.ConfigClient.export_lock_info](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_export_lock_info)

### google.cloud.config_v1.services.config.ConfigClient.export_preview_result
    
    
    export_preview_result(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ExportPreviewResultRequest, dict
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
    ) -> google.cloud.config_v1.types.config.ExportPreviewResultResponse

Export xref_Preview results.

See more: [google.cloud.config_v1.services.config.ConfigClient.export_preview_result](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_export_preview_result)

### google.cloud.config_v1.services.config.ConfigClient.export_revision_statefile
    
    
    export_revision_statefile(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ExportRevisionStatefileRequest, dict
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
    ) -> google.cloud.config_v1.types.config.Statefile

Exports Terraform state file from a given revision.

See more: [google.cloud.config_v1.services.config.ConfigClient.export_revision_statefile](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_export_revision_statefile)

### google.cloud.config_v1.services.config.ConfigClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.config_v1.services.config.ConfigClient.from_service_account_file](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_from_service_account_file)

### google.cloud.config_v1.services.config.ConfigClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.config_v1.services.config.ConfigClient.from_service_account_info](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_from_service_account_info)

### google.cloud.config_v1.services.config.ConfigClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.config_v1.services.config.ConfigClient.from_service_account_json](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_from_service_account_json)

### google.cloud.config_v1.services.config.ConfigClient.get_auto_migration_config
    
    
    get_auto_migration_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.GetAutoMigrationConfigRequest, dict
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
    ) -> google.cloud.config_v1.types.config.AutoMigrationConfig

Get the AutoMigrationConfig for a given project and location.

See more: [google.cloud.config_v1.services.config.ConfigClient.get_auto_migration_config](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_get_auto_migration_config)

### google.cloud.config_v1.services.config.ConfigClient.get_deployment
    
    
    get_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetDeploymentRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.Deployment

Gets details about a xref_Deployment.

See more: [google.cloud.config_v1.services.config.ConfigClient.get_deployment](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_get_deployment)

### google.cloud.config_v1.services.config.ConfigClient.get_deployment_group
    
    
    get_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.GetDeploymentGroupRequest, dict
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
    ) -> google.cloud.config_v1.types.config.DeploymentGroup

Get a DeploymentGroup for a given project and location.

See more: [google.cloud.config_v1.services.config.ConfigClient.get_deployment_group](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_get_deployment_group)

### google.cloud.config_v1.services.config.ConfigClient.get_deployment_group_revision
    
    
    get_deployment_group_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.GetDeploymentGroupRevisionRequest, dict
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
    ) -> google.cloud.config_v1.types.config.DeploymentGroupRevision

Gets details about a xref_DeploymentGroupRevision.

See more: [google.cloud.config_v1.services.config.ConfigClient.get_deployment_group_revision](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_get_deployment_group_revision)

### google.cloud.config_v1.services.config.ConfigClient.get_iam_policy
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigClient.get_iam_policy](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_get_iam_policy)

### google.cloud.config_v1.services.config.ConfigClient.get_location
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigClient.get_location](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_get_location)

### google.cloud.config_v1.services.config.ConfigClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.config_v1.services.config.ConfigClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_get_mtls_endpoint_and_cert_source)

### google.cloud.config_v1.services.config.ConfigClient.get_operation
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigClient.get_operation](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_get_operation)

### google.cloud.config_v1.services.config.ConfigClient.get_preview
    
    
    get_preview(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetPreviewRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.Preview

Gets details about a xref_Preview.

See more: [google.cloud.config_v1.services.config.ConfigClient.get_preview](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_get_preview)

### google.cloud.config_v1.services.config.ConfigClient.get_resource
    
    
    get_resource(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetResourceRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.Resource

Gets details about a xref_Resource deployed by Infra Manager.

See more: [google.cloud.config_v1.services.config.ConfigClient.get_resource](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_get_resource)

### google.cloud.config_v1.services.config.ConfigClient.get_resource_change
    
    
    get_resource_change(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetResourceChangeRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.ResourceChange

Get a ResourceChange for a given preview.

See more: [google.cloud.config_v1.services.config.ConfigClient.get_resource_change](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_get_resource_change)

### google.cloud.config_v1.services.config.ConfigClient.get_resource_drift
    
    
    get_resource_drift(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetResourceDriftRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.ResourceDrift

Get a ResourceDrift for a given preview.

See more: [google.cloud.config_v1.services.config.ConfigClient.get_resource_drift](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_get_resource_drift)

### google.cloud.config_v1.services.config.ConfigClient.get_revision
    
    
    get_revision(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.GetRevisionRequest, dict]
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
    ) -> google.cloud.config_v1.types.config.Revision

Gets details about a xref_Revision.

See more: [google.cloud.config_v1.services.config.ConfigClient.get_revision](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_get_revision)

### google.cloud.config_v1.services.config.ConfigClient.get_terraform_version
    
    
    get_terraform_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.GetTerraformVersionRequest, dict
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
    ) -> google.cloud.config_v1.types.config.TerraformVersion

Gets details about a xref_TerraformVersion.

See more: [google.cloud.config_v1.services.config.ConfigClient.get_terraform_version](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_get_terraform_version)

### google.cloud.config_v1.services.config.ConfigClient.import_statefile
    
    
    import_statefile(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ImportStatefileRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        lock_id: typing.Optional[int] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.config_v1.types.config.Statefile

Imports Terraform state file in a given deployment.

See more: [google.cloud.config_v1.services.config.ConfigClient.import_statefile](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_import_statefile)

### google.cloud.config_v1.services.config.ConfigClient.list_deployment_group_revisions
    
    
    list_deployment_group_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ListDeploymentGroupRevisionsRequest,
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
    ) -> google.cloud.config_v1.services.config.pagers.ListDeploymentGroupRevisionsPager

Lists xref_DeploymentGroupRevisions in a given xref_DeploymentGroup.

See more: [google.cloud.config_v1.services.config.ConfigClient.list_deployment_group_revisions](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_list_deployment_group_revisions)

### google.cloud.config_v1.services.config.ConfigClient.list_deployment_groups
    
    
    list_deployment_groups(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ListDeploymentGroupsRequest, dict
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
    ) -> google.cloud.config_v1.services.config.pagers.ListDeploymentGroupsPager

List DeploymentGroups for a given project and location.

See more: [google.cloud.config_v1.services.config.ConfigClient.list_deployment_groups](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_list_deployment_groups)

### google.cloud.config_v1.services.config.ConfigClient.list_deployments
    
    
    list_deployments(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ListDeploymentsRequest, dict]
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
    ) -> google.cloud.config_v1.services.config.pagers.ListDeploymentsPager

Lists xref_Deployments in a given project and location.

See more: [google.cloud.config_v1.services.config.ConfigClient.list_deployments](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_list_deployments)

### google.cloud.config_v1.services.config.ConfigClient.list_locations
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigClient.list_locations](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_list_locations)

### google.cloud.config_v1.services.config.ConfigClient.list_operations
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigClient.list_operations](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_list_operations)

### google.cloud.config_v1.services.config.ConfigClient.list_previews
    
    
    list_previews(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ListPreviewsRequest, dict]
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
    ) -> google.cloud.config_v1.services.config.pagers.ListPreviewsPager

Lists xref_Previews in a given project and location.

See more: [google.cloud.config_v1.services.config.ConfigClient.list_previews](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_list_previews)

### google.cloud.config_v1.services.config.ConfigClient.list_resource_changes
    
    
    list_resource_changes(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ListResourceChangesRequest, dict
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
    ) -> google.cloud.config_v1.services.config.pagers.ListResourceChangesPager

Lists ResourceChanges for a given preview.

See more: [google.cloud.config_v1.services.config.ConfigClient.list_resource_changes](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_list_resource_changes)

### google.cloud.config_v1.services.config.ConfigClient.list_resource_drifts
    
    
    list_resource_drifts(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ListResourceDriftsRequest, dict
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
    ) -> google.cloud.config_v1.services.config.pagers.ListResourceDriftsPager

List ResourceDrifts for a given preview.

See more: [google.cloud.config_v1.services.config.ConfigClient.list_resource_drifts](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_list_resource_drifts)

### google.cloud.config_v1.services.config.ConfigClient.list_resources
    
    
    list_resources(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ListResourcesRequest, dict]
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
    ) -> google.cloud.config_v1.services.config.pagers.ListResourcesPager

Lists xref_Resources in a given revision.

See more: [google.cloud.config_v1.services.config.ConfigClient.list_resources](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_list_resources)

### google.cloud.config_v1.services.config.ConfigClient.list_revisions
    
    
    list_revisions(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.ListRevisionsRequest, dict]
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
    ) -> google.cloud.config_v1.services.config.pagers.ListRevisionsPager

Lists xref_Revisions of a deployment.

See more: [google.cloud.config_v1.services.config.ConfigClient.list_revisions](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_list_revisions)

### google.cloud.config_v1.services.config.ConfigClient.list_terraform_versions
    
    
    list_terraform_versions(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ListTerraformVersionsRequest, dict
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
    ) -> google.cloud.config_v1.services.config.pagers.ListTerraformVersionsPager

Lists xref_TerraformVersions in a given project and location.

See more: [google.cloud.config_v1.services.config.ConfigClient.list_terraform_versions](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_list_terraform_versions)

### google.cloud.config_v1.services.config.ConfigClient.lock_deployment
    
    
    lock_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.LockDeploymentRequest, dict]
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

Locks a deployment.

See more: [google.cloud.config_v1.services.config.ConfigClient.lock_deployment](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_lock_deployment)

### google.cloud.config_v1.services.config.ConfigClient.parse_auto_migration_config_path
    
    
    parse_auto_migration_config_path(path: str) -> typing.Dict[str, str]

Parses a auto_migration_config path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_auto_migration_config_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_auto_migration_config_path)

### google.cloud.config_v1.services.config.ConfigClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_common_billing_account_path)

### google.cloud.config_v1.services.config.ConfigClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_common_folder_path)

### google.cloud.config_v1.services.config.ConfigClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_common_location_path)

### google.cloud.config_v1.services.config.ConfigClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_common_organization_path)

### google.cloud.config_v1.services.config.ConfigClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_common_project_path)

### google.cloud.config_v1.services.config.ConfigClient.parse_deployment_group_path
    
    
    parse_deployment_group_path(path: str) -> typing.Dict[str, str]

Parses a deployment_group path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_deployment_group_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_deployment_group_path)

### google.cloud.config_v1.services.config.ConfigClient.parse_deployment_group_revision_path
    
    
    parse_deployment_group_revision_path(path: str) -> typing.Dict[str, str]

Parses a deployment_group_revision path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_deployment_group_revision_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_deployment_group_revision_path)

### google.cloud.config_v1.services.config.ConfigClient.parse_deployment_path
    
    
    parse_deployment_path(path: str) -> typing.Dict[str, str]

Parses a deployment path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_deployment_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_deployment_path)

### google.cloud.config_v1.services.config.ConfigClient.parse_preview_path
    
    
    parse_preview_path(path: str) -> typing.Dict[str, str]

Parses a preview path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_preview_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_preview_path)

### google.cloud.config_v1.services.config.ConfigClient.parse_resource_change_path
    
    
    parse_resource_change_path(path: str) -> typing.Dict[str, str]

Parses a resource_change path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_resource_change_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_resource_change_path)

### google.cloud.config_v1.services.config.ConfigClient.parse_resource_drift_path
    
    
    parse_resource_drift_path(path: str) -> typing.Dict[str, str]

Parses a resource_drift path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_resource_drift_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_resource_drift_path)

### google.cloud.config_v1.services.config.ConfigClient.parse_resource_path
    
    
    parse_resource_path(path: str) -> typing.Dict[str, str]

Parses a resource path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_resource_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_resource_path)

### google.cloud.config_v1.services.config.ConfigClient.parse_revision_path
    
    
    parse_revision_path(path: str) -> typing.Dict[str, str]

Parses a revision path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_revision_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_revision_path)

### google.cloud.config_v1.services.config.ConfigClient.parse_service_account_path
    
    
    parse_service_account_path(path: str) -> typing.Dict[str, str]

Parses a service_account path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_service_account_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_service_account_path)

### google.cloud.config_v1.services.config.ConfigClient.parse_terraform_version_path
    
    
    parse_terraform_version_path(path: str) -> typing.Dict[str, str]

Parses a terraform_version path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_terraform_version_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_terraform_version_path)

### google.cloud.config_v1.services.config.ConfigClient.parse_worker_pool_path
    
    
    parse_worker_pool_path(path: str) -> typing.Dict[str, str]

Parses a worker_pool path into its component segments.

See more: [google.cloud.config_v1.services.config.ConfigClient.parse_worker_pool_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_parse_worker_pool_path)

### google.cloud.config_v1.services.config.ConfigClient.preview_path
    
    
    preview_path(project: str, location: str, preview: str) -> str

Returns a fully-qualified preview string.

See more: [google.cloud.config_v1.services.config.ConfigClient.preview_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_preview_path)

### google.cloud.config_v1.services.config.ConfigClient.provision_deployment_group
    
    
    provision_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.ProvisionDeploymentGroupRequest, dict
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

Provisions a deployment group.

See more: [google.cloud.config_v1.services.config.ConfigClient.provision_deployment_group](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_provision_deployment_group)

### google.cloud.config_v1.services.config.ConfigClient.resource_change_path
    
    
    resource_change_path(
        project: str, location: str, preview: str, resource_change: str
    ) -> str

Returns a fully-qualified resource_change string.

See more: [google.cloud.config_v1.services.config.ConfigClient.resource_change_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_resource_change_path)

### google.cloud.config_v1.services.config.ConfigClient.resource_drift_path
    
    
    resource_drift_path(
        project: str, location: str, preview: str, resource_drift: str
    ) -> str

Returns a fully-qualified resource_drift string.

See more: [google.cloud.config_v1.services.config.ConfigClient.resource_drift_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_resource_drift_path)

### google.cloud.config_v1.services.config.ConfigClient.resource_path
    
    
    resource_path(
        project: str, location: str, deployment: str, revision: str, resource: str
    ) -> str

Returns a fully-qualified resource string.

See more: [google.cloud.config_v1.services.config.ConfigClient.resource_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_resource_path)

### google.cloud.config_v1.services.config.ConfigClient.revision_path
    
    
    revision_path(project: str, location: str, deployment: str, revision: str) -> str

Returns a fully-qualified revision string.

See more: [google.cloud.config_v1.services.config.ConfigClient.revision_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_revision_path)

### google.cloud.config_v1.services.config.ConfigClient.service_account_path
    
    
    service_account_path(project: str, service_account: str) -> str

Returns a fully-qualified service_account string.

See more: [google.cloud.config_v1.services.config.ConfigClient.service_account_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_service_account_path)

### google.cloud.config_v1.services.config.ConfigClient.set_iam_policy
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigClient.set_iam_policy](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_set_iam_policy)

### google.cloud.config_v1.services.config.ConfigClient.terraform_version_path
    
    
    terraform_version_path(project: str, location: str, terraform_version: str) -> str

Returns a fully-qualified terraform_version string.

See more: [google.cloud.config_v1.services.config.ConfigClient.terraform_version_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_terraform_version_path)

### google.cloud.config_v1.services.config.ConfigClient.test_iam_permissions
    
    
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

See more: [google.cloud.config_v1.services.config.ConfigClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_test_iam_permissions)

### google.cloud.config_v1.services.config.ConfigClient.unlock_deployment
    
    
    unlock_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.UnlockDeploymentRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        lock_id: typing.Optional[int] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Unlocks a locked deployment.

See more: [google.cloud.config_v1.services.config.ConfigClient.unlock_deployment](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_unlock_deployment)

### google.cloud.config_v1.services.config.ConfigClient.update_auto_migration_config
    
    
    update_auto_migration_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.UpdateAutoMigrationConfigRequest, dict
            ]
        ] = None,
        *,
        auto_migration_config: typing.Optional[
            google.cloud.config_v1.types.config.AutoMigrationConfig
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

Updates the AutoMigrationConfig for a given project and location.

See more: [google.cloud.config_v1.services.config.ConfigClient.update_auto_migration_config](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_update_auto_migration_config)

### google.cloud.config_v1.services.config.ConfigClient.update_deployment
    
    
    update_deployment(
        request: typing.Optional[
            typing.Union[google.cloud.config_v1.types.config.UpdateDeploymentRequest, dict]
        ] = None,
        *,
        deployment: typing.Optional[google.cloud.config_v1.types.config.Deployment] = None,
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

Updates a xref_Deployment.

See more: [google.cloud.config_v1.services.config.ConfigClient.update_deployment](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_update_deployment)

### google.cloud.config_v1.services.config.ConfigClient.update_deployment_group
    
    
    update_deployment_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.config_v1.types.config.UpdateDeploymentGroupRequest, dict
            ]
        ] = None,
        *,
        deployment_group: typing.Optional[
            google.cloud.config_v1.types.config.DeploymentGroup
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

Updates a xref_DeploymentGroup.

See more: [google.cloud.config_v1.services.config.ConfigClient.update_deployment_group](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_update_deployment_group)

### google.cloud.config_v1.services.config.ConfigClient.worker_pool_path
    
    
    worker_pool_path(project: str, location: str, worker_pool: str) -> str

Returns a fully-qualified worker_pool string.

See more: [google.cloud.config_v1.services.config.ConfigClient.worker_pool_path](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.ConfigClient#google_cloud_config_v1_services_config_ConfigClient_worker_pool_path)

### google.cloud.config_v1.services.config.pagers.ListDeploymentGroupRevisionsAsyncPager
    
    
    ListDeploymentGroupRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.config_v1.types.config.ListDeploymentGroupRevisionsResponse
            ],
        ],
        request: google.cloud.config_v1.types.config.ListDeploymentGroupRevisionsRequest,
        response: google.cloud.config_v1.types.config.ListDeploymentGroupRevisionsResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListDeploymentGroupRevisionsAsyncPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListDeploymentGroupRevisionsAsyncPager#google_cloud_config_v1_services_config_pagers_ListDeploymentGroupRevisionsAsyncPager_ListDeploymentGroupRevisionsAsyncPager)

### google.cloud.config_v1.services.config.pagers.ListDeploymentGroupRevisionsPager
    
    
    ListDeploymentGroupRevisionsPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListDeploymentGroupRevisionsResponse
        ],
        request: google.cloud.config_v1.types.config.ListDeploymentGroupRevisionsRequest,
        response: google.cloud.config_v1.types.config.ListDeploymentGroupRevisionsResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListDeploymentGroupRevisionsPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListDeploymentGroupRevisionsPager#google_cloud_config_v1_services_config_pagers_ListDeploymentGroupRevisionsPager_ListDeploymentGroupRevisionsPager)

### google.cloud.config_v1.services.config.pagers.ListDeploymentGroupsAsyncPager
    
    
    ListDeploymentGroupsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.config_v1.types.config.ListDeploymentGroupsResponse
            ],
        ],
        request: google.cloud.config_v1.types.config.ListDeploymentGroupsRequest,
        response: google.cloud.config_v1.types.config.ListDeploymentGroupsResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListDeploymentGroupsAsyncPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListDeploymentGroupsAsyncPager#google_cloud_config_v1_services_config_pagers_ListDeploymentGroupsAsyncPager_ListDeploymentGroupsAsyncPager)

### google.cloud.config_v1.services.config.pagers.ListDeploymentGroupsPager
    
    
    ListDeploymentGroupsPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListDeploymentGroupsResponse
        ],
        request: google.cloud.config_v1.types.config.ListDeploymentGroupsRequest,
        response: google.cloud.config_v1.types.config.ListDeploymentGroupsResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListDeploymentGroupsPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListDeploymentGroupsPager#google_cloud_config_v1_services_config_pagers_ListDeploymentGroupsPager_ListDeploymentGroupsPager)

### google.cloud.config_v1.services.config.pagers.ListDeploymentsAsyncPager
    
    
    ListDeploymentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.config_v1.types.config.ListDeploymentsResponse],
        ],
        request: google.cloud.config_v1.types.config.ListDeploymentsRequest,
        response: google.cloud.config_v1.types.config.ListDeploymentsResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListDeploymentsAsyncPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListDeploymentsAsyncPager#google_cloud_config_v1_services_config_pagers_ListDeploymentsAsyncPager_ListDeploymentsAsyncPager)

### google.cloud.config_v1.services.config.pagers.ListDeploymentsPager
    
    
    ListDeploymentsPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListDeploymentsResponse
        ],
        request: google.cloud.config_v1.types.config.ListDeploymentsRequest,
        response: google.cloud.config_v1.types.config.ListDeploymentsResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListDeploymentsPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListDeploymentsPager#google_cloud_config_v1_services_config_pagers_ListDeploymentsPager_ListDeploymentsPager)

### google.cloud.config_v1.services.config.pagers.ListPreviewsAsyncPager
    
    
    ListPreviewsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.config_v1.types.config.ListPreviewsResponse],
        ],
        request: google.cloud.config_v1.types.config.ListPreviewsRequest,
        response: google.cloud.config_v1.types.config.ListPreviewsResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListPreviewsAsyncPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListPreviewsAsyncPager#google_cloud_config_v1_services_config_pagers_ListPreviewsAsyncPager_ListPreviewsAsyncPager)

### google.cloud.config_v1.services.config.pagers.ListPreviewsPager
    
    
    ListPreviewsPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListPreviewsResponse
        ],
        request: google.cloud.config_v1.types.config.ListPreviewsRequest,
        response: google.cloud.config_v1.types.config.ListPreviewsResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListPreviewsPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListPreviewsPager#google_cloud_config_v1_services_config_pagers_ListPreviewsPager_ListPreviewsPager)

### google.cloud.config_v1.services.config.pagers.ListResourceChangesAsyncPager
    
    
    ListResourceChangesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.config_v1.types.config.ListResourceChangesResponse
            ],
        ],
        request: google.cloud.config_v1.types.config.ListResourceChangesRequest,
        response: google.cloud.config_v1.types.config.ListResourceChangesResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListResourceChangesAsyncPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListResourceChangesAsyncPager#google_cloud_config_v1_services_config_pagers_ListResourceChangesAsyncPager_ListResourceChangesAsyncPager)

### google.cloud.config_v1.services.config.pagers.ListResourceChangesPager
    
    
    ListResourceChangesPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListResourceChangesResponse
        ],
        request: google.cloud.config_v1.types.config.ListResourceChangesRequest,
        response: google.cloud.config_v1.types.config.ListResourceChangesResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListResourceChangesPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListResourceChangesPager#google_cloud_config_v1_services_config_pagers_ListResourceChangesPager_ListResourceChangesPager)

### google.cloud.config_v1.services.config.pagers.ListResourceDriftsAsyncPager
    
    
    ListResourceDriftsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.config_v1.types.config.ListResourceDriftsResponse
            ],
        ],
        request: google.cloud.config_v1.types.config.ListResourceDriftsRequest,
        response: google.cloud.config_v1.types.config.ListResourceDriftsResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListResourceDriftsAsyncPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListResourceDriftsAsyncPager#google_cloud_config_v1_services_config_pagers_ListResourceDriftsAsyncPager_ListResourceDriftsAsyncPager)

### google.cloud.config_v1.services.config.pagers.ListResourceDriftsPager
    
    
    ListResourceDriftsPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListResourceDriftsResponse
        ],
        request: google.cloud.config_v1.types.config.ListResourceDriftsRequest,
        response: google.cloud.config_v1.types.config.ListResourceDriftsResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListResourceDriftsPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListResourceDriftsPager#google_cloud_config_v1_services_config_pagers_ListResourceDriftsPager_ListResourceDriftsPager)

### google.cloud.config_v1.services.config.pagers.ListResourcesAsyncPager
    
    
    ListResourcesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.config_v1.types.config.ListResourcesResponse],
        ],
        request: google.cloud.config_v1.types.config.ListResourcesRequest,
        response: google.cloud.config_v1.types.config.ListResourcesResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListResourcesAsyncPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListResourcesAsyncPager#google_cloud_config_v1_services_config_pagers_ListResourcesAsyncPager_ListResourcesAsyncPager)

### google.cloud.config_v1.services.config.pagers.ListResourcesPager
    
    
    ListResourcesPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListResourcesResponse
        ],
        request: google.cloud.config_v1.types.config.ListResourcesRequest,
        response: google.cloud.config_v1.types.config.ListResourcesResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListResourcesPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListResourcesPager#google_cloud_config_v1_services_config_pagers_ListResourcesPager_ListResourcesPager)

### google.cloud.config_v1.services.config.pagers.ListRevisionsAsyncPager
    
    
    ListRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.config_v1.types.config.ListRevisionsResponse],
        ],
        request: google.cloud.config_v1.types.config.ListRevisionsRequest,
        response: google.cloud.config_v1.types.config.ListRevisionsResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListRevisionsAsyncPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListRevisionsAsyncPager#google_cloud_config_v1_services_config_pagers_ListRevisionsAsyncPager_ListRevisionsAsyncPager)

### google.cloud.config_v1.services.config.pagers.ListRevisionsPager
    
    
    ListRevisionsPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListRevisionsResponse
        ],
        request: google.cloud.config_v1.types.config.ListRevisionsRequest,
        response: google.cloud.config_v1.types.config.ListRevisionsResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListRevisionsPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListRevisionsPager#google_cloud_config_v1_services_config_pagers_ListRevisionsPager_ListRevisionsPager)

### google.cloud.config_v1.services.config.pagers.ListTerraformVersionsAsyncPager
    
    
    ListTerraformVersionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.config_v1.types.config.ListTerraformVersionsResponse
            ],
        ],
        request: google.cloud.config_v1.types.config.ListTerraformVersionsRequest,
        response: google.cloud.config_v1.types.config.ListTerraformVersionsResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListTerraformVersionsAsyncPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListTerraformVersionsAsyncPager#google_cloud_config_v1_services_config_pagers_ListTerraformVersionsAsyncPager_ListTerraformVersionsAsyncPager)

### google.cloud.config_v1.services.config.pagers.ListTerraformVersionsPager
    
    
    ListTerraformVersionsPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListTerraformVersionsResponse
        ],
        request: google.cloud.config_v1.types.config.ListTerraformVersionsRequest,
        response: google.cloud.config_v1.types.config.ListTerraformVersionsResponse,
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

See more: [google.cloud.config_v1.services.config.pagers.ListTerraformVersionsPager](https://cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListTerraformVersionsPager#google_cloud_config_v1_services_config_pagers_ListTerraformVersionsPager_ListTerraformVersionsPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
