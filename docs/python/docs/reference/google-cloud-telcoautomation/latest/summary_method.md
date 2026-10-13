---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/summary_method/
title: Package Methods (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:55.247487+00:00
---

# Package Methods (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.4.0  0.3.0  0.2.11  0.1.2 

Summary of entries of Methods for google-cloud-telcoautomation.

## 

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient
    
    
    TelcoAutomationAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.telcoautomation_v1.services.telco_automation.transports.base.TelcoAutomationTransport,
                typing.Callable[
                    [...],
                    google.cloud.telcoautomation_v1.services.telco_automation.transports.base.TelcoAutomationTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the telco automation async client.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_TelcoAutomationAsyncClient)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.apply_deployment
    
    
    apply_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ApplyDeploymentRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Deployment

Applies the deployment's YAML files to the parent orchestration cluster.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.apply_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_apply_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.apply_hydrated_deployment
    
    
    apply_hydrated_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ApplyHydratedDeploymentRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.HydratedDeployment

Applies a hydrated deployment to a workload cluster.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.apply_hydrated_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_apply_hydrated_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.approve_blueprint
    
    
    approve_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ApproveBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Blueprint

Approves a blueprint and commits a new revision.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.approve_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_approve_blueprint)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.blueprint_path
    
    
    blueprint_path(
        project: str, location: str, orchestration_cluster: str, blueprint: str
    ) -> str

Returns a fully-qualified blueprint string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.blueprint_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_blueprint_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_cancel_operation)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_common_billing_account_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_common_folder_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_common_location_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_common_organization_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_common_project_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.compute_deployment_status
    
    
    compute_deployment_status(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ComputeDeploymentStatusRequest,
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
        google.cloud.telcoautomation_v1.types.telcoautomation.ComputeDeploymentStatusResponse
    )

Returns the requested deployment status.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.compute_deployment_status](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_compute_deployment_status)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.create_blueprint
    
    
    create_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.CreateBlueprintRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        blueprint: typing.Optional[
            google.cloud.telcoautomation_v1.types.telcoautomation.Blueprint
        ] = None,
        blueprint_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Blueprint

Creates a blueprint.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.create_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_create_blueprint)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.create_deployment
    
    
    create_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.CreateDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deployment: typing.Optional[
            google.cloud.telcoautomation_v1.types.telcoautomation.Deployment
        ] = None,
        deployment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Deployment

Creates a deployment.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.create_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_create_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.create_edge_slm
    
    
    create_edge_slm(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.CreateEdgeSlmRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        edge_slm: typing.Optional[
            google.cloud.telcoautomation_v1.types.telcoautomation.EdgeSlm
        ] = None,
        edge_slm_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new EdgeSlm in a given project and location.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.create_edge_slm](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_create_edge_slm)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.create_orchestration_cluster
    
    
    create_orchestration_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.CreateOrchestrationClusterRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        orchestration_cluster: typing.Optional[
            google.cloud.telcoautomation_v1.types.telcoautomation.OrchestrationCluster
        ] = None,
        orchestration_cluster_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new OrchestrationCluster in a given project and location.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.create_orchestration_cluster](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_create_orchestration_cluster)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.delete_blueprint
    
    
    delete_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.DeleteBlueprintRequest,
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

Deletes a blueprint and all its revisions.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.delete_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_delete_blueprint)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.delete_edge_slm
    
    
    delete_edge_slm(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.DeleteEdgeSlmRequest,
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

Deletes a single EdgeSlm.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.delete_edge_slm](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_delete_edge_slm)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.delete_operation
    
    
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_delete_operation)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.delete_orchestration_cluster
    
    
    delete_orchestration_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.DeleteOrchestrationClusterRequest,
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

Deletes a single OrchestrationCluster.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.delete_orchestration_cluster](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_delete_orchestration_cluster)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.deployment_path
    
    
    deployment_path(
        project: str, location: str, orchestration_cluster: str, deployment: str
    ) -> str

Returns a fully-qualified deployment string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_deployment_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.discard_blueprint_changes
    
    
    discard_blueprint_changes(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.DiscardBlueprintChangesRequest,
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
        google.cloud.telcoautomation_v1.types.telcoautomation.DiscardBlueprintChangesResponse
    )

Discards the changes in a blueprint and reverts the blueprint to the last approved blueprint revision.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.discard_blueprint_changes](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_discard_blueprint_changes)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.discard_deployment_changes
    
    
    discard_deployment_changes(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.DiscardDeploymentChangesRequest,
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
        google.cloud.telcoautomation_v1.types.telcoautomation.DiscardDeploymentChangesResponse
    )

Discards the changes in a deployment and reverts the deployment to the last approved deployment revision.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.discard_deployment_changes](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_discard_deployment_changes)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.edge_slm_path
    
    
    edge_slm_path(project: str, location: str, edge_slm: str) -> str

Returns a fully-qualified edge_slm string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.edge_slm_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_edge_slm_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_from_service_account_file)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_from_service_account_info)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_from_service_account_json)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_blueprint
    
    
    get_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.GetBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Blueprint

Returns the requested blueprint.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_get_blueprint)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_deployment
    
    
    get_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.GetDeploymentRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Deployment

Returns the requested deployment.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_get_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_edge_slm
    
    
    get_edge_slm(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.GetEdgeSlmRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.EdgeSlm

Gets details of a single EdgeSlm.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_edge_slm](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_get_edge_slm)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_hydrated_deployment
    
    
    get_hydrated_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.GetHydratedDeploymentRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.HydratedDeployment

Returns the requested hydrated deployment.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_hydrated_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_get_hydrated_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_location
    
    
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_get_location)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_operation
    
    
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_get_operation)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_orchestration_cluster
    
    
    get_orchestration_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.GetOrchestrationClusterRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.OrchestrationCluster

Gets details of a single OrchestrationCluster.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_orchestration_cluster](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_get_orchestration_cluster)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_public_blueprint
    
    
    get_public_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.GetPublicBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.PublicBlueprint

Returns the requested public blueprint.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_public_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_get_public_blueprint)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.telcoautomation_v1.services.telco_automation.transports.base.TelcoAutomationTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_get_transport_class)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.hydrated_deployment_path
    
    
    hydrated_deployment_path(
        project: str,
        location: str,
        orchestration_cluster: str,
        deployment: str,
        hydrated_deployment: str,
    ) -> str

Returns a fully-qualified hydrated_deployment string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.hydrated_deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_hydrated_deployment_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_blueprint_revisions
    
    
    list_blueprint_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListBlueprintRevisionsRequest,
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
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListBlueprintRevisionsAsyncPager
    )

List blueprint revisions of a given blueprint.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_blueprint_revisions](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_list_blueprint_revisions)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_blueprints
    
    
    list_blueprints(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListBlueprintsRequest,
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
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListBlueprintsAsyncPager
    )

List all blueprints.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_blueprints](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_list_blueprints)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_deployment_revisions
    
    
    list_deployment_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListDeploymentRevisionsRequest,
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
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListDeploymentRevisionsAsyncPager
    )

List deployment revisions of a given deployment.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_deployment_revisions](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_list_deployment_revisions)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_deployments
    
    
    list_deployments(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListDeploymentsRequest,
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
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListDeploymentsAsyncPager
    )

List all deployments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_deployments](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_list_deployments)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_edge_slms
    
    
    list_edge_slms(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListEdgeSlmsRequest,
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
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListEdgeSlmsAsyncPager
    )

Lists EdgeSlms in a given project and location.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_edge_slms](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_list_edge_slms)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_hydrated_deployments
    
    
    list_hydrated_deployments(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListHydratedDeploymentsRequest,
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
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListHydratedDeploymentsAsyncPager
    )

