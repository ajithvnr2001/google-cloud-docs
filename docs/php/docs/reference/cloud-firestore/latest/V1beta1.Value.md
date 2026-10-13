---
url: https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.Value
title: Cloud Firestore V1beta1 Client - Class Value (2.2.0-RC1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:13.105680+00:00
---

# Cloud Firestore V1beta1 Client - Class Value (2.2.0-RC1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.Value

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Firestore V1beta1 Client - Class Value (2.2.0-RC1) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0-RC1  2.1.0  2.0.2-RC1  1.55.0  1.54.4  1.53.1  1.52.0  1.51.0  1.50.0  1.48.1  1.47.3  1.46.0  1.45.2  1.44.1  1.43.3  1.40.0  1.39.0  1.38.0  1.37.7  1.36.1  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.28.0  1.27.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Cloud Firestore V1beta1 Client class Value.

A message that can hold any of the supported value types.

Generated from protobuf message `google.firestore.v1beta1.Value`

## Namespace

Google \ Cloud \ Firestore \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ null_value` |  `int`   
A null value.  
`↳ boolean_value` |  `bool`   
A boolean value.  
`↳ integer_value` |  `int|string`   
An integer value.  
`↳ double_value` |  `float`   
A double value.  
`↳ timestamp_value` |  `[Google\Protobuf\Timestamp](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/Timestamp)`   
A timestamp value. Precise only to microseconds. When stored, any additional precision is rounded down.  
`↳ string_value` |  `string`   
A string value. The string, represented as UTF-8, must not exceed 1 MiB - 89 bytes. Only the first 1,500 bytes of the UTF-8 representation are considered by queries.  
`↳ bytes_value` |  `string`   
A bytes value. Must not exceed 1 MiB - 89 bytes. Only the first 1,500 bytes are considered by queries.  
`↳ reference_value` |  `string`   
A reference to a document. For example: `projects/{project_id}/databases/{database_id}/documents/{document_path}`.  
`↳ geo_point_value` |  `[Google\Type\LatLng](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.LatLng.html)`   
A geo point value representing a point on the surface of Earth.  
`↳ array_value` |  `[ArrayValue](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.ArrayValue)`   
An array value. Cannot directly contain another array value, though can contain an map which contains another array.  
`↳ map_value` |  `[MapValue](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.MapValue)`   
A map value.  
  
### getNullValue

A null value.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [NullValue](https://protobuf.dev/reference/php/api-docs/NullValue).  
  
### setNullValue

A null value.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [NullValue](https://protobuf.dev/reference/php/api-docs/NullValue).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBooleanValue

A boolean value.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setBooleanValue

A boolean value.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getIntegerValue

An integer value.

**Returns**  
---  
**Type** | **Description**  
`int|string` |   
  
### setIntegerValue

An integer value.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int|string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDoubleValue

A double value.

**Returns**  
---  
**Type** | **Description**  
`float` |   
  
### setDoubleValue

A double value.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `float`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTimestampValue

A timestamp value.

Precise only to microseconds. When stored, any additional precision is rounded down.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\Timestamp](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/Timestamp)` |   
  
### setTimestampValue

A timestamp value.

Precise only to microseconds. When stored, any additional precision is rounded down.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Protobuf\Timestamp](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/Timestamp)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStringValue

A string value.

The string, represented as UTF-8, must not exceed 1 MiB - 89 bytes. Only the first 1,500 bytes of the UTF-8 representation are considered by queries.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setStringValue

A string value.

The string, represented as UTF-8, must not exceed 1 MiB - 89 bytes. Only the first 1,500 bytes of the UTF-8 representation are considered by queries.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBytesValue

A bytes value.

Must not exceed 1 MiB - 89 bytes. Only the first 1,500 bytes are considered by queries.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setBytesValue

A bytes value.

Must not exceed 1 MiB - 89 bytes. Only the first 1,500 bytes are considered by queries.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getReferenceValue

A reference to a document. For example: `projects/{project_id}/databases/{database_id}/documents/{document_path}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setReferenceValue

A reference to a document. For example: `projects/{project_id}/databases/{database_id}/documents/{document_path}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getGeoPointValue

A geo point value representing a point on the surface of Earth.

**Returns**  
---  
**Type** | **Description**  
`[Google\Type\LatLng](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.LatLng.html)` |   
  
### setGeoPointValue

A geo point value representing a point on the surface of Earth.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Type\LatLng](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.LatLng.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getArrayValue

An array value.

Cannot directly contain another array value, though can contain an map which contains another array.

**Returns**  
---  
**Type** | **Description**  
`[ArrayValue](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.ArrayValue)` |   
  
### setArrayValue

An array value.

Cannot directly contain another array value, though can contain an map which contains another array.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ArrayValue](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.ArrayValue)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMapValue

A map value.

**Returns**  
---  
**Type** | **Description**  
`[MapValue](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.MapValue)` |   
  
### setMapValue

A map value.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[MapValue](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.MapValue)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getValueType

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
