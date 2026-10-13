---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-migration_center-v1/latest/Google-Cloud-MigrationCenter-V1-ListReportsRequest/
title: Migration Center V1 API - Class Google::Cloud::MigrationCenter::V1::ListReportsRequest (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:45.324246+00:00
---

# Migration Center V1 API - Class Google::Cloud::MigrationCenter::V1::ListReportsRequest (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-migration_center-v1/latest/Google-Cloud-MigrationCenter-V1-ListReportsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Migration Center V1 API - Class Google::Cloud::MigrationCenter::V1::ListReportsRequest (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.3.0  0.2.2  0.1.0 

Reference documentation and code samples for the Migration Center V1 API class Google::Cloud::MigrationCenter::V1::ListReportsRequest.

A request for a list of Reports.

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

  * (::String) — Filtering results. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Filtering results. 



**Returns**

  * (::String) — Filtering results. 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Field to sort by. See https://google.aip.dev/132#ordering for more details. 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Field to sort by. See https://google.aip.dev/132#ordering for more details. 



**Returns**

  * (::String) — Field to sort by. See https://google.aip.dev/132#ordering for more details. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Requested page size. The server may return fewer items than requested. If unspecified, the server will pick an appropriate default value. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Requested page size. The server may return fewer items than requested. If unspecified, the server will pick an appropriate default value. 



**Returns**

  * (::Integer) — Requested page size. The server may return fewer items than requested. If unspecified, the server will pick an appropriate default value. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — A token identifying a page of results that the server should return. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token identifying a page of results that the server should return. 



**Returns**

  * (::String) — A token identifying a page of results that the server should return. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. Parent value for `ListReportsRequest`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Parent value for `ListReportsRequest`. 



**Returns**

  * (::String) — Required. Parent value for `ListReportsRequest`. 



### #view
    
    
    def view() -> ::Google::Cloud::MigrationCenter::V1::ReportView

**Returns**

  * ([::Google::Cloud::MigrationCenter::V1::ReportView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-migration_center-v1/latest/Google-Cloud-MigrationCenter-V1-ReportView)) — Determines what information to retrieve for each Report. 



### #view=
    
    
    def view=(value) -> ::Google::Cloud::MigrationCenter::V1::ReportView

**Parameter**

  * **value** ([::Google::Cloud::MigrationCenter::V1::ReportView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-migration_center-v1/latest/Google-Cloud-MigrationCenter-V1-ReportView)) — Determines what information to retrieve for each Report. 



**Returns**

  * ([::Google::Cloud::MigrationCenter::V1::ReportView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-migration_center-v1/latest/Google-Cloud-MigrationCenter-V1-ReportView)) — Determines what information to retrieve for each Report. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
