---
url: https://docs.cloud.google.com/compute/docs/reference/rest/beta/machineTypes/
title: REST Resource: machineTypes \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:38.926653+00:00
---

# REST Resource: machineTypes  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/beta/machineTypes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: machineTypes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MachineType
    * JSON representation
      * JSON representation
  * Methods



## Resource: MachineType

Represents a Machine Type resource.

You can use specific machine types for your VM instances based on performance and pricing requirements. For more information, read [Machine Types](https://docs.cloud.google.com/compute/docs/machine-types).

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "guestCpus": integer,
      "memoryMb": integer,
      "maximumPersistentDisks": integer,
      "maximumPersistentDisksSizeGb": string,
      "deprecated": {
        "state": enum,
        "replacement": string,
        "deprecated": string,
        "obsolete": string,
        "deleted": string,
        "stateOverride": {
          "locationRolloutPolicies": {
            string: string,
            ...
          },
          "defaultRolloutTime": string
        }
      },
      "zone": string,
      "selfLink": string,
      "isSharedCpu": boolean,
      "accelerators": [
        {
          "guestAcceleratorType": string,
          "guestAcceleratorCount": integer
        }
      ],
      "architecture": enum,
      "bundledLocalSsds": {
        "partitionCount": integer,
        "defaultInterface": string
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. The type of the resource. Always `compute#machineType` for machine types.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Output only. Name of the resource.  
`description` |  `string` Output only. An optional textual description of the resource.  
`guestCpus` |  `integer` Output only. The number of virtual CPUs that are available to the instance.  
`memoryMb` |  `integer` Output only. The amount of physical memory available to the instance, defined in MB.  
`maximumPersistentDisks` |  `integer` Output only. Maximum persistent disks allowed.  
`maximumPersistentDisksSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Maximum total persistent disks size (GB) allowed.  
`deprecated` |  `object` Output only. The deprecation status associated with this machine type. Only applicable if the machine type is unavailable.  
`deprecated.state` |  `enum` The deprecation state of this resource. This can be `ACTIVE`, `DEPRECATED`, `OBSOLETE`, or `DELETED`. Operations which communicate the end of life date for an image, can use `ACTIVE`. Operations which create a new resource using a `DEPRECATED` resource will return successfully, but with a warning indicating the deprecated resource and recommending its replacement. Operations which use `OBSOLETE` or `DELETED` resources will be rejected and result in an error.  
`deprecated.replacement` |  `string` The URL of the suggested replacement for a deprecated resource. The suggested replacement resource must be the same kind of resource as the deprecated resource.  
`deprecated.deprecated` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `DEPRECATED`. This is only informational and the status will not change unless the client explicitly changes it.  
`deprecated.obsolete` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `OBSOLETE`. This is only informational and the status will not change unless the client explicitly changes it.  
`deprecated.deleted` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the state of this resource is intended to change to `DELETED`. This is only informational and the status will not change unless the client explicitly changes it.  
`deprecated.stateOverride` |  `object` The rollout policy for this deprecation. This policy is only enforced by image family views. The rollout policy restricts the zones where the associated resource is considered in a deprecated state. When the rollout policy does not include the user specified zone, or if the zone is rolled out, the associated resource is considered in a deprecated state.The rollout policy for this deprecation is read-only, except for allowlisted users. This field might not be configured. To view the latest non-deprecated image in a specific zone, use the `imageFamilyViews.get` method.  
`deprecated.stateOverride.locationRolloutPolicies` |  `map (key: string, value: string)` Location based rollout policies to apply to the resource.Currently only zone names are supported and must be represented as valid URLs, like: zones/us-central1-a.The value expects an [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the update is considered rolled out to the specified location.  
`deprecated.stateOverride.defaultRolloutTime` |  `string` An optional [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) timestamp on or after which the update is considered rolled out to any zone that is not explicitly stated.  
`zone` |  `string` Output only. The name of the zone where the machine type resides, such as us-central1-a.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`isSharedCpu` |  `boolean` Output only. Whether this machine type has a shared CPU. See [Shared-core machine types](https://docs.cloud.google.com/compute/docs/machine-types#sharedcore) for more information.  
`accelerators[]` |  `object` Output only. A list of accelerator configurations assigned to this machine type.  
`accelerators[].guestAcceleratorType` |  `string` The accelerator type resource name, not a full URL, e.g. `nvidia-tesla-t4`.  
`accelerators[].guestAcceleratorCount` |  `integer` Number of accelerator cards exposed to the guest.  
`architecture` |  `enum` Output only. The architecture of the machine type.  
`bundledLocalSsds` |  `object` Output only. The configuration of bundled local SSD for the machine type.  
`bundledLocalSsds.partitionCount` |  `integer` The number of partitions.  
`bundledLocalSsds.defaultInterface` |  `string` The default disk interface if the interface is not specified.  
  
## Methods  
  
---  
  
### `[aggregatedList](https://docs.cloud.google.com/compute/docs/reference/rest/beta/machineTypes/aggregatedList)`

|  Retrieves an aggregated list of machine types.  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/beta/machineTypes/get)`

|  Returns the specified machine type.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/beta/machineTypes/list)`

|  Retrieves a list of machine types available to the specified project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
