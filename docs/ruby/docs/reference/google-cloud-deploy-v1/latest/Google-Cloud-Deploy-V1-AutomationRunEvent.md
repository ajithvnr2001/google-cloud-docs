---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-AutomationRunEvent/
title: Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::AutomationRunEvent (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:20.250594+00:00
---

# Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::AutomationRunEvent (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-AutomationRunEvent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Deploy V1 API - Class Google::Cloud::Deploy::V1::AutomationRunEvent (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.1  2.0.2  1.6.0  1.5.0  1.4.0  1.3.0  1.2.2  1.1.0  1.0.0  0.20.0  0.19.1  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Google Cloud Deploy V1 API class Google::Cloud::Deploy::V1::AutomationRunEvent.

Payload proto for "clouddeploy.googleapis.com/automation_run" Platform Log event that describes the AutomationRun related events.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #automation_id
    
    
    def automation_id() -> ::String

**Returns**

  * (::String) — Identifier of the `Automation`. 



### #automation_id=
    
    
    def automation_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier of the `Automation`. 



**Returns**

  * (::String) — Identifier of the `Automation`. 



### #automation_run
    
    
    def automation_run() -> ::String

**Returns**

  * (::String) — The name of the `AutomationRun`. 



### #automation_run=
    
    
    def automation_run=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the `AutomationRun`. 



**Returns**

  * (::String) — The name of the `AutomationRun`. 



### #destination_target_id
    
    
    def destination_target_id() -> ::String

**Returns**

  * (::String) — ID of the `Target` to which the `AutomationRun` is created. 



### #destination_target_id=
    
    
    def destination_target_id=(value) -> ::String

**Parameter**

  * **value** (::String) — ID of the `Target` to which the `AutomationRun` is created. 



**Returns**

  * (::String) — ID of the `Target` to which the `AutomationRun` is created. 



### #message
    
    
    def message() -> ::String

**Returns**

  * (::String) — Debug message for when there is an update on the AutomationRun. Provides further details about the resource creation or state change. 



### #message=
    
    
    def message=(value) -> ::String

**Parameter**

  * **value** (::String) — Debug message for when there is an update on the AutomationRun. Provides further details about the resource creation or state change. 



**Returns**

  * (::String) — Debug message for when there is an update on the AutomationRun. Provides further details about the resource creation or state change. 



### #pipeline_uid
    
    
    def pipeline_uid() -> ::String

**Returns**

  * (::String) — Unique identifier of the `DeliveryPipeline`. 



### #pipeline_uid=
    
    
    def pipeline_uid=(value) -> ::String

**Parameter**

  * **value** (::String) — Unique identifier of the `DeliveryPipeline`. 



**Returns**

  * (::String) — Unique identifier of the `DeliveryPipeline`. 



### #rule_id
    
    
    def rule_id() -> ::String

**Returns**

  * (::String) — Identifier of the `Automation` rule. 



### #rule_id=
    
    
    def rule_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier of the `Automation` rule. 



**Returns**

  * (::String) — Identifier of the `Automation` rule. 



### #type
    
    
    def type() -> ::Google::Cloud::Deploy::V1::Type

**Returns**

  * ([::Google::Cloud::Deploy::V1::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Type)) — Type of this notification, e.g. for a Pub/Sub failure. 



### #type=
    
    
    def type=(value) -> ::Google::Cloud::Deploy::V1::Type

**Parameter**

  * **value** ([::Google::Cloud::Deploy::V1::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Type)) — Type of this notification, e.g. for a Pub/Sub failure. 



**Returns**

  * ([::Google::Cloud::Deploy::V1::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-deploy-v1/latest/Google-Cloud-Deploy-V1-Type)) — Type of this notification, e.g. for a Pub/Sub failure. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
