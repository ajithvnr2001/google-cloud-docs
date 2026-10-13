---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-StreamAssistResponse/
title: Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::StreamAssistResponse (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:50.490022+00:00
---

# Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::StreamAssistResponse (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-StreamAssistResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::StreamAssistResponse (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.1  2.10.1  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Discovery Engine V1 API class Google::Cloud::DiscoveryEngine::V1::StreamAssistResponse.

Response for the [AssistantService.StreamAssist](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-AssistantService-Client#Google__Cloud__DiscoveryEngine__V1__AssistantService__Client_stream_assist_instance_ "Google::Cloud::DiscoveryEngine::V1::AssistantService::Client#stream_assist \(method\)") method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #answer
    
    
    def answer() -> ::Google::Cloud::DiscoveryEngine::V1::AssistAnswer

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::AssistAnswer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-AssistAnswer)) — Assist answer resource object containing parts of the assistant's final answer for the user's query.

Not present if the current response doesn't add anything to previously sent [AssistAnswer.replies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-AssistAnswer#Google__Cloud__DiscoveryEngine__V1__AssistAnswer_replies_instance_ "Google::Cloud::DiscoveryEngine::V1::AssistAnswer#replies \(method\)").

Observe [AssistAnswer.state](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-AssistAnswer#Google__Cloud__DiscoveryEngine__V1__AssistAnswer_state_instance_ "Google::Cloud::DiscoveryEngine::V1::AssistAnswer#state \(method\)") to see if more parts are to be expected. While the state is `IN_PROGRESS`, the [AssistAnswer.replies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-AssistAnswer#Google__Cloud__DiscoveryEngine__V1__AssistAnswer_replies_instance_ "Google::Cloud::DiscoveryEngine::V1::AssistAnswer#replies \(method\)") field in each response will contain replies (reply fragments) to be appended to the ones received in previous responses. [AssistAnswer.name][] won't be filled.

If the state is `SUCCEEDED`, `FAILED` or `SKIPPED`, the response is the last response and [AssistAnswer.name][] will have a value. 




### #answer=
    
    
    def answer=(value) -> ::Google::Cloud::DiscoveryEngine::V1::AssistAnswer

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1::AssistAnswer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-AssistAnswer)) — Assist answer resource object containing parts of the assistant's final answer for the user's query.

Not present if the current response doesn't add anything to previously sent [AssistAnswer.replies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-AssistAnswer#Google__Cloud__DiscoveryEngine__V1__AssistAnswer_replies_instance_ "Google::Cloud::DiscoveryEngine::V1::AssistAnswer#replies \(method\)").

Observe [AssistAnswer.state](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-AssistAnswer#Google__Cloud__DiscoveryEngine__V1__AssistAnswer_state_instance_ "Google::Cloud::DiscoveryEngine::V1::AssistAnswer#state \(method\)") to see if more parts are to be expected. While the state is `IN_PROGRESS`, the [AssistAnswer.replies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-AssistAnswer#Google__Cloud__DiscoveryEngine__V1__AssistAnswer_replies_instance_ "Google::Cloud::DiscoveryEngine::V1::AssistAnswer#replies \(method\)") field in each response will contain replies (reply fragments) to be appended to the ones received in previous responses. [AssistAnswer.name][] won't be filled.

If the state is `SUCCEEDED`, `FAILED` or `SKIPPED`, the response is the last response and [AssistAnswer.name][] will have a value. 




**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::AssistAnswer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-AssistAnswer)) — Assist answer resource object containing parts of the assistant's final answer for the user's query.

Not present if the current response doesn't add anything to previously sent [AssistAnswer.replies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-AssistAnswer#Google__Cloud__DiscoveryEngine__V1__AssistAnswer_replies_instance_ "Google::Cloud::DiscoveryEngine::V1::AssistAnswer#replies \(method\)").

Observe [AssistAnswer.state](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-AssistAnswer#Google__Cloud__DiscoveryEngine__V1__AssistAnswer_state_instance_ "Google::Cloud::DiscoveryEngine::V1::AssistAnswer#state \(method\)") to see if more parts are to be expected. While the state is `IN_PROGRESS`, the [AssistAnswer.replies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-AssistAnswer#Google__Cloud__DiscoveryEngine__V1__AssistAnswer_replies_instance_ "Google::Cloud::DiscoveryEngine::V1::AssistAnswer#replies \(method\)") field in each response will contain replies (reply fragments) to be appended to the ones received in previous responses. [AssistAnswer.name][] won't be filled.

If the state is `SUCCEEDED`, `FAILED` or `SKIPPED`, the response is the last response and [AssistAnswer.name][] will have a value. 




### #assist_token
    
    
    def assist_token() -> ::String

**Returns**

  * (::String) — A global unique ID that identifies the current pair of request and stream of responses. Used for feedback and support. 



### #assist_token=
    
    
    def assist_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A global unique ID that identifies the current pair of request and stream of responses. Used for feedback and support. 



**Returns**

  * (::String) — A global unique ID that identifies the current pair of request and stream of responses. Used for feedback and support. 



### #session_info
    
    
    def session_info() -> ::Google::Cloud::DiscoveryEngine::V1::StreamAssistResponse::SessionInfo

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::StreamAssistResponse::SessionInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-StreamAssistResponse-SessionInfo)) — Session information. 



### #session_info=
    
    
    def session_info=(value) -> ::Google::Cloud::DiscoveryEngine::V1::StreamAssistResponse::SessionInfo

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1::StreamAssistResponse::SessionInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-StreamAssistResponse-SessionInfo)) — Session information. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::StreamAssistResponse::SessionInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-StreamAssistResponse-SessionInfo)) — Session information. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
