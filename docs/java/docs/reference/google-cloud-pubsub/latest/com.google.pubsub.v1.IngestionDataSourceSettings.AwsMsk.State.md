---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.AwsMsk.State
title: Enum IngestionDataSourceSettings.AwsMsk.State (1.157.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:02.336028+00:00
---

# Enum IngestionDataSourceSettings.AwsMsk.State (1.157.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.AwsMsk.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum IngestionDataSourceSettings.AwsMsk.State (1.157.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.157.0 (latest)  1.153.0  1.152.0  1.151.0  1.150.1  1.149.0  1.148.0  1.147.0  1.145.0  1.143.1  1.142.0  1.141.5  1.140.2  1.139.4  1.138.0  1.137.1  1.136.1  1.135.0  1.134.2  1.133.1  1.132.2  1.131.0  1.130.0  1.129.6  1.127.3  1.126.6  1.125.13  1.123.18  1.122.2  1.121.1  1.120.24  1.119.1  1.118.0  1.117.0  1.116.4  1.115.5 
    
    
    public enum IngestionDataSourceSettings.AwsMsk.State extends Enum<IngestionDataSourceSettings.AwsMsk.State> implements ProtocolMessageEnum

Possible states for managed ingestion from Amazon MSK.

Protobuf enum `google.pubsub.v1.IngestionDataSourceSettings.AwsMsk.State`

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
`ACTIVE` |  Ingestion is active. `ACTIVE = 1;`  
`ACTIVE_VALUE` |  Ingestion is active. `ACTIVE = 1;`  
`CLUSTER_NOT_FOUND` |  The provided MSK cluster wasn't found. `CLUSTER_NOT_FOUND = 4;`  
`CLUSTER_NOT_FOUND_VALUE` |  The provided MSK cluster wasn't found. `CLUSTER_NOT_FOUND = 4;`  
`CONFLICTING_REGION_CONSTRAINTS` |  Indicates an error state where the ingestion source cannot be processed because the selected ingestion region is not permitted by the Regional Access Boundary (RAB) restrictions on the project's service account. `CONFLICTING_REGION_CONSTRAINTS = 6;`  
`CONFLICTING_REGION_CONSTRAINTS_VALUE` |  Indicates an error state where the ingestion source cannot be processed because the selected ingestion region is not permitted by the Regional Access Boundary (RAB) restrictions on the project's service account. `CONFLICTING_REGION_CONSTRAINTS = 6;`  
`MSK_PERMISSION_DENIED` |  Permission denied encountered while consuming data from Amazon MSK. `MSK_PERMISSION_DENIED = 2;`  
`MSK_PERMISSION_DENIED_VALUE` |  Permission denied encountered while consuming data from Amazon MSK. `MSK_PERMISSION_DENIED = 2;`  
`PUBLISH_PERMISSION_DENIED` |  Permission denied encountered while publishing to the topic. `PUBLISH_PERMISSION_DENIED = 3;`  
`PUBLISH_PERMISSION_DENIED_VALUE` |  Permission denied encountered while publishing to the topic. `PUBLISH_PERMISSION_DENIED = 3;`  
`STATE_UNSPECIFIED` |  Default value. This value is unused. `STATE_UNSPECIFIED = 0;`  
`STATE_UNSPECIFIED_VALUE` |  Default value. This value is unused. `STATE_UNSPECIFIED = 0;`  
`TOPIC_NOT_FOUND` |  The provided topic wasn't found. `TOPIC_NOT_FOUND = 5;`  
`TOPIC_NOT_FOUND_VALUE` |  The provided topic wasn't found. `TOPIC_NOT_FOUND = 5;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.AwsMsk.State#com_google_pubsub_v1_IngestionDataSourceSettings_AwsMsk_State_forNumber_int_) instead._  
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
