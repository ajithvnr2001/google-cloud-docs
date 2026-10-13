---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases
title: REST Resource: projects.agent.knowledgeBases \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:11.339372+00:00
---

# REST Resource: projects.agent.knowledgeBases  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.agent.knowledgeBases Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: KnowledgeBase
    * JSON representation
  * Methods



## Resource: KnowledgeBase

A knowledge base represents a collection of knowledge documents that you provide to Dialogflow. Your knowledge documents contain information that may be useful during conversations with end-users. Some Dialogflow features use knowledge bases when looking for a response to an end-user input.

For more information, see the [knowledge base guide](https://cloud.google.com/dialogflow/docs/how/knowledge-bases).

Note: The `projects.agent.knowledgeBases` resource is deprecated; only use `projects.knowledgeBases`.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "languageCode": string
    }  
  
Fields  
---  
`name` |  `string` The knowledge base resource name. The name must be empty when creating a knowledge base. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>`.  
`displayName` |  `string` Required. The display name of the knowledge base. The name must be 1024 bytes or less; otherwise, the creation request fails.  
`languageCode` |  `string` Language which represents the KnowledgeBase. When the KnowledgeBase is created/updated, expect this to be present for non en-us languages. When unspecified, the default language code en-us applies.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases/create)`

|  Creates a knowledge base.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases/delete)`

|  Deletes the specified knowledge base.  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases/get)`

|  Retrieves the specified knowledge base.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases/list)`

|  Returns the list of all knowledge bases of the specified agent.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases/patch)`

|  Updates the specified knowledge base.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
