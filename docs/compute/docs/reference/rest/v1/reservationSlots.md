---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservationSlots/
title: REST Resource: reservationSlots \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:16.468014+00:00
---

# REST Resource: reservationSlots  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservationSlots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: reservationSlots Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ReservationSlotsGetResponse
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Methods



## Resource: ReservationSlotsGetResponse

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
        "physicalTopology": {
          "cluster": string,
          "block": string,
          "subBlock": string,
          "host": string
        },
        "state": enum,
        "status": {
          "physicalTopology": {
            "cluster": string,
            "block": string,
            "subBlock": string,
            "host": string
          },
          "rdmaIpAddresses": [
            string
          ],
          "runningInstances": [
            string
          ]
        },
        "shareSettings": {
          "shareType": enum,
          "projectMap": {
            string: {
              "projectId": string
            },
            ...
          }
        }
      }
    }  
  
Fields  
---  
`resource` |  `object`  
`resource.kind` |  `string` Output only. The type of resource. Always `compute#reservationSlot` for reservation slots.  
`resource.id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for this resource. This identifier is defined by the server.  
`resource.creationTimestamp` |  `string` Output only. The creation timestamp, formatted as [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text.  
`resource.name` |  `string` Output only. The name of the reservation slot.  
`resource.zone` |  `string` Output only. The zone in which the reservation slot resides.  
`resource.selfLink` |  `string` Output only. A server-defined fully-qualified URL for this resource.  
`resource.selfLinkWithId` |  `string` Output only. A server-defined URL for this resource with the resource ID.  
`resource.physicalTopology  
**(deprecated)**` |  `object` Output only. The physical topology of the reservation slot.  
`resource.physicalTopology  
**(deprecated)**.cluster` |  `string` The cluster name of the reservation sub-block.  
`resource.physicalTopology  
**(deprecated)**.block` |  `string` The unique identifier of the capacity block within the cluster.  
`resource.physicalTopology  
**(deprecated)**.subBlock` |  `string` The unique identifier of the capacity sub-block within the capacity block.  
`resource.physicalTopology  
**(deprecated)**.host` |  `string` The unique identifier of the capacity host within the capacity sub-block.  
`resource.state` |  `enum` Output only. The state of the reservation slot.  
`resource.status` |  `object` Output only. The status of the reservation slot.  
`resource.status.physicalTopology` |  `object` Output only. The physical topology of the reservation sub-block.  
`resource.status.physicalTopology.cluster` |  `string` The cluster name of the reservation sub-block.  
`resource.status.physicalTopology.block` |  `string` The unique identifier of the capacity block within the cluster.  
`resource.status.physicalTopology.subBlock` |  `string` The unique identifier of the capacity sub-block within the capacity block.  
`resource.status.physicalTopology.host` |  `string` The unique identifier of the capacity host within the capacity sub-block.  
`resource.status.rdmaIpAddresses[]` |  `string` Output only. The RDMA IP address of the physical host.  
`resource.status.runningInstances[]` |  `string` Output only. The URIs of the instances currently running on this slot.  
`resource.shareSettings` |  `object` Specify share settings to create a shared slot. Set to empty to inherit the share settings from a parent resource.  
`resource.shareSettings.shareType` |  `enum` Type of sharing for this shared-reservation  
`resource.shareSettings.projectMap[]` |  `map (key: string, value: object)` A map of project id and project config. This is only valid when shareType's value is SPECIFIC_PROJECTS.  
`resource.shareSettings.projectMap[].projectId` |  `string` The project ID, should be same as the key of this project config in the parent map.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservationSlots/get)`

|  Retrieves information about the specified reservation slot.  
  
### `[getHealth](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservationSlots/getHealth)`

|  Get health info on a reservation slot.  
  
### `[getVersion](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservationSlots/getVersion)`

|  Allows customers to get SBOM versions of a reservation slot.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservationSlots/list)`

|  Retrieves a list of reservation slots under a single reservation.  
  
### `[update](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservationSlots/update)`

|  Update a reservation slot in the specified sub-block.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-07 UTC."],[],[]] 
