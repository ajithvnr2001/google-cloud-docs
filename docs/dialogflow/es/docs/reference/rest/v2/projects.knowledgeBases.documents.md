---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents
title: REST Resource: projects.knowledgeBases.documents \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:27.485292+00:00
---

# REST Resource: projects.knowledgeBases.documents  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.knowledgeBases.documents Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Document
    * JSON representation
  * Methods



## Resource: Document

A knowledge document to be used by a `[KnowledgeBase](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases#KnowledgeBase)`.

For more information, see the [knowledge base guide](https://cloud.google.com/dialogflow/docs/how/knowledge-bases).

Note: The `projects.agent.knowledgeBases.documents` resource is deprecated; only use `projects.knowledgeBases.documents`.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "mimeType": string,
      "knowledgeTypes": [
        enum ([KnowledgeType](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases.documents#Document.KnowledgeType))
      ],
      "enableAutoReload": boolean,
      "latestReloadStatus": {
        object ([ReloadStatus](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases.documents#Document.ReloadStatus))
      },
      "metadata": {
        string: string,
        ...
      },
      "state": enum ([State](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases.documents#Document.State)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "contentUri": string,
      "rawContent": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Optional. The document resource name. The name must be empty when creating a document. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>`.  
`displayName` |  `string` Required. The display name of the document. The name must be 1024 bytes or less; otherwise, the creation request fails.  
`mimeType` |  `string` Required. The MIME type of this document.  
`knowledgeTypes[]` |  `enum (`[KnowledgeType](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases.documents#Document.KnowledgeType)`)` Required. The knowledge type of document content.  
`enableAutoReload` |  `boolean` Optional. If true, we try to automatically reload the document every day (at a time picked by the system). If false or unspecified, we don't try to automatically reload the document.Currently you can only enable automatic reload for documents sourced from a public url, see `source` field for the source types.Reload status can be tracked in `latestReloadStatus`. If a reload fails, we will keep the document unchanged.If a reload fails with internal errors, the system will try to reload the document on the next day. If a reload fails with non-retriable errors (e.g. PERMISSION_DENIED), the system will not try to reload the document anymore. You need to manually reload the document successfully by calling `documents.reload` and clear the errors.  
`latestReloadStatus` |  `object (`[ReloadStatus](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases.documents#Document.ReloadStatus)`)` Output only. The time and status of the latest reload. This reload may have been triggered automatically or manually and may not have succeeded.  
`metadata` |  `map (key: string, value: string)` Optional. Metadata for the document. The metadata supports arbitrary key-value pairs. Suggested use cases include storing a document's title, an external URL distinct from the document's contentUri, etc. The max size of a `key` or a `value` of the metadata is 1024 bytes.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases.documents#Document.State)`)` Output only. The current state of the document.  
Required. The source of this document. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`contentUri` |  `string` The URI where the file content is located.For documents stored in Google Cloud Storage, these URIs must have the form `gs://<bucket-name>/<object-name>`.NOTE: External URLs must correspond to public webpages, i.e., they must be indexed by Google Search. In particular, URLs for showing documents in Google Cloud Storage (i.e. the URL in your browser) are not supported. Instead use the `gs://` format URI described above.  
`rawContent` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The raw content of the document. This field is only permitted for EXTRACTIVE_QA and FAQ knowledge types.A base64-encoded string.  
End of mutually exclusive fields.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/create)`

|  Creates a new document.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/delete)`

|  Deletes the specified document.  
  
### `[export](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/export)`

|  Exports a smart messaging candidate document into the specified destination.  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/get)`

|  Retrieves the specified document.  
  
### `[import](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/import)`

|  Creates documents by importing data from external sources.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/list)`

|  Returns the list of all documents of the knowledge base.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/patch)`

|  Updates the specified document.  
  
### `[reload](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/reload)`

|  Reloads the specified document from its specified source, content_uri or content.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
