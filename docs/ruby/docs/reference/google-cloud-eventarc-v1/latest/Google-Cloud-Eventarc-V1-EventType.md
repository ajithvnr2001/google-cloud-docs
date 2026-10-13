---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Cloud-Eventarc-V1-EventType/
title: Eventarc V1 API - Class Google::Cloud::Eventarc::V1::EventType (v2.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:44.148571+00:00
---

# Eventarc V1 API - Class Google::Cloud::Eventarc::V1::EventType (v2.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Cloud-Eventarc-V1-EventType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Eventarc V1 API - Class Google::Cloud::Eventarc::V1::EventType (v2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.0 (latest)  2.7.1  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.4 

Reference documentation and code samples for the Eventarc V1 API class Google::Cloud::Eventarc::V1::EventType.

A representation of the event type resource.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Output only. Human friendly description of what the event type is about. For example "Bucket created in Cloud Storage". 



### #event_schema_uri
    
    
    def event_schema_uri() -> ::String

**Returns**

  * (::String) — Output only. URI for the event schema. For example "https://github.com/googleapis/google-cloudevents/blob/master/proto/google/events/cloud/storage/v1/events.proto" 



### #filtering_attributes
    
    
    def filtering_attributes() -> ::Array<::Google::Cloud::Eventarc::V1::FilteringAttribute>

**Returns**

  * (::Array<[::Google::Cloud::Eventarc::V1::FilteringAttribute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-eventarc-v1/latest/Google-Cloud-Eventarc-V1-FilteringAttribute)>) — Output only. Filtering attributes for the event type. 



### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — Output only. The full name of the event type (for example, "google.cloud.storage.object.v1.finalized"). In the form of {provider-specific-prefix}.{resource}.{version}.{verb}. Types MUST be versioned and event schemas are guaranteed to remain backward compatible within one version. Note that event type versions and API versions do not need to match. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
