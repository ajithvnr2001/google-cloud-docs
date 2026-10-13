---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-ListFrameworkAuditsRequest/
title: Cloud Security Compliance V1 API - Class Google::Cloud::CloudSecurityCompliance::V1::ListFrameworkAuditsRequest (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:17.956570+00:00
---

# Cloud Security Compliance V1 API - Class Google::Cloud::CloudSecurityCompliance::V1::ListFrameworkAuditsRequest (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-ListFrameworkAuditsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Security Compliance V1 API - Class Google::Cloud::CloudSecurityCompliance::V1::ListFrameworkAuditsRequest (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Cloud Security Compliance V1 API class Google::Cloud::CloudSecurityCompliance::V1::ListFrameworkAuditsRequest.

The request message for [ListFrameworkAudits][].

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — Optional. The filters to apply to the framework audits. Supported filters are `compliance_framework`, `compliance_state`, `create_time,` and `framework_audit_name`. If the filter is invalid, an invalid argument error is returned. For syntax details, see [AIP-160][https://google.aip.dev/160]. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The filters to apply to the framework audits. Supported filters are `compliance_framework`, `compliance_state`, `create_time,` and `framework_audit_name`. If the filter is invalid, an invalid argument error is returned. For syntax details, see [AIP-160][https://google.aip.dev/160]. 



**Returns**

  * (::String) — Optional. The filters to apply to the framework audits. Supported filters are `compliance_framework`, `compliance_state`, `create_time,` and `framework_audit_name`. If the filter is invalid, an invalid argument error is returned. For syntax details, see [AIP-160][https://google.aip.dev/160]. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of framework audits to return. The service might return fewer audits than this value. If unspecified, a maximum of 10 framework audits are returned. The maximum value is 50; values above 50 are limited to 50. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of framework audits to return. The service might return fewer audits than this value. If unspecified, a maximum of 10 framework audits are returned. The maximum value is 50; values above 50 are limited to 50. 



**Returns**

  * (::Integer) — Optional. The maximum number of framework audits to return. The service might return fewer audits than this value. If unspecified, a maximum of 10 framework audits are returned. The maximum value is 50; values above 50 are limited to 50. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. The `next_page_token` value that's returned from a previous list request, if any. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The `next_page_token` value that's returned from a previous list request, if any. 



**Returns**

  * (::String) — Optional. The `next_page_token` value that's returned from a previous list request, if any. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — 

Required. The parent resource where the framework audits are listed.

Supported formats are the following:

    * `organizations/{organization_id}/locations/{location}`
    * `folders/{folder_id}/locations/{location}`
    * `projects/{project_id}/locations/{location}`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. The parent resource where the framework audits are listed.

Supported formats are the following:

    * `organizations/{organization_id}/locations/{location}`
    * `folders/{folder_id}/locations/{location}`
    * `projects/{project_id}/locations/{location}`



**Returns**

  * (::String) — 

Required. The parent resource where the framework audits are listed.

Supported formats are the following:

    * `organizations/{organization_id}/locations/{location}`
    * `folders/{folder_id}/locations/{location}`
    * `projects/{project_id}/locations/{location}`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
