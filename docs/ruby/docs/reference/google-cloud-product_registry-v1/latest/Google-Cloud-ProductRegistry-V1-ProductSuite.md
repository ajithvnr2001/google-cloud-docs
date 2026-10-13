---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-product_registry-v1/latest/Google-Cloud-ProductRegistry-V1-ProductSuite/
title: Cloud Product Registry V1 API - Class Google::Cloud::ProductRegistry::V1::ProductSuite (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:15.730315+00:00
---

# Cloud Product Registry V1 API - Class Google::Cloud::ProductRegistry::V1::ProductSuite (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-product_registry-v1/latest/Google-Cloud-ProductRegistry-V1-ProductSuite/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Product Registry V1 API - Class Google::Cloud::ProductRegistry::V1::ProductSuite (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the Cloud Product Registry V1 API class Google::Cloud::ProductRegistry::V1::ProductSuite.

Represents a unified grouping of products sharing a common brand and market positioning.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #logical_products
    
    
    def logical_products() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. LogicalProducts under this suite. Format: logicalProducts/{logical_product} 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. The resource name of the ProductSuite. Format: productSuites/{product_suite} 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. The resource name of the ProductSuite. Format: productSuites/{product_suite} 



**Returns**

  * (::String) — Identifier. The resource name of the ProductSuite. Format: productSuites/{product_suite} 



### #replaced
    
    
    def replaced() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Indicates whether the product suite has been replaced. If `false`, the product suite is active. If `true`, the product suite has been replaced by another type, and the `replacement` field contains the resource name of that replacement. 



### #replacement
    
    
    def replacement() -> ::String

**Returns**

  * (::String) — Output only. The resource name of the Logical Entity that the product suite is replaced by. This field is only populated when this product suite is replaced by some other type. Eg: logicalProducts/{logical_product}, logicalProducts/{logical_product}/variants/{variant}, etc. 



### #title
    
    
    def title() -> ::String

**Returns**

  * (::String) — Title of the ProductSuite. 



### #title=
    
    
    def title=(value) -> ::String

**Parameter**

  * **value** (::String) — Title of the ProductSuite. 



**Returns**

  * (::String) — Title of the ProductSuite. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
