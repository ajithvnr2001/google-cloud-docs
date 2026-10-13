---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/list/
title: Method: projects.locations.serviceLbPolicies.list \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:30.343681+00:00
---

# Method: projects.locations.serviceLbPolicies.list  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/list/

You are viewing v1.28 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.28/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)



Send feedback 

#  Method: projects.locations.serviceLbPolicies.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists ServiceLbPolicies in a given project and location.

### HTTP request

`GET https://networkservices.googleapis.com/v1/{parent=projects/*/locations/*}/serviceLbPolicies`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project and location from which the ServiceLbPolicies should be listed, specified in the format `projects/{project}/locations/{location}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `networkservices.serviceLbPolicies.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Maximum number of ServiceLbPolicies to return per call.  
`pageToken` |  `string` The value returned by the last `ListServiceLbPoliciesResponse` Indicates that this is a continuation of a prior `ListRouters` call, and that the system should return the next page of data.  
  
### Request body

The request body must be empty.

### Response body

Response returned by the serviceLbPolicies.list method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "serviceLbPolicies": [
        {
          object ([ServiceLbPolicy](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies#ServiceLbPolicy))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`serviceLbPolicies[]` |  `object (`[ServiceLbPolicy](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies#ServiceLbPolicy)`)` List of ServiceLbPolicy resources.  
`nextPageToken` |  `string` If there might be more results than those appearing in this response, then `nextPageToken` is included. To get the next set of results, call this method again using the value of `nextPageToken` as `pageToken`.  
`unreachable[]` |  `string` Unreachable resources. Populated when the request attempts to list all resources across all supported locations, while some locations are temporarily unavailable.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-28 UTC."],[],[]] 
