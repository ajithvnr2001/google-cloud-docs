---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ResourceEnrollmentStatus/
title: Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:11.409005+00:00
---

# Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ResourceEnrollmentStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.1  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Audit Manager V1 API class Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus.

An organization, folder, or project with its enrollment status.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Output only. Display name for the organization, folder, or project. 



### #enrolled
    
    
    def enrolled() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Deprecated. Whether the organization, folder, or project is enrolled. Use `enrollment_state` instead. 



### #enrollment
    
    
    def enrollment() -> ::Google::Cloud::AuditManager::V1::Enrollment

**Returns**

  * ([::Google::Cloud::AuditManager::V1::Enrollment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-Enrollment)) — Output only. Enrolled destination details for the organization, folder, or project. 



### #enrollment_state
    
    
    def enrollment_state() -> ::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus::ResourceEnrollmentState

**Returns**

  * ([::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus::ResourceEnrollmentState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ResourceEnrollmentStatus-ResourceEnrollmentState)) — Output only. Enrollment state of the organization, folder, or project. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — 

Identifier. Name of the resource enrollment status, in one of the following formats:

    * `folders/{folder}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}`
    * `projects/{project}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}`
    * `organizations/{organization}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Identifier. Name of the resource enrollment status, in one of the following formats:

    * `folders/{folder}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}`
    * `projects/{project}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}`
    * `organizations/{organization}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}`



**Returns**

  * (::String) — 

Identifier. Name of the resource enrollment status, in one of the following formats:

    * `folders/{folder}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}`
    * `projects/{project}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}`
    * `organizations/{organization}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
