---
url: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.hubs.groups
title: REST Resource: projects.locations.global.hubs.groups \u00a0|\u00a0 Network Connectivity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:13.843141+00:00
---

# REST Resource: projects.locations.global.hubs.groups  |  Network Connectivity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.hubs.groups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Reference ](https://docs.cloud.google.com/network-connectivity/docs/apis)



Send feedback 

#  REST Resource: projects.locations.global.hubs.groups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Group
    * JSON representation
  * AutoAccept
    * JSON representation
  * Methods



## Resource: Group

A group represents a subset of spokes attached to a hub.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "description": string,
      "uid": string,
      "state": enum (State),
      "autoAccept": {
        object ([AutoAccept](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.hubs.groups#AutoAccept))
      },
      "routeTable": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. The name of the group. Group names must be unique. They use the following form: `projects/{projectNumber}/locations/global/hubs/{hub}/groups/{groupId}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the group was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the group was last updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. The description of the group.  
`uid` |  `string` Output only. The Google-generated UUID for the group. This value is unique across all group resources. If a group is deleted and another with the same name is created, the new route table is assigned a different uniqueId.  
`state` |  `enum (`State`)` Output only. The current lifecycle state of this group.  
`autoAccept` |  `object (`[AutoAccept](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.hubs.groups#AutoAccept)`)` Optional. The auto-accept setting for this group.  
`routeTable` |  `string` Output only. The name of the route table that corresponds to this group. They use the following form: `projects/{projectNumber}/locations/global/hubs/{hubId}/routeTables/{route_table_id}`  
  
## AutoAccept

The auto-accept setting for a group controls whether proposed spokes are automatically attached to the hub. If auto-accept is enabled, the spoke immediately is attached to the hub and becomes part of the group. In this case, the new spoke is in the ACTIVE state. If auto-accept is disabled, the spoke goes to the INACTIVE state, and it must be reviewed and accepted by a hub administrator.

JSON representation  
---  
      
    
    {
      "autoAcceptProjects": [
        string
      ]
    }  
  
Fields  
---  
`autoAcceptProjects[]` |  `string` Optional. A list of project ids or project numbers for which you want to enable auto-accept. The auto-accept setting is applied to spokes being created or updated in these projects.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.hubs.groups/get)`

|  Gets details about a Network Connectivity Center group.  
  
### `[getIamPolicy](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.hubs.groups/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.hubs.groups/list)`

|  Lists groups in a given hub.  
  
### `[patch](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.hubs.groups/patch)`

|  Updates the parameters of a Network Connectivity Center group.  
  
### `[setIamPolicy](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.hubs.groups/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.hubs.groups/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