List all hydrated deployments present under a deployment.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_hydrated_deployments](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_list_hydrated_deployments)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_locations
    
    
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_list_locations)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_operations
    
    
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_list_operations)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_orchestration_clusters
    
    
    list_orchestration_clusters(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListOrchestrationClustersRequest,
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
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListOrchestrationClustersAsyncPager
    )

Lists OrchestrationClusters in a given project and location.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_orchestration_clusters](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_list_orchestration_clusters)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_public_blueprints
    
    
    list_public_blueprints(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListPublicBlueprintsRequest,
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
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListPublicBlueprintsAsyncPager
    )

Lists the blueprints in TNA's public catalog.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.list_public_blueprints](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_list_public_blueprints)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.orchestration_cluster_path
    
    
    orchestration_cluster_path(
        project: str, location: str, orchestration_cluster: str
    ) -> str

Returns a fully-qualified orchestration_cluster string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.orchestration_cluster_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_orchestration_cluster_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_blueprint_path
    
    
    parse_blueprint_path(path: str) -> typing.Dict[str, str]

Parses a blueprint path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_blueprint_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_parse_blueprint_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_parse_common_billing_account_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_parse_common_folder_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_parse_common_location_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_parse_common_organization_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_parse_common_project_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_deployment_path
    
    
    parse_deployment_path(path: str) -> typing.Dict[str, str]

Parses a deployment path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_parse_deployment_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_edge_slm_path
    
    
    parse_edge_slm_path(path: str) -> typing.Dict[str, str]

Parses a edge_slm path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_edge_slm_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_parse_edge_slm_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_hydrated_deployment_path
    
    
    parse_hydrated_deployment_path(path: str) -> typing.Dict[str, str]

Parses a hydrated_deployment path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_hydrated_deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_parse_hydrated_deployment_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_orchestration_cluster_path
    
    
    parse_orchestration_cluster_path(path: str) -> typing.Dict[str, str]

Parses a orchestration_cluster path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_orchestration_cluster_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_parse_orchestration_cluster_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_public_blueprint_path
    
    
    parse_public_blueprint_path(path: str) -> typing.Dict[str, str]

Parses a public_blueprint path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.parse_public_blueprint_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_parse_public_blueprint_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.propose_blueprint
    
    
    propose_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ProposeBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Blueprint

Proposes a blueprint for approval of changes.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.propose_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_propose_blueprint)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.public_blueprint_path
    
    
    public_blueprint_path(project: str, location: str, public_lueprint: str) -> str

Returns a fully-qualified public_blueprint string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.public_blueprint_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_public_blueprint_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.reject_blueprint
    
    
    reject_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.RejectBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Blueprint

Rejects a blueprint revision proposal and flips it back to Draft state.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.reject_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_reject_blueprint)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.remove_deployment
    
    
    remove_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.RemoveDeploymentRequest,
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

Removes the deployment by marking it as DELETING.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.remove_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_remove_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.rollback_deployment
    
    
    rollback_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.RollbackDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        revision_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Deployment

Rollback the active deployment to the given past approved deployment revision.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.rollback_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_rollback_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.search_blueprint_revisions
    
    
    search_blueprint_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.SearchBlueprintRevisionsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.SearchBlueprintRevisionsAsyncPager
    )

Searches across blueprint revisions.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.search_blueprint_revisions](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_search_blueprint_revisions)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.search_deployment_revisions
    
    
    search_deployment_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.SearchDeploymentRevisionsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.SearchDeploymentRevisionsAsyncPager
    )

Searches across deployment revisions.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.search_deployment_revisions](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_search_deployment_revisions)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.update_blueprint
    
    
    update_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.UpdateBlueprintRequest,
                dict,
            ]
        ] = None,
        *,
        blueprint: typing.Optional[
            google.cloud.telcoautomation_v1.types.telcoautomation.Blueprint
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Blueprint

Updates a blueprint.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.update_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_update_blueprint)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.update_deployment
    
    
    update_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.UpdateDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        deployment: typing.Optional[
            google.cloud.telcoautomation_v1.types.telcoautomation.Deployment
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Deployment

Updates a deployment.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.update_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_update_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.update_hydrated_deployment
    
    
    update_hydrated_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.UpdateHydratedDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        hydrated_deployment: typing.Optional[
            google.cloud.telcoautomation_v1.types.telcoautomation.HydratedDeployment
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.HydratedDeployment

Updates a hydrated deployment.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient.update_hydrated_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationAsyncClient_update_hydrated_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient
    
    
    TelcoAutomationClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.telcoautomation_v1.services.telco_automation.transports.base.TelcoAutomationTransport,
                typing.Callable[
                    [...],
                    google.cloud.telcoautomation_v1.services.telco_automation.transports.base.TelcoAutomationTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the telco automation client.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_TelcoAutomationClient)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient___exit__)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.apply_deployment
    
    
    apply_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ApplyDeploymentRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Deployment

Applies the deployment's YAML files to the parent orchestration cluster.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.apply_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_apply_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.apply_hydrated_deployment
    
    
    apply_hydrated_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ApplyHydratedDeploymentRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.HydratedDeployment

Applies a hydrated deployment to a workload cluster.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.apply_hydrated_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_apply_hydrated_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.approve_blueprint
    
    
    approve_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ApproveBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Blueprint

Approves a blueprint and commits a new revision.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.approve_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_approve_blueprint)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.blueprint_path
    
    
    blueprint_path(
        project: str, location: str, orchestration_cluster: str, blueprint: str
    ) -> str

Returns a fully-qualified blueprint string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.blueprint_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_blueprint_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.cancel_operation
    
    
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_cancel_operation)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_common_billing_account_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_common_folder_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_common_location_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_common_organization_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_common_project_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.compute_deployment_status
    
    
    compute_deployment_status(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ComputeDeploymentStatusRequest,
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
        google.cloud.telcoautomation_v1.types.telcoautomation.ComputeDeploymentStatusResponse
    )

Returns the requested deployment status.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.compute_deployment_status](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_compute_deployment_status)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.create_blueprint
    
    
    create_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.CreateBlueprintRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        blueprint: typing.Optional[
            google.cloud.telcoautomation_v1.types.telcoautomation.Blueprint
        ] = None,
        blueprint_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Blueprint

Creates a blueprint.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.create_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_create_blueprint)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.create_deployment
    
    
    create_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.CreateDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deployment: typing.Optional[
            google.cloud.telcoautomation_v1.types.telcoautomation.Deployment
        ] = None,
        deployment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Deployment

Creates a deployment.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.create_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_create_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.create_edge_slm
    
    
    create_edge_slm(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.CreateEdgeSlmRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        edge_slm: typing.Optional[
            google.cloud.telcoautomation_v1.types.telcoautomation.EdgeSlm
        ] = None,
        edge_slm_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new EdgeSlm in a given project and location.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.create_edge_slm](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_create_edge_slm)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.create_orchestration_cluster
    
    
    create_orchestration_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.CreateOrchestrationClusterRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        orchestration_cluster: typing.Optional[
            google.cloud.telcoautomation_v1.types.telcoautomation.OrchestrationCluster
        ] = None,
        orchestration_cluster_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new OrchestrationCluster in a given project and location.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.create_orchestration_cluster](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_create_orchestration_cluster)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.delete_blueprint
    
    
    delete_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.DeleteBlueprintRequest,
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

