---
url: https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/rollbackFunctionUpgradeTraffic/
title: Method: projects.locations.functions.rollbackFunctionUpgradeTraffic \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:29.471271+00:00
---

# Method: projects.locations.functions.rollbackFunctionUpgradeTraffic  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/reference/rest/v2beta/projects.locations.functions/rollbackFunctionUpgradeTraffic/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Reference ](https://docs.cloud.google.com/functions/docs/apis)



Send feedback 

#  Method: projects.locations.functions.rollbackFunctionUpgradeTraffic Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Reverts the traffic target of a function from the 2nd Gen copy to the original 1st Gen function. After this operation, all new traffic would be served by the 1st Gen.

### HTTP request

`POST https://cloudfunctions.googleapis.com/v2beta/{name}:rollbackFunctionUpgradeTraffic`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the function for which traffic target should be changed back to 1st Gen from 2nd Gen. It takes the form `projects/{project}/locations/{location}/functions/{function}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `cloudfunctions.functions.generationUpgrade`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/functions/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
