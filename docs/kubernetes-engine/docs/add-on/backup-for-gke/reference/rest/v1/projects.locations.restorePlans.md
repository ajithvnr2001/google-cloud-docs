---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans
title: REST Resource: projects.locations.restorePlans \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:43:58.881679+00:00
---

# REST Resource: projects.locations.restorePlans  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ APIs & Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest)



Send feedback 

#  REST Resource: projects.locations.restorePlans Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: RestorePlan
    * JSON representation
  * State
  * Methods



## Resource: RestorePlan

The configuration of a potential series of Restore operations to be performed against Backups belong to a particular BackupPlan.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "createTime": string,
      "updateTime": string,
      "description": string,
      "backupPlan": string,
      "cluster": string,
      "restoreConfig": {
        object ([RestoreConfig](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig))
      },
      "labels": {
        string: string,
        ...
      },
      "etag": string,
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans#State)),
      "stateReason": string,
      "restoreChannel": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The full name of the RestorePlan resource. Format: `projects/*/locations/*/restorePlans/*`.  
`uid` |  `string` Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this RestorePlan resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this RestorePlan resource was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`description` |  `string` Optional. User specified descriptive string for this RestorePlan.  
`backupPlan` |  `string` Required. Immutable. A reference to the `[BackupPlan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#BackupPlan)` from which Backups may be used as the source for Restores created via this RestorePlan. Format: `projects/*/locations/*/backupPlans/*`.  
`cluster` |  `string` Required. Immutable. The target cluster into which Restores created via this RestorePlan will restore data. NOTE: the cluster's region must be the same as the RestorePlan. Valid formats:

  * `projects/*/locations/*/clusters/*`
  * `projects/*/zones/*/clusters/*`

  
`restoreConfig` |  `object (`[RestoreConfig](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig)`)` Required. Configuration of Restores created via this RestorePlan.  
`labels` |  `map (key: string, value: string)` Optional. A set of custom labels supplied by user.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`etag` |  `string` Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a restore from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform restore updates in order to avoid race conditions: An `etag` is returned in the response to `restorePlans.get`, and systems are expected to put that etag in the request to `restorePlans.patch` or `restorePlans.delete` to ensure that their change will be applied to the same version of the resource.  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans#State)`)` Output only. State of the RestorePlan. This State field reflects the various stages a RestorePlan can be in during the Create operation.  
`stateReason` |  `string` Output only. Human-readable description of why RestorePlan is in the current `state`. This field is only meant for human readability and should not be used programmatically as this field is not guaranteed to be consistent.  
`restoreChannel` |  `string` Output only. The fully qualified name of the RestoreChannel to be used to create a RestorePlan. This field is set only if the `backupPlan` is in a different project than the RestorePlan. Format: `projects/*/locations/*/restoreChannels/*`  
  
## State

State

Enums  
---  
`STATE_UNSPECIFIED` | Default first value for Enums.  
`CLUSTER_PENDING` | Waiting for cluster state to be RUNNING.  
`READY` | The RestorePlan has successfully been created and is ready for Restores.  
`FAILED` | RestorePlan creation has failed.  
`DELETING` | The RestorePlan is in the process of being deleted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/create)`

|  Creates a new RestorePlan in a given location.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/delete)`

|  Deletes an existing RestorePlan.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/get)`

|  Retrieve the details of a single RestorePlan.  
  
### `[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[getTags](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/getTags)`

|  Returns tags directly bound to a GCP resource.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/list)`

|  Lists RestorePlans in a given location.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/patch)`

|  Update a RestorePlan.  
  
### `[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[setTags](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/setTags)`

|  Updates tags directly bound to a GCP resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
