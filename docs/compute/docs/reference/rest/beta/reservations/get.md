---
url: https://docs.cloud.google.com/compute/docs/reference/rest/beta/reservations/get/
title: Method: reservations.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:11.497432+00:00
---

# Method: reservations.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/beta/reservations/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: reservations.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Retrieves information about the specified reservation.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/beta/projects/{project}/zones/{zone}/reservations/{reservation}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`zone` |  `string` Name of the zone for this request.  
`reservation` |  `string` Name of the reservation to retrieve.  
  
### Request body

The request body must be empty.

### Response body

Represents a reservation resource. A reservation ensures that capacity is held in a specific zone even if the reserved VMs are not running. For more information, read [ Reserving zonal resources](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources).

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "selfLink": string,
      "zone": string,
      "description": string,
      "name": string,
      "commitment": string,
      "linkedCommitments": [
        string
      ],
      "specificReservationRequired": boolean,
      "status": enum,
      "shareSettings": {
        "shareType": enum,
        "projects": [
          string
        ],
        "projectMap": {
          string: {
            "projectId": string
          },
          ...
        },
        "folderMap": {
          string: {
            "folderId": string
          },
          ...
        }
      },
      "satisfiesPzs": boolean,
      "resourcePolicies": {
        string: string,
        ...
      },
      "resourceStatus": {
        "specificSkuAllocation": {
          "sourceInstanceTemplateId": string,
          "utilizations": {
            string: string,
            ...
          }
        },
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
        "reservationBlockCount": integer,
        "healthInfo": {
          "healthStatus": enum,
          "healthyBlockCount": integer,
          "degradedBlockCount": integer
        }
      },
      "reservationSharingPolicy": {
        "serviceShareType": enum
      },
      "deploymentType": enum,
      "advancedDeploymentControl": {
        "reservationOperationalMode": enum
      },
      "enableEmergentMaintenance": boolean,
      "reservationMode": enum,
      "protectionTier": enum,
      "schedulingType": enum,
      "params": {
        "resourceManagerTags": {
          string: string,
          ...
        }
      },
      "confidentialComputeType": enum,
      "earlyAccessMaintenance": enum,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "specificReservation": {
        "instanceProperties": {
          "machineType": string,
          "guestAccelerators": [
            {
              "acceleratorType": string,
              "acceleratorCount": integer
            }
          ],
          "minCpuPlatform": string,
          "localSsds": [
            {
              "diskSizeGb": string,
              "interface": enum
            }
          ],
          "maintenanceFreezeDurationHours": integer,
          "locationHint": string,
          "maintenanceInterval": enum
        },
        "count": string,
        "inUseCount": string,
        "assuredCount": string,
        "sourceInstanceTemplate": string
      },
      "aggregateReservation": {
        "vmFamily": enum,
        "reservedResources": [
          {
    
            // The following is a list of mutually exclusive fields. At most one of the
            // fields will be set in a response:
            "accelerator": {
              "acceleratorCount": integer,
              "acceleratorType": string
            }
            // End of mutually exclusive fields.
          }
        ],
        "inUseResources": [
          {
    
            // The following is a list of mutually exclusive fields. At most one of the
            // fields will be set in a response:
            "accelerator": {
              "acceleratorCount": integer,
              "acceleratorType": string
            }
            // End of mutually exclusive fields.
          }
        ],
        "workloadType": enum,
        "hostCount": integer,
        "inUseHostCount": integer,
        "inUseInstanceCount": integer
      }
      // End of mutually exclusive fields.
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "deleteAtTime": string,
      "deleteAfterDuration": {
        "seconds": string,
        "nanos": integer
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#reservations` for reservations.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`zone` |  `string` Zone in which the reservation resides. A zone must be provided if the reservation is created within a commitment.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`name` |  `string` The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`commitment` |  `string` Output only. Full or partial URL to a parent commitment. This field displays for reservations that are tied to a commitment.  
`linkedCommitments[]` |  `string` Output only. Full or partial URL to parent commitments. This field displays for reservations that are tied to multiple commitments.  
`specificReservationRequired` |  `boolean` Indicates whether the reservation can be consumed by VMs with affinity for "any" reservation. If the field is set, then only VMs that target the reservation by name can consume from this reservation.  
`status` |  `enum` Output only. The status of the reservation. 

  * `CREATING`: Reservation resources are being allocated.
  * `READY`: Reservation resources have been allocated, and the reservation is ready for use.
  * `DELETING`: Reservation deletion is in progress.
  * `UPDATING`: Reservation update is in progress.

  
`shareSettings` |  `object` Specify share-settings to create a shared reservation. This property is optional. For more information about the syntax and options for this field and its subfields, see the guide for [creating a shared reservation.](https://cloud.google.com/compute/docs/instances/reservations-shared#creating_a_shared_reservation)  
`shareSettings.shareType` |  `enum` Type of sharing for this shared-reservation  
`shareSettings.projects[]` |  `string` A reservations.list of Project names to specify consumer projects for this shared-reservation. This is only valid when shareType's value is SPECIFIC_PROJECTS.  
`shareSettings.projectMap[]` |  `map (key: string, value: object)` A map of project id and project config. This is only valid when shareType's value is SPECIFIC_PROJECTS.  
`shareSettings.projectMap[].projectId` |  `string` The project ID, should be same as the key of this project config in the parent map.  
`shareSettings.folderMap[]` |  `map (key: string, value: object)` A map of folder id and folder config to specify consumer projects for this shared-reservation. This is only valid when shareType's value is DIRECT_PROJECTS_UNDER_SPECIFIC_FOLDERS. Folder id should be a string of number, and without "folders/" prefix.  
`shareSettings.folderMap[].folderId` |  `string` The folder ID, should be same as the key of this folder config in the parent map. Folder id should be a string of number, and without "folders/" prefix.  
`satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`resourcePolicies` |  `map (key: string, value: string)` Resource policies to be added to this reservation. The key is defined by user, and the value is resource policy url. This is to define placement policy with reservation.  
`resourceStatus` |  `object` Output only. Status information for Reservation resource.  
`resourceStatus.specificSkuAllocation` |  `object` Allocation Properties of this reservation.  
`resourceStatus.specificSkuAllocation.sourceInstanceTemplateId` |  `string` ID of the instance template used to populate reservation properties.  
`resourceStatus.specificSkuAllocation.utilizations` |  `map (key: string, value: string ([int64](https://developers.google.com/discovery/v1/type-format) format))` Per service utilization breakdown. The Key is the Google Cloud managed service name.  
`resourceStatus.reservationMaintenance` |  `object` Maintenance information for this reservation  
`resourceStatus.reservationMaintenance.upcomingGroupMaintenance` |  `object` Maintenance information on this group of VMs.  
`resourceStatus.reservationMaintenance.upcomingGroupMaintenance.type` |  `enum` Defines the type of maintenance.  
`resourceStatus.reservationMaintenance.upcomingGroupMaintenance.canReschedule` |  `boolean` Indicates if the maintenance can be customer triggered.  
`resourceStatus.reservationMaintenance.upcomingGroupMaintenance.windowStartTime` |  `string` The current start time of the maintenance window. This timestamp value is in RFC3339 text format.  
`resourceStatus.reservationMaintenance.upcomingGroupMaintenance.windowEndTime` |  `string` The time by which the maintenance disruption will be completed. This timestamp value is in RFC3339 text format.  
`resourceStatus.reservationMaintenance.upcomingGroupMaintenance.latestWindowStartTime` |  `string` The latest time for the planned maintenance window to start. This timestamp value is in RFC3339 text format.  
`resourceStatus.reservationMaintenance.upcomingGroupMaintenance.maintenanceStatus` |  `enum`  
`resourceStatus.reservationMaintenance.upcomingGroupMaintenance.maintenanceOnShutdown` |  `boolean` Indicates whether the UpcomingMaintenance will be triggered on VM shutdown.  
`resourceStatus.reservationMaintenance.upcomingGroupMaintenance.maintenanceReasons[]` |  `enum` The reasons for the maintenance. Only valid for vms.  
`resourceStatus.reservationMaintenance.maintenanceOngoingCount` |  `integer` Progress for ongoing maintenance for this group of VMs/hosts. Describes number of hosts in the block that have ongoing maintenance.  
`resourceStatus.reservationMaintenance.maintenancePendingCount` |  `integer` Progress for ongoing maintenance for this group of VMs/hosts. Describes number of hosts in the block that have pending maintenance.  
`resourceStatus.reservationMaintenance.schedulingType` |  `enum` The type of maintenance for the reservation.  
`resourceStatus.reservationMaintenance.subblockInfraMaintenanceOngoingCount` |  `integer` Describes number of subblock Infrastructure that has ongoing maintenance. Here, Subblock Infrastructure Maintenance pertains to upstream hardware contained in the Subblock that is necessary for a VM Family(e.g. NVLink Domains). Not all VM Families will support this field.  
`resourceStatus.reservationMaintenance.subblockInfraMaintenancePendingCount` |  `integer` Describes number of subblock Infrastructure that has pending maintenance. Here, Subblock Infrastructure Maintenance pertains to upstream hardware contained in the Subblock that is necessary for a VM Family (e.g. NVLink Domains). Not all VM Families will support this field.  
`resourceStatus.reservationMaintenance.instanceMaintenanceOngoingCount` |  `integer` Describes number of instances that have ongoing maintenance.  
`resourceStatus.reservationMaintenance.instanceMaintenancePendingCount` |  `integer` Describes number of instances that have pending maintenance.  
`resourceStatus.reservationBlockCount` |  `integer` The number of reservation blocks associated with this reservation.  
`resourceStatus.healthInfo` |  `object` Output only. Health information for the reservation.  
`resourceStatus.healthInfo.healthStatus` |  `enum` The health status of the reservation.  
`resourceStatus.healthInfo.healthyBlockCount` |  `integer` The number of reservation blocks that are healthy.  
`resourceStatus.healthInfo.degradedBlockCount` |  `integer` The number of reservation blocks that are degraded.  
`reservationSharingPolicy` |  `object` Specify the reservation sharing policy. If unspecified, the reservation will not be shared with Google Cloud managed services.  
`reservationSharingPolicy.serviceShareType` |  `enum` Sharing config for all Google Cloud services.  
`deploymentType` |  `enum` Specifies the deployment strategy for this reservation.  
`advancedDeploymentControl` |  `object` Advanced control for cluster management, applicable only to DENSE deployment type reservations.  
`advancedDeploymentControl.reservationOperationalMode` |  `enum` Indicates chosen reservation operational mode for the reservation.  
`enableEmergentMaintenance` |  `boolean` Indicates whether Compute Engine allows unplanned maintenance for your VMs; for example, to fix hardware errors.  
`reservationMode` |  `enum` Output only. Indicates the reservation mode of the reservation.  
`protectionTier` |  `enum` Protection tier for the workload which specifies the workload expectations in the event of infrastructure failures at data center (e.g. power and/or cooling failures).  
`schedulingType` |  `enum` The type of maintenance for the reservation.  
`params` |  `object` Input only. Additional params passed with the request, but not persisted as part of resource payload.  
`params.resourceManagerTags` |  `map (key: string, value: string)` Input only. Resource manager tags to be bound to the reservation. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). Keys and values can be either in numeric format, such as `tagKeys/{tag_key_id}` and `tagValues/{tag_value_id}` or in namespaced format such as `{org_id|projectId}/{tag_key_short_name}` and `{tag_value_short_name}`. The field is ignored (both PUT & PATCH) when empty.  
`confidentialComputeType` |  `enum`  
`earlyAccessMaintenance` |  `enum` Indicates the early access maintenance for the reservation. If this field is absent or set to NO_EARLY_ACCESS, the reservation is not enrolled in early access maintenance and the standard notice applies.  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`specificReservation` |  `object` Reservation for instances with specific machine shapes.  
`specificReservation.instanceProperties` |  `object` The instance properties for the reservation.  
`specificReservation.instanceProperties.machineType` |  `string` Specifies type of machine (name only) which has fixed number of vCPUs and fixed amount of memory. This also includes specifying custom machine type following custom-NUMBER_OF_CPUS-AMOUNT_OF_MEMORY pattern.  
`specificReservation.instanceProperties.guestAccelerators[]` |  `object` Specifies accelerator type and count.  
`specificReservation.instanceProperties.guestAccelerators[].acceleratorType` |  `string` Full or partial URL of the accelerator type resource to attach to this instance. For example: `projects/my-project/zones/us-central1-c/acceleratorTypes/nvidia-tesla-p100` If you are creating an instance template, specify only the accelerator name. See [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#introduction) for a full list of accelerator types.  
`specificReservation.instanceProperties.guestAccelerators[].acceleratorCount` |  `integer` The number of the guest accelerator cards exposed to this instance.  
`specificReservation.instanceProperties.minCpuPlatform` |  `string` Minimum cpu platform the reservation.  
`specificReservation.instanceProperties.localSsds[]` |  `object` Specifies amount of local ssd to reserve with each instance. The type of disk is local-ssd.  
`specificReservation.instanceProperties.localSsds[].diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Specifies the size of the disk in base-2 GB.  
`specificReservation.instanceProperties.localSsds[].interface` |  `enum` Specifies the disk interface to use for attaching this disk, which is either `SCSI` or `NVME`. The default is `SCSI`. For performance characteristics of SCSI over NVMe, see [Local SSD performance](https://docs.cloud.google.com/compute/docs/disks#localssds).  
`specificReservation.instanceProperties.maintenanceFreezeDurationHours` |  `integer` Specifies the number of hours after reservation creation where instances using the reservation won't be scheduled for maintenance.  
`specificReservation.instanceProperties.locationHint` |  `string` An opaque location hint used to place the allocation close to other resources. This field is for use by internal tools that use the public API.  
`specificReservation.instanceProperties.maintenanceInterval` |  `enum` Specifies the frequency of planned maintenance events. The accepted values are: `PERIODIC`.  
`specificReservation.count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Specifies the number of resources that are allocated.  
`specificReservation.inUseCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Indicates how many instances are in use.  
`specificReservation.assuredCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Indicates how many instances are actually usable currently.  
`specificReservation.sourceInstanceTemplate` |  `string` Specifies the instance template to create the reservation. If you use this field, you must exclude the `instanceProperties` field.This field is optional, and it can be a full or partial URL. For example, the following are all valid URLs to an instance template: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/global/instanceTemplates/instanceTemplate`
  * `projects/project/global/instanceTemplates/instanceTemplate`
  * `global/instanceTemplates/instanceTemplate`

  
`aggregateReservation` |  `object` Reservation for aggregated resources, providing shape flexibility.  
`aggregateReservation.vmFamily` |  `enum` The VM family that all instances scheduled against this reservation must belong to.  
`aggregateReservation.reservedResources[]` |  `object` reservations.list of reserved resources (CPUs, memory, accelerators).  
`aggregateReservation.reservedResources[].accelerator` |  `object` Properties of accelerator resources in this reservation.  
`aggregateReservation.reservedResources[].accelerator.acceleratorCount` |  `integer` Number of accelerators of specified type.  
`aggregateReservation.reservedResources[].accelerator.acceleratorType` |  `string` Full or partial URL to accelerator type. e.g. "projects/{PROJECT}/zones/{ZONE}/acceleratorTypes/ct4l"  
`aggregateReservation.inUseResources[]` |  `object` Output only. reservations.list of resources currently in use.  
`aggregateReservation.inUseResources[].accelerator` |  `object` Properties of accelerator resources in this reservation.  
`aggregateReservation.inUseResources[].accelerator.acceleratorCount` |  `integer` Number of accelerators of specified type.  
`aggregateReservation.inUseResources[].accelerator.acceleratorType` |  `string` Full or partial URL to accelerator type. e.g. "projects/{PROJECT}/zones/{ZONE}/acceleratorTypes/ct4l"  
`aggregateReservation.workloadType` |  `enum` The workload type of the instances that will target this reservation.  
`aggregateReservation.hostCount` |  `integer` Count of reserved hosts of specified VM family. The host has fixed number of accelerators based on the accelerator/vm-family selected.  
`aggregateReservation.inUseHostCount` |  `integer` Output only. Number of hosts currently in use. If there is one or more Instances running on the host, it is considered in use.  
`aggregateReservation.inUseInstanceCount` |  `integer` Output only. Number of instances currently in use in this reservation.  
End of mutually exclusive fields.  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`deleteAtTime` |  `string` Absolute time in future when the reservation will be auto-deleted by Compute Engine. Timestamp is represented in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`deleteAfterDuration` |  `object` Duration time relative to reservation creation when Compute Engine will automatically delete this resource.  
`deleteAfterDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`deleteAfterDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
End of mutually exclusive fields.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.reservations.get`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
