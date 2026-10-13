---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream
title: Google Analytics Admin V1alpha Client - Class DataStream (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:01.473977+00:00
---

# Google Analytics Admin V1alpha Client - Class DataStream (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class DataStream (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class DataStream.

A resource message representing a data stream.

Generated from protobuf message `google.analytics.admin.v1alpha.DataStream`

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
`↳ web_stream_data` |  `[DataStream\WebStreamData](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream.WebStreamData)`   
Data specific to web streams. Must be populated if type is WEB_DATA_STREAM.  
`↳ android_app_stream_data` |  `[DataStream\AndroidAppStreamData](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream.AndroidAppStreamData)`   
Data specific to Android app streams. Must be populated if type is ANDROID_APP_DATA_STREAM.  
`↳ ios_app_stream_data` |  `[DataStream\IosAppStreamData](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream.IosAppStreamData)`   
Data specific to iOS app streams. Must be populated if type is IOS_APP_DATA_STREAM.  
`↳ name` |  `string`   
Identifier. Resource name of this Data Stream. Format: properties/{property_id}/dataStreams/{stream_id} Example: "properties/1000/dataStreams/2000"  
`↳ type` |  `int`   
Required. Immutable. The type of this DataStream resource.  
`↳ display_name` |  `string`   
Human-readable display name for the Data Stream. Required for web data streams. The max allowed display name length is 255 UTF-16 code units.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. Time when this stream was originally created.  
`↳ update_time` |  `Google\Protobuf\Timestamp`   
Output only. Time when stream payload fields were last updated.  
  
### getWebStreamData

Data specific to web streams. Must be populated if type is WEB_DATA_STREAM.

**Returns**  
---  
**Type** | **Description**  
`[DataStream\WebStreamData](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream.WebStreamData)|null` |   
  
### hasWebStreamData

### setWebStreamData

Data specific to web streams. Must be populated if type is WEB_DATA_STREAM.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[DataStream\WebStreamData](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream.WebStreamData)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAndroidAppStreamData

Data specific to Android app streams. Must be populated if type is ANDROID_APP_DATA_STREAM.

**Returns**  
---  
**Type** | **Description**  
`[DataStream\AndroidAppStreamData](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream.AndroidAppStreamData)|null` |   
  
### hasAndroidAppStreamData

### setAndroidAppStreamData

Data specific to Android app streams. Must be populated if type is ANDROID_APP_DATA_STREAM.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[DataStream\AndroidAppStreamData](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream.AndroidAppStreamData)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getIosAppStreamData

Data specific to iOS app streams. Must be populated if type is IOS_APP_DATA_STREAM.

**Returns**  
---  
**Type** | **Description**  
`[DataStream\IosAppStreamData](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream.IosAppStreamData)|null` |   
  
### hasIosAppStreamData

### setIosAppStreamData

Data specific to iOS app streams. Must be populated if type is IOS_APP_DATA_STREAM.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[DataStream\IosAppStreamData](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream.IosAppStreamData)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getName

Identifier. Resource name of this Data Stream.

Format: properties/{property_id}/dataStreams/{stream_id} Example: "properties/1000/dataStreams/2000"

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. Resource name of this Data Stream.

Format: properties/{property_id}/dataStreams/{stream_id} Example: "properties/1000/dataStreams/2000"

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getType

Required. Immutable. The type of this DataStream resource.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [DataStreamType](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream.DataStreamType).  
  
### setType

Required. Immutable. The type of this DataStream resource.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [DataStreamType](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DataStream.DataStreamType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisplayName

Human-readable display name for the Data Stream.

Required for web data streams. The max allowed display name length is 255 UTF-16 code units.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDisplayName

Human-readable display name for the Data Stream.

Required for web data streams. The max allowed display name length is 255 UTF-16 code units.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. Time when this stream was originally created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. Time when this stream was originally created.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Output only. Time when stream payload fields were last updated.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasUpdateTime

### clearUpdateTime

### setUpdateTime

Output only. Time when stream payload fields were last updated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStreamData

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
