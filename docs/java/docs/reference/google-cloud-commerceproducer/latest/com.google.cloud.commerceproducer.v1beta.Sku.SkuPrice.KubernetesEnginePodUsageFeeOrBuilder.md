---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Sku.SkuPrice.KubernetesEnginePodUsageFeeOrBuilder
title: Interface Sku.SkuPrice.KubernetesEnginePodUsageFeeOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:50.480543+00:00
---

# Interface Sku.SkuPrice.KubernetesEnginePodUsageFeeOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Sku.SkuPrice.KubernetesEnginePodUsageFeeOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Sku.SkuPrice.KubernetesEnginePodUsageFeeOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public static interface Sku.SkuPrice.KubernetesEnginePodUsageFeeOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getPodResource()
    
    
    public abstract Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResource getPodResource()

Output only. The pod resource type that the SKU applies to. SKUs with a non-default value are referred to as "resource-based" SKUs.

` .google.cloud.commerceproducer.v1beta.Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResource pod_resource = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResource)` | The podResource.  
  
### getPodResourceRange()
    
    
    public abstract Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResourceRange getPodResourceRange()

Output only. The range of pod resource values that the SKU applies to. The collection of SKUs in effect at any given time targeting the same service annotation and pod resource type will cover all possible values for that pod resource type without overlap. Such a collection of SKUs form a "tiered" price structure over the possible values of the pod resource, with each SKU acting as a "tier".

NOTE: This is distinct from a SKU with [tiered pricing](https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing).

` .google.cloud.commerceproducer.v1beta.Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResourceRange pod_resource_range = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResourceRange](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResourceRange)` | The podResourceRange.  
  
### getPodResourceRangeOrBuilder()
    
    
    public abstract Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResourceRangeOrBuilder getPodResourceRangeOrBuilder()

Output only. The range of pod resource values that the SKU applies to. The collection of SKUs in effect at any given time targeting the same service annotation and pod resource type will cover all possible values for that pod resource type without overlap. Such a collection of SKUs form a "tiered" price structure over the possible values of the pod resource, with each SKU acting as a "tier".

NOTE: This is distinct from a SKU with [tiered pricing](https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing).

` .google.cloud.commerceproducer.v1beta.Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResourceRange pod_resource_range = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResourceRangeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResourceRangeOrBuilder)` |   
  
### getPodResourceValue()
    
    
    public abstract int getPodResourceValue()

Output only. The pod resource type that the SKU applies to. SKUs with a non-default value are referred to as "resource-based" SKUs.

` .google.cloud.commerceproducer.v1beta.Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResource pod_resource = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for podResource.  
  
### getPricePerUnit()
    
    
    public abstract Money getPricePerUnit()

The price per unit of usage. The customer's usage charge is computed by measuring the customer's consumption denominated in price units and multiplying by this price.

`.google.type.Money price_per_unit = 6;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Money` | The pricePerUnit.  
  
### getPricePerUnitOrBuilder()
    
    
    public abstract MoneyOrBuilder getPricePerUnitOrBuilder()

The price per unit of usage. The customer's usage charge is computed by measuring the customer's consumption denominated in price units and multiplying by this price.

`.google.type.Money price_per_unit = 6;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.MoneyOrBuilder` |   
  
### getPriceStructureCase()
    
    
    public abstract Sku.SkuPrice.KubernetesEnginePodUsageFee.PriceStructureCase getPriceStructureCase()

**Returns**  
---  
**Type** | **Description**  
`[Sku.SkuPrice.KubernetesEnginePodUsageFee.PriceStructureCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Sku.SkuPrice.KubernetesEnginePodUsageFee.PriceStructureCase)` |   
  
### getUnit()
    
    
    public abstract String getUnit()

Output only. The price unit of the SKU. See <https://ucum.org/ucum.html> for the format of the price unit. For linear-priced memory SKUs, the price unit is 'GiBy.h'. For all other SKUs, the price unit is 'h'. This includes linear-priced VCPU, GPU, and TPU SKUs because these resources have unitless dimensions and the application of these scaling factors does not change the price unit.

`string unit = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The unit.  
  
### getUnitBytes()
    
    
    public abstract ByteString getUnitBytes()

Output only. The price unit of the SKU. See <https://ucum.org/ucum.html> for the format of the price unit. For linear-priced memory SKUs, the price unit is 'GiBy.h'. For all other SKUs, the price unit is 'h'. This includes linear-priced VCPU, GPU, and TPU SKUs because these resources have unitless dimensions and the application of these scaling factors does not change the price unit.

`string unit = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for unit.  
  
### getUsageCalculation()
    
    
    public abstract Sku.SkuPrice.KubernetesEnginePodUsageFee.UsageCalculation getUsageCalculation()

Output only. Determines how the customer's usage is calculated.

` .google.cloud.commerceproducer.v1beta.Sku.SkuPrice.KubernetesEnginePodUsageFee.UsageCalculation usage_calculation = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Sku.SkuPrice.KubernetesEnginePodUsageFee.UsageCalculation](https://docs.cloud.google.com/java/docs/reference/google-cloud-commerceproducer/latest/com.google.cloud.commerceproducer.v1beta.Sku.SkuPrice.KubernetesEnginePodUsageFee.UsageCalculation)` | The usageCalculation.  
  
### getUsageCalculationValue()
    
    
    public abstract int getUsageCalculationValue()

Output only. Determines how the customer's usage is calculated.

` .google.cloud.commerceproducer.v1beta.Sku.SkuPrice.KubernetesEnginePodUsageFee.UsageCalculation usage_calculation = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for usageCalculation.  
  
### hasPodResourceRange()
    
    
    public abstract boolean hasPodResourceRange()

Output only. The range of pod resource values that the SKU applies to. The collection of SKUs in effect at any given time targeting the same service annotation and pod resource type will cover all possible values for that pod resource type without overlap. Such a collection of SKUs form a "tiered" price structure over the possible values of the pod resource, with each SKU acting as a "tier".

NOTE: This is distinct from a SKU with [tiered pricing](https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing).

` .google.cloud.commerceproducer.v1beta.Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResourceRange pod_resource_range = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the podResourceRange field is set.  
  
### hasPricePerUnit()
    
    
    public abstract boolean hasPricePerUnit()

The price per unit of usage. The customer's usage charge is computed by measuring the customer's consumption denominated in price units and multiplying by this price.

`.google.type.Money price_per_unit = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pricePerUnit field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
