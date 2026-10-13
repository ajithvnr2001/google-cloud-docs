---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-connection-v1/latest/Google-Iam-V1-SetIamPolicyRequest/
title: BigQuery Connection V1 API - Class Google::Iam::V1::SetIamPolicyRequest (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:55.672921+00:00
---

# BigQuery Connection V1 API - Class Google::Iam::V1::SetIamPolicyRequest (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-connection-v1/latest/Google-Iam-V1-SetIamPolicyRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Connection V1 API - Class Google::Iam::V1::SetIamPolicyRequest (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.18.0  0.17.2  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.3 

Reference documentation and code samples for the BigQuery Connection V1 API class Google::Iam::V1::SetIamPolicyRequest.

Request message for `SetIamPolicy` method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #policy
    
    
    def policy() -> ::Google::Iam::V1::Policy

**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-connection-v1/latest/Google-Iam-V1-Policy)) — REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them. 



### #policy=
    
    
    def policy=(value) -> ::Google::Iam::V1::Policy

**Parameter**

  * **value** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-connection-v1/latest/Google-Iam-V1-Policy)) — REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them. 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-connection-v1/latest/Google-Iam-V1-Policy)) — REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them. 



### #resource
    
    
    def resource() -> ::String

**Returns**

  * (::String) — REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. 



### #resource=
    
    
    def resource=(value) -> ::String

**Parameter**

  * **value** (::String) — REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. 



**Returns**

  * (::String) — REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-connection-v1/latest/Google-Protobuf-FieldMask)) — OPTIONAL: A FieldMask specifying which fields of the policy to modify. Only the fields in the mask will be modified. If no mask is provided, the following default mask is used:

`paths: "bindings, etag"`




### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-connection-v1/latest/Google-Protobuf-FieldMask)) — OPTIONAL: A FieldMask specifying which fields of the policy to modify. Only the fields in the mask will be modified. If no mask is provided, the following default mask is used:

`paths: "bindings, etag"`




**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-connection-v1/latest/Google-Protobuf-FieldMask)) — OPTIONAL: A FieldMask specifying which fields of the policy to modify. Only the fields in the mask will be modified. If no mask is provided, the following default mask is used:

`paths: "bindings, etag"`




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
