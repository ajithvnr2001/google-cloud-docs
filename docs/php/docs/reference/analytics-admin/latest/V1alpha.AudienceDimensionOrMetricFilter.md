---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter
title: Google Analytics Admin V1alpha Client - Class AudienceDimensionOrMetricFilter (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:54:49.792222+00:00
---

# Google Analytics Admin V1alpha Client - Class AudienceDimensionOrMetricFilter (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class AudienceDimensionOrMetricFilter (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class AudienceDimensionOrMetricFilter.

A specific filter for a single dimension or metric.

Generated from protobuf message `google.analytics.admin.v1alpha.AudienceDimensionOrMetricFilter`

## Namespace

Google \ Analytics \ Admin \ V1alpha

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ string_filter` |  `[AudienceDimensionOrMetricFilter\StringFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter.StringFilter)`   
A filter for a string-type dimension that matches a particular pattern.  
`↳ in_list_filter` |  `[AudienceDimensionOrMetricFilter\InListFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter.InListFilter)`   
A filter for a string dimension that matches a particular list of options.  
`↳ numeric_filter` |  `[AudienceDimensionOrMetricFilter\NumericFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter.NumericFilter)`   
A filter for numeric or date values on a dimension or metric.  
`↳ between_filter` |  `[AudienceDimensionOrMetricFilter\BetweenFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter.BetweenFilter)`   
A filter for numeric or date values between certain values on a dimension or metric.  
`↳ field_name` |  `string`   
Required. Immutable. The dimension name or metric name to filter. If the field name refers to a custom dimension or metric, a scope prefix will be added to the front of the custom dimensions or metric name. For more on scope prefixes or custom dimensions/metrics, reference the [Google Analytics Data API documentation](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#custom_dimensions).  
`↳ at_any_point_in_time` |  `bool`   
Optional. Indicates whether this filter needs dynamic evaluation or not. If set to true, users join the Audience if they ever met the condition (static evaluation). If unset or set to false, user evaluation for an Audience is dynamic; users are added to an Audience when they meet the conditions and then removed when they no longer meet them. This can only be set when Audience scope is ACROSS_ALL_SESSIONS.  
`↳ in_any_n_day_period` |  `int`   
Optional. If set, specifies the time window for which to evaluate data in number of days. If not set, then audience data is evaluated against lifetime data (For example, infinite time window). For example, if set to 1 day, only the current day's data is evaluated. The reference point is the current day when at_any_point_in_time is unset or false. It can only be set when Audience scope is ACROSS_ALL_SESSIONS and cannot be greater than 60 days.  
  
### getStringFilter

A filter for a string-type dimension that matches a particular pattern.

**Returns**  
---  
**Type** | **Description**  
`[AudienceDimensionOrMetricFilter\StringFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter.StringFilter)|null` |   
  
### hasStringFilter

### setStringFilter

A filter for a string-type dimension that matches a particular pattern.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AudienceDimensionOrMetricFilter\StringFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter.StringFilter)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getInListFilter

A filter for a string dimension that matches a particular list of options.

**Returns**  
---  
**Type** | **Description**  
`[AudienceDimensionOrMetricFilter\InListFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter.InListFilter)|null` |   
  
### hasInListFilter

### setInListFilter

A filter for a string dimension that matches a particular list of options.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AudienceDimensionOrMetricFilter\InListFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter.InListFilter)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNumericFilter

A filter for numeric or date values on a dimension or metric.

**Returns**  
---  
**Type** | **Description**  
`[AudienceDimensionOrMetricFilter\NumericFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter.NumericFilter)|null` |   
  
### hasNumericFilter

### setNumericFilter

A filter for numeric or date values on a dimension or metric.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AudienceDimensionOrMetricFilter\NumericFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter.NumericFilter)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBetweenFilter

A filter for numeric or date values between certain values on a dimension or metric.

**Returns**  
---  
**Type** | **Description**  
`[AudienceDimensionOrMetricFilter\BetweenFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter.BetweenFilter)|null` |   
  
### hasBetweenFilter

### setBetweenFilter

A filter for numeric or date values between certain values on a dimension or metric.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AudienceDimensionOrMetricFilter\BetweenFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter.BetweenFilter)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFieldName

Required. Immutable. The dimension name or metric name to filter. If the field name refers to a custom dimension or metric, a scope prefix will be added to the front of the custom dimensions or metric name. For more on scope prefixes or custom dimensions/metrics, reference the [Google Analytics Data API documentation](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#custom_dimensions).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFieldName

Required. Immutable. The dimension name or metric name to filter. If the field name refers to a custom dimension or metric, a scope prefix will be added to the front of the custom dimensions or metric name. For more on scope prefixes or custom dimensions/metrics, reference the [Google Analytics Data API documentation](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#custom_dimensions).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAtAnyPointInTime

Optional. Indicates whether this filter needs dynamic evaluation or not. If set to true, users join the Audience if they ever met the condition (static evaluation). If unset or set to false, user evaluation for an Audience is dynamic; users are added to an Audience when they meet the conditions and then removed when they no longer meet them.

This can only be set when Audience scope is ACROSS_ALL_SESSIONS.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setAtAnyPointInTime

Optional. Indicates whether this filter needs dynamic evaluation or not. If set to true, users join the Audience if they ever met the condition (static evaluation). If unset or set to false, user evaluation for an Audience is dynamic; users are added to an Audience when they meet the conditions and then removed when they no longer meet them.

This can only be set when Audience scope is ACROSS_ALL_SESSIONS.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getInAnyNDayPeriod

Optional. If set, specifies the time window for which to evaluate data in number of days. If not set, then audience data is evaluated against lifetime data (For example, infinite time window).

For example, if set to 1 day, only the current day's data is evaluated. The reference point is the current day when at_any_point_in_time is unset or false. It can only be set when Audience scope is ACROSS_ALL_SESSIONS and cannot be greater than 60 days.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setInAnyNDayPeriod

Optional. If set, specifies the time window for which to evaluate data in number of days. If not set, then audience data is evaluated against lifetime data (For example, infinite time window).

For example, if set to 1 day, only the current day's data is evaluated. The reference point is the current day when at_any_point_in_time is unset or false. It can only be set when Audience scope is ACROSS_ALL_SESSIONS and cannot be greater than 60 days.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
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
