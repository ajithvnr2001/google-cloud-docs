---
url: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.TargetingType
title: Enum TargetingType (0.20.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:37.014225+00:00
---

# Enum TargetingType (0.20.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.TargetingType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum TargetingType (0.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.16.0  0.15.0  0.14.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public enum TargetingType extends Enum<TargetingType> implements ProtocolMessageEnum

The type of targeting used to serve the ad.

Protobuf enum `google.ads.datamanager.v1.TargetingType`

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
`TARGETING_TYPE_AUDIENCE` |  Audience targeting. `TARGETING_TYPE_AUDIENCE = 1;`  
`TARGETING_TYPE_AUDIENCE_VALUE` |  Audience targeting. `TARGETING_TYPE_AUDIENCE = 1;`  
`TARGETING_TYPE_CONTEXTUAL` |  Contextual targeting. `TARGETING_TYPE_CONTEXTUAL = 2;`  
`TARGETING_TYPE_CONTEXTUAL_VALUE` |  Contextual targeting. `TARGETING_TYPE_CONTEXTUAL = 2;`  
`TARGETING_TYPE_DEMOGRAPHIC` |  Demographic targeting. `TARGETING_TYPE_DEMOGRAPHIC = 3;`  
`TARGETING_TYPE_DEMOGRAPHIC_VALUE` |  Demographic targeting. `TARGETING_TYPE_DEMOGRAPHIC = 3;`  
`TARGETING_TYPE_DEVICE` |  Device targeting. `TARGETING_TYPE_DEVICE = 4;`  
`TARGETING_TYPE_DEVICE_VALUE` |  Device targeting. `TARGETING_TYPE_DEVICE = 4;`  
`TARGETING_TYPE_GEO` |  Geo targeting. `TARGETING_TYPE_GEO = 5;`  
`TARGETING_TYPE_GEO_VALUE` |  Geo targeting. `TARGETING_TYPE_GEO = 5;`  
`TARGETING_TYPE_INTEREST` |  Interest targeting. `TARGETING_TYPE_INTEREST = 6;`  
`TARGETING_TYPE_INTEREST_VALUE` |  Interest targeting. `TARGETING_TYPE_INTEREST = 6;`  
`TARGETING_TYPE_PURCHASE_INTENT` |  Purchase intent targeting. `TARGETING_TYPE_PURCHASE_INTENT = 7;`  
`TARGETING_TYPE_PURCHASE_INTENT_VALUE` |  Purchase intent targeting. `TARGETING_TYPE_PURCHASE_INTENT = 7;`  
`TARGETING_TYPE_REMARKETING` |  Remarketing targeting. `TARGETING_TYPE_REMARKETING = 8;`  
`TARGETING_TYPE_REMARKETING_VALUE` |  Remarketing targeting. `TARGETING_TYPE_REMARKETING = 8;`  
`TARGETING_TYPE_UNSPECIFIED` |  Unspecified targeting type. `TARGETING_TYPE_UNSPECIFIED = 0;`  
`TARGETING_TYPE_UNSPECIFIED_VALUE` |  Unspecified targeting type. `TARGETING_TYPE_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.TargetingType#com_google_ads_datamanager_v1_TargetingType_forNumber_int_) instead._  
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
