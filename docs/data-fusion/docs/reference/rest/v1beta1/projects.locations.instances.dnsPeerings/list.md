---
url: https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings/list/
title: Method: projects.locations.instances.dnsPeerings.list \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:17:10.759012+00:00
---

# Method: projects.locations.instances.dnsPeerings.list  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Reference ](https://docs.cloud.google.com/data-fusion/docs/reference)



Send feedback 

#  Method: projects.locations.instances.dnsPeerings.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists DNS peerings for a given resource.

### HTTP request

`GET https://datafusion.googleapis.com/v1beta1/{parent=projects/*/locations/*/instances/*}/dnsPeerings`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent, which owns this collection of dns peerings. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of dns peerings to return. The service may return fewer than this value. If unspecified, at most 50 dns peerings will be returned. The maximum value is 200; values above 200 will be coerced to 200.  
`pageToken` |  `string` A page token, received from a previous `dnsPeerings.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `dnsPeerings.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response message for list DNS peerings.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dnsPeerings": [
        {
          object ([DnsPeering](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings#DnsPeering))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`dnsPeerings[]` |  `object (`[DnsPeering](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings#DnsPeering)`)` List of dns peering.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-20 UTC."],[],[]] 
