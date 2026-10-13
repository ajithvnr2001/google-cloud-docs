---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors/list/
title: Method: projects.locations.appConnectors.list \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:08.681503+00:00
---

# Method: projects.locations.appConnectors.list  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Reference ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference)



Send feedback 

#  Method: projects.locations.appConnectors.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists AppConnectors in a given project and location.

### HTTP request

`GET https://beyondcorp.googleapis.com/v1/{parent=projects/*/locations/*}/appConnectors`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the AppConnector location using the form: `projects/{projectId}/locations/{locationId}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `beyondcorp.appConnectors.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the pageSize value, the response may include a partial list and a caller should only rely on response's `[nextPageToken](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors/list#body.ListAppConnectorsResponse.FIELDS.next_page_token)` to determine if there are more instances left to be queried.  
`pageToken` |  `string` Optional. The nextPageToken value returned from a previous ListAppConnectorsRequest, if any.  
`filter` |  `string` Optional. A filter specifying constraints of a list operation.  
`orderBy` |  `string` Optional. Specifies the ordering of results. See [Sorting order](https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.  
  
### Request body

The request body must be empty.

### Response body

Response message for BeyondCorp.ListAppConnectors.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "appConnectors": [
        {
          object ([AppConnector](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors#AppConnector))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`appConnectors[]` |  `object (`[AppConnector](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.appConnectors#AppConnector)`)` A list of BeyondCorp AppConnectors in the project.  
`nextPageToken` |  `string` A token to retrieve the next page of results, or empty if there are no more results in the list.  
`unreachable[]` |  `string` A list of locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-02 UTC."],[],[]] 
