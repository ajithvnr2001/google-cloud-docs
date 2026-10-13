---
url: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/summary_method/
title: Package Methods (2.12.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:42:36.194077+00:00
---

# Package Methods (2.12.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.0  2.9.0  2.8.0  2.7.1  2.6.3  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.0  1.19.1  1.18.1  1.17.3  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.1  1.1.1  1.0.0  0.3.2  0.2.0  0.1.1 

Summary of entries of Methods for clouddeploy.

## 

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient
    
    
    CloudDeployAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.deploy_v1.services.cloud_deploy.transports.base.CloudDeployTransport,
                typing.Callable[
                    [...],
                    google.cloud.deploy_v1.services.cloud_deploy.transports.base.CloudDeployTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the cloud deploy async client.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_CloudDeployAsyncClient)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.abandon_release
    
    
    abandon_release(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.AbandonReleaseRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.AbandonReleaseResponse

Abandons a Release in the Delivery Pipeline.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.abandon_release](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_abandon_release)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.advance_rollout
    
    
    advance_rollout(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.AdvanceRolloutRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        phase_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.deploy_v1.types.cloud_deploy.AdvanceRolloutResponse

Advances a Rollout in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.advance_rollout](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_advance_rollout)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.approve_rollout
    
    
    approve_rollout(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ApproveRolloutRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.ApproveRolloutResponse

Approves a Rollout.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.approve_rollout](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_approve_rollout)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.automation_path
    
    
    automation_path(
        project: str, location: str, delivery_pipeline: str, automation: str
    ) -> str

Returns a fully-qualified automation string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.automation_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_automation_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.automation_run_path
    
    
    automation_run_path(
        project: str, location: str, delivery_pipeline: str, automation_run: str
    ) -> str

Returns a fully-qualified automation_run string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.automation_run_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_automation_run_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.build_path
    
    
    build_path(project: str, location: str, build: str) -> str

Returns a fully-qualified build string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.build_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_build_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.cancel_automation_run
    
    
    cancel_automation_run(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CancelAutomationRunRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.CancelAutomationRunResponse

Cancels an AutomationRun.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.cancel_automation_run](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_cancel_automation_run)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_cancel_operation)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.cancel_rollout
    
    
    cancel_rollout(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CancelRolloutRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.CancelRolloutResponse

Cancels a Rollout in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.cancel_rollout](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_cancel_rollout)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.cluster_path
    
    
    cluster_path(project: str, location: str, cluster: str) -> str

Returns a fully-qualified cluster string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.cluster_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_cluster_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_common_billing_account_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_common_folder_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_common_location_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_common_organization_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_common_project_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.config_path
    
    
    config_path(project: str, location: str) -> str

Returns a fully-qualified config string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.config_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_config_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.create_automation
    
    
    create_automation(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateAutomationRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        automation: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.Automation
        ] = None,
        automation_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Automation in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.create_automation](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_create_automation)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.create_custom_target_type
    
    
    create_custom_target_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateCustomTargetTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        custom_target_type: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.CustomTargetType
        ] = None,
        custom_target_type_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new CustomTargetType in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.create_custom_target_type](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_create_custom_target_type)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.create_delivery_pipeline
    
    
    create_delivery_pipeline(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateDeliveryPipelineRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        delivery_pipeline: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.DeliveryPipeline
        ] = None,
        delivery_pipeline_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new DeliveryPipeline in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.create_delivery_pipeline](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_create_delivery_pipeline)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.create_deploy_policy
    
    
    create_deploy_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateDeployPolicyRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deploy_policy: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.DeployPolicy
        ] = None,
        deploy_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new DeployPolicy in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.create_deploy_policy](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_create_deploy_policy)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.create_release
    
    
    create_release(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateReleaseRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        release: typing.Optional[google.cloud.deploy_v1.types.cloud_deploy.Release] = None,
        release_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Release in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.create_release](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_create_release)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.create_rollout
    
    
    create_rollout(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateRolloutRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        rollout: typing.Optional[google.cloud.deploy_v1.types.cloud_deploy.Rollout] = None,
        rollout_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Rollout in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.create_rollout](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_create_rollout)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.create_target
    
    
    create_target(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateTargetRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        target: typing.Optional[google.cloud.deploy_v1.types.cloud_deploy.Target] = None,
        target_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Target in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.create_target](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_create_target)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.custom_target_type_path
    
    
    custom_target_type_path(
        project: str, location: str, custom_target_type: str
    ) -> str

Returns a fully-qualified custom_target_type string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.custom_target_type_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_custom_target_type_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.delete_automation
    
    
    delete_automation(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.DeleteAutomationRequest, dict
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

Deletes a single Automation resource.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.delete_automation](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_delete_automation)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.delete_custom_target_type
    
    
    delete_custom_target_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.DeleteCustomTargetTypeRequest,
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

