---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Dimension/
title: Dimension \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:57:07.104554+00:00
---

# Dimension  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Dimension/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Dimension Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * IssueDimensionMetadata
    * JSON representation
  * AgentDimensionMetadata
    * JSON representation
  * QaQuestionDimensionMetadata
    * JSON representation
  * QaQuestionAnswerDimensionMetadata
    * JSON representation
  * DimensionKey



A dimension determines the grouping key for the query. In SQL terms, these would be part of both the "SELECT" and "GROUP BY" clauses.

JSON representation  
---  
      
    
    {
      "dimensionKey": enum ([DimensionKey](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Dimension#DimensionKey)),
    
      // Union field dimension_metadata can be only one of the following:
      "issueDimensionMetadata": {
        object ([IssueDimensionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Dimension#IssueDimensionMetadata))
      },
      "agentDimensionMetadata": {
        object ([AgentDimensionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Dimension#AgentDimensionMetadata))
      },
      "qaQuestionDimensionMetadata": {
        object ([QaQuestionDimensionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Dimension#QaQuestionDimensionMetadata))
      },
      "qaQuestionAnswerDimensionMetadata": {
        object ([QaQuestionAnswerDimensionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Dimension#QaQuestionAnswerDimensionMetadata))
      }
      // End of list of possible types for union field dimension_metadata.
    }  
  
Fields  
---  
`dimensionKey` |  `enum (`[DimensionKey](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Dimension#DimensionKey)`)` The key of the dimension.  
Union field `dimension_metadata`. Output-only metadata about the dimension. `dimension_metadata` can be only one of the following:  
`issueDimensionMetadata` |  `object (`[IssueDimensionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Dimension#IssueDimensionMetadata)`)` Output only. Metadata about the issue dimension.  
`agentDimensionMetadata` |  `object (`[AgentDimensionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Dimension#AgentDimensionMetadata)`)` Output only. Metadata about the agent dimension.  
`qaQuestionDimensionMetadata` |  `object (`[QaQuestionDimensionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Dimension#QaQuestionDimensionMetadata)`)` Output only. Metadata about the QA question dimension.  
`qaQuestionAnswerDimensionMetadata` |  `object (`[QaQuestionAnswerDimensionMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Dimension#QaQuestionAnswerDimensionMetadata)`)` Output only. Metadata about the QA question-answer dimension.  
  
## IssueDimensionMetadata

Metadata about the issue dimension.

JSON representation  
---  
      
    
    {
      "issueId": string,
      "issueDisplayName": string,
      "issueModelId": string
    }  
  
Fields  
---  
`issueId` |  `string` The issue ID.  
`issueDisplayName` |  `string` The issue display name.  
`issueModelId` |  `string` The parent issue model ID.  
  
## AgentDimensionMetadata

Metadata about the agent dimension.

JSON representation  
---  
      
    
    {
      "agentId": string,
      "agentDisplayName": string,
      "agentTeam": string
    }  
  
Fields  
---  
`agentId` |  `string` Optional. A user-specified string representing the agent.  
`agentDisplayName` |  `string` Optional. The agent's name  
`agentTeam` |  `string` Optional. A user-specified string representing the agent's team.  
  
## QaQuestionDimensionMetadata

Metadata about the QA question dimension.

JSON representation  
---  
      
    
    {
      "qaScorecardId": string,
      "qaQuestionId": string,
      "questionBody": string
    }  
  
Fields  
---  
`qaScorecardId` |  `string` Optional. The QA scorecard ID.  
`qaQuestionId` |  `string` Optional. The QA question ID.  
`questionBody` |  `string` Optional. The full body of the question.  
  
## QaQuestionAnswerDimensionMetadata

Metadata about the QA question-answer dimension. This is useful for showing the answer distribution for questions for a given scorecard.

JSON representation  
---  
      
    
    {
      "qaScorecardId": string,
      "qaQuestionId": string,
      "questionBody": string,
      "answerValue": string
    }  
  
Fields  
---  
`qaScorecardId` |  `string` Optional. The QA scorecard ID.  
`qaQuestionId` |  `string` Optional. The QA question ID.  
`questionBody` |  `string` Optional. The full body of the question.  
`answerValue` |  `string` Optional. The full body of the question.  
  
## DimensionKey

The key of the dimension.

Enums  
---  
`DIMENSION_KEY_UNSPECIFIED` | The key of the dimension is unspecified.  
`ISSUE` | The dimension is keyed by issues.  
`ISSUE_NAME` | The dimension is keyed by issue names.  
`AGENT` | The dimension is keyed by agents.  
`AGENT_TEAM` | The dimension is keyed by agent teams.  
`QA_QUESTION_ID` | The dimension is keyed by QaQuestionIds. Note that: We only group by the QuestionId and not the revision-id of the scorecard this question is a part of. This allows for showing stats for the same question across different scorecard revisions.  
`QA_QUESTION_ANSWER_VALUE` | The dimension is keyed by QaQuestionIds-Answer value pairs. Note that: We only group by the QuestionId and not the revision-id of the scorecard this question is a part of. This allows for showing distribution of answers per question across different scorecard revisions.  
`CONVERSATION_PROFILE_ID` | The dimension is keyed by the conversation profile ID.  
`MEDIUM` | The dimension is keyed by the conversation medium.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
