---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/reservations/list/
title: Method: reservations.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:54.124559+00:00
---

# Method: reservations.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-10-01-preview/reservations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: reservations.list Stay organized with collections  Save and categorize content based on your preferences. 

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
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-10-01-preview

A list of all the reservations that have been configured for the specified project in specified zone.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/zones/{zone}/reservations?$apiVersion=2026-10-01-preview`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`zone` |  `string` Name of the zone for this request.  
  
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
      "selfLink": string
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of resource.Always `compute#reservationsList` for listsof reservations  
`id` |  `string` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items[]` |  `object` Output only. A list of Allocation resources.  
`items[].specificReservation` |  `object` Reservation for instances with specific machine shapes.  
`items[].specificReservation.instanceProperties` |  `object` The instance properties for the reservation.  
`items[].specificReservation.instanceProperties.machineType` |  `string` Specifies type of machine (name only) which has fixed number of vCPUs and fixed amount of memory. This also includes specifying custom machine type following custom-NUMBER_OF_CPUS-AMOUNT_OF_MEMORY pattern.  
`items[].specificReservation.instanceProperties.guestAccelerators[]` |  `object` Specifies accelerator type and count.  
`items[].specificReservation.instanceProperties.guestAccelerators[].acceleratorType` |  `string` Full or partial URL of the accelerator type resource to attach to this instance. For example: `projects/my-project/zones/us-central1-c/acceleratorTypes/nvidia-tesla-p100` If you are creating an instance template, specify only the accelerator name. See [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#introduction) for a full list of accelerator types.  
`items[].specificReservation.instanceProperties.guestAccelerators[].acceleratorCount` |  `integer` The number of the guest accelerator cards exposed to this instance.  
`items[].specificReservation.instanceProperties.minCpuPlatform` |  `string` Minimum cpu platform the reservation.  
`items[].specificReservation.instanceProperties.localSsds[]` |  `object` Specifies amount of local ssd to reserve with each instance. The type of disk is local-ssd.  
`items[].specificReservation.instanceProperties.localSsds[].diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Specifies the size of the disk in base-2 GB.  
`items[].specificReservation.instanceProperties.localSsds[].interface` |  `enum` Specifies the disk interface to use for attaching this disk, which is either `SCSI` or `NVME`. The default is `SCSI`. For performance characteristics of SCSI over NVMe, see [Local SSD performance](https://docs.cloud.google.com/compute/docs/disks#localssds).  
`items[].specificReservation.instanceProperties.locationHint` |  `string` An opaque location hint used to place the allocation close to other resources. This field is for use by internal tools that use the public API.  
`items[].specificReservation.count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Specifies the number of resources that are allocated.  
`items[].specificReservation.inUseCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Indicates how many instances are in use.  
`items[].specificReservation.assuredCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Indicates how many instances are actually usable currently.  
`items[].specificReservation.sourceInstanceTemplate` |  `string` Specifies the instance template to create the reservation. If you use this field, you must exclude the `instanceProperties` field.This field is optional, and it can be a full or partial URL. For example, the following are all valid URLs to an instance template: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/global/instanceTemplates/instanceTemplate`
  * `projects/project/global/instanceTemplates/instanceTemplate`
  * `global/instanceTemplates/instanceTemplate`

  
`items[].aggregateReservation` |  `object` Reservation for aggregated resources, providing shape flexibility.  
`items[].aggregateReservation.vmFamily` |  `enum` The VM family that all instances scheduled against this reservation must belong to.  
`items[].aggregateReservation.reservedResources[]` |  `object` reservations.list of reserved resources (CPUs, memory, accelerators).  
`items[].aggregateReservation.reservedResources[].accelerator` |  `object` Properties of accelerator resources in this reservation.  
`items[].aggregateReservation.reservedResources[].accelerator.acceleratorCount` |  `integer` Number of accelerators of specified type.  
`items[].aggregateReservation.reservedResources[].accelerator.acceleratorType` |  `string` Full or partial URL to accelerator type. e.g. "projects/{PROJECT}/zones/{ZONE}/acceleratorTypes/ct4l"  
`items[].aggregateReservation.inUseResources[]` |  `object` Output only. reservations.list of resources currently in use.  
`items[].aggregateReservation.inUseResources[].accelerator` |  `object` Properties of accelerator resources in this reservation.  
`items[].aggregateReservation.inUseResources[].accelerator.acceleratorCount` |  `integer` Number of accelerators of specified type.  
`items[].aggregateReservation.inUseResources[].accelerator.acceleratorType` |  `string` Full or partial URL to accelerator type. e.g. "projects/{PROJECT}/zones/{ZONE}/acceleratorTypes/ct4l"  
`items[].aggregateReservation.workloadType` |  `enum` The workload type of the instances that will target this reservation.  
`items[].deleteAtTime` |  `string` Absolute time in future when the reservation will be auto-deleted by Compute Engine. Timestamp is represented in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].deleteAfterDuration` |  `object` Duration time relative to reservation creation when Compute Engine will automatically delete this resource.  
`items[].deleteAfterDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`items[].deleteAfterDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`items[].kind` |  `string` Output only. Type of the resource. Always `compute#reservations` for reservations.  
`items[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].selfLink` |  `string` Output only. Server-defined fully-qualified URL for this resource.  
`items[].zone` |  `string` Zone in which the reservation resides. A zone must be provided if the reservation is created within a commitment.  
`items[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`items[].name` |  `string` The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items[].commitment` |  `string` Output only. Full or partial URL to a parent commitment. This field displays for reservations that are tied to a commitment.  
`items[].linkedCommitments[]` |  `string` Output only. Full or partial URL to parent commitments. This field displays for reservations that are tied to multiple commitments.  
`items[].specificReservationRequired` |  `boolean` Indicates whether the reservation can be consumed by VMs with affinity for "any" reservation. If the field is set, then only VMs that target the reservation by name can consume from this reservation.  
`items[].status` |  `enum` Output only. The status of the reservation. 

  * `CREATING`: Reservation resources are being allocated.
  * `READY`: Reservation resources have been allocated, and the reservation is ready for use.
  * `DELETING`: Reservation deletion is in progress.
  * `UPDATING`: Reservation update is in progress.

  
