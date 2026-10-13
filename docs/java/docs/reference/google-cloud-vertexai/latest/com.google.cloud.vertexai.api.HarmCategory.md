---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.HarmCategory
title: Enum HarmCategory (1.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:50.606339+00:00
---

# Enum HarmCategory (1.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.HarmCategory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum HarmCategory (1.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.48.0 (latest)  1.47.0  1.45.0  1.43.0  1.42.0  1.40.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.30.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.20.1  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public enum HarmCategory extends Enum<HarmCategory> implements ProtocolMessageEnum

Harm categories that will block the content.

Protobuf enum `google.cloud.vertexai.v1.HarmCategory`

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
`HARM_CATEGORY_CIVIC_INTEGRITY` |  Deprecated: Election filter is not longer supported. The harm category is civic integrity. `HARM_CATEGORY_CIVIC_INTEGRITY = 5 [deprecated = true];`  
`HARM_CATEGORY_CIVIC_INTEGRITY_VALUE` |  Deprecated: Election filter is not longer supported. The harm category is civic integrity. `HARM_CATEGORY_CIVIC_INTEGRITY = 5 [deprecated = true];`  
`HARM_CATEGORY_DANGEROUS_CONTENT` |  The harm category is dangerous content. `HARM_CATEGORY_DANGEROUS_CONTENT = 2;`  
`HARM_CATEGORY_DANGEROUS_CONTENT_VALUE` |  The harm category is dangerous content. `HARM_CATEGORY_DANGEROUS_CONTENT = 2;`  
`HARM_CATEGORY_HARASSMENT` |  The harm category is harassment. `HARM_CATEGORY_HARASSMENT = 3;`  
`HARM_CATEGORY_HARASSMENT_VALUE` |  The harm category is harassment. `HARM_CATEGORY_HARASSMENT = 3;`  
`HARM_CATEGORY_HATE_SPEECH` |  The harm category is hate speech. `HARM_CATEGORY_HATE_SPEECH = 1;`  
`HARM_CATEGORY_HATE_SPEECH_VALUE` |  The harm category is hate speech. `HARM_CATEGORY_HATE_SPEECH = 1;`  
`HARM_CATEGORY_JAILBREAK` |  The harm category is for jailbreak prompts. `HARM_CATEGORY_JAILBREAK = 6;`  
`HARM_CATEGORY_JAILBREAK_VALUE` |  The harm category is for jailbreak prompts. `HARM_CATEGORY_JAILBREAK = 6;`  
`HARM_CATEGORY_SEXUALLY_EXPLICIT` |  The harm category is sexually explicit content. `HARM_CATEGORY_SEXUALLY_EXPLICIT = 4;`  
`HARM_CATEGORY_SEXUALLY_EXPLICIT_VALUE` |  The harm category is sexually explicit content. `HARM_CATEGORY_SEXUALLY_EXPLICIT = 4;`  
`HARM_CATEGORY_UNSPECIFIED` |  The harm category is unspecified. `HARM_CATEGORY_UNSPECIFIED = 0;`  
`HARM_CATEGORY_UNSPECIFIED_VALUE` |  The harm category is unspecified. `HARM_CATEGORY_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.HarmCategory#com_google_cloud_vertexai_api_HarmCategory_forNumber_int_) instead._  
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

Last updated 2026-03-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-30 UTC."],[],[]] 
