---
url: https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1beta1/projects.locations.backupPolicies
title: REST Resource: projects.locations.backupPolicies \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:25.192088+00:00
---

# REST Resource: projects.locations.backupPolicies  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1beta1/projects.locations.backupPolicies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Reference ](https://docs.cloud.google.com/netapp/volumes/docs/apis)



Send feedback 

#  REST Resource: projects.locations.backupPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: BackupPolicy
    * JSON representation
  * State
  * Methods



## Resource: BackupPolicy

Backup Policy.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "labels": {
        string: string,
        ...
      },
      "state": enum ([State](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1beta1/projects.locations.backupPolicies#State)),
      "dailyBackupLimit": integer,
      "weeklyBackupLimit": integer,
      "monthlyBackupLimit": integer,
      "description": string,
      "enabled": boolean,
      "assignedVolumeCount": integer
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the backup policy. Format: `projects/{projectId}/locations/{location}/backupPolicies/{backupPolicyId}`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the backup policy was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Resource labels to represent user provided metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1beta1/projects.locations.backupPolicies#State)`)` Output only. The backup policy state.  
`dailyBackupLimit` |  `integer` Number of daily backups to keep. Note that the minimum daily backup limit is 2.  
`weeklyBackupLimit` |  `integer` Number of weekly backups to keep. Note that the sum of daily, weekly and monthly backups should be greater than 1.  
`monthlyBackupLimit` |  `integer` Number of monthly backups to keep. Note that the sum of daily, weekly and monthly backups should be greater than 1.  
`description` |  `string` Description of the backup policy.  
`enabled` |  `boolean` If enabled, make backups automatically according to the schedules. This will be applied to all volumes that have this policy attached and enforced on volume level. If not specified, default is true.  
`assignedVolumeCount` |  `integer` Output only. The total number of volumes assigned by this backup policy.  
  
## State

Enums  
---  
`STATE_UNSPECIFIED` | State not set.  
`CREATING` | BackupPolicy is being created.  
`READY` | BackupPolicy is available for use.  
`DELETING` | BackupPolicy is being deleted.  
`ERROR` | BackupPolicy is not valid and cannot be used.  
`UPDATING` | BackupPolicy is being updated.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1beta1/projects.locations.backupPolicies/create)`

|  Creates new backup policy  
  
### `[delete](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1beta1/projects.locations.backupPolicies/delete)`

|  Warning!  
  
### `[get](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1beta1/projects.locations.backupPolicies/get)`

|  Returns the description of the specified backup policy by backup_policy_id.  
  
### `[list](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1beta1/projects.locations.backupPolicies/list)`

|  Returns list of all available backup policies.  
  
### `[patch](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1beta1/projects.locations.backupPolicies/patch)`

|  Updates settings of a specific backup policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-04 UTC."],[],[]] 
