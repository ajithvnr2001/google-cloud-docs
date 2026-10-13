---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/list/
title: Method: organizations.developers.apps.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:35.782794+00:00
---

# Method: organizations.developers.apps.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.developers.apps.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists all apps created by a developer in an Apigee organization. Optionally, you can request an expanded view of the developer apps.

A maximum of 100 developer apps are returned per API call. You can paginate the list of deveoper apps returned using the `startKey` and `count` query parameters.

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*/developers/*}/apps`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the developer. Use the following structure in your request: `organizations/{org}/developers/{developerEmail}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.developerapps.list`

  
  
### Query parameters

Parameters  
---  
`expand` |  `boolean` Optional. Specifies whether to expand the results. Set to `true` to expand the results. This query parameter is not valid if you use the `count` or `startKey` query parameters.  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of developer apps to return in the API call. Use with the `startKey` parameter to provide more targeted filtering. The limit is 1000.  
`startKey` |  `string` **Note** : Must be used in conjunction with the `count` parameter.Name of the developer app from which to start displaying the list of developer apps. For example, if you're returning 50 developer apps at a time (using the `count` query parameter), you can view developer apps 50-99 by entering the name of the 50th developer app. The developer app name is case sensitive.  
`shallowExpand` |  `boolean` Optional. Specifies whether to expand the results in shallow mode. Set to `true` to expand the results in shallow mode.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "app": [
        {
          object ([DeveloperApp](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps#DeveloperApp))
        }
      ]
    }  
  
Fields  
---  
`app[]` |  `object (`[DeveloperApp](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps#DeveloperApp)`)` List of developer apps and their credentials.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
