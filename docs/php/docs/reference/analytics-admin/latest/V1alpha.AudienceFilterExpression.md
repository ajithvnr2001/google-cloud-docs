---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterExpression
title: Google Analytics Admin V1alpha Client - Class AudienceFilterExpression (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:54:51.375386+00:00
---

# Google Analytics Admin V1alpha Client - Class AudienceFilterExpression (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterExpression

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class AudienceFilterExpression (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class AudienceFilterExpression.

A logical expression of Audience dimension, metric, or event filters.

Generated from protobuf message `google.analytics.admin.v1alpha.AudienceFilterExpression`

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
`↳ and_group` |  `[AudienceFilterExpressionList](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterExpressionList)`   
A list of expressions to be AND’ed together. It can only contain AudienceFilterExpressions with or_group. This must be set for the top level AudienceFilterExpression.  
`↳ or_group` |  `[AudienceFilterExpressionList](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterExpressionList)`   
A list of expressions to OR’ed together. It cannot contain AudienceFilterExpressions with and_group or or_group.  
`↳ not_expression` |  `[AudienceFilterExpression](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterExpression)`   
A filter expression to be NOT'ed (For example, inverted, complemented). It can only include a dimension_or_metric_filter. This cannot be set on the top level AudienceFilterExpression.  
`↳ dimension_or_metric_filter` |  `[AudienceDimensionOrMetricFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter)`   
A filter on a single dimension or metric. This cannot be set on the top level AudienceFilterExpression.  
`↳ event_filter` |  `[AudienceEventFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceEventFilter)`   
Creates a filter that matches a specific event. This cannot be set on the top level AudienceFilterExpression.  
  
### getAndGroup

A list of expressions to be AND’ed together. It can only contain AudienceFilterExpressions with or_group. This must be set for the top level AudienceFilterExpression.

**Returns**  
---  
**Type** | **Description**  
`[AudienceFilterExpressionList](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterExpressionList)|null` |   
  
### hasAndGroup

### setAndGroup

A list of expressions to be AND’ed together. It can only contain AudienceFilterExpressions with or_group. This must be set for the top level AudienceFilterExpression.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AudienceFilterExpressionList](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterExpressionList)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOrGroup

A list of expressions to OR’ed together. It cannot contain AudienceFilterExpressions with and_group or or_group.

**Returns**  
---  
**Type** | **Description**  
`[AudienceFilterExpressionList](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterExpressionList)|null` |   
  
### hasOrGroup

### setOrGroup

A list of expressions to OR’ed together. It cannot contain AudienceFilterExpressions with and_group or or_group.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AudienceFilterExpressionList](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterExpressionList)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNotExpression

A filter expression to be NOT'ed (For example, inverted, complemented).

It can only include a dimension_or_metric_filter. This cannot be set on the top level AudienceFilterExpression.

**Returns**  
---  
**Type** | **Description**  
`[AudienceFilterExpression](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterExpression)|null` |   
  
### hasNotExpression

### setNotExpression

A filter expression to be NOT'ed (For example, inverted, complemented).

It can only include a dimension_or_metric_filter. This cannot be set on the top level AudienceFilterExpression.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AudienceFilterExpression](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceFilterExpression)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDimensionOrMetricFilter

A filter on a single dimension or metric. This cannot be set on the top level AudienceFilterExpression.

**Returns**  
---  
**Type** | **Description**  
`[AudienceDimensionOrMetricFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter)|null` |   
  
### hasDimensionOrMetricFilter

### setDimensionOrMetricFilter

A filter on a single dimension or metric. This cannot be set on the top level AudienceFilterExpression.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AudienceDimensionOrMetricFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceDimensionOrMetricFilter)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEventFilter

Creates a filter that matches a specific event. This cannot be set on the top level AudienceFilterExpression.

**Returns**  
---  
**Type** | **Description**  
`[AudienceEventFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceEventFilter)|null` |   
  
### hasEventFilter

### setEventFilter

Creates a filter that matches a specific event. This cannot be set on the top level AudienceFilterExpression.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AudienceEventFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.AudienceEventFilter)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExpr

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
