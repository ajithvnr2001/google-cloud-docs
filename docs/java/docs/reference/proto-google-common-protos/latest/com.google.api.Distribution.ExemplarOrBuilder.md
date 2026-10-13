---
url: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.Distribution.ExemplarOrBuilder
title: Interface Distribution.ExemplarOrBuilder (2.78.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:28.914613+00:00
---

# Interface Distribution.ExemplarOrBuilder (2.78.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.Distribution.ExemplarOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Distribution.ExemplarOrBuilder (2.78.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.78.0 (latest)  2.74.0  2.73.0  2.72.0  2.70.0  2.67.0  2.66.0  2.65.1  2.64.1  2.63.2  2.62.0  2.61.3  2.60.0  2.59.2  2.58.0  2.57.0  2.56.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.1  2.49.0  2.48.0  2.46.0  2.45.1  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.1  2.38.0  2.37.1  2.36.0  2.34.0  2.33.0  2.32.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.1  2.22.1  2.21.1  2.15.0  2.14.3  2.13.0  2.12.0  2.11.0  2.10.0  2.9.6  2.8.4  2.7.4 
    
    
    public static interface Distribution.ExemplarOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAttachments(int index)
    
    
    public abstract Any getAttachments(int index)

Contextual information about the example value. Examples are:

Trace: type.googleapis.com/google.monitoring.v3.SpanContext

Literal string: type.googleapis.com/google.protobuf.StringValue

Labels dropped during aggregation: type.googleapis.com/google.monitoring.v3.DroppedLabels

There may be only a single attachment of any given message type in a single exemplar, and this is enforced by the system.

`repeated .google.protobuf.Any attachments = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Any](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Any.html)` |   
  
### getAttachmentsCount()
    
    
    public abstract int getAttachmentsCount()

Contextual information about the example value. Examples are:

Trace: type.googleapis.com/google.monitoring.v3.SpanContext

Literal string: type.googleapis.com/google.protobuf.StringValue

Labels dropped during aggregation: type.googleapis.com/google.monitoring.v3.DroppedLabels

There may be only a single attachment of any given message type in a single exemplar, and this is enforced by the system.

`repeated .google.protobuf.Any attachments = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAttachmentsList()
    
    
    public abstract List<Any> getAttachmentsList()

Contextual information about the example value. Examples are:

Trace: type.googleapis.com/google.monitoring.v3.SpanContext

Literal string: type.googleapis.com/google.protobuf.StringValue

Labels dropped during aggregation: type.googleapis.com/google.monitoring.v3.DroppedLabels

There may be only a single attachment of any given message type in a single exemplar, and this is enforced by the system.

`repeated .google.protobuf.Any attachments = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Any](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Any.html)>` |   
  
### getAttachmentsOrBuilder(int index)
    
    
    public abstract AnyOrBuilder getAttachmentsOrBuilder(int index)

Contextual information about the example value. Examples are:

Trace: type.googleapis.com/google.monitoring.v3.SpanContext

Literal string: type.googleapis.com/google.protobuf.StringValue

Labels dropped during aggregation: type.googleapis.com/google.monitoring.v3.DroppedLabels

There may be only a single attachment of any given message type in a single exemplar, and this is enforced by the system.

`repeated .google.protobuf.Any attachments = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnyOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AnyOrBuilder.html)` |   
  
### getAttachmentsOrBuilderList()
    
    
    public abstract List<? extends AnyOrBuilder> getAttachmentsOrBuilderList()

Contextual information about the example value. Examples are:

Trace: type.googleapis.com/google.monitoring.v3.SpanContext

Literal string: type.googleapis.com/google.protobuf.StringValue

Labels dropped during aggregation: type.googleapis.com/google.monitoring.v3.DroppedLabels

There may be only a single attachment of any given message type in a single exemplar, and this is enforced by the system.

`repeated .google.protobuf.Any attachments = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.protobuf.AnyOrBuilder>` |   
  
### getTimestamp()
    
    
    public abstract Timestamp getTimestamp()

The observation (sampling) time of the above value.

`.google.protobuf.Timestamp timestamp = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The timestamp.  
  
### getTimestampOrBuilder()
    
    
    public abstract TimestampOrBuilder getTimestampOrBuilder()

The observation (sampling) time of the above value.

`.google.protobuf.Timestamp timestamp = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getValue()
    
    
    public abstract double getValue()

Value of the exemplar point. This value determines to which bucket the exemplar belongs.

`double value = 1;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The value.  
  
### hasTimestamp()
    
    
    public abstract boolean hasTimestamp()

The observation (sampling) time of the above value.

`.google.protobuf.Timestamp timestamp = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timestamp field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
