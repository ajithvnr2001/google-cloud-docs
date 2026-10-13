---
url: https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions/call/
title: Method: projects.locations.functions.call \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:51.398004+00:00
---

# Method: projects.locations.functions.call  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions/call/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Reference ](https://docs.cloud.google.com/functions/docs/apis)



Send feedback 

#  Method: projects.locations.functions.call Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Synchronously invokes a deployed Cloud Function. To be used for testing purposes as very limited traffic is allowed. For more information on the actual limits, refer to [Rate Limits](https://cloud.google.com/functions/quotas#rate_limits).

### HTTP request

`POST https://cloudfunctions.googleapis.com/v1/{name}:call`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the function to be called. It takes the form `projects/{project}/locations/{location}/functions/{function}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `cloudfunctions.functions.call`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "data": string
    }  
  
Fields  
---  
`data` |  `string` Required. Input to be passed to the function.  
  
### Response body

Response of `functions.call` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "executionId": string,
      "result": string,
      "error": string
    }  
  
Fields  
---  
`executionId` |  `string` Execution id of function invocation.  
`result` |  `string` Result populated for successful execution of synchronous function. Will not be populated if function does not return a result through context.  
`error` |  `string` Either system or user-function generated error. Set if execution was not successful.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-01 UTC."],[],[]] 
