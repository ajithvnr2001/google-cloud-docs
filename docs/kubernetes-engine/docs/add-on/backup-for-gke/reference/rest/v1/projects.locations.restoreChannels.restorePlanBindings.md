---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels.restorePlanBindings
title: REST Resource: projects.locations.restoreChannels.restorePlanBindings \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:43:58.743414+00:00
---

# REST Resource: projects.locations.restoreChannels.restorePlanBindings  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels.restorePlanBindings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ APIs & Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest)



Send feedback 

#  REST Resource: projects.locations.restoreChannels.restorePlanBindings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: RestorePlanBinding
    * JSON representation
  * Methods



## Resource: RestorePlanBinding

A RestorePlanBinding binds a RestorePlan with a RestoreChannel. This resource is created automatically when a RestorePlan is created using a RestoreChannel. This also serves as a holder for cross-project fields that need to be displayed in the current project.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "createTime": string,
      "updateTime": string,
      "restorePlan": string,
      "etag": string,
      "backupPlan": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The fully qualified name of the RestorePlanBinding. `projects/*/locations/*/restoreChannels/*/restorePlanBindings/*`  
`uid` |  `string` Output only. Server generated global unique identifier of [UUID4](https://en.wikipedia.org/wiki/Universally_unique_identifier)  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this binding was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this binding was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`restorePlan` |  `string` Output only. The fully qualified name of the RestorePlan bound to this RestoreChannel. `projects/*/locations/*/restorePlans/{restorePlan}`  
`etag` |  `string` Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a RestorePlanBinding from overwriting each other. It is strongly suggested that systems make use of the 'etag' in the read-modify-write cycle to perform RestorePlanBinding updates in order to avoid race conditions: An `etag` is returned in the response to `restorePlanBindings.get`, and systems are expected to put that etag in the request to `UpdateRestorePlanBinding` or `DeleteRestorePlanBinding` to ensure that their change will be applied to the same version of the resource.  
`backupPlan` |  `string` Output only. The fully qualified name of the BackupPlan bound to the specified RestorePlan. `projects/*/locations/*/backukpPlans/{backupPlan}`  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels.restorePlanBindings/get)`

|  Retrieve the details of a single RestorePlanBinding.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels.restorePlanBindings/list)`

|  Lists RestorePlanBindings in a given location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
