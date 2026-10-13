---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.SrumOrBuilder
title: Interface SrumOrBuilder (0.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:36.364409+00:00
---

# Interface SrumOrBuilder (0.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.SrumOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SrumOrBuilder (0.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.0 (latest)  0.3.0  0.2.0  0.1.0 
    
    
    public interface SrumOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBackgroundBytesRead()
    
    
    public abstract long getBackgroundBytesRead()

The number of bytes read by the application while running in the background.

`int64 background_bytes_read = 2;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The backgroundBytesRead.  
  
### getBackgroundBytesWritten()
    
    
    public abstract long getBackgroundBytesWritten()

The number of bytes written by the application while running in the background.

`int64 background_bytes_written = 3;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The backgroundBytesWritten.  
  
### getBackgroundContextSwitches()
    
    
    public abstract long getBackgroundContextSwitches()

The number of context switches performed by the application's threads while in the background.

`int64 background_context_switches = 4;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The backgroundContextSwitches.  
  
### getBackgroundCycleCount()
    
    
    public abstract long getBackgroundCycleCount()

The amount of CPU cycle time consumed by the application in the background, measured in clock cycles.

`int64 background_cycle_count = 5;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The backgroundCycleCount.  
  
### getBackgroundFlushesCount()
    
    
    public abstract long getBackgroundFlushesCount()

The number of flush operations performed by the application in the background.

`int64 background_flushes_count = 6;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The backgroundFlushesCount.  
  
### getBackgroundReadOperations()
    
    
    public abstract long getBackgroundReadOperations()

The number of read operations performed by the application in the background.

`int64 background_read_operations = 7;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The backgroundReadOperations.  
  
### getBackgroundWriteOperations()
    
    
    public abstract long getBackgroundWriteOperations()

The number of write operations performed by the application in the background.

`int64 background_write_operations = 8;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The backgroundWriteOperations.  
  
### getId()
    
    
    public abstract String getId()

A unique identifier for the SRUM record or the application/user being monitored.

`string id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public abstract ByteString getIdBytes()

A unique identifier for the SRUM record or the application/user being monitored.

`string id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getInterfaceLuid()
    
    
    public abstract String getInterfaceLuid()

The Locally Unique Identifier (LUID) for the network interface used for data transfer.

`string interface_luid = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The interfaceLuid.  
  
### getInterfaceLuidBytes()
    
    
    public abstract ByteString getInterfaceLuidBytes()

The Locally Unique Identifier (LUID) for the network interface used for data transfer.

`string interface_luid = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for interfaceLuid.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
