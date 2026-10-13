---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexTemplateRuntimeEnvironment/
title: Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::FlexTemplateRuntimeEnvironment (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:02.441977+00:00
---

# Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::FlexTemplateRuntimeEnvironment (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexTemplateRuntimeEnvironment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::FlexTemplateRuntimeEnvironment (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.0  0.15.0  0.14.1  0.13.1  0.12.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Dataflow V1beta3 API class Google::Cloud::Dataflow::V1beta3::FlexTemplateRuntimeEnvironment.

The environment values to be set at runtime for flex template.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #additional_experiments
    
    
    def additional_experiments() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Additional experiment flags for the job. 



### #additional_experiments=
    
    
    def additional_experiments=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Additional experiment flags for the job. 



**Returns**

  * (::Array<::String>) — Additional experiment flags for the job. 



### #additional_pipeline_options
    
    
    def additional_pipeline_options() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. Additional pipeline option flags for the job. 



### #additional_pipeline_options=
    
    
    def additional_pipeline_options=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. Additional pipeline option flags for the job. 



**Returns**

  * (::Array<::String>) — Optional. Additional pipeline option flags for the job. 



### #additional_user_labels
    
    
    def additional_user_labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Additional user labels to be specified for the job. Keys and values must follow the restrictions specified in the [labeling restrictions](https://cloud.google.com/compute/docs/labeling-resources#restrictions) page. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1kg", "count": "3" }. 



### #additional_user_labels=
    
    
    def additional_user_labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Additional user labels to be specified for the job. Keys and values must follow the restrictions specified in the [labeling restrictions](https://cloud.google.com/compute/docs/labeling-resources#restrictions) page. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1kg", "count": "3" }. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Additional user labels to be specified for the job. Keys and values must follow the restrictions specified in the [labeling restrictions](https://cloud.google.com/compute/docs/labeling-resources#restrictions) page. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1kg", "count": "3" }. 



### #autoscaling_algorithm
    
    
    def autoscaling_algorithm() -> ::Google::Cloud::Dataflow::V1beta3::AutoscalingAlgorithm

**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::AutoscalingAlgorithm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-AutoscalingAlgorithm)) — The algorithm to use for autoscaling 



### #autoscaling_algorithm=
    
    
    def autoscaling_algorithm=(value) -> ::Google::Cloud::Dataflow::V1beta3::AutoscalingAlgorithm

**Parameter**

  * **value** ([::Google::Cloud::Dataflow::V1beta3::AutoscalingAlgorithm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-AutoscalingAlgorithm)) — The algorithm to use for autoscaling 



**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::AutoscalingAlgorithm](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-AutoscalingAlgorithm)) — The algorithm to use for autoscaling 



### #disk_size_gb
    
    
    def disk_size_gb() -> ::Integer

**Returns**

  * (::Integer) — Worker disk size, in gigabytes. 



### #disk_size_gb=
    
    
    def disk_size_gb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Worker disk size, in gigabytes. 



**Returns**

  * (::Integer) — Worker disk size, in gigabytes. 



### #dump_heap_on_oom
    
    
    def dump_heap_on_oom() -> ::Boolean

**Returns**

  * (::Boolean) — If true, when processing time is spent almost entirely on garbage collection (GC), saves a heap dump before ending the thread or process. If false, ends the thread or process without saving a heap dump. Does not save a heap dump when the Java Virtual Machine (JVM) has an out of memory error during processing. The location of the heap file is either echoed back to the user, or the user is given the opportunity to download the heap file. 



### #dump_heap_on_oom=
    
    
    def dump_heap_on_oom=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If true, when processing time is spent almost entirely on garbage collection (GC), saves a heap dump before ending the thread or process. If false, ends the thread or process without saving a heap dump. Does not save a heap dump when the Java Virtual Machine (JVM) has an out of memory error during processing. The location of the heap file is either echoed back to the user, or the user is given the opportunity to download the heap file. 



**Returns**

  * (::Boolean) — If true, when processing time is spent almost entirely on garbage collection (GC), saves a heap dump before ending the thread or process. If false, ends the thread or process without saving a heap dump. Does not save a heap dump when the Java Virtual Machine (JVM) has an out of memory error during processing. The location of the heap file is either echoed back to the user, or the user is given the opportunity to download the heap file. 



### #enable_launcher_vm_serial_port_logging
    
    
    def enable_launcher_vm_serial_port_logging() -> ::Boolean

