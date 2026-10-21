---
url: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains
title: REST Resource: projects.locations.multicastDomains \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:29:00.940981+00:00
---

# REST Resource: projects.locations.multicastDomains  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Reference ](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest)



Send feedback 

#  REST Resource: projects.locations.multicastDomains Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MulticastDomain
    * JSON representation
  * Connection
    * JSON representation
  * ConnectionType
  * Methods



## Resource: MulticastDomain

Multicast domain resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "state": {
        object ([MulticastResourceState](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/MulticastResourceState))
      },
      "labels": {
        string: string,
        ...
      },
      "description": string,
      "adminNetwork": string,
      "connection": {
        object ([Connection](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains#Connection))
      },
      "uniqueId": string,
      "multicastDomainGroup": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the multicast domain. Use the following format: `projects/*/locations/global/multicastDomains/*`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] The timestamp when the multicast domain was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] The timestamp when the multicast domain was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `object (`[MulticastResourceState](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/MulticastResourceState)`)` Output only. [Output only] The state of the resource.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key-value pairs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. An optional text description of the multicast domain.  
`adminNetwork` |  `string` Required. The resource name of the multicast admin VPC network. Use the following format: `projects/{project}/locations/global/networks/{network}`.  
`connection` |  `object (`[Connection](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains#Connection)`)` Required. The VPC connection type for this multicast domain.  
`uniqueId` |  `string` Output only. [Output only] The Google-generated UUID for the resource. This value is unique across all multicast domain resources. If a domain is deleted and another with the same name is created, the new domain is assigned a different uniqueId.  
`multicastDomainGroup` |  `string` Optional. The multicast domain group this domain should be associated with. Use the following format: `projects/{project}/locations/global/multicastDomainGroups/{multicastDomainGroup}`.  
  
## Connection

VPC connectivity information.

JSON representation  
---  
      
    
    {
      "connectionType": enum ([ConnectionType](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains#ConnectionType)),
      "nccHub": string
    }  
  
Fields  
---  
`connectionType` |  `enum (`[ConnectionType](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains#ConnectionType)`)` Required. The VPC connection type.  
`nccHub` |  `string` Optional. The resource name of the [NCC](https://cloud.google.com/network-connectivity-center) hub. Use the following format: `projects/{project}/locations/global/hubs/{hub}`.  
  
## ConnectionType

The connection type for authorizing multicast traffic.

Enums  
---  
`CONNECTION_TYPE_UNSPECIFIED` | Unspecified connection type.  
`NCC` | Connected by [NCC](https://cloud.google.com/network-connectivity-center). Producers and consumers can be in separated VPCs connected by NCC, or the same VPC.  
`SAME_VPC` | Producer and consumers must be in the same VPC network.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains/create)`

|  Creates a new multicast domain in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains/delete)`

|  Deletes a single multicast domain.  
  
### `[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains/get)`

|  Gets details of a single multicast domain.  
  
### `[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains/list)`

|  Lists multicast domains in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-22 UTC."],[],[]] 
