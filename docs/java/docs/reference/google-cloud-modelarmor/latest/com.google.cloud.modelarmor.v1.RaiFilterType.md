---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterType
title: Enum RaiFilterType (0.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:15.765795+00:00
---

# Enum RaiFilterType (0.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum RaiFilterType (0.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.40.0 (latest)  0.36.0  0.35.0  0.34.0  0.32.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.21.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.9.0  0.8.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public enum RaiFilterType extends Enum<RaiFilterType> implements ProtocolMessageEnum

Options for responsible AI Filter Types.

Protobuf enum `google.cloud.modelarmor.v1.RaiFilterType`

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
`DANGEROUS` |  Danger `DANGEROUS = 17;`  
`DANGEROUS_VALUE` |  Danger `DANGEROUS = 17;`  
`HARASSMENT` |  Harassment. `HARASSMENT = 6;`  
`HARASSMENT_VALUE` |  Harassment. `HARASSMENT = 6;`  
`HATE_SPEECH` |  Hate Speech. `HATE_SPEECH = 3;`  
`HATE_SPEECH_VALUE` |  Hate Speech. `HATE_SPEECH = 3;`  
`RAI_FILTER_TYPE_UNSPECIFIED` |  Unspecified filter type. `RAI_FILTER_TYPE_UNSPECIFIED = 0;`  
`RAI_FILTER_TYPE_UNSPECIFIED_VALUE` |  Unspecified filter type. `RAI_FILTER_TYPE_UNSPECIFIED = 0;`  
`SEXUALLY_EXPLICIT` |  Sexually Explicit. `SEXUALLY_EXPLICIT = 2;`  
`SEXUALLY_EXPLICIT_VALUE` |  Sexually Explicit. `SEXUALLY_EXPLICIT = 2;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.RaiFilterType#com_google_cloud_modelarmor_v1_RaiFilterType_forNumber_int_) instead._  
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