Deletes a single CustomTargetType.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.delete_custom_target_type](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_delete_custom_target_type)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.delete_delivery_pipeline
    
    
    delete_delivery_pipeline(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.DeleteDeliveryPipelineRequest,
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

Deletes a single DeliveryPipeline.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.delete_delivery_pipeline](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_delete_delivery_pipeline)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.delete_deploy_policy
    
    
    delete_deploy_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.DeleteDeployPolicyRequest, dict
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

Deletes a single DeployPolicy.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.delete_deploy_policy](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_delete_deploy_policy)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.delete_operation
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_delete_operation)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.delete_target
    
    
    delete_target(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.DeleteTargetRequest, dict
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

Deletes a single Target.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.delete_target](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_delete_target)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.delivery_pipeline_path
    
    
    delivery_pipeline_path(project: str, location: str, delivery_pipeline: str) -> str

Returns a fully-qualified delivery_pipeline string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.delivery_pipeline_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_delivery_pipeline_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.deploy_policy_path
    
    
    deploy_policy_path(project: str, location: str, deploy_policy: str) -> str

Returns a fully-qualified deploy_policy string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.deploy_policy_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_deploy_policy_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_from_service_account_file)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_from_service_account_info)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_from_service_account_json)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_automation
    
    
    get_automation(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.GetAutomationRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.Automation

Gets details of a single Automation.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_automation](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_automation)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_automation_run
    
    
    get_automation_run(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.GetAutomationRunRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.AutomationRun

Gets details of a single AutomationRun.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_automation_run](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_automation_run)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_config
    
    
    get_config(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.GetConfigRequest, dict]
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.Config

Gets the configuration for a location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_config](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_config)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_custom_target_type
    
    
    get_custom_target_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.GetCustomTargetTypeRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.CustomTargetType

Gets details of a single CustomTargetType.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_custom_target_type](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_custom_target_type)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_delivery_pipeline
    
    
    get_delivery_pipeline(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.GetDeliveryPipelineRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.DeliveryPipeline

Gets details of a single DeliveryPipeline.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_delivery_pipeline](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_delivery_pipeline)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_deploy_policy
    
    
    get_deploy_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.GetDeployPolicyRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.DeployPolicy

Gets details of a single DeployPolicy.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_deploy_policy](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_deploy_policy)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_iam_policy
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_iam_policy)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_job_run
    
    
    get_job_run(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.GetJobRunRequest, dict]
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.JobRun

Gets details of a single JobRun.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_job_run](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_job_run)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_location
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_location](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_location)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_operation
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_operation)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_release
    
    
    get_release(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.GetReleaseRequest, dict]
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.Release

Gets details of a single Release.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_release](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_release)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_rollout
    
    
    get_rollout(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.GetRolloutRequest, dict]
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.Rollout

Gets details of a single Rollout.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_rollout](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_rollout)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_target
    
    
    get_target(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.GetTargetRequest, dict]
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.Target

Gets details of a single Target.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_target](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_target)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.deploy_v1.services.cloud_deploy.transports.base.CloudDeployTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_get_transport_class)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.ignore_job
    
    
    ignore_job(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.IgnoreJobRequest, dict]
        ] = None,
        *,
        rollout: typing.Optional[str] = None,
        phase_id: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.deploy_v1.types.cloud_deploy.IgnoreJobResponse

Ignores the specified Job in a Rollout.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.ignore_job](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_ignore_job)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.job_path
    
    
    job_path(project: str, location: str, job: str) -> str

Returns a fully-qualified job string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.job_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_job_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.job_run_path
    
    
    job_run_path(
        project: str,
        location: str,
        delivery_pipeline: str,
        release: str,
        rollout: str,
        job_run: str,
    ) -> str

Returns a fully-qualified job_run string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.job_run_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_job_run_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_automation_runs
    
    
    list_automation_runs(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListAutomationRunsRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationRunsAsyncPager

Lists AutomationRuns in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_automation_runs](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_automation_runs)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_automations
    
    
    list_automations(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListAutomationsRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationsAsyncPager

Lists Automations in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_automations](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_automations)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_custom_target_types
    
    
    list_custom_target_types(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListCustomTargetTypesRequest, dict
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
        google.cloud.deploy_v1.services.cloud_deploy.pagers.ListCustomTargetTypesAsyncPager
    )

Lists CustomTargetTypes in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_custom_target_types](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_custom_target_types)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_delivery_pipelines
    
    
    list_delivery_pipelines(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListDeliveryPipelinesRequest, dict
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
        google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeliveryPipelinesAsyncPager
    )

Lists DeliveryPipelines in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_delivery_pipelines](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_delivery_pipelines)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_deploy_policies
    
    
    list_deploy_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListDeployPoliciesRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeployPoliciesAsyncPager

Lists DeployPolicies in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_deploy_policies](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_deploy_policies)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_job_runs
    
    
    list_job_runs(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.ListJobRunsRequest, dict]
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListJobRunsAsyncPager

