---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p3beta1.PageOrBuilder
title: Interface PageOrBuilder (3.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:41.048396+00:00
---

# Interface PageOrBuilder (3.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p3beta1.PageOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PageOrBuilder (3.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.97.0 (latest)  3.93.0  3.92.0  3.91.0  3.89.0  3.86.0  3.85.0  3.83.0  3.81.0  3.80.0  3.78.0  3.76.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.68.0  3.66.0  3.65.0  3.62.0  3.61.0  3.60.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.3  2.1.4  2.0.29 
    
    
    public interface PageOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBlocks(int index)
    
    
    public abstract Block getBlocks(int index)

List of blocks of text, images etc on this page.

`repeated .google.cloud.vision.v1p3beta1.Block blocks = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Block](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p3beta1.Block)` |   
  
### getBlocksCount()
    
    
    public abstract int getBlocksCount()

List of blocks of text, images etc on this page.

`repeated .google.cloud.vision.v1p3beta1.Block blocks = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBlocksList()
    
    
    public abstract List<Block> getBlocksList()

List of blocks of text, images etc on this page.

`repeated .google.cloud.vision.v1p3beta1.Block blocks = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Block](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p3beta1.Block)>` |   
  
### getBlocksOrBuilder(int index)
    
    
    public abstract BlockOrBuilder getBlocksOrBuilder(int index)

List of blocks of text, images etc on this page.

`repeated .google.cloud.vision.v1p3beta1.Block blocks = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BlockOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p3beta1.BlockOrBuilder)` |   
  
### getBlocksOrBuilderList()
    
    
    public abstract List<? extends BlockOrBuilder> getBlocksOrBuilderList()

List of blocks of text, images etc on this page.

`repeated .google.cloud.vision.v1p3beta1.Block blocks = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.vision.v1p3beta1.BlockOrBuilder>` |   
  
### getConfidence()
    
    
    public abstract float getConfidence()

Confidence of the OCR results on the page. Range [0, 1].

`float confidence = 5;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The confidence.  
  
### getHeight()
    
    
    public abstract int getHeight()

Page height. For PDFs the unit is points. For images (including TIFFs) the unit is pixels.

`int32 height = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The height.  
  
### getProperty()
    
    
    public abstract TextAnnotation.TextProperty getProperty()

Additional information detected on the page.

`.google.cloud.vision.v1p3beta1.TextAnnotation.TextProperty property = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TextAnnotation.TextProperty](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p3beta1.TextAnnotation.TextProperty)` | The property.  
  
### getPropertyOrBuilder()
    
    
    public abstract TextAnnotation.TextPropertyOrBuilder getPropertyOrBuilder()

Additional information detected on the page.

`.google.cloud.vision.v1p3beta1.TextAnnotation.TextProperty property = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TextAnnotation.TextPropertyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p3beta1.TextAnnotation.TextPropertyOrBuilder)` |   
  
### getWidth()
    
    
    public abstract int getWidth()

Page width. For PDFs the unit is points. For images (including TIFFs) the unit is pixels.

`int32 width = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The width.  
  
### hasProperty()
    
    
    public abstract boolean hasProperty()

Additional information detected on the page.

`.google.cloud.vision.v1p3beta1.TextAnnotation.TextProperty property = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the property field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
