---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults
title: REST Resource: projects.locations.exascaleDbStorageVaults \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:47.028851+00:00
---

# REST Resource: projects.locations.exascaleDbStorageVaults  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.exascaleDbStorageVaults Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ExascaleDbStorageVault
    * JSON representation
  * ExascaleDbStorageVaultProperties
    * JSON representation
  * ExascaleDbStorageDetails
    * JSON representation
  * State
  * ShapeAttribute
  * Methods



## Resource: ExascaleDbStorageVault

ExascaleDbStorageVault represents a storage vault exadb vm cluster resource. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/ExascaleDbStorageVault/>

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "gcpOracleZone": string,
      "properties": {
        object ([ExascaleDbStorageVaultProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults#ExascaleDbStorageVaultProperties))
      },
      "createTime": string,
      "entitlementId": string,
      "labels": {
        string: string,
        ...
      },
      "exadataInfrastructure": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the ExascaleDbStorageVault. Format: projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascaleDbStorageVault}  
`displayName` |  `string` Required. The display name for the ExascaleDbStorageVault. The name does not have to be unique within your project. The name must be 1-255 characters long and can only contain alphanumeric characters.  
`gcpOracleZone` |  `string` Optional. The GCP Oracle zone where Oracle ExascaleDbStorageVault is hosted. Example: us-east4-b-r2. If not specified, the system will pick a zone based on availability.  
`properties` |  `object (`[ExascaleDbStorageVaultProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults#ExascaleDbStorageVaultProperties)`)` Required. The properties of the ExascaleDbStorageVault.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time when the ExascaleDbStorageVault was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`entitlementId` |  `string` Output only. The ID of the subscription entitlement associated with the ExascaleDbStorageVault.  
`labels` |  `map (key: string, value: string)` Optional. The labels or tags associated with the ExascaleDbStorageVault.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`exadataInfrastructure` |  `string` Optional. The Exadata Infrastructure resource on which ExascaleDbStorageVault resource is created, in the following format: projects/{project}/locations/{region}/cloudExadataInfrastuctures/{cloud_extradata_infrastructure}  
  
## ExascaleDbStorageVaultProperties

The properties of the ExascaleDbStorageVault. next ID: 12

JSON representation  
---  
      
    
    {
      "ocid": string,
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/TimeZone))
      },
      "exascaleDbStorageDetails": {
        object ([ExascaleDbStorageDetails](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults#ExascaleDbStorageDetails))
      },
      "state": enum ([State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults#State)),
      "description": string,
      "vmClusterIds": [
        string
      ],
      "vmClusterCount": integer,
      "additionalFlashCachePercent": integer,
      "ociUri": string,
      "attachedShapeAttributes": [
        enum ([ShapeAttribute](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults#ShapeAttribute))
      ],
      "availableShapeAttributes": [
        enum ([ShapeAttribute](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults#ShapeAttribute))
      ]
    }  
  
Fields  
---  
`ocid` |  `string` Output only. The OCID for the ExascaleDbStorageVault.  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/TimeZone)`)` Output only. The time zone of the ExascaleDbStorageVault.  
`exascaleDbStorageDetails` |  `object (`[ExascaleDbStorageDetails](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults#ExascaleDbStorageDetails)`)` Required. The storage details of the ExascaleDbStorageVault.  
`state` |  `enum (`[State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults#State)`)` Output only. The state of the ExascaleDbStorageVault.  
`description` |  `string` Optional. The description of the ExascaleDbStorageVault.  
`vmClusterIds[]` |  `string` Output only. The list of VM cluster OCIDs associated with the ExascaleDbStorageVault.  
`vmClusterCount` |  `integer` Output only. The number of VM clusters associated with the ExascaleDbStorageVault.  
`additionalFlashCachePercent` |  `integer` Optional. The size of additional flash cache in percentage of high capacity database storage.  
`ociUri` |  `string` Output only. Deep link to the OCI console to view this resource.  
`attachedShapeAttributes[]` |  `enum (`[ShapeAttribute](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults#ShapeAttribute)`)` Output only. The shape attributes of the VM clusters attached to the ExascaleDbStorageVault.  
`availableShapeAttributes[]` |  `enum (`[ShapeAttribute](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults#ShapeAttribute)`)` Output only. The shape attributes available for the VM clusters to be attached to the ExascaleDbStorageVault.  
  
## ExascaleDbStorageDetails

The storage details of the ExascaleDbStorageVault.

JSON representation  
---  
      
    
    {
      "availableSizeGbs": integer,
      "totalSizeGbs": integer
    }  
  
Fields  
---  
`availableSizeGbs` |  `integer` Output only. The available storage capacity for the ExascaleDbStorageVault, in gigabytes (GB).  
`totalSizeGbs` |  `integer` Required. The total storage allocation for the ExascaleDbStorageVault, in gigabytes (GB).  
  
## State

The state of the ExascaleDbStorageVault.

Enums  
---  
`STATE_UNSPECIFIED` | The state of the ExascaleDbStorageVault is unspecified.  
`PROVISIONING` | The ExascaleDbStorageVault is being provisioned.  
`AVAILABLE` | The ExascaleDbStorageVault is available.  
`UPDATING` | The ExascaleDbStorageVault is being updated.  
`TERMINATING` | The ExascaleDbStorageVault is being deleted.  
`TERMINATED` | The ExascaleDbStorageVault has been deleted.  
`FAILED` | The ExascaleDbStorageVault has failed.  
  
## ShapeAttribute

The shape attribute of the VM clusters attached to the ExascaleDbStorageVault.

Enums  
---  
`SHAPE_ATTRIBUTE_UNSPECIFIED` | Default unspecified value.  
`SMART_STORAGE` | Indicates that the resource is in smart storage.  
`BLOCK_STORAGE` | Indicates that the resource is in block storage.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults/create)`

|  Creates a new ExascaleDB Storage Vault resource.  
  
### `[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults/delete)`

|  Deletes a single ExascaleDB Storage Vault.  
  
### `[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults/get)`

|  Gets details of a single ExascaleDB Storage Vault.  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults/list)`

|  Lists all the ExascaleDB Storage Vaults for the given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
