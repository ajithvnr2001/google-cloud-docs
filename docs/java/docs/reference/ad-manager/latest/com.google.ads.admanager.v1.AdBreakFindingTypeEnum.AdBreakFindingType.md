---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreakFindingTypeEnum.AdBreakFindingType
title: Enum AdBreakFindingTypeEnum.AdBreakFindingType (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:57.149824+00:00
---

# Enum AdBreakFindingTypeEnum.AdBreakFindingType (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreakFindingTypeEnum.AdBreakFindingType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum AdBreakFindingTypeEnum.AdBreakFindingType (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public enum AdBreakFindingTypeEnum.AdBreakFindingType extends Enum<AdBreakFindingTypeEnum.AdBreakFindingType> implements ProtocolMessageEnum

A finding that occurred while serving an ad break for a session.

Protobuf enum `google.ads.admanager.v1.AdBreakFindingTypeEnum.AdBreakFindingType`

## Implements

[ProtocolMessageEnum](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolMessageEnum.html)

## Inherited Members

[Enum.<T>valueOf(Class<T>,String)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.Class-java.lang.String-)

[Enum.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#clone--)

[Enum.compareTo(E)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#compareTo-E-)

[Enum.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#equals-java.lang.Object-)

[Enum.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#finalize--)

[Enum.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#getDeclaringClass--)

[Enum.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#hashCode--)

[Enum.name()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#name--)

[Enum.ordinal()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#ordinal--)

[Enum.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#toString--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields   
  
---  
**Name** | **Description**  
`ADS_STATUS_ALL_ADS_MISSING_ASSETS` |  Ad pod was dropped due to all of the ads in the pod missing their assets, probably due to the assets not yet being transcoded. `ADS_STATUS_ALL_ADS_MISSING_ASSETS = 5;`  
`ADS_STATUS_ALL_ADS_MISSING_ASSETS_VALUE` |  Ad pod was dropped due to all of the ads in the pod missing their assets, probably due to the assets not yet being transcoded. `ADS_STATUS_ALL_ADS_MISSING_ASSETS = 5;`  
`ADS_STATUS_DISABLED` |  Ads are disabled for this session. `ADS_STATUS_DISABLED = 7;`  
`ADS_STATUS_DISABLED_VALUE` |  Ads are disabled for this session. `ADS_STATUS_DISABLED = 7;`  
`ADS_STATUS_DROPPED_BREAK_DURATION_TOO_SHORT` |  The duration of the ad break was too short to request ads. `ADS_STATUS_DROPPED_BREAK_DURATION_TOO_SHORT = 15;`  
`ADS_STATUS_DROPPED_BREAK_DURATION_TOO_SHORT_VALUE` |  The duration of the ad break was too short to request ads. `ADS_STATUS_DROPPED_BREAK_DURATION_TOO_SHORT = 15;`  
`ADS_STATUS_DROPPED_FOR_MIDROLL` |  The requested pre-roll break would overlap with a mid-roll ad break. `ADS_STATUS_DROPPED_FOR_MIDROLL = 14;`  
`ADS_STATUS_DROPPED_FOR_MIDROLL_VALUE` |  The requested pre-roll break would overlap with a mid-roll ad break. `ADS_STATUS_DROPPED_FOR_MIDROLL = 14;`  
`ADS_STATUS_DROPPED_FOR_PREROLL` |  The midroll ad break was skipped due to overlapping with preroll. `ADS_STATUS_DROPPED_FOR_PREROLL = 4;`  
`ADS_STATUS_DROPPED_FOR_PREROLL_VALUE` |  The midroll ad break was skipped due to overlapping with preroll. `ADS_STATUS_DROPPED_FOR_PREROLL = 4;`  
`ADS_STATUS_DROPPED_MEDIA_ANALYSIS_UNAVAILABLE` |  Information about the content stream that is required to stitch the ads is missing or unavailable. `ADS_STATUS_DROPPED_MEDIA_ANALYSIS_UNAVAILABLE = 17;`  
`ADS_STATUS_DROPPED_MEDIA_ANALYSIS_UNAVAILABLE_VALUE` |  Information about the content stream that is required to stitch the ads is missing or unavailable. `ADS_STATUS_DROPPED_MEDIA_ANALYSIS_UNAVAILABLE = 17;`  
`ADS_STATUS_DROPPED_SLATE_UNAVAILABLE` |  Ad pod was dropped because slate was unavailable and underlying content was stitched instead. `ADS_STATUS_DROPPED_SLATE_UNAVAILABLE = 11;`  
`ADS_STATUS_DROPPED_SLATE_UNAVAILABLE_VALUE` |  Ad pod was dropped because slate was unavailable and underlying content was stitched instead. `ADS_STATUS_DROPPED_SLATE_UNAVAILABLE = 11;`  
`ADS_STATUS_DROPPED_STREAM_CREATED_AFTER_BREAK` |  Session created after the ad break ended. `ADS_STATUS_DROPPED_STREAM_CREATED_AFTER_BREAK = 16;`  
`ADS_STATUS_DROPPED_STREAM_CREATED_AFTER_BREAK_VALUE` |  Session created after the ad break ended. `ADS_STATUS_DROPPED_STREAM_CREATED_AFTER_BREAK = 16;`  
`ADS_STATUS_EXPIRED` |  Ad pod expired because the ad request couldn't finish before the deadline. `ADS_STATUS_EXPIRED = 9;`  
`ADS_STATUS_EXPIRED_VALUE` |  Ad pod expired because the ad request couldn't finish before the deadline. `ADS_STATUS_EXPIRED = 9;`  
`ADS_STATUS_HOLIDAY` |  Ad pod occurred within the configured ad holiday. `ADS_STATUS_HOLIDAY = 10;`  
`ADS_STATUS_HOLIDAY_VALUE` |  Ad pod occurred within the configured ad holiday. `ADS_STATUS_HOLIDAY = 10;`  
`ADS_STATUS_INVALID_POD_REQUEST` |  Ad pod was dropped due to an invalid pod request. `ADS_STATUS_INVALID_POD_REQUEST = 13;`  
`ADS_STATUS_INVALID_POD_REQUEST_VALUE` |  Ad pod was dropped due to an invalid pod request. `ADS_STATUS_INVALID_POD_REQUEST = 13;`  
`ADS_STATUS_NO_ADS_AVAILABLE_BEFORE_DEADLINE` |  Ad pod was dropped because there were no ads available before the deadline. `ADS_STATUS_NO_ADS_AVAILABLE_BEFORE_DEADLINE = 12;`  
`ADS_STATUS_NO_ADS_AVAILABLE_BEFORE_DEADLINE_VALUE` |  Ad pod was dropped because there were no ads available before the deadline. `ADS_STATUS_NO_ADS_AVAILABLE_BEFORE_DEADLINE = 12;`  
`ADS_STATUS_OUT_OF_WINDOW` |  Ad pod is outside of the window at session creation time so ad pod was skipped and underlying content was stitched instead. `ADS_STATUS_OUT_OF_WINDOW = 6;`  
`ADS_STATUS_OUT_OF_WINDOW_VALUE` |  Ad pod is outside of the window at session creation time so ad pod was skipped and underlying content was stitched instead. `ADS_STATUS_OUT_OF_WINDOW = 6;`  
`ADS_STATUS_STORAGE_ERROR` |  Decisioned ad pod couldn't be fetched from storage. `ADS_STATUS_STORAGE_ERROR = 8;`  
`ADS_STATUS_STORAGE_ERROR_VALUE` |  Decisioned ad pod couldn't be fetched from storage. `ADS_STATUS_STORAGE_ERROR = 8;`  
`ADS_STATUS_UNKNOWN` |  The serving or insertion status of the ad break is unknown. `ADS_STATUS_UNKNOWN = 18;`  
`ADS_STATUS_UNKNOWN_VALUE` |  The serving or insertion status of the ad break is unknown. `ADS_STATUS_UNKNOWN = 18;`  
`AD_BREAK_FINDING_TYPE_UNSPECIFIED` |  Default value. `AD_BREAK_FINDING_TYPE_UNSPECIFIED = 0;`  
`AD_BREAK_FINDING_TYPE_UNSPECIFIED_VALUE` |  Default value. `AD_BREAK_FINDING_TYPE_UNSPECIFIED = 0;`  
`AD_POD_DROPPED_TOO_MANY_AD_PODS` |  Ad pod was dropped, the number of ad breaks is less than the number of decisioned ad pods. `AD_POD_DROPPED_TOO_MANY_AD_PODS = 2;`  
`AD_POD_DROPPED_TOO_MANY_AD_PODS_VALUE` |  Ad pod was dropped, the number of ad breaks is less than the number of decisioned ad pods. `AD_POD_DROPPED_TOO_MANY_AD_PODS = 2;`  
`EXCEEDS_MAX_FILLER` |  Ad pod doesn't contain enough ads - requires more filler than specified. `EXCEEDS_MAX_FILLER = 3;`  
`EXCEEDS_MAX_FILLER_VALUE` |  Ad pod doesn't contain enough ads - requires more filler than specified. `EXCEEDS_MAX_FILLER = 3;`  
`INTERNAL_ERROR` |  Internal DAI error. `INTERNAL_ERROR = 1;`  
`INTERNAL_ERROR_VALUE` |  Internal DAI error. `INTERNAL_ERROR = 1;`  
`PREROLL_AUDIO_VIDEO_MISALIGNMENT` |  The content segment boundary at the end of the preroll has misaligned video and audio segments. `PREROLL_AUDIO_VIDEO_MISALIGNMENT = 20;`  
`PREROLL_AUDIO_VIDEO_MISALIGNMENT_VALUE` |  The content segment boundary at the end of the preroll has misaligned video and audio segments. `PREROLL_AUDIO_VIDEO_MISALIGNMENT = 20;`  
`UNRECOGNIZED` |   
`UNSERVED_BREAK` |  Ad break was not served. `UNSERVED_BREAK = 19;`  
`UNSERVED_BREAK_VALUE` |  Ad break was not served. `UNSERVED_BREAK = 19;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreakFindingTypeEnum.AdBreakFindingType#com_google_ads_admanager_v1_AdBreakFindingTypeEnum_AdBreakFindingType_forNumber_int_) instead._  
`valueOf(String name)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`getDescriptorForType()` |   
`getNumber()` |   
`getValueDescriptor()` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
