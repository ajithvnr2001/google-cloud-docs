---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/regionCommitments/get/
title: Method: regionCommitments.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:07.861894+00:00
---

# Method: regionCommitments.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/regionCommitments/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: regionCommitments.get Stay organized with collections  Save and categorize content based on your preferences. 

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
      * JSON representation
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



API Version : 2026-10-01-preview

Returns the specified commitment resource.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/commitments/{commitment}?$apiVersion=2026-10-01-preview`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region for this request.  
`commitment` |  `string` Name of the commitment to return.  
  
### Request body

The request body must be empty.

### Response body

Represents a regional resource-based commitment resource.

Creating this commitment resource means that you are purchasing a resource-based committed use contract, with an explicit start and end time. You can purchase resource-based commitments for both hardware and software resources. For more information, read [ Resource-based committed use discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts)

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "region": string,
      "selfLink": string,
      "status": enum,
      "statusMessage": string,
      "plan": enum,
      "startTimestamp": string,
      "endTimestamp": string,
      "category": enum,
      "resources": [
        {
          "type": enum,
          "amount": string,
          "acceleratorType": string
        }
      ],
      "type": enum,
      "reservations": [
        {
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
              "locationHint": string
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
                "accelerator": {
                  "acceleratorCount": integer,
                  "acceleratorType": string
                }
              }
            ],
            "inUseResources": [
              {
                "accelerator": {
                  "acceleratorCount": integer,
                  "acceleratorType": string
                }
              }
            ],
            "workloadType": enum
          },
          "deleteAtTime": string,
          "deleteAfterDuration": {
            "seconds": string,
            "nanos": integer
          },
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
            "projectMap": {
              string: {
                "projectId": string
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
          "resourceMetadata": {
            "resourceType": string,
            "apiVersion": string
          }
        }
      ],
      "licenseResource": {
        "license": string,
        "amount": string,
        "coresPerLicense": string
      },
      "autoRenew": boolean,
      "mergeSourceCommitments": [
        string
      ],
      "splitSourceCommitment": string,
      "resourceStatus": {
        "customTermEligibilityEndTimestamp": string
      },
      "existingReservations": [
        string
      ],
      "customEndTimestamp": string,
      "params": {
        "resourceManagerTags": {
          string: string,
          ...
        }
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#commitment` for commitments.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the commitment. You must specify a name when you purchase the commitment. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of the commitment. You can provide this property when you create the resource.  
`region` |  `string` Output only. URL of the region where the commitment and committed resources are located.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`status` |  `enum` Output only. Status of the commitment with regards to eventual expiration (each commitment has an end date defined). Status can be one of the following values: `NOT_YET_ACTIVE`, `ACTIVE`, or `EXPIRED`.``  
`statusMessage` |  `string` Output only. An optional, human-readable explanation of the status.  
`plan` |  `enum` The minimum time duration that you commit to purchasing resources. The plan that you choose determines the preset term length of the commitment (which is 1 year or 3 years) and affects the discount rate that you receive for your resources. Committing to a longer time duration typically gives you a higher discount rate. The supported values for this field are `TWELVE_MONTH` (1 year), and `THIRTY_SIX_MONTH` (3 years).  
`startTimestamp` |  `string` Output only. Commitment start time in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`endTimestamp` |  `string` Output only. Commitment end time in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`category` |  `enum` The category of the commitment; specifies whether the commitment is for hardware or software resources. Category `MACHINE` specifies that you are committing to hardware machine resources such as `VCPU` or `MEMORY`, listed in `resources`. Category `LICENSE` specifies that you are committing to software licenses, listed in `licenseResources`. Note that if you specify `MACHINE` commitments, then you must also specify a `type` to indicate the machine series of the hardware resource that you are committing to. Available from version 2026-09-01.  
`resources[]` |  `object` The list of all the hardware resources, with their types and amounts, that you want to commit to. Specify as a separate entry in the list for each individual resource type.  
`resources[].type` |  `enum` The type of hardware resource that you want to specify. You can specify any of the following values: 

  * `VCPU`
  * `MEMORY`
  * `LOCAL_SSD`
  * `ACCELERATOR`

