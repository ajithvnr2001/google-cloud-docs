---
url: https://docs.cloud.google.com/dataflow/docs/guides/configure-worker-vm/
title: Configure Dataflow worker VMs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:20.523156+00:00
---

# Configure Dataflow worker VMs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/configure-worker-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Configure Dataflow worker VMs Stay organized with collections  Save and categorize content based on your preferences. 

Customizing worker VMs lets you customize compute and storage resources to your pipeline's memory and processing requirements. This helps you optimize job performance and manage infrastructure costs for resource-intensive workloads.

By default, Dataflow selects the machine type for the worker VMs that run your job, along with the size and type of Persistent Disk. To customize these resources, set the following [pipeline options](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#worker-level_options) when you create the job.

## Machine type

The Compute Engine [machine type](https://docs.cloud.google.com/compute/docs/machine-types) that Dataflow uses when starting worker VMs. You can use x86 or Arm machine types, including custom machine types.

**Note:** Dataflow Prime doesn't support designating specific VM types. For more information, see [Unsupported features](https://docs.cloud.google.com/dataflow/docs/guides/enable-dataflow-prime#unsupported_features).

### Java

Set the `workerMachineType` pipeline option.

### Python

Set the `machine_type` pipeline option.

### Go

Set the `worker_machine_type` pipeline option.

  * For [Arm](https://docs.cloud.google.com/compute/docs/machine-resource#arm), the [Tau T2A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines) and [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series) machine series are supported. For more information about using Arm VMs, see [Use Arm VMs in Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/use-arm-vms).

  * [x86 VMs](https://docs.cloud.google.com/compute/docs/machine-resource#x86) are automatically supported.

  * [Shared-core](https://docs.cloud.google.com/compute/docs/machine-resource#shared-core-types) machine types (for example, `f1-micro`, `g1-small`, `e2-micro`, `e2-small`, and `e2-medium`) are not recommended for Dataflow jobs and are not supported under the [Dataflow Service Level Agreement](https://cloud.google.com/dataflow/sla).

  * Billing is independent of the machine type family. For more information, see [Dataflow pricing](https://cloud.google.com/dataflow/pricing).

  * For `f1-micro` and `g1-small` machine types, Dataflow bills as if they have 1 vCPU, and for `e2-micro`, `e2-small`, and `e2-medium` machine types, Dataflow bills as if they have 2 vCPUs. These rates are billed even though shared-core machine types provide less than their billed vCPUs of sustained CPU time.




### Custom machine types

To specify a custom machine type, use the following format: `FAMILY-vCPU-MEMORY`. Replace the following:

  * FAMILY. Use one of the following values: Machine series| Value  
---|---  
N1| `custom`  
N2| `n2-custom`  
N2D| `n2d-custom`  
E2| `e2-custom`  
  * vCPU. The number of vCPUs.
  * MEMORY. The memory, in MB.



To enable [extended memory](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory), append `-ext` to the machine type. Examples: `n2-custom-6-3072`, `n2-custom-2-32768-ext`.

For more information about valid custom machine types, see [Custom machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types) in the Compute Engine documentation.

### Unsupported machine types for Hyperdisk Balanced

When you use Hyperdisk Balanced disks, your job might fail with an error similar to the following:
    
    
    hyperdisk-balanced disk type cannot be used by MACHINE_TYPE machine type
    

This happens if you select a machine type that's incompatible with Hyperdisk Balanced. This error can also happen when no machine type is specified, or when you use autoVM. For a list of machine types compatible with Hyperdisk Balanced, see [About Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#machine-series).

## Disk type

The type of [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks#pdspecs) to use.

Don't specify a Persistent Disk when using either [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine) or the N4 machine type.

### Java

Set the `workerDiskType` pipeline option.

### Python

Set the `worker_disk_type` pipeline option.

### Go

Set the `disk_type` pipeline option.

To specify the disk type, use the following format: `compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/diskTypes/DISK_TYPE`.

Replace the following:

  * PROJECT_ID: your project ID
  * ZONE: the zone for the Persistent Disk, for example `us-central1-b`
  * DISK_TYPE: the disk type, for example `pd-ssd`, `pd-standard`, or `hyperdisk-balanced`



For more information, see the Compute Engine API reference page for [diskTypes](https://docs.cloud.google.com/compute/docs/reference/latest/diskTypes).

## Provision IOPS and throughput

When you use Hyperdisk Balanced disks, you can provision IOPS and throughput independently of disk size. To provision IOPS and throughput, use the following [pipeline options](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#worker-level_options):

### Java

  * To provision IOPS, set the `diskProvisionedIOPS` pipeline option.
  * To provision throughput in MiB/s, set the `diskProvisionedThroughput` pipeline option.



### Python

  * To provision IOPS, set the `disk_provisioned_iops` pipeline option.
  * To provision throughput in MiB/s, set the `disk_provisioned_throughput_mibps` pipeline option.



### Go

  * To provision IOPS, set the `disk_provisioned_iops` pipeline option.
  * To provision throughput in MiB/s, set the `disk_provisioned_throughput_mibps` pipeline option.



If you don't set these options, jobs that use `hyperdisk-balanced` disks default to the baseline performance of 3,000 IOPS and 140 MiB/s throughput. For more information, see [About Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) in the Compute Engine documentation.

### Limitations

  * Provisioning IOPS and throughput for the Hyperdisk Balanced is supported in Apache Beam SDK versions 2.74.0 or later.



## Disk size

The Persistent Disk size.

### Java

Set the `diskSizeGb` pipeline option.

### Python

Set the `disk_size_gb` pipeline option.

### Go

Set the `disk_size_gb` pipeline option.

If you set this option, specify at least 30 GB to account for the worker boot image and local logs.

Lowering the disk size reduces available shuffle I/O. Shuffle-bound jobs not using Dataflow Shuffle or Streaming Engine may result in increased runtime and job cost.

### Batch jobs

For batch jobs using [Dataflow Shuffle](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch), this option sets the size of a worker VM boot disk. For batch jobs not using Dataflow Shuffle, this option sets the size of the disks used to store shuffled data; the boot disk size is not affected.

If a batch job uses Dataflow Shuffle, then the default disk size is 25 GB. Otherwise, the default is 250 GB.

### Streaming jobs

For streaming jobs using [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine), this option sets size of the boot disks. For streaming jobs not using Streaming Engine, this option sets the size of each additional Persistent Disk created by the Dataflow service; the boot disk is not affected.

If a streaming job doesn't use Streaming Engine, you can set the boot disk size with the experiment flag `streaming_boot_disk_size_gb`. For example, specify `--experiments=streaming_boot_disk_size_gb=80` to create boot disks of 80 GB.

If a streaming job uses Streaming Engine, then the default disk size is 30 GB. Otherwise, the default is 400 GB.

## Minimum CPU platform

If you have performance-sensitive workloads that depend on specific CPU features, you can specify a minimum CPU platform for worker VMs. This option ensures that Dataflow workers use a processor that meets or exceeds the specified CPU generation.

**Note:** Dataflow Prime doesn't support specifying a minimum CPU platform. For more information, see [Unsupported features](https://docs.cloud.google.com/dataflow/docs/guides/enable-dataflow-prime#unsupported_features).

To specify the minimum CPU platform, set the `min_cpu_platform` [experimental pipeline option](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options#experimental). The value must be the exact name of the selected CPU platform, such as `AMD Milan` or `Intel Ice Lake`. For example, specify `--experiments=min_cpu_platform='AMD Milan'` to set the minimum CPU platform to AMD Milan. For a list of supported minimum CPU platforms, see [Availability of CPU platforms](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform#availablezones). For information about limitations, see [limitations when specifying a minimum CPU platform](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform#limitations).

To verify that the Dataflow worker VMs are created with the specified minimum CPU platform, check the Cloud Logging entries for the job as follows:

  1. Navigate to the Cloud Logging console in the Google Cloud console.
  2. Use the following filter and replace the example CPU platform and Dataflow job ID with the information for your job.
         
         resource.type="gce_instance"
         protoPayload.request.minCpuPlatform="AMD Milan"
         "dataflow_job_id"
         

  3. Look at the resulting logs to confirm that Dataflow successfully specified the minimum CPU platform during the VM creation process.




## Use Cloud Storage FUSE to mount your Cloud Storage buckets onto Dataflow VMs

Cloud Storage FUSE lets you mount your Cloud Storage buckets directly with Dataflow VMs, allowing software to access files as if they are local. This integration eliminates the need for pre-downloading data, streamlining data access for your workloads. For more information, see [Process ML data using Dataflow and Cloud Storage FUSE](https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-process-dataflow-fuse).

## What's next

  * [Set Dataflow pipeline options ](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options)
  * [Use Arm VMs on Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/use-arm-vms)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
