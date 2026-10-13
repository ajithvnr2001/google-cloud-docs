---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-ConditionExplanation-EvaluationState/
title: Policy Troubleshooter V3 API - Class Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionExplanation::EvaluationState (v0.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:32.704629+00:00
---

# Policy Troubleshooter V3 API - Class Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionExplanation::EvaluationState (v0.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-ConditionExplanation-EvaluationState/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Policy Troubleshooter V3 API - Class Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionExplanation::EvaluationState (v0.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.0 (latest)  0.11.1  0.10.0  0.9.1  0.8.0  0.7.0  0.6.1  0.5.0  0.4.1  0.3.2  0.2.0  0.1.0 

Reference documentation and code samples for the Policy Troubleshooter V3 API class Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionExplanation::EvaluationState.

Evaluated state of a condition expression.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #end
    
    
    def end() -> ::Integer

**Returns**

  * (::Integer) — End position of an expression in the condition, by character, end included, for example: the end position of the first part of `a==b || c==d` would be 4. 



### #end=
    
    
    def end=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — End position of an expression in the condition, by character, end included, for example: the end position of the first part of `a==b || c==d` would be 4. 



**Returns**

  * (::Integer) — End position of an expression in the condition, by character, end included, for example: the end position of the first part of `a==b || c==d` would be 4. 



### #errors
    
    
    def errors() -> ::Array<::Google::Rpc::Status>

**Returns**

  * (::Array<[::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Rpc-Status)>) — Any errors that prevented complete evaluation of the condition expression. 



### #errors=
    
    
    def errors=(value) -> ::Array<::Google::Rpc::Status>

**Parameter**

  * **value** (::Array<[::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Rpc-Status)>) — Any errors that prevented complete evaluation of the condition expression. 



**Returns**

  * (::Array<[::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Rpc-Status)>) — Any errors that prevented complete evaluation of the condition expression. 



### #start
    
    
    def start() -> ::Integer

**Returns**

  * (::Integer) — Start position of an expression in the condition, by character. 



### #start=
    
    
    def start=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Start position of an expression in the condition, by character. 



**Returns**

  * (::Integer) — Start position of an expression in the condition, by character. 



### #value
    
    
    def value() -> ::Google::Protobuf::Value

**Returns**

  * ([::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Protobuf-Value)) — Value of this expression. 



### #value=
    
    
    def value=(value) -> ::Google::Protobuf::Value

**Parameter**

  * **value** ([::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Protobuf-Value)) — Value of this expression. 



**Returns**

  * ([::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Protobuf-Value)) — Value of this expression. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
