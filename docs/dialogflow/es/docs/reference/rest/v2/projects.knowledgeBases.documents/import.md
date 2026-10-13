---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/import/
title: Method: projects.knowledgeBases.documents.import \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:28.294349+00:00
---

# Method: projects.knowledgeBases.documents.import  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.knowledgeBases.documents.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Creates documents by importing data from external sources. Dialogflow supports up to 350 documents in each request. If you try to import more, Dialogflow will return an error.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: `[KnowledgeOperationMetadata](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/KnowledgeOperationMetadata)`
  * `response`: `[ImportDocumentsResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ImportDocumentsResponse)`



### HTTP request

`POST https://{endpoint}/v2/{parent=projects/*/knowledgeBases/*}/documents:import`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The knowledge base to import documents into. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.documents.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "documentTemplate": {
        object ([ImportDocumentTemplate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ImportDocumentTemplate))
      },
      "importGcsCustomMetadata": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsSource": {
        object ([GcsSources](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets#ConversationDataset.GcsSources))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`documentTemplate` |  `object (`[ImportDocumentTemplate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ImportDocumentTemplate)`)` Required. Document template used for importing all the documents.  
`importGcsCustomMetadata` |  `boolean` Whether to import custom metadata from Google Cloud Storage. Only valid when the document source is Google Cloud Storage URI.  
Required. The source to use for importing documents.If the source captures multiple objects, then multiple documents will be created, one corresponding to each object, and all of these documents will be created using the same document template.Dialogflow supports up to 350 documents in each request. If you try to import more, Dialogflow will return an error. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsSource` |  `object (`[GcsSources](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets#ConversationDataset.GcsSources)`)` Optional. The Google Cloud Storage location for the documents. The path can include a wildcard.These URIs may have the forms `gs://<bucket-name>/<object-name>`. `gs://<bucket-name>/<object-path>/*.<extension>`.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
