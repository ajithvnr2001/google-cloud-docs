---
url: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryIssues/
title: Method: queryIssues \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:28.427863+00:00
---

# Method: queryIssues  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryIssues/

The Database Center REST and RPC APIs are in [Preview](https://docs.cloud.google.com/products#product-launch-stages). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  Method: queryIssues Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * SignalProductsFilters
    * JSON representation
  * DatabaseResourceIssue
    * JSON representation
  * Try it!



v1beta.queryIssues provides a list of issues and recommendations that a user has access to and that are within the requested scope.

### HTTP request

`POST https://databasecenter.googleapis.com/v1beta:queryIssues`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "parent": string,
      "filter": string,
      "signalProductsFilters": [
        {
          object ([SignalProductsFilters](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryIssues#SignalProductsFilters))
        }
      ],
      "orderBy": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. Parent can be a project, a folder, or an organization. The list is limited to the one attached to resources within the `scope` that a user has access to.The allowed values are:

  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")

  
`filter` |  `string` Optional. Supported fields are: 'product', `location`, `issueSeverity`, 'tags', 'labels',  
`signalProductsFilters[]` |  `object (`[SignalProductsFilters](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryIssues#SignalProductsFilters)`)` Optional. Filters based on signal and product. The filter list will be ORed across pairs and ANDed within a signal and products pair.  
`orderBy` |  `string` Optional. Following fields are sortable: SignalType Product Location IssueSeverityThe default order is ascending. Add "DESC" after the field name to indicate descending order. Add "ASC" after the field name to indicate ascending order. It only supports a single field at a time.  
`pageSize` |  `integer` Optional. If unspecified, at most 50 issues will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `v1beta.queryIssues` call. Provide this to retrieve the subsequent page. All parameters except page size should match the parameters used in the call that provided the page token.  
  
### Response body

QueryIssuesResponse is the response containing a list of issues.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "resourceIssues": [
        {
          object ([DatabaseResourceIssue](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryIssues#DatabaseResourceIssue))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`resourceIssues[]` |  `object (`[DatabaseResourceIssue](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryIssues#DatabaseResourceIssue)`)` List of issues and resource details.  
`nextPageToken` |  `string` A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. List of unreachable regions from where data could not be retrieved.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `databasecenter.fleetHealthStats.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## SignalProductsFilters

SignalProductsFilters represents a signal and list of supported products.

JSON representation  
---  
      
    
    {
      "signalType": enum ([SignalType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalType)),
      "products": [
        {
          object ([Product](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Product))
        }
      ]
    }  
  
Fields  
---  
`signalType` |  `enum (`[SignalType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalType)`)` Optional. The type of signal.  
`products[]` |  `object (`[Product](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Product)`)` Optional. Product type of the resource. The version of the product will be ignored in filtering.  
  
## DatabaseResourceIssue

DatabaseResource and Issue associated with it.

JSON representation  
---  
      
    
    {
      "signal": {
        object ([Signal](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal))
      },
      "resource": {
        object ([DatabaseResource](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource))
      }
    }  
  
Fields  
---  
`signal` |  `object (`[Signal](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal)`)` Signal associated with the issue.  
`resource` |  `object (`[DatabaseResource](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource)`)` Resource associated with the issue.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
