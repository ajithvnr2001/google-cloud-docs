---
url: https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3beta/latest/Google-Longrunning-ListOperationsRequest/
title: Identity and Access Management (IAM) V3BETA API - Class Google::Longrunning::ListOperationsRequest (v0.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:19.174754+00:00
---

# Identity and Access Management (IAM) V3BETA API - Class Google::Longrunning::ListOperationsRequest (v0.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3beta/latest/Google-Longrunning-ListOperationsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) V3BETA API - Class Google::Longrunning::ListOperationsRequest (v0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.4.1  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Identity and Access Management (IAM) V3BETA API class Google::Longrunning::ListOperationsRequest.

The request message for Operations.ListOperations.

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

  * (::String) — The standard list filter. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — The standard list filter. 



**Returns**

  * (::String) — The standard list filter. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The name of the operation's parent resource. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the operation's parent resource. 



**Returns**

  * (::String) — The name of the operation's parent resource. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The standard list page size. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The standard list page size. 



**Returns**

  * (::Integer) — The standard list page size. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — The standard list page token. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — The standard list page token. 



**Returns**

  * (::String) — The standard list page token. 



### #return_partial_success
    
    
    def return_partial_success() -> ::Boolean

**Returns**

  * (::Boolean) — When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the [ListOperationsResponse.unreachable] field.

This can only be `true` when reading across collections e.g. when `parent` is set to `"projects/example/locations/-"`.

This field is not by default supported and will result in an `UNIMPLEMENTED` error if set unless explicitly documented otherwise in service or product specific documentation. 




### #return_partial_success=
    
    
    def return_partial_success=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the [ListOperationsResponse.unreachable] field.

This can only be `true` when reading across collections e.g. when `parent` is set to `"projects/example/locations/-"`.

This field is not by default supported and will result in an `UNIMPLEMENTED` error if set unless explicitly documented otherwise in service or product specific documentation. 




**Returns**

  * (::Boolean) — When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the [ListOperationsResponse.unreachable] field.

This can only be `true` when reading across collections e.g. when `parent` is set to `"projects/example/locations/-"`.

This field is not by default supported and will result in an `UNIMPLEMENTED` error if set unless explicitly documented otherwise in service or product specific documentation. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
