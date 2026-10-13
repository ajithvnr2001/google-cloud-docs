---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange.Usage
title: Enum InternalRange.Usage (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:16.281577+00:00
---

# Enum InternalRange.Usage (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange.Usage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum InternalRange.Usage (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.9  1.1.1  1.0.0  0.5.0 
    
    
    public enum InternalRange.Usage extends Enum<InternalRange.Usage> implements ProtocolMessageEnum

Possible usage of an internal range.

Protobuf enum `google.cloud.networkconnectivity.v1.InternalRange.Usage`

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
`EXTERNAL_TO_VPC` |  Ranges created with EXTERNAL_TO_VPC cannot be associated with VPC resources and are meant to block out address ranges for various use cases, like for example, usage on-prem, with dynamic route announcements via interconnect. `EXTERNAL_TO_VPC = 2;`  
`EXTERNAL_TO_VPC_VALUE` |  Ranges created with EXTERNAL_TO_VPC cannot be associated with VPC resources and are meant to block out address ranges for various use cases, like for example, usage on-prem, with dynamic route announcements via interconnect. `EXTERNAL_TO_VPC = 2;`  
`FOR_MIGRATION` |  Ranges created FOR_MIGRATION can be used to lock a CIDR range between a source and target subnet. If usage is set to FOR_MIGRATION, the peering value has to be set to FOR_SELF or default to FOR_SELF when unset. `FOR_MIGRATION = 3;`  
`FOR_MIGRATION_VALUE` |  Ranges created FOR_MIGRATION can be used to lock a CIDR range between a source and target subnet. If usage is set to FOR_MIGRATION, the peering value has to be set to FOR_SELF or default to FOR_SELF when unset. `FOR_MIGRATION = 3;`  
`FOR_VPC` |  A VPC resource can use the reserved CIDR block by associating it with the internal range resource if usage is set to FOR_VPC. `FOR_VPC = 1;`  
`FOR_VPC_VALUE` |  A VPC resource can use the reserved CIDR block by associating it with the internal range resource if usage is set to FOR_VPC. `FOR_VPC = 1;`  
`UNRECOGNIZED` |   
`USAGE_UNSPECIFIED` |  Unspecified usage is allowed in calls which identify the resource by other fields and do not need Usage set to complete. These are, i.e.: GetInternalRange and DeleteInternalRange. Usage needs to be specified explicitly in CreateInternalRange or UpdateInternalRange calls. `USAGE_UNSPECIFIED = 0;`  
`USAGE_UNSPECIFIED_VALUE` |  Unspecified usage is allowed in calls which identify the resource by other fields and do not need Usage set to complete. These are, i.e.: GetInternalRange and DeleteInternalRange. Usage needs to be specified explicitly in CreateInternalRange or UpdateInternalRange calls. `USAGE_UNSPECIFIED = 0;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.InternalRange.Usage#com_google_cloud_networkconnectivity_v1_InternalRange_Usage_forNumber_int_) instead._  
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
