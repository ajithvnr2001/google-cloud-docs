---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Instance.State
title: Enum Instance.State (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:44.420610+00:00
---

# Enum Instance.State (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Instance.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum Instance.State (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.3  1.0.6  0.6.2 
    
    
    public enum Instance.State extends Enum<Instance.State> implements ProtocolMessageEnum

The definition of the states of this instance.

Protobuf enum `google.cloud.notebooks.v1beta1.Instance.State`

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
`ACTIVE` |  The instance is running. `ACTIVE = 3;`  
`ACTIVE_VALUE` |  The instance is running. `ACTIVE = 3;`  
`DELETED` |  The instance is deleted. `DELETED = 6;`  
`DELETED_VALUE` |  The instance is deleted. `DELETED = 6;`  
`INITIALIZING` |  The instance is being created. `INITIALIZING = 8;`  
`INITIALIZING_VALUE` |  The instance is being created. `INITIALIZING = 8;`  
`PROVISIONING` |  The control logic is installing required frameworks and registering the instance with notebook proxy `PROVISIONING = 2;`  
`PROVISIONING_VALUE` |  The control logic is installing required frameworks and registering the instance with notebook proxy `PROVISIONING = 2;`  
`REGISTERING` |  The instance is getting registered. `REGISTERING = 9;`  
`REGISTERING_VALUE` |  The instance is getting registered. `REGISTERING = 9;`  
`STARTING` |  The control logic is starting the instance. `STARTING = 1;`  
`STARTING_VALUE` |  The control logic is starting the instance. `STARTING = 1;`  
`STATE_UNSPECIFIED` |  State is not specified. `STATE_UNSPECIFIED = 0;`  
`STATE_UNSPECIFIED_VALUE` |  State is not specified. `STATE_UNSPECIFIED = 0;`  
`STOPPED` |  The instance is stopped. `STOPPED = 5;`  
`STOPPED_VALUE` |  The instance is stopped. `STOPPED = 5;`  
`STOPPING` |  The control logic is stopping the instance. `STOPPING = 4;`  
`STOPPING_VALUE` |  The control logic is stopping the instance. `STOPPING = 4;`  
`SUSPENDED` |  The instance is suspended. `SUSPENDED = 11;`  
`SUSPENDED_VALUE` |  The instance is suspended. `SUSPENDED = 11;`  
`SUSPENDING` |  The instance is suspending. `SUSPENDING = 10;`  
`SUSPENDING_VALUE` |  The instance is suspending. `SUSPENDING = 10;`  
`UNRECOGNIZED` |   
`UPGRADING` |  The instance is upgrading. `UPGRADING = 7;`  
`UPGRADING_VALUE` |  The instance is upgrading. `UPGRADING = 7;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Instance.State#com_google_cloud_notebooks_v1beta1_Instance_State_forNumber_int_) instead._  
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
