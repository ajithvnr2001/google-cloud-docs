---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Iam-V1-BindingDelta/
title: Secret Manager V1BETA2 API - Class Google::Iam::V1::BindingDelta (v0.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:26.696995+00:00
---

# Secret Manager V1BETA2 API - Class Google::Iam::V1::BindingDelta (v0.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Iam-V1-BindingDelta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Secret Manager V1BETA2 API - Class Google::Iam::V1::BindingDelta (v0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.1 

Reference documentation and code samples for the Secret Manager V1BETA2 API class Google::Iam::V1::BindingDelta.

One delta entry for Binding. Each individual change (only one member in each entry) to a binding will be a separate entry.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #action
    
    
    def action() -> ::Google::Iam::V1::BindingDelta::Action

**Returns**

  * ([::Google::Iam::V1::BindingDelta::Action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Iam-V1-BindingDelta-Action)) — The action that was performed on a Binding. Required 



### #action=
    
    
    def action=(value) -> ::Google::Iam::V1::BindingDelta::Action

**Parameter**

  * **value** ([::Google::Iam::V1::BindingDelta::Action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Iam-V1-BindingDelta-Action)) — The action that was performed on a Binding. Required 



**Returns**

  * ([::Google::Iam::V1::BindingDelta::Action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Iam-V1-BindingDelta-Action)) — The action that was performed on a Binding. Required 



### #condition
    
    
    def condition() -> ::Google::Type::Expr

**Returns**

  * ([::Google::Type::Expr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Type-Expr)) — The condition that is associated with this binding. 



### #condition=
    
    
    def condition=(value) -> ::Google::Type::Expr

**Parameter**

  * **value** ([::Google::Type::Expr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Type-Expr)) — The condition that is associated with this binding. 



**Returns**

  * ([::Google::Type::Expr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Type-Expr)) — The condition that is associated with this binding. 



### #member
    
    
    def member() -> ::String

**Returns**

  * (::String) — A single identity requesting access for a Google Cloud resource. Follows the same format of Binding.members. Required 



### #member=
    
    
    def member=(value) -> ::String

**Parameter**

  * **value** (::String) — A single identity requesting access for a Google Cloud resource. Follows the same format of Binding.members. Required 



**Returns**

  * (::String) — A single identity requesting access for a Google Cloud resource. Follows the same format of Binding.members. Required 



### #role
    
    
    def role() -> ::String

**Returns**

  * (::String) — Role that is assigned to `members`. For example, `roles/viewer`, `roles/editor`, or `roles/owner`. Required 



### #role=
    
    
    def role=(value) -> ::String

**Parameter**

  * **value** (::String) — Role that is assigned to `members`. For example, `roles/viewer`, `roles/editor`, or `roles/owner`. Required 



**Returns**

  * (::String) — Role that is assigned to `members`. For example, `roles/viewer`, `roles/editor`, or `roles/owner`. Required 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
