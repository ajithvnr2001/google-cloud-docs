---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Fulfillment-ConditionalCases-Case/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Fulfillment::ConditionalCases::Case (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:18.702093+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Fulfillment::ConditionalCases::Case (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Fulfillment-ConditionalCases-Case/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Fulfillment::ConditionalCases::Case (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::Fulfillment::ConditionalCases::Case.

Each case has a Boolean condition. When it is evaluated to be True, the corresponding messages will be selected and evaluated recursively.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #case_content
    
    
    def case_content() -> ::Array<::Google::Cloud::Dialogflow::CX::V3::Fulfillment::ConditionalCases::Case::CaseContent>

**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::CX::V3::Fulfillment::ConditionalCases::Case::CaseContent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Fulfillment-ConditionalCases-Case-CaseContent)>) — A list of case content. 



### #case_content=
    
    
    def case_content=(value) -> ::Array<::Google::Cloud::Dialogflow::CX::V3::Fulfillment::ConditionalCases::Case::CaseContent>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dialogflow::CX::V3::Fulfillment::ConditionalCases::Case::CaseContent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Fulfillment-ConditionalCases-Case-CaseContent)>) — A list of case content. 



**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::CX::V3::Fulfillment::ConditionalCases::Case::CaseContent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Fulfillment-ConditionalCases-Case-CaseContent)>) — A list of case content. 



### #condition
    
    
    def condition() -> ::String

**Returns**

  * (::String) — The condition to activate and select this case. Empty means the condition is always true. The condition is evaluated against [form parameters][Form.parameters] or [session parameters][SessionInfo.parameters].

See the [conditions reference](https://cloud.google.com/dialogflow/cx/docs/reference/condition). 




### #condition=
    
    
    def condition=(value) -> ::String

**Parameter**

  * **value** (::String) — The condition to activate and select this case. Empty means the condition is always true. The condition is evaluated against [form parameters][Form.parameters] or [session parameters][SessionInfo.parameters].

See the [conditions reference](https://cloud.google.com/dialogflow/cx/docs/reference/condition). 




**Returns**

  * (::String) — The condition to activate and select this case. Empty means the condition is always true. The condition is evaluated against [form parameters][Form.parameters] or [session parameters][SessionInfo.parameters].

See the [conditions reference](https://cloud.google.com/dialogflow/cx/docs/reference/condition). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
