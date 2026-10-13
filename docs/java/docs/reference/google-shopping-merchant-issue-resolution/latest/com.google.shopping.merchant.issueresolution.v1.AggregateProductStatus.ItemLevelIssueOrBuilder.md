---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.AggregateProductStatus.ItemLevelIssueOrBuilder
title: Interface AggregateProductStatus.ItemLevelIssueOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:49.110167+00:00
---

# Interface AggregateProductStatus.ItemLevelIssueOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.AggregateProductStatus.ItemLevelIssueOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AggregateProductStatus.ItemLevelIssueOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.9.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public static interface AggregateProductStatus.ItemLevelIssueOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAttribute()
    
    
    public abstract String getAttribute()

The attribute's name, if the issue is caused by a single attribute.

`string attribute = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The attribute.  
  
### getAttributeBytes()
    
    
    public abstract ByteString getAttributeBytes()

The attribute's name, if the issue is caused by a single attribute.

`string attribute = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for attribute.  
  
### getCode()
    
    
    public abstract String getCode()

The error code of the issue.

`string code = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The code.  
  
### getCodeBytes()
    
    
    public abstract ByteString getCodeBytes()

The error code of the issue.

`string code = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for code.  
  
### getDescription()
    
    
    public abstract String getDescription()

A short issue description in English.

`string description = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

A short issue description in English.

`string description = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDetail()
    
    
    public abstract String getDetail()

A detailed issue description in English.

`string detail = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The detail.  
  
### getDetailBytes()
    
    
    public abstract ByteString getDetailBytes()

A detailed issue description in English.

`string detail = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for detail.  
  
### getDocumentationUri()
    
    
    public abstract String getDocumentationUri()

The URL of a web page to help with resolving this issue.

`string documentation_uri = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The documentationUri.  
  
### getDocumentationUriBytes()
    
    
    public abstract ByteString getDocumentationUriBytes()

The URL of a web page to help with resolving this issue.

`string documentation_uri = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for documentationUri.  
  
### getProductCount()
    
    
    public abstract long getProductCount()

The number of products affected by this issue.

`int64 product_count = 9;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The productCount.  
  
### getResolution()
    
    
    public abstract AggregateProductStatus.ItemLevelIssue.Resolution getResolution()

Whether the issue can be resolved by the merchant.

` .google.shopping.merchant.issueresolution.v1.AggregateProductStatus.ItemLevelIssue.Resolution resolution = 3; `

**Returns**  
---  
**Type** | **Description**  
`[AggregateProductStatus.ItemLevelIssue.Resolution](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.AggregateProductStatus.ItemLevelIssue.Resolution)` | The resolution.  
  
### getResolutionValue()
    
    
    public abstract int getResolutionValue()

Whether the issue can be resolved by the merchant.

` .google.shopping.merchant.issueresolution.v1.AggregateProductStatus.ItemLevelIssue.Resolution resolution = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for resolution.  
  
### getSeverity()
    
    
    public abstract AggregateProductStatus.ItemLevelIssue.Severity getSeverity()

How this issue affects serving of the offer.

` .google.shopping.merchant.issueresolution.v1.AggregateProductStatus.ItemLevelIssue.Severity severity = 2; `

**Returns**  
---  
**Type** | **Description**  
`[AggregateProductStatus.ItemLevelIssue.Severity](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.AggregateProductStatus.ItemLevelIssue.Severity)` | The severity.  
  
### getSeverityValue()
    
    
    public abstract int getSeverityValue()

How this issue affects serving of the offer.

` .google.shopping.merchant.issueresolution.v1.AggregateProductStatus.ItemLevelIssue.Severity severity = 2; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for severity.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
