---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/advice/capacity/
title: Method: advice.capacity \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:01:42.760099+00:00
---

# Method: advice.capacity  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/advice/capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: advice.capacity Stay organized with collections  Save and categorize content based on your preferences. 

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
      * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`POST https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/advice/capacity?$apiVersion=2026-09-01`

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
        "scheduling": {
          "provisioningModel": enum
        }
      },
      "instanceFlexibilityPolicy": {
        "instanceSelections": {
          string: {
            "machineTypes": [
              string
            ],
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
            ],
            "rank": string
          },
          ...
        }
      },
      "size": integer,
      "distributionPolicy": {
        "zones": [
          {
            "zone": string
          }
        ],
        "targetShape": enum
      }
    }  
  
Fields  
---  
`instanceProperties` |  `object` Instance properties for this request.  
`instanceProperties.scheduling` |  `object` Specifies the scheduling options.  
`instanceProperties.scheduling.provisioningModel` |  `enum` Specifies the provisioning model.  
`instanceFlexibilityPolicy.instanceSelections[].key` |  `string`  
`instanceFlexibilityPolicy.instanceSelections[].value.machineTypes[]` |  `string` Full machine-type names, e.g. "n1-standard-16".  
`instanceFlexibilityPolicy.instanceSelections[].value.guestAccelerators[].acceleratorType` |  `string` Full or partial URL of the accelerator type resource to attach to this instance. For example: `projects/my-project/zones/us-central1-c/acceleratorTypes/nvidia-tesla-p100` If you are creating an instance template, specify only the accelerator name. See [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#introduction) for a full list of accelerator types.  
`instanceFlexibilityPolicy.instanceSelections[].value.guestAccelerators[].acceleratorCount` |  `integer` The number of the guest accelerator cards exposed to this instance.  
`instanceFlexibilityPolicy.instanceSelections[].value.disks[]` |  `object` Local SSDs.  
`instanceFlexibilityPolicy.instanceSelections[].value.disks[].type` |  `enum` Specifies the type of the disk.  
`instanceFlexibilityPolicy.instanceSelections[].value.rank` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Rank when prioritizing the shape flexibilities. The instance selections are considered in the ascending order of the rank. If not set, defaults to 0.  
`size` |  `integer` The number of VM instances to request.  
`distributionPolicy` |  `object` Policy specifying the distribution of instances across zones within the requested region.  
`distributionPolicy.zones[]` |  `object` Zones where advice.capacity Advisor looks for capacity.  
`distributionPolicy.zones[].zone` |  `string` The URL of the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available). It can be a partial or full URL. For example, the following are valid values: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/zones/zone`
  * `projects/project/zones/zone`
  * `zones/zone`

  
`distributionPolicy.targetShape` |  `enum` Target distribution shape. You can specify the following values: `ANY`, `ANY_SINGLE_ZONE`, or `BALANCED`.  
  
### Response body

A response contains scoring recommendations.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "recommendations": [
        {
          "scores": {
            "obtainability": number,
            "estimatedUptime": string
          },
          "shards": [
            {
              "zone": string,
              "machineType": string,
              "instanceCount": integer,
              "provisioningModel": enum
            }
          ]
        }
      ]
    }  
  
Fields  
---  
`recommendations[]` |  `object` Initially the API will provide one recommendation which balances the individual scores according to the service provider's preference.  
`recommendations[].scores` |  `object` Scores for the recommendation.  
`recommendations[].scores.obtainability` |  `number` The obtainability score indicates the likelihood of successfully obtaining (provisioning) the requested number of VMs. The score range is 0.0 through 1.0. Higher is better.  
`recommendations[].scores.estimatedUptime` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The estimated run time of the majority of Spot VMs in the request before preemption. The estimate is best-effort only. It is based on historical data and current conditions.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`recommendations[].shards[]` |  `object` Shards represent blocks of uniform capacity in recommendations.  
`recommendations[].shards[].zone` |  `string` Output only. The zone name for this shard.  
`recommendations[].shards[].machineType` |  `string` The machine type corresponds to the instance selection in the request.  
`recommendations[].shards[].instanceCount` |  `integer` The number of instances.  
`recommendations[].shards[].provisioningModel` |  `enum` The provisioning model that you want to view recommendations for.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.advice.capacity`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
