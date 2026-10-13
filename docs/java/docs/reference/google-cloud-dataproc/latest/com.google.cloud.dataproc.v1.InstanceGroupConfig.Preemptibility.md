---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Preemptibility
title: Enum InstanceGroupConfig.Preemptibility (4.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:51.386685+00:00
---

# Enum InstanceGroupConfig.Preemptibility (4.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Preemptibility

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum InstanceGroupConfig.Preemptibility (4.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.96.0 (latest)  4.92.0  4.91.1  4.90.0  4.88.0  4.85.0  4.84.0  4.82.0  4.80.0  4.79.0  4.78.0  4.77.0  4.75.0  4.73.0  4.72.0  4.71.0  4.70.0  4.69.0  4.67.0  4.65.0  4.64.0  4.61.0  4.60.0  4.59.0  4.57.0  4.56.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.46.0  4.45.0  4.44.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.34.0  4.33.0  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.8  3.1.2  3.0.3  2.3.1 
    
    
    public enum InstanceGroupConfig.Preemptibility extends Enum<InstanceGroupConfig.Preemptibility> implements ProtocolMessageEnum

Controls the use of preemptible instances within the group.

Protobuf enum `google.cloud.dataproc.v1.InstanceGroupConfig.Preemptibility`

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
`NON_PREEMPTIBLE` |  Instances are non-preemptible. This option is allowed for all instance groups and is the only valid value for Master and Worker instance groups. `NON_PREEMPTIBLE = 1;`  
`NON_PREEMPTIBLE_VALUE` |  Instances are non-preemptible. This option is allowed for all instance groups and is the only valid value for Master and Worker instance groups. `NON_PREEMPTIBLE = 1;`  
`PREEMPTIBILITY_UNSPECIFIED` |  Preemptibility is unspecified, the system will choose the appropriate setting for each instance group. `PREEMPTIBILITY_UNSPECIFIED = 0;`  
`PREEMPTIBILITY_UNSPECIFIED_VALUE` |  Preemptibility is unspecified, the system will choose the appropriate setting for each instance group. `PREEMPTIBILITY_UNSPECIFIED = 0;`  
`PREEMPTIBLE` |  Instances are [preemptible](https://cloud.google.com/compute/docs/instances/preemptible). This option is allowed only for [secondary worker](https://cloud.google.com/dataproc/docs/concepts/compute/secondary-vms) groups. `PREEMPTIBLE = 2;`  
`PREEMPTIBLE_VALUE` |  Instances are [preemptible](https://cloud.google.com/compute/docs/instances/preemptible). This option is allowed only for [secondary worker](https://cloud.google.com/dataproc/docs/concepts/compute/secondary-vms) groups. `PREEMPTIBLE = 2;`  
`SPOT` |  Instances are [Spot VMs](https://cloud.google.com/compute/docs/instances/spot). This option is allowed only for [secondary worker](https://cloud.google.com/dataproc/docs/concepts/compute/secondary-vms) groups. Spot VMs are the latest version of [preemptible VMs](https://cloud.google.com/compute/docs/instances/preemptible), and provide additional features. `SPOT = 3;`  
`SPOT_VALUE` |  Instances are [Spot VMs](https://cloud.google.com/compute/docs/instances/spot). This option is allowed only for [secondary worker](https://cloud.google.com/dataproc/docs/concepts/compute/secondary-vms) groups. Spot VMs are the latest version of [preemptible VMs](https://cloud.google.com/compute/docs/instances/preemptible), and provide additional features. `SPOT = 3;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.InstanceGroupConfig.Preemptibility#com_google_cloud_dataproc_v1_InstanceGroupConfig_Preemptibility_forNumber_int_) instead._  
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
