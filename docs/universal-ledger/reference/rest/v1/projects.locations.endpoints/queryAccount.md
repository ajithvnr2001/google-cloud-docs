---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryAccount/
title: Method: projects.locations.endpoints.queryAccount \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:05.091162+00:00
---

# Method: projects.locations.endpoints.queryAccount  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryAccount/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  Method: projects.locations.endpoints.queryAccount Stay organized with collections  Save and categorize content based on your preferences. 

Queries all the information stored about an account in the network. The returned account details may vary between calls, because an endpoint may route requests to different validators within the network and region, and the validators may not be at the same round ID at any given time.

### HTTP request

Choose an endpoint:

globalus-central1us-east1us-east4us-east5us-west1europe-west2europe-west3

  
`GET https://universalledger.googleapis.com/v1/{endpoint=projects/*/locations/*/endpoints/*}:queryAccount`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`endpoint` |  `string` Required. The endpoint to serve the request. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}` The location is a region.  
  
### Query parameters

Parameters  
---  
`accountId` |  `string` Required. The account ID to get information about. The value is limited to 60 characters.  
`roundId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The ID of the execution round (similar to block "height") at which to request data. The returned account information will be accurate for the world state at this execution round. If unspecified, uses the latest finalized round as known by the serving validator. The state at a given round ID is always consistent and canonical.  
  
### Request body

The request body must be empty.

### Response body

Response message for endpoints.queryAccount.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "account": {
        object ([Account](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account))
      }
    }  
  
Fields  
---  
`account` |  `object (`[Account](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account)`)` The account information, along with the height at which it was obtained.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
