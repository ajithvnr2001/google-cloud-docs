---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.VideoStreamInputConfigOrBuilder
title: Interface VideoStreamInputConfigOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:10.314726+00:00
---

# Interface VideoStreamInputConfigOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.VideoStreamInputConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface VideoStreamInputConfigOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.VideoStreamInputConfigOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.visionai.v1.VideoStreamInputConfigOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.visionai.v1.VideoStreamInputConfigOrBuilder)


    
    
    public interface VideoStreamInputConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getStreams(int index)
    
    
    public abstract String getStreams(int index)

`repeated string streams = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The streams at the given index.  
  
### getStreamsBytes(int index)
    
    
    public abstract ByteString getStreamsBytes(int index)

`repeated string streams = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the streams at the given index.  
  
### getStreamsCount()
    
    
    public abstract int getStreamsCount()

`repeated string streams = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of streams.  
  
### getStreamsList()
    
    
    public abstract List<String> getStreamsList()

`repeated string streams = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the streams.  
  
### getStreamsWithAnnotation(int index)
    
    
    public abstract StreamWithAnnotation getStreamsWithAnnotation(int index)

` repeated .google.events.cloud.visionai.v1.StreamWithAnnotation streams_with_annotation = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWithAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.StreamWithAnnotation)` |   
  
### getStreamsWithAnnotationCount()
    
    
    public abstract int getStreamsWithAnnotationCount()

` repeated .google.events.cloud.visionai.v1.StreamWithAnnotation streams_with_annotation = 2; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getStreamsWithAnnotationList()
    
    
    public abstract List<StreamWithAnnotation> getStreamsWithAnnotationList()

` repeated .google.events.cloud.visionai.v1.StreamWithAnnotation streams_with_annotation = 2; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[StreamWithAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.StreamWithAnnotation)>` |   
  
### getStreamsWithAnnotationOrBuilder(int index)
    
    
    public abstract StreamWithAnnotationOrBuilder getStreamsWithAnnotationOrBuilder(int index)

` repeated .google.events.cloud.visionai.v1.StreamWithAnnotation streams_with_annotation = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamWithAnnotationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.visionai.v1.StreamWithAnnotationOrBuilder)` |   
  
### getStreamsWithAnnotationOrBuilderList()
    
    
    public abstract List<? extends StreamWithAnnotationOrBuilder> getStreamsWithAnnotationOrBuilderList()

` repeated .google.events.cloud.visionai.v1.StreamWithAnnotation streams_with_annotation = 2; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.events.cloud.visionai.v1.StreamWithAnnotationOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
