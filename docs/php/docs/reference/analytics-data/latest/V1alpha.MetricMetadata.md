---
url: https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.MetricMetadata
title: Google Analytics Data V1alpha Client - Class MetricMetadata (0.28.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:10.932071+00:00
---

# Google Analytics Data V1alpha Client - Class MetricMetadata (0.28.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.MetricMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Data V1alpha Client - Class MetricMetadata (0.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.28.0 (latest)  0.24.0  0.23.3  0.22.3  0.21.1  0.20.1  0.19.0  0.18.0  0.17.1  0.16.4  0.14.0  0.13.0  0.12.0  0.11.2  0.10.1  0.9.5 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Data V1alpha Client class MetricMetadata.

Explains a metric.

Generated from protobuf message `google.analytics.data.v1alpha.MetricMetadata`

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
`↳ api_name` |  `string`   
A metric name. Usable in Metric's `name`. For example, `eventCount`.  
`↳ ui_name` |  `string`   
This metric's name within the Google Analytics user interface. For example, `Event count`.  
`↳ description` |  `string`   
Description of how this metric is used and calculated.  
`↳ deprecated_api_names` |  `string[]`   
Still usable but deprecated names for this metric. If populated, this metric is available by either `apiName` or one of `deprecatedApiNames` for a period of time. After the deprecation period, the metric will be available only by `apiName`.  
`↳ type` |  `int`   
The type of this metric.  
`↳ expression` |  `string`   
The mathematical expression for this derived metric. Can be used in Metric's `expression` field for equivalent reports. Most metrics are not expressions, and for non-expressions, this field is empty.  
`↳ custom_definition` |  `bool`   
True if the metric is a custom metric for this property.  
`↳ blocked_reasons` |  `int[]`   
If reasons are specified, your access is blocked to this metric for this property. API requests from you to this property for this metric will succeed; however, the report will contain only zeros for this metric. API requests with metric filters on blocked metrics will fail. If reasons are empty, you have access to this metric. To learn more, see [Access and data-restriction management](https://support.google.com/analytics/answer/10851388).  
`↳ category` |  `string`   
The display name of the category that this metrics belongs to. Similar dimensions and metrics are categorized together.  
`↳ sections` |  `int[]`   
Specifies the Google Analytics sections this metric applies to.  
  
### getApiName

A metric name. Usable in Metric's `name`. For example, `eventCount`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setApiName

A metric name. Usable in Metric's `name`. For example, `eventCount`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUiName

This metric's name within the Google Analytics user interface. For example, `Event count`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setUiName

This metric's name within the Google Analytics user interface. For example, `Event count`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

Description of how this metric is used and calculated.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

Description of how this metric is used and calculated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDeprecatedApiNames

Still usable but deprecated names for this metric. If populated, this metric is available by either `apiName` or one of `deprecatedApiNames` for a period of time. After the deprecation period, the metric will be available only by `apiName`.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setDeprecatedApiNames

Still usable but deprecated names for this metric. If populated, this metric is available by either `apiName` or one of `deprecatedApiNames` for a period of time. After the deprecation period, the metric will be available only by `apiName`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getType

The type of this metric.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [MetricType](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.MetricType).  
  
### setType

The type of this metric.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [MetricType](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1alpha.MetricType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExpression

The mathematical expression for this derived metric. Can be used in Metric's `expression` field for equivalent reports. Most metrics are not expressions, and for non-expressions, this field is empty.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setExpression

The mathematical expression for this derived metric. Can be used in Metric's `expression` field for equivalent reports. Most metrics are not expressions, and for non-expressions, this field is empty.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCustomDefinition

True if the metric is a custom metric for this property.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setCustomDefinition

True if the metric is a custom metric for this property.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBlockedReasons

If reasons are specified, your access is blocked to this metric for this property. API requests from you to this property for this metric will succeed; however, the report will contain only zeros for this metric. API requests with metric filters on blocked metrics will fail. If reasons are empty, you have access to this metric.

To learn more, see [Access and data-restriction management](https://support.google.com/analytics/answer/10851388).

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<int>` |   
  
### setBlockedReasons

If reasons are specified, your access is blocked to this metric for this property. API requests from you to this property for this metric will succeed; however, the report will contain only zeros for this metric. API requests with metric filters on blocked metrics will fail. If reasons are empty, you have access to this metric.

To learn more, see [Access and data-restriction management](https://support.google.com/analytics/answer/10851388).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCategory

The display name of the category that this metrics belongs to. Similar dimensions and metrics are categorized together.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setCategory

The display name of the category that this metrics belongs to. Similar dimensions and metrics are categorized together.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSections

Specifies the Google Analytics sections this metric applies to.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<int>` |   
  
### setSections

Specifies the Google Analytics sections this metric applies to.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
