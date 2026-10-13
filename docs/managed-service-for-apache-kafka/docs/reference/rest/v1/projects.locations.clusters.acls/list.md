---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.clusters.acls/list/
title: Method: projects.locations.clusters.acls.list \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:39.513373+00:00
---

# Method: projects.locations.clusters.acls.list  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.clusters.acls/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Reference ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/apis)



Send feedback 

#  Method: projects.locations.clusters.acls.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the acls in a given cluster.

### HTTP request

`GET https://managedkafka.googleapis.com/v1/{parent=projects/*/locations/*/clusters/*}/acls`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent cluster whose acls are to be listed. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of acls to return. The service may return fewer than this value. If unset or zero, all acls for the parent is returned.  
`pageToken` |  `string` Optional. A page token, received from a previous `acls.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `acls.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response for acls.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "acls": [
        {
          object ([Acl](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.clusters.acls#Acl))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`acls[]` |  `object (`[Acl](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.clusters.acls#Acl)`)` The list of acls in the requested parent. The order of the acls is unspecified.  
`nextPageToken` |  `string` A token that can be sent as `pageToken` to retrieve the next page of results. If this field is omitted, there are no more results.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-13 UTC."],[],[]] 
