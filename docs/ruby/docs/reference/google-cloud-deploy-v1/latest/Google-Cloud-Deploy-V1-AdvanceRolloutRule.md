---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-AdvanceRolloutRule/
title: Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::AdvanceRolloutRule (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:18.594080+00:00
---

# Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::AdvanceRolloutRule (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-AdvanceRolloutRule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::AdvanceRolloutRule (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.1  2.0.2  1.6.0  1.5.0  1.4.0  1.3.0  1.2.2  1.1.0  1.0.0  0.20.0  0.19.1  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Google Cloud Deploy V1 API class Google::Cloud::Deploy::V1::AdvanceRolloutRule.

The `AdvanceRollout` automation rule will automatically advance a successful Rollout to the next phase.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #condition
    
    
    def condition() -> ::Google::Cloud::Deploy::V1::AutomationRuleCondition

**Returns**

  * ([::Google::Cloud::Deploy::V1::AutomationRuleCondition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-AutomationRuleCondition)) — Output only. Information around the state of the Automation rule. 



### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — Required. ID of the rule. This id must be unique in the `Automation` resource to which this rule belongs. The format is `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`. 



### #id=
    
    
    def id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. ID of the rule. This id must be unique in the `Automation` resource to which this rule belongs. The format is `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`. 



**Returns**

  * (::String) — Required. ID of the rule. This id must be unique in the `Automation` resource to which this rule belongs. The format is `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`. 



### #source_phases
    
    
    def source_phases() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. Proceeds only after phase name matched any one in the list. This value must consist of lower-case letters, numbers, and hyphens, start with a letter and end with a letter or a number, and have a max length of 63 characters. In other words, it must match the following regex: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`. 



### #source_phases=
    
    
    def source_phases=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. Proceeds only after phase name matched any one in the list. This value must consist of lower-case letters, numbers, and hyphens, start with a letter and end with a letter or a number, and have a max length of 63 characters. In other words, it must match the following regex: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`. 



**Returns**

  * (::Array<::String>) — Optional. Proceeds only after phase name matched any one in the list. This value must consist of lower-case letters, numbers, and hyphens, start with a letter and end with a letter or a number, and have a max length of 63 characters. In other words, it must match the following regex: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`. 



### #wait
    
    
    def wait() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Duration)) — Optional. How long to wait after a rollout is finished. 



### #wait=
    
    
    def wait=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Duration)) — Optional. How long to wait after a rollout is finished. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Protobuf-Duration)) — Optional. How long to wait after a rollout is finished. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