Lists JobRuns in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_job_runs](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_job_runs)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_locations
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_locations)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_operations
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_operations)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_releases
    
    
    list_releases(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListReleasesRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListReleasesAsyncPager

Lists Releases in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_releases](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_releases)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_rollouts
    
    
    list_rollouts(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListRolloutsRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListRolloutsAsyncPager

Lists Rollouts in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_rollouts](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_rollouts)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_targets
    
    
    list_targets(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.ListTargetsRequest, dict]
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListTargetsAsyncPager

Lists Targets in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.list_targets](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_list_targets)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.membership_path
    
    
    membership_path(project: str, location: str, membership: str) -> str

Returns a fully-qualified membership string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.membership_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_membership_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_automation_path
    
    
    parse_automation_path(path: str) -> typing.Dict[str, str]

Parses a automation path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_automation_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_automation_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_automation_run_path
    
    
    parse_automation_run_path(path: str) -> typing.Dict[str, str]

Parses a automation_run path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_automation_run_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_automation_run_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_build_path
    
    
    parse_build_path(path: str) -> typing.Dict[str, str]

Parses a build path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_build_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_build_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_cluster_path
    
    
    parse_cluster_path(path: str) -> typing.Dict[str, str]

Parses a cluster path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_cluster_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_cluster_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_common_billing_account_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_common_folder_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_common_location_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_common_organization_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_common_project_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_config_path
    
    
    parse_config_path(path: str) -> typing.Dict[str, str]

Parses a config path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_config_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_config_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_custom_target_type_path
    
    
    parse_custom_target_type_path(path: str) -> typing.Dict[str, str]

Parses a custom_target_type path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_custom_target_type_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_custom_target_type_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_delivery_pipeline_path
    
    
    parse_delivery_pipeline_path(path: str) -> typing.Dict[str, str]

Parses a delivery_pipeline path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_delivery_pipeline_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_delivery_pipeline_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_deploy_policy_path
    
    
    parse_deploy_policy_path(path: str) -> typing.Dict[str, str]

Parses a deploy_policy path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_deploy_policy_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_deploy_policy_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_job_path
    
    
    parse_job_path(path: str) -> typing.Dict[str, str]

Parses a job path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_job_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_job_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_job_run_path
    
    
    parse_job_run_path(path: str) -> typing.Dict[str, str]

Parses a job_run path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_job_run_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_job_run_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_membership_path
    
    
    parse_membership_path(path: str) -> typing.Dict[str, str]

Parses a membership path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_membership_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_membership_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_release_path
    
    
    parse_release_path(path: str) -> typing.Dict[str, str]

Parses a release path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_release_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_release_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_repository_path
    
    
    parse_repository_path(path: str) -> typing.Dict[str, str]

Parses a repository path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_repository_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_repository_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_rollout_path
    
    
    parse_rollout_path(path: str) -> typing.Dict[str, str]

Parses a rollout path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_rollout_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_rollout_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_service_path
    
    
    parse_service_path(path: str) -> typing.Dict[str, str]

Parses a service path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_service_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_service_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_target_path
    
    
    parse_target_path(path: str) -> typing.Dict[str, str]

Parses a target path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_target_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_target_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_worker_pool_path
    
    
    parse_worker_pool_path(path: str) -> typing.Dict[str, str]

Parses a worker_pool path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.parse_worker_pool_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_parse_worker_pool_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.release_path
    
    
    release_path(
        project: str, location: str, delivery_pipeline: str, release: str
    ) -> str

Returns a fully-qualified release string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.release_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_release_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.repository_path
    
    
    repository_path(
        project: str, location: str, connection: str, repository: str
    ) -> str

Returns a fully-qualified repository string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.repository_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_repository_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.retry_job
    
    
    retry_job(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.RetryJobRequest, dict]
        ] = None,
        *,
        rollout: typing.Optional[str] = None,
        phase_id: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.deploy_v1.types.cloud_deploy.RetryJobResponse

Retries the specified Job in a Rollout.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.retry_job](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_retry_job)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.rollback_target
    
    
    rollback_target(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.RollbackTargetRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        target_id: typing.Optional[str] = None,
        rollout_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.deploy_v1.types.cloud_deploy.RollbackTargetResponse

Creates a `Rollout` to roll back the specified target.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.rollback_target](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_rollback_target)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.rollout_path
    
    
    rollout_path(
        project: str, location: str, delivery_pipeline: str, release: str, rollout: str
    ) -> str

Returns a fully-qualified rollout string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.rollout_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_rollout_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.service_path
    
    
    service_path(project: str, location: str, service: str) -> str

Returns a fully-qualified service string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.service_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_service_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.set_iam_policy
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_set_iam_policy)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.target_path
    
    
    target_path(project: str, location: str, target: str) -> str

