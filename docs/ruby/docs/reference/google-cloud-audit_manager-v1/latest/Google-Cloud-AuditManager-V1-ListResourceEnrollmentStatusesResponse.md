---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListResourceEnrollmentStatusesResponse/
title: Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::ListResourceEnrollmentStatusesResponse (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:52.903050+00:00
---

# Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::ListResourceEnrollmentStatusesResponse (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ListResourceEnrollmentStatusesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::ListResourceEnrollmentStatusesResponse (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.1  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Audit Manager V1 API class Google::Cloud::AuditManager::V1::ListResourceEnrollmentStatusesResponse.

Response message for [ListResourceEnrollmentStatuses](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client#Google__Cloud__AuditManager__V1__AuditManager__Client_list_resource_enrollment_statuses_instance_ "Google::Cloud::AuditManager::V1::AuditManager::Client#list_resource_enrollment_statuses \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — Output only. A token that you can send as the `page_token` in a subsequent request to retrieve the next page of results. If this field is empty, there are no subsequent pages. 



### #resource_enrollment_statuses
    
    
    def resource_enrollment_statuses() -> ::Array<::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus>

**Returns**

  * (::Array<[::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ResourceEnrollmentStatus)>) — Resources with their enrollment status. 



### #resource_enrollment_statuses=
    
    
    def resource_enrollment_statuses=(value) -> ::Array<::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus>

**Parameter**

  * **value** (::Array<[::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ResourceEnrollmentStatus)>) — Resources with their enrollment status. 



**Returns**

  * (::Array<[::Google::Cloud::AuditManager::V1::ResourceEnrollmentStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ResourceEnrollmentStatus)>) — Resources with their enrollment status. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
