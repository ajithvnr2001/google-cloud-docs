---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-OperationMetadata/
title: Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::OperationMetadata (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:53.308577+00:00
---

# Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::OperationMetadata (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-OperationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::OperationMetadata (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.1  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Audit Manager V1 API class Google::Cloud::AuditManager::V1::OperationMetadata.

Metadata for the long-running operation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #api_version
    
    
    def api_version() -> ::String

**Returns**

  * (::String) — Output only. The API version used to start the operation. For example, `v1`. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time that the operation was created. 



### #end_time
    
    
    def end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time that the operation finished running. 



### #requested_cancellation
    
    
    def requested_cancellation() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Whether you requested that the operation be cancelled. Operations that were cancelled successfully have an [Operation.error](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_error_instance_ "Google::Longrunning::Operation#error \(method\)") value with a status code [Code.CANCELLED][google.rpc.Status.code.CANCELLED]. 



### #status_message
    
    
    def status_message() -> ::String

**Returns**

  * (::String) — Output only. A human-readable status of the operation, if any. 



### #target
    
    
    def target() -> ::String

**Returns**

  * (::String) — Output only. A server-defined resource path for the target of the operation. 



### #verb
    
    
    def verb() -> ::String

**Returns**

  * (::String) — Output only. The name of the verb that was executed by the operation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