Returns a fully-qualified target string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.target_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_target_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.terminate_job_run
    
    
    terminate_job_run(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.TerminateJobRunRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.TerminateJobRunResponse

Terminates a Job Run in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.terminate_job_run](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_terminate_job_run)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.test_iam_permissions
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_test_iam_permissions)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.update_automation
    
    
    update_automation(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.UpdateAutomationRequest, dict
            ]
        ] = None,
        *,
        automation: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.Automation
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

Updates the parameters of a single Automation resource.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.update_automation](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_update_automation)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.update_custom_target_type
    
    
    update_custom_target_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.UpdateCustomTargetTypeRequest,
                dict,
            ]
        ] = None,
        *,
        custom_target_type: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.CustomTargetType
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

Updates a single CustomTargetType.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.update_custom_target_type](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_update_custom_target_type)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.update_delivery_pipeline
    
    
    update_delivery_pipeline(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.UpdateDeliveryPipelineRequest,
                dict,
            ]
        ] = None,
        *,
        delivery_pipeline: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.DeliveryPipeline
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

Updates the parameters of a single DeliveryPipeline.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.update_delivery_pipeline](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_update_delivery_pipeline)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.update_deploy_policy
    
    
    update_deploy_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.UpdateDeployPolicyRequest, dict
            ]
        ] = None,
        *,
        deploy_policy: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.DeployPolicy
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

Updates the parameters of a single DeployPolicy.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.update_deploy_policy](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_update_deploy_policy)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.update_target
    
    
    update_target(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.UpdateTargetRequest, dict
            ]
        ] = None,
        *,
        target: typing.Optional[google.cloud.deploy_v1.types.cloud_deploy.Target] = None,
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

Updates the parameters of a single Target.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.update_target](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_update_target)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.worker_pool_path
    
    
    worker_pool_path(project: str, location: str, worker_pool: str) -> str

Returns a fully-qualified worker_pool string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient.worker_pool_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployAsyncClient_worker_pool_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient
    
    
    CloudDeployClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.deploy_v1.services.cloud_deploy.transports.base.CloudDeployTransport,
                typing.Callable[
                    [...],
                    google.cloud.deploy_v1.services.cloud_deploy.transports.base.CloudDeployTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the cloud deploy client.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_CloudDeployClient)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.**exit**](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient___exit__)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.abandon_release
    
    
    abandon_release(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.AbandonReleaseRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.AbandonReleaseResponse

Abandons a Release in the Delivery Pipeline.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.abandon_release](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_abandon_release)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.advance_rollout
    
    
    advance_rollout(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.AdvanceRolloutRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        phase_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.deploy_v1.types.cloud_deploy.AdvanceRolloutResponse

Advances a Rollout in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.advance_rollout](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_advance_rollout)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.approve_rollout
    
    
    approve_rollout(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ApproveRolloutRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.ApproveRolloutResponse

Approves a Rollout.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.approve_rollout](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_approve_rollout)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.automation_path
    
    
    automation_path(
        project: str, location: str, delivery_pipeline: str, automation: str
    ) -> str

Returns a fully-qualified automation string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.automation_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_automation_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.automation_run_path
    
    
    automation_run_path(
        project: str, location: str, delivery_pipeline: str, automation_run: str
    ) -> str

Returns a fully-qualified automation_run string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.automation_run_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_automation_run_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.build_path
    
    
    build_path(project: str, location: str, build: str) -> str

Returns a fully-qualified build string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.build_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_build_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.cancel_automation_run
    
    
    cancel_automation_run(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CancelAutomationRunRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.CancelAutomationRunResponse

Cancels an AutomationRun.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.cancel_automation_run](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_cancel_automation_run)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.cancel_operation
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.cancel_operation](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_cancel_operation)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.cancel_rollout
    
    
    cancel_rollout(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CancelRolloutRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.CancelRolloutResponse

Cancels a Rollout in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.cancel_rollout](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_cancel_rollout)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.cluster_path
    
    
    cluster_path(project: str, location: str, cluster: str) -> str

Returns a fully-qualified cluster string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.cluster_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_cluster_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_common_billing_account_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.common_folder_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_common_folder_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.common_location_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_common_location_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.common_organization_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_common_organization_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.common_project_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_common_project_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.config_path
    
    
    config_path(project: str, location: str) -> str

