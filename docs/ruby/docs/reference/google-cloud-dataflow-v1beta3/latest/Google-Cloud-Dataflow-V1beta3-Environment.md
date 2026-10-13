---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-Environment/
title: Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::Environment (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:00.757860+00:00
---

# Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::Environment (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-Environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::Environment (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.0  0.15.0  0.14.1  0.13.1  0.12.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Dataflow V1beta3 API class Google::Cloud::Dataflow::V1beta3::Environment.

Describes the environment in which a Dataflow Job runs.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cluster_manager_api_service
    
    
    def cluster_manager_api_service() -> ::String

**Returns**

  * (::String) — The type of cluster manager API to use. If unknown or unspecified, the service will attempt to choose a reasonable default. This should be in the form of the API service name, e.g. "compute.googleapis.com". 



### #cluster_manager_api_service=
    
    
    def cluster_manager_api_service=(value) -> ::String

**Parameter**

  * **value** (::String) — The type of cluster manager API to use. If unknown or unspecified, the service will attempt to choose a reasonable default. This should be in the form of the API service name, e.g. "compute.googleapis.com". 



**Returns**

  * (::String) — The type of cluster manager API to use. If unknown or unspecified, the service will attempt to choose a reasonable default. This should be in the form of the API service name, e.g. "compute.googleapis.com". 



### #dataset
    
    
    def dataset() -> ::String

**Returns**

  * (::String) — Optional. The dataset for the current project where various workflow related tables are stored.

The supported resource type is:

Google BigQuery: bigquery.googleapis.com/{dataset} 




### #dataset=
    
    
    def dataset=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The dataset for the current project where various workflow related tables are stored.

The supported resource type is:

Google BigQuery: bigquery.googleapis.com/{dataset} 




**Returns**

  * (::String) — Optional. The dataset for the current project where various workflow related tables are stored.

The supported resource type is:

Google BigQuery: bigquery.googleapis.com/{dataset} 




### #debug_options
    
    
    def debug_options() -> ::Google::Cloud::Dataflow::V1beta3::DebugOptions

**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::DebugOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-DebugOptions)) — Optional. Any debugging options to be supplied to the job. 



### #debug_options=
    
    
    def debug_options=(value) -> ::Google::Cloud::Dataflow::V1beta3::DebugOptions

**Parameter**

  * **value** ([::Google::Cloud::Dataflow::V1beta3::DebugOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-DebugOptions)) — Optional. Any debugging options to be supplied to the job. 



**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::DebugOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-DebugOptions)) — Optional. Any debugging options to be supplied to the job. 



### #experiments
    
    
    def experiments() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The list of experiments to enable. This field should be used for SDK related experiments and not for service related experiments. The proper field for service related experiments is service_options. 



### #experiments=
    
    
    def experiments=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The list of experiments to enable. This field should be used for SDK related experiments and not for service related experiments. The proper field for service related experiments is service_options. 



**Returns**

  * (::Array<::String>) — The list of experiments to enable. This field should be used for SDK related experiments and not for service related experiments. The proper field for service related experiments is service_options. 



### #flex_resource_scheduling_goal
    
    
    def flex_resource_scheduling_goal() -> ::Google::Cloud::Dataflow::V1beta3::FlexResourceSchedulingGoal

**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::FlexResourceSchedulingGoal](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexResourceSchedulingGoal)) — Optional. Which Flexible Resource Scheduling mode to run in. 



### #flex_resource_scheduling_goal=
    
    
    def flex_resource_scheduling_goal=(value) -> ::Google::Cloud::Dataflow::V1beta3::FlexResourceSchedulingGoal

**Parameter**

  * **value** ([::Google::Cloud::Dataflow::V1beta3::FlexResourceSchedulingGoal](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexResourceSchedulingGoal)) — Optional. Which Flexible Resource Scheduling mode to run in. 



**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::FlexResourceSchedulingGoal](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexResourceSchedulingGoal)) — Optional. Which Flexible Resource Scheduling mode to run in. 



