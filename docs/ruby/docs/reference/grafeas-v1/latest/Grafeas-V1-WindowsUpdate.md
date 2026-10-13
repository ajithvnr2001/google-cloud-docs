---
url: https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-WindowsUpdate/
title: Grafeas V1 API - Class Grafeas::V1::WindowsUpdate (v1.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:12.487148+00:00
---

# Grafeas V1 API - Class Grafeas::V1::WindowsUpdate (v1.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-WindowsUpdate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Grafeas V1 API - Class Grafeas::V1::WindowsUpdate (v1.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.1 (latest)  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.0  1.1.1  1.0.0  0.16.1  0.15.0  0.14.2  0.13.0  0.12.1  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.1 

Reference documentation and code samples for the Grafeas V1 API class Grafeas::V1::WindowsUpdate.

Windows Update represents the metadata about the update for the Windows operating system. The fields in this message come from the Windows Update API documented at <https://docs.microsoft.com/en-us/windows/win32/api/wuapi/nn-wuapi-iupdate>.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #categories
    
    
    def categories() -> ::Array<::Grafeas::V1::WindowsUpdate::Category>

**Returns**

  * (::Array<[::Grafeas::V1::WindowsUpdate::Category](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-WindowsUpdate-Category)>) — The list of categories to which the update belongs. 



### #categories=
    
    
    def categories=(value) -> ::Array<::Grafeas::V1::WindowsUpdate::Category>

**Parameter**

  * **value** (::Array<[::Grafeas::V1::WindowsUpdate::Category](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-WindowsUpdate-Category)>) — The list of categories to which the update belongs. 



**Returns**

  * (::Array<[::Grafeas::V1::WindowsUpdate::Category](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-WindowsUpdate-Category)>) — The list of categories to which the update belongs. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — The localized description of the update. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — The localized description of the update. 



**Returns**

  * (::String) — The localized description of the update. 



### #identity
    
    
    def identity() -> ::Grafeas::V1::WindowsUpdate::Identity

**Returns**

  * ([::Grafeas::V1::WindowsUpdate::Identity](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-WindowsUpdate-Identity)) — Required - The unique identifier for the update. 



### #identity=
    
    
    def identity=(value) -> ::Grafeas::V1::WindowsUpdate::Identity

**Parameter**

  * **value** ([::Grafeas::V1::WindowsUpdate::Identity](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-WindowsUpdate-Identity)) — Required - The unique identifier for the update. 



**Returns**

  * ([::Grafeas::V1::WindowsUpdate::Identity](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Grafeas-V1-WindowsUpdate-Identity)) — Required - The unique identifier for the update. 



### #kb_article_ids
    
    
    def kb_article_ids() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The Microsoft Knowledge Base article IDs that are associated with the update. 



### #kb_article_ids=
    
    
    def kb_article_ids=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The Microsoft Knowledge Base article IDs that are associated with the update. 



**Returns**

  * (::Array<::String>) — The Microsoft Knowledge Base article IDs that are associated with the update. 



### #last_published_timestamp
    
    
    def last_published_timestamp() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — The last published timestamp of the update. 



### #last_published_timestamp=
    
    
    def last_published_timestamp=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — The last published timestamp of the update. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/grafeas-v1/latest/Google-Protobuf-Timestamp)) — The last published timestamp of the update. 



### #support_url
    
    
    def support_url() -> ::String

**Returns**

  * (::String) — The hyperlink to the support information for the update. 



### #support_url=
    
    
    def support_url=(value) -> ::String

**Parameter**

  * **value** (::String) — The hyperlink to the support information for the update. 



**Returns**

  * (::String) — The hyperlink to the support information for the update. 



### #title
    
    
    def title() -> ::String

**Returns**

  * (::String) — The localized title of the update. 



### #title=
    
    
    def title=(value) -> ::String

**Parameter**

  * **value** (::String) — The localized title of the update. 



**Returns**

  * (::String) — The localized title of the update. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