Deletes a blueprint and all its revisions.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.delete_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_delete_blueprint)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.delete_edge_slm
    
    
    delete_edge_slm(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.DeleteEdgeSlmRequest,
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

Deletes a single EdgeSlm.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.delete_edge_slm](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_delete_edge_slm)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.delete_operation
    
    
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_delete_operation)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.delete_orchestration_cluster
    
    
    delete_orchestration_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.DeleteOrchestrationClusterRequest,
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

Deletes a single OrchestrationCluster.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.delete_orchestration_cluster](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_delete_orchestration_cluster)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.deployment_path
    
    
    deployment_path(
        project: str, location: str, orchestration_cluster: str, deployment: str
    ) -> str

Returns a fully-qualified deployment string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_deployment_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.discard_blueprint_changes
    
    
    discard_blueprint_changes(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.DiscardBlueprintChangesRequest,
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
        google.cloud.telcoautomation_v1.types.telcoautomation.DiscardBlueprintChangesResponse
    )

Discards the changes in a blueprint and reverts the blueprint to the last approved blueprint revision.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.discard_blueprint_changes](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_discard_blueprint_changes)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.discard_deployment_changes
    
    
    discard_deployment_changes(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.DiscardDeploymentChangesRequest,
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
        google.cloud.telcoautomation_v1.types.telcoautomation.DiscardDeploymentChangesResponse
    )

Discards the changes in a deployment and reverts the deployment to the last approved deployment revision.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.discard_deployment_changes](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_discard_deployment_changes)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.edge_slm_path
    
    
    edge_slm_path(project: str, location: str, edge_slm: str) -> str

Returns a fully-qualified edge_slm string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.edge_slm_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_edge_slm_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_from_service_account_file)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_from_service_account_info)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_from_service_account_json)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_blueprint
    
    
    get_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.GetBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Blueprint

Returns the requested blueprint.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_get_blueprint)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_deployment
    
    
    get_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.GetDeploymentRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Deployment

Returns the requested deployment.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_get_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_edge_slm
    
    
    get_edge_slm(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.GetEdgeSlmRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.EdgeSlm

Gets details of a single EdgeSlm.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_edge_slm](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_get_edge_slm)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_hydrated_deployment
    
    
    get_hydrated_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.GetHydratedDeploymentRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.HydratedDeployment

Returns the requested hydrated deployment.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_hydrated_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_get_hydrated_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_location
    
    
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_get_location)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_get_mtls_endpoint_and_cert_source)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_operation
    
    
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_get_operation)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_orchestration_cluster
    
    
    get_orchestration_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.GetOrchestrationClusterRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.OrchestrationCluster

Gets details of a single OrchestrationCluster.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_orchestration_cluster](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_get_orchestration_cluster)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_public_blueprint
    
    
    get_public_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.GetPublicBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.PublicBlueprint

Returns the requested public blueprint.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.get_public_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_get_public_blueprint)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.hydrated_deployment_path
    
    
    hydrated_deployment_path(
        project: str,
        location: str,
        orchestration_cluster: str,
        deployment: str,
        hydrated_deployment: str,
    ) -> str

Returns a fully-qualified hydrated_deployment string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.hydrated_deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_hydrated_deployment_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_blueprint_revisions
    
    
    list_blueprint_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListBlueprintRevisionsRequest,
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
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListBlueprintRevisionsPager
    )

List blueprint revisions of a given blueprint.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_blueprint_revisions](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_list_blueprint_revisions)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_blueprints
    
    
    list_blueprints(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListBlueprintsRequest,
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
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListBlueprintsPager
    )

List all blueprints.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_blueprints](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_list_blueprints)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_deployment_revisions
    
    
    list_deployment_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListDeploymentRevisionsRequest,
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
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListDeploymentRevisionsPager
    )

List deployment revisions of a given deployment.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_deployment_revisions](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_list_deployment_revisions)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_deployments
    
    
    list_deployments(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListDeploymentsRequest,
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
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListDeploymentsPager
    )

List all deployments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_deployments](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_list_deployments)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_edge_slms
    
    
    list_edge_slms(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListEdgeSlmsRequest,
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
    ) -> google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListEdgeSlmsPager

Lists EdgeSlms in a given project and location.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_edge_slms](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_list_edge_slms)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_hydrated_deployments
    
    
    list_hydrated_deployments(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListHydratedDeploymentsRequest,
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
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListHydratedDeploymentsPager
    )

List all hydrated deployments present under a deployment.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_hydrated_deployments](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_list_hydrated_deployments)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_locations
    
    
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_list_locations)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_operations
    
    
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_list_operations)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_orchestration_clusters
    
    
    list_orchestration_clusters(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListOrchestrationClustersRequest,
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
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListOrchestrationClustersPager
    )

Lists OrchestrationClusters in a given project and location.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_orchestration_clusters](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_list_orchestration_clusters)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_public_blueprints
    
    
    list_public_blueprints(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListPublicBlueprintsRequest,
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
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListPublicBlueprintsPager
    )

Lists the blueprints in TNA's public catalog.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.list_public_blueprints](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_list_public_blueprints)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.orchestration_cluster_path
    
    
    orchestration_cluster_path(
        project: str, location: str, orchestration_cluster: str
    ) -> str

Returns a fully-qualified orchestration_cluster string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.orchestration_cluster_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_orchestration_cluster_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_blueprint_path
    
    
    parse_blueprint_path(path: str) -> typing.Dict[str, str]

Parses a blueprint path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_blueprint_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_parse_blueprint_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_parse_common_billing_account_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_parse_common_folder_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_parse_common_location_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_parse_common_organization_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_parse_common_project_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_deployment_path
    
    
    parse_deployment_path(path: str) -> typing.Dict[str, str]

Parses a deployment path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_parse_deployment_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_edge_slm_path
    
    
    parse_edge_slm_path(path: str) -> typing.Dict[str, str]

Parses a edge_slm path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_edge_slm_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_parse_edge_slm_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_hydrated_deployment_path
    
    
    parse_hydrated_deployment_path(path: str) -> typing.Dict[str, str]

Parses a hydrated_deployment path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_hydrated_deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_parse_hydrated_deployment_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_orchestration_cluster_path
    
    
    parse_orchestration_cluster_path(path: str) -> typing.Dict[str, str]

Parses a orchestration_cluster path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_orchestration_cluster_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_parse_orchestration_cluster_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_public_blueprint_path
    
    
    parse_public_blueprint_path(path: str) -> typing.Dict[str, str]

Parses a public_blueprint path into its component segments.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.parse_public_blueprint_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_parse_public_blueprint_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.propose_blueprint
    
    
    propose_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.ProposeBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Blueprint

Proposes a blueprint for approval of changes.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.propose_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_propose_blueprint)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.public_blueprint_path
    
    
    public_blueprint_path(project: str, location: str, public_lueprint: str) -> str

Returns a fully-qualified public_blueprint string.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.public_blueprint_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_public_blueprint_path)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.reject_blueprint
    
    
    reject_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.RejectBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Blueprint

Rejects a blueprint revision proposal and flips it back to Draft state.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.reject_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_reject_blueprint)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.remove_deployment
    
    
    remove_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.RemoveDeploymentRequest,
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

Removes the deployment by marking it as DELETING.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.remove_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_remove_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.rollback_deployment
    
    
    rollback_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.RollbackDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        revision_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Deployment

Rollback the active deployment to the given past approved deployment revision.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.rollback_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_rollback_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.search_blueprint_revisions
    
    
    search_blueprint_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.SearchBlueprintRevisionsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.SearchBlueprintRevisionsPager
    )

Searches across blueprint revisions.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.search_blueprint_revisions](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_search_blueprint_revisions)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.search_deployment_revisions
    
    
    search_deployment_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.SearchDeploymentRevisionsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.telcoautomation_v1.services.telco_automation.pagers.SearchDeploymentRevisionsPager
    )

