---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs/reference/container/rest/v1/projects.locations.machines
title: REST Resource: projects.locations.machines \u00a0|\u00a0 Google Distributed Cloud connected, version 1.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:38.291107+00:00
---

# REST Resource: projects.locations.machines  |  Google Distributed Cloud connected, version 1.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs/reference/container/rest/v1/projects.locations.machines

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
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs/apis)



Send feedback 

#  REST Resource: projects.locations.machines Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Machine
    * JSON representation
  * Methods



## Resource: Machine

A Google Distributed Cloud Edge machine capable of acting as a Kubernetes node.

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
      "hostedNode": string,
      "zone": string,
      "version": string,
      "disabled": boolean
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the machine.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time when the node pool was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The time when the node pool was last updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`labels` |  `map (key: string, value: string)` Labels associated with this resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`hostedNode` |  `string` Canonical resource name of the node that this machine is responsible for hosting e.g. projects/{project}/locations/{location}/clusters/{clusterId}/nodePools/{pool_id}/{node}, Or empty if the machine is not assigned to assume the role of a node.For control plane nodes hosted on edge machines, this will return the following format: "projects/{project}/locations/{location}/clusters/{clusterId}/controlPlaneNodes/{node}".  
`zone` |  `string` The Google Distributed Cloud Edge zone of this machine.  
`version` |  `string` Output only. The software version of the machine.  
`disabled` |  `boolean` Output only. Whether the machine is disabled. If disabled, the machine is unable to enter service.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs/reference/container/rest/v1/projects.locations.machines/get)`

|  Gets details of a single Machine.  
  
### `[list](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs/reference/container/rest/v1/projects.locations.machines/list)`

|  Lists Machines in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