**Returns**

  * (::Boolean) — If true serial port logging will be enabled for the launcher VM. 



### #enable_launcher_vm_serial_port_logging=
    
    
    def enable_launcher_vm_serial_port_logging=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If true serial port logging will be enabled for the launcher VM. 



**Returns**

  * (::Boolean) — If true serial port logging will be enabled for the launcher VM. 



### #enable_streaming_engine
    
    
    def enable_streaming_engine() -> ::Boolean

**Returns**

  * (::Boolean) — Whether to enable Streaming Engine for the job. 



### #enable_streaming_engine=
    
    
    def enable_streaming_engine=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether to enable Streaming Engine for the job. 



**Returns**

  * (::Boolean) — Whether to enable Streaming Engine for the job. 



### #flexrs_goal
    
    
    def flexrs_goal() -> ::Google::Cloud::Dataflow::V1beta3::FlexResourceSchedulingGoal

**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::FlexResourceSchedulingGoal](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexResourceSchedulingGoal)) — Set FlexRS goal for the job. https://cloud.google.com/dataflow/docs/guides/flexrs 



### #flexrs_goal=
    
    
    def flexrs_goal=(value) -> ::Google::Cloud::Dataflow::V1beta3::FlexResourceSchedulingGoal

**Parameter**

  * **value** ([::Google::Cloud::Dataflow::V1beta3::FlexResourceSchedulingGoal](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexResourceSchedulingGoal)) — Set FlexRS goal for the job. https://cloud.google.com/dataflow/docs/guides/flexrs 



**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::FlexResourceSchedulingGoal](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexResourceSchedulingGoal)) — Set FlexRS goal for the job. https://cloud.google.com/dataflow/docs/guides/flexrs 



### #ip_configuration
    
    
    def ip_configuration() -> ::Google::Cloud::Dataflow::V1beta3::WorkerIPAddressConfiguration

**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::WorkerIPAddressConfiguration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-WorkerIPAddressConfiguration)) — Configuration for VM IPs. 



### #ip_configuration=
    
    
    def ip_configuration=(value) -> ::Google::Cloud::Dataflow::V1beta3::WorkerIPAddressConfiguration

**Parameter**

  * **value** ([::Google::Cloud::Dataflow::V1beta3::WorkerIPAddressConfiguration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-WorkerIPAddressConfiguration)) — Configuration for VM IPs. 



**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::WorkerIPAddressConfiguration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-WorkerIPAddressConfiguration)) — Configuration for VM IPs. 



### #kms_key_name
    
    
    def kms_key_name() -> ::String

**Returns**

  * (::String) — Name for the Cloud KMS key for the job. Key format is: projects/



### #kms_key_name=
    
    
    def kms_key_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Name for the Cloud KMS key for the job. Key format is: projects/



**Returns**

  * (::String) — Name for the Cloud KMS key for the job. Key format is: projects/



### #launcher_machine_type
    
    
    def launcher_machine_type() -> ::String

**Returns**

  * (::String) — The machine type to use for launching the job. The default is n1-standard-1. 



### #launcher_machine_type=
    
    
    def launcher_machine_type=(value) -> ::String

**Parameter**

  * **value** (::String) — The machine type to use for launching the job. The default is n1-standard-1. 



**Returns**

  * (::String) — The machine type to use for launching the job. The default is n1-standard-1. 



### #machine_type
    
    
    def machine_type() -> ::String

**Returns**

  * (::String) — The machine type to use for the job. Defaults to the value from the template if not specified. 



### #machine_type=
    
    
    def machine_type=(value) -> ::String

**Parameter**

  * **value** (::String) — The machine type to use for the job. Defaults to the value from the template if not specified. 



**Returns**

  * (::String) — The machine type to use for the job. Defaults to the value from the template if not specified. 



### #max_workers
    
    
    def max_workers() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of Google Compute Engine instances to be made available to your pipeline during execution, from 1 to 1000. 



### #max_workers=
    
    
    def max_workers=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of Google Compute Engine instances to be made available to your pipeline during execution, from 1 to 1000. 



**Returns**

  * (::Integer) — The maximum number of Google Compute Engine instances to be made available to your pipeline during execution, from 1 to 1000. 



### #network
    
    
    def network() -> ::String

**Returns**

  * (::String) — Network to which VMs will be assigned. If empty or unspecified, the service will use the network "default". 



