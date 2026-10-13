---
url: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups
title: REST Resource: projects.locations.global.domains.backups \u00a0|\u00a0 Managed Microsoft AD \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:39.511367+00:00
---

# REST Resource: projects.locations.global.domains.backups  |  Managed Microsoft AD  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad)
  * [ Reference ](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest)



Send feedback 

#  REST Resource: projects.locations.global.domains.backups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Backup
    * JSON representation
  * Type
  * State
  * Methods



## Resource: Backup

Represents a Managed Microsoft Identities backup.

JSON representation  
---  
      
    
    {
      "name": string,
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string,
      "type": enum ([Type](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups#Type)),
      "state": enum ([State](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups#State)),
      "statusMessage": string,
      "description": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The unique name of the Backup in the form of projects/{projectId}/locations/global/domains/{domainName}/backups/{name}  
`labels` |  `map (key: string, value: string)` Optional. Resource labels to represent user provided metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time the backups was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Last update time.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups#Type)`)` Output only. Indicates whether it’s an on-demand backup or scheduled.  
`state` |  `enum (`[State](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups#State)`)` Output only. The current state of the backup.  
`statusMessage` |  `string` Output only. Additional information about the current status of this backup, if available.  
`description` |  `string` Optional. A short description of the backup.  
  
## Type

Represents type of Backup.

Enums  
---  
`TYPE_UNSPECIFIED` | Backup type not specified.  
`ON_DEMAND` | Backup was manually created.  
`SCHEDULED` | Backup was automatically created.  
`SCHEMA_EXTENSION` | Backup was taken as part of Schema Extension request.  
  
## State

Represents the different states of a Cloud AD Backup.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`CREATING` | Backup is being created.  
`ACTIVE` | Backup has been created and validated.  
`FAILED` | Backup has been created but failed validation.  
`DELETING` | Backup is being deleted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups/create)`

|  Creates a Backup for a domain.  
  
### `[delete](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups/delete)`

|  Deletes identified Backup.  
  
### `[get](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups/get)`

|  Gets details of a single Backup.  
  
### `[getIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups/list)`

|  Lists Backup in a given project.  
  
### `[patch](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups/patch)`

|  Updates the labels for specified Backup.  
  
### `[setIamPolicy](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1beta1/projects.locations.global.domains.backups/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
