---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ConversationalSearchSpec/
title: ConversationalSearchSpec \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:20.667990+00:00
---

# ConversationalSearchSpec  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ConversationalSearchSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  ConversationalSearchSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * UserAnswer
    * JSON representation
  * SelectedAnswer
    * JSON representation



This field specifies all conversational related parameters addition to traditional retail search.

JSON representation  
---  
      
    
    {
      "followupConversationRequested": boolean,
      "conversationId": string,
      "userAnswer": {
        object ([UserAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ConversationalSearchSpec#UserAnswer))
      }
    }  
  
Fields  
---  
`followupConversationRequested` |  `boolean` This field specifies whether the customer would like to do conversational search. If this field is set to true, conversational related extra information will be returned from server side, including follow-up question, answer options, etc.  
`conversationId` |  `string` This field specifies the conversation id, which maintains the state of the conversation between client side and server side. Use the value from the previous `[SearchResponse.ConversationalSearchResult.conversation_id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#ConversationalSearchResult.FIELDS.conversation_id)`. For the initial request, this should be empty.  
`userAnswer` |  `object (`[UserAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ConversationalSearchSpec#UserAnswer)`)` This field specifies the current user answer during the conversational search. This can be either user selected from suggested answers or user input plain text.  
  
## UserAnswer

This field specifies the current user answer during the conversational search. This can be either user selected from suggested answers or user input plain text.

JSON representation  
---  
      
    
    {
    
      // Union field type can be only one of the following:
      "textAnswer": string,
      "selectedAnswer": {
        object ([SelectedAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ConversationalSearchSpec#SelectedAnswer))
      }
      // End of list of possible types for union field type.
    }  
  
Fields  
---  
Union field `type`. This field specifies the type of user answer. `type` can be only one of the following:  
`textAnswer` |  `string` This field specifies the incremental input text from the user during the conversational search.  
`selectedAnswer` |  `object (`[SelectedAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ConversationalSearchSpec#SelectedAnswer)`)` This field specifies the selected attributes during the conversational search. This should be a subset of `[SearchResponse.ConversationalSearchResult.suggested_answers](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/SearchResponse#ConversationalSearchResult.FIELDS.suggested_answers)`.  
  
## SelectedAnswer

This field specifies the selected answers during the conversational search.

JSON representation  
---  
      
    
    {
      "productAttributeValues": [
        {
          object ([ProductAttributeValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ProductAttributeValue))
        }
      ],
      "productAttributeValue": {
        object ([ProductAttributeValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ProductAttributeValue))
      }
    }  
  
Fields  
---  
`productAttributeValues[]  
**(deprecated)**` |  `object (`[ProductAttributeValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ProductAttributeValue)`)` This item is deprecated!This field is deprecated and should not be set.  
`productAttributeValue` |  `object (`[ProductAttributeValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ProductAttributeValue)`)` This field specifies the selected answer which is a attribute key-value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
