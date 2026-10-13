---
url: https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.backupVaults/list/
title: Method: projects.locations.backupVaults.list \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:54.898475+00:00
---

# Method: projects.locations.backupVaults.list  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.backupVaults/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Reference ](https://docs.cloud.google.com/netapp/volumes/docs/apis)



Send feedback 

#  Method: projects.locations.backupVaults.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Returns list of all available backup vaults.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4

  
`GET https://netapp.googleapis.com/v1/{parent=projects/*/locations/*}/backupVaults`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The location for which to retrieve backupVault information, in the format `projects/{projectId}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of items to return.  
`pageToken` |  `string` The nextPageToken value to use if there are additional results to retrieve for this list request.  
`orderBy` |  `string` Sort results. Supported values are "name", "name desc" or "" (unsorted).  
`filter` |  `string` List filter.  
  
### Request body

The request body must be empty.

### Response body

ListBackupVaultsResponse is the result of ListBackupVaultsRequest.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "backupVaults": [
        {
          object ([BackupVault](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.backupVaults#BackupVault))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`backupVaults[]` |  `object (`[BackupVault](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.backupVaults#BackupVault)`)` A list of backupVaults in the project for the specified location.  
`nextPageToken` |  `string` The token you can use to retrieve the next page of results. Not returned if there are no more results in the list.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `netapp.backupVaults.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-02 UTC."],[],[]] 
