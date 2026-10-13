---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-OpenSessionRequest/
title: Cloud Bigtable V2 API - Class Google::Cloud::Bigtable::V2::OpenSessionRequest (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:37.061115+00:00
---

# Cloud Bigtable V2 API - Class Google::Cloud::Bigtable::V2::OpenSessionRequest (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-OpenSessionRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Bigtable V2 API - Class Google::Cloud::Bigtable::V2::OpenSessionRequest (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the Cloud Bigtable V2 API class Google::Cloud::Bigtable::V2::OpenSessionRequest.

Internal usage only.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #consecutive_failed_connection_attempts
    
    
    def consecutive_failed_connection_attempts() -> ::Integer

**Returns**

  * (::Integer) — Used for serverside observability. 



### #consecutive_failed_connection_attempts=
    
    
    def consecutive_failed_connection_attempts=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Used for serverside observability. 



**Returns**

  * (::Integer) — Used for serverside observability. 



### #flags
    
    
    def flags() -> ::Google::Cloud::Bigtable::V2::FeatureFlags

**Returns**

  * ([::Google::Cloud::Bigtable::V2::FeatureFlags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-FeatureFlags)) — Client settings, including a record of 



### #flags=
    
    
    def flags=(value) -> ::Google::Cloud::Bigtable::V2::FeatureFlags

**Parameter**

  * **value** ([::Google::Cloud::Bigtable::V2::FeatureFlags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-FeatureFlags)) — Client settings, including a record of 



**Returns**

  * ([::Google::Cloud::Bigtable::V2::FeatureFlags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-FeatureFlags)) — Client settings, including a record of 



### #payload
    
    
    def payload() -> ::String

**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — Can be Open\\{Table,AuthorizedView,MaterializedView}Request, (or in post-V1, PrepareSqlQueryRequest) 



### #payload=
    
    
    def payload=(value) -> ::String

**Parameter**

  * **value** ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — Can be Open\\{Table,AuthorizedView,MaterializedView}Request, (or in post-V1, PrepareSqlQueryRequest) 



**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — Can be Open\\{Table,AuthorizedView,MaterializedView}Request, (or in post-V1, PrepareSqlQueryRequest) 



### #protocol_version
    
    
    def protocol_version() -> ::Integer

**Returns**

  * (::Integer) — A version indicator from the client stating its understanding of the protocol. This is to disambiguate client behavior amidst changes in semantic usage of the API, e.g. if the structure remains the same but behavior changes. 



### #protocol_version=
    
    
    def protocol_version=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — A version indicator from the client stating its understanding of the protocol. This is to disambiguate client behavior amidst changes in semantic usage of the API, e.g. if the structure remains the same but behavior changes. 



**Returns**

  * (::Integer) — A version indicator from the client stating its understanding of the protocol. This is to disambiguate client behavior amidst changes in semantic usage of the API, e.g. if the structure remains the same but behavior changes. 



### #routing_cookie
    
    
    def routing_cookie() -> ::String

**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — How the request should be routed (if presented as part of a GOAWAY from a previous session). Post V1. 



### #routing_cookie=
    
    
    def routing_cookie=(value) -> ::String

**Parameter**

  * **value** ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — How the request should be routed (if presented as part of a GOAWAY from a previous session). Post V1. 



**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — How the request should be routed (if presented as part of a GOAWAY from a previous session). Post V1. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
