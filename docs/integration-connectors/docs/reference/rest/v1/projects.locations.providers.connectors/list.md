---
url: https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.providers.connectors/list/
title: Method: projects.locations.providers.connectors.list \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:38.912737+00:00
---

# Method: projects.locations.providers.connectors.list  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.providers.connectors/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Reference ](https://docs.cloud.google.com/integration-connectors/docs/reference/rest)



Send feedback 

#  Method: projects.locations.providers.connectors.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists Connectors in a given project and location.

### HTTP request

`GET https://connectors.googleapis.com/v1/{parent=projects/*/locations/*/providers/*}/connectors`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent resource of the connectors, of the form: `projects/*/locations/*/providers/*` Only global location is supported for Connector resource. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `connectors.connectors.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Page size.  
`pageToken` |  `string` Page token.  
`filter` |  `string` Filter string.  
  
### Request body

The request body must be empty.

### Response body

Response message for Connectors.ListConnectors.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "connectors": [
        {
          object ([Connector](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.providers.connectors#Connector))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`connectors[]` |  `object (`[Connector](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.providers.connectors#Connector)`)` A list of connectors.  
`nextPageToken` |  `string` Next page token.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
