---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/list/
title: Method: projects.locations.instances.list \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:14.827382+00:00
---

# Method: projects.locations.instances.list  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Reference ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest)



Send feedback 

#  Method: projects.locations.instances.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Lists instances.

### HTTP request

`GET https://financialservices.googleapis.com/v1/{parent=projects/*/locations/*}/instances`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent of the Instance is the location for that Instance. Every location has exactly one instance. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `financialservices.v1instances.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The number of resources to be included in the response. The response contains a nextPageToken, which can be used to retrieve the next page of resources.  
`pageToken` |  `string` In case of paginated results, this is the token that was returned in the previous ListInstancesResponse. It should be copied here to retrieve the next page of resources. This will be empty for the first instance of ListInstancesRequest.  
`filter` |  `string` Specify a filter to narrow search results.  
`orderBy` |  `string` Specify a field to use for ordering.  
  
### Request body

The request body must be empty.

### Response body

Response for retrieving a list of Instances

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "instances": [
        {
          object ([Instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances#Instance))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`instances[]` |  `object (`[Instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances#Instance)`)` List of Instance resources  
`nextPageToken` |  `string` This token should be passed to the next ListInstancesRequest to retrieve the next page of Instances.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `financialservices.v1instances.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-18 UTC."],[],[]] 
