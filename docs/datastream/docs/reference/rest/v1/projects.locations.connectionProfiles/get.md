---
url: https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles/get/
title: Method: projects.locations.connectionProfiles.get \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:39.657756+00:00
---

# Method: projects.locations.connectionProfiles.get  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Reference ](https://docs.cloud.google.com/datastream/docs/reference/rest)



Send feedback 

#  Method: projects.locations.connectionProfiles.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Examples
  * Try it!



Use this method to get details about a connection profile.

### HTTP request

`GET https://datastream.googleapis.com/v1/{name}`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the connection profile resource to get. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `datastream.connectionProfiles.get`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ConnectionProfile](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles#ConnectionProfile)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `datastream.connectionProfiles.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-13 UTC."],[],[]] 
