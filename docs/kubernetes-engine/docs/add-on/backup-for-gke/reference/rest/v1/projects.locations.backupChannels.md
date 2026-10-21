---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels
title: REST Resource: projects.locations.backupChannels \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:43:52.615623+00:00
---

# REST Resource: projects.locations.backupChannels  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ APIs & Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest)



Send feedback 

#  REST Resource: projects.locations.backupChannels Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: BackupChannel
    * JSON representation
  * Methods



## Resource: BackupChannel

A BackupChannel imposes constraints on where clusters can be backed up. The BackupChannel should be in the same project and region as the cluster being backed up. The backup can be created only in destinationProject.

JSON representation  
---  
      
    
    {
      "name": string,
      "destinationProject": string,
      "uid": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "description": string,
      "etag": string,
      "destinationProjectId": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The fully qualified name of the BackupChannel. `projects/*/locations/*/backupChannels/*`  
`destinationProject` |  `string` Required. Immutable. The project where Backups are allowed to be stored. The format is `projects/{projectId}` or `projects/{projectNumber}`.  
`uid` |  `string` Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this BackupChannel resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this BackupChannel resource was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. A set of custom labels supplied by user.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. User specified descriptive string for this BackupChannel.  
`etag` |  `string` Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a BackupChannel from overwriting each other. It is strongly suggested that systems make use of the 'etag' in the read-modify-write cycle to perform BackupChannel updates in order to avoid race conditions: An `etag` is returned in the response to `backupChannels.get`, and systems are expected to put that etag in the request to `backupChannels.patch` or `backupChannels.delete` to ensure that their change will be applied to the same version of the resource.  
`destinationProjectId` |  `string` Output only. The projectId where Backups are allowed to be stored. Example Project ID: "my-project-id". This will be an OUTPUT_ONLY field to return the projectId of the destination project.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels/create)`

|  Creates a new BackupChannel in a given location.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels/delete)`

|  Deletes an existing BackupChannel.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels/get)`

|  Retrieve the details of a single BackupChannel.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels/list)`

|  Lists BackupChannels in a given location.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels/patch)`

|  Update a BackupChannel.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
