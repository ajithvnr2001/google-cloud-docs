---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-BindingDelta/
title: BigQuery Reservation V1 API - Class Google::Iam::V1::BindingDelta (v1.14.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:29.748102+00:00
---

# BigQuery Reservation V1 API - Class Google::Iam::V1::BindingDelta (v1.14.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-BindingDelta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Reservation V1 API - Class Google::Iam::V1::BindingDelta (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.1  1.12.1  1.11.0  1.10.0  1.9.2  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.12.0  0.11.2  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.2 

Reference documentation and code samples for the BigQuery Reservation V1 API class Google::Iam::V1::BindingDelta.

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

  * ([::Google::Iam::V1::BindingDelta::Action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-BindingDelta-Action)) — The action that was performed on a Binding. Required 



### #action=
    
    
    def action=(value) -> ::Google::Iam::V1::BindingDelta::Action

**Parameter**

  * **value** ([::Google::Iam::V1::BindingDelta::Action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-BindingDelta-Action)) — The action that was performed on a Binding. Required 



**Returns**

  * ([::Google::Iam::V1::BindingDelta::Action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-BindingDelta-Action)) — The action that was performed on a Binding. Required 



### #condition
    
    
    def condition() -> ::Google::Type::Expr

**Returns**

  * ([::Google::Type::Expr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Type-Expr)) — The condition that is associated with this binding. 



### #condition=
    
    
    def condition=(value) -> ::Google::Type::Expr

**Parameter**

  * **value** ([::Google::Type::Expr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Type-Expr)) — The condition that is associated with this binding. 



**Returns**

  * ([::Google::Type::Expr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Type-Expr)) — The condition that is associated with this binding. 



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
