---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apps/list/
title: Method: organizations.apps.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:30.775578+00:00
---

# Method: organizations.apps.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apps/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.apps.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists IDs of apps within an organization that have the specified app status (approved or revoked) or are of the specified app type (developer or company).

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*}/apps`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Resource path of the parent in the following format: `organizations/{org}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.apps.list`

  
  
### Query parameters

Parameters  
---  
`status` |  `string` Optional. Filter by the status of the app. Valid values are `approved` or `revoked`. Defaults to `approved`.  
`apptype` |  `string` Optional. 'apptype' is no longer available. Use a 'filter' instead.  
`includeCred` |  `boolean` Optional. Flag that specifies whether to include credentials in the response.  
`startKey` |  `string` Returns the list of apps starting from the specified app ID.  
`rows` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Maximum number of app IDs to return. Defaults to 1000, which is also the upper limit. To get more than 1000, use pagination with 'pageSize' and 'pageToken' parameters.  
`expand` |  `boolean` Optional. Flag that specifies whether to return an expanded list of apps for the organization. Defaults to `false`.  
`ids` |  `string` Optional. Comma-separated list of app IDs on which to filter.  
`keyStatus` |  `string` Optional. Key status of the app. Valid values include `approved` or `revoked`. Defaults to `approved`.  
`apiProduct` |  `string` API product.  
`pageSize` |  `integer` Optional. Count of apps a single page can have in the response. If unspecified, at most 1000 apps will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. "pageSize" is supported from ver 1.10.0 and above.  
`pageToken` |  `string` Optional. The starting index record for listing the developers. "pageToken" is supported from ver 1.10.0 and above.  
`filter` |  `string` Optional. The filter expression to be used to get the list of apps, where filtering can be done on developerEmail, apiProduct, consumerKey, status, appId, appName, appType and appGroup. Examples: "developerEmail=foo@bar.com", "appType=AppGroup", or "appType=Developer" "filter" is supported from ver 1.10.0 and above.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "app": [
        {
          object ([App](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apps#App))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`app[]` |  `object (`[App](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apps#App)`)`  
`nextPageToken` |  `string` Token that can be sent as `nextPageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`totalSize` |  `integer` Total count of Apps.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
