---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.connectivityTests/list/
title: Method: projects.locations.global.connectivityTests.list \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:37.931492+00:00
---

# Method: projects.locations.global.connectivityTests.list  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.connectivityTests/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  Method: projects.locations.global.connectivityTests.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists all Connectivity Tests owned by a project.

### HTTP request

`GET https://networkmanagement.googleapis.com/v1beta1/{parent=projects/*/locations/global}/connectivityTests`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource of the Connectivity Tests: `projects/{projectId}/locations/global` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `networkmanagement.connectivitytests.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Number of `ConnectivityTests` to return.  
`pageToken` |  `string` Page token from an earlier query, as returned in `nextPageToken`.  
`filter` |  `string` Lists the `ConnectivityTests` that match the filter expression. A filter expression filters the resources listed in the response. The expression must be of the form `<field> <operator> <value>` where operators: `<`, `>`, `<=`, `>=`, `!=`, `=`, `:` are supported (colon `:` represents a HAS operator which is roughly synonymous with equality).  can refer to a proto or JSON field, or a synthetic field. Field names can be camelCase or snake_case.Examples: - Filter by name: name = "projects/proj-1/locations/global/connectivityTests/test-1

  * Filter by labels:
  * Resources that have a key called `foo` labels.foo:*
  * Resources that have a key called `foo` whose value is `bar` labels.foo = bar

  
`orderBy` |  `string` Field to use to sort the list.  
  
### Request body

The request body must be empty.

### Response body

Response for the `connectivityTests.list` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "resources": [
        {
          object ([ConnectivityTest](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.connectivityTests#ConnectivityTest))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`resources[]` |  `object (`[ConnectivityTest](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/projects.locations.global.connectivityTests#ConnectivityTest)`)` List of Connectivity Tests.  
`nextPageToken` |  `string` Page token to fetch the next set of Connectivity Tests.  
`unreachable[]` |  `string` Locations that could not be reached (when querying all locations with `-`).  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-13 UTC."],[],[]] 
