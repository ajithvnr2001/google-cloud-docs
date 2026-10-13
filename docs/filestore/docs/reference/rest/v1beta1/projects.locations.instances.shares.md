---
url: https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.shares
title: REST Resource: projects.locations.instances.shares \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:23.489147+00:00
---

# REST Resource: projects.locations.instances.shares  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.shares

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Reference ](https://docs.cloud.google.com/filestore/docs/apis)



Send feedback 

#  REST Resource: projects.locations.instances.shares Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Share
    * JSON representation
  * State
  * Methods



## Resource: Share

A Filestore share.

JSON representation  
---  
      
    
    {
      "name": string,
      "mountName": string,
      "description": string,
      "capacityGb": string,
      "nfsExportOptions": [
        {
          object ([NfsExportOptions](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/NfsExportOptions))
        }
      ],
      "state": enum ([State](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.shares#State)),
      "createTime": string,
      "labels": {
        string: string,
        ...
      },
    
      // Union field source can be only one of the following:
      "backup": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the share, in the format `projects/{projectId}/locations/{locationId}/instances/{instanceId}/shares/{shareId}`.  
`mountName` |  `string` The mount name of the share. Must be 63 characters or less and consist of uppercase or lowercase letters, numbers, and underscores.  
`description` |  `string` A description of the share with 2048 characters or less. Requests with longer descriptions will be rejected.  
`capacityGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` File share capacity in gigabytes (GB). Filestore defines 1 GB as 1024^3 bytes. Must be greater than 0.  
`nfsExportOptions[]` |  `object (`[NfsExportOptions](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/NfsExportOptions)`)` Nfs Export Options. There is a limit of 10 export options per file share.  
`state` |  `enum (`[State](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.shares#State)`)` Output only. The share state.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the share was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Resource labels to represent user provided metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Union field `source`. The source that this Share has been restored from. Empty if the Share is created from scratch. `source` can be only one of the following:  
`backup` |  `string` Immutable. Full name of the Cloud Filestore Backup resource that this Share is restored from, in the format of projects/{projectId}/locations/{locationId}/backups/{backupId}. Empty, if the Share is created from scratch and not restored from a backup.  
  
## State

The share state.

Enums  
---  
`STATE_UNSPECIFIED` | State not set.  
`CREATING` | Share is being created.  
`READY` | Share is ready for use.  
`DELETING` | Share is being deleted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.shares/create)`

|  Creates a share.  
  
### `[delete](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.shares/delete)`

|  Deletes a share.  
  
### `[get](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.shares/get)`

|  Gets the details of a specific share.  
  
### `[list](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.shares/list)`

|  Lists all shares for a specified instance.  
  
### `[patch](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.shares/patch)`

|  Updates the settings of a specific share.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-11 UTC."],[],[]] 
