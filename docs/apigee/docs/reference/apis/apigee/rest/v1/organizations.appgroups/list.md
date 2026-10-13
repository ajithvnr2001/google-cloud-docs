---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/list/
title: Method: organizations.appgroups.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:26.965447+00:00
---

# Method: organizations.appgroups.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.appgroups.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists all AppGroups in an organization. A maximum of 1000 AppGroups are returned in the response if PageSize is not specified, or if the PageSize is greater than 1000.

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*}/appgroups`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the Apigee organization. Use the following structure in your request: `organizations/{org}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.appgroups.list`

  
  
### Query parameters

Parameters  
---  
`filter` |  `string` The filter expression to be used to get the list of AppGroups, where filtering can be done on status, channelId or channelUri of the app group. Examples: filter=status=active", filter=channelId=, filter=channelUri=  
`pageSize` |  `integer` Count of AppGroups a single page can have in the response. If unspecified, at most 1000 AppGroups will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` The starting index record for listing the AppGroups.  
  
### Request body

The request body must be empty.

### Response body

ListAppGroupsResponse contains the 0 or more AppGroups, along with the optional page token and the total count of apps.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "appGroups": [
        {
          object ([AppGroup](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups#AppGroup))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`appGroups[]` |  `object (`[AppGroup](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups#AppGroup)`)` List of AppGroups.  
`nextPageToken` |  `string` Token that can be sent as `nextPageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`totalSize` |  `integer` Total count of AppGroups.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
