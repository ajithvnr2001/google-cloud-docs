---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/advice/capacityHistory/
title: Method: advice.capacityHistory \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:01:43.921395+00:00
---

# Method: advice.capacityHistory  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/advice/capacityHistory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: advice.capacityHistory Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Response body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Gets the capacity history.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`POST https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/advice/capacityHistory?$apiVersion=2026-09-01`

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
      "instanceProperties": {
        "machineType": string,
        "scheduling": {
          "provisioningModel": enum
        },
        "guestAccelerators": [
          {
            "acceleratorType": string,
            "acceleratorCount": integer
          }
        ],
        "disks": [
          {
            "type": enum
          }
        ]
      },
      "locationPolicy": {
        "location": string
      },
      "types": [
        enum
      ]
    }  
  
Fields  
---  
`instanceProperties.machineType` |  `string` The machine type for the VM, such as `n2-standard-4`.  
`instanceProperties.scheduling` |  `object` Specifies the scheduling options.  
`instanceProperties.scheduling.provisioningModel` |  `enum` The provisioning model to get capacity history for. This field must be set to `SPOT`.For more information, see [ Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).  
`instanceProperties.guestAccelerators[].acceleratorType` |  `string` Full or partial URL of the accelerator type resource to attach to this instance. For example: `projects/my-project/zones/us-central1-c/acceleratorTypes/nvidia-tesla-p100` If you are creating an instance template, specify only the accelerator name. See [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#introduction) for a full list of accelerator types.  
`instanceProperties.guestAccelerators[].acceleratorCount` |  `integer` The number of the guest accelerator cards exposed to this instance.  
`instanceProperties.disks[]` |  `object` Local SSDs.  
`instanceProperties.disks[].type` |  `enum` Specifies the type of the disk.  
`locationPolicy` |  `object` Location policy for this request.  
`locationPolicy.location` |  `string` The region or zone to get capacity history for.It can be a partial or full URL. For example, the following are valid values: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/zones/zone`
  * `projects/project/zones/zone`
  * `zones/zone`

This field is optional.  
`types[]` |  `enum` List of history types to get capacity history for.  
  
### Response body

Contains the capacity history.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "machineType": string,
      "location": string,
      "preemptionHistory": [
        {
          "interval": {
            "startTime": string,
            "endTime": string
          },
          "preemptionRate": number
        }
      ],
      "priceHistory": [
        {
          "interval": {
            "startTime": string,
            "endTime": string
          },
          "listPrice": {
            "currencyCode": string,
            "units": string,
            "nanos": integer
          }
        }
      ]
    }  
  
Fields  
---  
`machineType` |  `string` The machine type for which the capacity history is returned.  
`location` |  `string` Output only. The location (region or zone) for which the capacity history is returned. It is returned as a URL - For example, `<https://www.googleapis.com/compute/v1/projects/>project/zones/zone`.  
`preemptionHistory[]` |  `object` The preemption history for the requested machine type and location.  
`preemptionHistory[].interval` |  `object` The time interval for this preemption record.  
`preemptionHistory[].interval.startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Inclusive start of the interval.If specified, a Timestamp matching this interval will have to be the same or after the start.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`preemptionHistory[].interval.endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Exclusive end of the interval.If specified, a Timestamp matching this interval will have to be before the end.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`preemptionHistory[].preemptionRate` |  `number` The preemption rate during the interval, representing the fraction of Spot VMs that were preempted. Range: 0.0 to 1.0. Preemption rate is calculated as `(total preempted Spots) / (total Spots that stopped running)`.  
`priceHistory[]` |  `object` The price history for the requested machine type and location.  
`priceHistory[].interval` |  `object` The time interval for this price record.  
`priceHistory[].interval.startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Inclusive start of the interval.If specified, a Timestamp matching this interval will have to be the same or after the start.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`priceHistory[].interval.endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Exclusive end of the interval.If specified, a Timestamp matching this interval will have to be before the end.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`priceHistory[].listPrice` |  `object` The Spot VM list price during the interval.  
`priceHistory[].listPrice.currencyCode` |  `string` The three-letter currency code defined in ISO 4217.  
`priceHistory[].listPrice.units` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The whole units of the amount. For example if `currencyCode` is `"USD"`, then 1 unit is one US dollar.  
`priceHistory[].listPrice.nanos` |  `integer` Number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If `units` is positive, `nanos` must be positive or zero. If `units` is zero, `nanos` can be positive, zero, or negative. If `units` is negative, `nanos` must be negative or zero. For example $-1.75 is represented as `units`=-1 and `nanos`=-750,000,000.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.advice.capacityHistory`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
