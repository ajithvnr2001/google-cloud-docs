---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiSession.CreationContext.VodInfoOrBuilder
title: Interface DaiSession.CreationContext.VodInfoOrBuilder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:22.194790+00:00
---

# Interface DaiSession.CreationContext.VodInfoOrBuilder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiSession.CreationContext.VodInfoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DaiSession.CreationContext.VodInfoOrBuilder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface DaiSession.CreationContext.VodInfoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCmsId()
    
    
    public abstract long getCmsId()

Output only. The identifier of the content source from which Google Ad Manager ingested the Content resource associated with this session. For more information, see [Create a content source for video on demand](https://support.google.com/admanager/answer/7064112).

`optional int64 cms_id = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The cmsId.  
  
### getContent()
    
    
    public abstract String getContent()

Output only. The name field of the VOD Content resource.

` optional string content = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The content.  
  
### getContentBytes()
    
    
    public abstract ByteString getContentBytes()

Output only. The name field of the VOD Content resource.

` optional string content = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for content.  
  
### getContentDuration()
    
    
    public abstract Duration getContentDuration()

Output only. The VOD Content.duration field. Represents the duration of the content without ads.

` .google.protobuf.Duration content_duration = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The contentDuration.  
  
### getContentDurationOrBuilder()
    
    
    public abstract DurationOrBuilder getContentDurationOrBuilder()

Output only. The VOD Content.duration field. Represents the duration of the content without ads.

` .google.protobuf.Duration content_duration = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getCuePoints(int index)
    
    
    public abstract long getCuePoints(int index)

Output only. The cue points detected in the ingested VOD content manifest. Stored in milliseconds starting from the beginning of the content.

`repeated int64 cue_points = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The cuePoints at the given index.  
  
### getCuePointsCount()
    
    
    public abstract int getCuePointsCount()

Output only. The cue points detected in the ingested VOD content manifest. Stored in milliseconds starting from the beginning of the content.

`repeated int64 cue_points = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of cuePoints.  
  
### getCuePointsList()
    
    
    public abstract List<Long> getCuePointsList()

Output only. The cue points detected in the ingested VOD content manifest. Stored in milliseconds starting from the beginning of the content.

`repeated int64 cue_points = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` | A list containing the cuePoints.  
  
### getVid()
    
    
    public abstract String getVid()

Output only. The video ID of the Content resource that this session is associated with. This value is the same as the CmsContent.cms_content_id field. For details, see [Content ingestion and best practices](https://support.google.com/admanager/answer/6057894).

`optional string vid = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The vid.  
  
### getVidBytes()
    
    
    public abstract ByteString getVidBytes()

Output only. The video ID of the Content resource that this session is associated with. This value is the same as the CmsContent.cms_content_id field. For details, see [Content ingestion and best practices](https://support.google.com/admanager/answer/6057894).

`optional string vid = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for vid.  
  
### hasCmsId()
    
    
    public abstract boolean hasCmsId()

Output only. The identifier of the content source from which Google Ad Manager ingested the Content resource associated with this session. For more information, see [Create a content source for video on demand](https://support.google.com/admanager/answer/7064112).

`optional int64 cms_id = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cmsId field is set.  
  
### hasContent()
    
    
    public abstract boolean hasContent()

Output only. The name field of the VOD Content resource.

` optional string content = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the content field is set.  
  
### hasContentDuration()
    
    
    public abstract boolean hasContentDuration()

Output only. The VOD Content.duration field. Represents the duration of the content without ads.

` .google.protobuf.Duration content_duration = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the contentDuration field is set.  
  
### hasVid()
    
    
    public abstract boolean hasVid()

Output only. The video ID of the Content resource that this session is associated with. This value is the same as the CmsContent.cms_content_id field. For details, see [Content ingestion and best practices](https://support.google.com/admanager/answer/6057894).

`optional string vid = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the vid field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
