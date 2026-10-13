---
url: https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts/
title: REST Resource: logicalProducts \u00a0|\u00a0 Cloud Product Registry API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:46:00.254352+00:00
---

# REST Resource: logicalProducts  |  Cloud Product Registry API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Product Registry API ](https://docs.cloud.google.com/product-registry)
  * [ APIs & Reference ](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest)



Send feedback 

#  REST Resource: logicalProducts Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: LogicalProduct
    * JSON representation
  * Methods



## Resource: LogicalProduct

Represents an independent service offering that can be provisioned by a customer.

JSON representation  
---  
      
    
    {
      "name": string,
      "title": string,
      "productSuite": string,
      "variants": [
        string
      ],
      "lifecycleState": enum ([LifecycleState](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/LifecycleState)),
      "replaced": boolean,
      "replacement": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the LogicalProduct. Format: logicalProducts/{logicalProduct}.  
`title` |  `string` Display name of the LogicalProduct.  
`productSuite` |  `string` Product suite associated with the logical product. Format: productSuites/{productSuite}.  
`variants[]` |  `string` Output only. Child variant resource references. Format: logicalProducts/{logicalProduct}/variants/{variant}  
`lifecycleState` |  `enum (`[LifecycleState](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/LifecycleState)`)` Output only. Current Lifecycle state of the logical product.  
`replaced` |  `boolean` Output only. Indicates whether the logical product has been replaced. If `false`, the product is active. If `true`, the product has been replaced by another type, and the `replacement` field contains the resource name of that replacement.  
`replacement` |  `string` Output only. The resource name of the Logical Entity that the logical product is replaced by. This field is only populated when this logical product is replaced by some other type. Eg: logicalProducts/{logicalProduct}/variants/{variant}, productSuites/{productSuite}, etc.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts/get)`

|  Gets details of a LogicalProduct.  
  
### `[list](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts/list)`

|  Lists LogicalProducts matching given criteria.  
  
### `[lookupEntity](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts/lookupEntity)`

|  Look up entities.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-27 UTC."],[],[]] 
