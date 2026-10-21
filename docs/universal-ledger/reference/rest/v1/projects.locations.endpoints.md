---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints
title: REST Resource: projects.locations.endpoints \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:42:07.694450+00:00
---

# REST Resource: projects.locations.endpoints  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  REST Resource: projects.locations.endpoints Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: Endpoint

Represents a Universal Ledger endpoint.

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the endpoint. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/get)`

|  Gets the details of a specific endpoint.  
  
### `[list](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/list)`

|  Lists all endpoints for a given project and location.  
  
### `[queryAccount](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryAccount)`

|  Queries all the information stored about an account in the network.  
  
### `[queryData](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryData)`

|  Queries the network for information stored on the ledger, such as accounts and transactions.  
  
### `[queryTransactionState](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryTransactionState)`

|  Queries the state of a transaction.  
  
### `[submitOperationalTransaction](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/submitOperationalTransaction)`

|  Submits an operational transaction to the network.  
  
### `[submitTransaction](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/submitTransaction)`

|  Submits a transaction to the network.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
