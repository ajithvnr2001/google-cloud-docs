---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/submitOperationalTransaction/
title: Method: projects.locations.endpoints.submitOperationalTransaction \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:04.909866+00:00
---

# Method: projects.locations.endpoints.submitOperationalTransaction  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/submitOperationalTransaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  Method: projects.locations.endpoints.submitOperationalTransaction Stay organized with collections  Save and categorize content based on your preferences. 

Submits an operational transaction to the network. This method returns only after the transaction has been replicated across a majority of validators in the network, or if the transaction fails.

### HTTP request

Choose an endpoint:

globalus-central1us-east1us-east4us-east5us-west1europe-west2europe-west3

  
`POST https://universalledger.googleapis.com/v1/{endpoint=projects/*/locations/*/endpoints/*}:submitOperationalTransaction`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`endpoint` |  `string` Required. The endpoint to serve the request. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}` The location is a region.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "serializedSignedOperationalTransaction": string
    }  
  
Fields  
---  
`serializedSignedOperationalTransaction` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. A protobuf serialized `[SignedTransaction](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/SignedTransaction)` to submit to the ledger. The enclosed client transaction must be an operational transaction, and the sender must be the platform operator. Using a serialized format ensures that all validators compute the same transaction ID as the SHA-256 digest of the serialized bytes.A base64-encoded string.  
  
### Response body

Response message for endpoints.submitOperationalTransaction.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "transactionDigestHex": string
    }  
  
Fields  
---  
`transactionDigestHex` |  `string` Identifier that uniquely represents the submitted operational transaction. It is the hexadecimal representation of the SHA-256 digest of the `serializedSignedOperationalTransaction`. This transaction ID is provided so that a client can track the transaction without needing to implement the hashing logic itself. The identifier can be directly used in subsequent API calls, for example to query the transaction state.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-19 UTC."],[],[]] 
