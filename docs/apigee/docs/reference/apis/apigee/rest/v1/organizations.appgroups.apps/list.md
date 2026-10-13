---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps/list/
title: Method: organizations.appgroups.apps.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:28.166184+00:00
---

# Method: organizations.appgroups.apps.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.appgroups.apps.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists all apps created by an AppGroup in an Apigee organization. Optionally, you can request an expanded view of the AppGroup apps.

Lists all AppGroupApps in an AppGroup. A maximum of 1000 AppGroup apps are returned in the response if PageSize is not specified, or if the PageSize is greater than 1000.

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*/appgroups/*}/apps`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the AppGroup. Use the following structure in your request: `organizations/{org}/appgroups/{app_group_name}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.appgroupapps.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum number entries to return. If unspecified, at most 1000 entries will be returned.  
`pageToken` |  `string` Optional. Page token. If provides, must be a valid AppGroup app returned from a previous call that can be used to retrieve the next page.  
  
### Request body

The request body must be empty.

### Response body

Response for [apps.list][AppGroups.ListAppGroupApps]

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "appGroupApps": [
        {
          object ([AppGroupApp](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps#AppGroupApp))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`appGroupApps[]` |  `object (`[AppGroupApp](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps#AppGroupApp)`)` List of AppGroup apps and their credentials.  
`nextPageToken` |  `string` Token that can be sent as `nextPageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
