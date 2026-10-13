---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations
title: REST Resource: projects.conversationModels.evaluations \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:19.659045+00:00
---

# REST Resource: projects.conversationModels.evaluations  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.conversationModels.evaluations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ConversationModelEvaluation
    * JSON representation
    * EvaluationConfig
      * JSON representation
    * SmartReplyConfig
      * JSON representation
    * SmartComposeConfig
      * JSON representation
    * SmartReplyMetrics
      * JSON representation
    * TopNMetrics
      * JSON representation
  * Methods



## Resource: ConversationModelEvaluation

Represents evaluation result of a conversation model.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "evaluationConfig": {
        object ([EvaluationConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations#ConversationModelEvaluation.EvaluationConfig))
      },
      "createTime": string,
      "rawHumanEvalTemplateCsv": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "smartReplyMetrics": {
        object ([SmartReplyMetrics](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations#ConversationModelEvaluation.SmartReplyMetrics))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` The resource name of the evaluation. Format: `projects/<Project ID>/conversationModels/<Conversation Model ID>/evaluations/<Evaluation ID>`  
`displayName` |  `string` Optional. The display name of the model evaluation. At most 64 bytes long.  
`evaluationConfig` |  `object (`[EvaluationConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations#ConversationModelEvaluation.EvaluationConfig)`)` Optional. The configuration of the evaluation task.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this model.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`rawHumanEvalTemplateCsv` |  `string` Output only. Human eval template in csv format. It takes real-world conversations provided through input dataset, generates example suggestions for customer to verify quality of the model. For Smart Reply, the generated csv file contains columns of Context, (Suggestions,Q1,Q2)*3, Actual reply. Context contains at most 10 latest messages in the conversation prior to the current suggestion. Q1: "Would you send it as the next message of agent?" Evaluated based on whether the suggest is appropriate to be sent by agent in current context. Q2: "Does the suggestion move the conversation closer to resolution?" Evaluated based on whether the suggestion provide solutions, or answers customer's question or collect information from customer to resolve the customer's issue. Actual reply column contains the actual agent reply sent in the context.  
Metrics details. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`smartReplyMetrics` |  `object (`[SmartReplyMetrics](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations#ConversationModelEvaluation.SmartReplyMetrics)`)` Output only. Only available when model is for smart reply.  
End of mutually exclusive fields.  
  
### EvaluationConfig

The configuration for model evaluation.

JSON representation  
---  
      
    
    {
      "datasets": [
        {
          object ([InputDataset](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/InputDataset))
        }
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "smartReplyConfig": {
        object ([SmartReplyConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations#ConversationModelEvaluation.SmartReplyConfig))
      },
      "smartComposeConfig": {
        object ([SmartComposeConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations#ConversationModelEvaluation.SmartComposeConfig))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`datasets[]` |  `object (`[InputDataset](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/InputDataset)`)` Required. Datasets used for evaluation.  
Specific configurations for different models in order to do evaluation. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`smartReplyConfig` |  `object (`[SmartReplyConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations#ConversationModelEvaluation.SmartReplyConfig)`)` Configuration for smart reply model evaluation.  
`smartComposeConfig` |  `object (`[SmartComposeConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations#ConversationModelEvaluation.SmartComposeConfig)`)` Configuration for smart compose model evaluation.  
End of mutually exclusive fields.  
  
### SmartReplyConfig

Smart reply specific configuration for evaluation job.

JSON representation  
---  
      
    
    {
      "allowlistDocument": string,
      "maxResultCount": integer
    }  
  
Fields  
---  
`allowlistDocument` |  `string` The allowlist document resource name. Format: `projects/<Project ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>`. Only used for smart reply model.  
`maxResultCount` |  `integer` Required. The model to be evaluated can return multiple results with confidence score on each query. These results will be sorted by the descending order of the scores and we only keep the first maxResultCount results as the final results to evaluate.  
  
### SmartComposeConfig

Smart compose specific configuration for evaluation job.

JSON representation  
---  
      
    
    {
      "allowlistDocument": string,
      "maxResultCount": integer
    }  
  
Fields  
---  
`allowlistDocument` |  `string` The allowlist document resource name. Format: `projects/<Project ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>`. Only used for smart compose model.  
`maxResultCount` |  `integer` Required. The model to be evaluated can return multiple results with confidence score on each query. These results will be sorted by the descending order of the scores and we only keep the first maxResultCount results as the final results to evaluate.  
  
### SmartReplyMetrics

The evaluation metrics for smart reply model.

JSON representation  
---  
      
    
    {
      "allowlistCoverage": number,
      "topNMetrics": [
        {
          object ([TopNMetrics](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations#ConversationModelEvaluation.TopNMetrics))
        }
      ],
      "conversationCount": string
    }  
  
Fields  
---  
`allowlistCoverage` |  `number` Percentage of target participant messages in the evaluation dataset for which similar messages have appeared at least once in the allowlist. Should be [0, 1].  
`topNMetrics[]` |  `object (`[TopNMetrics](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations#ConversationModelEvaluation.TopNMetrics)`)` Metrics of top n smart replies, sorted by [TopNMetric.n][].  
`conversationCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total number of conversations used to generate this metric.  
  
### TopNMetrics

Evaluation metrics when retrieving `n` smart replies with the model.

JSON representation  
---  
      
    
    {
      "n": integer,
      "recall": number
    }  
  
Fields  
---  
`n` |  `integer` Number of retrieved smart replies. For example, when `n` is 3, this evaluation contains metrics for when Dialogflow retrieves 3 smart replies with the model.  
`recall` |  `number` Defined as `number of queries whose top n smart replies have at least one similar (token match similarity above the defined threshold) reply as the real reply` divided by `number of queries with at least one smart reply`. Value ranges from 0.0 to 1.0 inclusive.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations/get)`

|  Gets an evaluation of conversation model.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels.evaluations/list)`

|  Lists evaluations of a conversation model.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
