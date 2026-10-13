---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/hosts/get/
title: Method: hosts.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:05:28.888935+00:00
---

# Method: hosts.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/hosts/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: hosts.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
  * Authorization scopes
  * Try it!



API Version : 2026-09-01

Retrieves information about the specified host.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/zones/{zone}/{association}/hosts/{host}?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` The project ID for this request.  
`zone` |  `string` The name of the zone for this request, formatted as RFC1035.  
`association` |  `string` The parent resource association for the Host. This field specifies the hierarchical context (e.g., reservation, block, sub-block) when accessing the host. For example, reservations/reservationName, reservations/reservationName/reservationBlocks/reservation_block_name or reservations/reservationName/reservationBlocks/reservation_block_name/reservationSubBlocks/reservation_sub_block_name.  
`host` |  `string` The name of the host, formatted as RFC1035 or a resource ID number.  
  
### Request body

The request body must be empty.

### Response body

Represents a host resource.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "zone": string,
      "selfLink": string,
      "selfLinkWithId": string,
      "aliasLinks": [
        string
      ],
      "description": string,
      "state": enum,
      "status": {
        "physicalTopology": {
          "cluster": string,
          "block": string,
          "subBlock": string,
          "host": string
        },
        "runningInstances": [
          string
        ]
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. The type of resource. Always `compute#host` for hosts.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for this resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. The creation timestamp, formatted as [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text.  
`name` |  `string` Output only. The name of the host.  
`zone` |  `string` Output only. The zone in which the host resides.  
`selfLink` |  `string` Output only. The self link of the host.  
`selfLinkWithId` |  `string` Output only. The self link with id of the host.  
`aliasLinks[]` |  `string` Output only. All aliases for this resource. e.g. projects/123/zones/us-centra1-a/reservation/r1/reservationBlock/b1/hosts/h1  
`description` |  `string` An optional description of this resource.  
`state` |  `enum` Output only. The state of the host.  
`status` |  `object` Output only. The status of the host  
`status.physicalTopology` |  `object` Output only. The physical topology of the reservation sub-block, if present  
`status.physicalTopology.cluster` |  `string` The cluster name of the reservation sub-block.  
`status.physicalTopology.block` |  `string` The unique identifier of the capacity block within the cluster.  
`status.physicalTopology.subBlock` |  `string` The unique identifier of the capacity sub-block within the capacity block.  
`status.physicalTopology.host` |  `string` The unique identifier of the capacity host within the capacity sub-block.  
`status.runningInstances[]` |  `string` Output only. The URIs of the instances currently running on this host.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
