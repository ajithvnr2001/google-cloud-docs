---
url: https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.SegmentParameterFilter
title: Google Analytics Data V1alpha Client - Class SegmentParameterFilter (0.28.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:08.515552+00:00
---

# Google Analytics Data V1alpha Client - Class SegmentParameterFilter (0.28.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.SegmentParameterFilter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Data V1alpha Client - Class SegmentParameterFilter (0.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.28.0 (latest)  0.24.0  0.23.3  0.22.3  0.21.1  0.20.1  0.19.0  0.18.0  0.17.1  0.16.4  0.14.0  0.13.0  0.12.0  0.11.2  0.10.1  0.9.5 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Data V1alpha Client class SegmentParameterFilter.

An expression to filter parameter values in a segment.

Generated from protobuf message `google.analytics.data.v1alpha.SegmentParameterFilter`

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
`↳ event_parameter_name` |  `string`   
This filter will be evaluated on the specified event parameter. Event parameters are logged as parameters of the event. Event parameters include fields like "firebase_screen" & "currency". Event parameters can only be used in segments & funnels and can only be used in a descendent filter from an EventFilter. In a descendent filter from an EventFilter either event or item parameters should be used.  
`↳ item_parameter_name` |  `string`   
This filter will be evaluated on the specified item parameter. Item parameters are logged as parameters in the item array. Item parameters include fields like "item_name" & "item_category". Item parameters can only be used in segments & funnels and can only be used in a descendent filter from an EventFilter. In a descendent filter from an EventFilter either event or item parameters should be used. Item parameters are only available in ecommerce events. To learn more about ecommerce events, see the [Measure ecommerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce) guide.  
`↳ string_filter` |  `[StringFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.StringFilter)`   
Strings related filter.  
`↳ in_list_filter` |  `[InListFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.InListFilter)`   
A filter for in list values.  
`↳ numeric_filter` |  `[NumericFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.NumericFilter)`   
A filter for numeric or date values.  
`↳ between_filter` |  `[BetweenFilter](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.BetweenFilter)`   
A filter for between two values.  
`↳ filter_scoping` |  `[SegmentParameterFilterScoping](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.SegmentParameterFilterScoping)`   
Specifies the scope for the filter.  
  
### getEventParameterName

This filter will be evaluated on the specified event parameter. Event parameters are logged as parameters of the event. Event parameters include fields like "firebase_screen" & "currency".

Event parameters can only be used in segments & funnels and can only be used in a descendent filter from an EventFilter. In a descendent filter from an EventFilter either event or item parameters should be used.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasEventParameterName

### setEventParameterName

This filter will be evaluated on the specified event parameter. Event parameters are logged as parameters of the event. Event parameters include fields like "firebase_screen" & "currency".

Event parameters can only be used in segments & funnels and can only be used in a descendent filter from an EventFilter. In a descendent filter from an EventFilter either event or item parameters should be used.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getItemParameterName

This filter will be evaluated on the specified item parameter. Item parameters are logged as parameters in the item array. Item parameters include fields like "item_name" & "item_category".

Item parameters can only be used in segments & funnels and can only be used in a descendent filter from an EventFilter. In a descendent filter from an EventFilter either event or item parameters should be used. Item parameters are only available in ecommerce events. To learn more about ecommerce events, see the [Measure ecommerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce) guide.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasItemParameterName

### setItemParameterName

This filter will be evaluated on the specified item parameter. Item parameters are logged as parameters in the item array. Item parameters include fields like "item_name" & "item_category".

Item parameters can only be used in segments & funnels and can only be used in a descendent filter from an EventFilter. In a descendent filter from an EventFilter either event or item parameters should be used. Item parameters are only available in ecommerce events. To learn more about ecommerce events, see the [Measure ecommerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce) guide.

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
  
### getFilterScoping

Specifies the scope for the filter.

**Returns**  
---  
**Type** | **Description**  
`[SegmentParameterFilterScoping](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.SegmentParameterFilterScoping)|null` |   
  
### hasFilterScoping

### clearFilterScoping

### setFilterScoping

Specifies the scope for the filter.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[SegmentParameterFilterScoping](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.SegmentParameterFilterScoping)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOneParameter

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### getOneFilter

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