### #internal_experiments
    
    
    def internal_experiments() -> ::Google::Protobuf::Any

**Returns**

  * ([::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Any)) — Experimental settings. 



### #internal_experiments=
    
    
    def internal_experiments=(value) -> ::Google::Protobuf::Any

**Parameter**

  * **value** ([::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Any)) — Experimental settings. 



**Returns**

  * ([::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Any)) — Experimental settings. 



### #sdk_pipeline_options
    
    
    def sdk_pipeline_options() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Struct)) — The Cloud Dataflow SDK pipeline options specified by the user. These options are passed through the service and are used to recreate the SDK pipeline options on the worker in a language agnostic and platform independent way. 



### #sdk_pipeline_options=
    
    
    def sdk_pipeline_options=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Struct)) — The Cloud Dataflow SDK pipeline options specified by the user. These options are passed through the service and are used to recreate the SDK pipeline options on the worker in a language agnostic and platform independent way. 



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Struct)) — The Cloud Dataflow SDK pipeline options specified by the user. These options are passed through the service and are used to recreate the SDK pipeline options on the worker in a language agnostic and platform independent way. 



### #service_account_email
    
    
    def service_account_email() -> ::String

**Returns**

  * (::String) — Optional. Identity to run virtual machines as. Defaults to the default account. 



### #service_account_email=
    
    
    def service_account_email=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Identity to run virtual machines as. Defaults to the default account. 



**Returns**

  * (::String) — Optional. Identity to run virtual machines as. Defaults to the default account. 



### #service_kms_key_name
    
    
    def service_kms_key_name() -> ::String

**Returns**

  * (::String) — Optional. If set, contains the Cloud KMS key identifier used to encrypt data at rest, AKA a Customer Managed Encryption Key (CMEK).

Format: projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY 




### #service_kms_key_name=
    
    
    def service_kms_key_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. If set, contains the Cloud KMS key identifier used to encrypt data at rest, AKA a Customer Managed Encryption Key (CMEK).

Format: projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY 




**Returns**

  * (::String) — Optional. If set, contains the Cloud KMS key identifier used to encrypt data at rest, AKA a Customer Managed Encryption Key (CMEK).

Format: projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY 




### #service_options
    
    
    def service_options() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. The list of service options to enable. This field should be used for service related experiments only. These experiments, when graduating to GA, should be replaced by dedicated fields or become default (i.e. always on). 



### #service_options=
    
    
    def service_options=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. The list of service options to enable. This field should be used for service related experiments only. These experiments, when graduating to GA, should be replaced by dedicated fields or become default (i.e. always on). 



**Returns**

  * (::Array<::String>) — Optional. The list of service options to enable. This field should be used for service related experiments only. These experiments, when graduating to GA, should be replaced by dedicated fields or become default (i.e. always on). 



### #shuffle_mode
    
    
    def shuffle_mode() -> ::Google::Cloud::Dataflow::V1beta3::ShuffleMode

**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::ShuffleMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-ShuffleMode)) — Output only. The shuffle mode used for the job. 



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



### #temp_storage_prefix
    
    
    def temp_storage_prefix() -> ::String

**Returns**

  * (::String) — The prefix of the resources the system should use for temporary storage. The system will append the suffix "/temp-{JOBNAME} to this resource prefix, where {JOBNAME} is the value of the job_name field. The resulting bucket and object prefix is used as the prefix of the resources used to store temporary data needed during the job execution. NOTE: This will override the value in taskrunner_settings. The supported resource type is:

Google Cloud Storage:

storage.googleapis.com/{bucket}/{object} bucket.storage.googleapis.com/{object} 




### #temp_storage_prefix=
    
    
    def temp_storage_prefix=(value) -> ::String

**Parameter**

  * **value** (::String) — The prefix of the resources the system should use for temporary storage. The system will append the suffix "/temp-{JOBNAME} to this resource prefix, where {JOBNAME} is the value of the job_name field. The resulting bucket and object prefix is used as the prefix of the resources used to store temporary data needed during the job execution. NOTE: This will override the value in taskrunner_settings. The supported resource type is:

