---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ExpandedDataSet
title: Google Analytics Admin V1alpha Client - Class ExpandedDataSet (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:06.611450+00:00
---

# Google Analytics Admin V1alpha Client - Class ExpandedDataSet (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ExpandedDataSet

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class ExpandedDataSet (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class ExpandedDataSet.

A resource message representing an `ExpandedDataSet`.

Generated from protobuf message `google.analytics.admin.v1alpha.ExpandedDataSet`

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
`↳ name` |  `string`   
Output only. The resource name for this ExpandedDataSet resource. Format: properties/{property_id}/expandedDataSets/{expanded_data_set}  
`↳ display_name` |  `string`   
Required. The display name of the ExpandedDataSet. Max 200 chars.  
`↳ description` |  `string`   
Optional. The description of the ExpandedDataSet. Max 50 chars.  
`↳ dimension_names` |  `string[]`   
Immutable. The list of dimensions included in the ExpandedDataSet. See the [API Dimensions](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#dimensions) for the list of dimension names.  
`↳ metric_names` |  `string[]`   
Immutable. The list of metrics included in the ExpandedDataSet. See the [API Metrics](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#metrics) for the list of dimension names.  
`↳ dimension_filter_expression` |  `[ExpandedDataSetFilterExpression](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ExpandedDataSetFilterExpression)`   
Immutable. A logical expression of ExpandedDataSet filters applied to dimension included in the ExpandedDataSet. This filter is used to reduce the number of rows and thus the chance of encountering `other` row.  
`↳ data_collection_start_time` |  `Google\Protobuf\Timestamp`   
Output only. Time when expanded data set began (or will begin) collecing data.  
  
### getName

Output only. The resource name for this ExpandedDataSet resource.

Format: properties/{property_id}/expandedDataSets/{expanded_data_set}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. The resource name for this ExpandedDataSet resource.

Format: properties/{property_id}/expandedDataSets/{expanded_data_set}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisplayName

Required. The display name of the ExpandedDataSet.

Max 200 chars.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDisplayName

Required. The display name of the ExpandedDataSet.

Max 200 chars.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

Optional. The description of the ExpandedDataSet.

Max 50 chars.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

Optional. The description of the ExpandedDataSet.

Max 50 chars.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDimensionNames

Immutable. The list of dimensions included in the ExpandedDataSet.

See the [API Dimensions](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#dimensions) for the list of dimension names.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setDimensionNames

Immutable. The list of dimensions included in the ExpandedDataSet.

See the [API Dimensions](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#dimensions) for the list of dimension names.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMetricNames

Immutable. The list of metrics included in the ExpandedDataSet.

See the [API Metrics](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#metrics) for the list of dimension names.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setMetricNames

Immutable. The list of metrics included in the ExpandedDataSet.

See the [API Metrics](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#metrics) for the list of dimension names.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDimensionFilterExpression

Immutable. A logical expression of ExpandedDataSet filters applied to dimension included in the ExpandedDataSet. This filter is used to reduce the number of rows and thus the chance of encountering `other` row.

**Returns**  
---  
**Type** | **Description**  
`[ExpandedDataSetFilterExpression](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ExpandedDataSetFilterExpression)|null` |   
  
### hasDimensionFilterExpression

### clearDimensionFilterExpression

### setDimensionFilterExpression

Immutable. A logical expression of ExpandedDataSet filters applied to dimension included in the ExpandedDataSet. This filter is used to reduce the number of rows and thus the chance of encountering `other` row.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ExpandedDataSetFilterExpression](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.ExpandedDataSetFilterExpression)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDataCollectionStartTime

Output only. Time when expanded data set began (or will begin) collecing data.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasDataCollectionStartTime

### clearDataCollectionStartTime

### setDataCollectionStartTime

Output only. Time when expanded data set began (or will begin) collecing data.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
