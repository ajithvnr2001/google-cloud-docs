---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/
title: Universal Ledger API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:03.914401+00:00
---

# Universal Ledger API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  Universal Ledger API Stay organized with collections  Save and categorize content based on your preferences. 

Universal Ledger API.

## Service: universalledger.googleapis.com

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://universalledger.googleapis.com`



### Regional service endpoint

A regional service endpoint is a base URL that specifies the network address of an API service in a single region. A service that is available in multiple regions might have multiple regional endpoints. Select a location to see its regional service endpoint for this service. 

global us-central1 us-east1 us-east4 us-east5 us-west1 europe-west2 europe-west3

  

* `https://universalledger.googleapis.com`

## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.endpoints](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints)

Methods  
---  
`[get](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/get)` |  `GET /v1/{name=projects/*/locations/*/endpoints/*}`   
Gets the details of a specific endpoint.  
`[list](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/list)` |  `GET /v1/{parent=projects/*/locations/*}/endpoints`   
Lists all endpoints for a given project and location.  
`[queryAccount](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryAccount)` |  `GET /v1/{endpoint=projects/*/locations/*/endpoints/*}:queryAccount`   
Queries all the information stored about an account in the network.  
`[queryData](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryData)` |  `POST /v1/{endpoint=projects/*/locations/*/endpoints/*}:queryData`   
Queries the network for information stored on the ledger, such as accounts and transactions.  
`[queryTransactionState](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryTransactionState)` |  `GET /v1/{endpoint=projects/*/locations/*/endpoints/*}:queryTransactionState`   
Queries the state of a transaction.  
`[submitOperationalTransaction](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/submitOperationalTransaction)` |  `POST /v1/{endpoint=projects/*/locations/*/endpoints/*}:submitOperationalTransaction`   
Submits an operational transaction to the network.  
`[submitTransaction](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/submitTransaction)` |  `POST /v1/{endpoint=projects/*/locations/*/endpoints/*}:submitTransaction`   
Submits a transaction to the network.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
