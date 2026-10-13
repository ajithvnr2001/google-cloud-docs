---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LookupEntityResponseOrBuilder
title: Interface LookupEntityResponseOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:18.247032+00:00
---

# Interface LookupEntityResponseOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LookupEntityResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface LookupEntityResponseOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface LookupEntityResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getEntityCase()
    
    
    public abstract LookupEntityResponse.EntityCase getEntityCase()

**Returns**  
---  
**Type** | **Description**  
`[LookupEntityResponse.EntityCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LookupEntityResponse.EntityCase)` |   
  
### getLogicalProduct()
    
    
    public abstract LogicalProduct getLogicalProduct()

Matched LogicalProduct.

`.google.cloud.productregistry.v1.LogicalProduct logical_product = 1;`

**Returns**  
---  
**Type** | **Description**  
`[LogicalProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LogicalProduct)` | The logicalProduct.  
  
### getLogicalProductOrBuilder()
    
    
    public abstract LogicalProductOrBuilder getLogicalProductOrBuilder()

Matched LogicalProduct.

`.google.cloud.productregistry.v1.LogicalProduct logical_product = 1;`

**Returns**  
---  
**Type** | **Description**  
`[LogicalProductOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LogicalProductOrBuilder)` |   
  
### getLogicalProductVariant()
    
    
    public abstract LogicalProductVariant getLogicalProductVariant()

Matched LogicalProductVariant.

`.google.cloud.productregistry.v1.LogicalProductVariant logical_product_variant = 2; `

**Returns**  
---  
**Type** | **Description**  
`[LogicalProductVariant](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LogicalProductVariant)` | The logicalProductVariant.  
  
### getLogicalProductVariantOrBuilder()
    
    
    public abstract LogicalProductVariantOrBuilder getLogicalProductVariantOrBuilder()

Matched LogicalProductVariant.

`.google.cloud.productregistry.v1.LogicalProductVariant logical_product_variant = 2; `

**Returns**  
---  
**Type** | **Description**  
`[LogicalProductVariantOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LogicalProductVariantOrBuilder)` |   
  
### getProductSuite()
    
    
    public abstract ProductSuite getProductSuite()

Matched ProductSuite.

`.google.cloud.productregistry.v1.ProductSuite product_suite = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ProductSuite](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.ProductSuite)` | The productSuite.  
  
### getProductSuiteOrBuilder()
    
    
    public abstract ProductSuiteOrBuilder getProductSuiteOrBuilder()

Matched ProductSuite.

`.google.cloud.productregistry.v1.ProductSuite product_suite = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ProductSuiteOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.ProductSuiteOrBuilder)` |   
  
### hasLogicalProduct()
    
    
    public abstract boolean hasLogicalProduct()

Matched LogicalProduct.

`.google.cloud.productregistry.v1.LogicalProduct logical_product = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the logicalProduct field is set.  
  
### hasLogicalProductVariant()
    
    
    public abstract boolean hasLogicalProductVariant()

Matched LogicalProductVariant.

`.google.cloud.productregistry.v1.LogicalProductVariant logical_product_variant = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the logicalProductVariant field is set.  
  
### hasProductSuite()
    
    
    public abstract boolean hasProductSuite()

Matched ProductSuite.

`.google.cloud.productregistry.v1.ProductSuite product_suite = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the productSuite field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
