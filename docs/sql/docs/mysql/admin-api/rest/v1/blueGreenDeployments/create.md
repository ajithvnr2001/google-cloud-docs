---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments/create/
title: Method: blueGreenDeployments.create \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:50.319392+00:00
---

# Method: blueGreenDeployments.create  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Method: blueGreenDeployments.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Creates a blue-green deployment under a given project and location.

### HTTP request

`POST https://sqladmin.googleapis.com/v1/{parent=projects/*/locations/*}/blueGreenDeployments`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where this blue-green deployment will be created. Format: projects/{project}/locations/{location}  
  
### Query parameters

Parameters  
---  
`blueGreenDeploymentId` |  `string` Required. The ID to use for the blue-green deployment, which will become the final component of the deployment's resource name. The ID must be unique within the given project and location and between 2-63 characters.  
  
### Request body

The request body contains an instance of `[BlueGreenDeployment](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments#BlueGreenDeployment)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/operations#Operation)`.

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