Searches across deployment revisions.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.search_deployment_revisions](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_search_deployment_revisions)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.update_blueprint
    
    
    update_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.UpdateBlueprintRequest,
                dict,
            ]
        ] = None,
        *,
        blueprint: typing.Optional[
            google.cloud.telcoautomation_v1.types.telcoautomation.Blueprint
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Blueprint

Updates a blueprint.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.update_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_update_blueprint)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.update_deployment
    
    
    update_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.UpdateDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        deployment: typing.Optional[
            google.cloud.telcoautomation_v1.types.telcoautomation.Deployment
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.Deployment

Updates a deployment.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.update_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_update_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.update_hydrated_deployment
    
    
    update_hydrated_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1.types.telcoautomation.UpdateHydratedDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        hydrated_deployment: typing.Optional[
            google.cloud.telcoautomation_v1.types.telcoautomation.HydratedDeployment
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
    ) -> google.cloud.telcoautomation_v1.types.telcoautomation.HydratedDeployment

Updates a hydrated deployment.

See more: [google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient.update_hydrated_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1_services_telco_automation_TelcoAutomationClient_update_hydrated_deployment)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListBlueprintRevisionsAsyncPager
    
    
    ListBlueprintRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListBlueprintRevisionsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.ListBlueprintRevisionsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.ListBlueprintRevisionsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListBlueprintRevisionsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListBlueprintRevisionsAsyncPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_ListBlueprintRevisionsAsyncPager_ListBlueprintRevisionsAsyncPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListBlueprintRevisionsPager
    
    
    ListBlueprintRevisionsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1.types.telcoautomation.ListBlueprintRevisionsResponse,
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.ListBlueprintRevisionsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.ListBlueprintRevisionsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListBlueprintRevisionsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListBlueprintRevisionsPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_ListBlueprintRevisionsPager_ListBlueprintRevisionsPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListBlueprintsAsyncPager
    
    
    ListBlueprintsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListBlueprintsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.ListBlueprintsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.ListBlueprintsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListBlueprintsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListBlueprintsAsyncPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_ListBlueprintsAsyncPager_ListBlueprintsAsyncPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListBlueprintsPager
    
    
    ListBlueprintsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1.types.telcoautomation.ListBlueprintsResponse,
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.ListBlueprintsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.ListBlueprintsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListBlueprintsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListBlueprintsPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_ListBlueprintsPager_ListBlueprintsPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListDeploymentRevisionsAsyncPager
    
    
    ListDeploymentRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListDeploymentRevisionsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.ListDeploymentRevisionsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.ListDeploymentRevisionsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListDeploymentRevisionsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListDeploymentRevisionsAsyncPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_ListDeploymentRevisionsAsyncPager_ListDeploymentRevisionsAsyncPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListDeploymentRevisionsPager
    
    
    ListDeploymentRevisionsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1.types.telcoautomation.ListDeploymentRevisionsResponse,
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.ListDeploymentRevisionsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.ListDeploymentRevisionsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListDeploymentRevisionsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListDeploymentRevisionsPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_ListDeploymentRevisionsPager_ListDeploymentRevisionsPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListDeploymentsAsyncPager
    
    
    ListDeploymentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListDeploymentsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.ListDeploymentsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.ListDeploymentsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListDeploymentsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListDeploymentsAsyncPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_ListDeploymentsAsyncPager_ListDeploymentsAsyncPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListDeploymentsPager
    
    
    ListDeploymentsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1.types.telcoautomation.ListDeploymentsResponse,
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.ListDeploymentsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.ListDeploymentsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListDeploymentsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListDeploymentsPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_ListDeploymentsPager_ListDeploymentsPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListEdgeSlmsAsyncPager
    
    
    ListEdgeSlmsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListEdgeSlmsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.ListEdgeSlmsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.ListEdgeSlmsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListEdgeSlmsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListEdgeSlmsAsyncPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_ListEdgeSlmsAsyncPager_ListEdgeSlmsAsyncPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListEdgeSlmsPager
    
    
    ListEdgeSlmsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1.types.telcoautomation.ListEdgeSlmsResponse,
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.ListEdgeSlmsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.ListEdgeSlmsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListEdgeSlmsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListEdgeSlmsPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_ListEdgeSlmsPager_ListEdgeSlmsPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListHydratedDeploymentsAsyncPager
    
    
    ListHydratedDeploymentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListHydratedDeploymentsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.ListHydratedDeploymentsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.ListHydratedDeploymentsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListHydratedDeploymentsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListHydratedDeploymentsAsyncPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_ListHydratedDeploymentsAsyncPager_ListHydratedDeploymentsAsyncPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListHydratedDeploymentsPager
    
    
    ListHydratedDeploymentsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1.types.telcoautomation.ListHydratedDeploymentsResponse,
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.ListHydratedDeploymentsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.ListHydratedDeploymentsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListHydratedDeploymentsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListHydratedDeploymentsPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_ListHydratedDeploymentsPager_ListHydratedDeploymentsPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListOrchestrationClustersAsyncPager
    
    
    ListOrchestrationClustersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListOrchestrationClustersResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.ListOrchestrationClustersRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.ListOrchestrationClustersResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListOrchestrationClustersAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListOrchestrationClustersAsyncPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_ListOrchestrationClustersAsyncPager_ListOrchestrationClustersAsyncPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListOrchestrationClustersPager
    
    
    ListOrchestrationClustersPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1.types.telcoautomation.ListOrchestrationClustersResponse,
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.ListOrchestrationClustersRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.ListOrchestrationClustersResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListOrchestrationClustersPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListOrchestrationClustersPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_ListOrchestrationClustersPager_ListOrchestrationClustersPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListPublicBlueprintsAsyncPager
    
    
    ListPublicBlueprintsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1.types.telcoautomation.ListPublicBlueprintsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.ListPublicBlueprintsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.ListPublicBlueprintsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListPublicBlueprintsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListPublicBlueprintsAsyncPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_ListPublicBlueprintsAsyncPager_ListPublicBlueprintsAsyncPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListPublicBlueprintsPager
    
    
    ListPublicBlueprintsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1.types.telcoautomation.ListPublicBlueprintsResponse,
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.ListPublicBlueprintsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.ListPublicBlueprintsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListPublicBlueprintsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.ListPublicBlueprintsPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_ListPublicBlueprintsPager_ListPublicBlueprintsPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.SearchBlueprintRevisionsAsyncPager
    
    
    SearchBlueprintRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1.types.telcoautomation.SearchBlueprintRevisionsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.SearchBlueprintRevisionsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.SearchBlueprintRevisionsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.SearchBlueprintRevisionsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.SearchBlueprintRevisionsAsyncPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_SearchBlueprintRevisionsAsyncPager_SearchBlueprintRevisionsAsyncPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.SearchBlueprintRevisionsPager
    
    
    SearchBlueprintRevisionsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1.types.telcoautomation.SearchBlueprintRevisionsResponse,
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.SearchBlueprintRevisionsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.SearchBlueprintRevisionsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.SearchBlueprintRevisionsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.SearchBlueprintRevisionsPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_SearchBlueprintRevisionsPager_SearchBlueprintRevisionsPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.SearchDeploymentRevisionsAsyncPager
    
    
    SearchDeploymentRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1.types.telcoautomation.SearchDeploymentRevisionsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.SearchDeploymentRevisionsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.SearchDeploymentRevisionsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.SearchDeploymentRevisionsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.SearchDeploymentRevisionsAsyncPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_SearchDeploymentRevisionsAsyncPager_SearchDeploymentRevisionsAsyncPager)

