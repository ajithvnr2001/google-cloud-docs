---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-CreateJobRequest/
title: Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::CreateJobRequest (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:58.671371+00:00
---

# Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::CreateJobRequest (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-CreateJobRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::CreateJobRequest (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.0  0.15.0  0.14.1  0.13.1  0.12.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Dataflow V1beta3 API class Google::Cloud::Dataflow::V1beta3::CreateJobRequest.

Request to create a Cloud Dataflow job.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #job
    
    
    def job() -> ::Google::Cloud::Dataflow::V1beta3::Job

**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-Job)) — The job to create. 



### #job=
    
    
    def job=(value) -> ::Google::Cloud::Dataflow::V1beta3::Job

**Parameter**

  * **value** ([::Google::Cloud::Dataflow::V1beta3::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-Job)) — The job to create. 



**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-Job)) — The job to create. 



### #location
    
    
    def location() -> ::String

**Returns**

  * (::String) — The [regional endpoint](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job. 



### #location=
    
    
    def location=(value) -> ::String

**Parameter**

  * **value** (::String) — The [regional endpoint](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job. 



**Returns**

  * (::String) — The [regional endpoint](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job. 



### #project_id
    
    
    def project_id() -> ::String

**Returns**

  * (::String) — The ID of the Cloud Platform project that the job belongs to. 



### #project_id=
    
    
    def project_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The ID of the Cloud Platform project that the job belongs to. 



**Returns**

  * (::String) — The ID of the Cloud Platform project that the job belongs to. 



### #replace_job_id
    
    
    def replace_job_id() -> ::String

**Returns**

  * (::String) — Deprecated. This field is now in the Job message. 



### #replace_job_id=
    
    
    def replace_job_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Deprecated. This field is now in the Job message. 



**Returns**

  * (::String) — Deprecated. This field is now in the Job message. 



### #view
    
    
    def view() -> ::Google::Cloud::Dataflow::V1beta3::JobView

**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::JobView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-JobView)) — The level of information requested in response. 



### #view=
    
    
    def view=(value) -> ::Google::Cloud::Dataflow::V1beta3::JobView

**Parameter**

  * **value** ([::Google::Cloud::Dataflow::V1beta3::JobView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-JobView)) — The level of information requested in response. 



**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::JobView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-JobView)) — The level of information requested in response. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
