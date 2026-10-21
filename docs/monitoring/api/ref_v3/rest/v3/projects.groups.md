---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups
title: REST Resource: projects.groups \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:11.908101+00:00
---

# REST Resource: projects.groups  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  REST Resource: projects.groups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Group
    * JSON representation
  * Methods



## Resource: Group

The description of a dynamic collection of monitored resources. Each group has a filter that is matched against monitored resources and their associated metadata. If a group's filter matches an available monitored resource, then that resource is a member of that group. Groups can contain any number of monitored resources, and each monitored resource can be a member of any number of groups.

Groups can be nested in parent-child hierarchies. The `parentName` field identifies an optional parent for each group. If a group has a parent, then the only monitored resources available to be matched by the group's filter are the resources contained in the parent group. In other words, a group contains the monitored resources that match its filter and the filters of all the group's ancestors. A group without a parent can contain any monitored resource.

For example, consider an infrastructure running a set of instances with two user-defined tags: `"environment"` and `"role"`. A parent group has a filter, `environment="production"`. A child of that parent group has a filter, `role="transcoder"`. The parent group contains all instances in the production environment, regardless of their roles. The child group contains instances that have the transcoder role _and_ are in the production environment.

The monitored resources contained in a group can change at any moment, depending on what resources exist and what filters are associated with the group and its ancestors.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "parentName": string,
      "filter": string,
      "isCluster": boolean
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of this group. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]
    

When creating a group, this field is ignored and a new name is created consisting of the project specified in the call to `groups.create` and a unique `[GROUP_ID]` that is generated automatically.  
`displayName` |  `string` A user-assigned name for this group, used only for display purposes.  
`parentName` |  `string` The name of the group's parent, if it has one. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/groups/[GROUP_ID]
    

For groups with no parent, `parentName` is the empty string, `""`.  
`filter` |  `string` The filter used to determine which monitored resources belong to this group.  
`isCluster` |  `boolean` If true, the members of this group are considered to be a cluster. The system can perform additional analysis on groups that are clusters.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/create)`

|  Creates a new group.  
  
### `[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/delete)`

|  Deletes an existing group.  
  
### `[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/get)`

|  Gets a single group.  
  
### `[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/list)`

|  Lists the existing groups.  
  
### `[update](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/update)`

|  Updates an existing group.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
