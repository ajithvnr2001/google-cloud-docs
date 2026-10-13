---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments/list/
title: Method: blueGreenDeployments.list \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:51.136186+00:00
---

# Method: blueGreenDeployments.list  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Method: blueGreenDeployments.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists blue-green deployments under a given project.

### HTTP request

`GET https://sqladmin.googleapis.com/v1/{parent=projects/*/locations/*}/blueGreenDeployments`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource whose blue-green deployments are to be listed. Format: projects/{project}/locations/{location}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of deployments to return. The service may return fewer deployments than this value. If unspecified, at most 500 deployments are returned. The maximum value is 1000; values above 1000 are treated as 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `blueGreenDeployments.list` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` Optional. A filter expression that filters the results.  
`orderBy` |  `string` Optional. A comma-separated list of fields to order the results by.  
  
### Request body

The request body must be empty.

### Response body

The response message for listing blue-green deployment resources.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "blueGreenDeployments": [
        {
          object ([BlueGreenDeployment](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#BlueGreenDeployment))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`blueGreenDeployments[]` |  `object (`[BlueGreenDeployment](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#BlueGreenDeployment)`)` The list of blue-green deployment resources.  
`nextPageToken` |  `string` A token to retrieve the next page of results, or empty if there are no more results.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
