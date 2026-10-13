---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-WaitOperationRequest/
title: Cloud Spanner Database Admin V1 API - Class Google::Longrunning::WaitOperationRequest (v1.14.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:07.033579+00:00
---

# Cloud Spanner Database Admin V1 API - Class Google::Longrunning::WaitOperationRequest (v1.14.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-WaitOperationRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Spanner Database Admin V1 API - Class Google::Longrunning::WaitOperationRequest (v1.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.1 (latest)  1.14.0  1.13.1  1.12.0  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.1  1.0.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.1  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.6 

Reference documentation and code samples for the Cloud Spanner Database Admin V1 API class Google::Longrunning::WaitOperationRequest.

The request message for Operations.WaitOperation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The name of the operation resource to wait on. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the operation resource to wait on. 



**Returns**

  * (::String) — The name of the operation resource to wait on. 



### #timeout
    
    
    def timeout() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Protobuf-Duration)) — The maximum duration to wait before timing out. If left blank, the wait will be at most the time permitted by the underlying HTTP/RPC protocol. If RPC context deadline is also specified, the shorter one will be used. 



### #timeout=
    
    
    def timeout=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Protobuf-Duration)) — The maximum duration to wait before timing out. If left blank, the wait will be at most the time permitted by the underlying HTTP/RPC protocol. If RPC context deadline is also specified, the shorter one will be used. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Protobuf-Duration)) — The maximum duration to wait before timing out. If left blank, the wait will be at most the time permitted by the underlying HTTP/RPC protocol. If RPC context deadline is also specified, the shorter one will be used. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
