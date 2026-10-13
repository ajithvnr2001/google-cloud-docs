---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-DeleteExecutionRequest/
title: Cloud Run V2 API - Class Google::Cloud::Run::V2::DeleteExecutionRequest (v0.29.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:16.188165+00:00
---

# Cloud Run V2 API - Class Google::Cloud::Run::V2::DeleteExecutionRequest (v0.29.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-DeleteExecutionRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Run V2 API - Class Google::Cloud::Run::V2::DeleteExecutionRequest (v0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.1  0.23.0  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.2  0.12.0  0.11.0  0.10.1  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Run V2 API class Google::Cloud::Run::V2::DeleteExecutionRequest.

Request message for deleting an Execution.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — A system-generated fingerprint for this version of the resource. This may be used to detect modification conflict during updates. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — A system-generated fingerprint for this version of the resource. This may be used to detect modification conflict during updates. 



**Returns**

  * (::String) — A system-generated fingerprint for this version of the resource. This may be used to detect modification conflict during updates. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The name of the Execution to delete. Format: `projects/{project}/locations/{location}/jobs/{job}/executions/{execution}`, where `{project}` can be project id or number. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the Execution to delete. Format: `projects/{project}/locations/{location}/jobs/{job}/executions/{execution}`, where `{project}` can be project id or number. 



**Returns**

  * (::String) — Required. The name of the Execution to delete. Format: `projects/{project}/locations/{location}/jobs/{job}/executions/{execution}`, where `{project}` can be project id or number. 



### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — Indicates that the request should be validated without actually deleting any resources. 



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Indicates that the request should be validated without actually deleting any resources. 



**Returns**

  * (::Boolean) — Indicates that the request should be validated without actually deleting any resources. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
