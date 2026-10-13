---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs/reference/network/rest/v1/projects.locations/list/
title: Method: projects.locations.list \u00a0|\u00a0 Google Distributed Cloud connected, version 1.5.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:07.441498+00:00
---

# Method: projects.locations.list  |  Google Distributed Cloud connected, version 1.5.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs/reference/network/rest/v1/projects.locations/list/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs/apis)



Send feedback 

#  Method: projects.locations.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes
  * Try it!



Lists information about the supported locations for this service.

### HTTP request

`GET https://edgenetwork.googleapis.com/v1/{name=projects/*}/locations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` The resource that owns the locations collection, if applicable.  
  
### Query parameters

Parameters  
---  
`filter` |  `string` A filter to narrow down results to a preferred subset. The filtering language accepts strings like `"displayName=tokyo"`, and is documented in more detail in [AIP-160](https://google.aip.dev/160).  
`pageSize` |  `integer` The maximum number of results to return. If not set, the service selects a default.  
`pageToken` |  `string` A page token received from the `nextPageToken` field in the response. Send that page token to receive the subsequent page.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

The response message for `Locations.ListLocations`.

JSON representation  
---  
      
    
    {
      "locations": [
        {
          object ([Location](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs/reference/network/rest/v1/projects.locations#Location))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`locations[]` |  `object (`[Location](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs/reference/network/rest/v1/projects.locations#Location)`)` A list of locations that matches the specified filter in the request.  
`nextPageToken` |  `string` The standard List next-page token.  
  
### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
