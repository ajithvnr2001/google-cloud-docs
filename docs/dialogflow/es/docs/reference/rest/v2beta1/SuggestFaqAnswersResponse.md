---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SuggestFaqAnswersResponse/
title: SuggestFaqAnswersResponse \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:10.929061+00:00
---

# SuggestFaqAnswersResponse  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SuggestFaqAnswersResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  SuggestFaqAnswersResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The request message for `[Participants.SuggestFaqAnswers](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants.suggestions/suggestFaqAnswers#google.cloud.dialogflow.v2beta1.Participants.SuggestFaqAnswers)`.

JSON representation  
---  
      
    
    {
      "faqAnswers": [
        {
          object ([FaqAnswer](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.FaqAnswer))
        }
      ],
      "latestMessage": string,
      "contextSize": integer
    }  
  
Fields  
---  
`faqAnswers[]` |  `object (`[FaqAnswer](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.FaqAnswer)`)` Output only. Answers extracted from FAQ documents.  
`latestMessage` |  `string` The name of the latest conversation message used to compile suggestion for.Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>`.  
`contextSize` |  `integer` Number of messages prior to and including `[latestMessage](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SuggestFaqAnswersResponse#FIELDS.latest_message)` to compile the suggestion. It may be smaller than the `[SuggestFaqAnswersRequest.context_size](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants.suggestions/suggestFaqAnswers#body.request_body.FIELDS.context_size)` field in the request if there aren't that many messages in the conversation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
