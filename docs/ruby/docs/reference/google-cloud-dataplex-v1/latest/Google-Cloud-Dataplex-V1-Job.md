---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Job/
title: Dataplex V1 API - Class Google::Cloud::Dataplex::V1::Job (v2.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:56.130747+00:00
---

# Dataplex V1 API - Class Google::Cloud::Dataplex::V1::Job (v2.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataplex V1 API - Class Google::Cloud::Dataplex::V1::Job (v2.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.1 (latest)  2.10.0  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.2  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.1  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataplex V1 API class Google::Cloud::Dataplex::V1::Job.

A job represents an instance of a task.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #end_time
    
    
    def end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the job ended. 



### #execution_spec
    
    
    def execution_spec() -> ::Google::Cloud::Dataplex::V1::Task::ExecutionSpec

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Task::ExecutionSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Task-ExecutionSpec)) — Output only. Spec related to how a task is executed. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Output only. User-defined labels for the task. 



### #message
    
    
    def message() -> ::String

**Returns**

  * (::String) — Output only. Additional information about the current state. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The relative resource name of the job, of the form: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{task_id}/jobs/{job_id}`. 



### #retry_count
    
    
    def retry_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The number of times the job has been retried (excluding the initial attempt). 



### #service
    
    
    def service() -> ::Google::Cloud::Dataplex::V1::Job::Service

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Job::Service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Job-Service)) — Output only. The underlying service running a job. 



### #service_job
    
    
    def service_job() -> ::String

**Returns**

  * (::String) — Output only. The full resource name for the job run under a particular service. 



### #start_time
    
    
    def start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the job was started. 



### #state
    
    
    def state() -> ::Google::Cloud::Dataplex::V1::Job::State

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Job::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Job-State)) — Output only. Execution state for the job. 



### #trigger
    
    
    def trigger() -> ::Google::Cloud::Dataplex::V1::Job::Trigger

**Returns**

  * ([::Google::Cloud::Dataplex::V1::Job::Trigger](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-Job-Trigger)) — Output only. Job execution trigger. 



### #uid
    
    
    def uid() -> ::String

**Returns**

  * (::String) — Output only. System generated globally unique ID for the job. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
