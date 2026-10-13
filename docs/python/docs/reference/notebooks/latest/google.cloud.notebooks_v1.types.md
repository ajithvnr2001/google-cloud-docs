---
url: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types
title: Package types (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:36.708302+00:00
---

# Package types (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.3  1.12.0  1.11.1  1.10.5  1.9.0  1.8.0  1.7.1  1.6.1  1.5.1  1.4.4  1.3.2  1.2.1  1.1.1  1.0.0  0.4.3  0.3.2  0.2.0  0.1.2 

API documentation for `notebooks_v1.types` package.

## Classes 

### [ContainerImage](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ContainerImage)

Definition of a container image for starting a notebook instance with the environment installed in a container.

### [CreateEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.CreateEnvironmentRequest)

Request for creating a notebook environment.

### [CreateExecutionRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.CreateExecutionRequest)

Request to create notebook execution

### [CreateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.CreateInstanceRequest)

Request for creating a notebook instance.

### [CreateRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.CreateRuntimeRequest)

Request for creating a Managed Notebook Runtime.

### [CreateScheduleRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.CreateScheduleRequest)

Request for created scheduled notebooks

### [DeleteEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DeleteEnvironmentRequest)

Request for deleting a notebook environment.

### [DeleteExecutionRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DeleteExecutionRequest)

Request for deleting a scheduled notebook execution

### [DeleteInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DeleteInstanceRequest)

Request for deleting a notebook instance.

### [DeleteRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DeleteRuntimeRequest)

Request for deleting a Managed Notebook Runtime.

### [DeleteScheduleRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DeleteScheduleRequest)

Request for deleting an Schedule

### [DiagnoseInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DiagnoseInstanceRequest)

Request for creating a notebook instance diagnostic file.

### [DiagnoseRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DiagnoseRuntimeRequest)

Request for creating a notebook instance diagnostic file.

### [DiagnosticConfig](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DiagnosticConfig)

Defines flags that are used to run the diagnostic tool

### [EncryptionConfig](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.EncryptionConfig)

Represents a custom encryption key configuration that can be applied to a resource. This will encrypt all disks in Virtual Machine.

### [Environment](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Environment)

Definition of a software environment that is used to start a notebook instance.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Event](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Event)

The definition of an Event for a managed / semi-managed notebook instance.

### [Execution](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Execution)

The definition of a single executed notebook.

### [ExecutionTemplate](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ExecutionTemplate)

The description a notebook execution workload.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GetEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetEnvironmentRequest)

Request for getting a notebook environment.

### [GetExecutionRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetExecutionRequest)

Request for getting scheduled notebook execution

### [GetInstanceHealthRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetInstanceHealthRequest)

Request for checking if a notebook instance is healthy.

### [GetInstanceHealthResponse](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetInstanceHealthResponse)

Response for checking if a notebook instance is healthy.

### [GetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetInstanceRequest)

Request for getting a notebook instance.

### [GetRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetRuntimeRequest)

Request for getting a Managed Notebook Runtime.

### [GetScheduleRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetScheduleRequest)

Request for getting scheduled notebook.

### [Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance)

The definition of a notebook instance.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InstanceConfig](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.InstanceConfig)

Notebook instance configurations that can be updated.

### [IsInstanceUpgradeableRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.IsInstanceUpgradeableRequest)

Request for checking if a notebook instance is upgradeable.

### [IsInstanceUpgradeableResponse](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.IsInstanceUpgradeableResponse)

Response for checking if a notebook instance is upgradeable.

### [ListEnvironmentsRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListEnvironmentsRequest)

Request for listing environments.

### [ListEnvironmentsResponse](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListEnvironmentsResponse)

Response for listing environments.

### [ListExecutionsRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListExecutionsRequest)

Request for listing scheduled notebook executions.

### [ListExecutionsResponse](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListExecutionsResponse)

Response for listing scheduled notebook executions

### [ListInstancesRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListInstancesRequest)

Request for listing notebook instances.

### [ListInstancesResponse](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListInstancesResponse)

Response for listing notebook instances.

### [ListRuntimesRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListRuntimesRequest)

Request for listing Managed Notebook Runtimes.

### [ListRuntimesResponse](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListRuntimesResponse)

Response for listing Managed Notebook Runtimes.

### [ListSchedulesRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListSchedulesRequest)

Request for listing scheduled notebook job.

### [ListSchedulesResponse](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListSchedulesResponse)

Response for listing scheduled notebook job.

### [LocalDisk](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.LocalDisk)

A Local attached disk resource.

### [LocalDiskInitializeParams](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.LocalDiskInitializeParams)

Input only. Specifies the parameters for a new disk that will be created alongside the new instance. Use initialization parameters to create boot disks or local SSDs attached to the new runtime. This property is mutually exclusive with the source property; you can only define one or the other, but not both.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [RefreshRuntimeTokenInternalRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.RefreshRuntimeTokenInternalRequest)