Returns a fully-qualified config string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.config_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_config_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.create_automation
    
    
    create_automation(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateAutomationRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        automation: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.Automation
        ] = None,
        automation_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Automation in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.create_automation](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_create_automation)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.create_custom_target_type
    
    
    create_custom_target_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateCustomTargetTypeRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        custom_target_type: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.CustomTargetType
        ] = None,
        custom_target_type_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new CustomTargetType in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.create_custom_target_type](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_create_custom_target_type)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.create_delivery_pipeline
    
    
    create_delivery_pipeline(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateDeliveryPipelineRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        delivery_pipeline: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.DeliveryPipeline
        ] = None,
        delivery_pipeline_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new DeliveryPipeline in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.create_delivery_pipeline](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_create_delivery_pipeline)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.create_deploy_policy
    
    
    create_deploy_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateDeployPolicyRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        deploy_policy: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.DeployPolicy
        ] = None,
        deploy_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new DeployPolicy in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.create_deploy_policy](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_create_deploy_policy)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.create_release
    
    
    create_release(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateReleaseRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        release: typing.Optional[google.cloud.deploy_v1.types.cloud_deploy.Release] = None,
        release_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Release in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.create_release](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_create_release)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.create_rollout
    
    
    create_rollout(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateRolloutRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        rollout: typing.Optional[google.cloud.deploy_v1.types.cloud_deploy.Rollout] = None,
        rollout_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Rollout in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.create_rollout](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_create_rollout)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.create_target
    
    
    create_target(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.CreateTargetRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        target: typing.Optional[google.cloud.deploy_v1.types.cloud_deploy.Target] = None,
        target_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Target in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.create_target](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_create_target)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.custom_target_type_path
    
    
    custom_target_type_path(
        project: str, location: str, custom_target_type: str
    ) -> str

Returns a fully-qualified custom_target_type string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.custom_target_type_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_custom_target_type_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.delete_automation
    
    
    delete_automation(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.DeleteAutomationRequest, dict
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

Deletes a single Automation resource.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.delete_automation](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_delete_automation)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.delete_custom_target_type
    
    
    delete_custom_target_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.DeleteCustomTargetTypeRequest,
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

Deletes a single CustomTargetType.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.delete_custom_target_type](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_delete_custom_target_type)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.delete_delivery_pipeline
    
    
    delete_delivery_pipeline(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.DeleteDeliveryPipelineRequest,
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

Deletes a single DeliveryPipeline.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.delete_delivery_pipeline](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_delete_delivery_pipeline)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.delete_deploy_policy
    
    
    delete_deploy_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.DeleteDeployPolicyRequest, dict
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

Deletes a single DeployPolicy.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.delete_deploy_policy](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_delete_deploy_policy)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.delete_operation
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.delete_operation](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_delete_operation)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.delete_target
    
    
    delete_target(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.DeleteTargetRequest, dict
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

Deletes a single Target.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.delete_target](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_delete_target)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.delivery_pipeline_path
    
    
    delivery_pipeline_path(project: str, location: str, delivery_pipeline: str) -> str

Returns a fully-qualified delivery_pipeline string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.delivery_pipeline_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_delivery_pipeline_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.deploy_policy_path
    
    
    deploy_policy_path(project: str, location: str, deploy_policy: str) -> str

Returns a fully-qualified deploy_policy string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.deploy_policy_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_deploy_policy_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.from_service_account_file](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_from_service_account_file)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.from_service_account_info](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_from_service_account_info)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.from_service_account_json](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_from_service_account_json)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_automation
    
    
    get_automation(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.GetAutomationRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.Automation

Gets details of a single Automation.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_automation](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_get_automation)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_automation_run
    
    
    get_automation_run(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.GetAutomationRunRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.AutomationRun

Gets details of a single AutomationRun.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_automation_run](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_get_automation_run)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_config
    
    
    get_config(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.GetConfigRequest, dict]
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.Config

Gets the configuration for a location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_config](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_get_config)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_custom_target_type
    
    
    get_custom_target_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.GetCustomTargetTypeRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.CustomTargetType

Gets details of a single CustomTargetType.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_custom_target_type](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_get_custom_target_type)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_delivery_pipeline
    
    
    get_delivery_pipeline(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.GetDeliveryPipelineRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.DeliveryPipeline

Gets details of a single DeliveryPipeline.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_delivery_pipeline](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_get_delivery_pipeline)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_deploy_policy
    
    
    get_deploy_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.GetDeployPolicyRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.DeployPolicy

Gets details of a single DeployPolicy.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_deploy_policy](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_get_deploy_policy)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_iam_policy
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_iam_policy](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_get_iam_policy)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_job_run
    
    
    get_job_run(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.GetJobRunRequest, dict]
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.JobRun

Gets details of a single JobRun.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_job_run](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_get_job_run)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_location
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_location](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_get_location)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_get_mtls_endpoint_and_cert_source)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_operation
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_operation](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_get_operation)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_release
    
    
    get_release(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.GetReleaseRequest, dict]
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.Release

Gets details of a single Release.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_release](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_get_release)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_rollout
    
    
    get_rollout(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.GetRolloutRequest, dict]
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.Rollout

Gets details of a single Rollout.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_rollout](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_get_rollout)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_target
    
    
    get_target(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.GetTargetRequest, dict]
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.Target

