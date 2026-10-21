---
url: https://docs.cloud.google.com/dataflow/docs/concepts/design-for-flexibility-and-efficiency/
title: Design for flexibility and efficiency on Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T22:59:25.517735+00:00
---

# Design for flexibility and efficiency on Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/concepts/design-for-flexibility-and-efficiency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Design for flexibility and efficiency on Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

This document explains design for flexibility and efficiency (DFE), a set of architectural best practices for building resilient Dataflow pipelines. 

Transitioning from rigid infrastructure constraints to flexible resource definitions helps you:

  * Maximize compute resource obtainability.
  * Ensure seamless autoscaling during periods of high regional demand.
  * Prevent pipeline launch delays and eliminate capacity bottlenecks.



For example, instead of restricting your pipeline to one specific machine type in one zone, such as requiring `n1-standard-4` workers in `us-central1-a`, you can set minimum resource needs (like 4 vCPUs and 16 GB of RAM). If `us-central1-a` or the N1 machine series experiences temporary capacity constraints, Dataflow can automatically provision compatible worker VMs across other zones and machine families (such as E2, N2, or N2D). This flexibility helps to ensure that your pipeline starts and scales without waiting for a single constrained hardware pool.

This document is intended for data engineers, cloud architects, and platform administrators who manage Dataflow workloads and want to optimize pipeline reliability, throughput, and infrastructure availability.

## Overview of DFE

Dataflow is a fully managed, serverless data processing service that dynamically provisions Compute Engine virtual machine (VM) instances to execute Apache Beam pipelines. In large-scale batch processing and streaming pipelines, worker pools frequently scale up to dozens or hundreds of VM instances.

Pipelines configured with rigid infrastructure constraints are susceptible to provisioning delays during periods of high demand. Examples of rigid constraints include the following:

  * Hardcoding a single machine type, such as `n1-standard-4`.
  * Pinning the pipeline to a specific Compute Engine zone.



If that specific machine type or zone experiences temporary high demand, Dataflow can't allocate compute resources. This can cause provisioning delays or errors such as `ZONE_RESOURCE_POOL_EXHAUSTED` or `RESOURCE_POOL_EXHAUSTED`.

Using DFE principles helps you shift your pipeline architecture from rigid, static infrastructure declarations to flexible, requirement-based resource definitions. This flexibility lets Dataflow dynamically distribute compute across diverse, available hardware pools in Google Cloud, helping you maximize compute obtainability while minimizing operational overhead.

## Best practices for DFE

Adopt the following best practices to maximize compute obtainability, improve autoscaling responsiveness, and build resilient pipelines.

### Enable Auto VM Selection

