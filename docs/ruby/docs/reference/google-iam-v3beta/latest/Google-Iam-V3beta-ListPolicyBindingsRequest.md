---
url: https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3beta/latest/Google-Iam-V3beta-ListPolicyBindingsRequest/
title: Identity and Access Management (IAM) V3BETA API - Class Google::Iam::V3beta::ListPolicyBindingsRequest (v0.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:15:43.266679+00:00
---

# Identity and Access Management (IAM) V3BETA API - Class Google::Iam::V3beta::ListPolicyBindingsRequest (v0.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3beta/latest/Google-Iam-V3beta-ListPolicyBindingsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) V3BETA API - Class Google::Iam::V3beta::ListPolicyBindingsRequest (v0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.4.1  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Identity and Access Management (IAM) V3BETA API class Google::Iam::V3beta::ListPolicyBindingsRequest.

Request message for ListPolicyBindings method.

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

  * (::String) — 

Optional. An expression for filtering the results of the request. Filter rules are case insensitive. Some eligible fields for filtering are the following:

    * `target`
    * `policy`

Some examples of filter queries:

    * `target:ex*`: The binding target's name starts with "ex".
    * `target:example`: The binding target's name is `example`.
    * `policy:example`: The binding policy's name is `example`.



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. An expression for filtering the results of the request. Filter rules are case insensitive. Some eligible fields for filtering are the following:

    * `target`
    * `policy`

Some examples of filter queries:

    * `target:ex*`: The binding target's name starts with "ex".
    * `target:example`: The binding target's name is `example`.
    * `policy:example`: The binding policy's name is `example`.



**Returns**

  * (::String) — 

Optional. An expression for filtering the results of the request. Filter rules are case insensitive. Some eligible fields for filtering are the following:

    * `target`
    * `policy`

Some examples of filter queries:

    * `target:ex*`: The binding target's name starts with "ex".
    * `target:example`: The binding target's name is `example`.
    * `policy:example`: The binding policy's name is `example`.



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of policy bindings to return. The service may return fewer than this value.

The default value is 50. The maximum value is 1000. 




### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of policy bindings to return. The service may return fewer than this value.

The default value is 50. The maximum value is 1000. 




**Returns**

  * (::Integer) — Optional. The maximum number of policy bindings to return. The service may return fewer than this value.

The default value is 50. The maximum value is 1000. 




### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A page token, received from a previous `ListPolicyBindings` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListPolicyBindings` must match the call that provided the page token. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A page token, received from a previous `ListPolicyBindings` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListPolicyBindings` must match the call that provided the page token. 




**Returns**

  * (::String) — Optional. A page token, received from a previous `ListPolicyBindings` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListPolicyBindings` must match the call that provided the page token. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — 

Required. The parent resource, which owns the collection of policy bindings.

Format:

    * `projects/{project_id}/locations/{location}`
    * `projects/{project_number}/locations/{location}`
    * `folders/{folder_id}/locations/{location}`
    * `organizations/{organization_id}/locations/{location}`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. The parent resource, which owns the collection of policy bindings.

Format:

    * `projects/{project_id}/locations/{location}`
    * `projects/{project_number}/locations/{location}`
    * `folders/{folder_id}/locations/{location}`
    * `organizations/{organization_id}/locations/{location}`



**Returns**

  * (::String) — 

Required. The parent resource, which owns the collection of policy bindings.

Format:

    * `projects/{project_id}/locations/{location}`
    * `projects/{project_number}/locations/{location}`
    * `folders/{folder_id}/locations/{location}`
    * `organizations/{organization_id}/locations/{location}`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