### google.cloud.telcoautomation_v1.services.telco_automation.pagers.SearchDeploymentRevisionsPager
    
    
    SearchDeploymentRevisionsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1.types.telcoautomation.SearchDeploymentRevisionsResponse,
        ],
        request: google.cloud.telcoautomation_v1.types.telcoautomation.SearchDeploymentRevisionsRequest,
        response: google.cloud.telcoautomation_v1.types.telcoautomation.SearchDeploymentRevisionsResponse,
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

See more: [google.cloud.telcoautomation_v1.services.telco_automation.pagers.SearchDeploymentRevisionsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.services.telco_automation.pagers.SearchDeploymentRevisionsPager#google_cloud_telcoautomation_v1_services_telco_automation_pagers_SearchDeploymentRevisionsPager_SearchDeploymentRevisionsPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient
    
    
    TelcoAutomationAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.telcoautomation_v1alpha1.services.telco_automation.transports.base.TelcoAutomationTransport,
                typing.Callable[
                    [...],
                    google.cloud.telcoautomation_v1alpha1.services.telco_automation.transports.base.TelcoAutomationTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the telco automation async client.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_TelcoAutomationAsyncClient)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.apply_deployment
    
    
    apply_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ApplyDeploymentRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Deployment

Applies the deployment's YAML files to the parent orchestration cluster.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.apply_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_apply_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.apply_hydrated_deployment
    
    
    apply_hydrated_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ApplyHydratedDeploymentRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.HydratedDeployment

Applies a hydrated deployment to a workload cluster.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.apply_hydrated_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_apply_hydrated_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.approve_blueprint
    
    
    approve_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ApproveBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Blueprint

Approves a blueprint and commits a new revision.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.approve_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_approve_blueprint)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.blueprint_path
    
    
    blueprint_path(
        project: str, location: str, orchestration_cluster: str, blueprint: str
    ) -> str

Returns a fully-qualified blueprint string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.blueprint_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_blueprint_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_cancel_operation)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_common_billing_account_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_common_folder_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_common_location_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_common_organization_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_common_project_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.compute_deployment_status
    
    
    compute_deployment_status(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ComputeDeploymentStatusRequest,
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
        google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ComputeDeploymentStatusResponse
    )

Returns the requested deployment status.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.compute_deployment_status](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_compute_deployment_status)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.create_blueprint
    
    
    create_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.CreateBlueprintRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        blueprint: typing.Optional[
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Blueprint
        ] = None,
        blueprint_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Blueprint

Creates a blueprint.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.create_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_create_blueprint)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.create_deployment
    
    
    create_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.CreateDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deployment: typing.Optional[
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Deployment
        ] = None,
        deployment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Deployment

Creates a deployment.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.create_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_create_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.create_edge_slm
    
    
    create_edge_slm(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.CreateEdgeSlmRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        edge_slm: typing.Optional[
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.EdgeSlm
        ] = None,
        edge_slm_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new EdgeSlm in a given project and location.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.create_edge_slm](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_create_edge_slm)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.create_orchestration_cluster
    
    
    create_orchestration_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.CreateOrchestrationClusterRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        orchestration_cluster: typing.Optional[
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.OrchestrationCluster
        ] = None,
        orchestration_cluster_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new OrchestrationCluster in a given project and location.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.create_orchestration_cluster](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_create_orchestration_cluster)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.delete_blueprint
    
    
    delete_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.DeleteBlueprintRequest,
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

Deletes a blueprint and all its revisions.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.delete_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_delete_blueprint)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.delete_edge_slm
    
    
    delete_edge_slm(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.DeleteEdgeSlmRequest,
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

Deletes a single EdgeSlm.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.delete_edge_slm](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_delete_edge_slm)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.delete_operation
    
    
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_delete_operation)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.delete_orchestration_cluster
    
    
    delete_orchestration_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.DeleteOrchestrationClusterRequest,
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

Deletes a single OrchestrationCluster.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.delete_orchestration_cluster](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_delete_orchestration_cluster)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.deployment_path
    
    
    deployment_path(
        project: str, location: str, orchestration_cluster: str, deployment: str
    ) -> str

Returns a fully-qualified deployment string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_deployment_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.discard_blueprint_changes
    
    
    discard_blueprint_changes(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.DiscardBlueprintChangesRequest,
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
        google.cloud.telcoautomation_v1alpha1.types.telcoautomation.DiscardBlueprintChangesResponse
    )

Discards the changes in a blueprint and reverts the blueprint to the last approved blueprint revision.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.discard_blueprint_changes](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_discard_blueprint_changes)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.discard_deployment_changes
    
    
    discard_deployment_changes(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.DiscardDeploymentChangesRequest,
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
        google.cloud.telcoautomation_v1alpha1.types.telcoautomation.DiscardDeploymentChangesResponse
    )

Discards the changes in a deployment and reverts the deployment to the last approved deployment revision.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.discard_deployment_changes](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_discard_deployment_changes)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.edge_slm_path
    
    
    edge_slm_path(project: str, location: str, edge_slm: str) -> str

Returns a fully-qualified edge_slm string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.edge_slm_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_edge_slm_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_from_service_account_file)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_from_service_account_info)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_from_service_account_json)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_blueprint
    
    
    get_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.GetBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Blueprint

Returns the requested blueprint.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_get_blueprint)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_deployment
    
    
    get_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.GetDeploymentRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Deployment

Returns the requested deployment.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_get_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_edge_slm
    
    
    get_edge_slm(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.GetEdgeSlmRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.EdgeSlm

Gets details of a single EdgeSlm.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_edge_slm](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_get_edge_slm)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_hydrated_deployment
    
    
    get_hydrated_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.GetHydratedDeploymentRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.HydratedDeployment

Returns the requested hydrated deployment.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_hydrated_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_get_hydrated_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_location
    
    
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_get_location)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_operation
    
    
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_get_operation)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_orchestration_cluster
    
    
    get_orchestration_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.GetOrchestrationClusterRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.OrchestrationCluster

Gets details of a single OrchestrationCluster.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_orchestration_cluster](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_get_orchestration_cluster)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_public_blueprint
    
    
    get_public_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.GetPublicBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.PublicBlueprint

Returns the requested public blueprint.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_public_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_get_public_blueprint)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.transports.base.TelcoAutomationTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_get_transport_class)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.hydrated_deployment_path
    
    
    hydrated_deployment_path(
        project: str,
        location: str,
        orchestration_cluster: str,
        deployment: str,
        hydrated_deployment: str,
    ) -> str

Returns a fully-qualified hydrated_deployment string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.hydrated_deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_hydrated_deployment_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_blueprint_revisions
    
    
    list_blueprint_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListBlueprintRevisionsRequest,
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
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListBlueprintRevisionsAsyncPager
    )

List blueprint revisions of a given blueprint.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_blueprint_revisions](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_list_blueprint_revisions)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_blueprints
    
    
    list_blueprints(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListBlueprintsRequest,
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
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListBlueprintsAsyncPager
    )

List all blueprints.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_blueprints](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_list_blueprints)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_deployment_revisions
    
    
    list_deployment_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListDeploymentRevisionsRequest,
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
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListDeploymentRevisionsAsyncPager
    )

List deployment revisions of a given deployment.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_deployment_revisions](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_list_deployment_revisions)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_deployments
    
    
    list_deployments(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListDeploymentsRequest,
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
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListDeploymentsAsyncPager
    )

List all deployments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_deployments](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_list_deployments)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_edge_slms
    
    
    list_edge_slms(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListEdgeSlmsRequest,
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
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListEdgeSlmsAsyncPager
    )

