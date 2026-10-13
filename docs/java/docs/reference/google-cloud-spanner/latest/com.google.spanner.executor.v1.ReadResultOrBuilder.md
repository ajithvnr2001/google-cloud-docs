---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.executor.v1.ReadResultOrBuilder
title: Interface ReadResultOrBuilder (6.124.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:05.429461+00:00
---

# Interface ReadResultOrBuilder (6.124.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.executor.v1.ReadResultOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReadResultOrBuilder (6.124.0) Stay organized with collections  Save and categorize content based on your preferences. 

6.124.0 (latest)  6.120.0  6.119.0  6.118.0  6.116.0  6.111.1  6.108.0  6.107.0  6.103.0  6.102.1  6.101.1  6.100.0  6.99.0  6.98.1  6.97.1  6.96.1  6.95.1  6.94.0  6.93.0  6.89.0  6.88.0  6.87.0  6.86.0  6.85.0  6.83.0  6.82.0  6.80.1  6.79.0  6.77.0  6.74.1  6.72.0  6.71.0  6.69.0  6.68.0  6.66.0  6.65.1  6.62.0  6.60.0  6.58.0  6.57.0  6.56.0  6.55.0  6.54.0  6.53.0  6.52.1  6.51.0  6.50.1  6.49.0  6.25.1  6.24.0  6.23.4  6.22.0  6.21.2  6.20.0  6.19.1  6.18.0  6.17.4  6.14.1 
    
    
    public interface ReadResultOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getIndex()
    
    
    public abstract String getIndex()

Index name, if read from an index.

`optional string index = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The index.  
  
### getIndexBytes()
    
    
    public abstract ByteString getIndexBytes()

Index name, if read from an index.

`optional string index = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for index.  
  
### getRequestIndex()
    
    
    public abstract int getRequestIndex()

Request index (multiread only).

`optional int32 request_index = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The requestIndex.  
  
### getRow(int index)
    
    
    public abstract ValueList getRow(int index)

Rows read. Each row is a struct with multiple fields, one for each column in read result. All rows have the same type.

`repeated .google.spanner.executor.v1.ValueList row = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ValueList](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.executor.v1.ValueList)` |   
  
### getRowCount()
    
    
    public abstract int getRowCount()

Rows read. Each row is a struct with multiple fields, one for each column in read result. All rows have the same type.

`repeated .google.spanner.executor.v1.ValueList row = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRowList()
    
    
    public abstract List<ValueList> getRowList()

Rows read. Each row is a struct with multiple fields, one for each column in read result. All rows have the same type.

`repeated .google.spanner.executor.v1.ValueList row = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ValueList](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.executor.v1.ValueList)>` |   
  
### getRowOrBuilder(int index)
    
    
    public abstract ValueListOrBuilder getRowOrBuilder(int index)

Rows read. Each row is a struct with multiple fields, one for each column in read result. All rows have the same type.

`repeated .google.spanner.executor.v1.ValueList row = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ValueListOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.executor.v1.ValueListOrBuilder)` |   
  
### getRowOrBuilderList()
    
    
    public abstract List<? extends ValueListOrBuilder> getRowOrBuilderList()

Rows read. Each row is a struct with multiple fields, one for each column in read result. All rows have the same type.

`repeated .google.spanner.executor.v1.ValueList row = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.spanner.executor.v1.ValueListOrBuilder>` |   
  
### getRowType()
    
    
    public abstract StructType getRowType()

The type of rows read. It must be set if at least one row was read.

`optional .google.spanner.v1.StructType row_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[StructType](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.StructType)` | The rowType.  
  
### getRowTypeOrBuilder()
    
    
    public abstract StructTypeOrBuilder getRowTypeOrBuilder()

The type of rows read. It must be set if at least one row was read.

`optional .google.spanner.v1.StructType row_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[StructTypeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.StructTypeOrBuilder)` |   
  
### getTable()
    
    
    public abstract String getTable()

Table name.

`string table = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The table.  
  
### getTableBytes()
    
    
    public abstract ByteString getTableBytes()

Table name.

`string table = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for table.  
  
### hasIndex()
    
    
    public abstract boolean hasIndex()

Index name, if read from an index.

`optional string index = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the index field is set.  
  
### hasRequestIndex()
    
    
    public abstract boolean hasRequestIndex()

Request index (multiread only).

`optional int32 request_index = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the requestIndex field is set.  
  
### hasRowType()
    
    
    public abstract boolean hasRowType()

The type of rows read. It must be set if at least one row was read.

`optional .google.spanner.v1.StructType row_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rowType field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
