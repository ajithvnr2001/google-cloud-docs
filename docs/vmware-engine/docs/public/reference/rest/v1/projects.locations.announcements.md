---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.announcements
title: REST Resource: projects.locations.announcements \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:06.699387+00:00
---

# REST Resource: projects.locations.announcements  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.announcements

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  REST Resource: projects.locations.announcements Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Announcement
    * JSON representation
  * State
  * Methods



## Resource: Announcement

Announcement for the resources of Vmware Engine.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "code": string,
      "description": string,
      "state": enum ([State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.announcements#State)),
      "targetResourceType": string,
      "metadata": {
        string: string,
        ...
      },
      "activityType": string,
    
      // Union field target can be only one of the following:
      "privateCloud": string,
      "cluster": string
      // End of list of possible types for union field target.
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the announcement. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-west1-a/announcements/my-announcement-id`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this resource. It also serves as start time of notification.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last update time of this resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`code` |  `string` Required. Code of the announcement. Indicates the presence of a VMware Engine related announcement and corresponds to a related message in the `description` field.  
`description` |  `string` Output only. Description of the announcement.  
`state` |  `enum (`[State](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.announcements#State)`)` Output only. State of the resource. New values may be added to this enum when appropriate.  
`targetResourceType` |  `string` Output only. Target Resource Type defines the type of the target for the announcement  
`metadata` |  `map (key: string, value: string)` Output only. Additional structured details about this announcement.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`activityType` |  `string` Optional. Activity type of the announcement There can be only one active announcement for a given activity type and target resource.  
Union field `target`. Target has the details of the resource for which the announcement is created `target` can be only one of the following:  
`privateCloud` |  `string` A Private Cloud resource name.  
`cluster` |  `string` A Cluster resource name.  
  
## State

Enum state defines current state of an announcement

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value should never be used.  
`ACTIVE` | Active announcement which should be visible to user.  
`INACTIVE` | Inactive announcement which should not be visible to user.  
`DELETING` | Announcement which is being deleted  
`CREATING` | Announcement which being created  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.announcements/get)`

|  Retrieves a `Announcement` by its resource name.  
  
### `[list](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.announcements/list)`

|  Lists `Announcements` for a given region and project  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