`items[].shareSettings` |  `object` Specify share-settings to create a shared reservation. This property is optional. For more information about the syntax and options for this field and its subfields, see the guide for [creating a shared reservation.](https://cloud.google.com/compute/docs/instances/reservations-shared#creating_a_shared_reservation)  
`items[].shareSettings.shareType` |  `enum` Type of sharing for this shared-reservation  
`items[].shareSettings.projectMap[]` |  `map (key: string, value: object)` A map of project id and project config. This is only valid when shareType's value is SPECIFIC_PROJECTS.  
`items[].shareSettings.projectMap[].projectId` |  `string` The project ID, should be same as the key of this project config in the parent map.  
`items[].satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`items[].resourcePolicies` |  `map (key: string, value: string)` Resource policies to be added to this reservation. The key is defined by user, and the value is resource policy url. This is to define placement policy with reservation.  
`items[].resourceStatus` |  `object` Output only. Status information for Reservation resource.  
`items[].resourceStatus.specificSkuAllocation` |  `object` Allocation Properties of this reservation.  
`items[].resourceStatus.specificSkuAllocation.sourceInstanceTemplateId` |  `string` ID of the instance template used to populate reservation properties.  
`items[].resourceStatus.specificSkuAllocation.utilizations` |  `map (key: string, value: string ([int64](https://developers.google.com/discovery/v1/type-format) format))` Per service utilization breakdown. The Key is the Google Cloud managed service name.  
`items[].resourceStatus.reservationMaintenance` |  `object` Maintenance information for this reservation  
`items[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance` |  `object` Maintenance information on this group of VMs.  
`items[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.type` |  `enum` Defines the type of maintenance.  
`items[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.canReschedule` |  `boolean` Indicates if the maintenance can be customer triggered.  
`items[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.windowStartTime` |  `string` The current start time of the maintenance window. This timestamp value is in RFC3339 text format.  
`items[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.windowEndTime` |  `string` The time by which the maintenance disruption will be completed. This timestamp value is in RFC3339 text format.  
`items[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.latestWindowStartTime` |  `string` The latest time for the planned maintenance window to start. This timestamp value is in RFC3339 text format.  
`items[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.maintenanceStatus` |  `enum`  
`items[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.maintenanceOnShutdown` |  `boolean` Indicates whether the UpcomingMaintenance will be triggered on VM shutdown.  
`items[].resourceStatus.reservationMaintenance.upcomingGroupMaintenance.maintenanceReasons[]` |  `enum` The reasons for the maintenance. Only valid for vms.  
`items[].resourceStatus.reservationMaintenance.maintenanceOngoingCount` |  `integer` Progress for ongoing maintenance for this group of VMs/hosts. Describes number of hosts in the block that have ongoing maintenance.  
`items[].resourceStatus.reservationMaintenance.maintenancePendingCount` |  `integer` Progress for ongoing maintenance for this group of VMs/hosts. Describes number of hosts in the block that have pending maintenance.  
`items[].resourceStatus.reservationMaintenance.schedulingType` |  `enum` The type of maintenance for the reservation.  
`items[].resourceStatus.reservationMaintenance.subblockInfraMaintenanceOngoingCount` |  `integer` Describes number of subblock Infrastructure that has ongoing maintenance. Here, Subblock Infrastructure Maintenance pertains to upstream hardware contained in the Subblock that is necessary for a VM Family(e.g. NVLink Domains). Not all VM Families will support this field.  
`items[].resourceStatus.reservationMaintenance.subblockInfraMaintenancePendingCount` |  `integer` Describes number of subblock Infrastructure that has pending maintenance. Here, Subblock Infrastructure Maintenance pertains to upstream hardware contained in the Subblock that is necessary for a VM Family (e.g. NVLink Domains). Not all VM Families will support this field.  
`items[].resourceStatus.reservationMaintenance.instanceMaintenanceOngoingCount` |  `integer` Describes number of instances that have ongoing maintenance.  
`items[].resourceStatus.reservationMaintenance.instanceMaintenancePendingCount` |  `integer` Describes number of instances that have pending maintenance.  
`items[].resourceStatus.reservationBlockCount` |  `integer` The number of reservation blocks associated with this reservation.  
`items[].resourceStatus.healthInfo` |  `object` Output only. Health information for the reservation.  
`items[].resourceStatus.healthInfo.healthStatus` |  `enum` The health status of the reservation.  
`items[].resourceStatus.healthInfo.healthyBlockCount` |  `integer` The number of reservation blocks that are healthy.  
`items[].resourceStatus.healthInfo.degradedBlockCount` |  `integer` The number of reservation blocks that are degraded.  
`items[].reservationSharingPolicy` |  `object` Specify the reservation sharing policy. If unspecified, the reservation will not be shared with Google Cloud managed services.  
`items[].reservationSharingPolicy.serviceShareType` |  `enum` Sharing config for all Google Cloud services.  
`items[].deploymentType` |  `enum` Specifies the deployment strategy for this reservation.  
`items[].advancedDeploymentControl` |  `object` Advanced control for cluster management, applicable only to DENSE deployment type reservations.  
`items[].advancedDeploymentControl.reservationOperationalMode` |  `enum` Indicates chosen reservation operational mode for the reservation.  
`items[].enableEmergentMaintenance` |  `boolean` Indicates whether Compute Engine allows unplanned maintenance for your VMs; for example, to fix hardware errors.  
`items[].protectionTier` |  `enum` Protection tier for the workload which specifies the workload expectations in the event of infrastructure failures at data center (e.g. power and/or cooling failures).  
`items[].schedulingType` |  `enum` The type of maintenance for the reservation.  
`items[].params` |  `object` Input only. Additional params passed with the request, but not persisted as part of resource payload.  
`items[].params.resourceManagerTags` |  `map (key: string, value: string)` Input only. Resource manager tags to be bound to the reservation. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). Keys and values can be either in numeric format, such as `tagKeys/{tag_key_id}` and `tagValues/{tag_value_id}` or in namespaced format such as `{org_id|projectId}/{tag_key_short_name}` and `{tag_value_short_name}`. The field is ignored (both PUT & PATCH) when empty.  
`items[].confidentialComputeType` |  `enum`  
`items[].earlyAccessMaintenance` |  `enum` Indicates the early access maintenance for the reservation. If this field is absent or set to NO_EARLY_ACCESS, the reservation is not enrolled in early access maintenance and the standard notice applies.  
`items[].resourceMetadata` |  `object` Output only. Contains standard resource metadata for an Allocation resource. It is populated for each instance of the Allocation resource, and includes the `apiVersion` the instance was retrieved through, and its canonical `resourceType` name.  
`items[].resourceMetadata.resourceType` |  `string` The canonical resource type name in the format of a resource type as defined by [AIP-123](https://google.aip.dev/123). For example, `"compute.googleapis.com/Instance"`.  
`items[].resourceMetadata.apiVersion` |  `string` The version of the API interface that this resource was retrieved through. For example, `"2025-01-01"` or `"2025-01-01-preview"`.  
`nextPageToken` |  `string` Output only. This token allows you to get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
`warning` |  `object` Output only. Informational warning message.  
`warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warning.message` |  `string` Output only. A human-readable description of the warning code.  
`warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`selfLink` |  `string` Output only. Server-defined URL for this resource.  
  
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
