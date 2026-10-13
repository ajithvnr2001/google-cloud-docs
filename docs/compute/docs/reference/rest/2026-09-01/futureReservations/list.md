---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/futureReservations/list/
title: Method: futureReservations.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:04:14.065437+00:00
---

# Method: futureReservations.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/futureReservations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: futureReservations.list Stay organized with collections  Save and categorize content based on your preferences. 

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



API Version : 2026-09-01

A list of all the future reservations that have been configured for the specified project in specified zone.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/zones/{zone}/futureReservations?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`zone` |  `string` Name of the zone for this request. Name should conform to RFC1035.  
  
### Query parameters

Parameters  
---  
`maxResults` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The maximum number of results per page that should be returned. If the number of available results is larger than `maxResults`, Compute Engine returns a `nextPageToken` that can be used to get the next page of results in subsequent list requests. Acceptable values are `0` to `500`, inclusive. (Default: `500`)  
`pageToken` |  `string` Specifies a page token to use. Set `pageToken` to the `nextPageToken` returned by a previous list request to get the next page of results.  
`filter` |  `string` A filter expression that filters resources listed in the response. Most Compute resources support two types of filter expressions: expressions that support regular expressions and expressions that follow API improvement proposal [AIP-160](https://google.aip.dev/160). These two types of filter expressions cannot be mixed in one request.If you want to use AIP-160, your expression must specify the field name, an operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The operator must be either `=`, `!=`, `>`, `<`, `<=`, `>=` or `:`.For example, if you are filtering Compute Engine instances, you can exclude instances named `example-instance` by specifying `name != example-instance`.The `:*` comparison can be used to test whether a key has been defined. For example, to find all objects with `owner` label use:
    
    
    labels.owner:*
    

You can also filter nested fields. For example, you could specify `scheduling.automaticRestart = false` to include instances only if they are not scheduled for automatic restarts. You can use filtering on nested fields to filter based on [resource labels](https://docs.cloud.google.com/compute/docs/labeling-resources).To filter on multiple expressions, provide each separate expression within parentheses. For example:
    
    
    (scheduling.automaticRestart = true)
    (cpuPlatform = "Intel Skylake")
    

By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example:
    
    
    (cpuPlatform = "Intel Skylake") OR
    (cpuPlatform = "Intel Broadwell") AND
    (scheduling.automaticRestart = true)
    

If you want to use a regular expression, use the `eq` (equal) or `ne` (not equal) operator against a single un-parenthesized expression with or without quotes or against multiple parenthesized expressions. Examples:`fieldname eq unquoted literal` `fieldname eq 'single quoted literal'` `fieldname eq "double quoted literal"` `(fieldname1 eq literal) (fieldname2 ne "literal")`The literal value is interpreted as a regular expression using Google [RE2](https://github.com/google/re2/wiki/Syntax) library syntax. The literal value must match the entire field.For example, to filter for instances that do not end with name "instance", you would use `name ne .*instance`.You cannot combine constraints on multiple fields using regular expressions.  
`orderBy` |  `string` Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.You can also sort results in descending order based on the creation timestamp using `orderBy="creationTimestamp desc"`. This sorts results based on the `creationTimestamp` field in reverse chronological order (newest result first). Use this to sort resources like operations so that the newest operation is returned first.Currently, only sorting by `name` or `creationTimestamp desc` is supported.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "items": [
        {
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
              "locationHint": string
            },
            "totalCount": string,
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
          "storagePoolProperties": {
            "storagePoolType": string,
    
            // The following is a list of mutually exclusive fields. At most one of the
            // fields will be set in a response:
            "requestedStoragePoolProvisionedCapacity": {
              "poolProvisionedCapacityGb": string,
              "poolProvisionedIops": string,
              "poolProvisionedThroughput": string
            },
            "requestedExapoolProvisionedCapacityGb": {
              "writeOptimized": string,
              "readOptimized": string,
              "capacityOptimized": string
            }
            // End of mutually exclusive fields.
          },
          "autoCreatedReservationsDeleteTime": string,
          "autoCreatedReservationsDuration": {
            "seconds": string,
            "nanos": integer
          },
          "kind": string,
          "id": string,
          "creationTimestamp": string,
          "selfLink": string,
          "selfLinkWithId": string,
          "zone": string,
          "description": string,
          "name": string,
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
            "projectMap": {
              string: {
                "projectId": string
              },
              ...
            }
          },
          "namePrefix": string,
          "status": {
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
                  "projectMap": {
                    string: {
                      "projectId": string
                    },
                    ...
                  }
                },
    
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
                    "locationHint": string
                  },
                  "totalCount": string,
                  "sourceInstanceTemplate": string
                }
                // End of mutually exclusive fields.
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
            },
    
            // The following is a list of mutually exclusive fields. At most one of the
            // fields will be set in a response:
            "storagePoolProvisionedCapacity": {
              "poolProvisionedCapacityGb": string,
              "poolProvisionedIops": string,
              "poolProvisionedThroughput": string
            },
            "exapoolProvisionedCapacityGb": {
              "writeOptimized": string,
              "readOptimized": string,
              "capacityOptimized": string
            }
            // End of mutually exclusive fields.
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
          "enableEmergentMaintenance": boolean,
          "params": {
            "resourceManagerTags": {
              string: string,
              ...
            }
          },
          "confidentialComputeType": enum,
          "resourceMetadata": {
            "resourceType": string,
            "apiVersion": string
          },
          "resourceName": string,
          "colocationResource": string
        }
      ],
      "nextPageToken": string,
      "warning": {
        "code": enum,
        "message": string,
        "data": [
          {
            "key": string,
            "value": string
          }
        ]
      },
      "selfLink": string,
      "etag": string,
      "unreachables": [
        string
      ]
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of resource.Always `compute#FutureReservationsListResponse` for lists of reservations  
`id` |  `string` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items[]` |  `object` Output only. A list of future reservation resources.  
`items[].specificSkuProperties` |  `object` Future Reservation configuration to indicate instance properties and total count.  
`items[].specificSkuProperties.instanceProperties` |  `object` Properties of the SKU instances being reserved.  
`items[].specificSkuProperties.instanceProperties.machineType` |  `string` Specifies type of machine (name only) which has fixed number of vCPUs and fixed amount of memory. This also includes specifying custom machine type following custom-NUMBER_OF_CPUS-AMOUNT_OF_MEMORY pattern.  
`items[].specificSkuProperties.instanceProperties.guestAccelerators[]` |  `object` Specifies accelerator type and count.  
`items[].specificSkuProperties.instanceProperties.guestAccelerators[].acceleratorType` |  `string` Full or partial URL of the accelerator type resource to attach to this instance. For example: `projects/my-project/zones/us-central1-c/acceleratorTypes/nvidia-tesla-p100` If you are creating an instance template, specify only the accelerator name. See [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#introduction) for a full list of accelerator types.  
`items[].specificSkuProperties.instanceProperties.guestAccelerators[].acceleratorCount` |  `integer` The number of the guest accelerator cards exposed to this instance.  
`items[].specificSkuProperties.instanceProperties.minCpuPlatform` |  `string` Minimum cpu platform the reservation.  
`items[].specificSkuProperties.instanceProperties.localSsds[]` |  `object` Specifies amount of local ssd to reserve with each instance. The type of disk is local-ssd.  
`items[].specificSkuProperties.instanceProperties.localSsds[].diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Specifies the size of the disk in base-2 GB.  
`items[].specificSkuProperties.instanceProperties.localSsds[].interface` |  `enum` Specifies the disk interface to use for attaching this disk, which is either `SCSI` or `NVME`. The default is `SCSI`. For performance characteristics of SCSI over NVMe, see [Local SSD performance](https://docs.cloud.google.com/compute/docs/disks#localssds).  
`items[].specificSkuProperties.instanceProperties.locationHint` |  `string` An opaque location hint used to place the allocation close to other resources. This field is for use by internal tools that use the public API.  
`items[].specificSkuProperties.totalCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total number of instances for which capacity assurance is requested at a future time period.  
`items[].specificSkuProperties.sourceInstanceTemplate` |  `string` The instance template that will be used to populate the ReservedInstanceProperties of the future reservation  
`items[].aggregateReservation` |  `object` Aggregate reservation details for the future reservation.  
`items[].aggregateReservation.vmFamily` |  `enum` The VM family that all instances scheduled against this reservation must belong to.  
`items[].aggregateReservation.reservedResources[]` |  `object` futureReservations.list of reserved resources (CPUs, memory, accelerators).  
`items[].aggregateReservation.reservedResources[].accelerator` |  `object` Properties of accelerator resources in this reservation.  
`items[].aggregateReservation.reservedResources[].accelerator.acceleratorCount` |  `integer` Number of accelerators of specified type.  
`items[].aggregateReservation.reservedResources[].accelerator.acceleratorType` |  `string` Full or partial URL to accelerator type. e.g. "projects/{PROJECT}/zones/{ZONE}/acceleratorTypes/ct4l"  
`items[].aggregateReservation.inUseResources[]` |  `object` Output only. futureReservations.list of resources currently in use.  
`items[].aggregateReservation.inUseResources[].accelerator` |  `object` Properties of accelerator resources in this reservation.  
`items[].aggregateReservation.inUseResources[].accelerator.acceleratorCount` |  `integer` Number of accelerators of specified type.  
`items[].aggregateReservation.inUseResources[].accelerator.acceleratorType` |  `string` Full or partial URL to accelerator type. e.g. "projects/{PROJECT}/zones/{ZONE}/acceleratorTypes/ct4l"  
`items[].aggregateReservation.workloadType` |  `enum` The workload type of the instances that will target this reservation.  
`items[].storagePoolProperties` |  `object` Storage pool details for the future reservation.  
`items[].storagePoolProperties.requestedStoragePoolProvisionedCapacity` |  `object` Requested storage pool provisioned capacity.  
`items[].storagePoolProperties.requestedStoragePoolProvisionedCapacity.poolProvisionedCapacityGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size of the storage pool in GiB.  
`items[].storagePoolProperties.requestedStoragePoolProvisionedCapacity.poolProvisionedIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Provisioned IOPS of the storage pool. Only relevant if the storage pool type is hyperdisk-balanced.  
`items[].storagePoolProperties.requestedStoragePoolProvisionedCapacity.poolProvisionedThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Provisioned throughput of the storage pool in MiB/s. Only relevant if the storage pool type is hyperdisk-balanced or hyperdisk-throughput.  
`items[].storagePoolProperties.requestedExapoolProvisionedCapacityGb` |  `object` Requested exapool provisioned capacity in GiB.  
`items[].storagePoolProperties.requestedExapoolProvisionedCapacityGb.writeOptimized` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size, in GiB, of provisioned write-optimized capacity for this Exapool  
`items[].storagePoolProperties.requestedExapoolProvisionedCapacityGb.readOptimized` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size, in GiB, of provisioned read-optimized capacity for this Exapool  
`items[].storagePoolProperties.requestedExapoolProvisionedCapacityGb.capacityOptimized` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size, in GiB, of provisioned capacity-optimized capacity for this Exapool  
`items[].storagePoolProperties.storagePoolType` |  `string` Type of the storage pool.  
`items[].autoCreatedReservationsDeleteTime` |  `string` Future timestamp when the FR auto-created reservations will be deleted by Compute Engine. Format of this field must be a valid href="https://www.ietf.org/rfc/rfc3339.txt">RFC3339 value.  
`items[].autoCreatedReservationsDuration` |  `object` Specifies the duration of auto-created reservations. It represents relative time to future reservation startTime when auto-created reservations will be automatically deleted by Compute Engine. Duration time unit is represented as a count of seconds and fractions of seconds at nanosecond resolution.  
`items[].autoCreatedReservationsDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`items[].autoCreatedReservationsDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`items[].kind` |  `string` Output only. Type of the resource. Always `compute#futureReservation` for future reservations.  
`items[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. A unique identifier for this future reservation. The server defines this identifier.  
`items[].creationTimestamp` |  `string` Output only. The creation timestamp for this future reservation in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`items[].selfLinkWithId` |  `string` Output only. Server-defined URL for this resource with the resource id.  
`items[].zone` |  `string` Output only. URL of the Zone where this future reservation resides.  
`items[].description` |  `string` An optional description of this resource. Provide this property when you create the future reservation.  
`items[].name` |  `string` The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items[].timeWindow` |  `object` Time window for this Future Reservation.  
`items[].timeWindow.endTime` |  `string`  
`items[].timeWindow.duration` |  `object`  
`items[].timeWindow.duration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`items[].timeWindow.duration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`items[].timeWindow.startTime` |  `string` Start time of the Future Reservation. The startTime is an RFC3339 string.  
`items[].shareSettings` |  `object` futureReservations.list of Projects/Folders to share with.  
`items[].shareSettings.shareType` |  `enum` Type of sharing for this shared-reservation  
`items[].shareSettings.projectMap[]` |  `map (key: string, value: object)` A map of project id and project config. This is only valid when shareType's value is SPECIFIC_PROJECTS.  
`items[].shareSettings.projectMap[].projectId` |  `string` The project ID, should be same as the key of this project config in the parent map.  
`items[].namePrefix` |  `string` Name prefix for the reservations to be created at the time of delivery. The name prefix must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Maximum allowed length for name prefix is 20. Automatically created reservations name format will be -date-####.  
`items[].status` |  `object` Output only. Status of the Future Reservation  
`items[].status.storagePoolProvisionedCapacity` |  `object` Output only. Storage pool provisioned capacities for each SKU type.  
`items[].status.storagePoolProvisionedCapacity.poolProvisionedCapacityGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size of the storage pool in GiB.  
`items[].status.storagePoolProvisionedCapacity.poolProvisionedIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Provisioned IOPS of the storage pool. Only relevant if the storage pool type is hyperdisk-balanced.  
`items[].status.storagePoolProvisionedCapacity.poolProvisionedThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Provisioned throughput of the storage pool in MiB/s. Only relevant if the storage pool type is hyperdisk-balanced or hyperdisk-throughput.  
`items[].status.exapoolProvisionedCapacityGb` |  `object` Output only. Exapool provisioned capacities for each SKU type.  
`items[].status.exapoolProvisionedCapacityGb.writeOptimized` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size, in GiB, of provisioned write-optimized capacity for this Exapool  
`items[].status.exapoolProvisionedCapacityGb.readOptimized` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size, in GiB, of provisioned read-optimized capacity for this Exapool  
`items[].status.exapoolProvisionedCapacityGb.capacityOptimized` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size, in GiB, of provisioned capacity-optimized capacity for this Exapool  
`items[].status.procurementStatus` |  `enum` Output only. Current state of this Future Reservation  
`items[].status.lockTime` |  `string` Output only. Time when Future Reservation would become LOCKED, after which no modifications to Future Reservation will be allowed. Applicable only after the Future Reservation is in the APPROVED state. The lockTime is an RFC3339 string. The procurementStatus will transition to PROCURING state at this time.  
`items[].status.autoCreatedReservations[]` |  `string` Output only. Fully qualified urls of the automatically created reservations at startTime.  
`items[].status.fulfilledCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. This count indicates the fulfilled capacity so far. This is set during "PROVISIONING" state. This count also includes capacity delivered as part of existing matching reservations.  
`items[].status.specificSkuProperties` |  `object`  
`items[].status.specificSkuProperties.sourceInstanceTemplateId` |  `string` ID of the instance template used to populate the Future Reservation properties.  
`items[].status.amendmentStatus` |  `enum` Output only. The current status of the requested amendment.  
`items[].status.lastKnownGoodState` |  `object` Output only. This field represents the future reservation before an amendment was requested. If the amendment is declined, the Future Reservation will be reverted to the last known good state. The last known good state is not set when updating a future reservation whose Procurement Status is DRAFTING.  
`items[].status.lastKnownGoodState.futureReservationSpecs` |  `object`  
`items[].status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties` |  `object` Output only. The previous instance related properties of the Future Reservation.  
`items[].status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties` |  `object` Properties of the SKU instances being reserved.  
`items[].status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.machineType` |  `string` Specifies type of machine (name only) which has fixed number of vCPUs and fixed amount of memory. This also includes specifying custom machine type following custom-NUMBER_OF_CPUS-AMOUNT_OF_MEMORY pattern.  
`items[].status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.guestAccelerators[]` |  `object` Specifies accelerator type and count.  
`items[].status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.guestAccelerators[].acceleratorType` |  `string` Full or partial URL of the accelerator type resource to attach to this instance. For example: `projects/my-project/zones/us-central1-c/acceleratorTypes/nvidia-tesla-p100` If you are creating an instance template, specify only the accelerator name. See [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#introduction) for a full list of accelerator types.  
`items[].status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.guestAccelerators[].acceleratorCount` |  `integer` The number of the guest accelerator cards exposed to this instance.  
`items[].status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.minCpuPlatform` |  `string` Minimum cpu platform the reservation.  
`items[].status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.localSsds[]` |  `object` Specifies amount of local ssd to reserve with each instance. The type of disk is local-ssd.  
`items[].status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.localSsds[].diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Specifies the size of the disk in base-2 GB.  
`items[].status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.localSsds[].interface` |  `enum` Specifies the disk interface to use for attaching this disk, which is either `SCSI` or `NVME`. The default is `SCSI`. For performance characteristics of SCSI over NVMe, see [Local SSD performance](https://docs.cloud.google.com/compute/docs/disks#localssds).  
`items[].status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.instanceProperties.locationHint` |  `string` An opaque location hint used to place the allocation close to other resources. This field is for use by internal tools that use the public API.  
`items[].status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.totalCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total number of instances for which capacity assurance is requested at a future time period.  
`items[].status.lastKnownGoodState.futureReservationSpecs.specificSkuProperties.sourceInstanceTemplate` |  `string` The instance template that will be used to populate the ReservedInstanceProperties of the future reservation  
`items[].status.lastKnownGoodState.futureReservationSpecs.timeWindow` |  `object` Output only. The previous time window of the Future Reservation.  
`items[].status.lastKnownGoodState.futureReservationSpecs.timeWindow.endTime` |  `string`  
`items[].status.lastKnownGoodState.futureReservationSpecs.timeWindow.duration` |  `object`  
`items[].status.lastKnownGoodState.futureReservationSpecs.timeWindow.duration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`items[].status.lastKnownGoodState.futureReservationSpecs.timeWindow.duration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`items[].status.lastKnownGoodState.futureReservationSpecs.timeWindow.startTime` |  `string` Start time of the Future Reservation. The startTime is an RFC3339 string.  
`items[].status.lastKnownGoodState.futureReservationSpecs.shareSettings` |  `object` Output only. The previous share settings of the Future Reservation.  
`items[].status.lastKnownGoodState.futureReservationSpecs.shareSettings.shareType` |  `enum` Type of sharing for this shared-reservation  
`items[].status.lastKnownGoodState.futureReservationSpecs.shareSettings.projectMap[]` |  `map (key: string, value: object)` A map of project id and project config. This is only valid when shareType's value is SPECIFIC_PROJECTS.  
`items[].status.lastKnownGoodState.futureReservationSpecs.shareSettings.projectMap[].projectId` |  `string` The project ID, should be same as the key of this project config in the parent map.  
`items[].status.lastKnownGoodState.procurementStatus` |  `enum` Output only. The status of the last known good state for the Future Reservation.  
`items[].status.lastKnownGoodState.namePrefix` |  `string` Output only. The name prefix of the Future Reservation before an amendment was requested.  
`items[].status.lastKnownGoodState.description` |  `string` Output only. The description of the FutureReservation before an amendment was requested.  
`items[].status.lastKnownGoodState.lockTime` |  `string` Output only. The lock time of the FutureReservation before an amendment was requested.  
`items[].status.lastKnownGoodState.existingMatchingUsageInfo` |  `object` Output only. Represents the matching usage for the future reservation before an amendment was requested.  
`items[].status.lastKnownGoodState.existingMatchingUsageInfo.count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Count to represent min(FR totalCount, matching_reserved_capacity+matching_unreserved_instances)  
`items[].status.lastKnownGoodState.existingMatchingUsageInfo.timestamp` |  `string` Output only. Timestamp when the matching usage was calculated  
`items[].status.existingMatchingUsageInfo` |  `object` Output only. Represents the existing matching usage for the future reservation.  
`items[].status.existingMatchingUsageInfo.count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Count to represent min(FR totalCount, matching_reserved_capacity+matching_unreserved_instances)  
`items[].status.existingMatchingUsageInfo.timestamp` |  `string` Output only. Timestamp when the matching usage was calculated  
`items[].planningStatus` |  `enum` Planning state before being submitted for evaluation  
`items[].autoDeleteAutoCreatedReservations` |  `boolean` Setting for enabling or disabling automatic deletion for auto-created reservation. If set to true, auto-created reservations will be deleted at Future Reservation's end time (default) or at user's defined timestamp if any of the [autoCreatedReservationsDeleteTime, autoCreatedReservationsDuration] values is specified. For keeping auto-created reservation indefinitely, this value should be set to false.  
`items[].specificReservationRequired` |  `boolean` Indicates whether the auto-created reservation can be consumed by VMs with affinity for "any" reservation. If the field is set, then only VMs that target the reservation by name can consume from the delivered reservation.  
`items[].reservationName` |  `string` Name of reservations where the capacity is provisioned at the time of delivery of future reservations. If the reservation with the given name does not exist already, it is created automatically at the time of Approval with INACTIVE state till specified start-time. Either provide the reservationName or a namePrefix.  
`items[].deploymentType` |  `enum` Type of the deployment requested as part of future reservation.  
`items[].commitmentInfo` |  `object` If not present, then FR will not deliver a new commitment or update an existing commitment.  
`items[].commitmentInfo.commitmentPlan` |  `enum` Indicates if a Commitment needs to be created as part of FR delivery. If this field is not present, then no commitment needs to be created.  
`items[].commitmentInfo.commitmentName` |  `string` name of the commitment where capacity is being delivered to.  
`items[].commitmentInfo.previousCommitmentTerms` |  `enum` Only applicable if FR is delivering to the same reservation. If set, all parent commitments will be extended to match the end date of the plan for this commitment.  
`items[].schedulingType` |  `enum` Maintenance information for this reservation  
`items[].reservationMode` |  `enum` The reservation mode which determines reservation-termination behavior and expected pricing.  
`items[].enableEmergentMaintenance` |  `boolean` Indicates if this group of VMs have emergent maintenance enabled.  
`items[].params` |  `object` Input only. Additional params passed with the request, but not persisted as part of resource payload.  
`items[].params.resourceManagerTags` |  `map (key: string, value: string)` Input only. Resource manager tags to be bound to the future reservation. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). Keys and values can be either in numeric format, such as `tagKeys/{tag_key_id}` and `tagValues/{tag_value_id}` or in namespaced format such as `{org_id|projectId}/{tag_key_short_name}` and `{tag_value_short_name}`. The field is ignored (both PUT & PATCH) when empty.  
`items[].confidentialComputeType` |  `enum`  
`items[].resourceMetadata` |  `object` Output only. Contains standard resource metadata for an FutureReservation resource. It is populated for each instance of the FutureReservation resource, and includes the `apiVersion` the instance was retrieved through, and its canonical `resourceType` name.  
`items[].resourceMetadata.resourceType` |  `string` The canonical resource type name in the format of a resource type as defined by [AIP-123](https://google.aip.dev/123). For example, `"compute.googleapis.com/Instance"`.  
`items[].resourceMetadata.apiVersion` |  `string` The version of the API interface that this resource was retrieved through. For example, `"2025-01-01"` or `"2025-01-01-preview"`.  
`items[].resourceName` |  `string` Name of the resource intended to be delivered. Name should conform to RFC1035. This will be the name of storage pool or Exapool for persistent disk FRs.  
`items[].colocationResource` |  `string` Full or partial URL of an existing future reservation to indicate intent for reserving capacity in the same cluster as the colocation resource.  
`nextPageToken` |  `string` Output only. This token allows you to get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
`warning` |  `object` Output only. Informational warning message.  
`warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warning.message` |  `string` Output only. A human-readable description of the warning code.  
`warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`selfLink` |  `string` Output only. Server-defined URL for this resource.  
`etag` |  `string`  
`unreachables[]` |  `string` Output only. Unreachable resources.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.futureReservations.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
