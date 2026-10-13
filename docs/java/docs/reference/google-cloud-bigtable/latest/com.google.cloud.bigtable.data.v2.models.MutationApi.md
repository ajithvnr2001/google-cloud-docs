---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.MutationApi
title: Interface MutationApi<T> (2.85.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:50.434209+00:00
---

# Interface MutationApi<T> (2.85.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.MutationApi

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MutationApi<T> (2.85.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.85.0 (latest)  2.81.0  2.80.0  2.79.0  2.78.1  2.77.0  2.74.0  2.73.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.1  2.66.0  2.65.1  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.2  2.56.0  2.54.0  2.52.0  2.51.2  2.49.0  2.46.0  2.45.1  2.44.1  2.43.0  2.42.0  2.40.0  2.39.5  2.37.0  2.35.1  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0 
    
    
    public interface MutationApi<T>

The API for creating mutations for a single row.

## Type Parameter  
  
---  
**Name** | **Description**  
`T` |   
  
## Methods 

### addToCell(String familyName, Value qualifier, Value timestamp, Value input)
    
    
    public abstract T addToCell(String familyName, Value qualifier, Value timestamp, Value input)

Adds a [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Value) to an aggregate cell. The column family must be an aggregate family and have an input type matching the type of [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Value) or this mutation will be rejected.

Note: The timestamp values are in microseconds but must match the granularity of the table(defaults to `MILLIS`). Therefore, the given value must be a multiple of 1000 (millisecond granularity). For example: `1571902339435000`.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Value)`  
  
`timestamp` | `[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Value)`  
  
`input` | `[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Value)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### addToCell(String familyName, ByteString qualifier, long timestamp, long input)
    
    
    public default T addToCell(String familyName, ByteString qualifier, long timestamp, long input)

Adds an int64 value to an aggregate cell. The column family must be an aggregate family and have an "int64" input type or this mutation will be rejected.

Note: The timestamp values are in microseconds but must match the granularity of the table(defaults to `MILLIS`). Therefore, the given value must be a multiple of 1000 (millisecond granularity). For example: `1571902339435000`.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`timestamp` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`input` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### addToCell(String familyName, String qualifier, long timestamp, long value)
    
    
    public default T addToCell(String familyName, String qualifier, long timestamp, long value)

Adds an int64 value to an aggregate cell. The column family must be an aggregate family and have an "int64" input type or this mutation will be rejected.

This is a convenience override that converts Strings to ByteStrings.

Note: The timestamp values are in microseconds but must match the granularity of the table(defaults to `MILLIS`). Therefore, the given value must be a multiple of 1000 (millisecond granularity). For example: `1571902339435000`.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`timestamp` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### deleteCells(String familyName, ByteString qualifier)
    
    
    public abstract T deleteCells(String familyName, ByteString qualifier)

Adds a mutation which deletes cells from the specified column.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### deleteCells(String familyName, ByteString qualifier, Range.TimestampRange timestampRange)
    
    
    public abstract T deleteCells(String familyName, ByteString qualifier, Range.TimestampRange timestampRange)

Adds a mutation which deletes cells from the specified column, restricted to a given timestamp range.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The family name.  
`qualifier` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The qualifier.  
`timestampRange` | `[Range.TimestampRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Range.TimestampRange)`  
The timestamp range in microseconds.  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### deleteCells(String familyName, String qualifier)
    
    
    public abstract T deleteCells(String familyName, String qualifier)

Adds a mutation which deletes cells from the specified column.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### deleteFamily(String familyName)
    
    
    public abstract T deleteFamily(String familyName)

Adds a mutation which deletes all cells from the specified column family.

**Parameter**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### deleteRow()
    
    
    public abstract T deleteRow()

Adds a mutation which deletes all cells from the containing row.

**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### mergeToCell(String familyName, Value qualifier, Value timestamp, Value input)
    
    
    public abstract T mergeToCell(String familyName, Value qualifier, Value timestamp, Value input)

Merges a [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Value) accumulator to an aggregate cell. The column family must be an aggregate family or this mutation will be rejected.

Note: The timestamp values are in microseconds but must match the granularity of the table(defaults to `MILLIS`). Therefore, the given value must be a multiple of 1000 (millisecond granularity). For example: `1571902339435000`.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Value)`  
  
`timestamp` | `[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Value)`  
  
`input` | `[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.Value)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### mergeToCell(String familyName, ByteString qualifier, long timestamp, ByteString input)
    
    
    public default T mergeToCell(String familyName, ByteString qualifier, long timestamp, ByteString input)