Gets details of a single Target.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.get_target](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_get_target)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.ignore_job
    
    
    ignore_job(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.IgnoreJobRequest, dict]
        ] = None,
        *,
        rollout: typing.Optional[str] = None,
        phase_id: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.deploy_v1.types.cloud_deploy.IgnoreJobResponse

Ignores the specified Job in a Rollout.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.ignore_job](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_ignore_job)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.job_path
    
    
    job_path(project: str, location: str, job: str) -> str

Returns a fully-qualified job string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.job_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_job_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.job_run_path
    
    
    job_run_path(
        project: str,
        location: str,
        delivery_pipeline: str,
        release: str,
        rollout: str,
        job_run: str,
    ) -> str

Returns a fully-qualified job_run string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.job_run_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_job_run_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_automation_runs
    
    
    list_automation_runs(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListAutomationRunsRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationRunsPager

Lists AutomationRuns in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_automation_runs](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_list_automation_runs)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_automations
    
    
    list_automations(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListAutomationsRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationsPager

Lists Automations in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_automations](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_list_automations)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_custom_target_types
    
    
    list_custom_target_types(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListCustomTargetTypesRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListCustomTargetTypesPager

Lists CustomTargetTypes in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_custom_target_types](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_list_custom_target_types)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_delivery_pipelines
    
    
    list_delivery_pipelines(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListDeliveryPipelinesRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeliveryPipelinesPager

Lists DeliveryPipelines in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_delivery_pipelines](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_list_delivery_pipelines)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_deploy_policies
    
    
    list_deploy_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListDeployPoliciesRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeployPoliciesPager

Lists DeployPolicies in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_deploy_policies](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_list_deploy_policies)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_job_runs
    
    
    list_job_runs(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.ListJobRunsRequest, dict]
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListJobRunsPager

Lists JobRuns in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_job_runs](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_list_job_runs)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_locations
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_locations](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_list_locations)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_operations
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_operations](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_list_operations)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_releases
    
    
    list_releases(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListReleasesRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListReleasesPager

Lists Releases in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_releases](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_list_releases)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_rollouts
    
    
    list_rollouts(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.ListRolloutsRequest, dict
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListRolloutsPager

Lists Rollouts in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_rollouts](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_list_rollouts)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_targets
    
    
    list_targets(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.ListTargetsRequest, dict]
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
    ) -> google.cloud.deploy_v1.services.cloud_deploy.pagers.ListTargetsPager

Lists Targets in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.list_targets](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_list_targets)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.membership_path
    
    
    membership_path(project: str, location: str, membership: str) -> str

Returns a fully-qualified membership string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.membership_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_membership_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_automation_path
    
    
    parse_automation_path(path: str) -> typing.Dict[str, str]

Parses a automation path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_automation_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_automation_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_automation_run_path
    
    
    parse_automation_run_path(path: str) -> typing.Dict[str, str]

Parses a automation_run path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_automation_run_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_automation_run_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_build_path
    
    
    parse_build_path(path: str) -> typing.Dict[str, str]

Parses a build path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_build_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_build_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_cluster_path
    
    
    parse_cluster_path(path: str) -> typing.Dict[str, str]

Parses a cluster path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_cluster_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_cluster_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_common_billing_account_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_common_folder_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_common_location_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_common_organization_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_common_project_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_config_path
    
    
    parse_config_path(path: str) -> typing.Dict[str, str]

Parses a config path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_config_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_config_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_custom_target_type_path
    
    
    parse_custom_target_type_path(path: str) -> typing.Dict[str, str]

Parses a custom_target_type path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_custom_target_type_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_custom_target_type_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_delivery_pipeline_path
    
    
    parse_delivery_pipeline_path(path: str) -> typing.Dict[str, str]

Parses a delivery_pipeline path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_delivery_pipeline_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_delivery_pipeline_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_deploy_policy_path
    
    
    parse_deploy_policy_path(path: str) -> typing.Dict[str, str]

Parses a deploy_policy path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_deploy_policy_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_deploy_policy_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_job_path
    
    
    parse_job_path(path: str) -> typing.Dict[str, str]

Parses a job path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_job_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_job_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_job_run_path
    
    
    parse_job_run_path(path: str) -> typing.Dict[str, str]

Parses a job_run path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_job_run_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_job_run_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_membership_path
    
    
    parse_membership_path(path: str) -> typing.Dict[str, str]

Parses a membership path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_membership_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_membership_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_release_path
    
    
    parse_release_path(path: str) -> typing.Dict[str, str]

Parses a release path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_release_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_release_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_repository_path
    
    
    parse_repository_path(path: str) -> typing.Dict[str, str]

Parses a repository path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_repository_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_repository_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_rollout_path
    
    
    parse_rollout_path(path: str) -> typing.Dict[str, str]

Parses a rollout path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_rollout_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_rollout_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_service_path
    
    
    parse_service_path(path: str) -> typing.Dict[str, str]

