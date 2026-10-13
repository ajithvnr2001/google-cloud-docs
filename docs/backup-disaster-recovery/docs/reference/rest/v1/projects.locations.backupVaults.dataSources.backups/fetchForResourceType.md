---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.backupVaults.dataSources.backups/fetchForResourceType/
title: Method: projects.locations.backupVaults.dataSources.backups.fetchForResourceType \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:53.614692+00:00
---

# Method: projects.locations.backupVaults.dataSources.backups.fetchForResourceType  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.backupVaults.dataSources.backups/fetchForResourceType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Reference ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/reference)



Send feedback 

#  Method: projects.locations.backupVaults.dataSources.backups.fetchForResourceType Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Fetch Backups for a given resource type.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 europe-west10 europe-west12 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-central2 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us eu

  
`GET https://backupdr.googleapis.com/v1/{parent=projects/*/locations/*/backupVaults/*/dataSources/*}/backups:fetchForResourceType`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Datasources are the parent resource for the backups. Format: projects/{project}/locations/{location}/backupVaults/{backupVaultId}/dataSources/{datasourceId}  
  
### Query parameters

Parameters  
---  
`resourceType` |  `string` Required. The type of the Google Cloud resource. Ex: sqladmin.googleapis.com/Instance  
`pageSize` |  `integer` Optional. The maximum number of Backups to return. The service may return fewer than this value. If unspecified, at most 50 Backups will be returned. The maximum value is 100; values above 100 will be coerced to 100.  
`pageToken` |  `string` Optional. A page token, received from a previous call of `backups.fetchForResourceType`. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `backups.fetchForResourceType` must match the call that provided the page token.  
`filter` |  `string` Optional. A filter expression that filters the results fetched in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. Supported fields: * name * state * backupType * createTime * expireTime * enforcedRetentionEndTime * gcpBackupPlanInfo.backup_plan * cloudSqlInstanceBackupProperties.instance_tier * cloudSqlInstanceBackupProperties.database_installed_version  
`orderBy` |  `string` Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.Supported fields: * name  
`view` |  `enum (`[BackupView](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/BackupView)`)` Optional. This parameter is used to specify the view of the backup. If not specified, the default view is BASIC.  
  
### Request body

The request body must be empty.

### Response body

Response for the backups.fetchForResourceType method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "backups": [
        {
          object ([Backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.backupVaults.dataSources.backups#Backup))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`backups[]` |  `object (`[Backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.backupVaults.dataSources.backups#Backup)`)` The Backups from the specified parent.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
