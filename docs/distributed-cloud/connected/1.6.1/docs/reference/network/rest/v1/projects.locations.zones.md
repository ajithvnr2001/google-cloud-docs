---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/network/rest/v1/projects.locations.zones
title: REST Resource: projects.locations.zones \u00a0|\u00a0 Google Distributed Cloud connected, version 1.6.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:46.147035+00:00
---

# REST Resource: projects.locations.zones  |  Google Distributed Cloud connected, version 1.6.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/network/rest/v1/projects.locations.zones

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/apis)



Send feedback 

#  REST Resource: projects.locations.zones Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Zone
    * JSON representation
  * Methods



## Resource: Zone

A Google Edge Cloud zone.

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
      "layoutName": string
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the zone.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time when the zone was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time when the zone was last updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`labels  
**(deprecated)**` |  `map (key: string, value: string)` This item is deprecated!Deprecated: not implemented. Labels as key value pairs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`layoutName  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: not implemented. The deployment layout type.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/network/rest/v1/projects.locations.zones/get)   
**(deprecated)**`

|  Deprecated: not implemented.  
  
### `[initialize](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/network/rest/v1/projects.locations.zones/initialize)`

|  InitializeZone will initialize resources for a zone in a project.  
  
### `[list](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/network/rest/v1/projects.locations.zones/list)   
**(deprecated)**`

|  Deprecated: not implemented.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