Merges a ByteString accumulator value to a cell in an aggregate column family.

Note: The timestamp values are in microseconds but must match the granularity of the table(defaults to `MILLIS`). Therefore, the given value must be a multiple of 1000 (millisecond granularity). For example: `1571902339435000`.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`timestamp` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`input` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### mergeToCell(String familyName, String qualifier, long timestamp, ByteString value)
    
    
    public default T mergeToCell(String familyName, String qualifier, long timestamp, ByteString value)

Merges a ByteString accumulator value to a cell in an aggregate column family.

This is a convenience override that converts Strings to ByteStrings.

Note: The timestamp values are in microseconds but must match the granularity of the table(defaults to `MILLIS`). Therefore, the given value must be a multiple of 1000 (millisecond granularity). For example: `1571902339435000`.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`timestamp` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### setCell(String familyName, ByteString qualifier, ByteString value)
    
    
    public abstract T setCell(String familyName, ByteString qualifier, ByteString value)

Adds a mutation which sets the value of the specified cell.

Uses microseconds since epoch as the timestamp.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### setCell(String familyName, ByteString qualifier, long value)
    
    
    public abstract T setCell(String familyName, ByteString qualifier, long value)

Adds a mutation which sets the value of the specified cell.

Uses microseconds since epoch as the timestamp.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### setCell(String familyName, ByteString qualifier, long timestamp, ByteString value)
    
    
    public abstract T setCell(String familyName, ByteString qualifier, long timestamp, ByteString value)

Adds a mutation which sets the value of the specified cell.

Note: The timestamp values are in microseconds but must match the granularity of the table(defaults to `MILLIS`). Therefore, the given value must be a multiple of 1000 (millisecond granularity). For example: `1571902339435000`.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`timestamp` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### setCell(String familyName, ByteString qualifier, long timestamp, long value)
    
    
    public abstract T setCell(String familyName, ByteString qualifier, long timestamp, long value)

Adds a mutation which sets the value of the specified cell.

Note: The timestamp values are in microseconds but must match the granularity of the table(defaults to `MILLIS`). Therefore, the given value must be a multiple of 1000 (millisecond granularity). For example: `1571902339435000`.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`timestamp` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### setCell(String familyName, String qualifier, String value)
    
    
    public abstract T setCell(String familyName, String qualifier, String value)

Adds a mutation which sets the value of the specified cell.

This a convenience method that converts Strings to ByteStrings and uses microseconds since epoch as the timestamp.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### setCell(String familyName, String qualifier, long value)
    
    
    public abstract T setCell(String familyName, String qualifier, long value)

Adds a mutation which sets the value of the specified cell.

This a convenience method that converts Strings to ByteStrings and uses microseconds since epoch as the timestamp. Also it accepts long value.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### setCell(String familyName, String qualifier, long timestamp, String value)
    
    
    public abstract T setCell(String familyName, String qualifier, long timestamp, String value)

Adds a mutation which sets the value of the specified cell.

This is a convenience override that converts Strings to ByteStrings.

Note: The timestamp values are in microseconds but must match the granularity of the table(defaults to `MILLIS`). Therefore, the given value must be a multiple of 1000 (millisecond granularity). For example: `1571902339435000`.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`timestamp` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
### setCell(String familyName, String qualifier, long timestamp, long value)
    
    
    public abstract T setCell(String familyName, String qualifier, long timestamp, long value)

Adds a mutation which sets the value of the specified cell.

This is a convenience override that converts Strings to ByteStrings.

Note: The timestamp values are in microseconds but must match the granularity of the table(defaults to `MILLIS`). Therefore, the given value must be a multiple of 1000 (millisecond granularity). For example: `1571902339435000`.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`timestamp` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`T` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
