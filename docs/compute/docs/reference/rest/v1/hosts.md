---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/hosts/
title: REST Resource: hosts \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:42.804329+00:00
---

# REST Resource: hosts  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/hosts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: hosts Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: HostsGetResponse
    * JSON representation
      * JSON representation
  * Methods



## Resource: HostsGetResponse

JSON representation  
---  
      
    
    {
      "resource": {
        "kind": string,
        "id": string,
        "creationTimestamp": string,
        "name": string,
        "zone": string,
        "selfLink": string,
        "selfLinkWithId": string,
        "aliasLinks": [
          string
        ],
        "description": string,
        "state": enum,
        "status": {
          "physicalTopology": {
            "cluster": string,
            "block": string,
            "subBlock": string,
            "host": string
          },
          "runningInstances": [
            string
          ]
        }
      },
      "etag": string
    }  
  
Fields  
---  
`resource` |  `object`  
`resource.kind` |  `string` Output only. The type of resource. Always `compute#host` for hosts.  
`resource.id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for this resource. This identifier is defined by the server.  
`resource.creationTimestamp` |  `string` Output only. The creation timestamp, formatted as [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text.  
`resource.name` |  `string` Output only. The name of the host.  
`resource.zone` |  `string` Output only. The zone in which the host resides.  
`resource.selfLink` |  `string` Output only. The self link of the host.  
`resource.selfLinkWithId` |  `string` Output only. The self link with id of the host.  
`resource.aliasLinks[]` |  `string` Output only. All aliases for this resource. e.g. projects/123/zones/us-centra1-a/reservation/r1/reservationBlock/b1/hosts/h1  
`resource.description` |  `string` An optional description of this resource.  
`resource.state` |  `enum` Output only. The state of the host.  
`resource.status` |  `object` Output only. The status of the host  
`resource.status.physicalTopology` |  `object` Output only. The physical topology of the reservation sub-block, if present  
`resource.status.physicalTopology.cluster` |  `string` The cluster name of the reservation sub-block.  
`resource.status.physicalTopology.block` |  `string` The unique identifier of the capacity block within the cluster.  
`resource.status.physicalTopology.subBlock` |  `string` The unique identifier of the capacity sub-block within the capacity block.  
`resource.status.physicalTopology.host` |  `string` The unique identifier of the capacity host within the capacity sub-block.  
`resource.status.runningInstances[]` |  `string` Output only. The URIs of the instances currently running on this host.  
`etag` |  `string` end_interface: MixerGetResponseWithEtagBuilder  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/hosts/get)`

|  Retrieves information about the specified host.  
  
### `[getVersion](https://docs.cloud.google.com/compute/docs/reference/rest/v1/hosts/getVersion)`

|  Allows customers to get SBOM versions of a host.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/v1/hosts/list)`

|  Retrieves a list of hosts.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-14 UTC."],[],[]] 
