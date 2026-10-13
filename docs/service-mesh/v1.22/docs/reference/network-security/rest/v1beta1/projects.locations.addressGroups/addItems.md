---
url: https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/projects.locations.addressGroups/addItems/
title: Method: projects.locations.addressGroups.addItems \u00a0|\u00a0 Cloud Service Mesh v1.22 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:02.161166+00:00
---

# Method: projects.locations.addressGroups.addItems  |  Cloud Service Mesh v1.22  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/projects.locations.addressGroups/addItems/

You are viewing archived v1.22 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.22 ](https://docs.cloud.google.com/service-mesh/v1.22/docs)



Send feedback 

#  Method: projects.locations.addressGroups.addItems Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes



Adds items to an address group.

### HTTP request

`POST https://networksecurity.googleapis.com/v1beta1/{addressGroup=projects/*/locations/*/addressGroups/*}:addItems`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`addressGroup` |  `string` Required. A name of the AddressGroup to add items to. Must be in the format `projects|organization/*/locations/{location}/addressGroups/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `addressGroup`:

  * `networksecurity.addressGroups.update`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "items": [
        string
      ],
      "requestId": string
    }  
  
Fields  
---  
`items[]` |  `string` Required. List of items to add.  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/service-mesh/v1.22/docs/reference/network-security/rest/v1beta1/organizations.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-18 UTC."],[],[]] 
