---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels
title: REST Resource: projects.locations.restoreChannels \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:04.905226+00:00
---

# REST Resource: projects.locations.restoreChannels  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ APIs & Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest)



Send feedback 

#  REST Resource: projects.locations.restoreChannels Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: RestoreChannel
    * JSON representation
  * Methods



## Resource: RestoreChannel

A RestoreChannel imposes constraints on where backups can be restored. The RestoreChannel should be in the same project and region as the backups. The backups can only be restored in the `destinationProject`.

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
`name` |  `string` Identifier. The fully qualified name of the RestoreChannel. `projects/*/locations/*/restoreChannels/*`  
`destinationProject` |  `string` Required. Immutable. The project into which the backups will be restored. The format is `projects/{projectId}` or `projects/{projectNumber}`.  
`uid` |  `string` Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this RestoreChannel was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this RestoreChannel was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. A set of custom labels supplied by user.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. User specified descriptive string for this RestoreChannel.  
`etag` |  `string` Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a RestoreChannel from overwriting each other. It is strongly suggested that systems make use of the 'etag' in the read-modify-write cycle to perform RestoreChannel updates in order to avoid race conditions: An `etag` is returned in the response to `restoreChannels.get`, and systems are expected to put that etag in the request to `restoreChannels.patch` or `restoreChannels.delete` to ensure that their change will be applied to the same version of the resource.  
`destinationProjectId` |  `string` Output only. The projectId where backups will be restored. Example Project ID: "my-project-id". This will be an OUTPUT_ONLY field to return the projectId of the destination project.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels/create)`

|  Creates a new RestoreChannel in a given location.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels/delete)`

|  Deletes an existing RestoreChannel.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels/get)`

|  Retrieve the details of a single RestoreChannel.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels/list)`

|  Lists RestoreChannels in a given location.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels/patch)`

|  Update a RestoreChannel.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
