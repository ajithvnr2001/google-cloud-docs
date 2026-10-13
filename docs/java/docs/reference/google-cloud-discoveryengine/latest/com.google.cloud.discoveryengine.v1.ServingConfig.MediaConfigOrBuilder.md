---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ServingConfig.MediaConfigOrBuilder
title: Interface ServingConfig.MediaConfigOrBuilder (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:30.840667+00:00
---

# Interface ServingConfig.MediaConfigOrBuilder (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ServingConfig.MediaConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ServingConfig.MediaConfigOrBuilder (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface ServingConfig.MediaConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getContentFreshnessCutoffDays()
    
    
    public abstract int getContentFreshnessCutoffDays()

Specifies the content freshness used for recommendation result. Contents will be demoted if contents were published for more than content freshness cutoff days.

`int32 content_freshness_cutoff_days = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The contentFreshnessCutoffDays.  
  
### getContentWatchedPercentageThreshold()
    
    
    public abstract float getContentWatchedPercentageThreshold()

Specifies the content watched percentage threshold for demotion. Threshold value must be between [0, 1.0] inclusive.

`float content_watched_percentage_threshold = 2;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The contentWatchedPercentageThreshold.  
  
### getContentWatchedSecondsThreshold()
    
    
    public abstract float getContentWatchedSecondsThreshold()

Specifies the content watched minutes threshold for demotion.

`float content_watched_seconds_threshold = 5;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The contentWatchedSecondsThreshold.  
  
### getDemoteContentWatchedCase()
    
    
    public abstract ServingConfig.MediaConfig.DemoteContentWatchedCase getDemoteContentWatchedCase()

**Returns**  
---  
**Type** | **Description**  
`[ServingConfig.MediaConfig.DemoteContentWatchedCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ServingConfig.MediaConfig.DemoteContentWatchedCase)` |   
  
### getDemoteContentWatchedPastDays()
    
    
    public abstract int getDemoteContentWatchedPastDays()

Optional. Specifies the number of days to look back for demoting watched content. If set to zero or unset, defaults to the maximum of 365 days.

`int32 demote_content_watched_past_days = 37 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The demoteContentWatchedPastDays.  
  
### getDemotionEventType()
    
    
    public abstract String getDemotionEventType()

Specifies the event type used for demoting recommendation result. Currently supported values:

  * `view-item`: Item viewed.
  * `media-play`: Start/resume watching a video, playing a song, etc.
  * `media-complete`: Finished or stopped midway through a video, song, etc.

If unset, watch history demotion will not be applied. Content freshness demotion will still be applied.




`string demotion_event_type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The demotionEventType.  
  
### getDemotionEventTypeBytes()
    
    
    public abstract ByteString getDemotionEventTypeBytes()

Specifies the event type used for demoting recommendation result. Currently supported values:

  * `view-item`: Item viewed.
  * `media-play`: Start/resume watching a video, playing a song, etc.
  * `media-complete`: Finished or stopped midway through a video, song, etc.

If unset, watch history demotion will not be applied. Content freshness demotion will still be applied.




`string demotion_event_type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for demotionEventType.  
  
### hasContentWatchedPercentageThreshold()
    
    
    public abstract boolean hasContentWatchedPercentageThreshold()

Specifies the content watched percentage threshold for demotion. Threshold value must be between [0, 1.0] inclusive.

`float content_watched_percentage_threshold = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the contentWatchedPercentageThreshold field is set.  
  
### hasContentWatchedSecondsThreshold()
    
    
    public abstract boolean hasContentWatchedSecondsThreshold()

Specifies the content watched minutes threshold for demotion.

`float content_watched_seconds_threshold = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the contentWatchedSecondsThreshold field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
