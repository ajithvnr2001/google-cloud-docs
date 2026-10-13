---
url: https://docs.cloud.google.com/compute/docs/reference/rest/beta/futureReservations/get/
title: Method: futureReservations.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:25.792963+00:00
---

# Method: futureReservations.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/beta/futureReservations/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: futureReservations.get Stay organized with collections  Save and categorize content based on your preferences. 

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
      * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Retrieves information about the specified future reservation.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/beta/projects/{project}/zones/{zone}/futureReservations/{futureReservation}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`zone` |  `string` Name of the zone for this request. Name should conform to RFC1035.  
`futureReservation` |  `string` Name of the future reservation to retrieve. Name should conform to RFC1035.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "selfLink": string,
      "selfLinkWithId": string,
      "zone": string,
      "description": string,
      "name": string,
      "timeWindow": {
        "endTime": string,
        "duration": {
          "seconds": string,
          "nanos": integer
        },
        "startTime": string
      },
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
      "namePrefix": string,
      "status": {
        "storagePoolProvisionedCapacity": {
          "poolProvisionedCapacityGb": string,
          "poolProvisionedIops": string,
          "poolProvisionedThroughput": string
        },
        "exapoolProvisionedCapacityGb": {
          "writeOptimized": string,
          "readOptimized": string,
          "capacityOptimized": string
        },
        "procurementStatus": enum,
        "lockTime": string,
        "autoCreatedReservations": [
          string
        ],
        "fulfilledCount": string,
        "specificSkuProperties": {
          "sourceInstanceTemplateId": string
        },
        "amendmentStatus": enum,
        "lastKnownGoodState": {
          "futureReservationSpecs": {
            "specificSkuProperties": {
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
              "totalCount": string,
              "sourceInstanceTemplate": string
            },
            "timeWindow": {
              "startTime": string,
    
              // The following is a list of mutually exclusive fields. At most one of the
              // fields will be set in a response:
              "endTime": string,
              "duration": {
                "seconds": string,
                "nanos": integer
              }
              // End of mutually exclusive fields.
            },
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
            }
          },
          "procurementStatus": enum,
          "namePrefix": string,
          "description": string,
          "lockTime": string,
          "existingMatchingUsageInfo": {
            "count": string,
            "timestamp": string
          }
        },
        "existingMatchingUsageInfo": {
          "count": string,
          "timestamp": string
        }
      },
      "planningStatus": enum,
      "autoDeleteAutoCreatedReservations": boolean,
      "specificReservationRequired": boolean,
      "reservationName": string,
      "deploymentType": enum,
      "commitmentInfo": {
        "commitmentPlan": enum,
        "commitmentName": string,
        "previousCommitmentTerms": enum
      },
      "schedulingType": enum,
      "reservationMode": enum,
      "advancedDeploymentControl": {
        "reservationOperationalMode": enum
      },
      "enableEmergentMaintenance": boolean,
      "protectionTier": enum,
      "params": {
        "resourceManagerTags": {
          string: string,
          ...
        }
      },
      "confidentialComputeType": enum,
      "resourceName": string,
      "colocationResource": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "specificSkuProperties": {
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
        "totalCount": string,
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
      },
      "storagePoolProperties": {
        "requestedStoragePoolProvisionedCapacity": {
          "poolProvisionedCapacityGb": string,
          "poolProvisionedIops": string,
          "poolProvisionedThroughput": string
        },
        "requestedExapoolProvisionedCapacityGb": {
          "writeOptimized": string,
          "readOptimized": string,
          "capacityOptimized": string
        },
        "storagePoolType": string
      }
      // End of mutually exclusive fields.
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "autoCreatedReservationsDeleteTime": string,
      "autoCreatedReservationsDuration": {
        "seconds": string,
        "nanos": integer
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#futureReservation` for future reservations.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. A unique identifier for this future reservation. The server defines this identifier.  
`creationTimestamp` |  `string` Output only. The creation timestamp for this future reservation in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`selfLinkWithId` |  `string` Output only. Server-defined URL for this resource with the resource id.  
`zone` |  `string` Output only. URL of the Zone where this future reservation resides.  
`description` |  `string` An optional description of this resource. Provide this property when you create the future reservation.  
`name` |  `string` The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`timeWindow` |  `object` Time window for this Future Reservation.  
`timeWindow.endTime` |  `string`  
`timeWindow.duration` |  `object`  
`timeWindow.duration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`timeWindow.duration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`timeWindow.startTime` |  `string` Start time of the Future Reservation. The startTime is an RFC3339 string.  
`shareSettings` |  `object` futureReservations.list of Projects/Folders to share with.  
`shareSettings.shareType` |  `enum` Type of sharing for this shared-reservation  
`shareSettings.projects[]` |  `string` A futureReservations.list of Project names to specify consumer projects for this shared-reservation. This is only valid when shareType's value is SPECIFIC_PROJECTS.  
`shareSettings.projectMap[]` |  `map (key: string, value: object)` A map of project id and project config. This is only valid when shareType's value is SPECIFIC_PROJECTS.  
`shareSettings.projectMap[].projectId` |  `string` The project ID, should be same as the key of this project config in the parent map.  
`shareSettings.folderMap[]` |  `map (key: string, value: object)` A map of folder id and folder config to specify consumer projects for this shared-reservation. This is only valid when shareType's value is DIRECT_PROJECTS_UNDER_SPECIFIC_FOLDERS. Folder id should be a string of number, and without "folders/" prefix.  
`shareSettings.folderMap[].folderId` |  `string` The folder ID, should be same as the key of this folder config in the parent map. Folder id should be a string of number, and without "folders/" prefix.  
`namePrefix` |  `string` Name prefix for the reservations to be created at the time of delivery. The name prefix must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Maximum allowed length for name prefix is 20. Automatically created reservations name format will be -date-####.  
`status` |  `object` Output only. Status of the Future Reservation  
`status.storagePoolProvisionedCapacity` |  `object` Output only. Storage pool provisioned capacities for each SKU type.  
`status.storagePoolProvisionedCapacity.poolProvisionedCapacityGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size of the storage pool in GiB.  
`status.storagePoolProvisionedCapacity.poolProvisionedIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Provisioned IOPS of the storage pool. Only relevant if the storage pool type is hyperdisk-balanced.  
`status.storagePoolProvisionedCapacity.poolProvisionedThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Provisioned throughput of the storage pool in MiB/s. Only relevant if the storage pool type is hyperdisk-balanced or hyperdisk-throughput.  
`status.exapoolProvisionedCapacityGb` |  `object` Output only. Exapool provisioned capacities for each SKU type.  
`status.exapoolProvisionedCapacityGb.writeOptimized` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size, in GiB, of provisioned write-optimized capacity for this Exapool  
`status.exapoolProvisionedCapacityGb.readOptimized` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size, in GiB, of provisioned read-optimized capacity for this Exapool  
`status.exapoolProvisionedCapacityGb.capacityOptimized` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size, in GiB, of provisioned capacity-optimized capacity for this Exapool  
`status.procurementStatus` |  `enum` Output only. Current state of this Future Reservation  
`status.lockTime` |  `string` Output only. Time when Future Reservation would become LOCKED, after which no modifications to Future Reservation will be allowed. Applicable only after the Future Reservation is in the APPROVED state. The lockTime is an RFC3339 string. The procurementStatus will transition to PROCURING state at this time.  
`status.autoCreatedReservations[]` |  `string` Output only. Fully qualified urls of the automatically created reservations at startTime.  
`status.fulfilledCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. This count indicates the fulfilled capacity so far. This is set during "PROVISIONING" state. This count also includes capacity delivered as part of existing matching reservations.  
`status.specificSkuProperties` |  `object`  
`status.specificSkuProperties.sourceInstanceTemplateId` |  `string` ID of the instance template used to populate the Future Reservation properties.  
`status.amendmentStatus` |  `enum` Output only. The current status of the requested amendment.  
`status.lastKnownGoodState` |  `object` Output only. This field represents the future reservation before an amendment was requested. If the amendment is declined, the Future Reservation will be reverted to the last known good state. The last known good state is not set when updating a future reservation whose Procurement Status is DRAFTING.  
`status.lastKnownGoodState.futureReservationSpecs` |  `object`  
`status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties` |  `object` Output only. The previous instance related properties of the Future Reservation.  
`status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties` |  `object` Properties of the SKU instances being reserved.  
`status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.machineType` |  `string` Specifies type of machine (name only) which has fixed number of vCPUs and fixed amount of memory. This also includes specifying custom machine type following custom-NUMBER_OF_CPUS-AMOUNT_OF_MEMORY pattern.  
`status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.guestAccelerators[]` |  `object` Specifies accelerator type and count.  
`status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.guestAccelerators[].acceleratorType` |  `string` Full or partial URL of the accelerator type resource to attach to this instance. For example: `projects/my-project/zones/us-central1-c/acceleratorTypes/nvidia-tesla-p100` If you are creating an instance template, specify only the accelerator name. See [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#introduction) for a full list of accelerator types.  
`status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.guestAccelerators[].acceleratorCount` |  `integer` The number of the guest accelerator cards exposed to this instance.  
`status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.minCpuPlatform` |  `string` Minimum cpu platform the reservation.  
`status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.localSsds[]` |  `object` Specifies amount of local ssd to reserve with each instance. The type of disk is local-ssd.  
`status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.localSsds[].diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Specifies the size of the disk in base-2 GB.  
`status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.localSsds[].interface` |  `enum` Specifies the disk interface to use for attaching this disk, which is either `SCSI` or `NVME`. The default is `SCSI`. For performance characteristics of SCSI over NVMe, see [Local SSD performance](https://docs.cloud.google.com/compute/docs/disks#localssds).  
`status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.maintenanceFreezeDurationHours` |  `integer` Specifies the number of hours after reservation creation where instances using the reservation won't be scheduled for maintenance.  
`status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.locationHint` |  `string` An opaque location hint used to place the allocation close to other resources. This field is for use by internal tools that use the public API.  
`status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.maintenanceInterval` |  `enum` Specifies the frequency of planned maintenance events. The accepted values are: `PERIODIC`.  
`status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.totalCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total number of instances for which capacity assurance is requested at a future time period.  
`status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.sourceInstanceTemplate` |  `string` The instance template that will be used to populate the ReservedInstanceProperties of the future reservation  
`status.lastKnownGoodState.futureReservationSpecs.timeWindow` |  `object` Output only. The previous time window of the Future Reservation.  
`status.lastKnownGoodState.futureReservationSpecs.timeWindow.endTime` |  `string`  
`status.lastKnownGoodState.futureReservationSpecs.timeWindow.duration` |  `object`  
`status.lastKnownGoodState.futureReservationSpecs.timeWindow.duration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`status.lastKnownGoodState.futureReservationSpecs.timeWindow.duration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`status.lastKnownGoodState.futureReservationSpecs.timeWindow.startTime` |  `string` Start time of the Future Reservation. The startTime is an RFC3339 string.  
`status.lastKnownGoodState.futureReservationSpecs.shareSettings` |  `object` Output only. The previous share settings of the Future Reservation.  
`status.lastKnownGoodState.futureReservationSpecs.shareSettings.shareType` |  `enum` Type of sharing for this shared-reservation  
`status.lastKnownGoodState.futureReservationSpecs.shareSettings.projects[]` |  `string` A futureReservations.list of Project names to specify consumer projects for this shared-reservation. This is only valid when shareType's value is SPECIFIC_PROJECTS.  
`status.lastKnownGoodState.futureReservationSpecs.shareSettings.projectMap[]` |  `map (key: string, value: object)` A map of project id and project config. This is only valid when shareType's value is SPECIFIC_PROJECTS.  
`status.lastKnownGoodState.futureReservationSpecs.shareSettings.projectMap[].projectId` |  `string` The project ID, should be same as the key of this project config in the parent map.  
`status.lastKnownGoodState.futureReservationSpecs.shareSettings.folderMap[]` |  `map (key: string, value: object)` A map of folder id and folder config to specify consumer projects for this shared-reservation. This is only valid when shareType's value is DIRECT_PROJECTS_UNDER_SPECIFIC_FOLDERS. Folder id should be a string of number, and without "folders/" prefix.  
`status.lastKnownGoodState.futureReservationSpecs.shareSettings.folderMap[].folderId` |  `string` The folder ID, should be same as the key of this folder config in the parent map. Folder id should be a string of number, and without "folders/" prefix.  
`status.lastKnownGoodState.procurementStatus` |  `enum` Output only. The status of the last known good state for the Future Reservation.  
`status.lastKnownGoodState.namePrefix` |  `string` Output only. The name prefix of the Future Reservation before an amendment was requested.  
`status.lastKnownGoodState.description` |  `string` Output only. The description of the FutureReservation before an amendment was requested.  
`status.lastKnownGoodState.lockTime` |  `string` Output only. The lock time of the FutureReservation before an amendment was requested.  
`status.lastKnownGoodState.existingMatchingUsageInfo` |  `object` Output only. Represents the matching usage for the future reservation before an amendment was requested.  
`status.lastKnownGoodState.existingMatchingUsageInfo.count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Count to represent min(FR totalCount, matching_reserved_capacity+matching_unreserved_instances)  
`status.lastKnownGoodState.existingMatchingUsageInfo.timestamp` |  `string` Output only. Timestamp when the matching usage was calculated  
`status.existingMatchingUsageInfo` |  `object` Output only. Represents the existing matching usage for the future reservation.  
`status.existingMatchingUsageInfo.count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Count to represent min(FR totalCount, matching_reserved_capacity+matching_unreserved_instances)  
`status.existingMatchingUsageInfo.timestamp` |  `string` Output only. Timestamp when the matching usage was calculated  
`planningStatus` |  `enum` Planning state before being submitted for evaluation  
`autoDeleteAutoCreatedReservations` |  `boolean` Setting for enabling or disabling automatic deletion for auto-created reservation. If set to true, auto-created reservations will be deleted at Future Reservation's end time (default) or at user's defined timestamp if any of the [autoCreatedReservationsDeleteTime, autoCreatedReservationsDuration] values is specified. For keeping auto-created reservation indefinitely, this value should be set to false.  
`specificReservationRequired` |  `boolean` Indicates whether the auto-created reservation can be consumed by VMs with affinity for "any" reservation. If the field is set, then only VMs that target the reservation by name can consume from the delivered reservation.  
`reservationName` |  `string` Name of reservations where the capacity is provisioned at the time of delivery of future reservations. If the reservation with the given name does not exist already, it is created automatically at the time of Approval with INACTIVE state till specified start-time. Either provide the reservationName or a namePrefix.  
`deploymentType` |  `enum` Type of the deployment requested as part of future reservation.  
`commitmentInfo` |  `object` If not present, then FR will not deliver a new commitment or update an existing commitment.  
`commitmentInfo.commitmentPlan` |  `enum` Indicates if a Commitment needs to be created as part of FR delivery. If this field is not present, then no commitment needs to be created.  
`commitmentInfo.commitmentName` |  `string` name of the commitment where capacity is being delivered to.  
`commitmentInfo.previousCommitmentTerms` |  `enum` Only applicable if FR is delivering to the same reservation. If set, all parent commitments will be extended to match the end date of the plan for this commitment.  
`schedulingType` |  `enum` Maintenance information for this reservation  
`reservationMode` |  `enum` The reservation mode which determines reservation-termination behavior and expected pricing.  
`advancedDeploymentControl` |  `object` Advanced control for cluster management, applicable only to DENSE deployment type future reservations.  
`advancedDeploymentControl.reservationOperationalMode` |  `enum` Indicates chosen reservation operational mode for the reservation.  
`enableEmergentMaintenance` |  `boolean` Indicates if this group of VMs have emergent maintenance enabled.  
`protectionTier` |  `enum` Protection tier for the workload.  
`params` |  `object` Input only. Additional params passed with the request, but not persisted as part of resource payload.  
`params.resourceManagerTags` |  `map (key: string, value: string)` Input only. Resource manager tags to be bound to the future reservation. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). Keys and values can be either in numeric format, such as `tagKeys/{tag_key_id}` and `tagValues/{tag_value_id}` or in namespaced format such as `{org_id|projectId}/{tag_key_short_name}` and `{tag_value_short_name}`. The field is ignored (both PUT & PATCH) when empty.  
`confidentialComputeType` |  `enum`  
`resourceName` |  `string` Name of the resource intended to be delivered. Name should conform to RFC1035. This will be the name of storage pool or Exapool for persistent disk FRs.  
`colocationResource` |  `string` Full or partial URL of an existing future reservation to indicate intent for reserving capacity in the same cluster as the colocation resource.  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`specificSkuProperties` |  `object` Future Reservation configuration to indicate instance properties and total count.  
`specificSkuProperties.instanceProperties` |  `object` Properties of the SKU instances being reserved.  
`specificSkuProperties.instanceProperties.machineType` |  `string` Specifies type of machine (name only) which has fixed number of vCPUs and fixed amount of memory. This also includes specifying custom machine type following custom-NUMBER_OF_CPUS-AMOUNT_OF_MEMORY pattern.  
`specificSkuProperties.instanceProperties.guestAccelerators[]` |  `object` Specifies accelerator type and count.  
`specificSkuProperties.instanceProperties.guestAccelerators[].acceleratorType` |  `string` Full or partial URL of the accelerator type resource to attach to this instance. For example: `projects/my-project/zones/us-central1-c/acceleratorTypes/nvidia-tesla-p100` If you are creating an instance template, specify only the accelerator name. See [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#introduction) for a full list of accelerator types.  
`specificSkuProperties.instanceProperties.guestAccelerators[].acceleratorCount` |  `integer` The number of the guest accelerator cards exposed to this instance.  
`specificSkuProperties.instanceProperties.minCpuPlatform` |  `string` Minimum cpu platform the reservation.  
`specificSkuProperties.instanceProperties.localSsds[]` |  `object` Specifies amount of local ssd to reserve with each instance. The type of disk is local-ssd.  
`specificSkuProperties.instanceProperties.localSsds[].diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Specifies the size of the disk in base-2 GB.  
`specificSkuProperties.instanceProperties.localSsds[].interface` |  `enum` Specifies the disk interface to use for attaching this disk, which is either `SCSI` or `NVME`. The default is `SCSI`. For performance characteristics of SCSI over NVMe, see [Local SSD performance](https://docs.cloud.google.com/compute/docs/disks#localssds).  
`specificSkuProperties.instanceProperties.maintenanceFreezeDurationHours` |  `integer` Specifies the number of hours after reservation creation where instances using the reservation won't be scheduled for maintenance.  
`specificSkuProperties.instanceProperties.locationHint` |  `string` An opaque location hint used to place the allocation close to other resources. This field is for use by internal tools that use the public API.  
`specificSkuProperties.instanceProperties.maintenanceInterval` |  `enum` Specifies the frequency of planned maintenance events. The accepted values are: `PERIODIC`.  
`specificSkuProperties.totalCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total number of instances for which capacity assurance is requested at a future time period.  
`specificSkuProperties.sourceInstanceTemplate` |  `string` The instance template that will be used to populate the ReservedInstanceProperties of the future reservation  
`aggregateReservation` |  `object` Aggregate reservation details for the future reservation.  
`aggregateReservation.vmFamily` |  `enum` The VM family that all instances scheduled against this reservation must belong to.  
`aggregateReservation.reservedResources[]` |  `object` futureReservations.list of reserved resources (CPUs, memory, accelerators).  
`aggregateReservation.reservedResources[].accelerator` |  `object` Properties of accelerator resources in this reservation.  
`aggregateReservation.reservedResources[].accelerator.acceleratorCount` |  `integer` Number of accelerators of specified type.  
`aggregateReservation.reservedResources[].accelerator.acceleratorType` |  `string` Full or partial URL to accelerator type. e.g. "projects/{PROJECT}/zones/{ZONE}/acceleratorTypes/ct4l"  
`aggregateReservation.inUseResources[]` |  `object` Output only. futureReservations.list of resources currently in use.  
`aggregateReservation.inUseResources[].accelerator` |  `object` Properties of accelerator resources in this reservation.  
`aggregateReservation.inUseResources[].accelerator.acceleratorCount` |  `integer` Number of accelerators of specified type.  
`aggregateReservation.inUseResources[].accelerator.acceleratorType` |  `string` Full or partial URL to accelerator type. e.g. "projects/{PROJECT}/zones/{ZONE}/acceleratorTypes/ct4l"  
`aggregateReservation.workloadType` |  `enum` The workload type of the instances that will target this reservation.  
`aggregateReservation.hostCount` |  `integer` Count of reserved hosts of specified VM family. The host has fixed number of accelerators based on the accelerator/vm-family selected.  
`aggregateReservation.inUseHostCount` |  `integer` Output only. Number of hosts currently in use. If there is one or more Instances running on the host, it is considered in use.  
`aggregateReservation.inUseInstanceCount` |  `integer` Output only. Number of instances currently in use in this reservation.  
`storagePoolProperties` |  `object` Storage pool details for the future reservation.  
`storagePoolProperties.requestedStoragePoolProvisionedCapacity` |  `object` Requested storage pool provisioned capacity.  
`storagePoolProperties.requestedStoragePoolProvisionedCapacity.poolProvisionedCapacityGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size of the storage pool in GiB.  
`storagePoolProperties.requestedStoragePoolProvisionedCapacity.poolProvisionedIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Provisioned IOPS of the storage pool. Only relevant if the storage pool type is hyperdisk-balanced.  
`storagePoolProperties.requestedStoragePoolProvisionedCapacity.poolProvisionedThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Provisioned throughput of the storage pool in MiB/s. Only relevant if the storage pool type is hyperdisk-balanced or hyperdisk-throughput.  
`storagePoolProperties.requestedExapoolProvisionedCapacityGb` |  `object` Requested exapool provisioned capacity in GiB.  
`storagePoolProperties.requestedExapoolProvisionedCapacityGb.writeOptimized` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size, in GiB, of provisioned write-optimized capacity for this Exapool  
`storagePoolProperties.requestedExapoolProvisionedCapacityGb.readOptimized` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size, in GiB, of provisioned read-optimized capacity for this Exapool  
`storagePoolProperties.requestedExapoolProvisionedCapacityGb.capacityOptimized` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size, in GiB, of provisioned capacity-optimized capacity for this Exapool  
`storagePoolProperties.storagePoolType` |  `string` Type of the storage pool.  
End of mutually exclusive fields.  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`autoCreatedReservationsDeleteTime` |  `string` Future timestamp when the FR auto-created reservations will be deleted by Compute Engine. Format of this field must be a valid href="https://www.ietf.org/rfc/rfc3339.txt">RFC3339 value.  
`autoCreatedReservationsDuration` |  `object` Specifies the duration of auto-created reservations. It represents relative time to future reservation startTime when auto-created reservations will be automatically deleted by Compute Engine. Duration time unit is represented as a count of seconds and fractions of seconds at nanosecond resolution.  
`autoCreatedReservationsDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`autoCreatedReservationsDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
End of mutually exclusive fields.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.futureReservations.get`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
