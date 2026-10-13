---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRequestFindingTypeEnum.AdRequestFindingType
title: Enum AdRequestFindingTypeEnum.AdRequestFindingType (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:43:44.957649+00:00
---

# Enum AdRequestFindingTypeEnum.AdRequestFindingType (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRequestFindingTypeEnum.AdRequestFindingType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum AdRequestFindingTypeEnum.AdRequestFindingType (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public enum AdRequestFindingTypeEnum.AdRequestFindingType extends Enum<AdRequestFindingTypeEnum.AdRequestFindingType> implements ProtocolMessageEnum

A finding that occurred while making an ad request.

Protobuf enum `google.ads.admanager.v1.AdRequestFindingTypeEnum.AdRequestFindingType`

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
`AD_BREAK_TYPE_NOT_SUPPORTED` |  VMAP contains an adbreak that is not supported. `AD_BREAK_TYPE_NOT_SUPPORTED = 14;`  
`AD_BREAK_TYPE_NOT_SUPPORTED_VALUE` |  VMAP contains an adbreak that is not supported. `AD_BREAK_TYPE_NOT_SUPPORTED = 14;`  
`AD_REQUEST_ERROR` |  An error while making an ad request. `AD_REQUEST_ERROR = 2;`  
`AD_REQUEST_ERROR_VALUE` |  An error while making an ad request. `AD_REQUEST_ERROR = 2;`  
`AD_REQUEST_FINDING_TYPE_UNSPECIFIED` |  Default value. `AD_REQUEST_FINDING_TYPE_UNSPECIFIED = 0;`  
`AD_REQUEST_FINDING_TYPE_UNSPECIFIED_VALUE` |  Default value. `AD_REQUEST_FINDING_TYPE_UNSPECIFIED = 0;`  
`AD_REQUEST_TIMEOUT` |  The request has timed out. `AD_REQUEST_TIMEOUT = 17;`  
`AD_REQUEST_TIMEOUT_VALUE` |  The request has timed out. `AD_REQUEST_TIMEOUT = 17;`  
`AD_TAG_PARSE_ERROR` |  Error while parsing ad tag. `AD_TAG_PARSE_ERROR = 9;`  
`AD_TAG_PARSE_ERROR_VALUE` |  Error while parsing ad tag. `AD_TAG_PARSE_ERROR = 9;`  
`CANNOT_FIND_UNIQUE_TRANSCODE_ID` |  Ad element does not contain enough information to generate a unique transcode ID. `CANNOT_FIND_UNIQUE_TRANSCODE_ID = 5;`  
`CANNOT_FIND_UNIQUE_TRANSCODE_ID_VALUE` |  Ad element does not contain enough information to generate a unique transcode ID. `CANNOT_FIND_UNIQUE_TRANSCODE_ID = 5;`  
`CUSTOM_AD_SOURCE_IN_VMAP` |  VMAP contains custom ad source which is not supported. `CUSTOM_AD_SOURCE_IN_VMAP = 13;`  
`CUSTOM_AD_SOURCE_IN_VMAP_VALUE` |  VMAP contains custom ad source which is not supported. `CUSTOM_AD_SOURCE_IN_VMAP = 13;`  
`DUPLICATE_AD_TAG` |  The same ad tag was already used in the same pod. `DUPLICATE_AD_TAG = 18;`  
`DUPLICATE_AD_TAG_VALUE` |  The same ad tag was already used in the same pod. `DUPLICATE_AD_TAG = 18;`  
`FOLLOW_REDIRECTS_IS_FALSE` |  VMAP AdSource followRedirects is set as false. `FOLLOW_REDIRECTS_IS_FALSE = 19;`  
`FOLLOW_REDIRECTS_IS_FALSE_VALUE` |  VMAP AdSource followRedirects is set as false. `FOLLOW_REDIRECTS_IS_FALSE = 19;`  
`INTERNAL_ERROR` |  Internal DAI error. `INTERNAL_ERROR = 1;`  
`INTERNAL_ERROR_VALUE` |  Internal DAI error. `INTERNAL_ERROR = 1;`  
`INVALID_VMAP_RESPONSE` |  Invalid VMAP data (Able to parse VMAP but XML attributes have invalid data). `INVALID_VMAP_RESPONSE = 11;`  
`INVALID_VMAP_RESPONSE_VALUE` |  Invalid VMAP data (Able to parse VMAP but XML attributes have invalid data). `INVALID_VMAP_RESPONSE = 11;`  
`MAX_WRAPPER_DEPTH_REACHED` |  Reached the maximum number of VAST redirects. `MAX_WRAPPER_DEPTH_REACHED = 8;`  
`MAX_WRAPPER_DEPTH_REACHED_VALUE` |  Reached the maximum number of VAST redirects. `MAX_WRAPPER_DEPTH_REACHED = 8;`  
`MISSING_INLINE_ELEMENTS` |  No InLine elements found in the Ad. `MISSING_INLINE_ELEMENTS = 7;`  
`MISSING_INLINE_ELEMENTS_VALUE` |  No InLine elements found in the Ad. `MISSING_INLINE_ELEMENTS = 7;`  
`NEITHER_AD_SOURCE_NOR_TRACKING` |  VMAP contains an adbreak that has neither ad source nor tracking events. `NEITHER_AD_SOURCE_NOR_TRACKING = 15;`  
`NEITHER_AD_SOURCE_NOR_TRACKING_VALUE` |  VMAP contains an adbreak that has neither ad source nor tracking events. `NEITHER_AD_SOURCE_NOR_TRACKING = 15;`  
`NO_AD_BREAKS_IN_VMAP` |  VMAP response contains no ad breaks. `NO_AD_BREAKS_IN_VMAP = 12;`  
`NO_AD_BREAKS_IN_VMAP_VALUE` |  VMAP response contains no ad breaks. `NO_AD_BREAKS_IN_VMAP = 12;`  
`NO_VALID_MEDIAFILES_FOUND` |  No media files were found in the VAST ad. `NO_VALID_MEDIAFILES_FOUND = 21;`  
`NO_VALID_MEDIAFILES_FOUND_VALUE` |  No media files were found in the VAST ad. `NO_VALID_MEDIAFILES_FOUND = 21;`  
`SKIPPABLE_AD_NOT_SUPPORTED` |  Client doesn't support skippable ads. The ad was a skippable ad. `SKIPPABLE_AD_NOT_SUPPORTED = 16;`  
`SKIPPABLE_AD_NOT_SUPPORTED_VALUE` |  Client doesn't support skippable ads. The ad was a skippable ad. `SKIPPABLE_AD_NOT_SUPPORTED = 16;`  
`UNRECOGNIZED` |   
`UNSUPPORTED_AD_SYSTEM` |  AdSystem reported in VAST is not supported. `UNSUPPORTED_AD_SYSTEM = 4;`  
`UNSUPPORTED_AD_SYSTEM_VALUE` |  AdSystem reported in VAST is not supported. `UNSUPPORTED_AD_SYSTEM = 4;`  
`UNSUPPORTED_VAST_VERSION` |  VAST version is not supported. `UNSUPPORTED_VAST_VERSION = 20;`  
`UNSUPPORTED_VAST_VERSION_VALUE` |  VAST version is not supported. `UNSUPPORTED_VAST_VERSION = 20;`  
`VAST_PARSE_ERROR` |  Generic VAST parsing error. `VAST_PARSE_ERROR = 3;`  
`VAST_PARSE_ERROR_VALUE` |  Generic VAST parsing error. `VAST_PARSE_ERROR = 3;`  
`VMAP_PARSE_ERROR` |  Generic VMAP parsing error. `VMAP_PARSE_ERROR = 10;`  
`VMAP_PARSE_ERROR_VALUE` |  Generic VMAP parsing error. `VMAP_PARSE_ERROR = 10;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRequestFindingTypeEnum.AdRequestFindingType#com_google_ads_admanager_v1_AdRequestFindingTypeEnum_AdRequestFindingType_forNumber_int_) instead._  
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