### #network=
    
    
    def network=(value) -> ::String

**Parameter**

  * **value** (::String) — Network to which VMs will be assigned. If empty or unspecified, the service will use the network "default". 



**Returns**

  * (::String) — Network to which VMs will be assigned. If empty or unspecified, the service will use the network "default". 



### #num_workers
    
    
    def num_workers() -> ::Integer

**Returns**

  * (::Integer) — The initial number of Google Compute Engine instances for the job. 



### #num_workers=
    
    
    def num_workers=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The initial number of Google Compute Engine instances for the job. 



**Returns**

  * (::Integer) — The initial number of Google Compute Engine instances for the job. 



### #save_heap_dumps_to_gcs_path
    
    
    def save_heap_dumps_to_gcs_path() -> ::String

**Returns**

  * (::String) — Cloud Storage bucket (directory) to upload heap dumps to. Enabling this field implies that `dump_heap_on_oom` is set to true. 



### #save_heap_dumps_to_gcs_path=
    
    
    def save_heap_dumps_to_gcs_path=(value) -> ::String

**Parameter**

  * **value** (::String) — Cloud Storage bucket (directory) to upload heap dumps to. Enabling this field implies that `dump_heap_on_oom` is set to true. 



**Returns**

  * (::String) — Cloud Storage bucket (directory) to upload heap dumps to. Enabling this field implies that `dump_heap_on_oom` is set to true. 



### #sdk_container_image
    
    
    def sdk_container_image() -> ::String

**Returns**

  * (::String) — Docker registry location of container image to use for the 'worker harness. Default is the container for the version of the SDK. Note this field is only valid for portable pipelines. 



### #sdk_container_image=
    
    
    def sdk_container_image=(value) -> ::String

**Parameter**

  * **value** (::String) — Docker registry location of container image to use for the 'worker harness. Default is the container for the version of the SDK. Note this field is only valid for portable pipelines. 



**Returns**

  * (::String) — Docker registry location of container image to use for the 'worker harness. Default is the container for the version of the SDK. Note this field is only valid for portable pipelines. 



### #service_account_email
    
    
    def service_account_email() -> ::String

**Returns**

  * (::String) — The email address of the service account to run the job as. 



### #service_account_email=
    
    
    def service_account_email=(value) -> ::String

**Parameter**

  * **value** (::String) — The email address of the service account to run the job as. 



**Returns**

  * (::String) — The email address of the service account to run the job as. 



### #staging_location
    
    
    def staging_location() -> ::String

**Returns**

  * (::String) — The Cloud Storage path for staging local files. Must be a valid Cloud Storage URL, beginning with `gs://`. 



### #staging_location=
    
    
    def staging_location=(value) -> ::String

**Parameter**

  * **value** (::String) — The Cloud Storage path for staging local files. Must be a valid Cloud Storage URL, beginning with `gs://`. 



**Returns**

  * (::String) — The Cloud Storage path for staging local files. Must be a valid Cloud Storage URL, beginning with `gs://`. 



### #streaming_mode
    
    
    def streaming_mode() -> ::Google::Cloud::Dataflow::V1beta3::StreamingMode

