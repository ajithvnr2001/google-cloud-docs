---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents/purge/
title: Method: projects.locations.collections.dataStores.branches.documents.purge \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:37.602158+00:00
---

# Method: projects.locations.collections.dataStores.branches.documents.purge  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents/purge/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  Method: projects.locations.collections.dataStores.branches.documents.purge Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Permanently deletes all selected `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents#Document)`s in a branch.

This process is asynchronous. Depending on the number of `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents#Document)`s to be deleted, this operation can take hours to complete. Before the delete operation completes, some `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents#Document)`s might still be returned by `[DocumentService.GetDocument](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.branches.documents/get#google.cloud.discoveryengine.v1.DocumentService.GetDocument)` or `[DocumentService.ListDocuments](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.branches.documents/list#google.cloud.discoveryengine.v1.DocumentService.ListDocuments)`.

To get a list of the `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents#Document)`s to be deleted, set `[PurgeDocumentsRequest.force](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.branches.documents/purge#body.request_body.FIELDS.force)` to false.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:purge`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}/branches/{branch}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "filter": string,
      "errorConfig": {
        object ([PurgeErrorConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/PurgeErrorConfig))
      },
      "force": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/GcsSource))
      },
      "inlineSource": {
        object (InlineSource)
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`filter` |  `string` Required. Filter matching documents to purge. Only currently supported value is `*` (all items).  
`errorConfig` |  `object (`[PurgeErrorConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/PurgeErrorConfig)`)` The desired location of errors incurred during the purge.  
`force` |  `boolean` Actually performs the purge. If `force` is set to false, return the expected purge count without deleting any documents.  
The desired input source for the purging documents based on document IDs. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsSource` |  `object (`[GcsSource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/GcsSource)`)` Cloud Storage location for the input content. Supported `dataSchema`: * `documentId`: One valid `[Document.id](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents#Document.FIELDS.id)` per line.  
`inlineSource` |  `object (`InlineSource`)` Inline source for the input content for purge.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `discoveryengine.documents.purge`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
