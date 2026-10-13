---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ReportSummary/
title: Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::ReportSummary (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:53.425186+00:00
---

# Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::ReportSummary (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ReportSummary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::ReportSummary (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.1  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Audit Manager V1 API class Google::Cloud::AuditManager::V1::ReportSummary.

Additional information about the number of checks that were made during an audit operation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #compliant_count
    
    
    def compliant_count() -> ::Integer

**Returns**

  * (::Integer) — Number of compliant checks. 



### #compliant_count=
    
    
    def compliant_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Number of compliant checks. 



**Returns**

  * (::Integer) — Number of compliant checks. 



### #error_count
    
    
    def error_count() -> ::Integer

**Returns**

  * (::Integer) — Number of checks that can't be performed due to errors. 



### #error_count=
    
    
    def error_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Number of checks that can't be performed due to errors. 



**Returns**

  * (::Integer) — Number of checks that can't be performed due to errors. 



### #manual_review_needed_count
    
    
    def manual_review_needed_count() -> ::Integer

**Returns**

  * (::Integer) — Number of checks that require a manual review. 



### #manual_review_needed_count=
    
    
    def manual_review_needed_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Number of checks that require a manual review. 



**Returns**

  * (::Integer) — Number of checks that require a manual review. 



### #total_count
    
    
    def total_count() -> ::Integer

**Returns**

  * (::Integer) — Total number of evaluated checks. 



### #total_count=
    
    
    def total_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Total number of evaluated checks. 



**Returns**

  * (::Integer) — Total number of evaluated checks. 



### #violation_count
    
    
    def violation_count() -> ::Integer

**Returns**

  * (::Integer) — Number of checks with violations. 



### #violation_count=
    
    
    def violation_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Number of checks with violations. 



**Returns**

  * (::Integer) — Number of checks with violations. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
