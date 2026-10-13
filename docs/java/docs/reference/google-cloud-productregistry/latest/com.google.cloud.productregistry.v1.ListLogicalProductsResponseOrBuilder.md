---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.ListLogicalProductsResponseOrBuilder
title: Interface ListLogicalProductsResponseOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:18.774247+00:00
---

# Interface ListLogicalProductsResponseOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.ListLogicalProductsResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ListLogicalProductsResponseOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface ListLogicalProductsResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getLogicalProducts(int index)
    
    
    public abstract LogicalProduct getLogicalProducts(int index)

Matched LogicalProducts

`repeated .google.cloud.productregistry.v1.LogicalProduct logical_products = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogicalProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LogicalProduct)` |   
  
### getLogicalProductsCount()
    
    
    public abstract int getLogicalProductsCount()

Matched LogicalProducts

`repeated .google.cloud.productregistry.v1.LogicalProduct logical_products = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLogicalProductsList()
    
    
    public abstract List<LogicalProduct> getLogicalProductsList()

Matched LogicalProducts

`repeated .google.cloud.productregistry.v1.LogicalProduct logical_products = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LogicalProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LogicalProduct)>` |   
  
### getLogicalProductsOrBuilder(int index)
    
    
    public abstract LogicalProductOrBuilder getLogicalProductsOrBuilder(int index)

Matched LogicalProducts

`repeated .google.cloud.productregistry.v1.LogicalProduct logical_products = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogicalProductOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LogicalProductOrBuilder)` |   
  
### getLogicalProductsOrBuilderList()
    
    
    public abstract List<? extends LogicalProductOrBuilder> getLogicalProductsOrBuilderList()

Matched LogicalProducts

`repeated .google.cloud.productregistry.v1.LogicalProduct logical_products = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.productregistry.v1.LogicalProductOrBuilder>` |   
  
### getNextPageToken()
    
    
    public abstract String getNextPageToken()

A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextPageToken.  
  
### getNextPageTokenBytes()
    
    
    public abstract ByteString getNextPageTokenBytes()

A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextPageToken.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
