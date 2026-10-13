---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations/list/
title: Method: projects.locations.list \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:58.715915+00:00
---

# Method: projects.locations.list  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations/list/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the `[ListLocationsRequest.name](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations/list#body.PATH_PARAMETERS.name)` field:

  * **Global locations** : If `name` is empty, the method lists the public locations available to all projects.
  * **Project-specific locations** : If `name` follows the format `projects/{project}`, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.



For gRPC and client library implementations, the resource name is passed as the `name` field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

### HTTP request

`GET https://{endpoint}/v3/{name=projects/*}/locations`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

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
`extraLocationTypes[]` |  `string` Optional. Do not use this field unless explicitly documented otherwise. This is primarily for internal usage.  
  
### Request body

The request body must be empty.

### Response body

The response message for `Locations.ListLocations`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "locations": [
        {
          object ([Location](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations#Location))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`locations[]` |  `object (`[Location](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations#Location)`)` A list of locations that matches the specified filter in the request.  
`nextPageToken` |  `string` The standard List next-page token.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-03 UTC."],[],[]] 
