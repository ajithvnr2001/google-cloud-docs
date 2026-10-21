---
url: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/pointInTimeRestore/
title: Method: instances.pointInTimeRestore \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:14:32.560219+00:00
---

# Method: instances.pointInTimeRestore  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/pointInTimeRestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/postgres/apis)



Send feedback 

#  Method: instances.pointInTimeRestore Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * PointInTimeRestoreContext
    * JSON representation
  * Examples
  * Try it!



Point in time restore for an instance managed by Google Cloud Backup and Disaster Recovery.

### HTTP request

`POST https://sqladmin.googleapis.com/sql/v1beta4/{parent=projects/*}:pointInTimeRestore`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where you created this instance. Format: projects/{project}  
  
### Request body

The request body contains an instance of `[PointInTimeRestoreContext](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/pointInTimeRestore#PointInTimeRestoreContext)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## PointInTimeRestoreContext

Context to perform a point-in-time restore of an instance managed by Backup and Disaster Recovery (DR) Service.

JSON representation  
---  
      
    
    {
      "pointInTime": string,
      "targetInstanceSettings": {
        object ([DatabaseInstance](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances#DatabaseInstance))
      },
      "targetInstanceClearSettingsFieldNames": [
        string
      ],
      "datasource": string,
      "targetInstance": string,
      "privateNetwork": string,
      "allocatedIpRange": string,
      "preferredZone": string,
      "preferredSecondaryZone": string,
      "region": string
    }  
  
Fields  
---  
`pointInTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The date and time to which you want to restore the instance.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`targetInstanceSettings` |  `object (`[DatabaseInstance](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances#DatabaseInstance)`)` Optional. Specifies the instance settings that will be overridden from the source instance. This field is only applicable for cross project PITRs.  
`targetInstanceClearSettingsFieldNames[]` |  `string` Optional. Specifies the instance settings that will be cleared from the source instance. This field is only applicable for cross project PITRs.  
`datasource` |  `string` The Backup and Disaster Recovery (DR) Service Datasource URI. Format: projects/{project}/locations/{region}/backupVaults/{backupvault}/dataSources/{datasource}.  
`targetInstance` |  `string` Target instance name.  
`privateNetwork` |  `string` Optional. The resource link for the VPC network from which the Cloud SQL instance is accessible for private IP. For example, `/projects/myProject/global/networks/default`.  
`allocatedIpRange` |  `string` Optional. The name of the allocated IP range for the internal IP Cloud SQL instance. For example: "google-managed-services-default". If you set this, then Cloud SQL creates the IP address for the cloned instance in the allocated range. This range must comply with [RFC 1035](https://tools.ietf.org/html/rfc1035) standards. Specifically, the name must be 1-63 characters long and match the regular expression [a-z](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/\[-a-z0-9\]*\[a-z0-9\])?. Reserved for future use.  
`preferredZone` |  `string` Optional. Point-in-time recovery of an instance to the specified zone. If no zone is specified, then clone to the same primary zone as the source instance.  
`preferredSecondaryZone` |  `string` Optional. Point-in-time recovery of a regional instance in the specified zones. If not specified, clone to the same secondary zone as the source instance. This value cannot be the same as the preferredZone field.  
`region` |  `string` Optional. The region of the target instance where the datasource will be restored. For example: "us-central1".  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
