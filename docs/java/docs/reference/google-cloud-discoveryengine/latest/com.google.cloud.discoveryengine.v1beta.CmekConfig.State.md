---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.CmekConfig.State
title: Enum CmekConfig.State (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:04.877264+00:00
---

# Enum CmekConfig.State (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.CmekConfig.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum CmekConfig.State (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public enum CmekConfig.State extends Enum<CmekConfig.State> implements ProtocolMessageEnum

States of the CmekConfig.

Protobuf enum `google.cloud.discoveryengine.v1beta.CmekConfig.State`

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
`ACTIVE` |  The CmekConfig can be used with DataStores. `ACTIVE = 2;`  
`ACTIVE_ROTATING` |  The KMS key version is being rotated. `ACTIVE_ROTATING = 6;`  
`ACTIVE_ROTATING_VALUE` |  The KMS key version is being rotated. `ACTIVE_ROTATING = 6;`  
`ACTIVE_VALUE` |  The CmekConfig can be used with DataStores. `ACTIVE = 2;`  
`CREATING` |  The CmekConfig is creating. `CREATING = 1;`  
`CREATING_VALUE` |  The CmekConfig is creating. `CREATING = 1;`  
`DELETED` |  The KMS key is soft deleted. Some cleanup policy will eventually be applied. `DELETED = 8;`  
`DELETED_VALUE` |  The KMS key is soft deleted. Some cleanup policy will eventually be applied. `DELETED = 8;`  
`DELETE_FAILED` |  The CmekConfig deletion process failed. `DELETE_FAILED = 7;`  
`DELETE_FAILED_VALUE` |  The CmekConfig deletion process failed. `DELETE_FAILED = 7;`  
`DELETING` |  The CmekConfig is deleting. `DELETING = 4;`  
`DELETING_VALUE` |  The CmekConfig is deleting. `DELETING = 4;`  
`EXPIRED` |  The KMS key is expired, meaning the key has been disabled for 30+ days. The customer can call DeleteCmekConfig to change the state to DELETED. `EXPIRED = 9;`  
`EXPIRED_VALUE` |  The KMS key is expired, meaning the key has been disabled for 30+ days. The customer can call DeleteCmekConfig to change the state to DELETED. `EXPIRED = 9;`  
`KEY_ISSUE` |  The CmekConfig is unavailable, most likely due to the KMS Key being revoked. `KEY_ISSUE = 3;`  
`KEY_ISSUE_VALUE` |  The CmekConfig is unavailable, most likely due to the KMS Key being revoked. `KEY_ISSUE = 3;`  
`STATE_UNSPECIFIED` |  The CmekConfig state is unknown. `STATE_UNSPECIFIED = 0;`  
`STATE_UNSPECIFIED_VALUE` |  The CmekConfig state is unknown. `STATE_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
`UNUSABLE` |  The CmekConfig is not usable, most likely due to some internal issue. `UNUSABLE = 5;`  
`UNUSABLE_VALUE` |  The CmekConfig is not usable, most likely due to some internal issue. `UNUSABLE = 5;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.CmekConfig.State#com_google_cloud_discoveryengine_v1beta_CmekConfig_State_forNumber_int_) instead._  
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