Lists EdgeSlms in a given project and location.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_edge_slms](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_list_edge_slms)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_hydrated_deployments
    
    
    list_hydrated_deployments(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListHydratedDeploymentsRequest,
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
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListHydratedDeploymentsAsyncPager
    )

List all hydrated deployments present under a deployment.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_hydrated_deployments](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_list_hydrated_deployments)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_locations
    
    
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_list_locations)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_operations
    
    
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_list_operations)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_orchestration_clusters
    
    
    list_orchestration_clusters(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListOrchestrationClustersRequest,
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
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListOrchestrationClustersAsyncPager
    )

Lists OrchestrationClusters in a given project and location.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_orchestration_clusters](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_list_orchestration_clusters)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_public_blueprints
    
    
    list_public_blueprints(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListPublicBlueprintsRequest,
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
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListPublicBlueprintsAsyncPager
    )

Lists the blueprints in TNA's public catalog.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.list_public_blueprints](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_list_public_blueprints)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.orchestration_cluster_path
    
    
    orchestration_cluster_path(
        project: str, location: str, orchestration_cluster: str
    ) -> str

Returns a fully-qualified orchestration_cluster string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.orchestration_cluster_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_orchestration_cluster_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_blueprint_path
    
    
    parse_blueprint_path(path: str) -> typing.Dict[str, str]

Parses a blueprint path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_blueprint_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_parse_blueprint_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_parse_common_billing_account_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_parse_common_folder_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_parse_common_location_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_parse_common_organization_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_parse_common_project_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_deployment_path
    
    
    parse_deployment_path(path: str) -> typing.Dict[str, str]

Parses a deployment path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_parse_deployment_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_edge_slm_path
    
    
    parse_edge_slm_path(path: str) -> typing.Dict[str, str]

Parses a edge_slm path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_edge_slm_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_parse_edge_slm_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_hydrated_deployment_path
    
    
    parse_hydrated_deployment_path(path: str) -> typing.Dict[str, str]

Parses a hydrated_deployment path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_hydrated_deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_parse_hydrated_deployment_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_orchestration_cluster_path
    
    
    parse_orchestration_cluster_path(path: str) -> typing.Dict[str, str]

Parses a orchestration_cluster path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_orchestration_cluster_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_parse_orchestration_cluster_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_public_blueprint_path
    
    
    parse_public_blueprint_path(path: str) -> typing.Dict[str, str]

Parses a public_blueprint path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.parse_public_blueprint_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_parse_public_blueprint_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.propose_blueprint
    
    
    propose_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ProposeBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Blueprint

Proposes a blueprint for approval of changes.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.propose_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_propose_blueprint)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.public_blueprint_path
    
    
    public_blueprint_path(project: str, location: str, public_lueprint: str) -> str

Returns a fully-qualified public_blueprint string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.public_blueprint_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_public_blueprint_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.reject_blueprint
    
    
    reject_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.RejectBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Blueprint

Rejects a blueprint revision proposal and flips it back to Draft state.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.reject_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_reject_blueprint)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.remove_deployment
    
    
    remove_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.RemoveDeploymentRequest,
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

Removes the deployment by marking it as DELETING.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.remove_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_remove_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.rollback_deployment
    
    
    rollback_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.RollbackDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        revision_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Deployment

Rollback the active deployment to the given past approved deployment revision.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.rollback_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_rollback_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.search_blueprint_revisions
    
    
    search_blueprint_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.SearchBlueprintRevisionsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.SearchBlueprintRevisionsAsyncPager
    )

Searches across blueprint revisions.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.search_blueprint_revisions](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_search_blueprint_revisions)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.search_deployment_revisions
    
    
    search_deployment_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.SearchDeploymentRevisionsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.SearchDeploymentRevisionsAsyncPager
    )

Searches across deployment revisions.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.search_deployment_revisions](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_search_deployment_revisions)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.update_blueprint
    
    
    update_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.UpdateBlueprintRequest,
                dict,
            ]
        ] = None,
        *,
        blueprint: typing.Optional[
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Blueprint
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Blueprint

Updates a blueprint.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.update_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_update_blueprint)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.update_deployment
    
    
    update_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.UpdateDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        deployment: typing.Optional[
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Deployment
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Deployment

Updates a deployment.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.update_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_update_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.update_hydrated_deployment
    
    
    update_hydrated_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.UpdateHydratedDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        hydrated_deployment: typing.Optional[
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.HydratedDeployment
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.HydratedDeployment

Updates a hydrated deployment.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient.update_hydrated_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationAsyncClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationAsyncClient_update_hydrated_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient
    
    
    TelcoAutomationClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.telcoautomation_v1alpha1.services.telco_automation.transports.base.TelcoAutomationTransport,
                typing.Callable[
                    [...],
                    google.cloud.telcoautomation_v1alpha1.services.telco_automation.transports.base.TelcoAutomationTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the telco automation client.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_TelcoAutomationClient)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient___exit__)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.apply_deployment
    
    
    apply_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ApplyDeploymentRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Deployment

Applies the deployment's YAML files to the parent orchestration cluster.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.apply_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_apply_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.apply_hydrated_deployment
    
    
    apply_hydrated_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ApplyHydratedDeploymentRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.HydratedDeployment

Applies a hydrated deployment to a workload cluster.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.apply_hydrated_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_apply_hydrated_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.approve_blueprint
    
    
    approve_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ApproveBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Blueprint

Approves a blueprint and commits a new revision.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.approve_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_approve_blueprint)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.blueprint_path
    
    
    blueprint_path(
        project: str, location: str, orchestration_cluster: str, blueprint: str
    ) -> str

Returns a fully-qualified blueprint string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.blueprint_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_blueprint_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.cancel_operation
    
    
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_cancel_operation)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_common_billing_account_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_common_folder_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_common_location_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_common_organization_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_common_project_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.compute_deployment_status
    
    
    compute_deployment_status(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ComputeDeploymentStatusRequest,
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
        google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ComputeDeploymentStatusResponse
    )

Returns the requested deployment status.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.compute_deployment_status](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_compute_deployment_status)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.create_blueprint
    
    
    create_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.CreateBlueprintRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        blueprint: typing.Optional[
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Blueprint
        ] = None,
        blueprint_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Blueprint

Creates a blueprint.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.create_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_create_blueprint)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.create_deployment
    
    
    create_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.CreateDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deployment: typing.Optional[
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Deployment
        ] = None,
        deployment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Deployment

Creates a deployment.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.create_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_create_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.create_edge_slm
    
    
    create_edge_slm(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.CreateEdgeSlmRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        edge_slm: typing.Optional[
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.EdgeSlm
        ] = None,
        edge_slm_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new EdgeSlm in a given project and location.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.create_edge_slm](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_create_edge_slm)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.create_orchestration_cluster
    
    
    create_orchestration_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.CreateOrchestrationClusterRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        orchestration_cluster: typing.Optional[
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.OrchestrationCluster
        ] = None,
        orchestration_cluster_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new OrchestrationCluster in a given project and location.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.create_orchestration_cluster](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_create_orchestration_cluster)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.delete_blueprint
    
    
    delete_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.DeleteBlueprintRequest,
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

Deletes a blueprint and all its revisions.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.delete_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_delete_blueprint)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.delete_edge_slm
    
    
    delete_edge_slm(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.DeleteEdgeSlmRequest,
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

Deletes a single EdgeSlm.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.delete_edge_slm](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_delete_edge_slm)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.delete_operation
    
    
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_delete_operation)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.delete_orchestration_cluster
    
    
    delete_orchestration_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.DeleteOrchestrationClusterRequest,
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

