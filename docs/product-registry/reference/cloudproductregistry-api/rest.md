---
url: https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/
title: Cloud Product Registry API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:46:00.326970+00:00
---

# Cloud Product Registry API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Product Registry API ](https://docs.cloud.google.com/product-registry)
  * [ APIs & Reference ](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest)



Send feedback 

#  Cloud Product Registry API Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Product Registry API provides capabilities to access all first Google Cloud products.

  * REST Resource: v1.logicalProducts
  * REST Resource: v1.logicalProducts.variants
  * REST Resource: v1.productSuites



## Service: cloudproductregistry.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://cloudproductregistry.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://cloudproductregistry.googleapis.com`



## REST Resource: [v1.logicalProducts](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts)

Methods  
---  
`[get](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts/get)` |  `GET /v1/{name=logicalProducts/*}`   
Gets details of a LogicalProduct.  
`[list](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts/list)` |  `GET /v1/logicalProducts`   
Lists LogicalProducts matching given criteria.  
`[lookupEntity](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts/lookupEntity)` |  `GET /v1/{lookupUri=logicalProducts/*}:lookupEntity`   
Look up entities.  
  
## REST Resource: [v1.logicalProducts.variants](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts.variants)

Methods  
---  
`[get](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts.variants/get)` |  `GET /v1/{name=logicalProducts/*/variants/*}`   
Get details of a LogicalProductVariant.  
`[list](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts.variants/list)` |  `GET /v1/{parent=logicalProducts/*}/variants`   
Lists LogicalProductVariants matching given criteria.  
`[lookupEntity](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts.variants/lookupEntity)` |  `GET /v1/{lookupUri=logicalProducts/*/variants/*}:lookupEntity`   
Look up entities.  
  
## REST Resource: [v1.productSuites](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/productSuites)

Methods  
---  
`[get](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/productSuites/get)` |  `GET /v1/{name=productSuites/*}`   
Get details of a ProductSuite.  
`[list](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/productSuites/list)` |  `GET /v1/productSuites`   
Lists ProductSuites.  
`[lookupEntity](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/productSuites/lookupEntity)` |  `GET /v1/{lookupUri=productSuites/*}:lookupEntity`   
Look up entities.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
