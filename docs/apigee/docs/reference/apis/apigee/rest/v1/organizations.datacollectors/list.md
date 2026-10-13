---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors/list/
title: Method: organizations.datacollectors.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:31.960882+00:00
---

# Method: organizations.datacollectors.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.datacollectors.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists all data collectors.

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*}/datacollectors`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the organization for which to list data collectors in the following format: `organizations/{org}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.datacollectors.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Maximum number of data collectors to return. The page size defaults to 25.  
`pageToken` |  `string` Page token, returned from a previous datacollectors.list call, that you can use to retrieve the next page.  
  
### Request body

The request body must be empty.

### Response body

Response for `[datacollectors.list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors/list#google.cloud.apigee.v1.DataCollectorService.ListDataCollectors)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dataCollectors": [
        {
          object ([DataCollector](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors#DataCollector))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`dataCollectors[]` |  `object (`[DataCollector](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors#DataCollector)`)` Data collectors in the specified organization.  
`nextPageToken` |  `string` Page token that you can include in a datacollectors.list request to retrieve the next page. If omitted, no subsequent pages exist.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
