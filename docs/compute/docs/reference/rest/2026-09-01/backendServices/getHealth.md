---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendServices/getHealth/
title: Method: backendServices.getHealth \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:02:24.094472+00:00
---

# Method: backendServices.getHealth  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendServices/getHealth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: backendServices.getHealth Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Gets the most recent health check results for this BackendService.

Example request body:

{ "group": "/zones/us-east1-b/instanceGroups/lb-backend-example" }

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`POST https://compute.googleapis.com/compute/v1/projects/{project}/global/backendServices/{backendService}/getHealth?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string`  
`backendService` |  `string` Name of the BackendService resource to which the queried instance belongs.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "group": string
    }  
  
Fields  
---  
`group` |  `string` A URI referencing one of the instance groups or network endpoint groups listed in the backend service.  
  
### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "healthStatus": [
        {
          "weight": string,
          "weightError": enum,
          "ipAddress": string,
          "ipv6Address": string,
          "port": integer,
          "instance": string,
          "healthState": enum,
          "ipv6HealthState": enum,
          "annotations": {
            string: string,
            ...
          },
          "forwardingRuleIp": string,
          "forwardingRule": string
        }
      ],
      "annotations": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of resource. Always `compute#backendServiceGroupHealth` for the health of backend services.  
`healthStatus[]` |  `object` Health state of the backend instances or endpoints in requested instance or network endpoint group, determined based on configured health checks.  
`healthStatus[].weight` |  `string`  
`healthStatus[].weightError` |  `enum`  
`healthStatus[].ipAddress` |  `string` For target pool based Network Load Balancing, it indicates the forwarding rule's IP address assigned to this instance. For other types of load balancing, the field indicates VM internal ip.  
`healthStatus[].ipv6Address` |  `string`  
`healthStatus[].port` |  `integer` The named port of the instance group, not necessarily the port that is health-checked.  
`healthStatus[].instance` |  `string` URL of the instance resource.  
`healthStatus[].healthState` |  `enum` Health state of the IPv4 address of the instance.  
`healthStatus[].ipv6HealthState` |  `enum` Health state of the IPv6 address of the instance.  
`healthStatus[].annotations` |  `map (key: string, value: string)` Metadata defined as annotations for network endpoint.  
`healthStatus[].forwardingRuleIp` |  `string` A forwarding rule IP address assigned to this instance.  
`healthStatus[].forwardingRule` |  `string` URL of the forwarding rule associated with the health status of the instance.  
`annotations` |  `map (key: string, value: string)` Metadata defined as annotations on the network endpoint group.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.backendServices.get`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
