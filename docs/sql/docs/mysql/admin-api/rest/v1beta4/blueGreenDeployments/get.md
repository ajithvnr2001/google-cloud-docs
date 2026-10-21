---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments/get/
title: Method: blueGreenDeployments.get \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:04.026974+00:00
---

# Method: blueGreenDeployments.get  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Method: blueGreenDeployments.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * BlueGreenDeploymentView
  * Examples
  * Try it!



Retrieves a blue-green deployment resource under a given project and location.

### HTTP request

`GET https://sqladmin.googleapis.com/sql/v1beta4/{name=projects/*/locations/*/blueGreenDeployments/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the blue-green deployment to retrieve. Format: projects/{project}/locations/{location}/blueGreenDeployments/{blueGreenDeployment}  
  
### Query parameters

Parameters  
---  
`view` |  `enum (`[BlueGreenDeploymentView](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments/get#BlueGreenDeploymentView)`)` Optional. Specifies whether to return the basic or detailed view of the resource in the response.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[BlueGreenDeployment](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments#BlueGreenDeployment)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## BlueGreenDeploymentView

The view of a `BlueGreenDeployment` resource.

Enums  
---  
`BLUE_GREEN_DEPLOYMENT_VIEW_UNSPECIFIED` | Blue-green deployment view enumeration. This allows the caller to specify what view they query. If unspecified (BLUE_GREEN_DEPLOYMENT_VIEW_UNSPECIFIED), the behavior is the same as BASIC.  
`BASIC` | Includes basic metadata about the blue-green deployment. `BASIC` is the default view.  
`DETAILED` | Includes basic metadata and configuration differences between source and target instances (`databaseVersion`, `tier`, `edition`, `availabilityType`, `dataDiskSizeGb`, and `dataDiskType`).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
