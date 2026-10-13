---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/export/
title: Method: projects.knowledgeBases.documents.export \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:27.671999+00:00
---

# Method: projects.knowledgeBases.documents.export  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases.documents/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.knowledgeBases.documents.export Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Exports a smart messaging candidate document into the specified destination.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

  * `metadata`: `[KnowledgeOperationMetadata](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/KnowledgeOperationMetadata)`
  * `response`: `[Document](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases.documents#Document)`



### HTTP request

`POST https://{endpoint}/v2/{name=projects/*/knowledgeBases/*/documents/*}:export`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the document to export. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dialogflow.documents.get`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "exportFullContent": boolean,
      "smartMessagingPartialUpdate": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsDestination": {
        object ([GcsDestination](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/GcsDestination))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`exportFullContent` |  `boolean` When enabled, export the full content of the document including empirical probability.  
`smartMessagingPartialUpdate` |  `boolean` When enabled, export the smart messaging allowlist document for partial update.  
Required. The destination for the export. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsDestination` |  `object (`[GcsDestination](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/GcsDestination)`)` Cloud Storage file path to export the document.  
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
