---
url: https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/failover/
title: Method: projects.locations.instances.failover \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:50.164318+00:00
---

# Method: projects.locations.instances.failover  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/failover/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/redis/apis)



Send feedback 

#  Method: projects.locations.instances.failover Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * DataProtectionMode
  * Examples
  * Try it!



Initiates a failover of the primary node to current replica node for a specific STANDARD tier Cloud Memorystore for Redis instance.

### HTTP request

`POST https://redis.googleapis.com/v1beta1/{name=projects/*/locations/*/instances/*}:failover`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Redis instance resource name using the form: `projects/{projectId}/locations/{locationId}/instances/{instanceId}` where `locationId` refers to a GCP region.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dataProtectionMode": enum ([DataProtectionMode](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/failover#DataProtectionMode))
    }  
  
Fields  
---  
`dataProtectionMode` |  `enum (`[DataProtectionMode](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/failover#DataProtectionMode)`)` Optional. Available data protection modes that the user can choose. If it's unspecified, data protection mode will be LIMITED_DATA_LOSS by default.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## DataProtectionMode

Specifies different modes of operation in relation to the data retention.

Enums  
---  
`DATA_PROTECTION_MODE_UNSPECIFIED` | Defaults to LIMITED_DATA_LOSS if a data protection mode is not specified.  
`LIMITED_DATA_LOSS` | Instance failover will be protected with data loss control. More specifically, the failover will only be performed if the current replication offset diff between primary and replica is under a certain threshold.  
`FORCE_DATA_LOSS` | Instance failover will be performed without data loss control.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