Deletes a single OrchestrationCluster.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.delete_orchestration_cluster](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_delete_orchestration_cluster)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.deployment_path
    
    
    deployment_path(
        project: str, location: str, orchestration_cluster: str, deployment: str
    ) -> str

Returns a fully-qualified deployment string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_deployment_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.discard_blueprint_changes
    
    
    discard_blueprint_changes(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.DiscardBlueprintChangesRequest,
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
        google.cloud.telcoautomation_v1alpha1.types.telcoautomation.DiscardBlueprintChangesResponse
    )

Discards the changes in a blueprint and reverts the blueprint to the last approved blueprint revision.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.discard_blueprint_changes](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_discard_blueprint_changes)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.discard_deployment_changes
    
    
    discard_deployment_changes(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.DiscardDeploymentChangesRequest,
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
        google.cloud.telcoautomation_v1alpha1.types.telcoautomation.DiscardDeploymentChangesResponse
    )

Discards the changes in a deployment and reverts the deployment to the last approved deployment revision.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.discard_deployment_changes](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_discard_deployment_changes)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.edge_slm_path
    
    
    edge_slm_path(project: str, location: str, edge_slm: str) -> str

Returns a fully-qualified edge_slm string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.edge_slm_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_edge_slm_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_from_service_account_file)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_from_service_account_info)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_from_service_account_json)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_blueprint
    
    
    get_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.GetBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Blueprint

Returns the requested blueprint.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_get_blueprint)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_deployment
    
    
    get_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.GetDeploymentRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Deployment

Returns the requested deployment.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_get_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_edge_slm
    
    
    get_edge_slm(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.GetEdgeSlmRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.EdgeSlm

Gets details of a single EdgeSlm.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_edge_slm](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_get_edge_slm)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_hydrated_deployment
    
    
    get_hydrated_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.GetHydratedDeploymentRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.HydratedDeployment

Returns the requested hydrated deployment.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_hydrated_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_get_hydrated_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_location
    
    
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_get_location)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_get_mtls_endpoint_and_cert_source)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_operation
    
    
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_get_operation)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_orchestration_cluster
    
    
    get_orchestration_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.GetOrchestrationClusterRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.OrchestrationCluster

Gets details of a single OrchestrationCluster.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_orchestration_cluster](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_get_orchestration_cluster)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_public_blueprint
    
    
    get_public_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.GetPublicBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.PublicBlueprint

Returns the requested public blueprint.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.get_public_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_get_public_blueprint)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.hydrated_deployment_path
    
    
    hydrated_deployment_path(
        project: str,
        location: str,
        orchestration_cluster: str,
        deployment: str,
        hydrated_deployment: str,
    ) -> str

Returns a fully-qualified hydrated_deployment string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.hydrated_deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_hydrated_deployment_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_blueprint_revisions
    
    
    list_blueprint_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListBlueprintRevisionsRequest,
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
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListBlueprintRevisionsPager
    )

List blueprint revisions of a given blueprint.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_blueprint_revisions](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_list_blueprint_revisions)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_blueprints
    
    
    list_blueprints(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListBlueprintsRequest,
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
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListBlueprintsPager
    )

List all blueprints.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_blueprints](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_list_blueprints)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_deployment_revisions
    
    
    list_deployment_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListDeploymentRevisionsRequest,
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
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListDeploymentRevisionsPager
    )

List deployment revisions of a given deployment.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_deployment_revisions](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_list_deployment_revisions)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_deployments
    
    
    list_deployments(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListDeploymentsRequest,
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
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListDeploymentsPager
    )

List all deployments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_deployments](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_list_deployments)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_edge_slms
    
    
    list_edge_slms(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListEdgeSlmsRequest,
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
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListEdgeSlmsPager
    )

Lists EdgeSlms in a given project and location.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_edge_slms](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_list_edge_slms)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_hydrated_deployments
    
    
    list_hydrated_deployments(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListHydratedDeploymentsRequest,
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
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListHydratedDeploymentsPager
    )

List all hydrated deployments present under a deployment.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_hydrated_deployments](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_list_hydrated_deployments)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_locations
    
    
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_list_locations)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_operations
    
    
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_list_operations)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_orchestration_clusters
    
    
    list_orchestration_clusters(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListOrchestrationClustersRequest,
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
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListOrchestrationClustersPager
    )

Lists OrchestrationClusters in a given project and location.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_orchestration_clusters](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_list_orchestration_clusters)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_public_blueprints
    
    
    list_public_blueprints(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListPublicBlueprintsRequest,
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
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListPublicBlueprintsPager
    )

Lists the blueprints in TNA's public catalog.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.list_public_blueprints](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_list_public_blueprints)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.orchestration_cluster_path
    
    
    orchestration_cluster_path(
        project: str, location: str, orchestration_cluster: str
    ) -> str

Returns a fully-qualified orchestration_cluster string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.orchestration_cluster_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_orchestration_cluster_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_blueprint_path
    
    
    parse_blueprint_path(path: str) -> typing.Dict[str, str]

Parses a blueprint path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_blueprint_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_parse_blueprint_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_parse_common_billing_account_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_parse_common_folder_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_parse_common_location_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_parse_common_organization_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_parse_common_project_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_deployment_path
    
    
    parse_deployment_path(path: str) -> typing.Dict[str, str]

Parses a deployment path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_parse_deployment_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_edge_slm_path
    
    
    parse_edge_slm_path(path: str) -> typing.Dict[str, str]

Parses a edge_slm path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_edge_slm_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_parse_edge_slm_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_hydrated_deployment_path
    
    
    parse_hydrated_deployment_path(path: str) -> typing.Dict[str, str]

Parses a hydrated_deployment path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_hydrated_deployment_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_parse_hydrated_deployment_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_orchestration_cluster_path
    
    
    parse_orchestration_cluster_path(path: str) -> typing.Dict[str, str]

Parses a orchestration_cluster path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_orchestration_cluster_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_parse_orchestration_cluster_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_public_blueprint_path
    
    
    parse_public_blueprint_path(path: str) -> typing.Dict[str, str]

Parses a public_blueprint path into its component segments.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.parse_public_blueprint_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_parse_public_blueprint_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.propose_blueprint
    
    
    propose_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ProposeBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Blueprint

Proposes a blueprint for approval of changes.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.propose_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_propose_blueprint)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.public_blueprint_path
    
    
    public_blueprint_path(project: str, location: str, public_lueprint: str) -> str

Returns a fully-qualified public_blueprint string.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.public_blueprint_path](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_public_blueprint_path)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.reject_blueprint
    
    
    reject_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.RejectBlueprintRequest,
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Blueprint

Rejects a blueprint revision proposal and flips it back to Draft state.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.reject_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_reject_blueprint)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.remove_deployment
    
    
    remove_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.RemoveDeploymentRequest,
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

Removes the deployment by marking it as DELETING.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.remove_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_remove_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.rollback_deployment
    
    
    rollback_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.RollbackDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        revision_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Deployment

Rollback the active deployment to the given past approved deployment revision.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.rollback_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_rollback_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.search_blueprint_revisions
    
    
    search_blueprint_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.SearchBlueprintRevisionsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.SearchBlueprintRevisionsPager
    )

Searches across blueprint revisions.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.search_blueprint_revisions](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_search_blueprint_revisions)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.search_deployment_revisions
    
    
    search_deployment_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.SearchDeploymentRevisionsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.SearchDeploymentRevisionsPager
    )

