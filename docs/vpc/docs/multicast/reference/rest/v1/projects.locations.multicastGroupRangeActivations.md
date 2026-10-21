---
url: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations
title: REST Resource: projects.locations.multicastGroupRangeActivations \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:29:02.895745+00:00
---

# REST Resource: projects.locations.multicastGroupRangeActivations  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Reference ](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest)



Send feedback 

#  REST Resource: projects.locations.multicastGroupRangeActivations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MulticastGroupRangeActivation
    * JSON representation
  * Methods



## Resource: MulticastGroupRangeActivation

Multicast group range activation resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "state": {
        object ([MulticastResourceState](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/MulticastResourceState))
      },
      "description": string,
      "labels": {
        string: string,
        ...
      },
      "multicastDomainActivation": string,
      "multicastGroupRange": string,
      "ipCidrRange": string,
      "multicastGroupConsumerActivations": [
        string
      ],
      "uniqueId": string,
      "logConfig": {
        object ([MulticastLogConfig](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/MulticastLogConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the multicast group range activation. Use the following format: `projects/*/locations/*/multicastGroupRangeActivations/*`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] The timestamp when the multicast group range activation was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] The timestamp when the multicast group range activation was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `object (`[MulticastResourceState](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/MulticastResourceState)`)` Output only. [Output only] The state of the resource.  
`description` |  `string` Optional. An optional text description of the multicast group range activation.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key-value pairs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`multicastDomainActivation` |  `string` Optional. The resource name of a multicast domain activation that is in the same zone as this multicast group. Use the following format: `projects/*/locations/*/multicastDomainActivations/*`  
`multicastGroupRange` |  `string` Optional. The resource name of the global multicast group range for the group. Use the following format: `projects/*/locations/global/multicastGroupRanges/*`  
`ipCidrRange` |  `string` Output only. [Output only] The multicast group IP address range.  
`multicastGroupConsumerActivations[]` |  `string` Output only. The resource names of associated multicast group consumer activations. Use the following format: `projects/*/locations/*/multicastGroupConsumerActivations/*`.  
`uniqueId` |  `string` Output only. [Output only] The Google-generated UUID for the resource. This value is unique across all multicast group resources. If a group is deleted and another with the same name is created, the new group is assigned a different uniqueId.  
`logConfig` |  `object (`[MulticastLogConfig](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/MulticastLogConfig)`)` Optional. Specifies the logging options for the activities performed regarding the multicast group range activation. Defaults to false. If not specified, inherit the logging options from the global multicast group range resource. If logging is enabled, logs are exported to Cloud Logging. If the log config is explicitly set for the multicast group range activation, regardless if it is enabled or not, the value overrides what is configured by the multicast group range resource.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations/create)`

|  Creates a new multicast group range activation in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations/delete)`

|  Deletes a single multicast group range activation.  
  
### `[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations/get)`

|  Gets details of a single multicast group range activation.  
  
### `[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations/list)`

|  Lists multicast group range activationsin a given project and location.  
  
### `[patch](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations/patch)`

|  Updates the parameters of a single multicast group range activation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-22 UTC."],[],[]] 
