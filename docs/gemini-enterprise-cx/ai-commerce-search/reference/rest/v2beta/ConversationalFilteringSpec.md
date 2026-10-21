---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ConversationalFilteringSpec/
title: ConversationalFilteringSpec \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:18:27.277634+00:00
---

# ConversationalFilteringSpec  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ConversationalFilteringSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  ConversationalFilteringSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * UserAnswer
    * JSON representation
  * SelectedAnswer
    * JSON representation
  * Mode



This field specifies all conversational filtering related parameters addition to conversational retail search.

JSON representation  
---  
      
    
    {
      "enableConversationalFiltering": boolean,
      "userAnswer": {
        object ([UserAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ConversationalFilteringSpec#UserAnswer))
      },
      "conversationalFilteringMode": enum ([Mode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ConversationalFilteringSpec#Mode))
    }  
  
Fields  
---  
`enableConversationalFiltering  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. This field is deprecated. Please use `[ConversationalFilteringSpec.conversational_filtering_mode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ConversationalFilteringSpec#FIELDS.conversational_filtering_mode)` instead.  
`userAnswer` |  `object (`[UserAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ConversationalFilteringSpec#UserAnswer)`)` Optional. This field specifies the current user answer during the conversational filtering search. It can be either user selected from suggested answers or user input plain text.  
`conversationalFilteringMode` |  `enum (`[Mode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ConversationalFilteringSpec#Mode)`)` Optional. Mode to control Conversational Filtering. Defaults to `[Mode.DISABLED](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ConversationalFilteringSpec#Mode.ENUM_VALUES.DISABLED)` if it's unset.  
  
## UserAnswer

This field specifies the current user answer during the conversational filtering search. This can be either user selected from suggested answers or user input plain text.

JSON representation  
---  
      
    
    {
    
      // Union field type can be only one of the following:
      "textAnswer": string,
      "selectedAnswer": {
        object ([SelectedAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ConversationalFilteringSpec#SelectedAnswer))
      }
      // End of list of possible types for union field type.
    }  
  
Fields  
---  
Union field `type`. This field specifies the type of user answer. `type` can be only one of the following:  
`textAnswer` |  `string` This field specifies the incremental input text from the user during the conversational search.  
`selectedAnswer` |  `object (`[SelectedAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ConversationalFilteringSpec#SelectedAnswer)`)` Optional. This field specifies the selected answer during the conversational search. This should be a subset of `[ConversationalSearchResponse.FollowupQuestion.SuggestedAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ConversationalSearchResponse#SuggestedAnswer)`.  
  
## SelectedAnswer

This field specifies the selected answers during the conversational search.

JSON representation  
---  
      
    
    {
      "productAttributeValue": {
        object ([ProductAttributeValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ProductAttributeValue))
      },
      "productAttributeInterval": {
        object ([ProductAttributeInterval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ProductAttributeInterval))
      }
    }  
  
Fields  
---  
`productAttributeValue` |  `object (`[ProductAttributeValue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ProductAttributeValue)`)` Optional. This field specifies the selected answer which is a attribute key-value.  
`productAttributeInterval` |  `object (`[ProductAttributeInterval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ProductAttributeInterval)`)` Optional. This is an experimental feature. Please contact Google before using it. This field specifies the selected answer which is a attribute key-numeric interval.  
  
## Mode

Enum to control Conversational Filtering mode. A single conversation session including multiple turns supports modes for Conversational Search OR Conversational Filtering without Conversational Search, but not both.

Enums  
---  
`MODE_UNSPECIFIED` | Default value.  
`DISABLED` | Disables Conversational Filtering when using Conversational Search.  
`ENABLED` | Enables Conversational Filtering when using Conversational Search.  
`CONVERSATIONAL_FILTER_ONLY` | Enables Conversational Filtering without Conversational Search.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
