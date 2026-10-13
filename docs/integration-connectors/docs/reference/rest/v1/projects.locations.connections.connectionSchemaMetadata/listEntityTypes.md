---
url: https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections.connectionSchemaMetadata/listEntityTypes/
title: Method: projects.locations.connections.connectionSchemaMetadata.listEntityTypes \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:50:57.100410+00:00
---

# Method: projects.locations.connections.connectionSchemaMetadata.listEntityTypes  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections.connectionSchemaMetadata/listEntityTypes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Reference ](https://docs.cloud.google.com/integration-connectors/docs/reference/rest)



Send feedback 

#  Method: projects.locations.connections.connectionSchemaMetadata.listEntityTypes Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * View
  * Try it!



List entity types.

### HTTP request

`GET https://connectors.googleapis.com/v1/{name=projects/*/locations/*/connections/*/connectionSchemaMetadata}:listEntityTypes`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Resource name format: projects/{project}/locations/{location}/connections/{connection}/connectionSchemaMetadata Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `connectors.connections.getConnectionSchemaMetadata`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Page size. If unspecified, at most 50 entity types will be returned.  
`pageToken` |  `string` Page token.  
`filter` |  `string` Required. Filter Wildcards are not supported in the filter currently.  
`view` |  `enum (`[View](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections.connectionSchemaMetadata/listEntityTypes#View)`)` Specifies which fields are returned in response. Defaults to BASIC view.  
  
### Request body

The request body must be empty.

### Response body

Response message for connectionSchemaMetadata.listEntityTypes API

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "entityTypes": [
        {
          object ([RuntimeEntitySchema](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/RuntimeEntitySchema))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`entityTypes[]` |  `object (`[RuntimeEntitySchema](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/RuntimeEntitySchema)`)` list of entity types  
`nextPageToken` |  `string` token for next page  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## View

View: Basic is the only supported view for now

Enums  
---  
`VIEW_UNSPECIFIED` |   
`BASIC` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
