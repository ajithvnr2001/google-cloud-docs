---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/targetPools/get/
title: Method: targetPools.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:46.255652+00:00
---

# Method: targetPools.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/targetPools/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: targetPools.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Returns the specified target pool.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/targetPools/{targetPool}?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region scoping this request.  
`targetPool` |  `string` Name of the TargetPool resource to return.  
  
### Request body

The request body must be empty.

### Response body

Represents a Target Pool resource.

Target pools are used with external passthrough Network Load Balancers. A target pool references member instances, an associated legacy HttpHealthCheck resource, and, optionally, a backup target pool. For more information, read [Using target pools](https://docs.cloud.google.com/load-balancing/docs/target-pools).

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "region": string,
      "healthChecks": [
        string
      ],
      "instances": [
        string
      ],
      "sessionAffinity": enum,
      "failoverRatio": number,
      "backupPool": string,
      "selfLink": string,
      "securityPolicy": string
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#targetPool` for target pools.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`region` |  `string` Output only. URL of the region where the target pool resides.  
`healthChecks[]` |  `string` The URL of the HttpHealthCheck resource. A member instance in this pool is considered healthy if and only if the health checks pass. Only legacy HttpHealthChecks are supported. Only one health check may be specified.  
`instances[]` |  `string` A list of resource URLs to the virtual machine instances serving this pool. They must live in zones contained in the same region as this pool.  
`sessionAffinity` |  `enum` Session affinity option, must be one of the following values:   
`NONE`: Connections from the same client IP may go to any instance in the pool.   
`CLIENT_IP`: Connections from the same client IP will go to the same instance in the pool while that instance remains healthy.   
`CLIENT_IP_PROTO`: Connections from the same client IP with the same IP protocol will go to the same instance in the pool while that instance remains healthy.  
`failoverRatio` |  `number` This field is applicable only when the containing target pool is serving a forwarding rule as the primary pool (i.e., not as a backup pool to some other target pool). The value of the field must be in [0, 1].If set, `backupPool` must also be set. They together define the fallback behavior of the primary target pool: if the ratio of the healthy instances in the primary pool is at or below this number, traffic arriving at the load-balanced IP will be directed to the backup pool.In case where `failoverRatio` is not set or all the instances in the backup pool are unhealthy, the traffic will be directed back to the primary pool in the "force" mode, where traffic will be spread to the healthy instances with the best effort, or to all instances when no instance is healthy.  
`backupPool` |  `string` The server-defined URL for the resource. This field is applicable only when the containing target pool is serving a forwarding rule as the primary pool, and its `failoverRatio` field is properly set to a value between [0, 1].`backupPool` and `failoverRatio` together define the fallback behavior of the primary target pool: if the ratio of the healthy instances in the primary pool is at or below `failoverRatio`, traffic arriving at the load-balanced IP will be directed to the backup pool.In case where `failoverRatio` and `backupPool` are not set, or all the instances in the backup pool are unhealthy, the traffic will be directed back to the primary pool in the "force" mode, where traffic will be spread to the healthy instances with the best effort, or to all instances when no instance is healthy.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`securityPolicy` |  `string` Output only. The resource URL for the security policy associated with this target pool.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.targetPools.get`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