**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::StreamingMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-StreamingMode)) — Optional. Specifies the Streaming Engine message processing guarantees. Reduces cost and latency but might result in duplicate messages committed to storage. Designed to run simple mapping streaming ETL jobs at the lowest cost. For example, Change Data Capture (CDC) to BigQuery is a canonical use case. For more information, see [Set the pipeline streaming mode](https://cloud.google.com/dataflow/docs/guides/streaming-modes). 



### #streaming_mode=
    
    
    def streaming_mode=(value) -> ::Google::Cloud::Dataflow::V1beta3::StreamingMode

**Parameter**

  * **value** ([::Google::Cloud::Dataflow::V1beta3::StreamingMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-StreamingMode)) — Optional. Specifies the Streaming Engine message processing guarantees. Reduces cost and latency but might result in duplicate messages committed to storage. Designed to run simple mapping streaming ETL jobs at the lowest cost. For example, Change Data Capture (CDC) to BigQuery is a canonical use case. For more information, see [Set the pipeline streaming mode](https://cloud.google.com/dataflow/docs/guides/streaming-modes). 



**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::StreamingMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-StreamingMode)) — Optional. Specifies the Streaming Engine message processing guarantees. Reduces cost and latency but might result in duplicate messages committed to storage. Designed to run simple mapping streaming ETL jobs at the lowest cost. For example, Change Data Capture (CDC) to BigQuery is a canonical use case. For more information, see [Set the pipeline streaming mode](https://cloud.google.com/dataflow/docs/guides/streaming-modes). 



### #subnetwork
    
    
    def subnetwork() -> ::String

**Returns**

  * (::String) — Subnetwork to which VMs will be assigned, if desired. You can specify a subnetwork using either a complete URL or an abbreviated path. Expected to be of the form "https://www.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNETWORK" or "regions/REGION/subnetworks/SUBNETWORK". If the subnetwork is located in a Shared VPC network, you must use the complete URL. 



### #subnetwork=
    
    
    def subnetwork=(value) -> ::String

**Parameter**

  * **value** (::String) — Subnetwork to which VMs will be assigned, if desired. You can specify a subnetwork using either a complete URL or an abbreviated path. Expected to be of the form "https://www.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNETWORK" or "regions/REGION/subnetworks/SUBNETWORK". If the subnetwork is located in a Shared VPC network, you must use the complete URL. 



**Returns**

  * (::String) — Subnetwork to which VMs will be assigned, if desired. You can specify a subnetwork using either a complete URL or an abbreviated path. Expected to be of the form "https://www.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNETWORK" or "regions/REGION/subnetworks/SUBNETWORK". If the subnetwork is located in a Shared VPC network, you must use the complete URL. 



### #temp_location
    
    
    def temp_location() -> ::String

**Returns**

  * (::String) — The Cloud Storage path to use for temporary files. Must be a valid Cloud Storage URL, beginning with `gs://`. 



### #temp_location=
    
    
    def temp_location=(value) -> ::String

**Parameter**

  * **value** (::String) — The Cloud Storage path to use for temporary files. Must be a valid Cloud Storage URL, beginning with `gs://`. 



**Returns**

  * (::String) — The Cloud Storage path to use for temporary files. Must be a valid Cloud Storage URL, beginning with `gs://`. 



### #worker_region
    
    
    def worker_region() -> ::String

**Returns**

  * (::String) — The Compute Engine region (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. "us-west1". Mutually exclusive with worker_zone. If neither worker_region nor worker_zone is specified, default to the control plane's region. 



### #worker_region=
    
    
    def worker_region=(value) -> ::String

**Parameter**

  * **value** (::String) — The Compute Engine region (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. "us-west1". Mutually exclusive with worker_zone. If neither worker_region nor worker_zone is specified, default to the control plane's region. 



**Returns**

  * (::String) — The Compute Engine region (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. "us-west1". Mutually exclusive with worker_zone. If neither worker_region nor worker_zone is specified, default to the control plane's region. 



### #worker_zone
    
    
    def worker_zone() -> ::String

**Returns**

  * (::String) — The Compute Engine zone (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. "us-west1-a". Mutually exclusive with worker_region. If neither worker_region nor worker_zone is specified, a zone in the control plane's region is chosen based on available capacity. If both `worker_zone` and `zone` are set, `worker_zone` takes precedence. 



### #worker_zone=
    
    
    def worker_zone=(value) -> ::String

**Parameter**

  * **value** (::String) — The Compute Engine zone (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. "us-west1-a". Mutually exclusive with worker_region. If neither worker_region nor worker_zone is specified, a zone in the control plane's region is chosen based on available capacity. If both `worker_zone` and `zone` are set, `worker_zone` takes precedence. 



**Returns**

  * (::String) — The Compute Engine zone (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. "us-west1-a". Mutually exclusive with worker_region. If neither worker_region nor worker_zone is specified, a zone in the control plane's region is chosen based on available capacity. If both `worker_zone` and `zone` are set, `worker_zone` takes precedence. 



### #zone
    
    
    def zone() -> ::String

**Returns**

  * (::String) — The Compute Engine [availability zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones) for launching worker instances to run your pipeline. In the future, worker_zone will take precedence. 



### #zone=
    
    
    def zone=(value) -> ::String

**Parameter**

  * **value** (::String) — The Compute Engine [availability zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones) for launching worker instances to run your pipeline. In the future, worker_zone will take precedence. 



**Returns**

  * (::String) — The Compute Engine [availability zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones) for launching worker instances to run your pipeline. In the future, worker_zone will take precedence. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