Google Cloud Storage:

storage.googleapis.com/{bucket}/{object} bucket.storage.googleapis.com/{object} 




**Returns**

  * (::String) — The prefix of the resources the system should use for temporary storage. The system will append the suffix "/temp-{JOBNAME} to this resource prefix, where {JOBNAME} is the value of the job_name field. The resulting bucket and object prefix is used as the prefix of the resources used to store temporary data needed during the job execution. NOTE: This will override the value in taskrunner_settings. The supported resource type is:

Google Cloud Storage:

storage.googleapis.com/{bucket}/{object} bucket.storage.googleapis.com/{object} 




### #use_public_ips
    
    
    def use_public_ips() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. True when any worker pool that uses public IPs is present. 



### #use_public_ips=
    
    
    def use_public_ips=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. True when any worker pool that uses public IPs is present. 



**Returns**

  * (::Boolean) — Optional. True when any worker pool that uses public IPs is present. 



### #use_streaming_engine_resource_based_billing
    
    
    def use_streaming_engine_resource_based_billing() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Whether the job uses the Streaming Engine resource-based billing model. 



### #user_agent
    
    
    def user_agent() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Struct)) — Optional. A description of the process that generated the request. 



### #user_agent=
    
    
    def user_agent=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Struct)) — Optional. A description of the process that generated the request. 



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Struct)) — Optional. A description of the process that generated the request. 



### #version
    
    
    def version() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Struct)) — A structure describing which components and their versions of the service are required in order to run the job. 



### #version=
    
    
    def version=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Struct)) — A structure describing which components and their versions of the service are required in order to run the job. 



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Struct)) — A structure describing which components and their versions of the service are required in order to run the job. 



### #worker_pools
    
    
    def worker_pools() -> ::Array<::Google::Cloud::Dataflow::V1beta3::WorkerPool>

**Returns**

  * (::Array<[::Google::Cloud::Dataflow::V1beta3::WorkerPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-WorkerPool)>) — The worker pools. At least one "harness" worker pool must be specified in order for the job to have workers. 



### #worker_pools=
    
    
    def worker_pools=(value) -> ::Array<::Google::Cloud::Dataflow::V1beta3::WorkerPool>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dataflow::V1beta3::WorkerPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-WorkerPool)>) — The worker pools. At least one "harness" worker pool must be specified in order for the job to have workers. 



**Returns**

  * (::Array<[::Google::Cloud::Dataflow::V1beta3::WorkerPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-WorkerPool)>) — The worker pools. At least one "harness" worker pool must be specified in order for the job to have workers. 



### #worker_region
    
    
    def worker_region() -> ::String

**Returns**

  * (::String) — Optional. The Compute Engine region (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. "us-west1". Mutually exclusive with worker_zone. If neither worker_region nor worker_zone is specified, default to the control plane's region. 



### #worker_region=
    
    
    def worker_region=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The Compute Engine region (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. "us-west1". Mutually exclusive with worker_zone. If neither worker_region nor worker_zone is specified, default to the control plane's region. 



**Returns**

  * (::String) — Optional. The Compute Engine region (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. "us-west1". Mutually exclusive with worker_zone. If neither worker_region nor worker_zone is specified, default to the control plane's region. 



### #worker_zone
    
    
    def worker_zone() -> ::String

**Returns**

  * (::String) — Optional. The Compute Engine zone (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. "us-west1-a". Mutually exclusive with worker_region. If neither worker_region nor worker_zone is specified, a zone in the control plane's region is chosen based on available capacity. 



### #worker_zone=
    
    
    def worker_zone=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The Compute Engine zone (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. "us-west1-a". Mutually exclusive with worker_region. If neither worker_region nor worker_zone is specified, a zone in the control plane's region is chosen based on available capacity. 



**Returns**

  * (::String) — Optional. The Compute Engine zone (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. "us-west1-a". Mutually exclusive with worker_region. If neither worker_region nor worker_zone is specified, a zone in the control plane's region is chosen based on available capacity. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
