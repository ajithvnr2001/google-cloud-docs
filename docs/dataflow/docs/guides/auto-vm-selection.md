---
url: https://docs.cloud.google.com/dataflow/docs/guides/auto-vm-selection/
title: Auto VM Selection \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:33:36.107921+00:00
---

# Auto VM Selection  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/auto-vm-selection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Auto VM Selection Stay organized with collections  Save and categorize content based on your preferences. 

When you pin a job to a specific machine type using the [`workerMachineType` pipeline option](https://docs.cloud.google.com/dataflow/docs/guides/configure-worker-vm#machine-type), you risk experiencing delays or job failures due to resource stockouts. Auto VM Selection addresses this problem by automatically choosing workers from a pool of compatible and available machine types using Compute Engine [instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility). This helps to ensure that your Dataflow pipelines acquire capacity reliably, helping you maintain consistent performance and avoid interruptions.

## Unsupported configurations

Auto VM Selection is turned off if your pipeline is configured with any of the following:

  * [Dataflow Prime](https://docs.cloud.google.com/dataflow/docs/guides/enable-dataflow-prime) is enabled.
  * The `min_cpu_platform` pipeline option is set.
  * [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) disks or custom provisioned performance (IOPS and throughput) are used. Jobs started with these configurations will fail.
  * [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/about-cvm) is enabled.
  * Accelerators (GPUs or TPUs) are required.



Additionally, Auto VM Selection is not supported for jobs using Shuffle Appliance or Streaming Appliance.

**Note:** To ensure maximum compatibility and allow the use of newer machine generations, don't specify a disk type when using Auto VM Selection.

## Enable Auto VM Selection

Auto VM Selection is enabled automatically in any of the following scenarios:

  * If you set `min_ram` or `cpu_count` [resource hints](https://docs.cloud.google.com/dataflow/docs/guides/right-fitting) for pipeline steps that don't require accelerators (GPUs or TPUs). For information about how to use resource hints with template-based jobs, see [Pipeline resource hints](https://docs.cloud.google.com/dataflow/docs/guides/right-fitting#pipeline_resource_hints).



## Auto VM Selection behavior

Configure `min_ram` and `cpu_count` resource hints either in isolation or in combination. For example:

  1. A job with only `cpu_count=2` may provision instances with `n4-standard-2` (2 vCPUs, 8 GB RAM), `c4-standard-2` (2 vCPUs, 7 GB RAM) and other machine types.
  2. A job with both `cpu_count=4` and `min_ram=16GB` may provision instances with `n4-standard-4` (4 vCPUs, 16 GB RAM), `c4-highmem-4` (4 vCPUs, 31 GB RAM) and other machine types.



Auto VM Selection optimizes VM selection for resource obtainability. This means that you might experience reduced performance while using Auto VM Selection to improve the obtainability of some of your highly-tuned jobs. We recommend that you test Auto VM Selection on a subset of your existing jobs before gradually deploying them more broadly. For more information about obtainability, see [Improve resource obtainability for jobs](https://docs.cloud.google.com/batch/docs/improve-obtainability-overview) in the Batch documentation.

Dataflow attempts to use 4th generation machine families first (for example, N4 or C4) to offer better efficiency. If 4th generation machines are unavailable in your region, lack sufficient quota, or are incompatible with your configurations, Dataflow automatically falls back to widely available 2nd generation machine families (for example, N2 or E2) to ensure your job can start without capacity delays.

If you specify a disk type such as `pd-ssd` or `pd-standard` when enabling Auto VM Selection using resource hints (right fitting), Dataflow only provisions compatible 2nd generation machine families. To ensure maximum compatibility and allow the use of newer machine generations, don't assign a disk type.

## Compute Engine reservations

If you use Compute Engine reservations with Auto VM Selection, note the following:

  * If you have reservations configured to be [consumed automatically](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#auto-reservations), they might be used if Auto VM Selection provisions machine types that match the reservation.
  * Auto VM Selection consumes compute instances as they are available. Consequently, you can't specify that the service [consume instances from a specific reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation).



## Known issues

When using Auto VM Selection, be aware of the following known issues:

### Unexpected parallelism

If you observe low CPU utilization or unexpected parallelism on worker VMs when using Auto VM Selection with right fitting, it might be due to a known issue where the number of threads per worker isn't automatically set to match the selected machine type's vCPU count.

To work around this issue, you can explicitly set the number of worker harness threads by using the `numberOfWorkerHarnessThreads` [pipeline option](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#resource_utilization). This option applies globally to all worker pools in the pipeline.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
