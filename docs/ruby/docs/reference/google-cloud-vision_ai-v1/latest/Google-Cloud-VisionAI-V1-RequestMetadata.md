---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-RequestMetadata/
title: Vision AI V1 API - Class Google::Cloud::VisionAI::V1::RequestMetadata (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:00.409974+00:00
---

# Vision AI V1 API - Class Google::Cloud::VisionAI::V1::RequestMetadata (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-RequestMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vision AI V1 API - Class Google::Cloud::VisionAI::V1::RequestMetadata (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.1  1.2.0  1.1.1  1.0.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vision AI V1 API class Google::Cloud::VisionAI::V1::RequestMetadata.

RequestMetadata is the metadata message for the request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #event
    
    
    def event() -> ::String

**Returns**

  * (::String) — Evevt name. 



### #event=
    
    
    def event=(value) -> ::String

**Parameter**

  * **value** (::String) — Evevt name. 



**Returns**

  * (::String) — Evevt name. 



### #lease_id
    
    
    def lease_id() -> ::String

**Returns**

  * (::String) — Lease id. 



### #lease_id=
    
    
    def lease_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Lease id. 



**Returns**

  * (::String) — Lease id. 



### #lease_term
    
    
    def lease_term() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Protobuf-Duration)) — Lease term specifies how long the client wants the session to be maintained by the server after the client leaves. If the lease term is not set, the server will release the session immediately and the client cannot reconnect to the same session later. 



### #lease_term=
    
    
    def lease_term=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Protobuf-Duration)) — Lease term specifies how long the client wants the session to be maintained by the server after the client leaves. If the lease term is not set, the server will release the session immediately and the client cannot reconnect to the same session later. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Protobuf-Duration)) — Lease term specifies how long the client wants the session to be maintained by the server after the client leaves. If the lease term is not set, the server will release the session immediately and the client cannot reconnect to the same session later. 



### #owner
    
    
    def owner() -> ::String

**Returns**

  * (::String) — Owner name. 



### #owner=
    
    
    def owner=(value) -> ::String

**Parameter**

  * **value** (::String) — Owner name. 



**Returns**

  * (::String) — Owner name. 



### #series
    
    
    def series() -> ::String

**Returns**

  * (::String) — Series name. 



### #series=
    
    
    def series=(value) -> ::String

**Parameter**

  * **value** (::String) — Series name. 



**Returns**

  * (::String) — Series name. 



### #stream
    
    
    def stream() -> ::String

**Returns**

  * (::String) — Stream name. 



### #stream=
    
    
    def stream=(value) -> ::String

**Parameter**

  * **value** (::String) — Stream name. 



**Returns**

  * (::String) — Stream name. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
