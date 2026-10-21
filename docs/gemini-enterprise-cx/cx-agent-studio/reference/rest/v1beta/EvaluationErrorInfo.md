---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationErrorInfo/
title: EvaluationErrorInfo \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:13:53.900295+00:00
---

# EvaluationErrorInfo  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationErrorInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  EvaluationErrorInfo Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * EvaluationErrorInfo.ErrorType



Information about an error encountered during an evaluation execution.

JSON representation  
---  
      
    
    {
      "errorType": enum ([EvaluationErrorInfo.ErrorType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationErrorInfo#EvaluationErrorInfo.ErrorType)),
      "errorMessage": string,
      "sessionId": string,
      "userFacingErrorMessage": string
    }  
  
Fields  
---  
`errorType` |  `enum (`[EvaluationErrorInfo.ErrorType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationErrorInfo#EvaluationErrorInfo.ErrorType)`)` Output only. The type of error.  
`errorMessage` |  `string` Output only. The error message.  
`sessionId` |  `string` Output only. The session ID for the conversation that caused the error.  
`userFacingErrorMessage` |  `string` Output only. The user facing error message.  
  
## EvaluationErrorInfo.ErrorType

The type of error

Enums  
---  
`ERROR_TYPE_UNSPECIFIED` | Unspecified error type.  
`RUNTIME_FAILURE` | Failure during runtime execution.  
`CONVERSATION_RETRIEVAL_FAILURE` | Failure to retrieve conversation from CES Runtime.  
`METRIC_CALCULATION_FAILURE` | Failure to calculate a metric / outcome.  
`EVALUATION_UPDATE_FAILURE` | Failure to update the evaluation.  
`QUOTA_EXHAUSTED` | Ran out of quota.  
`USER_SIMULATION_FAILURE` | Failure during user simulation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
