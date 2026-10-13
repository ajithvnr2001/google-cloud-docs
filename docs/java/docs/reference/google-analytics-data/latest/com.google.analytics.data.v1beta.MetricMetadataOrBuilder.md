---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.MetricMetadataOrBuilder
title: Interface MetricMetadataOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:11:32.815549+00:00
---

# Interface MetricMetadataOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.MetricMetadataOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MetricMetadataOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 
    
    
    public interface MetricMetadataOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getApiName()
    
    
    public abstract String getApiName()

A metric name. Useable in Metric's `name`. For example, `eventCount`.

`string api_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The apiName.  
  
### getApiNameBytes()
    
    
    public abstract ByteString getApiNameBytes()

A metric name. Useable in Metric's `name`. For example, `eventCount`.

`string api_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for apiName.  
  
### getBlockedReasons(int index)
    
    
    public abstract MetricMetadata.BlockedReason getBlockedReasons(int index)

If reasons are specified, your access is blocked to this metric for this property. API requests from you to this property for this metric will succeed; however, the report will contain only zeros for this metric. API requests with metric filters on blocked metrics will fail. If reasons are empty, you have access to this metric.

To learn more, see [Access and data-restriction management](https://support.google.com/analytics/answer/10851388).

`repeated .google.analytics.data.v1beta.MetricMetadata.BlockedReason blocked_reasons = 8; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[MetricMetadata.BlockedReason](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.MetricMetadata.BlockedReason)` | The blockedReasons at the given index.  
  
### getBlockedReasonsCount()
    
    
    public abstract int getBlockedReasonsCount()

If reasons are specified, your access is blocked to this metric for this property. API requests from you to this property for this metric will succeed; however, the report will contain only zeros for this metric. API requests with metric filters on blocked metrics will fail. If reasons are empty, you have access to this metric.

To learn more, see [Access and data-restriction management](https://support.google.com/analytics/answer/10851388).

`repeated .google.analytics.data.v1beta.MetricMetadata.BlockedReason blocked_reasons = 8; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of blockedReasons.  
  
### getBlockedReasonsList()
    
    
    public abstract List<MetricMetadata.BlockedReason> getBlockedReasonsList()

If reasons are specified, your access is blocked to this metric for this property. API requests from you to this property for this metric will succeed; however, the report will contain only zeros for this metric. API requests with metric filters on blocked metrics will fail. If reasons are empty, you have access to this metric.

To learn more, see [Access and data-restriction management](https://support.google.com/analytics/answer/10851388).

`repeated .google.analytics.data.v1beta.MetricMetadata.BlockedReason blocked_reasons = 8; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[BlockedReason](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.MetricMetadata.BlockedReason)>` | A list containing the blockedReasons.  
  
### getBlockedReasonsValue(int index)
    
    
    public abstract int getBlockedReasonsValue(int index)

If reasons are specified, your access is blocked to this metric for this property. API requests from you to this property for this metric will succeed; however, the report will contain only zeros for this metric. API requests with metric filters on blocked metrics will fail. If reasons are empty, you have access to this metric.

To learn more, see [Access and data-restriction management](https://support.google.com/analytics/answer/10851388).

`repeated .google.analytics.data.v1beta.MetricMetadata.BlockedReason blocked_reasons = 8; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of blockedReasons at the given index.  
  
### getBlockedReasonsValueList()
    
    
    public abstract List<Integer> getBlockedReasonsValueList()

If reasons are specified, your access is blocked to this metric for this property. API requests from you to this property for this metric will succeed; however, the report will contain only zeros for this metric. API requests with metric filters on blocked metrics will fail. If reasons are empty, you have access to this metric.

To learn more, see [Access and data-restriction management](https://support.google.com/analytics/answer/10851388).

`repeated .google.analytics.data.v1beta.MetricMetadata.BlockedReason blocked_reasons = 8; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for blockedReasons.  
  
### getCategory()
    
    
    public abstract String getCategory()

The display name of the category that this metrics belongs to. Similar dimensions and metrics are categorized together.

`string category = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The category.  
  
### getCategoryBytes()
    
    
    public abstract ByteString getCategoryBytes()

The display name of the category that this metrics belongs to. Similar dimensions and metrics are categorized together.

`string category = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for category.  
  
### getCustomDefinition()
    
    
    public abstract boolean getCustomDefinition()

True if the metric is a custom metric for this property.

`bool custom_definition = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The customDefinition.  
  
### getDeprecatedApiNames(int index)
    
    
    public abstract String getDeprecatedApiNames(int index)

Still usable but deprecated names for this metric. If populated, this metric is available by either `apiName` or one of `deprecatedApiNames` for a period of time. After the deprecation period, the metric will be available only by `apiName`.

`repeated string deprecated_api_names = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The deprecatedApiNames at the given index.  
  
### getDeprecatedApiNamesBytes(int index)
    
    
    public abstract ByteString getDeprecatedApiNamesBytes(int index)

Still usable but deprecated names for this metric. If populated, this metric is available by either `apiName` or one of `deprecatedApiNames` for a period of time. After the deprecation period, the metric will be available only by `apiName`.

`repeated string deprecated_api_names = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the deprecatedApiNames at the given index.  
  
### getDeprecatedApiNamesCount()
    
    
    public abstract int getDeprecatedApiNamesCount()

Still usable but deprecated names for this metric. If populated, this metric is available by either `apiName` or one of `deprecatedApiNames` for a period of time. After the deprecation period, the metric will be available only by `apiName`.

`repeated string deprecated_api_names = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of deprecatedApiNames.  
  
### getDeprecatedApiNamesList()
    
    
    public abstract List<String> getDeprecatedApiNamesList()

Still usable but deprecated names for this metric. If populated, this metric is available by either `apiName` or one of `deprecatedApiNames` for a period of time. After the deprecation period, the metric will be available only by `apiName`.

`repeated string deprecated_api_names = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the deprecatedApiNames.  
  
### getDescription()
    
    
    public abstract String getDescription()

Description of how this metric is used and calculated.

`string description = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Description of how this metric is used and calculated.

`string description = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getExpression()
    
    
    public abstract String getExpression()

The mathematical expression for this derived metric. Can be used in Metric's `expression` field for equivalent reports. Most metrics are not expressions, and for non-expressions, this field is empty.

`string expression = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The expression.  
  
### getExpressionBytes()
    
    
    public abstract ByteString getExpressionBytes()

The mathematical expression for this derived metric. Can be used in Metric's `expression` field for equivalent reports. Most metrics are not expressions, and for non-expressions, this field is empty.

`string expression = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for expression.  
  
### getType()
    
    
    public abstract MetricType getType()

The type of this metric.

`.google.analytics.data.v1beta.MetricType type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[MetricType](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.MetricType)` | The type.  
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

The type of this metric.

`.google.analytics.data.v1beta.MetricType type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### getUiName()
    
    
    public abstract String getUiName()

This metric's name within the Google Analytics user interface. For example, `Event count`.

`string ui_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uiName.  
  
### getUiNameBytes()
    
    
    public abstract ByteString getUiNameBytes()

This metric's name within the Google Analytics user interface. For example, `Event count`.

`string ui_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uiName.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