Rather than hardcoding a static machine type with the [worker machine type](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#worker-level_options) pipeline option, use [Auto VM selection](https://docs.cloud.google.com/dataflow/docs/guides/right-fitting#auto_vm_selection) with Apache Beam resource hints. When you specify minimum resource requirements (`min_ram` or `cpu_count`), Dataflow automatically enables instance flexibility and provisions workers from a list of compatible machine types.

**Workload support:**

  * **Batch pipelines:** Right-fitting and Auto VM Selection are automatically enabled when you specify resource hints.
  * **Streaming pipelines:** Right-fitting requires setting the `--experiments=enable_streaming_rightfitting` pipeline option, along with [horizontal autoscaling](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling) (enabled by default) and [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#streaming-engine) (`--enable_streaming_engine`).



To configure Auto VM Selection, specify minimum resource requirements (`min_ram` or `cpu_count`) at the pipeline level using command-line options, SDK pipeline options, or Flex Template execution parameters. For detailed setup instructions and code examples for Java and Python, see [Use resource hints](https://docs.cloud.google.com/dataflow/docs/guides/right-fitting#use_resource_hints).

### Use regional worker placement (avoid zonal pinning)

Configure Dataflow to dynamically schedule worker VMs across any healthy zone within your chosen region.

Specify the [`--region`](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints) pipeline option and omit `--zone` and `--worker_zone`. For example:
    
    
    --region=us-central1
    

**Note:** Regional worker placement requires [Dataflow Shuffle](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch) for batch jobs or [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine) for streaming jobs.

### Decouple state and shuffle using managed services

Pipelines that don't use managed backend services execute shuffle data operations and streaming state storage directly on worker VM disks and memory. This tight coupling requires larger worker disks and binds workload survival to specific VM instances, making worker replacement harder during capacity constraints.

  * **For Batch jobs - use[Dataflow Shuffle](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch)**: Dataflow Shuffle is enabled by default for batch pipelines running on supported worker machine types and offloads shuffle operations from worker VMs to a dedicated, Google-managed backend service.
  * **For Streaming jobs - use[Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine)**: Streaming Engine offloads window state storage and timer management from worker VMs to a specialized, highly responsive backend infrastructure. For pipelines using Apache Beam SDK 2.30.0 or later, Streaming Engine is enabled by default. To explicitly enable it, pass the `--enable_streaming_engine` pipeline option.



### Use flexible resource scheduling (FlexRS) for batch pipelines

For non-time-critical batch workloads such as nightly ETL, data lake ingestion, or daily rollups, use [Flexible Resource Scheduling (FlexRS)](https://docs.cloud.google.com/dataflow/docs/guides/flexrs).

To enable FlexRS, set the flexRS goal pipeline option:

  * For Python pipelines: `--flexrs_goal=COST_OPTIMIZED`
  * For Java pipelines: `--flexRSGoal=COST_OPTIMIZED`



### Configure flexible launcher VM types for Flex Templates

When launching pipelines using [Flex Templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/using-flex-templates), the pipeline launcher VM defaults to `e2-standard-2`. The default VM works in most cases, but if you experience capacity constraints, you can customize the configuration by using the [`--launcher-machine-type`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run#--launcher-machine-type) option when running the `gcloud dataflow flex-template run` command:
    
    
    gcloud dataflow flex-template run my-job \
        --template-file-gcs-location="gs://my-bucket/template.json" \
        --region="us-central1" \**    --launcher-machine-type="n2-standard-2"**
    

## Operational considerations and trade-offs

While adopting DFE best practices significantly improves compute obtainability, autoscaling responsiveness, and operational reliability, consider the following operational factors and trade-offs when designing your architecture:

### Auto VM Selection considerations

  * **Reliability versus peak performance:** Auto VM Selection prioritizes job launch reliability and compute obtainability over peak execution performance. Because Dataflow provisions from multiple candidate machine families (such as E2, N2, N4, and N2D), runtime performance and throughput might vary slightly depending on which machine family is provisioned. For compute-intensive workloads with strict execution SLAs, test your pipeline with Auto VM Selection to establish a performance baseline before deploying it broadly. If a workload requires a specific hardware platform or clock speed and you can tolerate capacity constraints, you can continue to set a specific machine type.
  * **Compute Engine quota across candidate families:** Because Auto VM Selection can provision workers from multiple candidate machine families, make sure your Google Cloud project has sufficient Compute Engine vCPU and memory quota for each candidate family in your target region. If a capacity shortage occurs in the primary family and your project lacks quota for the fallback family, worker provisioning fails with a `QUOTA_EXCEEDED` error.
  * **Streaming pipeline prerequisite:** For streaming pipelines, right-fitting and Auto VM Selection aren't enabled by default. You must explicitly specify `--experiments=enable_streaming_rightfitting` and make sure that both Streaming Engine (`--enable_streaming_engine`) and horizontal autoscaling are active.
  * **Configuration exclusions:** Auto VM Selection is automatically bypassed or not supported if you configure any of the features or options in the following table:

Feature | Flag or configuration option | Notes  
---|---|---  
Explicit machine types | `--worker_machine_type` or `--machine_type` (Python)  
`--workerMachineType` (Java) | Auto VM Selection is bypassed in favor of the specified machine type.  
Custom disk types, provisioned IOPS, or throughput | `--disk_type`, `--disk_provisioned_iops`, or `--disk_provisioned_throughput_mibps` | Auto VM Selection is bypassed. Setting a custom disk size with `--disk_size_gb` is supported.  
Minimum CPU platforms | `--min_cpu_platform` (Python)  
`--minCpuPlatform` (Java) | Setting a minimum CPU platform bypasses Auto VM Selection.  
Confidential VM | `--experiments=enable_confidential_compute` | Confidential VM instances aren't supported with Auto VM Selection.  
GPU or TPU accelerators | `--dataflow_service_options=worker_accelerator=...` or `accelerator` resource hint | Auto VM Selection applies only to workloads without accelerators.  
Dataflow Prime | `--dataflow_service_options=enable_prime` | Dataflow Prime uses vertical autoscaling and dynamic right-fitting instead of Auto VM Selection.  
Flexible Resource Scheduling (FlexRS) | `--flexrs_goal=COST_OPTIMIZED` (Python)  
`--flexRSGoal=COST_OPTIMIZED` (Java) | FlexRS manages its own worker pool and scheduling buffer.  



### Flexible Resource Scheduling (FlexRS) trade-offs

  * **Scheduling delay window:** FlexRS can introduce a scheduling buffer of up to 6 hours before job execution begins. Don't use FlexRS for pipelines with strict time-to-completion SLAs or tight downstream dependencies.



### Regional placement and data locality

  * **Managed service prerequisite:** Regional worker placement is supported only for jobs that use Dataflow Shuffle for batch or Streaming Engine for streaming. Jobs that don't use these managed backend services use automatic zone placement, which selects a single best zone within the region.
  * **Data locality and cross-region egress:** Regional placement distributes workers across available zones within your chosen region. To minimize network latency and avoid inter-region network egress charges, make sure that all data sources and sinks (such as Cloud Storage buckets, BigQuery datasets, and Pub/Sub topics) reside in the same region as your Dataflow job.



### Compute Engine reservations

  * **Reservation affinity:** On-demand Dataflow jobs automatically consume matching Compute Engine reservations that use `ANY` reservation affinity. However, Auto VM Selection doesn't support consuming instances from specific named reservations.
  * **Suitability for transient workloads:** Compute Engine reservations are generally not recommended for surge-prone, autoscaling, or short-lived batch workloads. Additionally, creating new reservations during an active zonal shortage fails with the same capacity constraints as on-demand VM creation.



## What's next

  * [Optimize Dataflow resource utilization with Auto VM selection](https://docs.cloud.google.com/dataflow/docs/guides/right-fitting#auto_vm_selection)
  * [Dataflow Shuffle overview](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch)
  * [Dataflow Streaming Engine overview](https://docs.cloud.google.com/dataflow/docs/streaming-engine)
  * [Using Flexible Resource Scheduling (FlexRS)](https://docs.cloud.google.com/dataflow/docs/guides/flexrs)
  * [Troubleshoot resource pool exhaustion errors](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#zone_resource_pool_exhausted_with_details)
  * [Troubleshoot template launcher VM resource exhaustion](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-templates#launcher-resource-exhaustion)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
