---
url: https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3beta/latest/Google-Iam-V3beta-SearchTargetPolicyBindingsRequest/
title: Identity and Access Management (IAM) V3BETA API - Class Google::Iam::V3beta::SearchTargetPolicyBindingsRequest (v0.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:50.670971+00:00
---

# Identity and Access Management (IAM) V3BETA API - Class Google::Iam::V3beta::SearchTargetPolicyBindingsRequest (v0.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3beta/latest/Google-Iam-V3beta-SearchTargetPolicyBindingsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) V3BETA API - Class Google::Iam::V3beta::SearchTargetPolicyBindingsRequest (v0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.4.1  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Identity and Access Management (IAM) V3BETA API class Google::Iam::V3beta::SearchTargetPolicyBindingsRequest.

Request message for SearchTargetPolicyBindings method.

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

Optional. Filtering currently only supports the kind of policies to return, and must be in the format "policy_kind={policy_kind}".

If String is empty, bindings bound to all kinds of policies would be returned.

The only supported values are the following:

    * "policy_kind=PRINCIPAL_ACCESS_BOUNDARY",
    * "policy_kind=ACCESS"



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. Filtering currently only supports the kind of policies to return, and must be in the format "policy_kind={policy_kind}".

If String is empty, bindings bound to all kinds of policies would be returned.

The only supported values are the following:

    * "policy_kind=PRINCIPAL_ACCESS_BOUNDARY",
    * "policy_kind=ACCESS"



**Returns**

  * (::String) — 

Optional. Filtering currently only supports the kind of policies to return, and must be in the format "policy_kind={policy_kind}".

If String is empty, bindings bound to all kinds of policies would be returned.

The only supported values are the following:

    * "policy_kind=PRINCIPAL_ACCESS_BOUNDARY",
    * "policy_kind=ACCESS"



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

  * (::String) — Optional. A page token, received from a previous `SearchTargetPolicyBindingsRequest` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `SearchTargetPolicyBindingsRequest` must match the call that provided the page token. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A page token, received from a previous `SearchTargetPolicyBindingsRequest` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `SearchTargetPolicyBindingsRequest` must match the call that provided the page token. 




**Returns**

  * (::String) — Optional. A page token, received from a previous `SearchTargetPolicyBindingsRequest` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `SearchTargetPolicyBindingsRequest` must match the call that provided the page token. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — 

Required. The parent resource where this search will be performed. This should be the nearest Resource Manager resource (project, folder, or organization) to the target.

Format:

    * `projects/{project_id}/locations/{location}`
    * `projects/{project_number}/locations/{location}`
    * `folders/{folder_id}/locations/{location}`
    * `organizations/{organization_id}/locations/{location}`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. The parent resource where this search will be performed. This should be the nearest Resource Manager resource (project, folder, or organization) to the target.

Format:

    * `projects/{project_id}/locations/{location}`
    * `projects/{project_number}/locations/{location}`
    * `folders/{folder_id}/locations/{location}`
    * `organizations/{organization_id}/locations/{location}`



**Returns**

  * (::String) — 

Required. The parent resource where this search will be performed. This should be the nearest Resource Manager resource (project, folder, or organization) to the target.

Format:

    * `projects/{project_id}/locations/{location}`
    * `projects/{project_number}/locations/{location}`
    * `folders/{folder_id}/locations/{location}`
    * `organizations/{organization_id}/locations/{location}`



### #target
    
    
    def target() -> ::String

**Returns**

  * (::String) — 

Required. The target resource, which is bound to the policy in the binding.

Format:

    * `//iam.googleapis.com/locations/global/workforcePools/POOL_ID`
    * `//iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID`
    * `//iam.googleapis.com/locations/global/workspace/WORKSPACE_ID`
    * `//cloudresourcemanager.googleapis.com/projects/{project_number}`
    * `//cloudresourcemanager.googleapis.com/folders/{folder_id}`
    * `//cloudresourcemanager.googleapis.com/organizations/{organization_id}`



### #target=
    
    
    def target=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. The target resource, which is bound to the policy in the binding.

Format:

    * `//iam.googleapis.com/locations/global/workforcePools/POOL_ID`
    * `//iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID`
    * `//iam.googleapis.com/locations/global/workspace/WORKSPACE_ID`
    * `//cloudresourcemanager.googleapis.com/projects/{project_number}`
    * `//cloudresourcemanager.googleapis.com/folders/{folder_id}`
    * `//cloudresourcemanager.googleapis.com/organizations/{organization_id}`



**Returns**

  * (::String) — 

Required. The target resource, which is bound to the policy in the binding.

Format:

    * `//iam.googleapis.com/locations/global/workforcePools/POOL_ID`
    * `//iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID`
    * `//iam.googleapis.com/locations/global/workspace/WORKSPACE_ID`
    * `//cloudresourcemanager.googleapis.com/projects/{project_number}`
    * `//cloudresourcemanager.googleapis.com/folders/{folder_id}`
    * `//cloudresourcemanager.googleapis.com/organizations/{organization_id}`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
