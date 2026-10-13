---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v2/latest/Google-Cloud-Notebooks-V2-Event/
title: Notebooks V2 API - Class Google::Cloud::Notebooks::V2::Event (v1.6.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:31.822389+00:00
---

# Notebooks V2 API - Class Google::Cloud::Notebooks::V2::Event (v1.6.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v2/latest/Google-Cloud-Notebooks-V2-Event/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Notebooks V2 API - Class Google::Cloud::Notebooks::V2::Event (v1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.6.0  0.5.0  0.4.2  0.3.2  0.2.0  0.1.0 

Reference documentation and code samples for the Notebooks V2 API class Google::Cloud::Notebooks::V2::Event.

The definition of an Event for a managed / semi-managed notebook instance.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #details
    
    
    def details() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Event details. This field is used to pass event information. 



### #details=
    
    
    def details=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Event details. This field is used to pass event information. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Event details. This field is used to pass event information. 



### #report_time
    
    
    def report_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v2/latest/Google-Protobuf-Timestamp)) — Optional. Event report time. 



### #report_time=
    
    
    def report_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v2/latest/Google-Protobuf-Timestamp)) — Optional. Event report time. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v2/latest/Google-Protobuf-Timestamp)) — Optional. Event report time. 



### #type
    
    
    def type() -> ::Google::Cloud::Notebooks::V2::Event::EventType

**Returns**

  * ([::Google::Cloud::Notebooks::V2::Event::EventType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v2/latest/Google-Cloud-Notebooks-V2-Event-EventType)) — Optional. Event type. 



### #type=
    
    
    def type=(value) -> ::Google::Cloud::Notebooks::V2::Event::EventType

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V2::Event::EventType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v2/latest/Google-Cloud-Notebooks-V2-Event-EventType)) — Optional. Event type. 



**Returns**

  * ([::Google::Cloud::Notebooks::V2::Event::EventType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v2/latest/Google-Cloud-Notebooks-V2-Event-EventType)) — Optional. Event type. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
