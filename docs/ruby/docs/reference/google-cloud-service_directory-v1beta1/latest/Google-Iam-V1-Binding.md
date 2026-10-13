---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1beta1/latest/Google-Iam-V1-Binding/
title: Service Directory V1beta1 API - Class Google::Iam::V1::Binding (v0.22.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:17.294605+00:00
---

# Service Directory V1beta1 API - Class Google::Iam::V1::Binding (v0.22.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1beta1/latest/Google-Iam-V1-Binding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Service Directory V1beta1 API - Class Google::Iam::V1::Binding (v0.22.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.1 (latest)  0.22.0  0.21.1  0.20.0  0.19.1  0.18.0  0.17.1  0.16.0  0.15.2  0.14.2  0.13.0  0.12.1  0.11.1  0.10.0  0.9.0  0.8.0  0.7.4 

Reference documentation and code samples for the Service Directory V1beta1 API class Google::Iam::V1::Binding.

Associates `members`, or principals, with a `role`.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #condition
    
    
    def condition() -> ::Google::Type::Expr

**Returns**

  * ([::Google::Type::Expr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1beta1/latest/Google-Type-Expr)) — The condition that is associated with this binding.

If the condition evaluates to `true`, then this binding applies to the current request.

If the condition evaluates to `false`, then this binding does not apply to the current request. However, a different role binding might grant the same role to one or more of the principals in this binding.

To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). 




### #condition=
    
    
    def condition=(value) -> ::Google::Type::Expr

**Parameter**

  * **value** ([::Google::Type::Expr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1beta1/latest/Google-Type-Expr)) — The condition that is associated with this binding.

If the condition evaluates to `true`, then this binding applies to the current request.

If the condition evaluates to `false`, then this binding does not apply to the current request. However, a different role binding might grant the same role to one or more of the principals in this binding.

To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). 




**Returns**

  * ([::Google::Type::Expr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1beta1/latest/Google-Type-Expr)) — The condition that is associated with this binding.

If the condition evaluates to `true`, then this binding applies to the current request.

If the condition evaluates to `false`, then this binding does not apply to the current request. However, a different role binding might grant the same role to one or more of the principals in this binding.

To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). 




### #members
    
    
    def members() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — 

Specifies the principals requesting access for a Google Cloud resource. `members` can have the following values:

    * `allUsers`: A special identifier that represents anyone who is on the internet; with or without a Google account.

    * `allAuthenticatedUsers`: A special identifier that represents anyone who is authenticated with a Google account or a service account.

    * `user:{emailid}`: An email address that represents a specific Google account. For example, `alice@example.com` .

    * `serviceAccount:{emailid}`: An email address that represents a service account. For example, `my-other-app@appspot.gserviceaccount.com`.

    * `group:{emailid}`: An email address that represents a Google group. For example, `admins@example.com`.

    * `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a user that has been recently deleted. For example, `alice@example.com?uid=123456789012345678901`. If the user is recovered, this value reverts to `user:{emailid}` and the recovered user retains the role in the binding.

    * `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a service account that has been recently deleted. For example, `my-other-app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the service account is undeleted, this value reverts to `serviceAccount:{emailid}` and the undeleted service account retains the role in the binding.

    * `deleted:group:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a Google group that has been recently deleted. For example, `admins@example.com?uid=123456789012345678901`. If the group is recovered, this value reverts to `group:{emailid}` and the recovered group retains the role in the binding.

    * `domain:{domain}`: The G Suite domain (primary) that represents all the users of that domain. For example, `google.com` or `example.com`.




### #members=
    
    
    def members=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — 

Specifies the principals requesting access for a Google Cloud resource. `members` can have the following values:

    * `allUsers`: A special identifier that represents anyone who is on the internet; with or without a Google account.

    * `allAuthenticatedUsers`: A special identifier that represents anyone who is authenticated with a Google account or a service account.

    * `user:{emailid}`: An email address that represents a specific Google account. For example, `alice@example.com` .

    * `serviceAccount:{emailid}`: An email address that represents a service account. For example, `my-other-app@appspot.gserviceaccount.com`.

    * `group:{emailid}`: An email address that represents a Google group. For example, `admins@example.com`.

    * `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a user that has been recently deleted. For example, `alice@example.com?uid=123456789012345678901`. If the user is recovered, this value reverts to `user:{emailid}` and the recovered user retains the role in the binding.

    * `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a service account that has been recently deleted. For example, `my-other-app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the service account is undeleted, this value reverts to `serviceAccount:{emailid}` and the undeleted service account retains the role in the binding.

    * `deleted:group:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a Google group that has been recently deleted. For example, `admins@example.com?uid=123456789012345678901`. If the group is recovered, this value reverts to `group:{emailid}` and the recovered group retains the role in the binding.

    * `domain:{domain}`: The G Suite domain (primary) that represents all the users of that domain. For example, `google.com` or `example.com`.




**Returns**

  * (::Array<::String>) — 

Specifies the principals requesting access for a Google Cloud resource. `members` can have the following values:

    * `allUsers`: A special identifier that represents anyone who is on the internet; with or without a Google account.

    * `allAuthenticatedUsers`: A special identifier that represents anyone who is authenticated with a Google account or a service account.

    * `user:{emailid}`: An email address that represents a specific Google account. For example, `alice@example.com` .

    * `serviceAccount:{emailid}`: An email address that represents a service account. For example, `my-other-app@appspot.gserviceaccount.com`.

    * `group:{emailid}`: An email address that represents a Google group. For example, `admins@example.com`.

    * `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a user that has been recently deleted. For example, `alice@example.com?uid=123456789012345678901`. If the user is recovered, this value reverts to `user:{emailid}` and the recovered user retains the role in the binding.

    * `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a service account that has been recently deleted. For example, `my-other-app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the service account is undeleted, this value reverts to `serviceAccount:{emailid}` and the undeleted service account retains the role in the binding.

    * `deleted:group:{emailid}?uid={uniqueid}`: An email address (plus unique identifier) representing a Google group that has been recently deleted. For example, `admins@example.com?uid=123456789012345678901`. If the group is recovered, this value reverts to `group:{emailid}` and the recovered group retains the role in the binding.

    * `domain:{domain}`: The G Suite domain (primary) that represents all the users of that domain. For example, `google.com` or `example.com`.




### #role
    
    
    def role() -> ::String

**Returns**

  * (::String) — Role that is assigned to the list of `members`, or principals. For example, `roles/viewer`, `roles/editor`, or `roles/owner`. 



### #role=
    
    
    def role=(value) -> ::String

**Parameter**

  * **value** (::String) — Role that is assigned to the list of `members`, or principals. For example, `roles/viewer`, `roles/editor`, or `roles/owner`. 



**Returns**

  * (::String) — Role that is assigned to the list of `members`, or principals. For example, `roles/viewer`, `roles/editor`, or `roles/owner`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
