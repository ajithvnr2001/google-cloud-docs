---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservationSubBlocks/get/
title: Method: reservationSubBlocks.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:22:17.604362+00:00
---

# Method: reservationSubBlocks.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservationSubBlocks/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: reservationSubBlocks.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
        * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Retrieves information about the specified reservation subBlock.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/zones/{zone}/{parentName=reservations/*/reservationBlocks/*}/reservationSubBlocks/{reservationSubBlock}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`zone` |  `string` Name of the zone for this request. Zone name should conform to RFC1035.  
`parentName` |  `string` The name of the parent reservation and parent block. In the format of reservations/{reservationName}/reservationBlocks/{reservation_block_name}  
`reservationSubBlock` |  `string` The name of the reservation subBlock. Name should conform to RFC1035 or be a resource ID.  
  
### Query parameters

Parameters  
---  
`view` |  `enum` View of the subBlock.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

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
        "count": integer,
        "inUseCount": integer,
        "reservationSubBlockMaintenance": {
          "upcomingGroupMaintenance": {
            "type": enum,
            "canReschedule": boolean,
            "windowStartTime": string,
            "windowEndTime": string,
            "latestWindowStartTime": string,
            "maintenanceStatus": enum,
            "maintenanceOnShutdown": boolean,
            "maintenanceReasons": [
              enum
            ]
          },
          "maintenanceOngoingCount": integer,
          "maintenancePendingCount": integer,
          "schedulingType": enum,
          "subblockInfraMaintenanceOngoingCount": integer,
          "subblockInfraMaintenancePendingCount": integer,
          "instanceMaintenanceOngoingCount": integer,
          "instanceMaintenancePendingCount": integer
        },
        "status": enum,
        "physicalTopology": {
          "cluster": string,
          "block": string,
          "subBlock": string
        },
        "inUseHostCount": integer,
        "healthInfo": {
          "healthStatus": enum,
          "healthyHostCount": integer,
          "degradedHostCount": integer,
          "healthyInfraCount": integer,
          "degradedInfraCount": integer
        },
        "acceleratorTopologiesInfo": {
          "acceleratorTopologyInfos": [
            {
              "acceleratorTopology": string,
              "infoPerTopologyStates": [
                {
                  "state": enum,
                  "count": integer
                }
              ]
            }
          ]
        }
      }
    }  
  
Fields  
---  
`resource` |  `object`  
`resource.kind` |  `string` Output only. Type of the resource. Always `compute#reservationSubBlock` for reservation subBlocks.  
`resource.id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`resource.creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`resource.name` |  `string` Output only. The name of this reservation subBlock generated by Google Compute Engine. The name must be 1-63 characters long, and comply with RFC1035 @pattern [a-z](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservationSubBlocks/get?:\[-a-z0-9\]{0,61}\[a-z0-9\])?  
`resource.zone` |  `string` Output only. Zone in which the reservation subBlock resides.  
`resource.selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`resource.selfLinkWithId` |  `string` Output only. Server-defined URL for this resource with the resource id.  
`resource.count` |  `integer` Output only. The number of hosts that are allocated in this reservation subBlock.  
`resource.inUseCount` |  `integer` Output only. The number of instances that are currently in use on this reservation subBlock.  
`resource.reservationSubBlockMaintenance` |  `object` Output only. Maintenance information for this reservation subBlock.  
`resource.reservationSubBlockMaintenance.upcomingGroupMaintenance` |  `object` Maintenance information on this group of VMs.  
`resource.reservationSubBlockMaintenance.upcomingGroupMaintenance.type` |  `enum` Defines the type of maintenance.  
`resource.reservationSubBlockMaintenance.upcomingGroupMaintenance.canReschedule` |  `boolean` Indicates if the maintenance can be customer triggered.  
`resource.reservationSubBlockMaintenance.upcomingGroupMaintenance.windowStartTime` |  `string` The current start time of the maintenance window. This timestamp value is in RFC3339 text format.  
`resource.reservationSubBlockMaintenance.upcomingGroupMaintenance.windowEndTime` |  `string` The time by which the maintenance disruption will be completed. This timestamp value is in RFC3339 text format.  
`resource.reservationSubBlockMaintenance.upcomingGroupMaintenance.latestWindowStartTime` |  `string` The latest time for the planned maintenance window to start. This timestamp value is in RFC3339 text format.  
`resource.reservationSubBlockMaintenance.upcomingGroupMaintenance.maintenanceStatus` |  `enum`  
`resource.reservationSubBlockMaintenance.upcomingGroupMaintenance.maintenanceOnShutdown` |  `boolean` Indicates whether the UpcomingMaintenance will be triggered on VM shutdown.  
`resource.reservationSubBlockMaintenance.upcomingGroupMaintenance.maintenanceReasons[]` |  `enum` The reasons for the maintenance. Only valid for vms.  
`resource.reservationSubBlockMaintenance.maintenanceOngoingCount` |  `integer` Progress for ongoing maintenance for this group of VMs/hosts. Describes number of hosts in the block that have ongoing maintenance.  
`resource.reservationSubBlockMaintenance.maintenancePendingCount` |  `integer` Progress for ongoing maintenance for this group of VMs/hosts. Describes number of hosts in the block that have pending maintenance.  
`resource.reservationSubBlockMaintenance.schedulingType` |  `enum` The type of maintenance for the reservation.  
`resource.reservationSubBlockMaintenance.subblockInfraMaintenanceOngoingCount` |  `integer` Describes number of subblock Infrastructure that has ongoing maintenance. Here, Subblock Infrastructure Maintenance pertains to upstream hardware contained in the Subblock that is necessary for a VM Family(e.g. NVLink Domains). Not all VM Families will support this field.  
`resource.reservationSubBlockMaintenance.subblockInfraMaintenancePendingCount` |  `integer` Describes number of subblock Infrastructure that has pending maintenance. Here, Subblock Infrastructure Maintenance pertains to upstream hardware contained in the Subblock that is necessary for a VM Family (e.g. NVLink Domains). Not all VM Families will support this field.  
`resource.reservationSubBlockMaintenance.instanceMaintenanceOngoingCount` |  `integer` Describes number of instances that have ongoing maintenance.  
`resource.reservationSubBlockMaintenance.instanceMaintenancePendingCount` |  `integer` Describes number of instances that have pending maintenance.  
`resource.status` |  `enum` Output only. Status of the reservation subBlock.  
`resource.physicalTopology` |  `object` Output only. The physical topology of the reservation subBlock.  
`resource.physicalTopology.cluster` |  `string` The cluster name of the reservation subBlock.  
`resource.physicalTopology.block` |  `string` The hash of the capacity block within the cluster.  
`resource.physicalTopology.subBlock` |  `string` The hash of the capacity sub-block within the capacity block.  
`resource.inUseHostCount` |  `integer` Output only. Number of hosts currently in use. If there is one or more Instances running on the host, it is considered in use.  
`resource.healthInfo` |  `object` Output only. Health information for the reservation subBlock.  
`resource.healthInfo.healthStatus` |  `enum` The health status of the reservation subBlock.  
`resource.healthInfo.healthyHostCount` |  `integer` The number of healthy hosts in the reservation subBlock.  
`resource.healthInfo.degradedHostCount` |  `integer` The number of degraded hosts in the reservation subBlock.  
`resource.healthInfo.healthyInfraCount` |  `integer` The number of healthy infrastructure (e.g NV link domain) in the reservation subblock.  
`resource.healthInfo.degradedInfraCount` |  `integer` The number of degraded infrastructure (e.g NV link domain) in the reservation subblock.  
`resource.acceleratorTopologiesInfo` |  `object` Output only. Slice info for the reservation subBlock.  
`resource.acceleratorTopologiesInfo.acceleratorTopologyInfos[]` |  `object` Info for each accelerator topology.  
`resource.acceleratorTopologiesInfo.acceleratorTopologyInfos[].acceleratorTopology` |  `string` The accelerator topology.  
`resource.acceleratorTopologiesInfo.acceleratorTopologyInfos[].infoPerTopologyStates[]` |  `object` Info for each topology state.  
`resource.acceleratorTopologiesInfo.acceleratorTopologyInfos[].infoPerTopologyStates[].state` |  `enum` The state of the accelerator topology.  
`resource.acceleratorTopologiesInfo.acceleratorTopologyInfos[].infoPerTopologyStates[].count` |  `integer` The number of accelerator topologies in this state.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.reservationSubBlocks.get`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
