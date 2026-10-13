---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestKnowledgeAssistRequest/
title: Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistRequest (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:44.725250+00:00
---

# Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistRequest (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestKnowledgeAssistRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistRequest (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.34.0  0.33.0  0.32.2  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0 

Reference documentation and code samples for the Dialogflow V2 API class Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistRequest.

The request message for [Participants.SuggestKnowledgeAssist](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participants-Client#Google__Cloud__Dialogflow__V2__Participants__Client_suggest_knowledge_assist_instance_ "Google::Cloud::Dialogflow::V2::Participants::Client#suggest_knowledge_assist \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #context_size
    
    
    def context_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. Max number of messages prior to and including [latest_message](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestKnowledgeAssistRequest#Google__Cloud__Dialogflow__V2__SuggestKnowledgeAssistRequest_latest_message_instance_ "Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistRequest#latest_message \(method\)") to use as context when compiling the suggestion. The context size is by default 100 and at most 100. 



### #context_size=
    
    
    def context_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Max number of messages prior to and including [latest_message](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestKnowledgeAssistRequest#Google__Cloud__Dialogflow__V2__SuggestKnowledgeAssistRequest_latest_message_instance_ "Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistRequest#latest_message \(method\)") to use as context when compiling the suggestion. The context size is by default 100 and at most 100. 



**Returns**

  * (::Integer) — Optional. Max number of messages prior to and including [latest_message](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestKnowledgeAssistRequest#Google__Cloud__Dialogflow__V2__SuggestKnowledgeAssistRequest_latest_message_instance_ "Google::Cloud::Dialogflow::V2::SuggestKnowledgeAssistRequest#latest_message \(method\)") to use as context when compiling the suggestion. The context size is by default 100 and at most 100. 



### #latest_message
    
    
    def latest_message() -> ::String

**Returns**

  * (::String) — Optional. The name of the latest conversation message to compile suggestions for. If empty, it will be the latest message of the conversation. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>`. 



### #latest_message=
    
    
    def latest_message=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The name of the latest conversation message to compile suggestions for. If empty, it will be the latest message of the conversation. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>`. 



**Returns**

  * (::String) — Optional. The name of the latest conversation message to compile suggestions for. If empty, it will be the latest message of the conversation. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>`. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The name of the participant to fetch suggestions for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the participant to fetch suggestions for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`. 



**Returns**

  * (::String) — Required. The name of the participant to fetch suggestions for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`. 



### #previous_suggested_query
    
    
    def previous_suggested_query() -> ::String

**Returns**

  * (::String) — Optional. The previously suggested query for the given conversation. This helps identify whether the next suggestion we generate is reasonably different from the previous one. This is useful to avoid similar suggestions within the conversation. 



### #previous_suggested_query=
    
    
    def previous_suggested_query=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The previously suggested query for the given conversation. This helps identify whether the next suggestion we generate is reasonably different from the previous one. This is useful to avoid similar suggestions within the conversation. 



**Returns**

  * (::String) — Optional. The previously suggested query for the given conversation. This helps identify whether the next suggestion we generate is reasonably different from the previous one. This is useful to avoid similar suggestions within the conversation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