Searches across deployment revisions.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.search_deployment_revisions](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_search_deployment_revisions)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.update_blueprint
    
    
    update_blueprint(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.UpdateBlueprintRequest,
                dict,
            ]
        ] = None,
        *,
        blueprint: typing.Optional[
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Blueprint
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Blueprint

Updates a blueprint.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.update_blueprint](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_update_blueprint)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.update_deployment
    
    
    update_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.UpdateDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        deployment: typing.Optional[
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Deployment
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.Deployment

Updates a deployment.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.update_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_update_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.update_hydrated_deployment
    
    
    update_hydrated_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.UpdateHydratedDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        hydrated_deployment: typing.Optional[
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.HydratedDeployment
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
    ) -> google.cloud.telcoautomation_v1alpha1.types.telcoautomation.HydratedDeployment

Updates a hydrated deployment.

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient.update_hydrated_deployment](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.TelcoAutomationClient#google_cloud_telcoautomation_v1alpha1_services_telco_automation_TelcoAutomationClient_update_hydrated_deployment)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListBlueprintRevisionsAsyncPager
    
    
    ListBlueprintRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListBlueprintRevisionsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListBlueprintRevisionsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListBlueprintRevisionsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListBlueprintRevisionsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListBlueprintRevisionsAsyncPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_ListBlueprintRevisionsAsyncPager_ListBlueprintRevisionsAsyncPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListBlueprintRevisionsPager
    
    
    ListBlueprintRevisionsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListBlueprintRevisionsResponse,
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListBlueprintRevisionsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListBlueprintRevisionsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListBlueprintRevisionsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListBlueprintRevisionsPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_ListBlueprintRevisionsPager_ListBlueprintRevisionsPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListBlueprintsAsyncPager
    
    
    ListBlueprintsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListBlueprintsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListBlueprintsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListBlueprintsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListBlueprintsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListBlueprintsAsyncPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_ListBlueprintsAsyncPager_ListBlueprintsAsyncPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListBlueprintsPager
    
    
    ListBlueprintsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListBlueprintsResponse,
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListBlueprintsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListBlueprintsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListBlueprintsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListBlueprintsPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_ListBlueprintsPager_ListBlueprintsPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListDeploymentRevisionsAsyncPager
    
    
    ListDeploymentRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListDeploymentRevisionsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListDeploymentRevisionsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListDeploymentRevisionsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListDeploymentRevisionsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListDeploymentRevisionsAsyncPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_ListDeploymentRevisionsAsyncPager_ListDeploymentRevisionsAsyncPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListDeploymentRevisionsPager
    
    
    ListDeploymentRevisionsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListDeploymentRevisionsResponse,
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListDeploymentRevisionsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListDeploymentRevisionsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListDeploymentRevisionsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListDeploymentRevisionsPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_ListDeploymentRevisionsPager_ListDeploymentRevisionsPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListDeploymentsAsyncPager
    
    
    ListDeploymentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListDeploymentsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListDeploymentsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListDeploymentsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListDeploymentsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListDeploymentsAsyncPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_ListDeploymentsAsyncPager_ListDeploymentsAsyncPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListDeploymentsPager
    
    
    ListDeploymentsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListDeploymentsResponse,
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListDeploymentsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListDeploymentsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListDeploymentsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListDeploymentsPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_ListDeploymentsPager_ListDeploymentsPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListEdgeSlmsAsyncPager
    
    
    ListEdgeSlmsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListEdgeSlmsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListEdgeSlmsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListEdgeSlmsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListEdgeSlmsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListEdgeSlmsAsyncPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_ListEdgeSlmsAsyncPager_ListEdgeSlmsAsyncPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListEdgeSlmsPager
    
    
    ListEdgeSlmsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListEdgeSlmsResponse,
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListEdgeSlmsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListEdgeSlmsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListEdgeSlmsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListEdgeSlmsPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_ListEdgeSlmsPager_ListEdgeSlmsPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListHydratedDeploymentsAsyncPager
    
    
    ListHydratedDeploymentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListHydratedDeploymentsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListHydratedDeploymentsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListHydratedDeploymentsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListHydratedDeploymentsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListHydratedDeploymentsAsyncPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_ListHydratedDeploymentsAsyncPager_ListHydratedDeploymentsAsyncPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListHydratedDeploymentsPager
    
    
    ListHydratedDeploymentsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListHydratedDeploymentsResponse,
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListHydratedDeploymentsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListHydratedDeploymentsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListHydratedDeploymentsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListHydratedDeploymentsPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_ListHydratedDeploymentsPager_ListHydratedDeploymentsPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListOrchestrationClustersAsyncPager
    
    
    ListOrchestrationClustersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListOrchestrationClustersResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListOrchestrationClustersRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListOrchestrationClustersResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListOrchestrationClustersAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListOrchestrationClustersAsyncPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_ListOrchestrationClustersAsyncPager_ListOrchestrationClustersAsyncPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListOrchestrationClustersPager
    
    
    ListOrchestrationClustersPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListOrchestrationClustersResponse,
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListOrchestrationClustersRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListOrchestrationClustersResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListOrchestrationClustersPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListOrchestrationClustersPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_ListOrchestrationClustersPager_ListOrchestrationClustersPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListPublicBlueprintsAsyncPager
    
    
    ListPublicBlueprintsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListPublicBlueprintsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListPublicBlueprintsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListPublicBlueprintsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListPublicBlueprintsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListPublicBlueprintsAsyncPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_ListPublicBlueprintsAsyncPager_ListPublicBlueprintsAsyncPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListPublicBlueprintsPager
    
    
    ListPublicBlueprintsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListPublicBlueprintsResponse,
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListPublicBlueprintsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.ListPublicBlueprintsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListPublicBlueprintsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.ListPublicBlueprintsPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_ListPublicBlueprintsPager_ListPublicBlueprintsPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.SearchBlueprintRevisionsAsyncPager
    
    
    SearchBlueprintRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.SearchBlueprintRevisionsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.SearchBlueprintRevisionsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.SearchBlueprintRevisionsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.SearchBlueprintRevisionsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.SearchBlueprintRevisionsAsyncPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_SearchBlueprintRevisionsAsyncPager_SearchBlueprintRevisionsAsyncPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.SearchBlueprintRevisionsPager
    
    
    SearchBlueprintRevisionsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.SearchBlueprintRevisionsResponse,
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.SearchBlueprintRevisionsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.SearchBlueprintRevisionsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.SearchBlueprintRevisionsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.SearchBlueprintRevisionsPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_SearchBlueprintRevisionsPager_SearchBlueprintRevisionsPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.SearchDeploymentRevisionsAsyncPager
    
    
    SearchDeploymentRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.telcoautomation_v1alpha1.types.telcoautomation.SearchDeploymentRevisionsResponse
            ],
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.SearchDeploymentRevisionsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.SearchDeploymentRevisionsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.SearchDeploymentRevisionsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.SearchDeploymentRevisionsAsyncPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_SearchDeploymentRevisionsAsyncPager_SearchDeploymentRevisionsAsyncPager)

### google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.SearchDeploymentRevisionsPager
    
    
    SearchDeploymentRevisionsPager(
        method: typing.Callable[
            [...],
            google.cloud.telcoautomation_v1alpha1.types.telcoautomation.SearchDeploymentRevisionsResponse,
        ],
        request: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.SearchDeploymentRevisionsRequest,
        response: google.cloud.telcoautomation_v1alpha1.types.telcoautomation.SearchDeploymentRevisionsResponse,
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

See more: [google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.SearchDeploymentRevisionsPager](https://cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.services.telco_automation.pagers.SearchDeploymentRevisionsPager#google_cloud_telcoautomation_v1alpha1_services_telco_automation_pagers_SearchDeploymentRevisionsPager_SearchDeploymentRevisionsPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
