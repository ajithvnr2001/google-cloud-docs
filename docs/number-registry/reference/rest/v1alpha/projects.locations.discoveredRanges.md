---
url: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges
title: REST Resource: projects.locations.discoveredRanges \u00a0|\u00a0 Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:43:09.214920+00:00
---

# REST Resource: projects.locations.discoveredRanges  |  Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Reference ](https://docs.cloud.google.com/number-registry/apis)



Send feedback 

#  REST Resource: projects.locations.discoveredRanges Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DiscoveredRange
    * JSON representation
  * Methods



## Resource: DiscoveredRange

A DiscoveredRange represents an IP address range automatically detected by the discovery pipeline.

JSON representation  
---  
      
    
    {
      "name": string,
      "realm": string,
      "parentRange": string,
      "registryBook": string,
      "description": string,
      "discoveryMetadata": {
        object ([DiscoveryMetadata](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/DiscoveryMetadata))
      },
      "attributes": [
        {
          object ([Attribute](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/Attribute))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "childCidrOverlapAllowed": boolean,
    
      // Union field ip_cidr_range can be only one of the following:
      "ipv4CidrRange": string,
      "ipv6CidrRange": string
      // End of list of possible types for union field ip_cidr_range.
    }  
  
Fields  
---  
`name` |  `string` Required. Identifier. The resource name of the DiscoveredRange, in the format `projects/{project}/locations/{location}/discoveredRanges/{discoveredRange}`.  
`realm` |  `string` Optional. The Realm of the DiscoveredRange.  
`parentRange` |  `string` Optional. The resource name of the parent DiscoveredRange, in the format `projects/{project}/locations/{location}/discoveredRanges/{discoveredRange}`.  
`registryBook` |  `string` Output only. The RegistryBook of the DiscoveredRange.  
`description` |  `string` Optional. Description of the DiscoveredRange.  
`discoveryMetadata` |  `object (`[DiscoveryMetadata](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/DiscoveryMetadata)`)` Output only. Owner metadata for this DiscoveredRange. A unique set of metadata is associated with each DiscoveredRange. If an IP range is shared by multiple resources (e.g., an Address resource and an Instance resource, or multiple ForwardingRules),separate DiscoveredRanges are created, each with a distinct owner. This ensures each DiscoveredRange has its own unique set of attributes, labels, create time and update time.  
`attributes[]` |  `object (`[Attribute](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/Attribute)`)` Optional. The attributes of the DiscoveredRange.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the DiscoveredRange was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the DiscoveredRange was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. User-defined labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`childCidrOverlapAllowed` |  `boolean` Output only. If true, allows child DiscoveredRanges of this DiscoveredRange to overlap with each other.  
Union field `ip_cidr_range`. The IP CIDR range of the DiscoveredRange. `ip_cidr_range` can be only one of the following:  
`ipv4CidrRange` |  `string` Optional. The IPv4 CIDR range of the DiscoveredRange.  
`ipv6CidrRange` |  `string` Optional. The IPv6 CIDR range of the DiscoveredRange.  
  
## Methods  
  
---  
  
### `[findFreeIpRanges](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges/findFreeIpRanges)`

|  Finds free IP ranges in a single DiscoveredRange.  
  
### `[get](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges/get)`

|  Gets details of a single DiscoveredRange.  
  
### `[list](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges/list)`

|  Lists DiscoveredRanges in a given project and location.  
  
### `[showUtilization](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges/showUtilization)`

|  Gets the details of a single DiscoveredRange and its utilization.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
