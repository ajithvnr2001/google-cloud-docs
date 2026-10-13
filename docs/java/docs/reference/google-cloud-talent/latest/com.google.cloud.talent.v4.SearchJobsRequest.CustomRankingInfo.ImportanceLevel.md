---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsRequest.CustomRankingInfo.ImportanceLevel
title: Enum SearchJobsRequest.CustomRankingInfo.ImportanceLevel (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:32.140302+00:00
---

# Enum SearchJobsRequest.CustomRankingInfo.ImportanceLevel (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsRequest.CustomRankingInfo.ImportanceLevel

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum SearchJobsRequest.CustomRankingInfo.ImportanceLevel (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.6  2.2.9 
    
    
    public enum SearchJobsRequest.CustomRankingInfo.ImportanceLevel extends Enum<SearchJobsRequest.CustomRankingInfo.ImportanceLevel> implements ProtocolMessageEnum

The importance level for CustomRankingInfo.ranking_expression.

Protobuf enum ` google.cloud.talent.v4.SearchJobsRequest.CustomRankingInfo.ImportanceLevel`

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
`EXTREME` |  The given ranking expression is of Extreme importance, and dominates job's final ranking position with existing relevance score (determined by API algorithm) ignored. `EXTREME = 6;`  
`EXTREME_VALUE` |  The given ranking expression is of Extreme importance, and dominates job's final ranking position with existing relevance score (determined by API algorithm) ignored. `EXTREME = 6;`  
`HIGH` |  The given ranking expression is of High importance in terms of job's final ranking position compared to existing relevance score (determined by API algorithm). `HIGH = 5;`  
`HIGH_VALUE` |  The given ranking expression is of High importance in terms of job's final ranking position compared to existing relevance score (determined by API algorithm). `HIGH = 5;`  
`IMPORTANCE_LEVEL_UNSPECIFIED` |  Default value if the importance level isn't specified. `IMPORTANCE_LEVEL_UNSPECIFIED = 0;`  
`IMPORTANCE_LEVEL_UNSPECIFIED_VALUE` |  Default value if the importance level isn't specified. `IMPORTANCE_LEVEL_UNSPECIFIED = 0;`  
`LOW` |  The given ranking expression is of Low importance in terms of job's final ranking position compared to existing relevance score (determined by API algorithm). `LOW = 2;`  
`LOW_VALUE` |  The given ranking expression is of Low importance in terms of job's final ranking position compared to existing relevance score (determined by API algorithm). `LOW = 2;`  
`MEDIUM` |  The given ranking expression is of Medium importance in terms of job's final ranking position compared to existing relevance score (determined by API algorithm). `MEDIUM = 4;`  
`MEDIUM_VALUE` |  The given ranking expression is of Medium importance in terms of job's final ranking position compared to existing relevance score (determined by API algorithm). `MEDIUM = 4;`  
`MILD` |  The given ranking expression is of Mild importance in terms of job's final ranking position compared to existing relevance score (determined by API algorithm). `MILD = 3;`  
`MILD_VALUE` |  The given ranking expression is of Mild importance in terms of job's final ranking position compared to existing relevance score (determined by API algorithm). `MILD = 3;`  
`NONE` |  The given ranking expression is of None importance, existing relevance score (determined by API algorithm) dominates job's final ranking position. `NONE = 1;`  
`NONE_VALUE` |  The given ranking expression is of None importance, existing relevance score (determined by API algorithm) dominates job's final ranking position. `NONE = 1;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsRequest.CustomRankingInfo.ImportanceLevel#com_google_cloud_talent_v4_SearchJobsRequest_CustomRankingInfo_ImportanceLevel_forNumber_int_) instead._  
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
