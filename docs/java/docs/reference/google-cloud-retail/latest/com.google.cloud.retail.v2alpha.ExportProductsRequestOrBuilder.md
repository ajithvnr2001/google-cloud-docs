---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ExportProductsRequestOrBuilder
title: Interface ExportProductsRequestOrBuilder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:51.164368+00:00
---

# Interface ExportProductsRequestOrBuilder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.ExportProductsRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ExportProductsRequestOrBuilder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 
    
    
    public interface ExportProductsRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getFilter()
    
    
    public abstract String getFilter()

A filtering expression to specify restrictions on returned events. The expression is a sequence of terms. Each term applies a restriction to the returned products. Use this expression to restrict results to a specific time range, tag, or stock state or to filter products by product type. For example, `lastModifiedTime > "2012-04-23T18:25:43.511Z" lastModifiedTime<"2012-04-23T18:25:43.511Z" productType=primary`

We expect only four types of fields:

  * `lastModifiedTime`: This can be specified twice, once with a less than operator and once with a greater than operator. The `lastModifiedTime` restriction should result in one, contiguous, valid, last-modified, time range.

  * `productType`: Supported values are `primary` and `variant`. The Boolean operators `OR` and `NOT` are supported if the expression is enclosed in parentheses and must be separated from the `productType` values by a space.

  * `availability`: Supported values are `IN_STOCK`, `OUT_OF_STOCK`, `PREORDER`, and `BACKORDER`. Boolean operators `OR` and `NOT` are supported if the expression is enclosed in parentheses and must be separated from the `availability` values by a space.

  * `Tag expressions`: Restricts output to products that match all of the specified tags. Boolean operators `OR` and `NOT` are supported if the expression is enclosed in parentheses and the operators are separated from the tag values by a space. Also supported is '`-"tagA"`', which is equivalent to '`NOT "tagA"`'. Tag values must be double-quoted, UTF-8 encoded strings and have a size limit of 1,000 characters.

Some examples of valid filters expressions:

  * Example 1: `lastModifiedTime > "2012-04-23T18:25:43.511Z" lastModifiedTime < "2012-04-23T18:30:43.511Z"`

  * Example 2: `lastModifiedTime > "2012-04-23T18:25:43.511Z" productType = "variant"`
  * Example 3: `tag=("Red" OR "Blue") tag="New-Arrival" tag=(NOT "promotional") productType = "primary" lastModifiedTime < "2018-04-23T18:30:43.511Z"`
  * Example 4: `lastModifiedTime > "2012-04-23T18:25:43.511Z"`
  * Example 5: `availability = (IN_STOCK OR BACKORDER)`



`string filter = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The filter.  
  
### getFilterBytes()
    
    
    public abstract ByteString getFilterBytes()

A filtering expression to specify restrictions on returned events. The expression is a sequence of terms. Each term applies a restriction to the returned products. Use this expression to restrict results to a specific time range, tag, or stock state or to filter products by product type. For example, `lastModifiedTime > "2012-04-23T18:25:43.511Z" lastModifiedTime<"2012-04-23T18:25:43.511Z" productType=primary`

We expect only four types of fields:

  * `lastModifiedTime`: This can be specified twice, once with a less than operator and once with a greater than operator. The `lastModifiedTime` restriction should result in one, contiguous, valid, last-modified, time range.

  * `productType`: Supported values are `primary` and `variant`. The Boolean operators `OR` and `NOT` are supported if the expression is enclosed in parentheses and must be separated from the `productType` values by a space.

  * `availability`: Supported values are `IN_STOCK`, `OUT_OF_STOCK`, `PREORDER`, and `BACKORDER`. Boolean operators `OR` and `NOT` are supported if the expression is enclosed in parentheses and must be separated from the `availability` values by a space.

  * `Tag expressions`: Restricts output to products that match all of the specified tags. Boolean operators `OR` and `NOT` are supported if the expression is enclosed in parentheses and the operators are separated from the tag values by a space. Also supported is '`-"tagA"`', which is equivalent to '`NOT "tagA"`'. Tag values must be double-quoted, UTF-8 encoded strings and have a size limit of 1,000 characters.

Some examples of valid filters expressions:

  * Example 1: `lastModifiedTime > "2012-04-23T18:25:43.511Z" lastModifiedTime < "2012-04-23T18:30:43.511Z"`

  * Example 2: `lastModifiedTime > "2012-04-23T18:25:43.511Z" productType = "variant"`
  * Example 3: `tag=("Red" OR "Blue") tag="New-Arrival" tag=(NOT "promotional") productType = "primary" lastModifiedTime < "2018-04-23T18:30:43.511Z"`
  * Example 4: `lastModifiedTime > "2012-04-23T18:25:43.511Z"`
  * Example 5: `availability = (IN_STOCK OR BACKORDER)`



`string filter = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for filter.  
  
### getOutputConfig()
    
    
    public abstract OutputConfig getOutputConfig()

Required. The output location of the data.

` .google.cloud.retail.v2alpha.OutputConfig output_config = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[OutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.OutputConfig)` | The outputConfig.  
  
### getOutputConfigOrBuilder()
    
    
    public abstract OutputConfigOrBuilder getOutputConfigOrBuilder()

Required. The output location of the data.

` .google.cloud.retail.v2alpha.OutputConfig output_config = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[OutputConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2alpha.OutputConfigOrBuilder)` |   
  
### getParent()
    
    
    public abstract String getParent()

Required. Resource name of a Branch, and `default_branch` for branch_id component is supported. For example `projects/1234/locations/global/catalogs/default_catalog/branches/default_branch`

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. Resource name of a Branch, and `default_branch` for branch_id component is supported. For example `projects/1234/locations/global/catalogs/default_catalog/branches/default_branch`

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### hasOutputConfig()
    
    
    public abstract boolean hasOutputConfig()

Required. The output location of the data.

` .google.cloud.retail.v2alpha.OutputConfig output_config = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the outputConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
