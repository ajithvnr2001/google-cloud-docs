---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.hostProjectRegistrations/get/
title: Method: projects.locations.hostProjectRegistrations.get \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:00.669245+00:00
---

# Method: projects.locations.hostProjectRegistrations.get  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.hostProjectRegistrations/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: projects.locations.hostProjectRegistrations.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Get a host project registration.

### HTTP request

`GET https://apihub.googleapis.com/v1/{name=projects/*/locations/*/hostProjectRegistrations/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Host project registration resource name. projects/{project}/locations/{location}/hostProjectRegistrations/{hostProjectRegistrationId}  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[HostProjectRegistration](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.hostProjectRegistrations#HostProjectRegistration)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/apihub.readonly`
  * ` https://www.googleapis.com/auth/apihub.readwrite`
  * ` https://www.googleapis.com/auth/cloud-platform`



### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `apihub.hostProjectRegistrations.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-25 UTC."],[],[]] 
