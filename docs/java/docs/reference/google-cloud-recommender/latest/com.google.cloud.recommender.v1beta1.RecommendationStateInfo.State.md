---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.RecommendationStateInfo.State
title: Enum RecommendationStateInfo.State (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:28.230987+00:00
---

# Enum RecommendationStateInfo.State (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.RecommendationStateInfo.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum RecommendationStateInfo.State (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.7  2.4.1  2.3.0  2.2.0  2.1.5 
    
    
    public enum RecommendationStateInfo.State extends Enum<RecommendationStateInfo.State> implements ProtocolMessageEnum

Represents Recommendation State.

Protobuf enum `google.cloud.recommender.v1beta1.RecommendationStateInfo.State`

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
`ACTIVE` |  Recommendation is active and can be applied. Recommendations content can be updated by Google. ACTIVE recommendations can be marked as CLAIMED, SUCCEEDED, or FAILED. `ACTIVE = 1;`  
`ACTIVE_VALUE` |  Recommendation is active and can be applied. Recommendations content can be updated by Google. ACTIVE recommendations can be marked as CLAIMED, SUCCEEDED, or FAILED. `ACTIVE = 1;`  
`CLAIMED` |  Recommendation is in claimed state. Recommendations content is immutable and cannot be updated by Google. CLAIMED recommendations can be marked as CLAIMED, SUCCEEDED, or FAILED. `CLAIMED = 6;`  
`CLAIMED_VALUE` |  Recommendation is in claimed state. Recommendations content is immutable and cannot be updated by Google. CLAIMED recommendations can be marked as CLAIMED, SUCCEEDED, or FAILED. `CLAIMED = 6;`  
`DISMISSED` |  Recommendation is in dismissed state. Recommendation content can be updated by Google. DISMISSED recommendations can be marked as ACTIVE. `DISMISSED = 5;`  
`DISMISSED_VALUE` |  Recommendation is in dismissed state. Recommendation content can be updated by Google. DISMISSED recommendations can be marked as ACTIVE. `DISMISSED = 5;`  
`FAILED` |  Recommendation is in failed state. Recommendations content is immutable and cannot be updated by Google. FAILED recommendations can be marked as SUCCEEDED, or FAILED. `FAILED = 4;`  
`FAILED_VALUE` |  Recommendation is in failed state. Recommendations content is immutable and cannot be updated by Google. FAILED recommendations can be marked as SUCCEEDED, or FAILED. `FAILED = 4;`  
`STATE_UNSPECIFIED` |  Default state. Don't use directly. `STATE_UNSPECIFIED = 0;`  
`STATE_UNSPECIFIED_VALUE` |  Default state. Don't use directly. `STATE_UNSPECIFIED = 0;`  
`SUCCEEDED` |  Recommendation is in succeeded state. Recommendations content is immutable and cannot be updated by Google. SUCCEEDED recommendations can be marked as SUCCEEDED, or FAILED. `SUCCEEDED = 3;`  
`SUCCEEDED_VALUE` |  Recommendation is in succeeded state. Recommendations content is immutable and cannot be updated by Google. SUCCEEDED recommendations can be marked as SUCCEEDED, or FAILED. `SUCCEEDED = 3;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommender/latest/com.google.cloud.recommender.v1beta1.RecommendationStateInfo.State#com_google_cloud_recommender_v1beta1_RecommendationStateInfo_State_forNumber_int_) instead._  
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

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
