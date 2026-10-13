---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-DeleteConnectionRequest/
title: Cloud Build V2 API - Class Google::Cloud::Build::V2::DeleteConnectionRequest (v0.14.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:15:00.542328+00:00
---

# Cloud Build V2 API - Class Google::Cloud::Build::V2::DeleteConnectionRequest (v0.14.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v2/latest/Google-Cloud-Build-V2-DeleteConnectionRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Build V2 API - Class Google::Cloud::Build::V2::DeleteConnectionRequest (v0.14.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.2 (latest)  0.14.1  0.13.0  0.12.1  0.11.0  0.10.0  0.9.1  0.8.0  0.7.2  0.6.0  0.5.2  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Build V2 API class Google::Cloud::Build::V2::DeleteConnectionRequest.

Message for deleting a Connection.

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

  * (::String) — The current etag of the connection. If an etag is provided and does not match the current etag of the connection, deletion will be blocked and an ABORTED error will be returned. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — The current etag of the connection. If an etag is provided and does not match the current etag of the connection, deletion will be blocked and an ABORTED error will be returned. 



**Returns**

  * (::String) — The current etag of the connection. If an etag is provided and does not match the current etag of the connection, deletion will be blocked and an ABORTED error will be returned. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The name of the Connection to delete. Format: `projects/*/locations/*/connections/*`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the Connection to delete. Format: `projects/*/locations/*/connections/*`. 



**Returns**

  * (::String) — Required. The name of the Connection to delete. Format: `projects/*/locations/*/connections/*`. 



### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — If set, validate the request, but do not actually post it. 



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If set, validate the request, but do not actually post it. 



**Returns**

  * (::Boolean) — If set, validate the request, but do not actually post it. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
