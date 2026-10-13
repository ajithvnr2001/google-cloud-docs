---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.targetProjects
title: REST Resource: projects.locations.targetProjects \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:03.480472+00:00
---

# REST Resource: projects.locations.targetProjects  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.targetProjects

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  REST Resource: projects.locations.targetProjects Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TargetProject
    * JSON representation
  * Methods



## Resource: TargetProject

TargetProject message represents a target Compute Engine project for a migration or a clone.

JSON representation  
---  
      
    
    {
      "name": string,
      "project": string,
      "description": string,
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the target project.  
`project` |  `string` Required. The target project ID (number) or project name.  
`description` |  `string` The target project's description.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time this target project resource was created (not related to when the Compute Engine project it points to was created).A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time the target project resource was updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.targetProjects/create)`

|  Creates a new TargetProject in a given project.  
  
### `[delete](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.targetProjects/delete)`

|  Deletes a single TargetProject.  
  
### `[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.targetProjects/get)`

|  Gets details of a single TargetProject.  
  
### `[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.targetProjects/list)`

|  Lists TargetProjects in a given project.  
  
### `[patch](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.targetProjects/patch)`

|  Updates the parameters of a single TargetProject.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
