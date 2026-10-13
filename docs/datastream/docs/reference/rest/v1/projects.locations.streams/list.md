---
url: https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams/list/
title: Method: projects.locations.streams.list \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:50.623353+00:00
---

# Method: projects.locations.streams.list  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Reference ](https://docs.cloud.google.com/datastream/docs/reference/rest)



Send feedback 

#  Method: projects.locations.streams.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Examples
  * Try it!



Use this method to list streams in a project and location.

### HTTP request

`GET https://datastream.googleapis.com/v1/{parent}/streams`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent that owns the collection of streams. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `datastream.streams.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum number of streams to return. If unspecified, at most 50 streams will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. Page token received from a previous `streams.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `streams.list` must match the call that provided the page token.  
`filter` |  `string` Optional. Filter request.  
`orderBy` |  `string` Optional. Order by fields for the result.  
  
### Request body

The request body must be empty.

### Response body

Response message for listing streams.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "streams": [
        {
          object ([Stream](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams#Stream))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`streams[]` |  `object (`[Stream](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams#Stream)`)` List of streams  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `datastream.streams.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-26 UTC."],[],[]] 
