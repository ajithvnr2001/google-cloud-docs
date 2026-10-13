---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/advice/calendarMode/
title: Method: advice.calendarMode \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:01:41.632306+00:00
---

# Method: advice.calendarMode  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/advice/calendarMode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: advice.calendarMode Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
        * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`POST https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/advice/calendarMode?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region for this request.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "futureResourcesSpecs": {
        string: {
          "locationPolicy": {
            "locations": {
              string: {
                "preference": enum
              },
              ...
            }
          },
          "timeRangeSpec": {
            "startTimeNotEarlierThan": string,
            "startTimeNotLaterThan": string,
            "minDuration": string,
            "maxDuration": string
          },
          "targetResources": {
    
            // The following is a list of mutually exclusive fields. At most one of the
            // fields will be set in a response:
            "specificSkuResources": {
              "machineType": string,
              "localSsdPartitions": [
                {
                  "diskInterface": enum,
                  "diskSizeGb": string
                }
              ],
              "instanceCount": string
            },
            "aggregateResources": {
              "vmFamily": enum,
              "workloadType": enum,
              "acceleratorCount": string
            }
            // End of mutually exclusive fields.
          },
          "deploymentType": enum
        },
        ...
      }
    }  
  
Fields  
---  
`futureResourcesSpecs[]` |  `map (key: string, value: object)` Specification of resources to create in the future. The key of the map is an arbitrary string specified by the caller. Value of the map is a specification of required resources and their constraints. Currently only one value is allowed in this map.  
`futureResourcesSpecs[].locationPolicy` |  `object` Optional location policy allowing to exclude some zone(s) in which the resources must not be created.  
`futureResourcesSpecs[].locationPolicy.locations[]` |  `map (key: string, value: object)` Preferences for specified locations. Keys of the map are locations - zones, in format of 'zones/'. Values are preferences for the zones. If a zone is not specified in this map, it is ALLOWed.  
`futureResourcesSpecs[].locationPolicy.locations[].preference` |  `enum` Preference for this location.  
`futureResourcesSpecs[].timeRangeSpec` |  `object` Specification of a time range in which the resources may be created. The time range specifies start of resource use and planned end of resource use.  
`futureResourcesSpecs[].timeRangeSpec.startTimeNotEarlierThan` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`futureResourcesSpecs[].timeRangeSpec.startTimeNotLaterThan` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`futureResourcesSpecs[].timeRangeSpec.minDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`futureResourcesSpecs[].timeRangeSpec.maxDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`futureResourcesSpecs[].targetResources` |  `object` Specification of the reserved resources.  
`futureResourcesSpecs[].targetResources.specificSkuResources` |  `object`  
`futureResourcesSpecs[].targetResources.specificSkuResources.machineType` |  `string` The machine type to use for instances that will use the reservation. This field only accepts machine type names. e.g. n2-standard-4 and does not accept machine type full or partial url. e.g. projects/my-l7ilb-project/zones/us-central1-a/machineTypes/n2-standard-4. Use for GPU reservations.  
`futureResourcesSpecs[].targetResources.specificSkuResources.localSsdPartitions[]` |  `object` Local SSD partitions. You do not have to include SSD partitions that are built in the machine type.  
`futureResourcesSpecs[].targetResources.specificSkuResources.localSsdPartitions[].diskInterface` |  `enum` Disk interface. Defaults to SCSI.  
`futureResourcesSpecs[].targetResources.specificSkuResources.localSsdPartitions[].diskSizeGb` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The size of the disk in GB.  
`futureResourcesSpecs[].targetResources.specificSkuResources.instanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size of the request, in instance count.  
`futureResourcesSpecs[].targetResources.aggregateResources` |  `object`  
`futureResourcesSpecs[].targetResources.aggregateResources.vmFamily` |  `enum` The VM family that all instances scheduled against this reservation must belong to. Use for TPU reservations.  
`futureResourcesSpecs[].targetResources.aggregateResources.workloadType` |  `enum` Workload type. Use for TPU reservations.  
`futureResourcesSpecs[].targetResources.aggregateResources.acceleratorCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size of the request, in accelerator (chip) count.  
`futureResourcesSpecs[].deploymentType` |  `enum` Indicates if the reservation allocation strategy is static (DENSE) or dynamic (STANDARD). Defaults to DENSE.  
  
### Response body

A response containing the recommended way of creating the specified resources in the future. It contains (will contain) multiple recommendations that can be analyzed by the customer and the best one can be picked.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "recommendations": [
        {
          "recommendationsPerSpec": {
            string: {
              "recommendationId": string,
              "recommendationType": enum,
              "startTime": string,
              "endTime": string,
              "location": string,
              "otherLocations": {
                string: {
                  "status": enum,
                  "details": string
                },
                ...
              }
            },
            ...
          }
        }
      ]
    }  
  
Fields  
---  
`recommendations[]` |  `object` Recommendations where, how and when to create the requested resources in order to maximize their obtainability and minimize cost.  
`recommendations[].recommendationsPerSpec[]` |  `map (key: string, value: object)` Recommendations for every future resource specification passed in CalendarModeAdviceRequest. Keys of the map correspond to keys specified in the request.  
`recommendations[].recommendationsPerSpec[].recommendationId` |  `string` Unique id of the recommendation, a UUID string generated by the API.  
`recommendations[].recommendationsPerSpec[].recommendationType` |  `enum` Type of recommendation. Currently only FUTURE_RESERVATION is supported.  
`recommendations[].recommendationsPerSpec[].startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`recommendations[].recommendationsPerSpec[].endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`recommendations[].recommendationsPerSpec[].location` |  `string` The advised location for resource usage. When a zone, in format 'zones/'. If not set, it means that no location is recommended - see otherLocations for details.  
`recommendations[].recommendationsPerSpec[].otherLocations[]` |  `map (key: string, value: object)` List of locations in the request scope that were not recommended. Keys of the map are zones, in format 'zones/'. The values are status information indicating the recommendation status.  
`recommendations[].recommendationsPerSpec[].otherLocations[].status` |  `enum` Status of recommendation in this location.  
`recommendations[].recommendationsPerSpec[].otherLocations[].details` |  `string` Details (human readable) describing the situation. For example, if status is CONDITION_NOT_MET, then details contain information about the parameters of the time window that did not meet the required conditions.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.advice.calendarMode`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
