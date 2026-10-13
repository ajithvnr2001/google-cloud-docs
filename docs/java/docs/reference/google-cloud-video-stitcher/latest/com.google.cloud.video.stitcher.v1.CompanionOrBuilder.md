---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CompanionOrBuilder
title: Interface CompanionOrBuilder (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:09.706335+00:00
---

# Interface CompanionOrBuilder (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CompanionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CompanionOrBuilder (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.6  0.1.2 
    
    
    public interface CompanionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAdResourceCase()
    
    
    public abstract Companion.AdResourceCase getAdResourceCase()

**Returns**  
---  
**Type** | **Description**  
`[Companion.AdResourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Companion.AdResourceCase)` |   
  
### getAdSlotId()
    
    
    public abstract String getAdSlotId()

The ID used to identify the desired placement on a publisher's page. Values to be used should be discussed between publishers and advertisers.

`string ad_slot_id = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The adSlotId.  
  
### getAdSlotIdBytes()
    
    
    public abstract ByteString getAdSlotIdBytes()

The ID used to identify the desired placement on a publisher's page. Values to be used should be discussed between publishers and advertisers.

`string ad_slot_id = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for adSlotId.  
  
### getApiFramework()
    
    
    public abstract String getApiFramework()

The API necessary to communicate with the creative if available.

`string api_framework = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The apiFramework.  
  
### getApiFrameworkBytes()
    
    
    public abstract ByteString getApiFrameworkBytes()

The API necessary to communicate with the creative if available.

`string api_framework = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for apiFramework.  
  
### getAssetHeightPx()
    
    
    public abstract int getAssetHeightPx()

The pixel height of the creative.

`int32 asset_height_px = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The assetHeightPx.  
  
### getAssetWidthPx()
    
    
    public abstract int getAssetWidthPx()

The pixel width of the creative.

`int32 asset_width_px = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The assetWidthPx.  
  
### getEvents(int index)
    
    
    public abstract Event getEvents(int index)

The list of tracking events for the companion.

`repeated .google.cloud.video.stitcher.v1.Event events = 9;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Event)` |   
  
### getEventsCount()
    
    
    public abstract int getEventsCount()

The list of tracking events for the companion.

`repeated .google.cloud.video.stitcher.v1.Event events = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getEventsList()
    
    
    public abstract List<Event> getEventsList()

The list of tracking events for the companion.

`repeated .google.cloud.video.stitcher.v1.Event events = 9;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Event)>` |   
  
### getEventsOrBuilder(int index)
    
    
    public abstract EventOrBuilder getEventsOrBuilder(int index)

The list of tracking events for the companion.

`repeated .google.cloud.video.stitcher.v1.Event events = 9;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EventOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.EventOrBuilder)` |   
  
### getEventsOrBuilderList()
    
    
    public abstract List<? extends EventOrBuilder> getEventsOrBuilderList()

The list of tracking events for the companion.

`repeated .google.cloud.video.stitcher.v1.Event events = 9;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.video.stitcher.v1.EventOrBuilder>` |   
  
### getExpandedHeightPx()
    
    
    public abstract int getExpandedHeightPx()

The maximum pixel height of the creative in its expanded state.

`int32 expanded_height_px = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The expandedHeightPx.  
  
### getExpandedWidthPx()
    
    
    public abstract int getExpandedWidthPx()

The maximum pixel width of the creative in its expanded state.

`int32 expanded_width_px = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The expandedWidthPx.  
  
### getHeightPx()
    
    
    public abstract int getHeightPx()

The pixel height of the placement slot for the intended creative.

`int32 height_px = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The heightPx.  
  
### getHtmlAdResource()
    
    
    public abstract HtmlAdResource getHtmlAdResource()

The HTML ad resource associated with the companion ad.

`.google.cloud.video.stitcher.v1.HtmlAdResource html_ad_resource = 12;`

**Returns**  
---  
**Type** | **Description**  
`[HtmlAdResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.HtmlAdResource)` | The htmlAdResource.  
  
### getHtmlAdResourceOrBuilder()
    
    
    public abstract HtmlAdResourceOrBuilder getHtmlAdResourceOrBuilder()

The HTML ad resource associated with the companion ad.

`.google.cloud.video.stitcher.v1.HtmlAdResource html_ad_resource = 12;`

**Returns**  
---  
**Type** | **Description**  
`[HtmlAdResourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.HtmlAdResourceOrBuilder)` |   
  
### getIframeAdResource()
    
    
    public abstract IframeAdResource getIframeAdResource()

The IFrame ad resource associated with the companion ad.

`.google.cloud.video.stitcher.v1.IframeAdResource iframe_ad_resource = 10;`

**Returns**  
---  
**Type** | **Description**  
`[IframeAdResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.IframeAdResource)` | The iframeAdResource.  
  
### getIframeAdResourceOrBuilder()
    
    
    public abstract IframeAdResourceOrBuilder getIframeAdResourceOrBuilder()

The IFrame ad resource associated with the companion ad.

`.google.cloud.video.stitcher.v1.IframeAdResource iframe_ad_resource = 10;`

**Returns**  
---  
**Type** | **Description**  
`[IframeAdResourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.IframeAdResourceOrBuilder)` |   
  
### getStaticAdResource()
    
    
    public abstract StaticAdResource getStaticAdResource()

The static ad resource associated with the companion ad.

`.google.cloud.video.stitcher.v1.StaticAdResource static_ad_resource = 11;`

**Returns**  
---  
**Type** | **Description**  
`[StaticAdResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.StaticAdResource)` | The staticAdResource.  
  
### getStaticAdResourceOrBuilder()
    
    
    public abstract StaticAdResourceOrBuilder getStaticAdResourceOrBuilder()

The static ad resource associated with the companion ad.

`.google.cloud.video.stitcher.v1.StaticAdResource static_ad_resource = 11;`

**Returns**  
---  
**Type** | **Description**  
`[StaticAdResourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.StaticAdResourceOrBuilder)` |   
  
### getWidthPx()
    
    
    public abstract int getWidthPx()

The pixel width of the placement slot for the intended creative.

`int32 width_px = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The widthPx.  
  
### hasHtmlAdResource()
    
    
    public abstract boolean hasHtmlAdResource()

The HTML ad resource associated with the companion ad.

`.google.cloud.video.stitcher.v1.HtmlAdResource html_ad_resource = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the htmlAdResource field is set.  
  
### hasIframeAdResource()
    
    
    public abstract boolean hasIframeAdResource()

The IFrame ad resource associated with the companion ad.

`.google.cloud.video.stitcher.v1.IframeAdResource iframe_ad_resource = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the iframeAdResource field is set.  
  
### hasStaticAdResource()
    
    
    public abstract boolean hasStaticAdResource()

The static ad resource associated with the companion ad.

`.google.cloud.video.stitcher.v1.StaticAdResource static_ad_resource = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the staticAdResource field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
