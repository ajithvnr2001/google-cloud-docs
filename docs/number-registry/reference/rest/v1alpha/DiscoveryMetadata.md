---
url: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/DiscoveryMetadata/
title: DiscoveryMetadata \u00a0|\u00a0 Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:35.930797+00:00
---

# DiscoveryMetadata  |  Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/DiscoveryMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Reference ](https://docs.cloud.google.com/number-registry/apis)



Send feedback 

#  DiscoveryMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ResourceState



Metadata about a discovered resource, tracking event times, state, and source information.

JSON representation  
---  
      
    
    {
      "eventTime": string,
      "createTime": string,
      "updateTime": string,
      "state": enum ([ResourceState](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/DiscoveryMetadata#ResourceState)),
      "resource": string,
      "resourceUri": string,
      "sourceId": string,
      "sourceSubId": string
    }  
  
Fields  
---  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the event happened.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the resource was last modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[ResourceState](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/DiscoveryMetadata#ResourceState)`)` Output only. The state of the resource.  
`resource` |  `string` Output only. The resource name of the discovered resource, should be API-agnostic. Example: "projects/{project_number}/networks/{network_id}".  
`resourceUri` |  `string` Output only. The resource uri of the discovered resource.  
`sourceId` |  `string` Output only. The canonical google.aip.dev/122 name of the source resource.  
`sourceSubId` |  `string` Output only. A single source resource can be the source of multiple CNR resources. This sub_id is used to distinguish between the different CNR resources derived from the same upstream resource. For example, a single subnetwork can be the source of multiple Ranges, one for each protocol. In this case, the sub_id could be "private-ipv4" or "private-ipv6".  
  
## ResourceState

The state of the resource.

Enums  
---  
`RESOURCE_STATE_UNSPECIFIED` | Unspecified state.  
`INVALID` | The resource is in an invalid state.  
`EXISTS` | The resource exists in the backing store (is not tombstoned or completely missing) and there were no failures reading out the resource level metadata.  
`DOES_NOT_EXIST` | Resource does not exist or has been deleted or soft-deleted.  
`ERROR` | There was an error reading out the resource level metadata.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