Parses a service path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_service_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_service_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_target_path
    
    
    parse_target_path(path: str) -> typing.Dict[str, str]

Parses a target path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_target_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_target_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_worker_pool_path
    
    
    parse_worker_pool_path(path: str) -> typing.Dict[str, str]

Parses a worker_pool path into its component segments.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.parse_worker_pool_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_parse_worker_pool_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.release_path
    
    
    release_path(
        project: str, location: str, delivery_pipeline: str, release: str
    ) -> str

Returns a fully-qualified release string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.release_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_release_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.repository_path
    
    
    repository_path(
        project: str, location: str, connection: str, repository: str
    ) -> str

Returns a fully-qualified repository string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.repository_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_repository_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.retry_job
    
    
    retry_job(
        request: typing.Optional[
            typing.Union[google.cloud.deploy_v1.types.cloud_deploy.RetryJobRequest, dict]
        ] = None,
        *,
        rollout: typing.Optional[str] = None,
        phase_id: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.deploy_v1.types.cloud_deploy.RetryJobResponse

Retries the specified Job in a Rollout.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.retry_job](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_retry_job)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.rollback_target
    
    
    rollback_target(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.RollbackTargetRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        target_id: typing.Optional[str] = None,
        rollout_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.deploy_v1.types.cloud_deploy.RollbackTargetResponse

Creates a `Rollout` to roll back the specified target.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.rollback_target](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_rollback_target)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.rollout_path
    
    
    rollout_path(
        project: str, location: str, delivery_pipeline: str, release: str, rollout: str
    ) -> str

Returns a fully-qualified rollout string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.rollout_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_rollout_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.service_path
    
    
    service_path(project: str, location: str, service: str) -> str

Returns a fully-qualified service string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.service_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_service_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.set_iam_policy
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.set_iam_policy](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_set_iam_policy)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.target_path
    
    
    target_path(project: str, location: str, target: str) -> str

Returns a fully-qualified target string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.target_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_target_path)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.terminate_job_run
    
    
    terminate_job_run(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.TerminateJobRunRequest, dict
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
    ) -> google.cloud.deploy_v1.types.cloud_deploy.TerminateJobRunResponse

Terminates a Job Run in a given project and location.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.terminate_job_run](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_terminate_job_run)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.test_iam_permissions
    
    
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_test_iam_permissions)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.update_automation
    
    
    update_automation(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.UpdateAutomationRequest, dict
            ]
        ] = None,
        *,
        automation: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.Automation
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

Updates the parameters of a single Automation resource.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.update_automation](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_update_automation)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.update_custom_target_type
    
    
    update_custom_target_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.UpdateCustomTargetTypeRequest,
                dict,
            ]
        ] = None,
        *,
        custom_target_type: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.CustomTargetType
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

Updates a single CustomTargetType.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.update_custom_target_type](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_update_custom_target_type)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.update_delivery_pipeline
    
    
    update_delivery_pipeline(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.UpdateDeliveryPipelineRequest,
                dict,
            ]
        ] = None,
        *,
        delivery_pipeline: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.DeliveryPipeline
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

Updates the parameters of a single DeliveryPipeline.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.update_delivery_pipeline](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_update_delivery_pipeline)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.update_deploy_policy
    
    
    update_deploy_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.UpdateDeployPolicyRequest, dict
            ]
        ] = None,
        *,
        deploy_policy: typing.Optional[
            google.cloud.deploy_v1.types.cloud_deploy.DeployPolicy
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

Updates the parameters of a single DeployPolicy.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.update_deploy_policy](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_update_deploy_policy)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.update_target
    
    
    update_target(
        request: typing.Optional[
            typing.Union[
                google.cloud.deploy_v1.types.cloud_deploy.UpdateTargetRequest, dict
            ]
        ] = None,
        *,
        target: typing.Optional[google.cloud.deploy_v1.types.cloud_deploy.Target] = None,
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

Updates the parameters of a single Target.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.update_target](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_update_target)

### google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.worker_pool_path
    
    
    worker_pool_path(project: str, location: str, worker_pool: str) -> str

Returns a fully-qualified worker_pool string.

