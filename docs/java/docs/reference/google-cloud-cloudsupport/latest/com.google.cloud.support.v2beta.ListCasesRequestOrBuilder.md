---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.ListCasesRequestOrBuilder
title: Interface ListCasesRequestOrBuilder (0.83.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:49.208855+00:00
---

# Interface ListCasesRequestOrBuilder (0.83.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.ListCasesRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ListCasesRequestOrBuilder (0.83.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.83.0 (latest)  0.79.0  0.78.0  0.77.0  0.75.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.65.0  0.64.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.54.0  0.52.0  0.51.0  0.48.0  0.47.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ListCasesRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getFilter()
    
    
    public abstract String getFilter()

An expression used to filter cases.

If it's an empty string, then no filtering happens. Otherwise, the endpoint returns the cases that match the filter.

Expressions use the following fields separated by `AND` and specified with `=`:

  * `state`: Can be `OPEN` or `CLOSED`.
  * `priority`: Can be `P0`, `P1`, `P2`, `P3`, or `P4`. You can specify multiple values for priority using the `OR` operator. For example, `priority=P1 OR priority=P2`.
  * `creator.email`: The email address of the case creator.

EXAMPLES:

  * `state=CLOSED`

  * `state=OPEN AND creator.email="tester@example.com"`
  * `state=OPEN AND (priority=P0 OR priority=P1)`



`string filter = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The filter.  
  
### getFilterBytes()
    
    
    public abstract ByteString getFilterBytes()

An expression used to filter cases.

If it's an empty string, then no filtering happens. Otherwise, the endpoint returns the cases that match the filter.

Expressions use the following fields separated by `AND` and specified with `=`:

  * `state`: Can be `OPEN` or `CLOSED`.
  * `priority`: Can be `P0`, `P1`, `P2`, `P3`, or `P4`. You can specify multiple values for priority using the `OR` operator. For example, `priority=P1 OR priority=P2`.
  * `creator.email`: The email address of the case creator.

EXAMPLES:

  * `state=CLOSED`

  * `state=OPEN AND creator.email="tester@example.com"`
  * `state=OPEN AND (priority=P0 OR priority=P1)`



`string filter = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for filter.  
  
### getPageSize()
    
    
    public abstract int getPageSize()

The maximum number of cases fetched with each request. Defaults to 10.

`int32 page_size = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pageSize.  
  
### getPageToken()
    
    
    public abstract String getPageToken()

A token identifying the page of results to return. If unspecified, the first page is retrieved.

`string page_token = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pageToken.  
  
### getPageTokenBytes()
    
    
    public abstract ByteString getPageTokenBytes()

A token identifying the page of results to return. If unspecified, the first page is retrieved.

`string page_token = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pageToken.  
  
### getParent()
    
    
    public abstract String getParent()

Required. The name of a parent to list cases under.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The name of a parent to list cases under.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getProductLine()
    
    
    public abstract ProductLine getProductLine()

The product line to request cases for. If unspecified, only Google Cloud cases will be returned.

`optional .google.cloud.support.v2beta.ProductLine product_line = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ProductLine](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.ProductLine)` | The productLine.  
  
### getProductLineValue()
    
    
    public abstract int getProductLineValue()

The product line to request cases for. If unspecified, only Google Cloud cases will be returned.

`optional .google.cloud.support.v2beta.ProductLine product_line = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for productLine.  
  
### hasProductLine()
    
    
    public abstract boolean hasProductLine()

The product line to request cases for. If unspecified, only Google Cloud cases will be returned.

`optional .google.cloud.support.v2beta.ProductLine product_line = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the productLine field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
