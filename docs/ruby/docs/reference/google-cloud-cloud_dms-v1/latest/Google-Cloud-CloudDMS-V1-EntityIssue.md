---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityIssue/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::EntityIssue (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:28.631901+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::EntityIssue (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityIssue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::EntityIssue (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::EntityIssue.

Issue related to the entity.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #code
    
    
    def code() -> ::String

**Returns**

  * (::String) — Error/Warning code 



### #code=
    
    
    def code=(value) -> ::String

**Parameter**

  * **value** (::String) — Error/Warning code 



**Returns**

  * (::String) — Error/Warning code 



### #ddl
    
    
    def ddl() -> ::String

**Returns**

  * (::String) — The ddl which caused the issue, if relevant. 



### #ddl=
    
    
    def ddl=(value) -> ::String

**Parameter**

  * **value** (::String) — The ddl which caused the issue, if relevant. 



**Returns**

  * (::String) — The ddl which caused the issue, if relevant. 



### #entity_type
    
    
    def entity_type() -> ::Google::Cloud::CloudDMS::V1::DatabaseEntityType

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — The entity type (if the DDL is for a sub entity). 



### #entity_type=
    
    
    def entity_type=(value) -> ::Google::Cloud::CloudDMS::V1::DatabaseEntityType

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — The entity type (if the DDL is for a sub entity). 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — The entity type (if the DDL is for a sub entity). 



### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — Unique Issue ID. 



### #id=
    
    
    def id=(value) -> ::String

**Parameter**

  * **value** (::String) — Unique Issue ID. 



**Returns**

  * (::String) — Unique Issue ID. 



### #message
    
    
    def message() -> ::String

**Returns**

  * (::String) — Issue detailed message 



### #message=
    
    
    def message=(value) -> ::String

**Parameter**

  * **value** (::String) — Issue detailed message 



**Returns**

  * (::String) — Issue detailed message 



### #position
    
    
    def position() -> ::Google::Cloud::CloudDMS::V1::EntityIssue::Position

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::EntityIssue::Position](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityIssue-Position)) — The position of the issue found, if relevant. 



### #position=
    
    
    def position=(value) -> ::Google::Cloud::CloudDMS::V1::EntityIssue::Position

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::EntityIssue::Position](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityIssue-Position)) — The position of the issue found, if relevant. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::EntityIssue::Position](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityIssue-Position)) — The position of the issue found, if relevant. 



### #severity
    
    
    def severity() -> ::Google::Cloud::CloudDMS::V1::EntityIssue::IssueSeverity

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::EntityIssue::IssueSeverity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityIssue-IssueSeverity)) — Severity of the issue 



### #severity=
    
    
    def severity=(value) -> ::Google::Cloud::CloudDMS::V1::EntityIssue::IssueSeverity

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::EntityIssue::IssueSeverity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityIssue-IssueSeverity)) — Severity of the issue 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::EntityIssue::IssueSeverity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityIssue-IssueSeverity)) — Severity of the issue 



### #type
    
    
    def type() -> ::Google::Cloud::CloudDMS::V1::EntityIssue::IssueType

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::EntityIssue::IssueType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityIssue-IssueType)) — The type of the issue. 



### #type=
    
    
    def type=(value) -> ::Google::Cloud::CloudDMS::V1::EntityIssue::IssueType

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::EntityIssue::IssueType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityIssue-IssueType)) — The type of the issue. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::EntityIssue::IssueType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityIssue-IssueType)) — The type of the issue. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
