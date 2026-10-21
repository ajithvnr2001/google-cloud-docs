---
url: https://docs.cloud.google.com/dataflow/docs/release-notes/
title: Dataflow release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:52:27.673150+00:00
---

# Dataflow release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Resources ](https://docs.cloud.google.com/dataflow/docs/resources)



Send feedback 

#  Dataflow release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to the Dataflow service. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/dataflow-release-notes.xml) directly. 

## October 09, 2026

Feature

Dataflow now supports change data capture (CDC) ingestion from Delta Lake and Apache Iceberg tables into Lakehouse ([Preview](https://cloud.google.com/products#product-launch-stages)).

You can use Dataflow batch jobs (for Delta Lake) or batch and streaming jobs (for Apache Iceberg) to synchronize CDC transaction logs into Lakehouse Apache Iceberg tables. For more information, see [Migrate Delta Lake CDC data into borderless Lakehouse using Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/delta-lake-cdc-df-lakehouse-integration) and [Migrate Apache Iceberg CDC data into borderless Lakehouse using Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/iceberg-cdc-df-lakehouse-integration).

## August 19, 2026

Feature

Dataflow job builder now supports Delta Lake tables as a source. You can now import existing Delta Lake tables from Cloud Storage (`gs://BUCKET_NAME`) directly into Lakehouse using Dataflow's job builder UI without writing code. For more information, see [Import Delta Lake tables into Lakehouse using Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/delta-lake-df-lakehouse-integration).

## July 31, 2026

Feature

You can now pause a Dataflow batch job using the `pause_on_failure` service option. This feature lets you preserve the state of your batch pipeline job, address external issues, and resume processing without losing completed work. You can use this option to automatically pause a job on failure, or use this feature to manually pause a job when you chose to. For more information, see [Pause a Dataflow job](https://docs.cloud.google.com/dataflow/docs/guides/pause-job).

## June 22, 2026

Feature

You can now use [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) disks for Dataflow worker VMs. With Hyperdisk Balanced disks, you can provision IOPS and throughput independently of disk size by using the `diskProvisionedIOPS` and `diskProvisionedThroughput` pipeline options (Java SDK) or `disk_provisioned_iops` and `disk_provisioned_throughput_mibps` pipeline options (Python and Go SDKs). For more information, see [Disk type](https://docs.cloud.google.com/dataflow/docs/guides/configure-worker-vm#disk-type) and [Provision IOPS and throughput](https://docs.cloud.google.com/dataflow/docs/guides/configure-worker-vm#provisioned-performance).

## June 16, 2026

Feature

Dataflow now supports NVIDIA RTX Pro 6000 GPUs. You can use this GPU model to run your Apache Beam pipelines on Dataflow. RTX Pro 6000 GPUs are recommended for large, medium, and small model inference workloads. To configure your workers with this GPU model, set the accelerator type to `nvidia-rtx-pro-6000`. For more information, see [Dataflow support for GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/gpu-support).

## June 15, 2026

Feature

Dataflow has updated and expanded its pipeline update features for streaming jobs:

  * **Automated stop-and-replace updates** : You can perform automated, declarative stop-and-replace updates to streaming jobs.
  * **Parallel updates with the same job name** : When you perform automated parallel updates, you can use the same job name for the new replacement job.
  * **Auto-cancel draining jobs** : When performing parallel or stop-and-replace updates, you can configure Dataflow to automatically cancel the old job if it does not finish draining after a timeout you specify.
  * **Update strategy configuration** : You can explicitly choose between a parallel update (`update_strategy_parallel_job_update`) and a standard in-place update (`update_strategy_in_place_update`) while keeping all other configuration the same.
  * **Template upsert functionality** : When launching pipelines from classic templates, flex templates, Terraform, or Config Connector, you can use the `create_or_update_job` experiment to enable automatic create-or-update (upsert) behavior. If an active job with the specified name already exists, it is updated. Otherwise, a new job is created.



For more information, see [Automated stop and replace](https://docs.cloud.google.com/dataflow/docs/guides/upgrade-guide#automated-stop-replace), [Automated parallel pipeline updates](https://docs.cloud.google.com/dataflow/docs/guides/upgrade-guide#automated-parallel-updates), and [Automatic create or update (upsert) for templates](https://docs.cloud.google.com/dataflow/docs/guides/upgrade-guide#templates-create-or-update).

## April 22, 2026

Feature

Dataflow job builder now supports external Iceberg REST Catalogs as a source. You can now ingest data from external Apache Iceberg REST catalogs (IRC) directly into Lakehouse tables using Dataflow's job builder UI without writing code. For more information, see [Import data from external Iceberg catalogs to Lakehouse using Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/iceberg-df-lakehouse-integration).

Feature

You can now add existing Apache Parquet files from cloud-based storage, for example, Cloud Storage or Amazon S3, to an Apache Iceberg table in Lakehouse using the Dataflow job builder. This process registers the files without moving or rewriting the underlying data. For more information, see [Import Parquet files from storage to Lakehouse using Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/parquet-df-lakehouse-integration).

## April 07, 2026

Feature

When you use `min_ram` or `cpu_count` resource hints for pipeline steps that don't require accelerators, Auto VM Selection (Instance Flexibility) is enabled automatically. With Auto VM Selection, workers are provisioned from a curated list of machine types that meet your RAM and CPU requirements. For more information, see [Auto VM Selection for worker machine types](https://docs.cloud.google.com/dataflow/docs/guides/right-fitting#auto_vm_selection).

## February 27, 2026

Feature

Dataflow support for the [C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series) of Arm processors is now generally available. Arm-based VMs are optimized for power efficiency and can provide improved price-performance for many workloads. For more information, see [Use Arm VMs on Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/use-arm-vms).

## February 02, 2026

Feature

Dataflow Managed I/O now supports rolling upgrades for streaming jobs. With this feature, Dataflow upgrades your Managed I/O connectors in running pipelines as new connector versions become available. For more information, see [Automatic upgrades](https://docs.cloud.google.com/dataflow/docs/guides/managed-io#upgrades).

## January 20, 2026

Feature

Dataflow is available in the Bangkok (`asia-southeast3`) region. Learn more about [Google Cloud locations](https://cloud.google.com/about/locations).

## January 13, 2026

Feature

Dataflow now serves a notice for when the Dataflow [Runner v2](https://docs.cloud.google.com/dataflow/docs/runner-v2) container image of a streaming pipeline will be upgraded. To use a new image and avoid the scheduled maintenance, launch a replacement job before the upgrade. For more information, see [Runner v2 harness update](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#runner_v2_harness_update).

## November 21, 2025

Feature

Dataflow now supports speculative execution for batch pipelines. This feature mitigates the impact of slow-running tasks (_stragglers_) by launching a redundant execution of these tasks. The first task to finish is used, and the other is canceled, which can improve the overall completion time of your pipeline. This feature is generally available. For more information, see [Use speculative execution to avoid stragglers](https://docs.cloud.google.com/dataflow/docs/guides/large-pipeline-best-practices#backup-tasks).

## September 24, 2025

Feature

For jobs that use GPUs, Dataflow now supports the flex-start provisioning model. This flex-start provisioning model can improve your ability to get access to constrained GPU resources for short-duration workloads. This feature is available in Preview and is for batch pipelines only. For more information, see [Configure a provisioning model](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus#optional_configure_a_provisioning_model).

## September 08, 2025

Feature

Dataflow now supports using [secure tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview) to set firewall rules on worker VMs. For more information, see [Use secure tags with Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/routes-firewall#secure_tags).

## August 27, 2025

Feature

Dataflow supports TPUs, Google's custom-designed AI accelerators that are optimized for large-scale AI/ML workloads. This feature lets you accelerate inference workloads on frameworks like PyTorch, JAX, and TensorFlow. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) with an allowlist. For more information, see [Dataflow support for TPUs](https://docs.cloud.google.com/dataflow/docs/tpu/tpu-support).

Feature

Dataflow supports [_specifically targeted_ reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type) for pipelines using accelerators (GPUs or TPUs). This functionality is generally available with an allowlist. For more information, see [Use Compute Engine reservations with Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/compute-engine-reservations#reservations-accelerators).

Change

Dataflow supports NVIDIA® H100 and NVIDIA® H100 Mega GPU types. For more information, see [Dataflow support for GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/gpu-support).

## August 26, 2025

Fixed

Dataflow [Runner v2](https://docs.cloud.google.com/dataflow/docs/runner-v2) fixes an issue that could cause data discrepancies when using splittable DoFns, particularly when processing large datasets as side inputs. This fix ensures that all data is accurately processed and transmitted within the pipeline. This improvement is available in recent Dataflow service releases, and is automatically enabled when using Dataflow Runner v2.

**Note:** After this fix, pipelines that previously experienced data loss due to this issue might consume more resources (such as CPU, memory, and processing time) because more data is being processed. This increase in resource usage is expected and reflects the correct behavior of the pipeline.

## August 11, 2025

Feature

Dataflow now automatically detects performance bottlenecks in streaming jobs. You can see the cause of the bottleneck in the **Step Info** panel to help with troubleshooting.

For more information, see [Troubleshoot bottlenecks](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-bottlenecks).

## June 26, 2025

Feature

Dataflow now supports an automated parallel update workflow for streaming jobs. This feature helps minimize disruption by launching a new replacement job that runs in parallel with the existing job. After a duration of time you specify, the old job is automatically drained.

For more information, see [Run parallel pipelines](https://docs.cloud.google.com/dataflow/docs/guides/upgrade-guide#run-parallel-pipelines).

## June 09, 2025

Feature

Dataflow now supports right fitting for streaming jobs. _Right fitting_ lets you specify resource requirements for an entire pipeline or for specific pipeline steps. Previously, right fitting was only supported for batch pipelines. For more information, see [Streaming right fitting](https://docs.cloud.google.com/dataflow/docs/guides/right-fitting#streaming-right-fitting).

## May 12, 2025

Libraries

### Go

#### [0.11.0](https://github.com/googleapis/google-cloud-go/compare/dataflow/v0.10.6...dataflow/v0.11.0) (2025-05-06)

##### Features

  * **dataflow:** A new enum `StreamingMode` is added ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `bugs` is added to message `.google.dataflow.v1beta3.SdkVersion` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `data_sampling` is added to message `.google.dataflow.v1beta3.DebugOptions` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `default_streaming_mode` is added to message `.google.dataflow.v1beta3.TemplateMetadata` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `default_value` is added to message `.google.dataflow.v1beta3.ParameterMetadata` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `disk_size_gb` is added to message `.google.dataflow.v1beta3.RuntimeEnvironment` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `dynamic_destinations` is added to message `.google.dataflow.v1beta3.PubsubLocation` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `enable_launcher_vm_serial_port_logging` is added to message `.google.dataflow.v1beta3.FlexTemplateRuntimeEnvironment` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `enum_options` is added to message `.google.dataflow.v1beta3.ParameterMetadata` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `group_name` is added to message `.google.dataflow.v1beta3.ParameterMetadata` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `hidden_ui` is added to message `.google.dataflow.v1beta3.ParameterMetadata` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `image_repository_cert_path` is added to message `.google.dataflow.v1beta3.ContainerSpec` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `image_repository_password_secret_id` is added to message `.google.dataflow.v1beta3.ContainerSpec` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `image_repository_username_secret_id` is added to message `.google.dataflow.v1beta3.ContainerSpec` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `name` is added to message `.google.dataflow.v1beta3.ListJobsRequest` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `parent_name` is added to message `.google.dataflow.v1beta3.ParameterMetadata` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `parent_trigger_values` is added to message `.google.dataflow.v1beta3.ParameterMetadata` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `runtime_updatable_params` is added to message `.google.dataflow.v1beta3.Job` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `satisfies_pzi` is added to message `.google.dataflow.v1beta3.Job` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `service_resources` is added to message `.google.dataflow.v1beta3.Job` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `step_names_hash` is added to message `.google.dataflow.v1beta3.PipelineDescription` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `straggler_info` is added to message `.google.dataflow.v1beta3.WorkItemDetails` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `straggler_summary` is added to message `.google.dataflow.v1beta3.StageSummary` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `streaming_mode` is added to message `.google.dataflow.v1beta3.Environment` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `streaming_mode` is added to message `.google.dataflow.v1beta3.FlexTemplateRuntimeEnvironment` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `streaming_mode` is added to message `.google.dataflow.v1beta3.RuntimeEnvironment` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `streaming` is added to message `.google.dataflow.v1beta3.TemplateMetadata` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `supports_at_least_once` is added to message `.google.dataflow.v1beta3.TemplateMetadata` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `supports_exactly_once` is added to message `.google.dataflow.v1beta3.TemplateMetadata` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `trie` is added to message `.google.dataflow.v1beta3.MetricUpdate` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `update_mask` is added to message `.google.dataflow.v1beta3.UpdateJobRequest` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `use_streaming_engine_resource_based_billing` is added to message `.google.dataflow.v1beta3.Environment` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new field `user_display_properties` is added to message `.google.dataflow.v1beta3.JobMetadata` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new message `DataSamplingConfig` is added ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new message `HotKeyDebuggingInfo` is added ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new message `ParameterMetadataEnumOption` is added ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new message `RuntimeUpdatableParams` is added ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new message `SdkBug` is added ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new message `ServiceResources` is added ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new message `Straggler` is added ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new message `StragglerInfo` is added ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new message `StragglerSummary` is added ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new message `StreamingStragglerInfo` is added ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new method_signature `job,update_mask` is added to method `UpdateJob` in service `JobsV1Beta3` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new value `BIGQUERY_TABLE` is added to enum `ParameterType` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new value `BOOLEAN` is added to enum `ParameterType` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new value `ENUM` is added to enum `ParameterType` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new value `GO` is added to enum `Language` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new value `JAVASCRIPT_UDF_FILE` is added to enum `ParameterType` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new value `KAFKA_READ_TOPIC` is added to enum `ParameterType` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new value `KAFKA_TOPIC` is added to enum `ParameterType` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new value `KAFKA_WRITE_TOPIC` is added to enum `ParameterType` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new value `KMS_KEY_NAME` is added to enum `ParameterType` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new value `MACHINE_TYPE` is added to enum `ParameterType` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new value `NUMBER` is added to enum `ParameterType` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new value `SERVICE_ACCOUNT` is added to enum `ParameterType` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new value `WORKER_REGION` is added to enum `ParameterType` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A new value `WORKER_ZONE` is added to enum `ParameterType` ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))



##### Bug Fixes

  * **dataflow:** An existing oauth_scope `https ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** An existing oauth_scope `https ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** An existing oauth_scope `https ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** An existing oauth_scope `https ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** An existing oauth_scope `https ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** An existing oauth_scope `https ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** An existing oauth_scope `https ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** An existing oauth_scope `https ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** An existing oauth_scope `https ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** An existing oauth_scope `https ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** An existing oauth_scope `https ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** An existing oauth_scope `https ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))



##### Documentation

  * **dataflow:** A comment for enum `JobState` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for enum `WorkerIPAddressConfiguration` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for enum value `JOB_VIEW_ALL` in enum `JobView` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `additional_experiments` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `additional_user_labels` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `bypass_temp_dir_validation` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `capabilities` in message `.google.dataflow.v1beta3.SdkHarnessContainerImage` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `current_state` in message `.google.dataflow.v1beta3.Job` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `dataset` in message `.google.dataflow.v1beta3.Environment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `debug_options` in message `.google.dataflow.v1beta3.Environment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `dump_heap_on_oom` in message `.google.dataflow.v1beta3.FlexTemplateRuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `dynamic_template` in message `.google.dataflow.v1beta3.LaunchTemplateRequest` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `enable_hot_key_logging` in message `.google.dataflow.v1beta3.DebugOptions` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `enable_streaming_engine` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `environment` in message `.google.dataflow.v1beta3.Job` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `flex_resource_scheduling_goal` in message `.google.dataflow.v1beta3.Environment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `gcs_path` in message `.google.dataflow.v1beta3.DynamicTemplateLaunchParams` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `gcs_path` in message `.google.dataflow.v1beta3.LaunchTemplateRequest` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `id` in message `.google.dataflow.v1beta3.Job` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `ip_configuration` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `job_name` in message `.google.dataflow.v1beta3.LaunchTemplateParameters` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `kms_key_name` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `launch_parameters` in message `.google.dataflow.v1beta3.LaunchTemplateRequest` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `location` in message `.google.dataflow.v1beta3.Job` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `machine_type` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `max_workers` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `name` in message `.google.dataflow.v1beta3.Job` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `network` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `num_workers` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `project_id` in message `.google.dataflow.v1beta3.Job` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `requested_state` in message `.google.dataflow.v1beta3.Job` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `save_heap_dumps_to_gcs_path` in message `.google.dataflow.v1beta3.FlexTemplateRuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `service_account_email` in message `.google.dataflow.v1beta3.Environment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `service_account_email` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `service_kms_key_name` in message `.google.dataflow.v1beta3.Environment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `service_options` in message `.google.dataflow.v1beta3.Environment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `set` in message `.google.dataflow.v1beta3.MetricUpdate` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `subnetwork` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `temp_location` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `transform_name_mapping` in message `.google.dataflow.v1beta3.Job` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `type` in message `.google.dataflow.v1beta3.Job` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `worker_region` in message `.google.dataflow.v1beta3.Environment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `worker_region` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `worker_zone` in message `.google.dataflow.v1beta3.Environment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `worker_zone` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for field `zone` in message `.google.dataflow.v1beta3.RuntimeEnvironment` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for message `DynamicTemplateLaunchParams` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for message `Job` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for message `JobExecutionStageInfo` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for message `JobMetrics` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for message `LaunchTemplateParameters` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for message `MetricUpdate` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for message `SdkHarnessContainerImage` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for message `Step` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for method `AggregatedListJobs` in service `JobsV1Beta3` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for method `CreateJob` in service `JobsV1Beta3` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for method `CreateJobFromTemplate` in service `TemplatesService` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for method `GetTemplate` in service `TemplatesService` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for method `LaunchTemplate` in service `TemplatesService` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for method `ListJobs` in service `JobsV1Beta3` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))
  * **dataflow:** A comment for service `FlexTemplatesService` is changed ([2f22244](https://github.com/googleapis/google-cloud-go/commit/2f2224464c132fbcf84e82cc4c3fabb21f07e858))



## April 21, 2025

Libraries

### Go

#### [0.10.6](https://github.com/googleapis/google-cloud-go/compare/dataflow/v0.10.5...dataflow/v0.10.6) (2025-04-15)

##### Bug Fixes

  * **dataflow:** Update google.golang.org/api to 0.229.0 ([3319672](https://github.com/googleapis/google-cloud-go/commit/3319672f3dba84a7150772ccb5433e02dab7e201))



## March 17, 2025

Libraries

### Go

#### [0.10.5](https://github.com/googleapis/google-cloud-go/compare/dataflow/v0.10.4...dataflow/v0.10.5) (2025-03-13)

##### Bug Fixes

  * **dataflow:** Update golang.org/x/net to 0.37.0 ([1144978](https://github.com/googleapis/google-cloud-go/commit/11449782c7fb4896bf8b8b9cde8e7441c84fb2fd))



## March 13, 2025

Feature

Dataflow now supports data lineage. Data lineage lets you track how data moves through your systems. This feature is [generally available](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages) (GA). For more information, see [Use data lineage in Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/lineage).

## March 10, 2025

Libraries

### Go

#### [0.10.4](https://github.com/googleapis/google-cloud-go/compare/dataflow/v0.10.3...dataflow/v0.10.4) (2025-03-06)

##### Bug Fixes

  * **dataflow:** Fix out-of-sync version.go ([28f0030](https://github.com/googleapis/google-cloud-go/commit/28f00304ebb13abfd0da2f45b9b79de093cca1ec))



## March 04, 2025

Feature

Dataflow is now available in Stockholm (`europe-north2`).

## January 21, 2025

Feature

Managed I/O now supports automatic upgrades for supported I/O connectors. Using this feature, Dataflow pipelines automatically use the latest reliable version of the connector. This feature is [generally available](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages) (GA). For more information, see [Dataflow managed I/O](https://docs.cloud.google.com/dataflow/docs/guides/managed-io).

## January 06, 2025

Libraries

### Go

#### [0.10.3](https://github.com/googleapis/google-cloud-go/compare/dataflow/v0.10.2...dataflow/v0.10.3) (2025-01-02)

##### Bug Fixes

  * **dataflow:** Update golang.org/x/net to v0.33.0 ([e9b0b69](https://github.com/googleapis/google-cloud-go/commit/e9b0b69644ea5b276cacff0a707e8a5e87efafc9))



## November 18, 2024

Feature

Dataflow is available in Queretaro, Mexico (northamerica-south1). Learn more about Google [Cloud locations](https://cloud.google.com/about/locations).

## July 11, 2024

Feature

You can now use the [Dataflow job builder UI](https://docs.cloud.google.com/dataflow/docs/guides/job-builder) to create and run Dataflow pipelines in the Google Cloud console, without writing any code. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## July 05, 2024

Security

The remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), in OpenSSH has been mitigated. A patched Dataflow VM image that includes an updated OpenSSH is available. For more information about how to apply mitigations, see the [GCP-2024-040 security bulletin](http://cloud.google.com/dataflow/docs/security-bulletins#GCP-2024-040).

## July 03, 2024

Security

A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. Dataflow jobs might create VMs that use an OS image with versions of OpenSSH that are vulnerable to CVE-2024-6387. For more information, see the [GCP-2024-040 security bulletin](http://cloud.google.com/dataflow/docs/security-bulletins#GCP-2024-040).

## July 01, 2024

Change

Dataflow batch jobs are now cancelled after ten days. Previously, they were cancelled after 30 days. See [Quotas and limits](https://docs.cloud.google.com/dataflow/quotas).

## June 21, 2024

Deprecated

Dataflow SQL is deprecated. As of July 31, 2024, you can't access Dataflow SQL in the Google Cloud console. As of January 31, 2025, you can't use Dataflow SQL in the Google Cloud CLI. As a replacement, use [Beam SQL](https://docs.cloud.google.com/dataflow/docs/guides/notebook-advanced#beam-sql).

## June 04, 2024

Feature

Iceberg read/write support is available through the new Managed I/O Java API. For more information, see [Dataflow managed I/O](https://docs.cloud.google.com/dataflow/docs/guides/managed-io).

## May 31, 2024

Feature

You can now [use Metrics Explorer](https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring#metrics-explorer) to find individual DoFns that cause latencies in streaming jobs. These metrics are available in streaming pipelines that use Apache Beam 2.53.0 and later versions. The following new metrics are available:

  * Average message processing time per DoFn (`job/dofn_latency_average`)
  * Maximum message processing time per DoFn (`job/dofn_latency_max`)
  * Minimum message processing time per DoFn (`job/dofn_latency_min`)
  * Number of messages processed per DoFn (`job/dofn_latency_num_messages`)
  * Oldest active message processing time per DoFn (`job/oldest_active_message_age`)
  * Total message processing time per DoFn (`job/dofn_latency_total`)



For more information about Dataflow metrics, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-dataflow).

## May 17, 2024

Change

Dataflow no longer supports the NVIDIA Tesla K80 GPU type. For a list of supported GPU types, see [Dataflow support for GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/gpu-support#availability).

## April 26, 2024

Feature

The following Dataflow templates now support user-defined functions (UDFs) written in Python:

  * [Cloud Storage Text to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-storage-to-bigquery-python-udf)
  * [Cloud Storage Text to BigQuery (Stream)](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/text-to-bigquery-stream-python-udf)
  * [Pub/Sub to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-bigquery-python-udf)
  * [Pub/Sub Proto to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-proto-to-bigquery-python-udf)



## April 05, 2024

Feature

The following Dataflow templates are generally available ([GA](https://cloud.google.com/products#product-launch-stages)):

  * [Google Cloud to Neo4j](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/google-cloud-to-neo4j)
  * [Pub/Sub to Datadog](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-datadog)



## March 28, 2024

Feature

The Dataflow [right fitting](https://docs.cloud.google.com/dataflow/docs/guides/right-fitting) feature is now supported by non-Prime batch pipelines.

## March 15, 2024

Feature

You can now use worker utilization hints to [tune horizontal autoscaling for streaming pipelines](https://docs.cloud.google.com/dataflow/docs/guides/tune-horizontal-autoscaling).

Feature

Added new [autoscaling metrics](https://docs.cloud.google.com/dataflow/docs/guides/autoscaling-metrics):

  * **Autoscaling rationale chart** : explains the factors driving autoscaling decisions
  * **Worker CPU utilization chart** : shows current user worker CPU utilization and customer autoscaling hint value
  * **Timer backlog per stage** : shows an estimate of time needed to materialize the output for windows whose timer has expired
  * **Parallel processing** : the number of keys available for parallel processing



## March 11, 2024

Feature

You can now use [committed use discounts (CUDs)](https://docs.cloud.google.com/dataflow/docs/cuds) with Dataflow streaming jobs. Committed use discounts provide discounted prices in exchange for your commitment to continuously use a certain amount of Dataflow compute resources for a year or longer.

## March 08, 2024

Change

Streaming jobs created after March 7, 2024 automatically encrypt all user data with [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/dataflow/docs/guides/customer-managed-encryption-keys). To enable this encryption for jobs created before March 7, 2024, [drain or cancel the job](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline), and then restart it.

## February 27, 2024

Feature

Dataflow now supports at-least-once streaming mode. You can use this mode to achieve lower latency and reduced costs for workloads that can tolerate duplicate records. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA). For more information, see [Set the pipeline streaming mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes).

## February 21, 2024

Feature

You can now use Gemma models in your Apache Beam inference pipelines. For more information, see [Use Gemma open models with Dataflow](https://docs.cloud.google.com/dataflow/docs/machine-learning/gemma).

## February 15, 2024

Feature

You can now use a turnkey transform to enrich streaming data in your Dataflow pipeline. When you enrich data, you augment the raw data from one source by adding related data from a second source. For more information, see [Enrich streaming data](https://docs.cloud.google.com/dataflow/docs/guides/enrichment).

## February 12, 2024

Feature

Dataflow Streaming Engine now supports [resource-based billing](https://cloud.google.com/dataflow/pricing#streaming-compute-units). When you [enable resource-based billing](https://docs.cloud.google.com/dataflow/docs/streaming-engine#pricing) with Streaming Engine, you're billed for the total resources consumed by your job.

## January 31, 2024

Feature

Dataflow is available in Johannesburg, South Africa (`africa-south1`).

## December 18, 2023

Feature

Dataflow now supports data sampling for pipeline exceptions. With this feature, you can see samples of the data being processed when an unhandled exception occurs. Use exception sampling to help troubleshoot pipeline errors. For more information, see [Use exception sampling](https://docs.cloud.google.com/dataflow/docs/guides/data-sampling#exception-sampling).

## December 12, 2023

Feature

You can now run a job graph validation check to verify whether a replacement job is valid before you launch the new job. For more information, see [Validate a replacement job](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline#validate).

## December 06, 2023

Feature

You can now archive completed Dataflow jobs. When you archive a Dataflow job, the job is moved from the Dataflow Jobs page in the console to the Archived jobs page. For more information, see [Archive Dataflow jobs](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#archive).

## December 05, 2023

Feature

The Dataflow web-based monitoring interface now includes a dashboard that monitors your Dataflow jobs at the project level. For more information, see [Dataflow project monitoring dashboard](https://docs.cloud.google.com/dataflow/docs/guides/project-monitoring).

## November 17, 2023

Change

Dataflow supports NVIDIA® L4 and NVIDIA® A100 80 GB GPU types. For more information, see [Dataflow support for GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/gpu-support).

## November 13, 2023

Feature

The [Cloud Spanner to Vertex AI Vector Search template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-spanner-to-vertex-vector-search) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

Feature

Dataflow jobs now [scale to 4,000 worker VMs](https://docs.cloud.google.com/dataflow/quotas).

## October 23, 2023

Feature

The [Cloud Spanner to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/cloud-spanner-to-bigquery) template for batch pipelines is available in preview.

## September 19, 2023

Feature

Dataflow is now available in Dammam, Saudi Arabia (`me-central2`).

## September 14, 2023

Feature

Dataflow now supports the Tau T2A Arm machine series as a worker machine type. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA). For more information, see [Use Arm VMs on Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/use-arm-vms).

## September 06, 2023

Feature

The following Dataflow templates are generally available ([GA](https://cloud.google.com/products#product-launch-stages)):

  * [BigQuery to Bigtable](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigquery-to-bigtable)
  * [Pub/Sub to Splunk](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-splunk)



## August 22, 2023

Feature

Dataflow is available in Berlin (`europe-west10`).

## August 15, 2023

Feature

You can now update streaming job options without stopping your job. For more information, see [In-flight job option update](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline#in-flight-updates).

Feature

[Dataflow cost monitoring](https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview#cost) is generally available (GA).

## July 27, 2023

Feature

The following Dataflow templates are generally available ([GA](https://cloud.google.com/products#product-launch-stages)):

  * [MySQL to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/mysql-to-bigquery)
  * [PostgreSQL to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/postgresql-to-bigquery)
  * [SQL Server to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/sqlserver-to-bigquery)



## July 26, 2023

Feature

[Dynamic thread scaling](https://docs.cloud.google.com/dataflow/docs/guides/thread-scaling) is generally available (GA). Dynamic thread scaling is a part of Dataflow's suite of vertical scaling features.

## July 25, 2023

Feature

When you run multiple SDK processes on a shared Dataflow GPU, you can improve GPU efficiency and utilization by enabling the [NVIDIA Multi-Process Service (MPS)](https://docs.cloud.google.com/dataflow/docs/gpu/use-nvidia-mps).

## July 24, 2023

Feature

You can now view streaming stragglers in the Google Cloud console. For more information, see [Troubleshoot stragglers in streaming jobs](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-streaming-stragglers).

## June 13, 2023

Feature

Dataflow now supports [Confidential VMs](https://docs.cloud.google.com/compute/confidential-vm/docs) for Dataflow worker VMs. For more information, see [Dataflow service options](https://docs.cloud.google.com/dataflow/docs/reference/service-options).

## May 31, 2023

Feature

Data sampling is now [generally available](https://cloud.google.com/products/#product-launch-stages) (GA). Data sampling lets you observe the data at each step of a pipeline. For more information, see [Use data sampling to observe pipeline data](https://docs.cloud.google.com/dataflow/docs/guides/data-sampling).

## April 21, 2023

Feature

[Dataflow ML](https://docs.cloud.google.com/dataflow/docs/machine-learning) now supports the [Automatic Model Refresh](https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-model-refresh) feature, which lets you update your machine learning model without stopping your Apache Beam pipeline.

## April 19, 2023

Feature

You can now manage Dataflow jobs by using Eventarc. For more information, see [Use Eventarc to manage Dataflow jobs](https://docs.cloud.google.com/dataflow/docs/guides/job-notifications-using-eventarc).

## April 10, 2023

Feature

Dataflow [cost monitoring](https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview#cost) is now available in preview.

## March 30, 2023

Feature

Dataflow is now available in Doha (`me-central1`).

## March 29, 2023

Change

The Dataflow VM image has been updated to include mitigations for multiple vulnerabilities by upgrading to [cos-97-16919-235-30](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m97#cos-97-16919-235-30_). For the full list of mitigations, see the [Container-Optimized OS release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m97#cos-97-16919-235-30_).

Dataflow jobs started on or after March 29, 2023 will run VM instances that use this image.

## March 28, 2023

Feature

Vertical Autoscaling now supports [batch jobs](https://docs.cloud.google.com/dataflow/docs/vertical-autoscaling#batch).

## March 23, 2023

Feature

Dataflow is now available in Turin (`europe-west12`).

## January 03, 2023

Feature

Starting in version 2023-01-03-00_RC00, the [Google-provided Dataflow templates ](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates) support ES6 syntax for JavaScript user-defined functions (UDFs). This change is backwards-compatible. ES5 syntax and existing user-defined functions are still supported.

When you run Google-provided templates using the latest version, your jobs are upgraded automatically on restart. If you want to keep running an earlier version of a template, when you run the template, specify version `2022-12-15-00_RC00` or earlier.

## December 27, 2022

Change

Starting with Beam SDK version 2.44.0, Dataflow will not support running Dataflow jobs with workers in a region that is different from the Dataflow [regional endpoint](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints).

## December 16, 2022

Feature

Dataflow now supports [regional placement](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints#regional_placement) for workers.

## December 15, 2022

Change

The Dataflow VM image has been updated to include mitigations for [OpenSSL CVE-2022-3602](https://nvd.nist.gov/vuln/detail/CVE-2022-3602) by upgrading to [cos-97-16919-189-12](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m97#cos-97-16919-189-12). For jobs that use GPUs, the NVIDIA drivers have also been updated to mitigate the vulnerability. Dataflow jobs started on or after December 14, 2022 will run VM instances that use this image.

## October 04, 2022

Feature

Dataflow is now available in Tel Aviv (`me-west1`).

Change

The Dataflow VM image has been updated to include several mitigations for a recently disclosed hardware speculative execution vulnerability named Retbleed. Dataflow jobs started on or after September 21, 2022 will run VM instances that use this image.

## August 25, 2022

Change

Dataflow now uses Regional Managed Instance Groups (MIGs). Previously, Dataflow used zonal MIGs.

If this change causes you to exceed your quota, set your **Regional managed instance groups** quota to the same limit assigned to your **Managed instance groups** quota. For more information, see [Working with quotas](https://docs.cloud.google.com/docs/quota).

## July 20, 2022

Feature

[Dataflow Prime](https://docs.cloud.google.com/dataflow/docs/guides/enable-dataflow-prime) is now in General Availability.

## July 11, 2022

Feature

You can use the Apache Beam SDK for Go to [create batch and streaming Dataflow pipelines](https://docs.cloud.google.com/dataflow/docs/quickstarts/quickstart-go). This feature is now in General Availability.

## June 07, 2022

Feature

Dataflow is now available in Dallas, Texas (`us-south1`).

## May 24, 2022

Feature

Dataflow is now available in Columbus (`us-east5`).

## May 13, 2022

Feature

Dataflow now supports Flex Template images from private registries. To learn more, see [Use an image from a private registry](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates#use_an_image_from_a_private_registry).

## May 10, 2022

Feature

Dataflow is now available in Madrid (`europe-southwest1`).

## May 03, 2022

Feature

Dataflow is now available in Paris (`europe-west9`).

## April 20, 2022

Feature

Dataflow is now available in Milan (`europe-west8`).

## April 06, 2022

Feature

Dataflow now supports [Runner v2](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#dataflow-runner-v2) in GA for all languages.

## March 31, 2022

Deprecated

Hot key detection and logging is deprecated for streaming pipelines. For information on pipeline debugging, see [Pipeline troubleshooting and debugging](https://docs.cloud.google.com/dataflow/docs/guides/troubleshooting-your-pipeline).

## March 17, 2022

Feature

Dataflow now supports the following [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates) in GA:

  * [Pub/Sub Subscription to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-streaming#cloudpubsubsubscriptiontobigquery)
  * [Pub/Sub Topic to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-streaming#cloudpubsubtobigquery)
  * [Pub/Sub Avro to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-streaming#cloudpubsubavrotobigquery)
  * [Pub/Sub Proto to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-streaming#cloudpubsubprototobigquery)
  * [Pub/Sub to Pub/Sub](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-streaming#cloudpubsubtocloudpubsub)
  * [Pub/Sub to Cloud Storage Avro](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-streaming#cloudpubsubtoavro)
  * [Pub/Sub to Cloud Storage Text](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-streaming#cloudpubsubtogcstext)
  * [Cloud Storage Text to BigQuery (Stream)](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-streaming#gcstexttobigquerystream)
  * [Cloud Storage Text to Pub/Sub (Stream)](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-streaming#gcstexttocloudpubsubstream)
  * [Change Data Capture to BigQuery (Stream)](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-streaming#change-data-capture)
  * [Apache Kafka to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-streaming#kafka-to-bigquery)
  * [BigQuery export to Parquet (via Storage API)](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-batch#bigquery-export-to-parquet-via-storage-api)
  * [Firestore to Cloud Storage Text](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-batch#firestoretogcstext)
  * [Cloud Spanner to Cloud Storage Text](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-batch#cloudspannertogcstext)
  * [Cloud Storage Text to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-batch#gcstexttobigquery)
  * [Cloud Storage Text to Firestore](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-batch#gcstexttofirestore)
  * [Cloud Storage Text to Pub/Sub (Batch)](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-batch#gcstexttocloudpubsub)
  * [Apache Cassandra to Bigtable](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-batch#cassandratocloudbigtable)
  * [Datastream to Cloud Spanner](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-streaming#datastreamtocloudspanner)
  * [File Format Conversion](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-utilities#file-format-conversion)
  * [Bulk Compress Cloud Storage Files](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-utilities#bulkcompressgcsfiles)
  * [Bulk Decompress Cloud Storage Files](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-utilities#bulkdecompressgcsfiles)
  * [Firestore Bulk Delete](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-utilities#firestorebulkdelete)
  * [Streaming Data Generator to Pub/Sub, BigQuery, and Cloud Storage](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-utilities#streamingdatagenerator)



## March 04, 2022

Feature

You can now use the Apache Beam SDK for Go to [create batch Dataflow pipelines](https://docs.cloud.google.com/dataflow/docs/quickstarts/quickstart-go). This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## February 16, 2022

Feature

Profiling Dataflow pipelines with [Cloud Profiler](https://docs.cloud.google.com/dataflow/docs/guides/profiling-a-pipeline) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Use Dataflow integration with Cloud Profiler to monitor pipeline performance.

## January 04, 2022

Feature

Dataflow now fully supports using Identity and Access Management (IAM) custom roles. You can create a custom IAM role and assign it to a [user-managed service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#specifying_a_user-managed_worker_service_account) used in Dataflow instead of assigning the Dataflow Worker role.

## November 16, 2021

Feature

Dataflow is now available in `Santiago` (southamerica-west1).

## September 21, 2021

Announcement

Dataflow now uses [Zonal DNS](https://docs.cloud.google.com/compute/docs/internal-dns#zonal-dns) for worker resources. This enables Dataflow to offer higher reliability guarantees around Internal DNS registration.

## September 07, 2021

Feature

Dataflow now supports [Shielded VM workers](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#dataflow-shielded-vm).

## August 31, 2021

Feature

[Dataflow Prime](https://docs.cloud.google.com/dataflow/docs/guides/enable-dataflow-prime) is now available in Preview.

## August 03, 2021

Feature

Dataflow is now able to use workers, Dataflow Shuffle, Streaming Engine, FlexRS, and regional endpoints in zones in `Toronto` (northamerica-northeast2).

## July 31, 2021

Feature

Dataflow now supports storing [Flex Template](https://docs.cloud.google.com/dataflow/docs/guides/templates/using-flex-templates) images in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview).

## July 22, 2021

Feature

Dataflow now supports [custom containers](https://docs.cloud.google.com/dataflow/docs/guides/using-custom-containers) in GA.

## June 30, 2021

Feature

[GPU](https://docs.cloud.google.com/dataflow/docs/guides/using-gpus) support on Dataflow is now in General Availability.

## June 29, 2021

Feature

Dataflow is now able to use workers, Dataflow Shuffle, Streaming Engine, FlexRS, and regional endpoints in zones in `Delhi` (asia-south2).

## June 28, 2021

Feature

[Dataflow snapshots](https://docs.cloud.google.com/dataflow/docs/guides/using-snapshots) are now available in GA.

## June 22, 2021

Feature

Dataflow is now able to use workers, Dataflow Shuffle, Streaming Engine, FlexRS, and regional endpoints in zones in `Melbourne` (australia-southeast2).

## June 14, 2021

Feature

In addition to scalar functions, Dataflow SQL now supports aggregate user-defined functions (UDFs) for Java. For more information, see [Dataflow SQL user-defined functions](https://docs.cloud.google.com/dataflow/docs/reference/sql/user-defined-functions#java_udfs). This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## June 09, 2021

Feature

Dataflow SQL now supports user-defined functions (UDFs) written using Java. For more information, see [Dataflow SQL user-defined functions](https://docs.cloud.google.com/dataflow/docs/reference/sql/user-defined-functions). This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## May 14, 2021

Feature

You can now enable logging of human-readable hot keys. For more information, see the hot key entry in [Pipeline options](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#debugging).

## May 11, 2021

Feature

[Dataflow Shuffle](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#dataflow-shuffle) is now the default mode for all batch pipelines.

## March 24, 2021

Feature

Dataflow is now able to use workers, Dataflow Shuffle, Streaming Engine, FlexRS, and regional endpoints in zones in `europe-central2` (Warsaw).

## March 22, 2021

Feature

Dataflow SQL now supports user-defined functions (UDFs) written using SQL. For more information, see [Dataflow SQL user-defined functions](https://docs.cloud.google.com/dataflow/docs/reference/sql/user-defined-functions). This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## March 19, 2021

Feature

[Execution details](https://docs.cloud.google.com/dataflow/docs/concepts/execution-details) are now available in Preview.

## February 03, 2021

Feature

Dataflow now [supports](https://cloud.google.com/dataflow/pricing#pricing_details) Dataflow Shuffle, Streaming Engine, FlexRS, and the following [regional endpoints](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints) in GA: 

  * `asia-east2` Hong Kong
  * `asia-northeast2` \- Japan (Osaka)
  * `asia-northeast3` \- Seoul
  * `asia-southeast2` \- Jakarta
  * `europe-north1` \- Finland
  * `us-west3` \- Salt Lake City
  * `us-west4` \- Las Vegas



## January 29, 2021

Announcement

[Flex templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/using-flex-templates) now support updating streaming jobs and Flexible Resource Scheduling (FlexRS).

Feature

[Dataflow snapshots](https://docs.cloud.google.com/dataflow/docs/guides/using-snapshots) are now available in Preview.

## January 25, 2021

Feature

GPU support on Dataflow is currently available in Preview. To enroll in this Preview offering, contact [Support](https://docs.cloud.google.com/support-hub) or [Sales](https://docs.cloud.google.com/contact).

## December 11, 2020

Change

Workers now use the Java 11 runtime.

## December 10, 2020

Feature

Dataflow now supports [custom containers](https://docs.cloud.google.com/dataflow/docs/guides/using-custom-containers) as a Preview offering.

## November 11, 2020

Feature

Dataflow now supports [Interactive Notebooks](https://docs.cloud.google.com/dataflow/docs/guides/interactive-pipeline-development) in GA.

## November 05, 2020

Feature

Dataflow now [supports](https://cloud.google.com/dataflow/pricing#pricing_details) Dataflow Shuffle, Streaming Engine, FlexRS, and the following [regional endpoints](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints) in GA: 

  * `us-west2` (Los Angeles)
  * `southamerica-east1` (São Paulo)
  * `europe-west6` (Zurich)
  * `asia-south1` (Mumbai)



Change

Pub/Sub I/O metrics in the Dataflow and Cloud Monitoring UIs may be unavailable for Dataflow jobs using [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#streaming-engine).

## October 30, 2020

Change

Dataflow Runner v2 is now the default runner for Python streaming pipelines using SDK 2.21.0 and above.

## September 30, 2020

Feature

Dataflow now supports [Flex Templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/using-flex-templates) in GA.

## September 29, 2020

Feature

You can now use a [network tags parameter](https://docs.cloud.google.com/dataflow/docs/guides/routes-firewall#specifying_network_tags) to add network tags to all worker VMs that execute a particular Dataflow job.

## July 27, 2020

Feature

Dataflow now [supports](https://cloud.google.com/dataflow/pricing#pricing_details) Dataflow Shuffle, Streaming Engine, FlexRS, and the following [regional endpoints](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints) in GA: 

  * `northamerica-northeast1` (Montréal)
  * `asia-southeast1` (Singapore)
  * `australia-southeast1` (Sydney)



## June 08, 2020

Feature

Dataflow is now able to use workers in zones in the `asia-southeast2` region (Jakarta).

## April 20, 2020

Feature

Dataflow is now able to use workers in zones in the `us-west4` region (Las Vegas).

## April 15, 2020

Feature

[Cloud Dataflow SQL](https://docs.cloud.google.com/dataflow/docs/guides/sql/dataflow-sql-intro) is now generally available. You can now run parameterized queries from the Dataflow SQL UI.

## April 09, 2020

Feature

Dataflow now provides beta support for [Flex Templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/using-flex-templates).

Feature

Dataflow now provides beta support for [Interactive Notebooks](https://docs.cloud.google.com/dataflow/docs/guides/interactive-pipeline-development).

## April 07, 2020

Feature

Dataflow now [supports](https://cloud.google.com/dataflow/pricing#pricing_details) Dataflow Shuffle, Streaming Engine, FlexRS, and the following [regional endpoints](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints) in GA: 

  * `us-east4` (Northern Virginia)
  * `europe-west2` (London)
  * `europe-west3` (Frankfurt)



## March 03, 2020

Feature

[Cloud Dataflow SQL](https://docs.cloud.google.com/dataflow/docs/guides/sql/dataflow-sql-intro) is now available in beta. You can now do the following in Cloud Dataflow SQL:

  * Write data to two destinations, including Cloud Pub/Sub
  * Specify how to load data into a BigQuery table
  * Set pipeline options in the Cloud Dataflow SQL UI



## February 24, 2020

Feature

Using [Cloud Dataflow with Cloud Key Management Service](https://docs.cloud.google.com/dataflow/docs/guides/customer-managed-encryption-keys) to create a customer-managed encryption key (CMEK) is generally available.

Feature

Cloud Dataflow is now able to use workers in zones in the `us-west3` region (Salt Lake City).

## February 04, 2020

Feature

The Cloud Dataflow monitoring UI now has [enhanced observability features](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf) to help with troubleshooting batch and streaming pipelines.

## January 24, 2020

Feature

Cloud Dataflow is now able to use workers in zones in the `asia-northeast3` region (Seoul).

## November 18, 2019

Feature

[Flexible Resource Scheduling (FlexRS)](https://docs.cloud.google.com/dataflow/docs/guides/flexrs) in Cloud Dataflow is generally available. The service is available in five additional regions:

  * `us-east1` (South Carolina)
  * `us-west1` (Oregon)
  * `asia-east1` (Taiwan)
  * `asia-northeast1` (Tokyo)
  * `europe-west4` (Netherlands)



Feature

You can now do the following in [Cloud Dataflow SQL](https://docs.cloud.google.com/dataflow/docs/guides/sql/dataflow-sql-intro):

  * Use Cloud Storage filesets as a data source
  * Assign schemas to data sources in the Cloud Dataflow SQL UI
  * Preview the content of Cloud Pub/Sub messages from the Cloud Dataflow SQL UI



## October 31, 2019

Feature

Cloud Dataflow [Shuffle](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#cloud-dataflow-shuffle) and [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#streaming-engine) are now available in `us-east1` (South Carolina).

## October 25, 2019

Feature

You can now see [audit logs](https://docs.cloud.google.com/dataflow/docs/guides/customer-managed-encryption-keys#audit_logging_cloud_kms_key_usage) of Cloud KMS key operations and protect [Cloud Dataflow Shuffle](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#cloud-dataflow-shuffle) state using a [customer-managed encryption key](https://docs.cloud.google.com/dataflow/docs/guides/customer-managed-encryption-keys).

## October 08, 2019

Feature

[Python streaming](https://docs.cloud.google.com/dataflow/docs/guides/specifying-exec-params#streaming-execution) for Apache Beam SDK 2.16 or higher is generally available. You can now do the following in Python:

  * [Update](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline) and [Drain](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#drain) streaming pipelines.
  * Enable [streaming autoscaling](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#autoscaling).
  * Use [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#streaming-engine).



Feature

Python 3 support for Apache Beam SDK 2.16.0 or higher is now generally available. This feature provides support for using Python 3.5, 3.6, and 3.7. You can run run any existing Python 2.7 batch and streaming pipelines that use `DirectRunner` or `DataflowRunner`. However, you might need to make changes to ensure that your pipeline code is [compatible with Python 3](https://docs.python.org/3/howto/pyporting.html). Keyword-only arguments (a syntactic construct introduced in Python 3) are not yet supported by Apache Beam SDK. For the current status and summary of recent Python 3-specific improvements, follow updates on the [Apache Beam issue tracker](https://issues.apache.org/jira/browse/BEAM-1251).

## October 07, 2019

Feature

Cloud Dataflow [Shuffle](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#cloud-dataflow-shuffle) and [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#streaming-engine) are now available in two additional regions:

  * `us-west1` (Oregon)
  * `asia-east1` (Taiwan)



## September 03, 2019

Feature

Automatic [hot key detection](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#hot-key-detected) is now enabled in batch pipelines for Apache Beam SDK 2.15.0 or higher.

## August 09, 2019

Feature

Integration with Cloud Dataflow [VPC Service Controls](https://docs.cloud.google.com/dataflow/docs/guides/specifying-networks#vpc-service-controls) is generally available.

## August 02, 2019

Feature

Using [Cloud Dataflow with Cloud Key Management Service](https://docs.cloud.google.com/dataflow/docs/guides/customer-managed-encryption-keys) is now available in beta. Customer-managed encryption keys (CMEK) allow for encryption of your pipeline state. This feature is limited to Persistent Disks attached to Cloud Dataflow workers and used for Persistent Disk-based shuffle and streaming state storage.

## August 01, 2019

Feature

Python 3 support for Apache Beam SDK 2.14.0 or higher is now in beta. This feature provides support for using Python 3.5, 3.6, and 3.7. You can run any existing Python 2.7 batch and streaming pipelines that use `DirectRunner` or `DataflowRunner`. However, you might need to make changes to ensure that your pipeline code is [compatible with Python 3](https://docs.python.org/3/howto/pyporting.html). Some syntactic constructs introduced in Python 3 are not yet fully supported by the Apache Beam SDK. For details and current status, follow updates on the [Apache Beam issue tracker](https://issues.apache.org/jira/browse/BEAM-1251).

## May 16, 2019

Feature

[Cloud Dataflow SQL](https://docs.cloud.google.com/dataflow/docs/guides/sql/dataflow-sql-intro) is now publicly available in alpha. Cloud Dataflow SQL lets you use SQL queries to develop and run Cloud Dataflow jobs from the BigQuery web UI.

## April 18, 2019

Feature

Cloud Dataflow is now able to use workers in zones in the `asia-northeast2` [region](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available) (Osaka, Japan).

## April 10, 2019

Feature

[Streaming autoscaling](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#streaming-autoscaling) is generally available for pipelines that use [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#streaming-engine).

Feature

Cloud Dataflow [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#streaming-engine) is generally available. The service is available in two additional regions:

  * `asia-northeast1` (Tokyo)
  * `europe-west4` (Netherlands)



Note that Streaming Engine requires the Apache Beam SDK for Java, versions 2.10.0 or higher.

Feature

Cloud Dataflow [Shuffle](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#cloud-dataflow-shuffle) is now available in two additional regions:

  * `asia-northeast1` (Tokyo)
  * `europe-west4` (Netherlands)



Feature

Cloud Dataflow provides beta support for [Flexible Resource Scheduling (FlexRS)](https://docs.cloud.google.com/dataflow/docs/guides/flexrs) in the `us-central1` and `europe-west1` [regions](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available).

## April 08, 2019

Issue

Apache Beam SDK for Python can only use [BigQuery resources](https://docs.cloud.google.com/bigquery/docs/locations) in the following regions:

  * Regional locations: `us-west2`, `us-east4`, `europe-north1`, `europe-west2`, `europe-west6`.
  * Multi-regional locations: `EU` and `US`.



Feature

Cloud Dataflow provides beta support for [Flexible Resource Scheduling (FlexRS)](https://docs.cloud.google.com/dataflow/docs/guides/flexrs) in the `us-central1` and `europe-west1` [regions](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available).

## April 01, 2019

Feature

Cloud Dataflow provides beta support for [VPC Service Controls](https://docs.cloud.google.com/dataflow/docs/guides/specifying-networks#vpc-service-controls).

## March 24, 2019

Change

The following SDK versions will be decommissioned later in 2019 due to the [discontinuation of support for JSON-RPC and Global HTTP Batch Endpoints](https://developers.googleblog.com/2018/03/discontinuing-support-for-json-rpc-and.html). Note that this change overrides the release note from December 17, that states that decommissioning was expected to happen in March 2019.

  * Apache Beam SDK for Java, versions 2.0.0 to 2.4.0 (inclusive)
  * Apache Beam SDK for Python, versions 2.0.0 to 2.4.0 (inclusive)
  * Cloud Dataflow SDK for Java, versions 2.0.0 to 2.4.0 (inclusive)
  * Cloud Dataflow SDK for Python, 2.0.0 to 2.4.0 (inclusive)



See the [SDK version support status page](https://docs.cloud.google.com/dataflow/docs/support/sdk-version-support-status) for detailed SDK support status.

## March 20, 2019

Deprecated

Apache Beam SDK 2.4.0 and Cloud Dataflow SDK 2.4.0 are now deprecated. For detailed support status information, see the [SDK version support status](https://docs.cloud.google.com/dataflow/docs/support/sdk-version-support-status) table.

## March 11, 2019

Feature

Cloud Dataflow is now able to use workers in zones in the `europe-west6` [region](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available) (Zürich, Switzerland).

## March 06, 2019

Issue

Apache Beam SDK 2.10.0 depends on [gcsio client library](https://mvnrepository.com/artifact/com.google.cloud.bigdataoss/gcsio) version 1.9.13, which has known issues:

  * Reading side inputs can result in [sending a large number of requests](https://github.com/GoogleCloudPlatform/bigdata-interop/pull/152) to Cloud Storage. As a result, Cloud Dataflow jobs can fail with HTTP 429 errors from Cloud Storage.
  * Apache Beam ParquetIO [fails when reading files](https://github.com/GoogleCloudPlatform/bigdata-interop/commit/8f6443bfd6ee821c5667dd2811cf3fe03167b755) from Cloud Storage.



To work around these issues, either upgrade to Apache Beam SDK 2.11.0, or override the gcsio client library version to 1.9.16 or later.

## February 25, 2019

Feature

You can now view [system latency and data freshness](https://docs.cloud.google.com/dataflow/pipelines/dataflow-monitoring-intf#system_latency_and_data_freshness) metrics for your pipeline in the Cloud Dataflow monitoring interface.

## February 20, 2019

Fixed

2018-2019-Apache Beam SDK 2.10.0 contains fixes for the known issues disclosed on December 20 and February 4.

## February 04, 2019

Issue

In a specific case, users of Apache Beam Java SDKs (2.9.0 and earlier) and Cloud Dataflow Java SDKs (2.5.0 and earlier) might experience data duplication when reading files from Cloud Storage. Duplication might occur when all of the following conditions are true:

  * You are reading files with the content-encoding set to gzip, and the files are [dynamically decompressive transcoded](https://docs.cloud.google.com/storage/docs/transcoding) by Cloud Storage.

  * The file size (decompressed) is larger than 2.14 GB.

  * The input stream runs into an error (and is recreated) after 2.14 GB is read.




As a workaround, do not set the content-encoding header, and store compressed files in Cloud Storage with the proper extension (for example, gz for gzip). For existing files, you can update the content-encoding header and file name with the [gsutil tool](https://docs.cloud.google.com/storage/docs/gsutil).

## December 20, 2018

Issue

Streaming Engine users should not upgrade to SDK 2.9.0 due to a known issue. If you choose to use SDK 2.9.0, you must also set the `enable_conscrypt_security_provider` experimental flag to enable conscrypt, which has known stability issues.

## December 17, 2018

Change

2019-The following decommission notice has been changed. For more information, see the release note for [March 24](https://docs.cloud.google.com/dataflow/docs/resources/release-notes-service#march_24_2019).

Deprecated

2019-The following SDK versions will be decommissioned on March 25 due to the [discontinuation of support for JSON-RPC and Global HTTP Batch Endpoints](https://developers.googleblog.com/2018/03/discontinuing-support-for-json-rpc-and.html). Shortly after this date, you will no longer be able to submit new Cloud Dataflow jobs or update running Cloud Dataflow jobs that use the decommissioned SDKs. In addition, existing streaming jobs that use these SDK versions might fail.

  * Apache Beam SDK for Java, versions 2.0.0 to 2.4.0 (inclusive)
  * Apache Beam SDK for Python, versions 2.0.0 to 2.4.0 (inclusive)
  * Cloud Dataflow SDK for Java, versions 2.0.0 to 2.4.0 (inclusive)
  * Cloud Dataflow SDK for Python, versions 2.0.0 to 2.4.0 (inclusive)



See the [SDK version support status page](https://docs.cloud.google.com/dataflow/docs/support/sdk-version-support-status) for detailed SDK support status.

## October 22, 2018

Feature

Cloud Dataflow is now able to use workers in zones in the `asia-east2` region (Hong Kong).

## October 16, 2018

Deprecated

2018-Cloud Dataflow SDK 1.x for Java is unsupported as of October 16. In the near future, the Cloud Dataflow service will reject new Cloud Dataflow jobs that are based on Cloud Dataflow SDK 1.x for Java. See [Migrating from Cloud Dataflow SDK 1.x for Java](https://docs.cloud.google.com/dataflow/docs/guides/migrate-java-1-to-2) for migration guidance.

## October 03, 2018

Feature

Cloud Dataflow now has a [Public IP parameter](https://docs.cloud.google.com/dataflow/docs/guides/specifying-networks#public_ip_parameter) that allows you to turn off public IP addresses for your worker nodes.

## July 16, 2018

Feature

[Cloud Dataflow Shuffle](https://docs.cloud.google.com/dataflow/service/dataflow-service-desc#cloud-dataflow-shuffle) is now generally available.

## July 10, 2018

Feature

Cloud Dataflow is now able to use workers in zones in the `us-west2` region (Los Angeles).

## June 14, 2018

Feature

[Streaming Engine](https://docs.cloud.google.com/dataflow/service/dataflow-service-desc#dataflow-streaming-engine) is now publicly available in beta. Streaming Engine moves streaming pipeline execution out of the worker VMs and into the Cloud Dataflow service backend.

## June 11, 2018

Feature

You can now specify a [user-managed controller service account](https://docs.cloud.google.com/dataflow/security-and-permissions#controller-service-account) when you run your pipeline job.

Feature

Cloud Dataflow is now able to use workers in zones in the `europe-north1` region (Finland).

## April 26, 2018

Feature

You can now view [side input metrics](https://docs.cloud.google.com/dataflow/pipelines/dataflow-monitoring-intf#side-input-metrics) for your pipeline from the Cloud Dataflow monitoring interface.

## February 21, 2018

Feature

Cloud Dataflow now supports the following [regional endpoints](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) in [GA](https://docs.cloud.google.com/terms/launch-stages): `us-central1`, `us-east1`, `europe-west1`, `asia-east1`, and `asia-northeast1`.

## January 10, 2018

Feature

Cloud Dataflow is now able to use workers in zones in the `northamerica-northeast1` region (Montréal).

Feature

Cloud Dataflow is now able to use workers in zones in the `europe-west4` region (Netherlands).

## October 31, 2017

Feature

Cloud Dataflow is now able to use workers in zones in the `asia-south1` region (Mumbai).

## October 30, 2017

Feature

[Cloud Dataflow Shuffle](https://docs.cloud.google.com/dataflow/service/dataflow-service-desc#cloud-dataflow-shuffle) is now available for pipelines using the Apache Beam SDK for Python version 2.1 or later.

Feature

[Cloud Dataflow Shuffle](https://docs.cloud.google.com/dataflow/service/dataflow-service-desc#cloud-dataflow-shuffle) is now available in the `europe-west1` region.

## October 25, 2017

Feature

Cloud Dataflow provides beta support for additional [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/templates/provided-templates). To get started with templates, follow the [quickstart](https://docs.cloud.google.com/dataflow/docs/quickstarts/quickstart-templates).

  * [Google Cloud Pub/Sub to Google BigQuery](https://docs.cloud.google.com/dataflow/docs/templates/provided-templates#cloudpubsubtobigquery)
  * [Google Cloud Storage Text to Google Cloud Pub/Sub](https://docs.cloud.google.com/dataflow/docs/templates/provided-templates#gcstexttocloudpubsub)
  * [Google Cloud Pub/Sub to Google Cloud Storage Text](https://docs.cloud.google.com/dataflow/docs/templates/provided-templates#cloudpubsubtogcstext)
  * [Google Cloud Datastore to Google Cloud Storage Text](https://docs.cloud.google.com/dataflow/docs/templates/provided-templates#datastoretogcstext)



## October 12, 2017

Fixed

Fixed the known issue disclosed on October 2, 2017.

## October 02, 2017

Issue

Cloud Dataflow 2.x pipelines in which the output of a PTransform is consumed by a flatten and at least one other PTransform results in a malformed graph, leaving the other PTransforms input-less.

## September 20, 2017

Feature

Cloud Dataflow provides beta support for [regional endpoints](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints) `us-central1` and `europe-west1`.

## September 05, 2017

Feature

Cloud Dataflow is now able to use workers in zones in the `southamerica-east1` region (São Paulo).

## August 01, 2017

Feature

Cloud Dataflow is now able to use workers in zones in the `europe-west3` region (Frankfurt).

## July 20, 2017

Feature

You can now access the Stackdriver [error report](https://docs.cloud.google.com/dataflow/pipelines/dataflow-monitoring-intf#error-reporting) for your pipeline directly from the Dataflow monitoring interface.

## June 20, 2017

Feature

Cloud Dataflow is now able to use workers in zones in the `australia-southeast1` region (Sydney).

## June 06, 2017

Feature

Cloud Dataflow is now able to use workers in zones in the `europe-west2` region (London).

## April 25, 2017

Feature

Per-step worker logs are now accessible directly in the Cloud Dataflow UI. Consult the [documentation](https://docs.cloud.google.com/dataflow/pipelines/troubleshooting-your-pipeline) for more information.

## April 11, 2017

Change

The Cloud Dataflow service will now automatically shut down a streaming job if all steps have reached the maximum watermark. This will only affect pipelines in which every source produces only bounded input – e.g., streaming pipelines reading from Cloud Pub/Sub are not affected.

## April 03, 2017

Change

Improved graph layout in the Cloud Dataflow UI.

## September 29, 2016

Feature

Autoscaling for streaming pipelines is now publicly available in beta for use with select sources and sinks. See the autoscaling [documentation](https://docs.cloud.google.com/dataflow/service/dataflow-service-desc#autotuning-features) for more details.

## September 15, 2016

Change

The default autoscaling ceiling for batch pipelines using the Cloud Dataflow SDK for Java 1.6 or newer has been raised to 10 worker VMs. You can specify an alternate ceiling using the `--maxNumWorkers` pipeline option. See the autoscaling [documentation](https://docs.cloud.google.com/dataflow/service/dataflow-service-desc#autotuning-features) for more details.

## August 18, 2016

Change

Autoscaling for batch pipelines using the Cloud Dataflow SDK for Java 1.6 or higher is now being enabled by default. This change will be rolled out to projects over the next several days. By default, the Cloud Dataflow service will cap the dynamic number of workers to a ceiling of 5 worker VMs. The default autoscaling ceiling may be raised in future service releases. You can specify an alternate ceiling using the `--maxNumWorkers` pipeline option. See autoscaling [documentation](https://docs.cloud.google.com/dataflow/service/dataflow-service-desc#autotuning-features) for more details.

## July 27, 2016

Change

Default disk size for pipelines in streaming mode is now 420GB. This change will be rolled out to projects over the next several days.

Feature

Announced beta support for the 0.4.0 release of the Cloud Dataflow SDK for Python. [Get started](https://docs.cloud.google.com/dataflow/docs/quickstarts/quickstart-python) and run your pipeline remotely on the service.

## March 14, 2016

Change

Scalability and performance improvements available when using Cloud Dataflow SDK for Java version 1.5.0:

  * The service now scales to tens of thousands of initial splits when reading from a `BoundedSource`. This includes `TextIO.Read`, `AvroIO.Read`, and `BigtableIO.Read`, among others.
  * The service will now use Avro instead of JSON as a BigQuery export format for `BigQueryIO.Read`. This change greatly increases the efficiency and performance when reading from BigQuery.



## January 29, 2016

Change

Changes to the runtime environment for **streaming** jobs:

  * Files uploaded with `--filesToStage` were previously downloaded to: `/dataflow/packages` on the workers. With the latest service release, files will now be in the location `/var/opt/google/dataflow`. This change was a cleanup intended to better follow standard Linux path conventions.



## January 19, 2016

Change

Changes to the runtime environment for **batch** jobs:

  * Files uploaded with `--filesToStage` were previously downloaded to: `/dataflow/packages` on the workers. With the latest service release, files will now be in the location `/var/opt/google/dataflow`. This change was a cleanup intended to better follow standard Linux path conventions.



## November 13, 2015

Change

Usability improvements in the Monitoring UI:

  * The **Job Log** tab has been renamed **Logs**.
  * The **View Log** button has moved into the **Logs** tab, and renamed **Worker Logs.**



Change

Performance and stability improvements for Streaming pipelines:

  * Addressed a condition that caused a slowly-growing memory usage in streaming workers.
  * Large Window buffers no longer need to fit entirely in memory at once.
  * Improved disk assignment to avoid data locality hotspots.
  * Worker logging is now optimized to avoid filling up the local disk.



## August 12, 2015

Feature

The Cloud Dataflow Service is now generally available.

## August 06, 2015

Change

Performance improvements to the unbounded runner.

Change

Monitoring changes:

  * Added JOB_STATE_CANCELLED as a possible state value for Cloud Dataflow jobs in the Monitoring UI and command-line interface. Appears when the user cancels a job.
  * Temporarily, as part of the above job state introduction, jobs may may show different job states in list view relative to the single job view.
  * Added Compute Engine core-hour count field to the monitoring UI and enabled core-hour counting for bounded jobs (field is populated with "-" for unbounded jobs).



## July 28, 2015

Change

Added a check during job creation to ensure active job names are unique within each project. You may no longer create a new job with the same name as an active job. If there are already active jobs with the same name running in the system, they will not be impacted by this change.

## April 23, 2015

Change

Improvements to the monitoring UI. Clicking **View Log** for a stage now defaults to display the logs generated by user code on the worker machines.

## April 16, 2015

Feature

The Cloud Dataflow Service is now in beta.

Change

Improvements to the monitoring UI: The job details page now provides more job information including job duration, and job type. For streaming pipelines, it additionally provides data watermark.

## April 13, 2015

Change

Default disk size in batch is 250 GB.

Feature

Command line interface now available for Cloud Dataflow in [`gcloud alpha`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataflow).

## April 09, 2015

Change

Default VM for batch jobs is now `n1-standard-1`.

Change

Improvements to the monitoring UI: Improved organization of pipeline visualization.

Change

Performance improvements for the service.

Change

Improved resource teardown operations on job completion and cancellations.

## April 03, 2015

Change

Improvements to the monitoring UI: The list of jobs now includes name, type, start time, and job ID.

## March 27, 2015

Feature

Improved mechanisms for elastic scaling of compute resources. Batch pipelines can now grow and shrink the worker pool size at different stages of execution.

## March 20, 2015

Change

Monitoring changes:

  * Jobs summary page now shows the status of the current job.
  * Performance improvements to the UI.



## March 06, 2015

Change

Workers now use the Java 8 runtime.

## March 01, 2015

Change

Streaming support enabled for all projects participating in alpha.

Feature

Dynamic work rebalancing

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
