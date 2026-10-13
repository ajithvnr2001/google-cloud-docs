---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BigQueryLink
title: Google Analytics Admin V1alpha Client - Class BigQueryLink (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:54:52.970808+00:00
---

# Google Analytics Admin V1alpha Client - Class BigQueryLink (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.BigQueryLink

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class BigQueryLink (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class BigQueryLink.

A link between a Google Analytics property and BigQuery project.

Generated from protobuf message `google.analytics.admin.v1alpha.BigQueryLink`

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
Output only. Resource name of this BigQuery link. Format: 'properties/{property_id}/bigQueryLinks/{bigquery_link_id}' Format: 'properties/1234/bigQueryLinks/abc567'  
`↳ project` |  `string`   
Immutable. The linked Google Cloud project. When creating a BigQueryLink, you may provide this resource name using either a project number or project ID. Once this resource has been created, the returned project will always have a project that contains a project number. Format: 'projects/{project number}' Example: 'projects/1234'  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. Time when the link was created.  
`↳ daily_export_enabled` |  `bool`   
If set true, enables daily data export to the linked Google Cloud project.  
`↳ streaming_export_enabled` |  `bool`   
If set true, enables streaming export to the linked Google Cloud project.  
`↳ fresh_daily_export_enabled` |  `bool`   
If set true, enables fresh daily export to the linked Google Cloud project.  
`↳ include_advertising_id` |  `bool`   
If set true, exported data will include advertising identifiers for mobile app streams.  
`↳ export_streams` |  `string[]`   
The list of streams under the parent property for which data will be exported. Format: properties/{property_id}/dataStreams/{stream_id} Example: ['properties/1000/dataStreams/2000']  
`↳ excluded_events` |  `string[]`   
The list of event names that will be excluded from exports.  
`↳ dataset_location` |  `string`   
Required. Immutable. The geographic location where the created BigQuery dataset should reside. See <https://cloud.google.com/bigquery/docs/locations> for supported locations.  
  
### getName

Output only. Resource name of this BigQuery link.

Format: 'properties/{property_id}/bigQueryLinks/{bigquery_link_id}' Format: 'properties/1234/bigQueryLinks/abc567'

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. Resource name of this BigQuery link.

Format: 'properties/{property_id}/bigQueryLinks/{bigquery_link_id}' Format: 'properties/1234/bigQueryLinks/abc567'

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProject

Immutable. The linked Google Cloud project. When creating a BigQueryLink, you may provide this resource name using either a project number or project ID. Once this resource has been created, the returned project will always have a project that contains a project number.

Format: 'projects/{project number}' Example: 'projects/1234'

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setProject

Immutable. The linked Google Cloud project. When creating a BigQueryLink, you may provide this resource name using either a project number or project ID. Once this resource has been created, the returned project will always have a project that contains a project number.

Format: 'projects/{project number}' Example: 'projects/1234'

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. Time when the link was created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. Time when the link was created.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDailyExportEnabled

If set true, enables daily data export to the linked Google Cloud project.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setDailyExportEnabled

If set true, enables daily data export to the linked Google Cloud project.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStreamingExportEnabled

If set true, enables streaming export to the linked Google Cloud project.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setStreamingExportEnabled

If set true, enables streaming export to the linked Google Cloud project.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFreshDailyExportEnabled

If set true, enables fresh daily export to the linked Google Cloud project.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setFreshDailyExportEnabled

If set true, enables fresh daily export to the linked Google Cloud project.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getIncludeAdvertisingId

If set true, exported data will include advertising identifiers for mobile app streams.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setIncludeAdvertisingId

If set true, exported data will include advertising identifiers for mobile app streams.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExportStreams

The list of streams under the parent property for which data will be exported.

Format: properties/{property_id}/dataStreams/{stream_id} Example: ['properties/1000/dataStreams/2000']

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setExportStreams

The list of streams under the parent property for which data will be exported.

Format: properties/{property_id}/dataStreams/{stream_id} Example: ['properties/1000/dataStreams/2000']

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExcludedEvents

The list of event names that will be excluded from exports.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setExcludedEvents

The list of event names that will be excluded from exports.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDatasetLocation

Required. Immutable. The geographic location where the created BigQuery dataset should reside. See <https://cloud.google.com/bigquery/docs/locations> for supported locations.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDatasetLocation

Required. Immutable. The geographic location where the created BigQuery dataset should reside. See <https://cloud.google.com/bigquery/docs/locations> for supported locations.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
