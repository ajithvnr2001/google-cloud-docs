---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Sku.SkuPrice.AiPlatformDeployedModelUsageFee.UsageCalculation
title: Enum Sku.SkuPrice.AiPlatformDeployedModelUsageFee.UsageCalculation (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:13.964565+00:00
---

# Enum Sku.SkuPrice.AiPlatformDeployedModelUsageFee.UsageCalculation (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Sku.SkuPrice.AiPlatformDeployedModelUsageFee.UsageCalculation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum Sku.SkuPrice.AiPlatformDeployedModelUsageFee.UsageCalculation (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public enum Sku.SkuPrice.AiPlatformDeployedModelUsageFee.UsageCalculation extends Enum<Sku.SkuPrice.AiPlatformDeployedModelUsageFee.UsageCalculation> implements ProtocolMessageEnum

Determines how the customer's usage is calculated.

Protobuf enum ` google.cloud.commerceproducer.v1beta.Sku.SkuPrice.AiPlatformDeployedModelUsageFee.UsageCalculation`

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
`LINEAR_RESOURCE_SCALED_DEPLOYMENT_RUNTIME` |  Usage is calculated from deployment runtime and size. Usage is calculated by measuring the deployment runtime in hours and multiplying by the amount of the deployed model's hardware resource matching the SKU's hardware resource type. This results in a composite `unit` of hours ('h') multiplied by the unit that denominates the hardware resource, though note that multiplying by the dimensionless unit ("1") has no effect. `LINEAR_RESOURCE_SCALED_DEPLOYMENT_RUNTIME = 2;`  
`LINEAR_RESOURCE_SCALED_DEPLOYMENT_RUNTIME_VALUE` |  Usage is calculated from deployment runtime and size. Usage is calculated by measuring the deployment runtime in hours and multiplying by the amount of the deployed model's hardware resource matching the SKU's hardware resource type. This results in a composite `unit` of hours ('h') multiplied by the unit that denominates the hardware resource, though note that multiplying by the dimensionless unit ("1") has no effect. `LINEAR_RESOURCE_SCALED_DEPLOYMENT_RUNTIME = 2;`  
`UNRECOGNIZED` |   
`USAGE_CALCULATION_UNSPECIFIED` |  Unused. `USAGE_CALCULATION_UNSPECIFIED = 0;`  
`USAGE_CALCULATION_UNSPECIFIED_VALUE` |  Unused. `USAGE_CALCULATION_UNSPECIFIED = 0;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Sku.SkuPrice.AiPlatformDeployedModelUsageFee.UsageCalculation#com_google_cloud_commerceproducer_v1beta_Sku_SkuPrice_AiPlatformDeployedModelUsageFee_UsageCalculation_forNumber_int_) instead._  
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
