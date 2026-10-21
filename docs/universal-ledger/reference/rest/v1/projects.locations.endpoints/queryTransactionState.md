---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryTransactionState/
title: Method: projects.locations.endpoints.queryTransactionState \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:51:46.123221+00:00
---

# Method: projects.locations.endpoints.queryTransactionState  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryTransactionState/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  Method: projects.locations.endpoints.queryTransactionState Stay organized with collections  Save and categorize content based on your preferences. 

Queries the state of a transaction. This method can be called for any transaction submitted to the network. The returned transaction details may vary between calls, because an endpoint may route requests to different validators within the network and region, and the validators may not be at the same round ID at any given time.

### HTTP request

Choose an endpoint:

globalus-central1us-east1us-east4us-east5us-west1europe-west2europe-west3

  
`GET https://universalledger.googleapis.com/v1/{endpoint=projects/*/locations/*/endpoints/*}:queryTransactionState`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`endpoint` |  `string` Required. The endpoint to serve the request. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}` The location is a region.  
  
### Query parameters

Parameters  
---  
`transactionDigestHex` |  `string` Required. The transaction ID to get the state of.  
  
### Request body

The request body must be empty.

### Response body

Response message for endpoints.queryTransactionState.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "transactionAttempts": [
        {
          object ([TransactionAttempt](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt))
        }
      ]
    }  
  
Fields  
---  
`transactionAttempts[]` |  `object (`[TransactionAttempt](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt)`)` One entry per each known submission of the transaction to the validator handling the request.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
