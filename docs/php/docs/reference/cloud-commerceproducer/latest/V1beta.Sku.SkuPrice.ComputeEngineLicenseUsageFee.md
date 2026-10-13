---
url: https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.Sku.SkuPrice.ComputeEngineLicenseUsageFee
title: Google Cloud Commerce Producer V1beta Client - Class ComputeEngineLicenseUsageFee (0.2.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:33.211542+00:00
---

# Google Cloud Commerce Producer V1beta Client - Class ComputeEngineLicenseUsageFee (0.2.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.Sku.SkuPrice.ComputeEngineLicenseUsageFee

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Commerce Producer V1beta Client - Class ComputeEngineLicenseUsageFee (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.2.0 (latest)  0.1.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Commerce Producer V1beta Client class ComputeEngineLicenseUsageFee.

Details about a SKU pricing usage of a [Compute Engine License](https://cloud.google.com/compute/docs/licenses/about).

The SKU applies to a single license, and may be further scoped to a [Compute Engine VM Instance](https://cloud.google.com/compute/docs/instances) machine resource type (e.g. "vCPU") and size range for that machine resource. Instances deployed from [Compute Engine Images](https://cloud.google.com/compute/docs/images) incorporating the target license and (if applicable) matching the machine resource type size range will be charged by the SKU. A single license may be priced by multiple SKUs covering different combinations of machine resource type and size range, allowing a single running instance to be charged by up to one SKU per machine resource type, with pricing tiered according to machine shape.

Generated from protobuf message `google.cloud.commerceproducer.v1beta.Sku.SkuPrice.ComputeEngineLicenseUsageFee`

## Namespace

Google \ Cloud \ CommerceProducer \ V1beta \ Sku \ SkuPrice

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ price_per_unit` |  `[Google\Type\Money](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.Money.html)`   
The price per unit of usage. The customer's usage charge is computed by measuring the customer's consumption denominated in price units and multiplying by this price.  
`↳ license_code` |  `string`   
Output only. The license code of the target Compute Engine License. Note that this is the numeric license code itself in uint64 format used to reference licenses attached to images, not the resource name of the related [Compute Engine LicenseCode resource](https://cloud.google.com/compute/docs/reference/rest/v1/licenseCodes). Example: "1234567890123456789"  
`↳ machine_resource` |  `int`   
Output only. The machine resource type that the SKU applies to, if any. SKUs with a non-default value are referred to as "resource-based" SKUs.  
`↳ machine_resource_range` |  `[ComputeEngineLicenseUsageFee\MachineResourceRange](https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.Sku.SkuPrice.ComputeEngineLicenseUsageFee.MachineResourceRange)`   
Output only. The range of machine resource values that the SKU applies to. Unset when the SKU is not scoped to a particular machine resource type. The collection of SKUs in effect at any given time targeting the same license and machine resource type will cover all possible values for that machine resource type without overlap. Such a collection of SKUs form a "tiered" price structure over the possible values of the machine resource, with each SKU acting as a "tier". NOTE: This is distinct from a SKU with [tiered pricing](https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing).  
`↳ usage_calculation` |  `int`   
Output only. Determines how the customer's usage is calculated.  
`↳ unit` |  `string`   
Output only. The price unit of the SKU. See <https://ucum.org/ucum.html> for the format of the price unit. For linear-priced memory SKUs, the price unit is 'GiBy.h'. For all other SKUs, the price unit is 'h'. This includes linear-priced vCPU and GPU SKUs because these resources have unitless dimensions and the application of these scaling factors does not change the price unit.  
  
### getPricePerUnit

The price per unit of usage.

The customer's usage charge is computed by measuring the customer's consumption denominated in price units and multiplying by this price.

**Returns**  
---  
**Type** | **Description**  
`[Google\Type\Money](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.Money.html)|null` |   
  
### hasPricePerUnit

### setPricePerUnit

The price per unit of usage.

The customer's usage charge is computed by measuring the customer's consumption denominated in price units and multiplying by this price.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Type\Money](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Type.Money.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLicenseCode

Output only. The license code of the target Compute Engine License.

Note that this is the numeric license code itself in uint64 format used to reference licenses attached to images, not the resource name of the related [Compute Engine LicenseCode resource](https://cloud.google.com/compute/docs/reference/rest/v1/licenseCodes). Example: "1234567890123456789"

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setLicenseCode

Output only. The license code of the target Compute Engine License.

Note that this is the numeric license code itself in uint64 format used to reference licenses attached to images, not the resource name of the related [Compute Engine LicenseCode resource](https://cloud.google.com/compute/docs/reference/rest/v1/licenseCodes). Example: "1234567890123456789"

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMachineResource

Output only. The machine resource type that the SKU applies to, if any.

SKUs with a non-default value are referred to as "resource-based" SKUs.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [MachineResource](https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.Sku.SkuPrice.ComputeEngineLicenseUsageFee.MachineResource).  
  
### setMachineResource

Output only. The machine resource type that the SKU applies to, if any.

SKUs with a non-default value are referred to as "resource-based" SKUs.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [MachineResource](https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.Sku.SkuPrice.ComputeEngineLicenseUsageFee.MachineResource).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMachineResourceRange

Output only. The range of machine resource values that the SKU applies to. Unset when the SKU is not scoped to a particular machine resource type. The collection of SKUs in effect at any given time targeting the same license and machine resource type will cover all possible values for that machine resource type without overlap. Such a collection of SKUs form a "tiered" price structure over the possible values of the machine resource, with each SKU acting as a "tier".

NOTE: This is distinct from a SKU with [tiered pricing](https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing).

**Returns**  
---  
**Type** | **Description**  
`[ComputeEngineLicenseUsageFee\MachineResourceRange](https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.Sku.SkuPrice.ComputeEngineLicenseUsageFee.MachineResourceRange)|null` |   
  
### hasMachineResourceRange

### clearMachineResourceRange

### setMachineResourceRange

Output only. The range of machine resource values that the SKU applies to. Unset when the SKU is not scoped to a particular machine resource type. The collection of SKUs in effect at any given time targeting the same license and machine resource type will cover all possible values for that machine resource type without overlap. Such a collection of SKUs form a "tiered" price structure over the possible values of the machine resource, with each SKU acting as a "tier".

NOTE: This is distinct from a SKU with [tiered pricing](https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ComputeEngineLicenseUsageFee\MachineResourceRange](https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.Sku.SkuPrice.ComputeEngineLicenseUsageFee.MachineResourceRange)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUsageCalculation

Output only. Determines how the customer's usage is calculated.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [UsageCalculation](https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.Sku.SkuPrice.ComputeEngineLicenseUsageFee.UsageCalculation).  
  
### setUsageCalculation

Output only. Determines how the customer's usage is calculated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [UsageCalculation](https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.Sku.SkuPrice.ComputeEngineLicenseUsageFee.UsageCalculation).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUnit

Output only. The price unit of the SKU.

See <https://ucum.org/ucum.html> for the format of the price unit. For linear-priced memory SKUs, the price unit is 'GiBy.h'. For all other SKUs, the price unit is 'h'. This includes linear-priced vCPU and GPU SKUs because these resources have unitless dimensions and the application of these scaling factors does not change the price unit.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setUnit

Output only. The price unit of the SKU.

See <https://ucum.org/ucum.html> for the format of the price unit. For linear-priced memory SKUs, the price unit is 'GiBy.h'. For all other SKUs, the price unit is 'h'. This includes linear-priced vCPU and GPU SKUs because these resources have unitless dimensions and the application of these scaling factors does not change the price unit.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPriceStructure

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
