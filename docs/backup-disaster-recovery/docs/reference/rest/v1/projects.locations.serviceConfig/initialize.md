---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.serviceConfig/initialize/
title: Method: projects.locations.serviceConfig.initialize \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:56.694094+00:00
---

# Method: projects.locations.serviceConfig.initialize  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.serviceConfig/initialize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Reference ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/reference)



Send feedback 

#  Method: projects.locations.serviceConfig.initialize Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * CloudSqlInstanceInitializationConfig
    * JSON representation
  * Edition
  * Try it!



Initializes the service related config for a project.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 europe-west10 europe-west12 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-central2 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us eu

  
`POST https://backupdr.googleapis.com/v1/{name=projects/*/locations/*/serviceConfig}:initialize`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the serviceConfig used to initialize the service. The location must be the location of the BackupVault. Format: `projects/{projectId}/locations/{location}/serviceConfig`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "resourceType": string,
      "requestId": string,
      "backupPlanLocation": string,
      "validateOnly": boolean,
    
      // Union field initialization_config can be only one of the following:
      "cloudSqlInstanceInitializationConfig": {
        object ([CloudSqlInstanceInitializationConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.serviceConfig/initialize#CloudSqlInstanceInitializationConfig))
      }
      // End of list of possible types for union field initialization_config.
    }  
  
Fields  
---  
`resourceType` |  `string` Required. The resource type to which the default service config will be applied. Examples include, "compute.googleapis.com/Instance" and "storage.googleapis.com/Bucket".  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
`backupPlanLocation` |  `string` Optional. The location where the BackupPlan will be created. This field is required for multi-region BackupVaults and is optional for regional BackupVaults. It is useful when creating a Backup Vault in a multi-region, allowing the BackupPlan to reside in a specific region within that multi-region. If this field is not provided, the BackupPlan will be created in the same location as specified in the `name` field.  
`validateOnly` |  `boolean` Optional. If set, validates the request and returns the result, but does not actually run it.  
Union field `initialization_config`. The configuration for initializing the resource. `initialization_config` can be only one of the following:  
`cloudSqlInstanceInitializationConfig` |  `object (`[CloudSqlInstanceInitializationConfig](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.serviceConfig/initialize#CloudSqlInstanceInitializationConfig)`)` Optional. The configuration for initializing a Cloud SQL instance.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## CloudSqlInstanceInitializationConfig

CloudSqlInstanceInitializationConfig contains the configuration for initializing a Cloud SQL instance.

JSON representation  
---  
      
    
    {
      "edition": enum ([Edition](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.serviceConfig/initialize#Edition))
    }  
  
Fields  
---  
`edition` |  `enum (`[Edition](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.serviceConfig/initialize#Edition)`)` Required. The edition of the Cloud SQL instance.  
  
## Edition

The edition of the Cloud SQL instance. For details, see <https://cloud.google.com/sql/docs/editions-intro>.

Enums  
---  
`EDITION_UNSPECIFIED` | Unspecified edition.  
`ENTERPRISE` | Enterprise edition.  
`ENTERPRISE_PLUS` | Enterprise Plus edition.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
