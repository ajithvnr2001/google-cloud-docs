---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-Control/
title: Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::Control (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:48.901689+00:00
---

# Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::Control (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-Control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::Control (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.1  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Audit Manager V1 API class Google::Cloud::AuditManager::V1::Control.

A control.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #control_family
    
    
    def control_family() -> ::Google::Cloud::AuditManager::V1::ControlFamily

**Returns**

  * ([::Google::Cloud::AuditManager::V1::ControlFamily](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ControlFamily)) — Output only. Regulatory family of the control. 



### #customer_responsibility_description
    
    
    def customer_responsibility_description() -> ::String

**Returns**

  * (::String) — Output only. A description of your responsibility for this control. 



### #customer_responsibility_implementation
    
    
    def customer_responsibility_implementation() -> ::String

**Returns**

  * (::String) — Output only. A description of how you can implement your responsibility for this control. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Output only. Description of the control. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Output only. Display name of the control. 



### #family
    
    
    def family() -> ::Google::Cloud::AuditManager::V1::Control::Family

**Returns**

  * ([::Google::Cloud::AuditManager::V1::Control::Family](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-Control-Family)) — Output only. Category that the control belongs to. 



### #google_responsibility_description
    
    
    def google_responsibility_description() -> ::String

**Returns**

  * (::String) — Output only. A description of Google's responsibility for this control. 



### #google_responsibility_implementation
    
    
    def google_responsibility_implementation() -> ::String

**Returns**

  * (::String) — Output only. A description of how Google implements its responsibility for this control. 



### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — Output only. Control identifier that's used to fetch the findings. The identifier is the same as the control report name. 



### #responsibility_type
    
    
    def responsibility_type() -> ::String

**Returns**

  * (::String) — Output only. Who is responsible for implementing this control. Set to one of the following values: `GOOGLE`, `CUSTOMER`, or `SHARED`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
