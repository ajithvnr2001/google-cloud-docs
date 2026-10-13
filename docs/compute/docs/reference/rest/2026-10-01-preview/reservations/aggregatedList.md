---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/reservations/aggregatedList/
title: Method: reservations.aggregatedList \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:00.765937+00:00
---

# Method: reservations.aggregatedList  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/reservations/aggregatedList/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: reservations.aggregatedList Stay organized with collections  Save and categorize content based on your preferences. 

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
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-10-01-preview

Retrieves an aggregated list of reservations.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/aggregated/reservations?$apiVersion=2026-10-01-preview`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
  
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
`includeAllScopes` |  `boolean` Indicates whether every visible scope for each scope type (zone, region, global) should be included in the response. For new resource types added after this field, the flag has no effect as new resource types will always include every visible scope for each scope type in response. For resource types which predate this field, if this flag is omitted or false, only scopes of the scope types where the resource type is expected to be found will be included.  
`serviceProjectNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The Shared VPC service project id or service project number for which aggregated list request is invoked for subnetworks list-usable api.  
  
### Request body

The request body must be empty.

### Response body

Contains a list of reservations.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "items": {
        string: {
          "reservations": [
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
              },
    
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
                "workloadType": enum
              }
              // End of mutually exclusive fields.,
    
              // The following is a list of mutually exclusive fields. At most one of the
              // fields will be set in a response:
              "deleteAtTime": string,
              "deleteAfterDuration": {
                "seconds": string,
                "nanos": integer
              }
              // End of mutually exclusive fields.
            }
          ],
          "warning": {
            "code": enum,
            "message": string,
            "data": [
              {
                "key": string,
                "value": string
              }
            ]
          }
        },
        ...
      },
      "nextPageToken": string,
      "selfLink": string,
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
      "unreachables": [
        string
      ]
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of resource.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items` |  `map (key: string, value: object)` A list of Allocation resources.**Key:** Name of the scope containing this set of reservations.  
`items.reservations[]` |  `object` A list of reservations contained in this scope.  
`items.reservations[].specificReservation` |  `object` Reservation for instances with specific machine shapes.  
`items.reservations[].specificReservation.instanceProperties` |  `object` The instance properties for the reservation.  
`items.reservations[].specificReservation.instanceProperties.machineType` |  `string` Specifies type of machine (name only) which has fixed number of vCPUs and fixed amount of memory. This also includes specifying custom machine type following custom-NUMBER_OF_CPUS-AMOUNT_OF_MEMORY pattern.  
`items.reservations[].specificReservation.instanceProperties.guestAccelerators[]` |  `object` Specifies accelerator type and count.  
`items.reservations[].specificReservation.instanceProperties.guestAccelerators[].acceleratorType` |  `string` Full or partial URL of the accelerator type resource to attach to this instance. For example: `projects/my-project/zones/us-central1-c/acceleratorTypes/nvidia-tesla-p100` If you are creating an instance template, specify only the accelerator name. See [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#introduction) for a full list of accelerator types.  
`items.reservations[].specificReservation.instanceProperties.guestAccelerators[].acceleratorCount` |  `integer` The number of the guest accelerator cards exposed to this instance.  
`items.reservations[].specificReservation.instanceProperties.minCpuPlatform` |  `string` Minimum cpu platform the reservation.  
`items.reservations[].specificReservation.instanceProperties.localSsds[]` |  `object` Specifies amount of local ssd to reserve with each instance. The type of disk is local-ssd.  
`items.reservations[].specificReservation.instanceProperties.localSsds[].diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Specifies the size of the disk in base-2 GB.  
`items.reservations[].specificReservation.instanceProperties.localSsds[].interface` |  `enum` Specifies the disk interface to use for attaching this disk, which is either `SCSI` or `NVME`. The default is `SCSI`. For performance characteristics of SCSI over NVMe, see [Local SSD performance](https://docs.cloud.google.com/compute/docs/disks#localssds).  
`items.reservations[].specificReservation.instanceProperties.locationHint` |  `string` An opaque location hint used to place the allocation close to other resources. This field is for use by internal tools that use the public API.  
`items.reservations[].specificReservation.count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Specifies the number of resources that are allocated.  
`items.reservations[].specificReservation.inUseCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Indicates how many instances are in use.  
`items.reservations[].specificReservation.assuredCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Indicates how many instances are actually usable currently.  
`items.reservations[].specificReservation.sourceInstanceTemplate` |  `string` Specifies the instance template to create the reservation. If you use this field, you must exclude the `instanceProperties` field.This field is optional, and it can be a full or partial URL. For example, the following are all valid URLs to an instance template: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/global/instanceTemplates/instanceTemplate`
  * `projects/project/global/instanceTemplates/instanceTemplate`
  * `global/instanceTemplates/instanceTemplate`

  
`items.reservations[].aggregateReservation` |  `object` Reservation for aggregated resources, providing shape flexibility.  
`items.reservations[].aggregateReservation.vmFamily` |  `enum` The VM family that all instances scheduled against this reservation must belong to.  
`items.reservations[].aggregateReservation.reservedResources[]` |  `object` reservations.list of reserved resources (CPUs, memory, accelerators).  
`items.reservations[].aggregateReservation.reservedResources[].accelerator` |  `object` Properties of accelerator resources in this reservation.  
`items.reservations[].aggregateReservation.reservedResources[].accelerator.acceleratorCount` |  `integer` Number of accelerators of specified type.  
`items.reservations[].aggregateReservation.reservedResources[].accelerator.acceleratorType` |  `string` Full or partial URL to accelerator type. e.g. "projects/{PROJECT}/zones/{ZONE}/acceleratorTypes/ct4l"  
`items.reservations[].aggregateReservation.inUseResources[]` |  `object` Output only. reservations.list of resources currently in use.  
`items.reservations[].aggregateReservation.inUseResources[].accelerator` |  `object` Properties of accelerator resources in this reservation.  
`items.reservations[].aggregateReservation.inUseResources[].accelerator.acceleratorCount` |  `integer` Number of accelerators of specified type.  
`items.reservations[].aggregateReservation.inUseResources[].accelerator.acceleratorType` |  `string` Full or partial URL to accelerator type. e.g. "projects/{PROJECT}/zones/{ZONE}/acceleratorTypes/ct4l"  
`items.reservations[].aggregateReservation.workloadType` |  `enum` The workload type of the instances that will target this reservation.  
`items.reservations[].deleteAtTime` |  `string` Absolute time in future when the reservation will be auto-deleted by Compute Engine. Timestamp is represented in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items.reservations[].deleteAfterDuration` |  `object` Duration time relative to reservation creation when Compute Engine will automatically delete this resource.  
`items.reservations[].deleteAfterDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`items.reservations[].deleteAfterDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`items.reservations[].kind` |  `string` Output only. Type of the resource. Always `compute#reservations` for reservations.  
`items.reservations[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items.reservations[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items.reservations[].selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`items.reservations[].zone` |  `string` Zone in which the reservation resides. A zone must be provided if the reservation is created within a commitment.  
`items.reservations[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`items.reservations[].name` |  `string` The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items.reservations[].commitment` |  `string` Output only. Full or partial URL to a parent commitment. This field displays for reservations that are tied to a commitment.  
`items.reservations[].linkedCommitments[]` |  `string` Output only. Full or partial URL to parent commitments. This field displays for reservations that are tied to multiple commitments.  
`items.reservations[].specificReservationRequired` |  `boolean` Indicates whether the reservation can be consumed by VMs with affinity for "any" reservation. If the field is set, then only VMs that target the reservation by name can consume from this reservation.  
`items.reservations[].status` |  `enum` Output only. The status of the reservation. 

  * `CREATING`: Reservation resources are being allocated.
  * `READY`: Reservation resources have been allocated, and the reservation is ready for use.
  * `DELETING`: Reservation deletion is in progress.
  * `UPDATING`: Reservation update is in progress.

  
`items.reservations[].shareSettings` |  `object` Specify share-settings to create a shared reservation. This property is optional. For more information about the syntax and options for this field and its subfields, see the guide for [creating a shared reservation.](https://cloud.google.com/compute/docs/instances/reservations-shared#creating_a_shared_reservation)  
`items.reservations[].shareSettings.shareType` |  `enum` Type of sharing for this shared-reservation  
`items.reservations[].shareSettings.projectMap[]` |  `map (key: string, value: object)` A map of project id and project config. This is only valid when shareType's value is SPECIFIC_PROJECTS.  
`items.reservations[].shareSettings.projectMap[].projectId` |  `string` The project ID, should be same as the key of this project config in the parent map.  
`items.reservations[].satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`items.reservations[].resourcePolicies` |  `map (key: string, value: string)` Resource policies to be added to this reservation. The key is defined by user, and the value is resource policy url. This is to define placement policy with reservation.  
`items.reservations[].resourceStatus` |  `object` Output only. Status information for Reservation resource.  
`items.reservations[].resourceStatus.specificSkuAllocation` |  `object` Allocation Properties of this reservation.  
`items.reservations[].resourceStatus.specificSkuAllocation.sourceInstanceTemplateId` |  `string` ID of the instance template used to populate reservation properties.  
`items.reservations[].resourceStatus.specificSkuAllocation.utilizations` |  `map (key: string, value: string ([int64](https://developers.google.com/discovery/v1/type-format) format))` Per service utilization breakdown. The Key is the Google Cloud managed service name.  
`items.reservations[].resourceStatus.reservationMaintenance` |  `object` Maintenance information for this reservation  
`items.reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance` |  `object` Maintenance information on this group of VMs.  
`items.reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.type` |  `enum` Defines the type of maintenance.  
`items.reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.canReschedule` |  `boolean` Indicates if the maintenance can be customer triggered.  
`items.reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.windowStartTime` |  `string` The current start time of the maintenance window. This timestamp value is in RFC3339 text format.  
`items.reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.windowEndTime` |  `string` The time by which the maintenance disruption will be completed. This timestamp value is in RFC3339 text format.  
`items.reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.latestWindowStartTime` |  `string` The latest time for the planned maintenance window to start. This timestamp value is in RFC3339 text format.  
`items.reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.maintenanceStatus` |  `enum`  
`items.reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.maintenanceOnShutdown` |  `boolean` Indicates whether the UpcomingMaintenance will be triggered on VM shutdown.  
`items.reservations[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.maintenanceReasons[]` |  `enum` The reasons for the maintenance. Only valid for vms.  
`items.reservations[].resourceStatus.reservationMaintenance.maintenanceOngoingCount` |  `integer` Progress for ongoing maintenance for this group of VMs/hosts. Describes number of hosts in the block that have ongoing maintenance.  
`items.reservations[].resourceStatus.reservationMaintenance.maintenancePendingCount` |  `integer` Progress for ongoing maintenance for this group of VMs/hosts. Describes number of hosts in the block that have pending maintenance.  
`items.reservations[].resourceStatus.reservationMaintenance.schedulingType` |  `enum` The type of maintenance for the reservation.  
`items.reservations[].resourceStatus.reservationMaintenance.subblockInfraMaintenanceOngoingCount` |  `integer` Describes number of subblock Infrastructure that has ongoing maintenance. Here, Subblock Infrastructure Maintenance pertains to upstream hardware contained in the Subblock that is necessary for a VM Family(e.g. NVLink Domains). Not all VM Families will support this field.  
`items.reservations[].resourceStatus.reservationMaintenance.subblockInfraMaintenancePendingCount` |  `integer` Describes number of subblock Infrastructure that has pending maintenance. Here, Subblock Infrastructure Maintenance pertains to upstream hardware contained in the Subblock that is necessary for a VM Family (e.g. NVLink Domains). Not all VM Families will support this field.  
`items.reservations[].resourceStatus.reservationMaintenance.instanceMaintenanceOngoingCount` |  `integer` Describes number of instances that have ongoing maintenance.  
`items.reservations[].resourceStatus.reservationMaintenance.instanceMaintenancePendingCount` |  `integer` Describes number of instances that have pending maintenance.  
`items.reservations[].resourceStatus.reservationBlockCount` |  `integer` The number of reservation blocks associated with this reservation.  
`items.reservations[].resourceStatus.healthInfo` |  `object` Output only. Health information for the reservation.  
`items.reservations[].resourceStatus.healthInfo.healthStatus` |  `enum` The health status of the reservation.  
`items.reservations[].resourceStatus.healthInfo.healthyBlockCount` |  `integer` The number of reservation blocks that are healthy.  
`items.reservations[].resourceStatus.healthInfo.degradedBlockCount` |  `integer` The number of reservation blocks that are degraded.  
`items.reservations[].reservationSharingPolicy` |  `object` Specify the reservation sharing policy. If unspecified, the reservation will not be shared with Google Cloud managed services.  
`items.reservations[].reservationSharingPolicy.serviceShareType` |  `enum` Sharing config for all Google Cloud services.  
`items.reservations[].deploymentType` |  `enum` Specifies the deployment strategy for this reservation.  
`items.reservations[].advancedDeploymentControl` |  `object` Advanced control for cluster management, applicable only to DENSE deployment type reservations.  
`items.reservations[].advancedDeploymentControl.reservationOperationalMode` |  `enum` Indicates chosen reservation operational mode for the reservation.  
`items.reservations[].enableEmergentMaintenance` |  `boolean` Indicates whether Compute Engine allows unplanned maintenance for your VMs; for example, to fix hardware errors.  
`items.reservations[].protectionTier` |  `enum` Protection tier for the workload which specifies the workload expectations in the event of infrastructure failures at data center (e.g. power and/or cooling failures).  
`items.reservations[].schedulingType` |  `enum` The type of maintenance for the reservation.  
`items.reservations[].params` |  `object` Input only. Additional params passed with the request, but not persisted as part of resource payload.  
`items.reservations[].params.resourceManagerTags` |  `map (key: string, value: string)` Input only. Resource manager tags to be bound to the reservation. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). Keys and values can be either in numeric format, such as `tagKeys/{tag_key_id}` and `tagValues/{tag_value_id}` or in namespaced format such as `{org_id|projectId}/{tag_key_short_name}` and `{tag_value_short_name}`. The field is ignored (both PUT & PATCH) when empty.  
`items.reservations[].confidentialComputeType` |  `enum`  
`items.reservations[].earlyAccessMaintenance` |  `enum` Indicates the early access maintenance for the reservation. If this field is absent or set to NO_EARLY_ACCESS, the reservation is not enrolled in early access maintenance and the standard notice applies.  
`items.reservations[].resourceMetadata` |  `object` Output only. Contains standard resource metadata for an Allocation resource. It is populated for each instance of the Allocation resource, and includes the `apiVersion` the instance was retrieved through, and its canonical `resourceType` name.  
`items.reservations[].resourceMetadata.resourceType` |  `string` The canonical resource type name in the format of a resource type as defined by [AIP-123](https://google.aip.dev/123). For example, `"compute.googleapis.com/Instance"`.  
`items.reservations[].resourceMetadata.apiVersion` |  `string` The version of the API interface that this resource was retrieved through. For example, `"2025-01-01"` or `"2025-01-01-preview"`.  
`items.warning` |  `object` Informational warning which replaces the list of reservations when the list is empty.  
`items.warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`items.warning.message` |  `string` Output only. A human-readable description of the warning code.  
`items.warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`items.warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`items.warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`nextPageToken` |  `string` Output only. This token allows you to get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
`selfLink` |  `string` Output only. Server-defined URL for this resource.  
`warning` |  `object` Output only. Informational warning message.  
`warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warning.message` |  `string` Output only. A human-readable description of the warning code.  
`warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`unreachables[]` |  `string` Output only. Unreachable resources.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.reservations.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
