---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance.State
title: Enum Instance.State (0.62.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:15:56.792783+00:00
---

# Enum Instance.State (0.62.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum Instance.State (0.62.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public enum Instance.State extends Enum<Instance.State> implements ProtocolMessageEnum

The possible states of a Parallelstore instance.

Protobuf enum `google.cloud.parallelstore.v1.Instance.State`

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
`ACTIVE` |  The instance is available for use. `ACTIVE = 2;`  
`ACTIVE_VALUE` |  The instance is available for use. `ACTIVE = 2;`  
`CREATING` |  The instance is being created. `CREATING = 1;`  
`CREATING_VALUE` |  The instance is being created. `CREATING = 1;`  
`DELETING` |  The instance is being deleted. `DELETING = 3;`  
`DELETING_VALUE` |  The instance is being deleted. `DELETING = 3;`  
`FAILED` |  The instance is not usable. `FAILED = 4;`  
`FAILED_VALUE` |  The instance is not usable. `FAILED = 4;`  
`REPAIRING` |  The instance is being repaired. This should only be used by instances using the `PERSISTENT` deployment type. `REPAIRING = 6;`  
`REPAIRING_VALUE` |  The instance is being repaired. This should only be used by instances using the `PERSISTENT` deployment type. `REPAIRING = 6;`  
`STATE_UNSPECIFIED` |  Not set. `STATE_UNSPECIFIED = 0;`  
`STATE_UNSPECIFIED_VALUE` |  Not set. `STATE_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
`UPGRADING` |  The instance is being upgraded. `UPGRADING = 5;`  
`UPGRADING_VALUE` |  The instance is being upgraded. `UPGRADING = 5;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1.Instance.State#com_google_cloud_parallelstore_v1_Instance_State_forNumber_int_) instead._  
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
