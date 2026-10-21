---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnswerValue/
title: AnswerValue \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:57:41.460117+00:00
---

# AnswerValue  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnswerValue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  AnswerValue Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Message for holding the value of a `[QaAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis.QaAnswer)`. `[QaQuestion.AnswerChoice](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.qaScorecards.revisions.qaQuestions#AnswerChoice)` defines the possible answer values for a question.

JSON representation  
---  
      
    
    {
      "key": string,
    
      // Union field value can be only one of the following:
      "strValue": string,
      "numValue": number,
      "boolValue": boolean,
      "naValue": boolean
      // End of list of possible types for union field value.
      "score": number,
      "potentialScore": number,
      "normalizedScore": number
    }  
  
Fields  
---  
`key` |  `string` A short string used as an identifier. Matches the value used in QaQuestion.AnswerChoice.key.  
Union field `value`. The answer value may be one of a few different types. `value` can be only one of the following:  
`strValue` |  `string` String value.  
`numValue` |  `number` Numerical value.  
`boolValue` |  `boolean` Boolean value.  
`naValue` |  `boolean` A value of "Not Applicable (N/A)". Should only ever be `true`.  
`score` |  `number` Output only. Numerical score of the answer.  
`potentialScore` |  `number` Output only. The maximum potential score of the question.  
`normalizedScore` |  `number` Output only. Normalized score of the questions. Calculated as score / potentialScore.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
