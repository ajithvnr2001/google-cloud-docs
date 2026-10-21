---
url: https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.instances/applyParameters/
title: Method: projects.locations.instances.applyParameters \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:10:48.761861+00:00
---

# Method: projects.locations.instances.applyParameters  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.instances/applyParameters/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/memcached/apis)



Send feedback 

#  Method: projects.locations.instances.applyParameters Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



`instances.applyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance.

### HTTP request

`POST https://memcache.googleapis.com/v1/{name=projects/*/locations/*/instances/*}:applyParameters`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Resource name of the Memcached instance for which parameter group updates should be applied.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "nodeIds": [
        string
      ],
      "applyAll": boolean
    }  
  
Fields  
---  
`nodeIds[]` |  `string` Nodes to which the instance-level parameter group is applied.  
`applyAll` |  `boolean` Whether to apply instance-level parameter group to all nodes. If set to true, users are restricted from specifying individual nodes, and `instances.applyParameters` updates all nodes within the instance.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
