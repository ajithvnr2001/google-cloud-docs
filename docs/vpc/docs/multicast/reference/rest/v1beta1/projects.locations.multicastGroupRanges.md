---
url: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRanges
title: REST Resource: projects.locations.multicastGroupRanges \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:29:10.589360+00:00
---

# REST Resource: projects.locations.multicastGroupRanges  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRanges

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Reference ](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest)



Send feedback 

#  REST Resource: projects.locations.multicastGroupRanges Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MulticastGroupRange
    * JSON representation
  * DistributionScope
  * Methods



## Resource: MulticastGroupRange

Multicast group range resource.

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
      "reservedInternalRange": string,
      "multicastDomain": string,
      "ipCidrRange": string,
      "description": string,
      "uniqueId": string,
      "consumerAcceptList": [
        string
      ],
      "requireExplicitAccept": boolean,
      "logConfig": {
        object ([MulticastLogConfig](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/MulticastLogConfig))
      },
      "distributionScope": enum ([DistributionScope](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRanges#DistributionScope))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the multicast group range. Use the following format: `projects/*/locations/global/multicastGroupRanges/*`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] The timestamp when the multicast group range was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] The timestamp when the multicast group range was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `object (`[MulticastResourceState](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/MulticastResourceState)`)` Output only. [Output only] The state of the resource.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key-value pairs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`reservedInternalRange` |  `string` Required. The resource name of the internal range reserved for this multicast group range.The internal range must be a Class D address (224.0.0.0 to 239.255.255.255) and have a prefix length >= 23.Use the following format: `projects/*/locations/global/internalRanges/*`.  
`multicastDomain` |  `string` Required. The resource name of the multicast domain in which to create this multicast group range. Use the following format: `projects/*/locations/global/multicastDomains/*`.  
`ipCidrRange` |  `string` Output only. [Output only] The multicast group IP address range.  
`description` |  `string` Optional. An optional text description of the multicast group range.  
`uniqueId` |  `string` Output only. [Output only] The Google-generated UUID for the resource. This value is unique across all multicast group range resources. If a group range is deleted and another with the same name is created, the new group range is assigned a different uniqueId.  
`consumerAcceptList[]` |  `string` Optional. A list of consumer projects that are allowed to subscribe to the multicast IP addresses within the range defined by this MulticastGroupRange. The project can be specified using its project ID or project number. If left empty, then all consumer projects are allowed (unless requireExplicitAccept is set to true) once they have VPC networks associated to the multicast domain. The current max length of the accept list is 100.  
`requireExplicitAccept` |  `boolean` Optional. Whether an empty consumerAcceptList will deny all consumer projects.  
`logConfig` |  `object (`[MulticastLogConfig](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/MulticastLogConfig)`)` Optional. Specifies the logging options for the activities performed related to all the multicast group range activations associated with the multicast group range. Defaults to false. If logging is enabled, logs are exported to Cloud Logging.  
`distributionScope` |  `enum (`[DistributionScope](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRanges#DistributionScope)`)` Optional. Multicast group range's distribution scope. Intra-zone or intra-region cross-zone is supported, with default value being intra-region. Cross region distribution is not supported.  
  
## DistributionScope

Multicast group range's distribution scope.

Enums  
---  
`DISTRIBUTION_SCOPE_UNSPECIFIED` | Unspecified value means no restriction, hence the broadest scope supported by the system applies.  
`INTRA_ZONE` | Multicast traffic is distributed from source to only subscribers in the same zone.  
`INTRA_REGION` | Multicast traffic is distributed from source to subscribers in any zone in the same region.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRanges/create)`

|  Creates a new multicast group range in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRanges/delete)`

|  Deletes a single multicast group range.  
  
### `[get](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRanges/get)`

|  Gets details of a single multicast group range.  
  
### `[list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRanges/list)`

|  Lists multicast group ranges in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupRanges/patch)`

|  Updates the parameters of a single multicast group range.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-22 UTC."],[],[]] 
