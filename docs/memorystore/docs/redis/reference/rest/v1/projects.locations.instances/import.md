---
url: https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/import/
title: Method: projects.locations.instances.import \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:48.739433+00:00
---

# Method: projects.locations.instances.import  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/redis/apis)



Send feedback 

#  Method: projects.locations.instances.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * InputConfig
    * JSON representation
  * GcsSource
    * JSON representation
  * Examples
  * Try it!



Import a Redis RDB snapshot file from Cloud Storage into a Redis instance.

Redis may stop serving during this operation. Instance state will be IMPORTING for entire operation. When complete, the instance will contain only data from the imported file.

The returned operation is automatically deleted after a few hours, so there is no need to call operations.delete.

### HTTP request

`POST https://redis.googleapis.com/v1/{name=projects/*/locations/*/instances/*}:import`

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
      "inputConfig": {
        object ([InputConfig](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/import#InputConfig))
      }
    }  
  
Fields  
---  
`inputConfig` |  `object (`[InputConfig](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/import#InputConfig)`)` Required. Specify data to be imported.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## InputConfig

The input content

JSON representation  
---  
      
    
    {
    
      // Union field source can be only one of the following:
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/import#GcsSource))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
Union field `source`. Required. Specify source location of input data `source` can be only one of the following:  
`gcsSource` |  `object (`[GcsSource](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/import#GcsSource)`)` Google Cloud Storage location where input content is located.  
  
## GcsSource

The Cloud Storage location for the input content

JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Fields  
---  
`uri` |  `string` Required. Source data URI. (e.g. 'gs://my_bucket/my_object').  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
