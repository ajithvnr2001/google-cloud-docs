---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets
title: REST Resource: projects.conversationDatasets \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:17.908731+00:00
---

# REST Resource: projects.conversationDatasets  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.conversationDatasets Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ConversationDataset
    * JSON representation
    * InputConfig
      * JSON representation
    * GcsSources
      * JSON representation
    * ConversationInfo
      * JSON representation
  * Methods



## Resource: ConversationDataset

Represents a conversation dataset that a user imports raw data into. The data inside ConversationDataset can not be changed after conversationDatasets.importConversationData finishes (and calling conversationDatasets.importConversationData on a dataset that already has data is not allowed).

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "createTime": string,
      "inputConfig": {
        object ([InputConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets#ConversationDataset.InputConfig))
      },
      "conversationInfo": {
        object ([ConversationInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets#ConversationDataset.ConversationInfo))
      },
      "conversationCount": string,
      "satisfiesPzi": boolean,
      "satisfiesPzs": boolean
    }  
  
Fields  
---  
`name` |  `string` Output only. ConversationDataset resource name. Format: `projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset ID>`  
`displayName` |  `string` Required. The display name of the dataset. Maximum of 64 bytes.  
`description` |  `string` Optional. The description of the dataset. Maximum of 10000 bytes.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this dataset.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`inputConfig` |  `object (`[InputConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets#ConversationDataset.InputConfig)`)` Output only. Input configurations set during conversation data import.  
`conversationInfo` |  `object (`[ConversationInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets#ConversationDataset.ConversationInfo)`)` Output only. Metadata set during conversation data import.  
`conversationCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of conversations this conversation dataset contains.  
`satisfiesPzi` |  `boolean` Output only. A read only boolean field reflecting Zone Isolation status of the dataset.  
`satisfiesPzs` |  `boolean` Output only. A read only boolean field reflecting Zone Separation status of the dataset.  
  
### InputConfig

Represents the configuration of importing a set of conversation files in Google Cloud Storage.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsSource": {
        object ([GcsSources](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets#ConversationDataset.GcsSources))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Required. Where the data is from. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsSource` |  `object (`[GcsSources](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets#ConversationDataset.GcsSources)`)` The Cloud Storage URI has the form gs:////agent*.json. Wildcards are allowed and will be expanded into all matched JSON files, which will be read as one conversation per file.  
End of mutually exclusive fields.  
  
### GcsSources

Google Cloud Storage location for the inputs.

JSON representation  
---  
      
    
    {
      "uris": [
        string
      ]
    }  
  
Fields  
---  
`uris[]` |  `string` Required. Google Cloud Storage URIs for the inputs. A URI is of the form: `gs://bucket/object-prefix-or-name` Whether a prefix or name is used depends on the use case.  
  
### ConversationInfo

Represents metadata of a conversation.

JSON representation  
---  
      
    
    {
      "languageCode": string
    }  
  
Fields  
---  
`languageCode` |  `string` Optional. The language code of the conversation data within this dataset. See <https://cloud.google.com/apis/design/standard_fields> for more information. Supports all UTF-8 languages.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets/get)`

|  Retrieves the specified conversation dataset.  
  
### `[importConversationData](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets/importConversationData)`

|  Import data into the specified conversation dataset.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets/list)`

|  Returns the list of all conversation datasets in the specified project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
