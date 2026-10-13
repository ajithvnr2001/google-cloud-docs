---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowAdapter.RowBuilder
title: Interface RowAdapter.RowBuilder<RowT> (2.85.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:50.434491+00:00
---

# Interface RowAdapter.RowBuilder<RowT> (2.85.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.models.RowAdapter.RowBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RowAdapter.RowBuilder<RowT> (2.85.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.85.0 (latest)  2.81.0  2.80.0  2.79.0  2.78.1  2.77.0  2.74.0  2.73.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.1  2.66.0  2.65.1  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.2  2.56.0  2.54.0  2.52.0  2.51.2  2.49.0  2.46.0  2.45.1  2.44.1  2.43.0  2.42.0  2.40.0  2.39.5  2.37.0  2.35.1  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0 
    
    
    public static interface RowAdapter.RowBuilder<RowT>

A SAX style row factory. It is responsible for creating two types of rows: standard data rows and special marker rows. Marker rows are emitted when skipping lots of rows due to filters. The server notifies the client of the last row it skipped to help client resume in case of error.

State management is handled external to the implementation of this class and guarantees the following order:

  1. Exactly 1 `startRow` for each row. 
  2. Exactly 1 `startCell` for each cell. 
  3. At least 1 `cellValue` for each cell. 
  4. Exactly 1 `finishCell` for each cell. 
  5. Exactly 1 `finishRow` for each row. 



`createScanMarkerRow` can be called one or more times between `finishRow` and `startRow`. `reset` can be called at any point and can be invoked multiple times in a row.

## Type Parameter  
  
---  
**Name** | **Description**  
`RowT` |   
  
## Methods 

### cellValue(ByteString value)
    
    
    public abstract void cellValue(ByteString value)

Called multiple times per cell to concatenate the cell value.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
  
### createScanMarkerRow(ByteString key)
    
    
    public abstract RowT createScanMarkerRow(ByteString key)

Creates a special row to mark server progress before any data is received

**Parameter**  
---  
**Name** | **Description**  
`key` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`RowT` |   
  
### finishCell()
    
    
    public abstract void finishCell()

Called once per cell to signal the end of the value (unless reset).

### finishRow()
    
    
    public abstract RowT finishRow()

Called once per row to signal that all cells have been processed (unless reset).

**Returns**  
---  
**Type** | **Description**  
`RowT` |   
  
### reset()
    
    
    public abstract void reset()

Called when the current in progress row should be dropped

### startCell(String family, ByteString qualifier, long timestamp, List<String> labels, long size)
    
    
    public abstract void startCell(String family, ByteString qualifier, long timestamp, List<String> labels, long size)

Called to start a new cell in a row.

**Parameters**  
---  
**Name** | **Description**  
`family` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`qualifier` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`timestamp` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`labels` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
`size` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### startRow(ByteString key)
    
    
    public abstract void startRow(ByteString key)

Called to start a new row. This will be called once per row.

**Parameter**  
---  
**Name** | **Description**  
`key` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
