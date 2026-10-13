---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/list/
title: Method: organizations.analytics.datastores.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:16.284863+00:00
---

# Method: organizations.analytics.datastores.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.analytics.datastores.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



List Datastores

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*}/analytics/datastores`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent organization name. Must be of the form `organizations/{org}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.datastores.list`

  
  
### Query parameters

Parameters  
---  
`targetType` |  `string` Optional. TargetType is used to fetch all Datastores that match the type  
  
### Request body

The request body must be empty.

### Response body

The response for `[datastores.list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/list#google.cloud.apigee.v1.AnalyticsDatastore.ListDatastores)`

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "datastores": [
        {
          object ([Datastore](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores#Datastore))
        }
      ]
    }  
  
Fields  
---  
`datastores[]` |  `object (`[Datastore](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores#Datastore)`)` A list of datastores  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
