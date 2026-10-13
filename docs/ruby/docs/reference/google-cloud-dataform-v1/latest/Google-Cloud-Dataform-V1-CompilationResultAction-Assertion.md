---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-CompilationResultAction-Assertion/
title: Dataform V1 API - Class Google::Cloud::Dataform::V1::CompilationResultAction::Assertion (v1.3.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:53.068972+00:00
---

# Dataform V1 API - Class Google::Cloud::Dataform::V1::CompilationResultAction::Assertion (v1.3.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-CompilationResultAction-Assertion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataform V1 API - Class Google::Cloud::Dataform::V1::CompilationResultAction::Assertion (v1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataform V1 API class Google::Cloud::Dataform::V1::CompilationResultAction::Assertion.

Represents an assertion upon a SQL query which is required return zero rows.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #dependency_targets
    
    
    def dependency_targets() -> ::Array<::Google::Cloud::Dataform::V1::Target>

**Returns**

  * (::Array<[::Google::Cloud::Dataform::V1::Target](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-Target)>) — A list of actions that this action depends on. 



### #dependency_targets=
    
    
    def dependency_targets=(value) -> ::Array<::Google::Cloud::Dataform::V1::Target>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dataform::V1::Target](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-Target)>) — A list of actions that this action depends on. 



**Returns**

  * (::Array<[::Google::Cloud::Dataform::V1::Target](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-Target)>) — A list of actions that this action depends on. 



### #disabled
    
    
    def disabled() -> ::Boolean

**Returns**

  * (::Boolean) — Whether this action is disabled (i.e. should not be run). 



### #disabled=
    
    
    def disabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether this action is disabled (i.e. should not be run). 



**Returns**

  * (::Boolean) — Whether this action is disabled (i.e. should not be run). 



### #parent_action
    
    
    def parent_action() -> ::Google::Cloud::Dataform::V1::Target

**Returns**

  * ([::Google::Cloud::Dataform::V1::Target](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-Target)) — The parent action of this assertion. Only set if this assertion was automatically generated. 



### #parent_action=
    
    
    def parent_action=(value) -> ::Google::Cloud::Dataform::V1::Target

**Parameter**

  * **value** ([::Google::Cloud::Dataform::V1::Target](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-Target)) — The parent action of this assertion. Only set if this assertion was automatically generated. 



**Returns**

  * ([::Google::Cloud::Dataform::V1::Target](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-Target)) — The parent action of this assertion. Only set if this assertion was automatically generated. 



### #relation_descriptor
    
    
    def relation_descriptor() -> ::Google::Cloud::Dataform::V1::RelationDescriptor

**Returns**

  * ([::Google::Cloud::Dataform::V1::RelationDescriptor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-RelationDescriptor)) — Descriptor for the assertion's automatically-generated view and its columns. 



### #relation_descriptor=
    
    
    def relation_descriptor=(value) -> ::Google::Cloud::Dataform::V1::RelationDescriptor

**Parameter**

  * **value** ([::Google::Cloud::Dataform::V1::RelationDescriptor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-RelationDescriptor)) — Descriptor for the assertion's automatically-generated view and its columns. 



**Returns**

  * ([::Google::Cloud::Dataform::V1::RelationDescriptor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Cloud-Dataform-V1-RelationDescriptor)) — Descriptor for the assertion's automatically-generated view and its columns. 



### #select_query
    
    
    def select_query() -> ::String

**Returns**

  * (::String) — The SELECT query which must return zero rows in order for this assertion to succeed. 



### #select_query=
    
    
    def select_query=(value) -> ::String

**Parameter**

  * **value** (::String) — The SELECT query which must return zero rows in order for this assertion to succeed. 



**Returns**

  * (::String) — The SELECT query which must return zero rows in order for this assertion to succeed. 



### #tags
    
    
    def tags() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Arbitrary, user-defined tags on this action. 



### #tags=
    
    
    def tags=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Arbitrary, user-defined tags on this action. 



**Returns**

  * (::Array<::String>) — Arbitrary, user-defined tags on this action. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
