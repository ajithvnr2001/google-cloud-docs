---
url: https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users/getLoginProfile/
title: Method: users.getLoginProfile \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:13:38.070744+00:00
---

# Method: users.getLoginProfile  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/users/getLoginProfile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: users.getLoginProfile Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Retrieves the profile information used for logging in to a virtual machine on Google Compute Engine.

### HTTP request

`GET https://oslogin.googleapis.com/v1beta/{name=users/*}/loginProfile`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The unique ID for the user in format `users/{user}`.  
  
### Query parameters

Parameters  
---  
`projectId` |  `string` Required. The project ID of the Google Cloud Platform project.  
`systemId` |  `string` Optional. A system ID for filtering the results of the request.  
`view` |  `enum (`[LoginProfileView](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/LoginProfileView)`)` The view configures whether to retrieve security keys information.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[LoginProfile](https://docs.cloud.google.com/compute/docs/oslogin/rest/v1beta/LoginProfile)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/compute.readonly`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
