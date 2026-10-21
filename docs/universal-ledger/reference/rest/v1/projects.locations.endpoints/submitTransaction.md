---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/submitTransaction/
title: Method: projects.locations.endpoints.submitTransaction \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:04.862695+00:00
---

# Method: projects.locations.endpoints.submitTransaction  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/submitTransaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  Method: projects.locations.endpoints.submitTransaction Stay organized with collections  Save and categorize content based on your preferences. 

Submits a transaction to the network. The request is first validated for basic correctness. If validation fails, the request will fail immediately. If validation succeeds, this method returns only after the transaction has been replicated across a majority of validators in the network, or until the request fails.

### HTTP request

Choose an endpoint:

globalus-central1us-east1us-east4us-east5us-west1europe-west2europe-west3

  
`POST https://universalledger.googleapis.com/v1/{endpoint=projects/*/locations/*/endpoints/*}:submitTransaction`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`endpoint` |  `string` Required. The endpoint to submit the transaction to. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}` The location is a region.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "serializedSignedTransaction": string
    }  
  
Fields  
---  
`serializedSignedTransaction` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. A protobuf serialized `[SignedTransaction](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/SignedTransaction)` to submit to the ledger. Using a serialized format ensures that all validators compute the same transaction ID as the SHA-256 digest of the serialized bytes.A base64-encoded string.  
  
### Response body

Response message for endpoints.submitTransaction.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "transactionDigestHex": string
    }  
  
Fields  
---  
`transactionDigestHex` |  `string` Identifier that uniquely represents the submitted transaction. It is the hexadecimal representation of the SHA-256 digest of the `serializedSignedTransaction`. This transaction ID is provided so that a client can track the transaction without needing to implement the hashing logic itself. The identifier can be directly used in subsequent API calls, for example to query the transaction state.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-19 UTC."],[],[]] 
