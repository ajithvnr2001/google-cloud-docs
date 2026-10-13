---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.dataSourceReferences/fetchForResourceType/
title: Method: projects.locations.dataSourceReferences.fetchForResourceType \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:01.935099+00:00
---

# Method: projects.locations.dataSourceReferences.fetchForResourceType  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.dataSourceReferences/fetchForResourceType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Method: projects.locations.dataSourceReferences.fetchForResourceType Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Fetch DataSourceReferences for a given project, location and resource type.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9europe-west10europe-west12me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-central2us-east1us-east4us-east5us-east7us-south1us-west1us-west2us-west3us-west4us-west8useu

  
`GET https://backupdr.googleapis.com/v1beta/{parent=projects/*/locations/*}/dataSourceReferences:fetchForResourceType`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name. Format: projects/{project}/locations/{location}  
  
### Query parameters

Parameters  
---  
`resourceType` |  `string` Required. The type of the Google Cloud resource. Ex: sql.googleapis.com/Instance  
`pageSize` |  `integer` Optional. The maximum number of DataSourceReferences to return. The service may return fewer than this value. If unspecified, at most 50 DataSourceReferences will be returned. The maximum value is 100; values above 100 will be coerced to 100.  
`pageToken` |  `string` Optional. A page token, received from a previous call of `dataSourceReferences.fetchForResourceType`. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `dataSourceReferences.fetchForResourceType` must match the call that provided the page token.  
`filter` |  `string` Optional. A filter expression that filters the results fetched in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. Supported fields: * dataSource * dataSourceGcpResourceInfo.gcp_resourcename * dataSourceBackupConfigState * dataSourceBackupCount * dataSourceBackupConfigInfo.last_backup_state * dataSourceGcpResourceInfo.gcp_resourcename * dataSourceGcpResourceInfo.type * dataSourceGcpResourceInfo.location * dataSourceGcpResourceInfo.cloud_sql_instance_properties.instance_create_time  
`orderBy` |  `string` Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.Supported fields: * name  
  
### Request body

The request body must be empty.

### Response body

Response for the dataSourceReferences.fetchForResourceType method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dataSourceReferences": [
        {
          object ([DataSourceReference](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.dataSourceReferences#DataSourceReference))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`dataSourceReferences[]` |  `object (`[DataSourceReference](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1beta/projects.locations.dataSourceReferences#DataSourceReference)`)` The DataSourceReferences from the specified parent.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-backupdr`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
