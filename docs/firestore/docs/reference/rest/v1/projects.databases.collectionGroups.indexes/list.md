---
url: https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.indexes/list/
title: Method: projects.databases.collectionGroups.indexes.list \u00a0|\u00a0 Firestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:44.820833+00:00
---

# Method: projects.databases.collectionGroups.indexes.list  |  Firestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.indexes/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback 

#  Method: projects.databases.collectionGroups.indexes.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists composite indexes.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 asia-southeast3 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 eu us

  
`GET https://firestore.googleapis.com/v1/{parent=projects/*/databases/*/collectionGroups/*}/indexes`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. A parent name of the form `projects/{projectId}/databases/{databaseId}/collectionGroups/{collectionId}`  
  
### Query parameters

Parameters  
---  
`filter` |  `string` The filter to apply to list results.  
`pageSize` |  `integer` The number of results to return.  
`pageToken` |  `string` A page token, returned from a previous call to `[FirestoreAdmin.ListIndexes](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.indexes/list#google.firestore.admin.v1.FirestoreAdmin.ListIndexes)`, that may be used to get the next page of results.  
  
### Request body

The request body must be empty.

### Response body

The response for `[FirestoreAdmin.ListIndexes](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.indexes/list#google.firestore.admin.v1.FirestoreAdmin.ListIndexes)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "indexes": [
        {
          object ([Index](https://docs.cloud.google.com/firestore/docs/reference/rest/Shared.Types/Index))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`indexes[]` |  `object (`[Index](https://docs.cloud.google.com/firestore/docs/reference/rest/Shared.Types/Index)`)` The requested indexes.  
`nextPageToken` |  `string` A page token that may be used to request another page of results. If blank, this is the last page.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/datastore`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-20 UTC."],[],[]] 
