---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroupFilterExpression
title: Google Analytics Admin V1alpha Client - Class ChannelGroupFilterExpression (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:54:54.291498+00:00
---

# Google Analytics Admin V1alpha Client - Class ChannelGroupFilterExpression (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroupFilterExpression

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class ChannelGroupFilterExpression (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class ChannelGroupFilterExpression.

A logical expression of Channel Group dimension filters.

Generated from protobuf message `google.analytics.admin.v1alpha.ChannelGroupFilterExpression`

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
`↳ and_group` |  `[ChannelGroupFilterExpressionList](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroupFilterExpressionList)`   
A list of expressions to be AND’ed together. It can only contain ChannelGroupFilterExpressions with or_group. This must be set for the top level ChannelGroupFilterExpression.  
`↳ or_group` |  `[ChannelGroupFilterExpressionList](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroupFilterExpressionList)`   
A list of expressions to OR’ed together. It cannot contain ChannelGroupFilterExpressions with and_group or or_group.  
`↳ not_expression` |  `[ChannelGroupFilterExpression](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroupFilterExpression)`   
A filter expression to be NOT'ed (that is inverted, complemented). It can only include a dimension_or_metric_filter. This cannot be set on the top level ChannelGroupFilterExpression.  
`↳ filter` |  `[ChannelGroupFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroupFilter)`   
A filter on a single dimension. This cannot be set on the top level ChannelGroupFilterExpression.  
  
### getAndGroup

A list of expressions to be AND’ed together. It can only contain ChannelGroupFilterExpressions with or_group. This must be set for the top level ChannelGroupFilterExpression.

**Returns**  
---  
**Type** | **Description**  
`[ChannelGroupFilterExpressionList](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroupFilterExpressionList)|null` |   
  
### hasAndGroup

### setAndGroup

A list of expressions to be AND’ed together. It can only contain ChannelGroupFilterExpressions with or_group. This must be set for the top level ChannelGroupFilterExpression.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ChannelGroupFilterExpressionList](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroupFilterExpressionList)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOrGroup

A list of expressions to OR’ed together. It cannot contain ChannelGroupFilterExpressions with and_group or or_group.

**Returns**  
---  
**Type** | **Description**  
`[ChannelGroupFilterExpressionList](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroupFilterExpressionList)|null` |   
  
### hasOrGroup

### setOrGroup

A list of expressions to OR’ed together. It cannot contain ChannelGroupFilterExpressions with and_group or or_group.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ChannelGroupFilterExpressionList](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroupFilterExpressionList)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNotExpression

A filter expression to be NOT'ed (that is inverted, complemented). It can only include a dimension_or_metric_filter. This cannot be set on the top level ChannelGroupFilterExpression.

**Returns**  
---  
**Type** | **Description**  
`[ChannelGroupFilterExpression](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroupFilterExpression)|null` |   
  
### hasNotExpression

### setNotExpression

A filter expression to be NOT'ed (that is inverted, complemented). It can only include a dimension_or_metric_filter. This cannot be set on the top level ChannelGroupFilterExpression.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ChannelGroupFilterExpression](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroupFilterExpression)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFilter

A filter on a single dimension. This cannot be set on the top level ChannelGroupFilterExpression.

**Returns**  
---  
**Type** | **Description**  
`[ChannelGroupFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroupFilter)|null` |   
  
### hasFilter

### setFilter

A filter on a single dimension. This cannot be set on the top level ChannelGroupFilterExpression.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ChannelGroupFilter](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ChannelGroupFilter)`   
  
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
