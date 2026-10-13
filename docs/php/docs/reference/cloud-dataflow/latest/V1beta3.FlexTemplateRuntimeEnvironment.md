---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.FlexTemplateRuntimeEnvironment
title: Google Cloud Dataflow V1beta3 Client - Class FlexTemplateRuntimeEnvironment (0.11.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:47.389626+00:00
---

# Google Cloud Dataflow V1beta3 Client - Class FlexTemplateRuntimeEnvironment (0.11.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.FlexTemplateRuntimeEnvironment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataflow V1beta3 Client - Class FlexTemplateRuntimeEnvironment (0.11.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.3 (latest)  0.10.0  0.9.3  0.8.2  0.7.1  0.6.6  0.5.1  0.4.1  0.3.10 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataflow V1beta3 Client class FlexTemplateRuntimeEnvironment.

The environment values to be set at runtime for flex template.

Generated from protobuf message `google.dataflow.v1beta3.FlexTemplateRuntimeEnvironment`

## Namespace

Google \ Cloud \ Dataflow \ V1beta3

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ num_workers` |  `int`   
The initial number of Google Compute Engine instances for the job.  
`↳ max_workers` |  `int`   
The maximum number of Google Compute Engine instances to be made available to your pipeline during execution, from 1 to 1000.  
`↳ zone` |  `string`   
The Compute Engine [availability zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones) for launching worker instances to run your pipeline. In the future, worker_zone will take precedence.  
`↳ service_account_email` |  `string`   
The email address of the service account to run the job as.  
`↳ temp_location` |  `string`   
The Cloud Storage path to use for temporary files. Must be a valid Cloud Storage URL, beginning with `gs://`.  
`↳ machine_type` |  `string`   
The machine type to use for the job. Defaults to the value from the template if not specified.  
`↳ additional_experiments` |  `string[]`   
Additional experiment flags for the job.  
`↳ network` |  `string`   
Network to which VMs will be assigned. If empty or unspecified, the service will use the network "default".  
`↳ subnetwork` |  `string`   
Subnetwork to which VMs will be assigned, if desired. You can specify a subnetwork using either a complete URL or an abbreviated path. Expected to be of the form "<https://www.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNETWORK>" or "regions/REGION/subnetworks/SUBNETWORK". If the subnetwork is located in a Shared VPC network, you must use the complete URL.  
`↳ additional_user_labels` |  `array|Google\Protobuf\Internal\MapField`   
Additional user labels to be specified for the job. Keys and values must follow the restrictions specified in the [labeling restrictions](https://cloud.google.com/compute/docs/labeling-resources#restrictions) page. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1kg", "count": "3" }.  
`↳ kms_key_name` |  `string`   
Name for the Cloud KMS key for the job. Key format is: projects/  
`↳ ip_configuration` |  `int`   
Configuration for VM IPs.  
`↳ worker_region` |  `string`   
The Compute Engine region (<https://cloud.google.com/compute/docs/regions-zones/regions-zones>) in which worker processing should occur, e.g. "us-west1". Mutually exclusive with worker_zone. If neither worker_region nor worker_zone is specified, default to the control plane's region.  
`↳ worker_zone` |  `string`   
The Compute Engine zone (<https://cloud.google.com/compute/docs/regions-zones/regions-zones>) in which worker processing should occur, e.g. "us-west1-a". Mutually exclusive with worker_region. If neither worker_region nor worker_zone is specified, a zone in the control plane's region is chosen based on available capacity. If both `worker_zone` and `zone` are set, `worker_zone` takes precedence.  
`↳ enable_streaming_engine` |  `bool`   
Whether to enable Streaming Engine for the job.  
`↳ flexrs_goal` |  `int`   
Set FlexRS goal for the job. <https://cloud.google.com/dataflow/docs/guides/flexrs>  
`↳ staging_location` |  `string`   
The Cloud Storage path for staging local files. Must be a valid Cloud Storage URL, beginning with `gs://`.  
`↳ sdk_container_image` |  `string`   
Docker registry location of container image to use for the 'worker harness. Default is the container for the version of the SDK. Note this field is only valid for portable pipelines.  
`↳ disk_size_gb` |  `int`   
Worker disk size, in gigabytes.  
`↳ autoscaling_algorithm` |  `int`   
The algorithm to use for autoscaling  
`↳ dump_heap_on_oom` |  `bool`   
If true, when processing time is spent almost entirely on garbage collection (GC), saves a heap dump before ending the thread or process. If false, ends the thread or process without saving a heap dump. Does not save a heap dump when the Java Virtual Machine (JVM) has an out of memory error during processing. The location of the heap file is either echoed back to the user, or the user is given the opportunity to download the heap file.  
`↳ save_heap_dumps_to_gcs_path` |  `string`   
Cloud Storage bucket (directory) to upload heap dumps to. Enabling this field implies that `dump_heap_on_oom` is set to true.  
`↳ launcher_machine_type` |  `string`   
The machine type to use for launching the job. The default is n1-standard-1.  
`↳ enable_launcher_vm_serial_port_logging` |  `bool`   
If true serial port logging will be enabled for the launcher VM.  
`↳ streaming_mode` |  `int`   
Optional. Specifies the Streaming Engine message processing guarantees. Reduces cost and latency but might result in duplicate messages committed to storage. Designed to run simple mapping streaming ETL jobs at the lowest cost. For example, Change Data Capture (CDC) to BigQuery is a canonical use case. For more information, see [Set the pipeline streaming mode](https://cloud.google.com/dataflow/docs/guides/streaming-modes).  
`↳ additional_pipeline_options` |  `string[]`   
Optional. Additional pipeline option flags for the job.  
  
### getNumWorkers

The initial number of Google Compute Engine instances for the job.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setNumWorkers

The initial number of Google Compute Engine instances for the job.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMaxWorkers

The maximum number of Google Compute Engine instances to be made available to your pipeline during execution, from 1 to 1000.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setMaxWorkers

The maximum number of Google Compute Engine instances to be made available to your pipeline during execution, from 1 to 1000.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getZone

The Compute Engine [availability zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones) for launching worker instances to run your pipeline.

In the future, worker_zone will take precedence.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setZone

The Compute Engine [availability zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones) for launching worker instances to run your pipeline.

In the future, worker_zone will take precedence.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getServiceAccountEmail

The email address of the service account to run the job as.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setServiceAccountEmail

The email address of the service account to run the job as.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTempLocation

The Cloud Storage path to use for temporary files.

Must be a valid Cloud Storage URL, beginning with `gs://`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setTempLocation

The Cloud Storage path to use for temporary files.

Must be a valid Cloud Storage URL, beginning with `gs://`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMachineType

The machine type to use for the job. Defaults to the value from the template if not specified.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setMachineType

The machine type to use for the job. Defaults to the value from the template if not specified.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAdditionalExperiments

Additional experiment flags for the job.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setAdditionalExperiments

Additional experiment flags for the job.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNetwork

Network to which VMs will be assigned. If empty or unspecified, the service will use the network "default".

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setNetwork

Network to which VMs will be assigned. If empty or unspecified, the service will use the network "default".

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSubnetwork

Subnetwork to which VMs will be assigned, if desired. You can specify a subnetwork using either a complete URL or an abbreviated path. Expected to be of the form "<https://www.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNETWORK>" or "regions/REGION/subnetworks/SUBNETWORK". If the subnetwork is located in a Shared VPC network, you must use the complete URL.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setSubnetwork

Subnetwork to which VMs will be assigned, if desired. You can specify a subnetwork using either a complete URL or an abbreviated path. Expected to be of the form "<https://www.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNETWORK>" or "regions/REGION/subnetworks/SUBNETWORK". If the subnetwork is located in a Shared VPC network, you must use the complete URL.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAdditionalUserLabels

Additional user labels to be specified for the job.

Keys and values must follow the restrictions specified in the [labeling restrictions](https://cloud.google.com/compute/docs/labeling-resources#restrictions) page. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1kg", "count": "3" }.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Internal\MapField` |   
  
### setAdditionalUserLabels

Additional user labels to be specified for the job.

Keys and values must follow the restrictions specified in the [labeling restrictions](https://cloud.google.com/compute/docs/labeling-resources#restrictions) page. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1kg", "count": "3" }.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|Google\Protobuf\Internal\MapField`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getKmsKeyName

Name for the Cloud KMS key for the job.

Key format is: projects/

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setKmsKeyName

Name for the Cloud KMS key for the job.

Key format is: projects/

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getIpConfiguration

Configuration for VM IPs.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [WorkerIPAddressConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.WorkerIPAddressConfiguration).  
  
### setIpConfiguration

Configuration for VM IPs.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [WorkerIPAddressConfiguration](https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.WorkerIPAddressConfiguration).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getWorkerRegion

The Compute Engine region (<https://cloud.google.com/compute/docs/regions-zones/regions-zones>) in which worker processing should occur, e.g. "us-west1". Mutually exclusive with worker_zone. If neither worker_region nor worker_zone is specified, default to the control plane's region.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setWorkerRegion

The Compute Engine region (<https://cloud.google.com/compute/docs/regions-zones/regions-zones>) in which worker processing should occur, e.g. "us-west1". Mutually exclusive with worker_zone. If neither worker_region nor worker_zone is specified, default to the control plane's region.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getWorkerZone

The Compute Engine zone (<https://cloud.google.com/compute/docs/regions-zones/regions-zones>) in which worker processing should occur, e.g. "us-west1-a". Mutually exclusive with worker_region. If neither worker_region nor worker_zone is specified, a zone in the control plane's region is chosen based on available capacity.

If both `worker_zone` and `zone` are set, `worker_zone` takes precedence.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setWorkerZone

The Compute Engine zone (<https://cloud.google.com/compute/docs/regions-zones/regions-zones>) in which worker processing should occur, e.g. "us-west1-a". Mutually exclusive with worker_region. If neither worker_region nor worker_zone is specified, a zone in the control plane's region is chosen based on available capacity.

If both `worker_zone` and `zone` are set, `worker_zone` takes precedence.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEnableStreamingEngine

Whether to enable Streaming Engine for the job.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setEnableStreamingEngine

Whether to enable Streaming Engine for the job.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFlexrsGoal

Set FlexRS goal for the job.

<https://cloud.google.com/dataflow/docs/guides/flexrs>

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [FlexResourceSchedulingGoal](https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.FlexResourceSchedulingGoal).  
  
### setFlexrsGoal

Set FlexRS goal for the job.

<https://cloud.google.com/dataflow/docs/guides/flexrs>

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [FlexResourceSchedulingGoal](https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.FlexResourceSchedulingGoal).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStagingLocation

The Cloud Storage path for staging local files.

Must be a valid Cloud Storage URL, beginning with `gs://`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setStagingLocation

The Cloud Storage path for staging local files.

Must be a valid Cloud Storage URL, beginning with `gs://`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSdkContainerImage

Docker registry location of container image to use for the 'worker harness.

Default is the container for the version of the SDK. Note this field is only valid for portable pipelines.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setSdkContainerImage

Docker registry location of container image to use for the 'worker harness.

Default is the container for the version of the SDK. Note this field is only valid for portable pipelines.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDiskSizeGb

Worker disk size, in gigabytes.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setDiskSizeGb

Worker disk size, in gigabytes.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAutoscalingAlgorithm

The algorithm to use for autoscaling

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [AutoscalingAlgorithm](https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.AutoscalingAlgorithm).  
  
### setAutoscalingAlgorithm

The algorithm to use for autoscaling

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [AutoscalingAlgorithm](https://docs.cloud.google.com/php/docs/reference/cloud-dataflow/latest/V1beta3.AutoscalingAlgorithm).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDumpHeapOnOom

If true, when processing time is spent almost entirely on garbage collection (GC), saves a heap dump before ending the thread or process. If false, ends the thread or process without saving a heap dump. Does not save a heap dump when the Java Virtual Machine (JVM) has an out of memory error during processing. The location of the heap file is either echoed back to the user, or the user is given the opportunity to download the heap file.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setDumpHeapOnOom

If true, when processing time is spent almost entirely on garbage collection (GC), saves a heap dump before ending the thread or process. If false, ends the thread or process without saving a heap dump. Does not save a heap dump when the Java Virtual Machine (JVM) has an out of memory error during processing. The location of the heap file is either echoed back to the user, or the user is given the opportunity to download the heap file.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSaveHeapDumpsToGcsPath

Cloud Storage bucket (directory) to upload heap dumps to.

Enabling this field implies that `dump_heap_on_oom` is set to true.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setSaveHeapDumpsToGcsPath

Cloud Storage bucket (directory) to upload heap dumps to.

Enabling this field implies that `dump_heap_on_oom` is set to true.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLauncherMachineType

The machine type to use for launching the job. The default is n1-standard-1.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setLauncherMachineType

The machine type to use for launching the job. The default is n1-standard-1.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEnableLauncherVmSerialPortLogging

If true serial port logging will be enabled for the launcher VM.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setEnableLauncherVmSerialPortLogging

If true serial port logging will be enabled for the launcher VM.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStreamingMode

Optional. Specifies the Streaming Engine message processing guarantees.

Reduces cost and latency but might result in duplicate messages committed to storage. Designed to run simple mapping streaming ETL jobs at the lowest cost. For example, Change Data Capture (CDC) to BigQuery is a canonical use case. For more information, see [Set the pipeline streaming mode](https://cloud.google.com/dataflow/docs/guides/streaming-modes).

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### hasStreamingMode

### clearStreamingMode

### setStreamingMode

Optional. Specifies the Streaming Engine message processing guarantees.

Reduces cost and latency but might result in duplicate messages committed to storage. Designed to run simple mapping streaming ETL jobs at the lowest cost. For example, Change Data Capture (CDC) to BigQuery is a canonical use case. For more information, see [Set the pipeline streaming mode](https://cloud.google.com/dataflow/docs/guides/streaming-modes).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAdditionalPipelineOptions

Optional. Additional pipeline option flags for the job.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setAdditionalPipelineOptions

Optional. Additional pipeline option flags for the job.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
