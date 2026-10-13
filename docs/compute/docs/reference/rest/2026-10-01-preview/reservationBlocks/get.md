---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/reservationBlocks/get/
title: Method: reservationBlocks.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:16.654539+00:00
---

# Method: reservationBlocks.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/reservationBlocks/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: reservationBlocks.get Stay organized with collections  Save and categorize content based on your preferences. 

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
  * Authorization scopes
  * Try it!



API Version : 2026-10-01-preview

Retrieves information about the specified reservation block.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/zones/{zone}/reservations/{reservation}/reservationBlocks/{reservationBlock}?$apiVersion=2026-10-01-preview`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`zone` |  `string` Name of the zone for this request. Zone name should conform to RFC1035.  
`reservation` |  `string` The name of the reservation. Name should conform to RFC1035 or be a resource ID. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `reservation`:

  * `compute.reservationBlocks.get`

  
`reservationBlock` |  `string` The name of the reservation block. Name should conform to RFC1035 or be a resource ID.  
  
### Query parameters

Parameters  
---  
`view` |  `enum` View of the Block.  
  
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
        "reservationMaintenance": {
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
          "instances": [
            {
              "instanceId": string,
              "projectId": string,
              "physicalHostTopology": {
                "subBlock": string,
                "host": string
              }
            }
          ]
        },
        "reservationSubBlockCount": integer,
        "reservationSubBlockInUseCount": integer,
        "inUseHostCount": integer,
        "healthInfo": {
          "healthStatus": enum,
          "healthySubBlockCount": integer,
          "degradedSubBlockCount": integer
        }
      }
    }  
  
Fields  
---  
`resource` |  `object`  
`resource.kind` |  `string` Output only. Type of the resource. Always `compute#reservationBlock` for reservation blocks.  
`resource.id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`resource.creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`resource.name` |  `string` Output only. The name of this reservation block generated by Google Compute Engine. The name must be 1-63 characters long, and comply with RFC1035 @pattern [a-z](https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/reservationBlocks/get?:\[-a-z0-9\]{0,61}\[a-z0-9\])?  
`resource.zone` |  `string` Output only. Zone in which the reservation block resides.  
`resource.selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`resource.selfLinkWithId` |  `string` Output only. Server-defined URL for this resource with the resource id.  
`resource.count` |  `integer` Output only. The number of resources that are allocated in this reservation block.  
`resource.inUseCount` |  `integer` Output only. The number of instances that are currently in use on this reservation block.  
`resource.reservationMaintenance` |  `object` Output only. Maintenance information for this reservation block.  
`resource.reservationMaintenance.upcomingGroupMaintenance` |  `object` Maintenance information on this group of VMs.  
`resource.reservationMaintenance.upcomingGroupMaintenance.type` |  `enum` Defines the type of maintenance.  
`resource.reservationMaintenance.upcomingGroupMaintenance.canReschedule` |  `boolean` Indicates if the maintenance can be customer triggered.  
`resource.reservationMaintenance.upcomingGroupMaintenance.windowStartTime` |  `string` The current start time of the maintenance window. This timestamp value is in RFC3339 text format.  
`resource.reservationMaintenance.upcomingGroupMaintenance.windowEndTime` |  `string` The time by which the maintenance disruption will be completed. This timestamp value is in RFC3339 text format.  
`resource.reservationMaintenance.upcomingGroupMaintenance.latestWindowStartTime` |  `string` The latest time for the planned maintenance window to start. This timestamp value is in RFC3339 text format.  
`resource.reservationMaintenance.upcomingGroupMaintenance.maintenanceStatus` |  `enum`  
`resource.reservationMaintenance.upcomingGroupMaintenance.maintenanceOnShutdown` |  `boolean` Indicates whether the UpcomingMaintenance will be triggered on VM shutdown.  
`resource.reservationMaintenance.upcomingGroupMaintenance.maintenanceReasons[]` |  `enum` The reasons for the maintenance. Only valid for vms.  
`resource.reservationMaintenance.maintenanceOngoingCount` |  `integer` Progress for ongoing maintenance for this group of VMs/hosts. Describes number of hosts in the block that have ongoing maintenance.  
`resource.reservationMaintenance.maintenancePendingCount` |  `integer` Progress for ongoing maintenance for this group of VMs/hosts. Describes number of hosts in the block that have pending maintenance.  
`resource.reservationMaintenance.schedulingType` |  `enum` The type of maintenance for the reservation.  
`resource.reservationMaintenance.subblockInfraMaintenanceOngoingCount` |  `integer` Describes number of subblock Infrastructure that has ongoing maintenance. Here, Subblock Infrastructure Maintenance pertains to upstream hardware contained in the Subblock that is necessary for a VM Family(e.g. NVLink Domains). Not all VM Families will support this field.  
`resource.reservationMaintenance.subblockInfraMaintenancePendingCount` |  `integer` Describes number of subblock Infrastructure that has pending maintenance. Here, Subblock Infrastructure Maintenance pertains to upstream hardware contained in the Subblock that is necessary for a VM Family (e.g. NVLink Domains). Not all VM Families will support this field.  
`resource.reservationMaintenance.instanceMaintenanceOngoingCount` |  `integer` Describes number of instances that have ongoing maintenance.  
`resource.reservationMaintenance.instanceMaintenancePendingCount` |  `integer` Describes number of instances that have pending maintenance.  
`resource.status` |  `enum` Output only. Status of the reservation block.  
`resource.physicalTopology` |  `object` Output only. The physical topology of the reservation block.  
`resource.physicalTopology.cluster` |  `string` The cluster name of the reservation block.  
`resource.physicalTopology.block` |  `string` The hash of the capacity block within the cluster.  
`resource.physicalTopology.instances[]` |  `object` Output only. The detailed instances information for a given Block  
`resource.physicalTopology.instances[].instanceId` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` The InstanceId of the instance  
`resource.physicalTopology.instances[].projectId` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Project where the instance lives  
`resource.physicalTopology.instances[].physicalHostTopology` |  `object` Output only. The PhysicalHostTopology of instances within a Block resource.  
`resource.physicalTopology.instances[].physicalHostTopology.subBlock` |  `string` Sub block hash for a given instance  
`resource.physicalTopology.instances[].physicalHostTopology.host` |  `string` Host hash for a given instance  
`resource.reservationSubBlockCount` |  `integer` Output only. The number of reservation subBlocks associated with this reservation block.  
`resource.reservationSubBlockInUseCount` |  `integer` Output only. The number of in-use reservation subBlocks associated with this reservation block. If at least one VM is running on a subBlock, it is considered in-use.  
`resource.inUseHostCount` |  `integer` Output only. Number of hosts currently in use. If there is one or more Instances running on the host, it is considered in use.  
`resource.healthInfo` |  `object` Output only. Health information for the reservation block.  
`resource.healthInfo.healthStatus` |  `enum` The health status of the reservation block.  
`resource.healthInfo.healthySubBlockCount` |  `integer` The number of subBlocks that are healthy.  
`resource.healthInfo.degradedSubBlockCount` |  `integer` The number of subBlocks that are degraded.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
