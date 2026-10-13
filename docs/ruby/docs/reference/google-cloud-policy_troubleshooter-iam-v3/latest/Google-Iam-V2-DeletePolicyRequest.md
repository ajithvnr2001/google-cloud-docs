---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Iam-V2-DeletePolicyRequest/
title: Policy Troubleshooter V3 API - Class Google::Iam::V2::DeletePolicyRequest (v0.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:30.030314+00:00
---

# Policy Troubleshooter V3 API - Class Google::Iam::V2::DeletePolicyRequest (v0.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Iam-V2-DeletePolicyRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Policy Troubleshooter V3 API - Class Google::Iam::V2::DeletePolicyRequest (v0.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.0 (latest)  0.11.1  0.10.0  0.9.1  0.8.0  0.7.0  0.6.1  0.5.0  0.4.1  0.3.2  0.2.0  0.1.0 

Reference documentation and code samples for the Policy Troubleshooter V3 API class Google::Iam::V2::DeletePolicyRequest.

Request message for `DeletePolicy`.

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

  * (::String) — Optional. The expected `etag` of the policy to delete. If the value does not match the value that is stored in IAM, the request fails with a `409` error code and `ABORTED` status.

If you omit this field, the policy is deleted regardless of its current `etag`. 




### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The expected `etag` of the policy to delete. If the value does not match the value that is stored in IAM, the request fails with a `409` error code and `ABORTED` status.

If you omit this field, the policy is deleted regardless of its current `etag`. 




**Returns**

  * (::String) — Optional. The expected `etag` of the policy to delete. If the value does not match the value that is stored in IAM, the request fails with a `409` error code and `ABORTED` status.

If you omit this field, the policy is deleted regardless of its current `etag`. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The resource name of the policy to delete. Format: `policies/{attachment_point}/denypolicies/{policy_id}`

Use the URL-encoded full resource name, which means that the forward-slash character, `/`, must be written as `%2F`. For example, `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project/denypolicies/my-policy`.

For organizations and folders, use the numeric ID in the full resource name. For projects, you can use the alphanumeric or the numeric ID. 




### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the policy to delete. Format: `policies/{attachment_point}/denypolicies/{policy_id}`

Use the URL-encoded full resource name, which means that the forward-slash character, `/`, must be written as `%2F`. For example, `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project/denypolicies/my-policy`.

For organizations and folders, use the numeric ID in the full resource name. For projects, you can use the alphanumeric or the numeric ID. 




**Returns**

  * (::String) — Required. The resource name of the policy to delete. Format: `policies/{attachment_point}/denypolicies/{policy_id}`

Use the URL-encoded full resource name, which means that the forward-slash character, `/`, must be written as `%2F`. For example, `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project/denypolicies/my-policy`.

For organizations and folders, use the numeric ID in the full resource name. For projects, you can use the alphanumeric or the numeric ID. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
