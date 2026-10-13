---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.FacetBucketOrBuilder
title: Interface FacetBucketOrBuilder (0.56.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:56.024533+00:00
---

# Interface FacetBucketOrBuilder (0.56.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.FacetBucketOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FacetBucketOrBuilder (0.56.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.56.0 (latest)  0.52.0  0.51.0  0.50.0  0.48.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.37.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface FacetBucketOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBucketValueCase()
    
    
    public abstract FacetBucket.BucketValueCase getBucketValueCase()

**Returns**  
---  
**Type** | **Description**  
`[FacetBucket.BucketValueCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.FacetBucket.BucketValueCase)` |   
  
### getRange()
    
    
    public abstract FacetBucket.Range getRange()

Range value.

`.google.cloud.visionai.v1.FacetBucket.Range range = 4;`

**Returns**  
---  
**Type** | **Description**  
`[FacetBucket.Range](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.FacetBucket.Range)` | The range.  
  
### getRangeOrBuilder()
    
    
    public abstract FacetBucket.RangeOrBuilder getRangeOrBuilder()

Range value.

`.google.cloud.visionai.v1.FacetBucket.Range range = 4;`

**Returns**  
---  
**Type** | **Description**  
`[FacetBucket.RangeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.FacetBucket.RangeOrBuilder)` |   
  
### getSelected()
    
    
    public abstract boolean getSelected()

Whether one facet bucket is selected. This field represents user's facet selection. It is set by frontend in SearchVideosRequest.

`bool selected = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The selected.  
  
### getValue()
    
    
    public abstract FacetValue getValue()

Singular value.

`.google.cloud.visionai.v1.FacetValue value = 2;`

**Returns**  
---  
**Type** | **Description**  
`[FacetValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.FacetValue)` | The value.  
  
### getValueOrBuilder()
    
    
    public abstract FacetValueOrBuilder getValueOrBuilder()

Singular value.

`.google.cloud.visionai.v1.FacetValue value = 2;`

**Returns**  
---  
**Type** | **Description**  
`[FacetValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.FacetValueOrBuilder)` |   
  
### hasRange()
    
    
    public abstract boolean hasRange()

Range value.

`.google.cloud.visionai.v1.FacetBucket.Range range = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the range field is set.  
  
### hasValue()
    
    
    public abstract boolean hasValue()

Singular value.

`.google.cloud.visionai.v1.FacetValue value = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the value field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
