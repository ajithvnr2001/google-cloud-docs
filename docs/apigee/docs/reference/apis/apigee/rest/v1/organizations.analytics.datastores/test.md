---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/test/
title: Method: organizations.analytics.datastores.test \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:16.677254+00:00
---

# Method: organizations.analytics.datastores.test  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/test/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.analytics.datastores.test Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Test if Datastore configuration is correct. This includes checking if credentials provided by customer have required permissions in target destination storage

### HTTP request

`POST https://apigee.googleapis.com/v1/{parent=organizations/*}/analytics/datastores:test`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent organization name Must be of the form `organizations/{org}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.datastores.create`

  
  
### Request body

The request body contains an instance of `[Datastore](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores#Datastore)`.

### Response body

The response for `[datastores.test](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/test#google.cloud.apigee.v1.AnalyticsDatastore.TestDatastore)`

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "state": string,
      "error": string
    }  
  
Fields  
---  
`state` |  `string` Output only. It could be `completed` or `failed`  
`error` |  `string` Output only. Error message of test connection failure  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
