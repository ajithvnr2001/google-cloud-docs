---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-BackgroundJobLogEntry/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::BackgroundJobLogEntry (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:19.228061+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::BackgroundJobLogEntry (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-BackgroundJobLogEntry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::BackgroundJobLogEntry (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::BackgroundJobLogEntry.

Execution log of a background job.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #apply_job_details
    
    
    def apply_job_details() -> ::Google::Cloud::CloudDMS::V1::BackgroundJobLogEntry::ApplyJobDetails

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::BackgroundJobLogEntry::ApplyJobDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-BackgroundJobLogEntry-ApplyJobDetails)) — Output only. Apply job details.

Note: The following fields are mutually exclusive: `apply_job_details`, `seed_job_details`, `import_rules_job_details`, `convert_job_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #completion_comment
    
    
    def completion_comment() -> ::String

**Returns**

  * (::String) — Output only. Job completion comment, such as how many entities were seeded, how many warnings were found during conversion, and similar information. 



### #completion_state
    
    
    def completion_state() -> ::Google::Cloud::CloudDMS::V1::BackgroundJobLogEntry::JobCompletionState

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::BackgroundJobLogEntry::JobCompletionState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-BackgroundJobLogEntry-JobCompletionState)) — Output only. Job completion state, i.e. the final state after the job completed. 



### #convert_job_details
    
    
    def convert_job_details() -> ::Google::Cloud::CloudDMS::V1::BackgroundJobLogEntry::ConvertJobDetails

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::BackgroundJobLogEntry::ConvertJobDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-BackgroundJobLogEntry-ConvertJobDetails)) — Output only. Convert job details.

Note: The following fields are mutually exclusive: `convert_job_details`, `seed_job_details`, `import_rules_job_details`, `apply_job_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #finish_time
    
    
    def finish_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Timestamp)) — The timestamp when the background job was finished. 



### #finish_time=
    
    
    def finish_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Timestamp)) — The timestamp when the background job was finished. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Timestamp)) — The timestamp when the background job was finished. 



### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — The background job log entry ID. 



### #id=
    
    
    def id=(value) -> ::String

**Parameter**

  * **value** (::String) — The background job log entry ID. 



**Returns**

  * (::String) — The background job log entry ID. 



### #import_rules_job_details
    
    
    def import_rules_job_details() -> ::Google::Cloud::CloudDMS::V1::BackgroundJobLogEntry::ImportRulesJobDetails

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::BackgroundJobLogEntry::ImportRulesJobDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-BackgroundJobLogEntry-ImportRulesJobDetails)) — Output only. Import rules job details.

Note: The following fields are mutually exclusive: `import_rules_job_details`, `seed_job_details`, `convert_job_details`, `apply_job_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #job_type
    
    
    def job_type() -> ::Google::Cloud::CloudDMS::V1::BackgroundJobType

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::BackgroundJobType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-BackgroundJobType)) — The type of job that was executed. 



### #job_type=
    
    
    def job_type=(value) -> ::Google::Cloud::CloudDMS::V1::BackgroundJobType

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::BackgroundJobType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-BackgroundJobType)) — The type of job that was executed. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::BackgroundJobType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-BackgroundJobType)) — The type of job that was executed. 



### #request_autocommit
    
    
    def request_autocommit() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Whether the client requested the conversion workspace to be committed after a successful completion of the job. 



### #seed_job_details
    
    
    def seed_job_details() -> ::Google::Cloud::CloudDMS::V1::BackgroundJobLogEntry::SeedJobDetails

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::BackgroundJobLogEntry::SeedJobDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-BackgroundJobLogEntry-SeedJobDetails)) — Output only. Seed job details.

Note: The following fields are mutually exclusive: `seed_job_details`, `import_rules_job_details`, `convert_job_details`, `apply_job_details`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #start_time
    
    
    def start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Timestamp)) — The timestamp when the background job was started. 



### #start_time=
    
    
    def start_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Timestamp)) — The timestamp when the background job was started. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Timestamp)) — The timestamp when the background job was started. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
