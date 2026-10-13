---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupPlans.revisions/list/
title: Method: projects.locations.backupPlans.revisions.list \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:51.044292+00:00
---

# Method: projects.locations.backupPlans.revisions.list  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupPlans.revisions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Method: projects.locations.backupPlans.revisions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists BackupPlanRevisions in a given project and location.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9europe-west10europe-west12me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-central2us-east1us-east4us-east5us-east7us-south1us-west1us-west2us-west3us-west4us-west8useu

  
`GET https://backupdr.googleapis.com/v1beta/{parent=projects/*/locations/*/backupPlans/*}/revisions`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project and location for which to retrieve `BackupPlanRevisions` information. Format: `projects/{project}/locations/{location}/backupPlans/{backupPlan}`. In Google Cloud Backup and DR, locations map to Google Cloud regions, for e.g. **us-central1**.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of `BackupPlans` to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's `[nextPageToken](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupPlans/list#body.ListBackupPlansResponse.FIELDS.next_page_token)` to determine if there are more instances left to be queried.  
`pageToken` |  `string` Optional. The value of `[nextPageToken](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupPlans/list#body.ListBackupPlansResponse.FIELDS.next_page_token)` received from a previous `ListBackupPlans` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListBackupPlans` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

The response message for getting a list of `BackupPlanRevision`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "backupPlanRevisions": [
        {
          object ([BackupPlanRevision](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupPlans.revisions#BackupPlanRevision))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`backupPlanRevisions[]` |  `object (`[BackupPlanRevision](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupPlans.revisions#BackupPlanRevision)`)` The list of `BackupPlanRevisions` in the project for the specified location.If the `{location}` value in the request is "-", the response contains a list of resources from all locations. In case any location is unreachable, the response will only return backup plans in reachable locations and the 'unreachable' field will be populated with a list of unreachable locations.  
`nextPageToken` |  `string` A token which may be sent as `[pageToken](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.backupPlans.revisions/list#body.QUERY_PARAMETERS.page_token)` in a subsequent `revisions.list` call to retrieve the next page of results. If this field is omitted or empty, then there are no more results to return.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-backupdr`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
