---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/connect/resolve/
title: Method: connect.resolve \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:03.861276+00:00
---

# Method: connect.resolve  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/connect/resolve/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Method: connect.resolve Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Retrieves connect settings about a Cloud SQL instance using the instance DNS name.

### HTTP request

`GET https://sqladmin.googleapis.com/sql/v1beta4/locations/{location}/dns/{dnsName}:resolveConnectSettings`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`location` |  `string` Required. The region of the instance.  
`dnsName` |  `string` Required. Cloud SQL instance ID. This does not include the project ID.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ConnectSettings](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/ConnectSettings)`.

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
