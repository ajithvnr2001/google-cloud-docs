---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels
title: REST Resource: projects.conversationModels \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:20.603744+00:00
---

# REST Resource: projects.conversationModels  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.conversationModels Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ConversationModel
    * JSON representation
    * State
    * ArticleSuggestionModelMetadata
      * JSON representation
    * ModelType
    * SmartReplyModelMetadata
      * JSON representation
  * Methods



## Resource: ConversationModel

Represents a conversation model.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "datasets": [
        {
          object ([InputDataset](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/InputDataset))
        }
      ],
      "state": enum ([State](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels#ConversationModel.State)),
      "languageCode": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "articleSuggestionModelMetadata": {
        object ([ArticleSuggestionModelMetadata](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels#ConversationModel.ArticleSuggestionModelMetadata))
      },
      "smartReplyModelMetadata": {
        object ([SmartReplyModelMetadata](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels#ConversationModel.SmartReplyModelMetadata))
      }
      // End of mutually exclusive fields.
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean
    }  
  
Fields  
---  
`name` |  `string` ConversationModel resource name. Format: `projects/<Project ID>/conversationModels/<Conversation Model ID>`  
`displayName` |  `string` Required. The display name of the model. At most 64 bytes long.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this model.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`datasets[]` |  `object (`[InputDataset](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/InputDataset)`)` Required. Datasets used to create model.  
`state` |  `enum (`[State](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels#ConversationModel.State)`)` Output only. State of the model. A model can only serve prediction requests after it gets deployed.  
`languageCode` |  `string` Language code for the conversation model. If not specified, the language is en-US. Language at ConversationModel should be set for all non en-us languages. This should be a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: "en-US".  
Required. The model metadata that is specific to the problem type. Must match the metadata type of the dataset used to train the model. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`articleSuggestionModelMetadata` |  `object (`[ArticleSuggestionModelMetadata](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels#ConversationModel.ArticleSuggestionModelMetadata)`)` Metadata for article suggestion models.  
`smartReplyModelMetadata` |  `object (`[SmartReplyModelMetadata](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels#ConversationModel.SmartReplyModelMetadata)`)` Metadata for smart reply models.  
End of mutually exclusive fields.  
`satisfiesPzs` |  `boolean` Output only. A read only boolean field reflecting Zone Separation status of the model.  
`satisfiesPzi` |  `boolean` Output only. A read only boolean field reflecting Zone Isolation status of the model.  
  
### State

State of the model.

Enums  
---  
`STATE_UNSPECIFIED` | Should not be used, an un-set enum has this value by default.  
`CREATING` | Model being created.  
`UNDEPLOYED` | Model is not deployed but ready to deploy.  
`DEPLOYING` | Model is deploying.  
`DEPLOYED` | Model is deployed and ready to use.  
`UNDEPLOYING` | Model is undeploying.  
`DELETING` | Model is deleting.  
`FAILED` | Model is in error state. Not ready to deploy and use.  
`PENDING` | Model is being created but the training has not started, The model may remain in this state until there is enough capacity to start training.  
  
### ArticleSuggestionModelMetadata

Metadata for article suggestion models.

JSON representation  
---  
      
    
    {
      "trainingModelType": enum ([ModelType](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels#ConversationModel.ModelType))
    }  
  
Fields  
---  
`trainingModelType` |  `enum (`[ModelType](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels#ConversationModel.ModelType)`)` Optional. Type of the article suggestion model. If not provided, modelType is used.  
  
### ModelType

Model type.

Enums  
---  
`MODEL_TYPE_UNSPECIFIED` | ModelType unspecified.  
`SMART_REPLY_DUAL_ENCODER_MODEL` | ModelType smart reply dual encoder model.  
`SMART_REPLY_BERT_MODEL` | ModelType smart reply bert model.  
  
### SmartReplyModelMetadata

Metadata for smart reply models.

JSON representation  
---  
      
    
    {
      "trainingModelType": enum ([ModelType](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels#ConversationModel.ModelType))
    }  
  
Fields  
---  
`trainingModelType` |  `enum (`[ModelType](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels#ConversationModel.ModelType)`)` Optional. Type of the smart reply model. If not provided, modelType is used.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels/create)`

|  Creates a model.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels/delete)`

|  Deletes a model.  
  
### `[deploy](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels/deploy)`

|  Deploys a model.  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels/get)`

|  Gets conversation model.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels/list)`

|  Lists conversation models.  
  
### `[undeploy](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationModels/undeploy)`

|  Undeploys a model.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
