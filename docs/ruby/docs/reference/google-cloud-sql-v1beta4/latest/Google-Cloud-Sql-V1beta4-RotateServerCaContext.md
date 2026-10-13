---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-RotateServerCaContext/
title: Cloud SQL Admin V1BETA4 API - Class Google::Cloud::Sql::V1beta4::RotateServerCaContext (v0.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:37.617689+00:00
---

# Cloud SQL Admin V1BETA4 API - Class Google::Cloud::Sql::V1beta4::RotateServerCaContext (v0.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-RotateServerCaContext/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud SQL Admin V1BETA4 API - Class Google::Cloud::Sql::V1beta4::RotateServerCaContext (v0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.2.0 (latest)  0.1.1 

Reference documentation and code samples for the Cloud SQL Admin V1BETA4 API class Google::Cloud::Sql::V1beta4::RotateServerCaContext.

Instance rotate server CA context.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — This is always `sql#rotateServerCaContext`. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — This is always `sql#rotateServerCaContext`. 



**Returns**

  * (::String) — This is always `sql#rotateServerCaContext`. 



### #next_version
    
    
    def next_version() -> ::String

**Returns**

  * (::String) — The fingerprint of the next version to be rotated to. If left unspecified, will be rotated to the most recently added server CA version. 



### #next_version=
    
    
    def next_version=(value) -> ::String

**Parameter**

  * **value** (::String) — The fingerprint of the next version to be rotated to. If left unspecified, will be rotated to the most recently added server CA version. 



**Returns**

  * (::String) — The fingerprint of the next version to be rotated to. If left unspecified, will be rotated to the most recently added server CA version. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
