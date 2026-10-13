---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/instances/getGuestAttributes/
title: Method: instances.getGuestAttributes \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:58.179249+00:00
---

# Method: instances.getGuestAttributes  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/instances/getGuestAttributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: instances.getGuestAttributes Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Returns the specified guest attributes entry.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instances/{instance}/getGuestAttributes?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`zone` |  `string` The name of the zone for this request.  
`instance` |  `string` Name of the instance scoping this request.  
  
### Query parameters

Parameters  
---  
`variableKey` |  `string` Specifies the key for the guest attributes entry.  
`queryPath` |  `string` Specifies the guest attributes path to be queried.  
  
### Request body

The request body must be empty.

### Response body

A guest attributes entry.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "variableKey": string,
      "variableValue": string,
      "queryPath": string,
      "queryValue": {
        "items": [
          {
            "namespace": string,
            "key": string,
            "value": string
          }
        ]
      },
      "selfLink": string
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#guestAttributes` for guest attributes entry.  
`variableKey` |  `string` The key to search for.  
`variableValue` |  `string` Output only. The value found for the requested key.  
`queryPath` |  `string` The path to be queried. This can be the default namespace ('') or a nested namespace ('<namespace>/') or a specified key ('<namespace>/<key>').  
`queryValue` |  `object` Output only. The value of the requested queried path.  
`queryValue.items[]` |  `object`  
`queryValue.items[].namespace` |  `string` Namespace for the guest attribute entry.  
`queryValue.items[].key` |  `string` Key for the guest attribute entry.  
`queryValue.items[].value` |  `string` Value for the guest attribute entry.  
`selfLink` |  `string` Output only. Server-defined URL for this resource.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.instances.getGuestAttributes`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
