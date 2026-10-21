---
url: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainActivations
title: REST Resource: projects.locations.multicastDomainActivations \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:29:06.029974+00:00
---

# REST Resource: projects.locations.multicastDomainActivations  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainActivations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Reference ](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest)



Send feedback 

#  REST Resource: projects.locations.multicastDomainActivations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MulticastDomainActivation
    * JSON representation
  * TrafficSpec
    * JSON representation
  * Methods



## Resource: MulticastDomainActivation

Multicast domain activation resource.

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
      "multicastDomain": string,
      "adminNetwork": string,
      "description": string,
      "multicastConsumerAssociations": [
        string
      ],
      "uniqueId": string,
      "trafficSpec": {
        object ([TrafficSpec](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainActivations#TrafficSpec))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the multicast domain activation. Use the following format: `projects/*/locations/*/multicastDomainActivations/*`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] The timestamp when the multicast domain activation was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] The timestamp when the multicast domain activation was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `object (`[MulticastResourceState](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/MulticastResourceState)`)` Output only. [Output only] The state of the resource.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key-value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`multicastDomain` |  `string` Optional. The resource name of the multicast domain to activate. Use the following format: `projects/*/locations/global/multicastDomains/*`.  
`adminNetwork` |  `string` Output only. [Output only] The URL of the admin network.  
`description` |  `string` Optional. An optional text description of the multicast domain activation.  
`multicastConsumerAssociations[]` |  `string` Output only. The resource names of associated multicast consumer associations. Use the following format: `projects/*/locations/*/multicastConsumerAssociations/*`.  
`uniqueId` |  `string` Output only. [Output only] The Google-generated UUID for the resource. This value is unique across all multicast domain activation resources. If a domain activation is deleted and another with the same name is created, the new domain activation is assigned a different uniqueId.  
`trafficSpec` |  `object (`[TrafficSpec](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainActivations#TrafficSpec)`)` Optional. The traffic specification for the multicast domain activation.  
  
## TrafficSpec

Specifies the traffic volume and multicast group scale parameters that are used to set up multicast infrastructure for a multicast domain in a zone.

JSON representation  
---  
      
    
    {
      "aggrEgressPps": string,
      "aggrIngressPps": string,
      "avgPacketSize": integer,
      "maxPerGroupIngressPps": string,
      "maxPerGroupSubscribers": string
    }  
  
Fields  
---  
`aggrEgressPps` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Aggregated egress Packet-Per-Second for all multicast groups in the domain in this zone.  
`aggrIngressPps` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Aggregated ingress Packet-Per-Second for all multicast groups in the domain in this zone. Default to (aggregated_egress_pps / maxPerGroupSubscribers) * 2.  
`avgPacketSize` |  `integer` Optional. Average packet size (Default to 512 bytes).  
`maxPerGroupIngressPps` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Maximum ingress Packet-Per-Second for a single multicast group in this zone. Default to aggregated_ingress_pps / 2.  
`maxPerGroupSubscribers` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Maximum number of subscribers for a single multicast group in this zone. Default to max(50, aggregated_egress_pps / aggregated_ingress_pps).  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainActivations/create)`

|  Creates a new multicast domain activation in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainActivations/delete)`

|  Deletes a single multicast domain activation.  
  
### `[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainActivations/get)`

|  Gets details of a single multicast domain activation.  
  
### `[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainActivations/list)`

|  Lists multicast domain activations in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastDomainActivations/patch)`

|  Updates the parameters of a single multicast domain activation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-22 UTC."],[],[]] 