Specify as a separate entry in the list for each individual resource type.  
`resources[].amount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The quantity of the hardware resource that you want to commit to purchasing (in a type-dependent unit). 

  * For vCPUs, you must specify an integer value.
  * For memory, you specify the amount of MB that you want. The value you specify must be a multiple of 256 MB, with up to 6.5 GB of memory per every vCPU.
  * For GPUs, you must specify an integer value.
  * For Local SSD disks, you must specify the amount in GB. The size of a single Local SSD disk is 375 GB.

  
`resources[].acceleratorType` |  `string` Name of the accelerator type or GPU resource. Specify this field only when the type of hardware resource is ACCELERATOR.  
`type` |  `enum` The type of commitment; specifies the [ machine series](https://cloud.google.com/compute/docs/machine-resource#vm_terminology) for which you want to commit to purchasing resources. The choice of machine series affects the discount rate and the eligible resource types.The type must be one of the following: `ACCELERATOR_OPTIMIZED`, `ACCELERATOR_OPTIMIZED_A3`, `ACCELERATOR_OPTIMIZED_A3_MEGA`, `COMPUTE_OPTIMIZED`, `COMPUTE_OPTIMIZED_C2D`, `COMPUTE_OPTIMIZED_C3`, `COMPUTE_OPTIMIZED_C3D`, `COMPUTE_OPTIMIZED_H3`, `GENERAL_PURPOSE`, `GENERAL_PURPOSE_C4`, `GENERAL_PURPOSE_E2`, `GENERAL_PURPOSE_N2`, `GENERAL_PURPOSE_N2D`, `GENERAL_PURPOSE_N4`, `GENERAL_PURPOSE_T2D`, `GRAPHICS_OPTIMIZED`, `GRAPHICS_OPTIMIZED_G4`, `GRAPHICS_OPTIMIZED_G4_VGPU`, `MEMORY_OPTIMIZED`, `MEMORY_OPTIMIZED_M3`, `MEMORY_OPTIMIZED_X4`, `STORAGE_OPTIMIZED_Z3`, `STORAGE_OPTIMIZED_Z4DS`, `STORAGE_OPTIMIZED_Z4DH`, `STORAGE_OPTIMIZED_Z4D4T`. For example, type `MEMORY_OPTIMIZED` specifies a commitment that applies only to eligible resources of memory optimized M1 and M2 machine series. Type `GENERAL_PURPOSE` specifies a commitment that applies only to eligible resources of general purpose N1 machine series. Available from version 2026-09-01.  
`reservations[]` |  `object` The list of new reservations that you want to create and attach to this commitment.You must attach reservations to your commitment if your commitment specifies any GPUs or Local SSD disks. For more information, see [ Attach reservations to resource-based commitments](https://cloud.google.com/compute/docs/instances/reservations-with-commitments#attach-reservations-to-resource-cuds).Specify this property only if you want to create new reservations to attach. To attach existing reservations, specify the `existingReservations` property instead.  
`reservations[].specificReservation` |  `object` Reservation for instances with specific machine shapes.  
`reservations[].specificReservation.instanceProperties` |  `object` The instance properties for the reservation.  
`reservations[].specificReservation.instanceProperties.machineType` |  `string` Specifies type of machine (name only) which has fixed number of vCPUs and fixed amount of memory. This also includes specifying custom machine type following custom-NUMBER_OF_CPUS-AMOUNT_OF_MEMORY pattern.  
`reservations[].specificReservation.instanceProperties.guestAccelerators[]` |  `object` Specifies accelerator type and count.  
`reservations[].specificReservation.instanceProperties.guestAccelerators[].acceleratorType` |  `string` Full or partial URL of the accelerator type resource to attach to this instance. For example: `projects/my-project/zones/us-central1-c/acceleratorTypes/nvidia-tesla-p100` If you are creating an instance template, specify only the accelerator name. See [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#introduction) for a full list of accelerator types.  
`reservations[].specificReservation.instanceProperties.guestAccelerators[].acceleratorCount` |  `integer` The number of the guest accelerator cards exposed to this instance.  
`reservations[].specificReservation.instanceProperties.minCpuPlatform` |  `string` Minimum cpu platform the reservation.  
`reservations[].specificReservation.instanceProperties.localSsds[]` |  `object` Specifies amount of local ssd to reserve with each instance. The type of disk is local-ssd.  
`reservations[].specificReservation.instanceProperties.localSsds[].diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Specifies the size of the disk in base-2 GB.  
`reservations[].specificReservation.instanceProperties.localSsds[].interface` |  `enum` Specifies the disk interface to use for attaching this disk, which is either `SCSI` or `NVME`. The default is `SCSI`. For performance characteristics of SCSI over NVMe, see [Local SSD performance](https://docs.cloud.google.com/compute/docs/disks#localssds).  
`reservations[].specificReservation.instanceProperties.locationHint` |  `string` An opaque location hint used to place the allocation close to other resources. This field is for use by internal tools that use the public API.  
`reservations[].specificReservation.count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Specifies the number of resources that are allocated.  
`reservations[].specificReservation.inUseCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Indicates how many instances are in use.  
`reservations[].specificReservation.assuredCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Indicates how many instances are actually usable currently.  
`reservations[].specificReservation.sourceInstanceTemplate` |  `string` Specifies the instance template to create the reservation. If you use this field, you must exclude the `instanceProperties` field.This field is optional, and it can be a full or partial URL. For example, the following are all valid URLs to an instance template: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/global/instanceTemplates/instanceTemplate`
  * `projects/project/global/instanceTemplates/instanceTemplate`
  * `global/instanceTemplates/instanceTemplate`

  
`reservations[].aggregateReservation` |  `object` Reservation for aggregated resources, providing shape flexibility.  
`reservations[].aggregateReservation.vmFamily` |  `enum` The VM family that all instances scheduled against this reservation must belong to.  
`reservations[].aggregateReservation.reservedResources[]` |  `object` regionCommitments.list of reserved resources (CPUs, memory, accelerators).  
`reservations[].aggregateReservation.reservedResources[].accelerator` |  `object` Properties of accelerator resources in this reservation.  
`reservations[].aggregateReservation.reservedResources[].accelerator.acceleratorCount` |  `integer` Number of accelerators of specified type.  
`reservations[].aggregateReservation.reservedResources[].accelerator.acceleratorType` |  `string` Full or partial URL to accelerator type. e.g. "projects/{PROJECT}/zones/{ZONE}/acceleratorTypes/ct4l"  
`reservations[].aggregateReservation.inUseResources[]` |  `object` Output only. regionCommitments.list of resources currently in use.  
`reservations[].aggregateReservation.inUseResources[].accelerator` |  `object` Properties of accelerator resources in this reservation.  
`reservations[].aggregateReservation.inUseResources[].accelerator.acceleratorCount` |  `integer` Number of accelerators of specified type.  
`reservations[].aggregateReservation.inUseResources[].accelerator.acceleratorType` |  `string` Full or partial URL to accelerator type. e.g. "projects/{PROJECT}/zones/{ZONE}/acceleratorTypes/ct4l"  
`reservations[].aggregateReservation.workloadType` |  `enum` The workload type of the instances that will target this reservation.  
`reservations[].deleteAtTime` |  `string` Absolute time in future when the reservation will be auto-deleted by Compute Engine. Timestamp is represented in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`reservations[].deleteAfterDuration` |  `object` Duration time relative to reservation creation when Compute Engine will automatically delete this resource.  
`reservations[].deleteAfterDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`reservations[].deleteAfterDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`reservations[].kind` |  `string` Output only. Type of the resource. Always `compute#reservations` for reservations.  
`reservations[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`reservations[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`reservations[].selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`reservations[].zone` |  `string` Zone in which the reservation resides. A zone must be provided if the reservation is created within a commitment.  
`reservations[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`reservations[].name` |  `string` The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`reservations[].commitment` |  `string` Output only. Full or partial URL to a parent commitment. This field displays for reservations that are tied to a commitment.  
`reservations[].linkedCommitments[]` |  `string` Output only. Full or partial URL to parent commitments. This field displays for reservations that are tied to multiple commitments.  
`reservations[].specificReservationRequired` |  `boolean` Indicates whether the reservation can be consumed by VMs with affinity for "any" reservation. If the field is set, then only VMs that target the reservation by name can consume from this reservation.  
`reservations[].status` |  `enum` Output only. The status of the reservation. 

  * `CREATING`: Reservation resources are being allocated.
  * `READY`: Reservation resources have been allocated, and the reservation is ready for use.
  * `DELETING`: Reservation deletion is in progress.
  * `UPDATING`: Reservation update is in progress.

  
`reservations[].shareSettings` |  `object` Specify share-settings to create a shared reservation. This property is optional. For more information about the syntax and options for this field and its subfields, see the guide for [creating a shared reservation.](https://cloud.google.com/compute/docs/instances/reservations-shared#creating_a_shared_reservation)  
`reservations[].shareSettings.shareType` |  `enum` Type of sharing for this shared-reservation  
`reservations[].shareSettings.projectMap[]` |  `map (key: string, value: object)` A map of project id and project config. This is only valid when shareType's value is SPECIFIC_PROJECTS.  
`reservations[].shareSettings.projectMap[].projectId` |  `string` The project ID, should be same as the key of this project config in the parent map.  
`reservations[].satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`reservations[].resourcePolicies` |  `map (key: string, value: string)` Resource policies to be added to this reservation. The key is defined by user, and the value is resource policy url. This is to define placement policy with reservation.  
`reservations[].resourceStatus` |  `object` Output only. Status information for Reservation resource.  
`reservations[].resourceStatus.specificSkuAllocation` |  `object` Allocation Properties of this reservation.  
`reservations[].resourceStatus.specificSkuAllocation.sourceInstanceTemplateId` |  `string` ID of the instance template used to populate reservation properties.  
`reservations[].resourceStatus.specificSkuAllocation.utilizations` |  `map (key: string, value: string ([int64](https://developers.google.com/discovery/v1/type-format) format))` Per service utilization breakdown. The Key is the Google Cloud managed service name.  
`reservations[].resourceStatus.reservationMaintenance` |  `object` Maintenance information for this reservation  
`reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance` |  `object` Maintenance information on this group of VMs.  
`reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.type` |  `enum` Defines the type of maintenance.  
`reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.canReschedule` |  `boolean` Indicates if the maintenance can be customer triggered.  
`reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.windowStartTime` |  `string` The current start time of the maintenance window. This timestamp value is in RFC3339 text format.  
`reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.windowEndTime` |  `string` The time by which the maintenance disruption will be completed. This timestamp value is in RFC3339 text format.  
`reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.latestWindowStartTime` |  `string` The latest time for the planned maintenance window to start. This timestamp value is in RFC3339 text format.  
`reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.maintenanceStatus` |  `enum`  
`reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.maintenanceOnShutdown` |  `boolean` Indicates whether the UpcomingMaintenance will be triggered on VM shutdown.  
`reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.maintenanceReasons[]` |  `enum` The reasons for the maintenance. Only valid for vms.  
`reservations[].resourceStatus.reservationMaintenance.maintenanceOngoingCount` |  `integer` Progress for ongoing maintenance for this group of VMs/hosts. Describes number of hosts in the block that have ongoing maintenance.  
`reservations[].resourceStatus.reservationMaintenance.maintenancePendingCount` |  `integer` Progress for ongoing maintenance for this group of VMs/hosts. Describes number of hosts in the block that have pending maintenance.  
`reservations[].resourceStatus.reservationMaintenance.schedulingType` |  `enum` The type of maintenance for the reservation.  
`reservations[].resourceStatus.reservationMaintenance.subblockInfraMaintenanceOngoingCount` |  `integer` Describes number of subblock Infrastructure that has ongoing maintenance. Here, Subblock Infrastructure Maintenance pertains to upstream hardware contained in the Subblock that is necessary for a VM Family(e.g. NVLink Domains). Not all VM Families will support this field.  
`reservations[].resourceStatus.reservationMaintenance.subblockInfraMaintenancePendingCount` |  `integer` Describes number of subblock Infrastructure that has pending maintenance. Here, Subblock Infrastructure Maintenance pertains to upstream hardware contained in the Subblock that is necessary for a VM Family (e.g. NVLink Domains). Not all VM Families will support this field.  
`reservations[].resourceStatus.reservationMaintenance.instanceMaintenanceOngoingCount` |  `integer` Describes number of instances that have ongoing maintenance.  
`reservations[].resourceStatus.reservationMaintenance.instanceMaintenancePendingCount` |  `integer` Describes number of instances that have pending maintenance.  
`reservations[].resourceStatus.reservationBlockCount` |  `integer` The number of reservation blocks associated with this reservation.  
`reservations[].resourceStatus.healthInfo` |  `object` Output only. Health information for the reservation.  
`reservations[].resourceStatus.healthInfo.healthStatus` |  `enum` The health status of the reservation.  
`reservations[].resourceStatus.healthInfo.healthyBlockCount` |  `integer` The number of reservation blocks that are healthy.  
`reservations[].resourceStatus.healthInfo.degradedBlockCount` |  `integer` The number of reservation blocks that are degraded.  
`reservations[].reservationSharingPolicy` |  `object` Specify the reservation sharing policy. If unspecified, the reservation will not be shared with Google Cloud managed services.  
`reservations[].reservationSharingPolicy.serviceShareType` |  `enum` Sharing config for all Google Cloud services.  
`reservations[].deploymentType` |  `enum` Specifies the deployment strategy for this reservation.  
`reservations[].advancedDeploymentControl` |  `object` Advanced control for cluster management, applicable only to DENSE deployment type reservations.  
`reservations[].advancedDeploymentControl.reservationOperationalMode` |  `enum` Indicates chosen reservation operational mode for the reservation.  
`reservations[].enableEmergentMaintenance` |  `boolean` Indicates whether Compute Engine allows unplanned maintenance for your VMs; for example, to fix hardware errors.  
`reservations[].protectionTier` |  `enum` Protection tier for the workload which specifies the workload expectations in the event of infrastructure failures at data center (e.g. power and/or cooling failures).  
`reservations[].schedulingType` |  `enum` The type of maintenance for the reservation.  
`reservations[].params` |  `object` Input only. Additional params passed with the request, but not persisted as part of resource payload.  
`reservations[].params.resourceManagerTags` |  `map (key: string, value: string)` Input only. Resource manager tags to be bound to the reservation. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). Keys and values can be either in numeric format, such as `tagKeys/{tag_key_id}` and `tagValues/{tag_value_id}` or in namespaced format such as `{org_id|projectId}/{tag_key_short_name}` and `{tag_value_short_name}`. The field is ignored (both PUT & PATCH) when empty.  
`reservations[].confidentialComputeType` |  `enum`  
`reservations[].earlyAccessMaintenance` |  `enum` Indicates the early access maintenance for the reservation. If this field is absent or set to NO_EARLY_ACCESS, the reservation is not enrolled in early access maintenance and the standard notice applies.  
`reservations[].resourceMetadata` |  `object` Output only. Contains standard resource metadata for an Allocation resource. It is populated for each instance of the Allocation resource, and includes the `apiVersion` the instance was retrieved through, and its canonical `resourceType` name.  
`reservations[].resourceMetadata.resourceType` |  `string` The canonical resource type name in the format of a resource type as defined by [AIP-123](https://google.aip.dev/123). For example, `"compute.googleapis.com/Instance"`.  
`reservations[].resourceMetadata.apiVersion` |  `string` The version of the API interface that this resource was retrieved through. For example, `"2025-01-01"` or `"2025-01-01-preview"`.  
`licenseResource` |  `object` The license specification required as part of a license commitment. Available from version 2026-09-01.  
`licenseResource.license` |  `string` The applicable license URI.  
`licenseResource.amount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of licenses you plan to purchase.  
`licenseResource.coresPerLicense` |  `string` The number of cores per license.  
`autoRenew` |  `boolean` Specifies whether to automatically renew the commitment at the end of its current term. The default value is `false`. If you set the field to `true`, each time your commitment reaches the end of its term, Compute Engine automatically renews it for another term. You can update this field anytime before the commitment expires. For example, if the commitment is set to expire at 12 AM UTC-8 on January 3, 2027, you can update this field until 11:59 PM UTC-8 on January 2, 2027.  
`mergeSourceCommitments[]` |  `string` The list of source commitments that you are merging to create the new merged commitment. For more information, see [ Merging commitments](https://cloud.google.com/compute/docs/instances/merge-and-split-commitments#merging).  
`splitSourceCommitment` |  `string` The source commitment from which you are transferring resources to create the new split commitment. For more information, see [ Split commitments](https://cloud.google.com/compute/docs/instances/merge-and-split-commitments#splitting).  
`resourceStatus` |  `object` Output only. Status information for Commitment resource.  
`resourceStatus.customTermEligibilityEndTimestamp` |  `string` Output only. Indicates the end time of customer's eligibility to send custom term requests in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. Term extension requests that (not the end time in the request) after this time will be rejected.  
`existingReservations[]` |  `string` Available from version 2026-09-01.  
`customEndTimestamp` |  `string` [Input Only] Optional, specifies the requested commitment end time in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. Use this option when the desired commitment's end date is later than the start date + term duration.  
`params` |  `object` Input only. Additional params passed with the request, but not persisted as part of resource payload.  
`params.resourceManagerTags` |  `map (key: string, value: string)` Input only. Resource manager tags to be bound to the commitment. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). Keys and values can be either in numeric format, such as `tagKeys/{tag_key_id}` and `tagValues/{tag_value_id}` or in namespaced format such as `{org_id|projectId}/{tag_key_short_name}` and `{tag_value_short_name}`. The field is ignored (both PUT & PATCH) when empty.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.commitments.get`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
