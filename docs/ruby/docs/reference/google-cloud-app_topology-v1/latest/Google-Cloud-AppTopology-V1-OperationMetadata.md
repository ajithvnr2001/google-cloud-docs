---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-OperationMetadata/
title: App Topology V1 API - Class Google::Cloud::AppTopology::V1::OperationMetadata (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:18.303835+00:00
---

# App Topology V1 API - Class Google::Cloud::AppTopology::V1::OperationMetadata (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Cloud-AppTopology-V1-OperationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Topology V1 API - Class Google::Cloud::AppTopology::V1::OperationMetadata (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the App Topology V1 API class Google::Cloud::AppTopology::V1::OperationMetadata.

Represents the metadata of the long-running operation.

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

  * (::String) — Output only. API version used to start the operation. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time the operation was created. 



### #end_time
    
    
    def end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_topology-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time the operation finished running. 



### #requested_cancellation
    
    
    def requested_cancellation() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Identifies whether the user has requested cancellation of the operation. Operations that have been cancelled successfully have [google.longrunning.Operation.error][google.longrunning.Operation.error] value with a [google.rpc.Status.code][google.rpc.Status.code] of `1`, corresponding to `Code.CANCELLED`. 



### #status_message
    
    
    def status_message() -> ::String

**Returns**

  * (::String) — Output only. Human-readable status of the operation, if any. 



### #target
    
    
    def target() -> ::String

**Returns**

  * (::String) — Output only. Server-defined resource path for the target of the operation. 



### #verb
    
    
    def verb() -> ::String

**Returns**

  * (::String) — Output only. Name of the verb executed by the operation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
