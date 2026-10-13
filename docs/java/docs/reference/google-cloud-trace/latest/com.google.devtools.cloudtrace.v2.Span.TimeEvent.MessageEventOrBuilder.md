---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.devtools.cloudtrace.v2.Span.TimeEvent.MessageEventOrBuilder
title: Interface Span.TimeEvent.MessageEventOrBuilder (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:30.513289+00:00
---

# Interface Span.TimeEvent.MessageEventOrBuilder (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.devtools.cloudtrace.v2.Span.TimeEvent.MessageEventOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Span.TimeEvent.MessageEventOrBuilder (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.7  2.2.0  2.1.13 
    
    
    public static interface Span.TimeEvent.MessageEventOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCompressedSizeBytes()
    
    
    public abstract long getCompressedSizeBytes()

The number of compressed bytes sent or received. If missing, the compressed size is assumed to be the same size as the uncompressed size.

`int64 compressed_size_bytes = 4;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The compressedSizeBytes.  
  
### getId()
    
    
    public abstract long getId()

An identifier for the MessageEvent's message that can be used to match `SENT` and `RECEIVED` MessageEvents.

`int64 id = 2;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The id.  
  
### getType()
    
    
    public abstract Span.TimeEvent.MessageEvent.Type getType()

Type of MessageEvent. Indicates whether the message was sent or received.

`.google.devtools.cloudtrace.v2.Span.TimeEvent.MessageEvent.Type type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Span.TimeEvent.MessageEvent.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-trace/latest/com.google.devtools.cloudtrace.v2.Span.TimeEvent.MessageEvent.Type)` | The type.  
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

Type of MessageEvent. Indicates whether the message was sent or received.

`.google.devtools.cloudtrace.v2.Span.TimeEvent.MessageEvent.Type type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### getUncompressedSizeBytes()
    
    
    public abstract long getUncompressedSizeBytes()

The number of uncompressed bytes sent or received.

`int64 uncompressed_size_bytes = 3;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The uncompressedSizeBytes.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