Request for getting a new access token.

### [RefreshRuntimeTokenInternalResponse](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.RefreshRuntimeTokenInternalResponse)

Response with a new access token.

### [RegisterInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.RegisterInstanceRequest)

Request for registering a notebook instance.

### [ReportInstanceInfoRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ReportInstanceInfoRequest)

Request for notebook instances to report information to Notebooks API.

### [ReportRuntimeEventRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ReportRuntimeEventRequest)

Request for reporting a Managed Notebook Event.

### [ReservationAffinity](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ReservationAffinity)

Reservation Affinity for consuming Zonal reservation.

### [ResetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ResetInstanceRequest)

Request for resetting a notebook instance

### [ResetRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ResetRuntimeRequest)

Request for resetting a Managed Notebook Runtime.

### [RollbackInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.RollbackInstanceRequest)

Request for rollbacking a notebook instance

### [Runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Runtime)

The definition of a Runtime for a managed notebook instance.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RuntimeAcceleratorConfig](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.RuntimeAcceleratorConfig)

Definition of the types of hardware accelerators that can be used. Definition of the types of hardware accelerators that can be used. See `Compute Engine AcceleratorTypes <https://cloud.google.com/compute/docs/reference/beta/acceleratorTypes>`__. Examples:

  * `nvidia-tesla-k80`
  * `nvidia-tesla-p100`
  * `nvidia-tesla-v100`
  * `nvidia-tesla-p4`
  * `nvidia-tesla-t4`
  * `nvidia-tesla-a100`



### [RuntimeAccessConfig](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.RuntimeAccessConfig)

Specifies the login configuration for Runtime

### [RuntimeMetrics](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.RuntimeMetrics)

Contains runtime daemon metrics, such as OS and kernels and sessions stats.

### [RuntimeShieldedInstanceConfig](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.RuntimeShieldedInstanceConfig)

A set of Shielded Instance options. Check `Images using supported Shielded VM features <https://cloud.google.com/compute/docs/instances/modifying-shielded-vm>`__. Not all combinations are valid.

### [RuntimeSoftwareConfig](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.RuntimeSoftwareConfig)

Specifies the selection and configuration of software inside the runtime. The properties to set on runtime. Properties keys are specified in `key:value` format, for example:

  * `idle_shutdown: true`
  * `idle_shutdown_timeout: 180`
  * `enable_health_monitoring: true`



.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Schedule](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Schedule)

The definition of a schedule.

### [SetInstanceAcceleratorRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.SetInstanceAcceleratorRequest)

Request for setting instance accelerator.

### [SetInstanceLabelsRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.SetInstanceLabelsRequest)

Request for setting instance labels.

### [SetInstanceMachineTypeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.SetInstanceMachineTypeRequest)

Request for setting instance machine type.

### [StartInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.StartInstanceRequest)

Request for starting a notebook instance

### [StartRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.StartRuntimeRequest)

Request for starting a Managed Notebook Runtime.

### [StopInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.StopInstanceRequest)

Request for stopping a notebook instance

### [StopRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.StopRuntimeRequest)

Request for stopping a Managed Notebook Runtime.

### [SwitchRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.SwitchRuntimeRequest)

Request for switching a Managed Notebook Runtime.

### [TriggerScheduleRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.TriggerScheduleRequest)

Request for created scheduled notebooks

### [UpdateInstanceConfigRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpdateInstanceConfigRequest)

Request for updating instance configurations.

### [UpdateInstanceMetadataItemsRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpdateInstanceMetadataItemsRequest)

Request for adding/changing metadata items for an instance.

### [UpdateInstanceMetadataItemsResponse](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpdateInstanceMetadataItemsResponse)

Response for adding/changing metadata items for an instance.

### [UpdateRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpdateRuntimeRequest)

Request for updating a Managed Notebook configuration.

### [UpdateShieldedInstanceConfigRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpdateShieldedInstanceConfigRequest)

Request for updating the Shielded Instance config for a notebook instance. You can only use this method on a stopped instance

### [UpgradeInstanceInternalRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpgradeInstanceInternalRequest)

Request for upgrading a notebook instance from within the VM

### [UpgradeInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpgradeInstanceRequest)

Request for upgrading a notebook instance

### [UpgradeRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpgradeRuntimeRequest)

Request for upgrading a Managed Notebook Runtime to the latest version. option (google.api.message_visibility).restriction = "TRUSTED_TESTER,SPECIAL_TESTER";

### [UpgradeType](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpgradeType)

Definition of the types of upgrade that can be used on this instance.

### [VirtualMachine](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.VirtualMachine)

Runtime using Virtual Machine for computing.

### [VirtualMachineConfig](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.VirtualMachineConfig)

The config settings for virtual machine.

### [VmImage](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.VmImage)

Definition of a custom Compute Engine virtual machine image for starting a notebook instance with the environment installed directly on the VM.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
