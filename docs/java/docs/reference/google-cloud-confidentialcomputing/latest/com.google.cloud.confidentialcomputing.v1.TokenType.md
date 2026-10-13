---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.TokenType
title: Enum TokenType (0.85.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:11.233242+00:00
---

# Enum TokenType (0.85.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.TokenType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum TokenType (0.85.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.85.0 (latest)  0.81.0  0.80.0  0.79.0  0.77.0  0.74.0  0.73.0  0.71.0  0.69.0  0.68.0  0.67.0  0.66.0  0.64.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.56.0  0.54.0  0.53.0  0.50.0  0.49.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public enum TokenType extends Enum<TokenType> implements ProtocolMessageEnum

Token type enum contains the different types of token responses Confidential Space supports

Protobuf enum `google.cloud.confidentialcomputing.v1.TokenType`

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
`TOKEN_TYPE_AWS_PRINCIPALTAGS` |  Principal-tag-based token for AWS integration `TOKEN_TYPE_AWS_PRINCIPALTAGS = 4;`  
`TOKEN_TYPE_AWS_PRINCIPALTAGS_VALUE` |  Principal-tag-based token for AWS integration `TOKEN_TYPE_AWS_PRINCIPALTAGS = 4;`  
`TOKEN_TYPE_LIMITED_AWS` |  Limited claim token type for AWS integration `TOKEN_TYPE_LIMITED_AWS = 3;`  
`TOKEN_TYPE_LIMITED_AWS_VALUE` |  Limited claim token type for AWS integration `TOKEN_TYPE_LIMITED_AWS = 3;`  
`TOKEN_TYPE_OIDC` |  OpenID Connect (OIDC) token type `TOKEN_TYPE_OIDC = 1;`  
`TOKEN_TYPE_OIDC_VALUE` |  OpenID Connect (OIDC) token type `TOKEN_TYPE_OIDC = 1;`  
`TOKEN_TYPE_PKI` |  Public Key Infrastructure (PKI) token type `TOKEN_TYPE_PKI = 2;`  
`TOKEN_TYPE_PKI_VALUE` |  Public Key Infrastructure (PKI) token type `TOKEN_TYPE_PKI = 2;`  
`TOKEN_TYPE_UNSPECIFIED` |  Unspecified token type `TOKEN_TYPE_UNSPECIFIED = 0;`  
`TOKEN_TYPE_UNSPECIFIED_VALUE` |  Unspecified token type `TOKEN_TYPE_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.TokenType#com_google_cloud_confidentialcomputing_v1_TokenType_forNumber_int_) instead._  
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
