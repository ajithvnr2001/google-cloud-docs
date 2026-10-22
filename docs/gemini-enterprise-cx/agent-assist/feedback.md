---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/feedback/
title: Send feedback to Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:57.304245+00:00
---

# Send feedback to Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/feedback/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Send feedback to Agent Assist Stay organized with collections  Save and categorize content based on your preferences. 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide describes how to send feedback to Agent Assist about the quality of a specific suggested answer. This information is used to improve the quality of your suggested answers in the future.

## Feedback types

Feedback falls into one of two categories. Information about both feedback types is conveyed by fields in an [`answerFeedback`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.answerRecords#answerfeedback) object:

  1. **Implicit feedback:** Whether or not an agent clicked on a suggested answer. This information is contained in the boolean `clicked` field.
  2. **Explicit feedback:** The level of correctness of the answer or other detailed information about the answer, provided by the agent. Level of correctness is conveyed by the `correctnessLevel` field. Optionally, additional details can be added to the `agentAssistDetailFeedback` field as an [`AgentAssistantFeedback`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2#agentassistantfeedback) object.



## Send feedback to Agent Assist

There is an `Answers` field in every Agent Assist response (for example, [`faqAnswers`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/SuggestFaqAnswersResponse#FaqAnswer), [`articleAnswers`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/SuggestArticlesResponse#articleanswer), and [`smartReplyAnswers`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/SuggestSmartRepliesResponse)). To provide feedback about an answer, find the resource name of the answer record. The resource name has the format "projects/project-id/answerRecords/answer-record-id". Use the answer record to call the [`UpdateAnswerRecord`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2#google.cloud.dialogflow.v2.AnswerRecords.UpdateAnswerRecord) method to send [`AnswerFeedback`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2#google.cloud.dialogflow.v2.AnswerFeedback) about the answer.

### Generative knowledge assist

Generative knowledge assist can either answer agent questions or proactively suggest question and answer pairs. These two features require different JSON requests for sending feedback.

Use the answer record to call the [`UpdateAnswerRecord`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2beta1#google.cloud.dialogflow.v2beta1.AnswerRecords.UpdateAnswerRecord) method to send [`AnswerFeedback`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2beta1#google.cloud.dialogflow.v2beta1.AnswerFeedback) to indicate possible feedback events:

  * `displayed`: Whether the suggestion is displayed to the human agent.
  * `clicked`: Whether the suggestion is clicked by the human agent.
  * `correctness_level`: Whether the suggestion is correct or not. A typical use case is to provide thumbs up and thumbs down buttons for the human agent to provide feedback.
  * `answer_copied`: Whether the answer is copied by the human agent.
  * `clicked_uris`: The URIs clicked by the human agent.



### Smart reply

Use the answer record to call the [`UpdateAnswerRecord`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2#google.cloud.dialogflow.v2.AnswerRecords.UpdateAnswerRecord) method to send [`AnswerFeedback`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2#google.cloud.dialogflow.v2.AnswerFeedback) to indicate two feedback events:

  1. **displayed** : a suggestion (identified by `answer-record-id` returned in the Smart Reply suggestions) was displayed in the agent UI.
  2. **clicked** : a suggestion (identified by `answer-record-id` returned in the Smart Reply suggestions) was clicked by the agent.



The suggestion was displayed to the agent. 
    
    
    curl -X PATCH   
    
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)"   
    
         -H "x-goog-user-project: quota-project-id"   
    
         -H "Content-Type: application/json" -d   
    
    '{
      "name": "projects/project-id/answerRecords/answer-record-id",
      "answerFeedback": {
        "displayed": true
      }
    }' https://dialogflow.googleapis.com/v2/projects/project-id/answerRecords/answer-record-id?updateMask=answer_feedback
    

The suggestion was clicked by the agent. 
    
    
    curl -X PATCH   
    
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)"   
    
         -H "x-goog-user-project: quota-project-id"   
    
         -H "Content-Type: application/json" -d   
    
    '{
      "name": "projects/project-id/answerRecords/answer-record-id",
      "answerFeedback": {
        "clicked": true
      }
    }' https://dialogflow.googleapis.com/v2/projects/project-id/answerRecords/answer-record-id?updateMask=answer_feedback
    

### Article suggestion and FAQ assist

The following sample demonstrates how to send direct feedback from an agent in response to the agent being asked about suggestion correctness. The `correctnessLevel` field can be one of `FULLY_CORRECT`, `PARTIALLY_CORRECT`, `NOT_CORRECT`, `CORRECTNESS_LEVEL_UNSPECIFIED`.
    
    
    curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "x-goog-user-project: quota-project-id" \
         -H "Content-Type: application/json" -d \
    '{
      "name": "projects/project-id/answerRecords/answer-record-id",
      "answerFeedback": {
        "correctnessLevel": "FULLY_CORRECT",
        "agentAssistantDetailFeedback": {},
        "clicked": true
      }
    }' https://dialogflow.googleapis.com/v2/projects/project-id/answerRecords/answer-record-id?updateMask=answer_feedback
    

The following sample demonstrates how to send click-only indirect feedback:
    
    
    curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "x-goog-user-project: quota-project-id" \
         -H "Content-Type: application/json" -d \
    '{
      "name": "projects/project-id/answerRecords/answer-record-id",
      "answerFeedback": {
        "clicked": true
      }
    }' https://dialogflow.googleapis.com/v2/projects/project-id/answerRecords/answer-record-id?updateMask=answer_feedback
    

### Summarization

Summarization uses feedback to calculate the duration spent on reviewing or editing a summary and edit rate.
    
    
    curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "x-goog-user-project: quota-project-id" \
         -H "Content-Type: application/json" -d \
    '{
      "name": "projects/project-id/answerRecords/answer-record-id",
      "answerFeedback": {
        "agentAssistantDetailFeedback": {
          "summarizationFeedback": {
            "startTimestamp": "2022-10-15T02:10:11.414Z",
            "submitTimestamp": "2022-10-15T02:12:41.000012345Z",
            "summaryText": "submitted summary"
          }
        }
      }
    }' \
    https://dialogflow.googleapis.com/v2beta1/projects/project-id/answerRecords/answer-record-id?updateMask=answer_feedback.agent_assistant_detail_feedback.summarization_feedback
    

Summarization feedback also supports updating summaries within each section. Note: Only one field should be updated at a time, either `summarizationFeedback.summaryText` or `summarizationFeedback.textSections`.
    
    
    curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "x-goog-user-project: quota-project-id" \
         -H "Content-Type: application/json" -d \
    '{
      "name": "projects/project-id/answerRecords/answer-record-id",
      "answerFeedback": {
        "agentAssistantDetailFeedback": {
          "summarizationFeedback": {
            "startTimestamp": "2022-10-15T02:10:11.414Z",
            "submitTimestamp": "2022-10-15T02:12:41.000012345Z",
            "textSections": {
              "section a": "section a summary",
              "section b": "section b summary"
            }
          }
        }
      }
    }' \
    https://dialogflow.googleapis.com/v2beta1/projects/project-id/answerRecords/answer-record-id?updateMask=answer_feedback.agent_assistant_detail_feedback.summarization_feedback
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
