---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.schema.predict.prediction.VideoObjectTrackingPredictionResult.FrameOrBuilder
title: Interface VideoObjectTrackingPredictionResult.FrameOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:45.781975+00:00
---

# Interface VideoObjectTrackingPredictionResult.FrameOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.schema.predict.prediction.VideoObjectTrackingPredictionResult.FrameOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface VideoObjectTrackingPredictionResult.FrameOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static interface VideoObjectTrackingPredictionResult.FrameOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getTimeOffset()
    
    
    public abstract Duration getTimeOffset()

A time (frame) of a video in which the object has been detected. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with "s" appended at the end.

`.google.protobuf.Duration time_offset = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The timeOffset.  
  
### getTimeOffsetOrBuilder()
    
    
    public abstract DurationOrBuilder getTimeOffsetOrBuilder()

A time (frame) of a video in which the object has been detected. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with "s" appended at the end.

`.google.protobuf.Duration time_offset = 1;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getXMax()
    
    
    public abstract FloatValue getXMax()

The rightmost coordinate of the bounding box.

`.google.protobuf.FloatValue x_max = 3;`

**Returns**  
---  
**Type** | **Description**  
`[FloatValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FloatValue.html)` | The xMax.  
  
### getXMaxOrBuilder()
    
    
    public abstract FloatValueOrBuilder getXMaxOrBuilder()

The rightmost coordinate of the bounding box.

`.google.protobuf.FloatValue x_max = 3;`

**Returns**  
---  
**Type** | **Description**  
`[FloatValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FloatValueOrBuilder.html)` |   
  
### getXMin()
    
    
    public abstract FloatValue getXMin()

The leftmost coordinate of the bounding box.

`.google.protobuf.FloatValue x_min = 2;`

**Returns**  
---  
**Type** | **Description**  
`[FloatValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FloatValue.html)` | The xMin.  
  
### getXMinOrBuilder()
    
    
    public abstract FloatValueOrBuilder getXMinOrBuilder()

The leftmost coordinate of the bounding box.

`.google.protobuf.FloatValue x_min = 2;`

**Returns**  
---  
**Type** | **Description**  
`[FloatValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FloatValueOrBuilder.html)` |   
  
### getYMax()
    
    
    public abstract FloatValue getYMax()

The bottommost coordinate of the bounding box.

`.google.protobuf.FloatValue y_max = 5;`

**Returns**  
---  
**Type** | **Description**  
`[FloatValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FloatValue.html)` | The yMax.  
  
### getYMaxOrBuilder()
    
    
    public abstract FloatValueOrBuilder getYMaxOrBuilder()

The bottommost coordinate of the bounding box.

`.google.protobuf.FloatValue y_max = 5;`

**Returns**  
---  
**Type** | **Description**  
`[FloatValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FloatValueOrBuilder.html)` |   
  
### getYMin()
    
    
    public abstract FloatValue getYMin()

The topmost coordinate of the bounding box.

`.google.protobuf.FloatValue y_min = 4;`

**Returns**  
---  
**Type** | **Description**  
`[FloatValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FloatValue.html)` | The yMin.  
  
### getYMinOrBuilder()
    
    
    public abstract FloatValueOrBuilder getYMinOrBuilder()

The topmost coordinate of the bounding box.

`.google.protobuf.FloatValue y_min = 4;`

**Returns**  
---  
**Type** | **Description**  
`[FloatValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FloatValueOrBuilder.html)` |   
  
### hasTimeOffset()
    
    
    public abstract boolean hasTimeOffset()

A time (frame) of a video in which the object has been detected. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with "s" appended at the end.

`.google.protobuf.Duration time_offset = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timeOffset field is set.  
  
### hasXMax()
    
    
    public abstract boolean hasXMax()

The rightmost coordinate of the bounding box.

`.google.protobuf.FloatValue x_max = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the xMax field is set.  
  
### hasXMin()
    
    
    public abstract boolean hasXMin()

The leftmost coordinate of the bounding box.

`.google.protobuf.FloatValue x_min = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the xMin field is set.  
  
### hasYMax()
    
    
    public abstract boolean hasYMax()

The bottommost coordinate of the bounding box.

`.google.protobuf.FloatValue y_max = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the yMax field is set.  
  
### hasYMin()
    
    
    public abstract boolean hasYMin()

The topmost coordinate of the bounding box.

`.google.protobuf.FloatValue y_min = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the yMin field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
