---
url: https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-DeletePrincipalAccessBoundaryPolicyRequest/
title: Identity and Access Management (IAM) V3 API - Class Google::Iam::V3::DeletePrincipalAccessBoundaryPolicyRequest (v0.6.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:06.997832+00:00
---

# Identity and Access Management (IAM) V3 API - Class Google::Iam::V3::DeletePrincipalAccessBoundaryPolicyRequest (v0.6.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-DeletePrincipalAccessBoundaryPolicyRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) V3 API - Class Google::Iam::V3::DeletePrincipalAccessBoundaryPolicyRequest (v0.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.0 (latest)  0.5.0  0.4.1  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Identity and Access Management (IAM) V3 API class Google::Iam::V3::DeletePrincipalAccessBoundaryPolicyRequest.

Request message for DeletePrincipalAccessBoundaryPolicy method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — Optional. The etag of the principal access boundary policy. If this is provided, it must match the server's etag. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The etag of the principal access boundary policy. If this is provided, it must match the server's etag. 



**Returns**

  * (::String) — Optional. The etag of the principal access boundary policy. If this is provided, it must match the server's etag. 



### #force
    
    
    def force() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If set to true, the request will force the deletion of the policy even if the policy is referenced in policy bindings. 



### #force=
    
    
    def force=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If set to true, the request will force the deletion of the policy even if the policy is referenced in policy bindings. 



**Returns**

  * (::Boolean) — Optional. If set to true, the request will force the deletion of the policy even if the policy is referenced in policy bindings. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The name of the principal access boundary policy to delete.

Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`




### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the principal access boundary policy to delete.

Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`




**Returns**

  * (::String) — Required. The name of the principal access boundary policy to delete.

Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`




### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If set, validate the request and preview the deletion, but do not actually post it. 



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If set, validate the request and preview the deletion, but do not actually post it. 



**Returns**

  * (::Boolean) — Optional. If set, validate the request and preview the deletion, but do not actually post it. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
