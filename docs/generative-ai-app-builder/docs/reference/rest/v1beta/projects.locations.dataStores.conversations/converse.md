---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.conversations/converse/
title: Method: projects.locations.dataStores.conversations.converse \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:34.762001+00:00
---

# Method: projects.locations.dataStores.conversations.converse  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.conversations/converse/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  Method: projects.locations.dataStores.conversations.converse Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Converses a conversation.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1beta/{name=projects/*/locations/*/dataStores/*/conversations/*}:converse`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the Conversation to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStoreId}/conversations/{conversationId}`. Use `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStoreId}/conversations/-` to activate auto session mode, which automatically creates a new conversation inside a conversations.converse session.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "query": {
        object ([TextInput](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.TextInput))
      },
      "servingConfig": string,
      "conversation": {
        object ([Conversation](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation))
      },
      "safeSearch": boolean,
      "userLabels": {
        string: string,
        ...
      },
      "summarySpec": {
        object ([SummarySpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/ContentSearchSpec#SummarySpec))
      },
      "filter": string,
      "boostSpec": {
        object ([BoostSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#BoostSpec))
      }
    }  
  
Fields  
---  
`query` |  `object (`[TextInput](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation.TextInput)`)` Required. Current user input.  
`servingConfig` |  `string` The resource name of the Serving Config to use. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStoreId}/servingConfigs/{servingConfigId}` If this is not set, the default serving config will be used.  
`conversation` |  `object (`[Conversation](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores.conversations#Conversation)`)` The conversation to be used by auto session only. The name field will be ignored as we automatically assign new name for the conversation in auto session.  
`safeSearch` |  `boolean` Whether to turn on safe search.  
`userLabels` |  `map (key: string, value: string)` The user labels applied to a resource must meet the following requirements:

  * Each resource can have multiple labels, up to a maximum of 64.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
  * The key portion of a label must be unique. However, you can use the same key with multiple resources.
  * Keys must start with a lowercase letter or international character.

See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details.  
`summarySpec` |  `object (`[SummarySpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/ContentSearchSpec#SummarySpec)`)` A specification for configuring the summary returned in the response.  
`filter` |  `string` The filter syntax consists of an expression language for constructing a predicate from one or more fields of the documents being filtered. Filter expression is case-sensitive. This will be used to filter search results which may affect the summary response.If this field is unrecognizable, an `INVALID_ARGUMENT` is returned.Filtering in Vertex AI Search is done by mapping the LHS filter key to a key property defined in the Vertex AI Search backend -- this mapping is defined by the customer in their schema. For example a media customer might have a field 'name' in their schema. In this case the filter would look like this: filter --> name:'ANY("king kong")'For more information about filtering including syntax and filter operators, see [Filter](https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata)  
`boostSpec` |  `object (`[BoostSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.evaluations#BoostSpec)`)` Boost specification to boost certain documents in search results which may affect the converse response. For more information on boosting, see [Boosting](https://cloud.google.com/retail/docs/boosting#boost)  
  
### Response body

If successful, the response body contains an instance of `[ConverseConversationResponse](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/ConverseConversationResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `discoveryengine.conversations.converse`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
