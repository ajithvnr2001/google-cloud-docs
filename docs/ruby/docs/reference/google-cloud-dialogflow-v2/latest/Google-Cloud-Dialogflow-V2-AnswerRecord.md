---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnswerRecord/
title: Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::AnswerRecord (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:43.607638+00:00
---

# Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::AnswerRecord (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnswerRecord/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::AnswerRecord (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.34.0  0.33.0  0.32.2  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0 

Reference documentation and code samples for the Dialogflow V2 API class Google::Cloud::Dialogflow::V2::AnswerRecord.

Answer records are records to manage answer history and feedbacks for Dialogflow.

Currently, answer record includes:

  * human agent assistant article suggestion
  * human agent assistant faq article



It doesn't include:

  * `DetectIntent` intent matching
  * `DetectIntent` knowledge



Answer records are not related to the conversation history in the Dialogflow Console. A Record is generated even when the end-user disables conversation history in the console. Records are created when there's a human agent assistant suggestion generated.

A typical workflow for customers provide feedback to an answer is:

  1. For human agent assistant, customers get suggestion via ListSuggestions API. Together with the answers, [AnswerRecord.name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnswerRecord#Google__Cloud__Dialogflow__V2__AnswerRecord_name_instance_ "Google::Cloud::Dialogflow::V2::AnswerRecord#name \(method\)") are returned to the customers.
  2. The customer uses the [AnswerRecord.name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnswerRecord#Google__Cloud__Dialogflow__V2__AnswerRecord_name_instance_ "Google::Cloud::Dialogflow::V2::AnswerRecord#name \(method\)") to call the [AnswerRecords.UpdateAnswerRecord](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnswerRecords-Client#Google__Cloud__Dialogflow__V2__AnswerRecords__Client_update_answer_record_instance_ "Google::Cloud::Dialogflow::V2::AnswerRecords::Client#update_answer_record \(method\)") method to send feedback about a specific answer that they believe is wrong.



## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #agent_assistant_record
    
    
    def agent_assistant_record() -> ::Google::Cloud::Dialogflow::V2::AgentAssistantRecord

**Returns**

  * ([::Google::Cloud::Dialogflow::V2::AgentAssistantRecord](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AgentAssistantRecord)) — Output only. The record for human agent assistant. 



### #answer_feedback
    
    
    def answer_feedback() -> ::Google::Cloud::Dialogflow::V2::AnswerFeedback

**Returns**

  * ([::Google::Cloud::Dialogflow::V2::AnswerFeedback](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnswerFeedback)) — Required. The AnswerFeedback for this record. You can set this with [AnswerRecords.UpdateAnswerRecord](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnswerRecords-Client#Google__Cloud__Dialogflow__V2__AnswerRecords__Client_update_answer_record_instance_ "Google::Cloud::Dialogflow::V2::AnswerRecords::Client#update_answer_record \(method\)") in order to give us feedback about this answer. 



### #answer_feedback=
    
    
    def answer_feedback=(value) -> ::Google::Cloud::Dialogflow::V2::AnswerFeedback

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::V2::AnswerFeedback](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnswerFeedback)) — Required. The AnswerFeedback for this record. You can set this with [AnswerRecords.UpdateAnswerRecord](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnswerRecords-Client#Google__Cloud__Dialogflow__V2__AnswerRecords__Client_update_answer_record_instance_ "Google::Cloud::Dialogflow::V2::AnswerRecords::Client#update_answer_record \(method\)") in order to give us feedback about this answer. 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::AnswerFeedback](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnswerFeedback)) — Required. The AnswerFeedback for this record. You can set this with [AnswerRecords.UpdateAnswerRecord](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnswerRecords-Client#Google__Cloud__Dialogflow__V2__AnswerRecords__Client_update_answer_record_instance_ "Google::Cloud::Dialogflow::V2::AnswerRecords::Client#update_answer_record \(method\)") in order to give us feedback about this answer. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The unique identifier of this answer record. Format: `projects/<Project ID>/locations/<Location ID>/answerRecords/<Answer Record ID>`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The unique identifier of this answer record. Format: `projects/<Project ID>/locations/<Location ID>/answerRecords/<Answer Record ID>`. 



**Returns**

  * (::String) — The unique identifier of this answer record. Format: `projects/<Project ID>/locations/<Location ID>/answerRecords/<Answer Record ID>`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
