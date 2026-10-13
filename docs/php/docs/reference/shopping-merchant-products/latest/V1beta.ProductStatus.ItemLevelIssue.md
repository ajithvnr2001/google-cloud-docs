---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.ProductStatus.ItemLevelIssue
title: Google Shopping Merchant Products V1beta Client - Class ItemLevelIssue (1.8.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:35.558473+00:00
---

# Google Shopping Merchant Products V1beta Client - Class ItemLevelIssue (1.8.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.ProductStatus.ItemLevelIssue

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Products V1beta Client - Class ItemLevelIssue (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.5  1.6.0  1.5.0  1.4.1  1.3.1  1.2.0  1.1.0  1.0.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Products V1beta Client class ItemLevelIssue.

The ItemLevelIssue of the product status.

Generated from protobuf message `google.shopping.merchant.products.v1beta.ProductStatus.ItemLevelIssue`

## Namespace

Google \ Shopping \ Merchant \ Products \ V1beta \ ProductStatus

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ code` |  `string`   
The error code of the issue.  
`↳ severity` |  `int`   
How this issue affects serving of the offer.  
`↳ resolution` |  `string`   
Whether the issue can be resolved by the business.  
`↳ attribute` |  `string`   
The attribute's name, if the issue is caused by a single attribute.  
`↳ reporting_context` |  `int`   
The reporting context the issue applies to.  
`↳ description` |  `string`   
A short issue description in English.  
`↳ detail` |  `string`   
A detailed issue description in English.  
`↳ documentation` |  `string`   
The URL of a web page to help with resolving this issue.  
`↳ applicable_countries` |  `string[]`   
List of country codes (ISO 3166-1 alpha-2) where issue applies to the offer.  
  
### getCode

The error code of the issue.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setCode

The error code of the issue.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSeverity

How this issue affects serving of the offer.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [Severity](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.ProductStatus.ItemLevelIssue.Severity).  
  
### setSeverity

How this issue affects serving of the offer.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [Severity](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-products/latest/V1beta.ProductStatus.ItemLevelIssue.Severity).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getResolution

Whether the issue can be resolved by the business.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setResolution

Whether the issue can be resolved by the business.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAttribute

The attribute's name, if the issue is caused by a single attribute.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setAttribute

The attribute's name, if the issue is caused by a single attribute.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getReportingContext

The reporting context the issue applies to.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [ReportingContextEnum](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.ReportingContext.ReportingContextEnum.html).  
  
### setReportingContext

The reporting context the issue applies to.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [ReportingContextEnum](https://docs.cloud.google.com/php/docs/reference/shopping-common-protos/latest/Type.ReportingContext.ReportingContextEnum.html).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

A short issue description in English.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

A short issue description in English.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDetail

A detailed issue description in English.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDetail

A detailed issue description in English.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDocumentation

The URL of a web page to help with resolving this issue.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDocumentation

The URL of a web page to help with resolving this issue.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getApplicableCountries

List of country codes (ISO 3166-1 alpha-2) where issue applies to the offer.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setApplicableCountries

List of country codes (ISO 3166-1 alpha-2) where issue applies to the offer.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
