---
url: https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.locations.backups/list/
title: Method: projects.locations.backups.list \u00a0|\u00a0 Firestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:46.843153+00:00
---

# Method: projects.locations.backups.list  |  Firestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.locations.backups/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback 

#  Method: projects.locations.backups.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists all the backups.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 asia-southeast3 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 eu us

  
`GET https://firestore.googleapis.com/v1/{parent=projects/*/locations/*}/backups`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The location to list backups from.Format is `projects/{project}/locations/{location}`. Use `{location} = '-'` to list backups from all locations for the given project. This allows listing backups from a single location or from all locations.  
  
### Query parameters

Parameters  
---  
`filter` |  `string` An expression that filters the list of returned backups.A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: `<`, `>`, `<=`, `>=`, `!=`, `=`, or `:`. Colon `:` is the contains operator. Filter rules are not case sensitive.The following fields in the `[Backup](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.locations.backups#Backup)` are eligible for filtering:

  * `databaseUid` (supports `=` only)

  
  
### Request body

The request body must be empty.

### Response body

The response for `[FirestoreAdmin.ListBackups](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.locations.backups/list#google.firestore.admin.v1.FirestoreAdmin.ListBackups)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "backups": [
        {
          object ([Backup](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.locations.backups#Backup))
        }
      ],
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`backups[]` |  `object (`[Backup](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.locations.backups#Backup)`)` List of all backups for the project.  
`unreachable[]` |  `string` List of locations that existing backups were not able to be fetched from.Instead of failing the entire requests when a single location is unreachable, this response returns a partial result set and list of locations unable to be reached here. The request can be retried against a single location to get a concrete error.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/datastore`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-20 UTC."],[],[]] 
