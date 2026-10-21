---
url: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainGroups
title: REST Resource: projects.locations.multicastDomainGroups \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:52:35.571600+00:00
---

# REST Resource: projects.locations.multicastDomainGroups  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainGroups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Reference ](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest)



Send feedback 

#  REST Resource: projects.locations.multicastDomainGroups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MulticastDomainGroup
    * JSON representation
  * Methods



## Resource: MulticastDomainGroup

Multicast domain group resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "state": {
        object ([MulticastResourceState](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/MulticastResourceState))
      },
      "labels": {
        string: string,
        ...
      },
      "description": string,
      "uniqueId": string,
      "multicastDomains": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the multicast domain group. Use the following format: `projects/*/locations/global/multicastDomainGroups/*`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] The timestamp when the multicast domain group was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] The timestamp when the multicast domain group was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `object (`[MulticastResourceState](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/MulticastResourceState)`)` Output only. [Output only] The state of the resource.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key-value pairs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. An optional text description of the multicast domain group.  
`uniqueId` |  `string` Output only. [Output only] The Google-generated UUID for the resource. This value is unique across all multicast domain group resources. If a domain is deleted and another with the same name is created, the new domain is assigned a different uniqueId.  
`multicastDomains[]` |  `string` Output only. [Output only] Multicast domains associated with the group. There can be at most 2 multicast domains in a group.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainGroups/create)`

|  Creates a new multicast domain group in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainGroups/delete)`

|  Deletes a single multicast domain.  
  
### `[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainGroups/get)`

|  Gets details of a single multicast domain group.  
  
### `[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainGroups/list)`

|  Lists multicast domain groups in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-22 UTC."],[],[]] 