See more: [google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient.worker_pool_path](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient#google_cloud_deploy_v1_services_cloud_deploy_CloudDeployClient_worker_pool_path)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationRunsAsyncPager
    
    
    ListAutomationRunsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.deploy_v1.types.cloud_deploy.ListAutomationRunsResponse
            ],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListAutomationRunsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListAutomationRunsResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationRunsAsyncPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationRunsAsyncPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListAutomationRunsAsyncPager_ListAutomationRunsAsyncPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationRunsPager
    
    
    ListAutomationRunsPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListAutomationRunsResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListAutomationRunsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListAutomationRunsResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationRunsPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationRunsPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListAutomationRunsPager_ListAutomationRunsPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationsAsyncPager
    
    
    ListAutomationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.deploy_v1.types.cloud_deploy.ListAutomationsResponse
            ],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListAutomationsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListAutomationsResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationsAsyncPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationsAsyncPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListAutomationsAsyncPager_ListAutomationsAsyncPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationsPager
    
    
    ListAutomationsPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListAutomationsResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListAutomationsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListAutomationsResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationsPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationsPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListAutomationsPager_ListAutomationsPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListCustomTargetTypesAsyncPager
    
    
    ListCustomTargetTypesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.deploy_v1.types.cloud_deploy.ListCustomTargetTypesResponse
            ],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListCustomTargetTypesRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListCustomTargetTypesResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListCustomTargetTypesAsyncPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListCustomTargetTypesAsyncPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListCustomTargetTypesAsyncPager_ListCustomTargetTypesAsyncPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListCustomTargetTypesPager
    
    
    ListCustomTargetTypesPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListCustomTargetTypesResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListCustomTargetTypesRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListCustomTargetTypesResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListCustomTargetTypesPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListCustomTargetTypesPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListCustomTargetTypesPager_ListCustomTargetTypesPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeliveryPipelinesAsyncPager
    
    
    ListDeliveryPipelinesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.deploy_v1.types.cloud_deploy.ListDeliveryPipelinesResponse
            ],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListDeliveryPipelinesRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListDeliveryPipelinesResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeliveryPipelinesAsyncPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeliveryPipelinesAsyncPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListDeliveryPipelinesAsyncPager_ListDeliveryPipelinesAsyncPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeliveryPipelinesPager
    
    
    ListDeliveryPipelinesPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListDeliveryPipelinesResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListDeliveryPipelinesRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListDeliveryPipelinesResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeliveryPipelinesPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeliveryPipelinesPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListDeliveryPipelinesPager_ListDeliveryPipelinesPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeployPoliciesAsyncPager
    
    
    ListDeployPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.deploy_v1.types.cloud_deploy.ListDeployPoliciesResponse
            ],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListDeployPoliciesRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListDeployPoliciesResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeployPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeployPoliciesAsyncPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListDeployPoliciesAsyncPager_ListDeployPoliciesAsyncPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeployPoliciesPager
    
    
    ListDeployPoliciesPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListDeployPoliciesResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListDeployPoliciesRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListDeployPoliciesResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeployPoliciesPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeployPoliciesPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListDeployPoliciesPager_ListDeployPoliciesPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListJobRunsAsyncPager
    
    
    ListJobRunsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.deploy_v1.types.cloud_deploy.ListJobRunsResponse],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListJobRunsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListJobRunsResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListJobRunsAsyncPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListJobRunsAsyncPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListJobRunsAsyncPager_ListJobRunsAsyncPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListJobRunsPager
    
    
    ListJobRunsPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListJobRunsResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListJobRunsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListJobRunsResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListJobRunsPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListJobRunsPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListJobRunsPager_ListJobRunsPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListReleasesAsyncPager
    
    
    ListReleasesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.deploy_v1.types.cloud_deploy.ListReleasesResponse
            ],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListReleasesRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListReleasesResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListReleasesAsyncPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListReleasesAsyncPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListReleasesAsyncPager_ListReleasesAsyncPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListReleasesPager
    
    
    ListReleasesPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListReleasesResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListReleasesRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListReleasesResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListReleasesPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListReleasesPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListReleasesPager_ListReleasesPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListRolloutsAsyncPager
    
    
    ListRolloutsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.deploy_v1.types.cloud_deploy.ListRolloutsResponse
            ],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListRolloutsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListRolloutsResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListRolloutsAsyncPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListRolloutsAsyncPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListRolloutsAsyncPager_ListRolloutsAsyncPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListRolloutsPager
    
    
    ListRolloutsPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListRolloutsResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListRolloutsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListRolloutsResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListRolloutsPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListRolloutsPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListRolloutsPager_ListRolloutsPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListTargetsAsyncPager
    
    
    ListTargetsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.deploy_v1.types.cloud_deploy.ListTargetsResponse],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListTargetsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListTargetsResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListTargetsAsyncPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListTargetsAsyncPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListTargetsAsyncPager_ListTargetsAsyncPager)

### google.cloud.deploy_v1.services.cloud_deploy.pagers.ListTargetsPager
    
    
    ListTargetsPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListTargetsResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListTargetsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListTargetsResponse,
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

See more: [google.cloud.deploy_v1.services.cloud_deploy.pagers.ListTargetsPager](https://cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListTargetsPager#google_cloud_deploy_v1_services_cloud_deploy_pagers_ListTargetsPager_ListTargetsPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
