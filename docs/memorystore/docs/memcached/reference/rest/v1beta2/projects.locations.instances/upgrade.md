---
url: https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/upgrade/
title: Method: projects.locations.instances.upgrade \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:10:53.246588+00:00
---

# Method: projects.locations.instances.upgrade  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/upgrade/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/memcached/apis)



Send feedback 

#  Method: projects.locations.instances.upgrade Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Upgrades the Memcache instance to a newer memcached engine version specified in the request.

### HTTP request

`POST https://memcache.googleapis.com/v1beta2/{name=projects/*/locations/*/instances/*}:upgrade`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Memcache instance resource name using the form: `projects/{project}/locations/{location}/instances/{instance}` where `locationId` refers to a GCP region.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "memcacheVersion": enum ([MemcacheVersion](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#MemcacheVersion))
    }  
  
Fields  
---  
`memcacheVersion` |  `enum (`[MemcacheVersion](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances#MemcacheVersion)`)` Required. Specifies the target version of memcached engine to upgrade to.  
  
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
