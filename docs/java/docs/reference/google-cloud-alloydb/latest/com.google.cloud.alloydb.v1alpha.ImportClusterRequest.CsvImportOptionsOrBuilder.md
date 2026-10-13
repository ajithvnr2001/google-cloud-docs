---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ImportClusterRequest.CsvImportOptionsOrBuilder
title: Interface ImportClusterRequest.CsvImportOptionsOrBuilder (0.88.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:19.550787+00:00
---

# Interface ImportClusterRequest.CsvImportOptionsOrBuilder (0.88.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ImportClusterRequest.CsvImportOptionsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ImportClusterRequest.CsvImportOptionsOrBuilder (0.88.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.88.0 (latest)  0.84.0  0.83.0  0.82.0  0.80.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.59.0  0.57.0  0.56.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface ImportClusterRequest.CsvImportOptionsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getColumns(int index)
    
    
    public abstract String getColumns(int index)

Optional. The columns to which CSV data is imported. If not specified, all columns of the database table are loaded with CSV data.

`repeated string columns = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The columns at the given index.  
  
### getColumnsBytes(int index)
    
    
    public abstract ByteString getColumnsBytes(int index)

Optional. The columns to which CSV data is imported. If not specified, all columns of the database table are loaded with CSV data.

`repeated string columns = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the columns at the given index.  
  
### getColumnsCount()
    
    
    public abstract int getColumnsCount()

Optional. The columns to which CSV data is imported. If not specified, all columns of the database table are loaded with CSV data.

`repeated string columns = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of columns.  
  
### getColumnsList()
    
    
    public abstract List<String> getColumnsList()

Optional. The columns to which CSV data is imported. If not specified, all columns of the database table are loaded with CSV data.

`repeated string columns = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the columns.  
  
### getEscapeCharacter()
    
    
    public abstract String getEscapeCharacter()

Optional. Specifies the character that should appear before a data character that needs to be escaped. The default is same as quote character. The value of this argument has to be a character in Hex ASCII Code.

`string escape_character = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The escapeCharacter.  
  
### getEscapeCharacterBytes()
    
    
    public abstract ByteString getEscapeCharacterBytes()

Optional. Specifies the character that should appear before a data character that needs to be escaped. The default is same as quote character. The value of this argument has to be a character in Hex ASCII Code.

`string escape_character = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for escapeCharacter.  
  
### getFieldDelimiter()
    
    
    public abstract String getFieldDelimiter()

Optional. Specifies the character that separates columns within each row (line) of the file. The default is comma. The value of this argument has to be a character in Hex ASCII Code.

`string field_delimiter = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The fieldDelimiter.  
  
### getFieldDelimiterBytes()
    
    
    public abstract ByteString getFieldDelimiterBytes()

Optional. Specifies the character that separates columns within each row (line) of the file. The default is comma. The value of this argument has to be a character in Hex ASCII Code.

`string field_delimiter = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for fieldDelimiter.  
  
### getQuoteCharacter()
    
    
    public abstract String getQuoteCharacter()

Optional. Specifies the quoting character to be used when a data value is quoted. The default is double-quote. The value of this argument has to be a character in Hex ASCII Code.

`string quote_character = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The quoteCharacter.  
  
### getQuoteCharacterBytes()
    
    
    public abstract ByteString getQuoteCharacterBytes()

Optional. Specifies the quoting character to be used when a data value is quoted. The default is double-quote. The value of this argument has to be a character in Hex ASCII Code.

`string quote_character = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for quoteCharacter.  
  
### getTable()
    
    
    public abstract String getTable()

Required. The database table to import CSV file into.

`string table = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The table.  
  
### getTableBytes()
    
    
    public abstract ByteString getTableBytes()

Required. The database table to import CSV file into.

`string table = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for table.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
