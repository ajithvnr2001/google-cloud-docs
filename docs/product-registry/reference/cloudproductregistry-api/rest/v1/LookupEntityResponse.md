---
url: https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/LookupEntityResponse/
title: LookupEntityResponse \u00a0|\u00a0 Cloud Product Registry API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:46:00.885203+00:00
---

# LookupEntityResponse  |  Cloud Product Registry API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/LookupEntityResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Product Registry API ](https://docs.cloud.google.com/product-registry)
  * [ APIs & Reference ](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest)



Send feedback 

#  LookupEntityResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response message for LookupEntity.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "logicalProduct": {
        object ([LogicalProduct](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts#LogicalProduct))
      },
      "logicalProductVariant": {
        object ([LogicalProductVariant](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts.variants#LogicalProductVariant))
      },
      "productSuite": {
        object ([ProductSuite](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/productSuites#ProductSuite))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Matched entity. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`logicalProduct` |  `object (`[LogicalProduct](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts#LogicalProduct)`)` Matched LogicalProduct.  
`logicalProductVariant` |  `object (`[LogicalProductVariant](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/logicalProducts.variants#LogicalProductVariant)`)` Matched LogicalProductVariant.  
`productSuite` |  `object (`[ProductSuite](https://docs.cloud.google.com/product-registry/reference/cloudproductregistry-api/rest/v1/productSuites#ProductSuite)`)` Matched ProductSuite.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
