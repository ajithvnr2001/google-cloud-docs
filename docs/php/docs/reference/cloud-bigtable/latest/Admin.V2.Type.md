---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type
title: Cloud Bigtable V2 Client - Class Type (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:55.678483+00:00
---

# Cloud Bigtable V2 Client - Class Type (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class Type (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class Type.

`Type` represents the type of data that is written to, read from, or stored in Bigtable. It is heavily based on the GoogleSQL standard to help maintain familiarity and consistency across products and features.

For compatibility with Bigtable's existing untyped APIs, each `Type` includes an `Encoding` which describes how to convert to or from the underlying data. Each encoding can operate in one of two modes:

  * Sorted: In this mode, Bigtable guarantees that `Encode(X) <= Encode(Y)` if and only if `X <= Y`. This is useful anywhere sort order is important, for example when encoding keys.
  * Distinct: In this mode, Bigtable guarantees that if `X != Y` then `Encode(X) != Encode(Y)`. However, the converse is not guaranteed. For example, both "{'foo': '1', 'bar': '2'}" and "{'bar': '2', 'foo': '1'}" are valid encodings of the same JSON value. The API clearly documents which mode is used wherever an encoding can be configured. Each encoding also documents which values are supported in which modes. For example, when encoding INT64 as a numeric STRING, negative numbers cannot be encoded in sorted mode. This is because `INT64(1) > INT64(-1)`, but `STRING("-00001") > STRING("00001")`.



Generated from protobuf message `google.bigtable.admin.v2.Type`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ bytes_type` |  `[Type\Bytes](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Bytes)`   
Bytes  
`↳ string_type` |  `[Type\PBString](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.PBString)`   
String  
`↳ int64_type` |  `[Type\Int64](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Int64)`   
Int64  
`↳ float32_type` |  `[Type\Float32](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Float32)`   
Float32  
`↳ float64_type` |  `[Type\Float64](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Float64)`   
Float64  
`↳ bool_type` |  `[Type\PBBool](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.PBBool)`   
Bool  
`↳ timestamp_type` |  `[Type\Timestamp](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Timestamp)`   
Timestamp  
`↳ date_type` |  `[Type\Date](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Date)`   
Date  
`↳ aggregate_type` |  `[Type\Aggregate](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate)`   
Aggregate  
`↳ struct_type` |  `[Type\Struct](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Struct)`   
Struct  
`↳ array_type` |  `[Type\PBArray](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.PBArray)`   
Array  
`↳ map_type` |  `[Type\Map](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Map)`   
Map  
`↳ proto_type` |  `[Type\Proto](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Proto)`   
Proto  
`↳ enum_type` |  `[Type\Enum](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Enum)`   
Enum  
  
### getBytesType

Bytes

**Returns**  
---  
**Type** | **Description**  
`[Type\Bytes](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Bytes)|null` |   
  
### hasBytesType

### setBytesType

Bytes

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type\Bytes](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Bytes)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStringType

String

**Returns**  
---  
**Type** | **Description**  
`[Type\PBString](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.PBString)|null` |   
  
### hasStringType

### setStringType

String

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type\PBString](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.PBString)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getInt64Type

Int64

**Returns**  
---  
**Type** | **Description**  
`[Type\Int64](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Int64)|null` |   
  
### hasInt64Type

### setInt64Type

Int64

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type\Int64](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Int64)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFloat32Type

Float32

**Returns**  
---  
**Type** | **Description**  
`[Type\Float32](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Float32)|null` |   
  
### hasFloat32Type

### setFloat32Type

Float32

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type\Float32](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Float32)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFloat64Type

Float64

**Returns**  
---  
**Type** | **Description**  
`[Type\Float64](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Float64)|null` |   
  
### hasFloat64Type

### setFloat64Type

Float64

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type\Float64](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Float64)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBoolType

Bool

**Returns**  
---  
**Type** | **Description**  
`[Type\PBBool](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.PBBool)|null` |   
  
### hasBoolType

### setBoolType

Bool

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type\PBBool](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.PBBool)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTimestampType

Timestamp

**Returns**  
---  
**Type** | **Description**  
`[Type\Timestamp](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Timestamp)|null` |   
  
### hasTimestampType

### setTimestampType

Timestamp

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type\Timestamp](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Timestamp)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDateType

Date

**Returns**  
---  
**Type** | **Description**  
`[Type\Date](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Date)|null` |   
  
### hasDateType

### setDateType

Date

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type\Date](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Date)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAggregateType

Aggregate

**Returns**  
---  
**Type** | **Description**  
`[Type\Aggregate](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate)|null` |   
  
### hasAggregateType

### setAggregateType

Aggregate

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type\Aggregate](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Aggregate)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStructType

Struct

**Returns**  
---  
**Type** | **Description**  
`[Type\Struct](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Struct)|null` |   
  
### hasStructType

### setStructType

Struct

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type\Struct](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Struct)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getArrayType

Array

**Returns**  
---  
**Type** | **Description**  
`[Type\PBArray](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.PBArray)|null` |   
  
### hasArrayType

### setArrayType

Array

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type\PBArray](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.PBArray)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMapType

Map

**Returns**  
---  
**Type** | **Description**  
`[Type\Map](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Map)|null` |   
  
### hasMapType

### setMapType

Map

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type\Map](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Map)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProtoType

Proto

**Returns**  
---  
**Type** | **Description**  
`[Type\Proto](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Proto)|null` |   
  
### hasProtoType

### setProtoType

Proto

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type\Proto](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Proto)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEnumType

Enum

**Returns**  
---  
**Type** | **Description**  
`[Type\Enum](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Enum)|null` |   
  
### hasEnumType

### setEnumType

Enum

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Type\Enum](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Type.Enum)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getKind

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
