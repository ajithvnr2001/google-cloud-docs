---
url: https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.Filter
title: Google Analytics Data V1alpha Client - Class Filter (0.28.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:17.675929+00:00
---

# Google Analytics Data V1alpha Client - Class Filter (0.28.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.Filter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Data V1alpha Client - Class Filter (0.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.28.0 (latest)  0.24.0  0.23.3  0.22.3  0.21.1  0.20.1  0.19.0  0.18.0  0.17.1  0.16.4  0.14.0  0.13.0  0.12.0  0.11.2  0.10.1  0.9.5 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Data V1alpha Client class Filter.

An expression to filter dimension or metric values.

Generated from protobuf message `google.analytics.data.v1alpha.Filter`

## Namespace

Google \ Analytics \ Data \ V1alpha

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ field_name` |  `string`   
The dimension name or metric name. Must be a name defined in dimensions or metrics.  
`↳ string_filter` |  `[StringFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.StringFilter)`   
Strings related filter.  
`↳ in_list_filter` |  `[InListFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.InListFilter)`   
A filter for in list values.  
`↳ numeric_filter` |  `[NumericFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.NumericFilter)`   
A filter for numeric or date values.  
`↳ between_filter` |  `[BetweenFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.BetweenFilter)`   
A filter for between two values.  
`↳ empty_filter` |  `[EmptyFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.EmptyFilter)`   
A filter for empty values such as "(not set)" and "" values.  
  
### getFieldName

The dimension name or metric name. Must be a name defined in dimensions or metrics.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFieldName

The dimension name or metric name. Must be a name defined in dimensions or metrics.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStringFilter

Strings related filter.

**Returns**  
---  
**Type** | **Description**  
`[StringFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.StringFilter)|null` |   
  
### hasStringFilter

### setStringFilter

Strings related filter.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[StringFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.StringFilter)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getInListFilter

A filter for in list values.

**Returns**  
---  
**Type** | **Description**  
`[InListFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.InListFilter)|null` |   
  
### hasInListFilter

### setInListFilter

A filter for in list values.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[InListFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.InListFilter)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNumericFilter

A filter for numeric or date values.

**Returns**  
---  
**Type** | **Description**  
`[NumericFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.NumericFilter)|null` |   
  
### hasNumericFilter

### setNumericFilter

A filter for numeric or date values.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[NumericFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.NumericFilter)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBetweenFilter

A filter for between two values.

**Returns**  
---  
**Type** | **Description**  
`[BetweenFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.BetweenFilter)|null` |   
  
### hasBetweenFilter

### setBetweenFilter

A filter for between two values.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[BetweenFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.BetweenFilter)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEmptyFilter

A filter for empty values such as "(not set)" and "" values.

**Returns**  
---  
**Type** | **Description**  
`[EmptyFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.EmptyFilter)|null` |   
  
### hasEmptyFilter

### setEmptyFilter

A filter for empty values such as "(not set)" and "" values.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[EmptyFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.EmptyFilter)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOneFilter

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
