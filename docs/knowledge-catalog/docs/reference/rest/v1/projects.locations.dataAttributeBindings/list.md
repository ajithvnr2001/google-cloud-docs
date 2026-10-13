---
url: https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataAttributeBindings/list/
title: Method: projects.locations.dataAttributeBindings.list \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:20.650896+00:00
---

# Method: projects.locations.dataAttributeBindings.list  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataAttributeBindings/list/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference)



Send feedback 

#  Method: projects.locations.dataAttributeBindings.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



This item is deprecated!

Lists DataAttributeBinding resources in a project and location.

### HTTP request

`GET https://dataplex.googleapis.com/v1/{parent=projects/*/locations/*}/dataAttributeBindings`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the Location: projects/{projectNumber}/locations/{locationId} Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dataplex.dataAttributeBindings.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum number of DataAttributeBindings to return. The service may return fewer than this value. If unspecified, at most 10 DataAttributeBindings will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. Page token received from a previous `dataAttributeBindings.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `dataAttributeBindings.list` must match the call that provided the page token.  
`filter` |  `string` Optional. Filter request. Filter using resource: filter=resource:"resource-name" Filter using attribute: filter=attributes:"attribute-name" Filter using attribute in paths list: filter=paths.attributes:"attribute-name"  
`orderBy` |  `string` Optional. Order by fields for the result.  
  
### Request body

The request body must be empty.

### Response body

List DataAttributeBindings response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dataAttributeBindings": [
        {
          object ([DataAttributeBinding](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataAttributeBindings#DataAttributeBinding))
        }
      ],
      "nextPageToken": string,
      "unreachableLocations": [
        string
      ]
    }  
  
Fields  
---  
`dataAttributeBindings[]` |  `object (`[DataAttributeBinding](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataAttributeBindings#DataAttributeBinding)`)` DataAttributeBindings under the given parent Location.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
`unreachableLocations[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dataplex.read-write`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
