---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TransferRule/
title: Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::TransferRule (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:41.341335+00:00
---

# Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::TransferRule (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TransferRule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1 API - Class Google::Cloud::Ces::V1::TransferRule (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1 API class Google::Cloud::Ces::V1::TransferRule.

Rule for transferring to a specific agent.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #child_agent
    
    
    def child_agent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the child agent the rule applies to. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`



### #child_agent=
    
    
    def child_agent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the child agent the rule applies to. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`



**Returns**

  * (::String) — Required. The resource name of the child agent the rule applies to. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`



### #deterministic_transfer
    
    
    def deterministic_transfer() -> ::Google::Cloud::Ces::V1::TransferRule::DeterministicTransfer

**Returns**

  * ([::Google::Cloud::Ces::V1::TransferRule::DeterministicTransfer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TransferRule-DeterministicTransfer)) — Optional. A rule that immediately transfers to the target agent when the condition is met.

Note: The following fields are mutually exclusive: `deterministic_transfer`, `disable_planner_transfer`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #deterministic_transfer=
    
    
    def deterministic_transfer=(value) -> ::Google::Cloud::Ces::V1::TransferRule::DeterministicTransfer

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::TransferRule::DeterministicTransfer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TransferRule-DeterministicTransfer)) — Optional. A rule that immediately transfers to the target agent when the condition is met.

Note: The following fields are mutually exclusive: `deterministic_transfer`, `disable_planner_transfer`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Ces::V1::TransferRule::DeterministicTransfer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TransferRule-DeterministicTransfer)) — Optional. A rule that immediately transfers to the target agent when the condition is met.

Note: The following fields are mutually exclusive: `deterministic_transfer`, `disable_planner_transfer`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #direction
    
    
    def direction() -> ::Google::Cloud::Ces::V1::TransferRule::Direction

**Returns**

  * ([::Google::Cloud::Ces::V1::TransferRule::Direction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TransferRule-Direction)) — Required. The direction of the transfer. 



### #direction=
    
    
    def direction=(value) -> ::Google::Cloud::Ces::V1::TransferRule::Direction

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::TransferRule::Direction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TransferRule-Direction)) — Required. The direction of the transfer. 



**Returns**

  * ([::Google::Cloud::Ces::V1::TransferRule::Direction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TransferRule-Direction)) — Required. The direction of the transfer. 



### #disable_planner_transfer
    
    
    def disable_planner_transfer() -> ::Google::Cloud::Ces::V1::TransferRule::DisablePlannerTransfer

**Returns**

  * ([::Google::Cloud::Ces::V1::TransferRule::DisablePlannerTransfer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TransferRule-DisablePlannerTransfer)) — Optional. Rule that prevents the planner from transferring to the target agent.

Note: The following fields are mutually exclusive: `disable_planner_transfer`, `deterministic_transfer`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #disable_planner_transfer=
    
    
    def disable_planner_transfer=(value) -> ::Google::Cloud::Ces::V1::TransferRule::DisablePlannerTransfer

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1::TransferRule::DisablePlannerTransfer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TransferRule-DisablePlannerTransfer)) — Optional. Rule that prevents the planner from transferring to the target agent.

Note: The following fields are mutually exclusive: `disable_planner_transfer`, `deterministic_transfer`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Ces::V1::TransferRule::DisablePlannerTransfer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1/latest/Google-Cloud-Ces-V1-TransferRule-DisablePlannerTransfer)) — Optional. Rule that prevents the planner from transferring to the target agent.

Note: The following fields are mutually exclusive: `disable_planner_transfer`, `deterministic_transfer`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
