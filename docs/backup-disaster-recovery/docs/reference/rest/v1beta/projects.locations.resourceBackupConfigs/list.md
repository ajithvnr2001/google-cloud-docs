---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs/list/
title: Method: projects.locations.resourceBackupConfigs.list \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:55.650668+00:00
---

# Method: projects.locations.resourceBackupConfigs.list  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Method: projects.locations.resourceBackupConfigs.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists ResourceBackupConfigs.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9europe-west10europe-west12me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-central2us-east1us-east4us-east5us-east7us-south1us-west1us-west2us-west3us-west4us-west8useu

  
`GET https://backupdr.googleapis.com/v1beta/{parent=projects/*/locations/*}/resourceBackupConfigs`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project and location for which to retrieve resource backup configs. Format: 'projects/{projectId}/locations/{location}'. In Google Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will use 100 as default. Maximum value is 500 and values above 500 will be coerced to 500.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Filtering results.  
`orderBy` |  `string` Optional. Hint for how to order the results.  
  
### Request body

The request body must be empty.

### Response body

Response for resourceBackupConfigs.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "resourceBackupConfigs": [
        {
          object ([ResourceBackupConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#ResourceBackupConfig))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`resourceBackupConfigs[]` |  `object (`[ResourceBackupConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.resourceBackupConfigs#ResourceBackupConfig)`)` The list of ResourceBackupConfigs for the specified scope.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-backupdr`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
