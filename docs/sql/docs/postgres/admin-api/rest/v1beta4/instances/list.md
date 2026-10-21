---
url: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/list/
title: Method: instances.list \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:14:32.225127+00:00
---

# Method: instances.list  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/postgres/apis)



Send feedback 

#  Method: instances.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists instances under a given project.

### HTTP request

`GET https://sqladmin.googleapis.com/sql/v1beta4/projects/{project}/instances`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID of the project for which to list Cloud SQL instances.  
  
### Query parameters

Parameters  
---  
`filter` |  `string` A filter expression that filters resources listed in the response. The expression is in the form of field:value. For example, 'instanceType:CLOUD_SQL_INSTANCE'. Fields can be nested as needed as per their JSON representation, such as 'settings.userLabels.auto_start:true'.Multiple filter queries are space-separated. For example. 'state:RUNNABLE instanceType:CLOUD_SQL_INSTANCE'. By default, each expression is an AND expression. However, you can include AND and OR expressions explicitly.  
`maxResults` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The maximum number of instances to return. The service may return fewer than this value. If unspecified, at most 500 instances are returned. The maximum value is 1000; values above 1000 are coerced to 1000.  
`pageToken` |  `string` A previously-returned page token representing part of the larger set of results to view.  
  
### Request body

The request body must be empty.

### Response body

Database instances list response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "warnings": [
        {
          object ([ApiWarning](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/operations#ApiWarning))
        }
      ],
      "items": [
        {
          object ([DatabaseInstance](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances#DatabaseInstance))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#instancesList`.  
`warnings[]` |  `object (`[ApiWarning](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/operations#ApiWarning)`)` instances.list of warnings that occurred while handling the request.  
`items[]` |  `object (`[DatabaseInstance](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances#DatabaseInstance)`)` instances.list of database instance resources.  
`nextPageToken` |  `string` The continuation token, used to page through large result sets. Provide this value in a subsequent request to return the next page of results.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
