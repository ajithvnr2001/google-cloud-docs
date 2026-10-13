---
url: https://docs.cloud.google.com/firestore/docs/reference/rest/v1beta1/projects.databases.documents/createDocument/
title: Method: projects.databases.documents.createDocument \u00a0|\u00a0 Firestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:36:26.570167+00:00
---

# Method: projects.databases.documents.createDocument  |  Firestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/reference/rest/v1beta1/projects.databases.documents/createDocument/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback 

#  Method: projects.databases.documents.createDocument Stay organized with collections  Save and categorize content based on your preferences. 

Creates a new document.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 asia-southeast3 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 eu us

  
`POST https://firestore.googleapis.com/v1beta1/{parent=projects/*/databases/*/documents/**}/{collectionId}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource. For example: `projects/{projectId}/databases/{databaseId}/documents` or `projects/{projectId}/databases/{databaseId}/documents/chatrooms/{chatroom_id}`  
`collectionId` |  `string` Required. The collection ID, relative to `parent`, to list. For example: `chatrooms`.  
  
### Query parameters

Parameters  
---  
`documentId` |  `string` The client-assigned document ID to use for this document.Optional. If not specified, an ID will be assigned by the service.  
`mask` |  `object (`[DocumentMask](https://docs.cloud.google.com/firestore/docs/reference/rest/v1beta1/DocumentMask)`)` The fields to return. If not set, returns all fields.If the document has a field that is not present in this mask, that field will not be returned in the response.  
  
### Request body

The request body contains an instance of `[Document](https://docs.cloud.google.com/firestore/docs/reference/rest/v1beta1/projects.databases.documents#Document)`.

### Response body

If successful, the response body contains an instance of `[Document](https://docs.cloud.google.com/firestore/docs/reference/rest/v1beta1/projects.databases.documents#Document)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/datastore`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-20 UTC."],[],[]] 
