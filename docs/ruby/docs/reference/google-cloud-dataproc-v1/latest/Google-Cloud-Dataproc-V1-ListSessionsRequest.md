---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-ListSessionsRequest/
title: Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::ListSessionsRequest (v1.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:04.860695+00:00
---

# Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::ListSessionsRequest (v1.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-ListSessionsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::ListSessionsRequest (v1.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.1 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.2  0.26.0  0.25.0  0.24.1  0.23.1  0.22.0  0.21.0  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1 

Reference documentation and code samples for the Cloud Dataproc V1 API class Google::Cloud::Dataproc::V1::ListSessionsRequest.

A request to list sessions in a project.

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

  * (::String) — Optional. A filter for the sessions to return in the response.

A filter is a logical expression constraining the values of various fields in each session resource. Filters are case sensitive, and may contain multiple clauses combined with logical operators (AND, OR). Supported fields are `session_id`, `session_uuid`, `state`, `create_time`, and `labels`.

Example: `state = ACTIVE and create_time < "2023-01-01T00:00:00Z"` is a filter for sessions in an ACTIVE state that were created before 2023-01-01. `state = ACTIVE and labels.environment=production` is a filter for sessions in an ACTIVE state that have a production environment label.

See https://google.aip.dev/assets/misc/ebnf-filtering.txt for a detailed description of the filter syntax and a list of supported comparators. 




### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A filter for the sessions to return in the response.

A filter is a logical expression constraining the values of various fields in each session resource. Filters are case sensitive, and may contain multiple clauses combined with logical operators (AND, OR). Supported fields are `session_id`, `session_uuid`, `state`, `create_time`, and `labels`.

Example: `state = ACTIVE and create_time < "2023-01-01T00:00:00Z"` is a filter for sessions in an ACTIVE state that were created before 2023-01-01. `state = ACTIVE and labels.environment=production` is a filter for sessions in an ACTIVE state that have a production environment label.

See https://google.aip.dev/assets/misc/ebnf-filtering.txt for a detailed description of the filter syntax and a list of supported comparators. 




**Returns**

  * (::String) — Optional. A filter for the sessions to return in the response.

A filter is a logical expression constraining the values of various fields in each session resource. Filters are case sensitive, and may contain multiple clauses combined with logical operators (AND, OR). Supported fields are `session_id`, `session_uuid`, `state`, `create_time`, and `labels`.

Example: `state = ACTIVE and create_time < "2023-01-01T00:00:00Z"` is a filter for sessions in an ACTIVE state that were created before 2023-01-01. `state = ACTIVE and labels.environment=production` is a filter for sessions in an ACTIVE state that have a production environment label.

See https://google.aip.dev/assets/misc/ebnf-filtering.txt for a detailed description of the filter syntax and a list of supported comparators. 




### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of sessions to return in each response. The service may return fewer than this value. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of sessions to return in each response. The service may return fewer than this value. 



**Returns**

  * (::Integer) — Optional. The maximum number of sessions to return in each response. The service may return fewer than this value. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A page token received from a previous `ListSessions` call. Provide this token to retrieve the subsequent page. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A page token received from a previous `ListSessions` call. Provide this token to retrieve the subsequent page. 



**Returns**

  * (::String) — Optional. A page token received from a previous `ListSessions` call. Provide this token to retrieve the subsequent page. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent, which owns this collection of sessions. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent, which owns this collection of sessions. 



**Returns**

  * (::String) — Required. The parent, which owns this collection of sessions. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
