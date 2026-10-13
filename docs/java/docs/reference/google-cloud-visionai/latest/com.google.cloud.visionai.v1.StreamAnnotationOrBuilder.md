---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamAnnotationOrBuilder
title: Interface StreamAnnotationOrBuilder (0.56.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:39.761202+00:00
---

# Interface StreamAnnotationOrBuilder (0.56.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamAnnotationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface StreamAnnotationOrBuilder (0.56.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.56.0 (latest)  0.52.0  0.51.0  0.50.0  0.48.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.37.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface StreamAnnotationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getActiveZone()
    
    
    public abstract NormalizedPolygon getActiveZone()

Annotation for type ACTIVE_ZONE

`.google.cloud.visionai.v1.NormalizedPolygon active_zone = 5;`

**Returns**  
---  
**Type** | **Description**  
`[NormalizedPolygon](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.NormalizedPolygon)` | The activeZone.  
  
### getActiveZoneOrBuilder()
    
    
    public abstract NormalizedPolygonOrBuilder getActiveZoneOrBuilder()

Annotation for type ACTIVE_ZONE

`.google.cloud.visionai.v1.NormalizedPolygon active_zone = 5;`

**Returns**  
---  
**Type** | **Description**  
`[NormalizedPolygonOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.NormalizedPolygonOrBuilder)` |   
  
### getAnnotationPayloadCase()
    
    
    public abstract StreamAnnotation.AnnotationPayloadCase getAnnotationPayloadCase()

**Returns**  
---  
**Type** | **Description**  
`[StreamAnnotation.AnnotationPayloadCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamAnnotation.AnnotationPayloadCase)` |   
  
### getCrossingLine()
    
    
    public abstract NormalizedPolyline getCrossingLine()

Annotation for type CROSSING_LINE

`.google.cloud.visionai.v1.NormalizedPolyline crossing_line = 6;`

**Returns**  
---  
**Type** | **Description**  
`[NormalizedPolyline](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.NormalizedPolyline)` | The crossingLine.  
  
### getCrossingLineOrBuilder()
    
    
    public abstract NormalizedPolylineOrBuilder getCrossingLineOrBuilder()

Annotation for type CROSSING_LINE

`.google.cloud.visionai.v1.NormalizedPolyline crossing_line = 6;`

**Returns**  
---  
**Type** | **Description**  
`[NormalizedPolylineOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.NormalizedPolylineOrBuilder)` |   
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

User-friendly name for the annotation.

`string display_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

User-friendly name for the annotation.

`string display_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getId()
    
    
    public abstract String getId()

ID of the annotation. It must be unique when used in the certain context. For example, all the annotations to one input streams of a Vision AI application.

`string id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public abstract ByteString getIdBytes()

ID of the annotation. It must be unique when used in the certain context. For example, all the annotations to one input streams of a Vision AI application.

`string id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getSourceStream()
    
    
    public abstract String getSourceStream()

The Vision AI stream resource name.

`string source_stream = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sourceStream.  
  
### getSourceStreamBytes()
    
    
    public abstract ByteString getSourceStreamBytes()

The Vision AI stream resource name.

`string source_stream = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sourceStream.  
  
### getType()
    
    
    public abstract StreamAnnotationType getType()

The actual type of Annotation.

`.google.cloud.visionai.v1.StreamAnnotationType type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[StreamAnnotationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamAnnotationType)` | The type.  
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

The actual type of Annotation.

`.google.cloud.visionai.v1.StreamAnnotationType type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### hasActiveZone()
    
    
    public abstract boolean hasActiveZone()

Annotation for type ACTIVE_ZONE

`.google.cloud.visionai.v1.NormalizedPolygon active_zone = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the activeZone field is set.  
  
### hasCrossingLine()
    
    
    public abstract boolean hasCrossingLine()

Annotation for type CROSSING_LINE

`.google.cloud.visionai.v1.NormalizedPolyline crossing_line = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the crossingLine field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
