---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus
title: REST Resource: projects.locations.services.skus \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:16.063323+00:00
---

# REST Resource: projects.locations.services.skus  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  REST Resource: projects.locations.services.skus Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Sku
    * JSON representation
  * SkuPrice
    * JSON representation
  * InactiveSkuPrice
  * ManagedServiceMetricUsageFee
    * JSON representation
  * TieredPrice
    * JSON representation
  * PriceTier
    * JSON representation
  * ComputeEngineLicenseUsageFee
    * JSON representation
  * MachineResource
  * MachineResourceRange
    * JSON representation
  * UsageCalculation
  * KubernetesEnginePodUsageFee
    * JSON representation
  * PodResource
  * PodResourceRange
    * JSON representation
  * UsageCalculation
  * AiPlatformManagedModelUsageFee
    * JSON representation
  * AiPlatformManagedModelUsageMetric
    * JSON representation
  * InputTokensMetric
  * CacheReadInputTokensMetric
  * CacheWriteInputTokensMetric
    * JSON representation
  * OutputTokensMetric
  * WebSearchRequestsMetric
  * AiPlatformManagedModelEndpointLocation
    * JSON representation
  * PredictionMode
  * CombinedRequestInputTokensRange
    * JSON representation
  * ProvisionedThroughputOverage
    * JSON representation
  * AiPlatformProvisionedThroughputFee
    * JSON representation
  * AiPlatformDeployedModelUsageFee
    * JSON representation
  * UsageCalculation
  * FlatSubscriptionFee
    * JSON representation
  * Methods



## Resource: Sku

Message describing the Sku resource.

Encapsulates and represents a stock keeping unit (SKU), the atomic unit of pricing and billing in Google Cloud. Each customer charge is associated with and originates from exactly one SKU. While the Cloud Marketplace Sku resource shares a close relationship with the public [Sku resource in the Cloud Billing API](https://cloud.google.com/billing/docs/how-to/get-pricing-information-api), Cloud Marketplace SKUs are represented here with additional information in an alternative format tailored for use by Cloud Marketplace partners, and are not necessarily public and by extension are not generally visible in the Cloud Billing API or the [Google Cloud Public SKUs](https://cloud.google.com/skus).

Note on terminology: While the name of the resource derives from the acronym 'SKU' it is named 'Sku' for consistency with other resource type names, and may be rendered variously as 'Sku', 'sku', or 'SKU' across this and other documentation.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "skuPriceTimeline": [
        {
          object ([SkuPrice](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#SkuPrice))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. Name of the SKU.  
`description` |  `string` Output only. Description of the SKU.  
`skuPriceTimeline[]` |  `object (`[SkuPrice](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#SkuPrice)`)` Output only. Timeline of the SKU prices, in chronological order by `effectiveTime`.Each entry is active in the time range starting inclusively from the entry's `effectiveTime` and ending exclusively at the next entry's `effectiveTime`, if one exists, or else remaining active indefinitely if it is the final entry. The currently active entry is the entry with the latest `effectiveTime` that is in the past. Because of scheduled future price changes the currently active entry may not be the last entry in the timeline. A SKU does not necessarily have a currently active entry, as the SKU's first timeline entry may have an `effectiveTime` in the future.  
  
## SkuPrice

The price of the SKU, active during a particular time range. Prices are in all cases in USD. Customers are billed in the currency of their billing account, subject to the currency conversion rate in effect at the time.

JSON representation  
---  
      
    
    {
      "effectiveTime": string,
    
      // Union field sku_type can be only one of the following:
      "inactive": {
        object ([InactiveSkuPrice](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#InactiveSkuPrice))
      },
      "managedServiceMetricUsageFee": {
        object ([ManagedServiceMetricUsageFee](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#ManagedServiceMetricUsageFee))
      },
      "gceLicenseUsageFee": {
        object ([ComputeEngineLicenseUsageFee](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#ComputeEngineLicenseUsageFee))
      },
      "gkePodUsageFee": {
        object ([KubernetesEnginePodUsageFee](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#KubernetesEnginePodUsageFee))
      },
      "aiPlatformManagedModelUsageFee": {
        object ([AiPlatformManagedModelUsageFee](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#AiPlatformManagedModelUsageFee))
      },
      "aiPlatformProvisionedThroughputFee": {
        object ([AiPlatformProvisionedThroughputFee](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#AiPlatformProvisionedThroughputFee))
      },
      "aiPlatformDeployedModelUsageFee": {
        object ([AiPlatformDeployedModelUsageFee](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#AiPlatformDeployedModelUsageFee))
      },
      "flatSubscriptionFee": {
        object ([FlatSubscriptionFee](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#FlatSubscriptionFee))
      }
      // End of list of possible types for union field sku_type.
    }  
  
Fields  
---  
`effectiveTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start of the time interval during which this price is effective.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `sku_type`. The type of the SKU. `sku_type` can be only one of the following:  
`inactive` |  `object (`[InactiveSkuPrice](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#InactiveSkuPrice)`)` Output only. The SKU has been disabled and has no price. SKUs, once created and allowed to go into effect, are never deleted. Disabled SKUs may accumulate over the lifetime of a product as the product's pricing evolves, and are retained for historical reference. A SKU in this state generally remains in this state indefinitely, but may be reactivated if needed. Clients must not depend on inactive SKUs remaining inactive.  
`managedServiceMetricUsageFee` |  `object (`[ManagedServiceMetricUsageFee](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#ManagedServiceMetricUsageFee)`)` Output only. The SKU prices usage reported by the partner for a partner-defined custom billing metric.  
`gceLicenseUsageFee` |  `object (`[ComputeEngineLicenseUsageFee](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#ComputeEngineLicenseUsageFee)`)` Output only. The SKU prices usage of a Compute Engine License via a license fee applied to running instances that use the license.  
`gkePodUsageFee` |  `object (`[KubernetesEnginePodUsageFee](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#KubernetesEnginePodUsageFee)`)` Output only. The SKU prices usage of software deployed on Kubernetes Engine.  
`aiPlatformManagedModelUsageFee` |  `object (`[AiPlatformManagedModelUsageFee](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#AiPlatformManagedModelUsageFee)`)` Output only. The SKU prices usage of an AI Platform Managed Model (MaaS).  
`aiPlatformProvisionedThroughputFee` |  `object (`[AiPlatformProvisionedThroughputFee](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#AiPlatformProvisionedThroughputFee)`)` Output only. The SKU prices reservation of AI Platform provisioned throughput.  
`aiPlatformDeployedModelUsageFee` |  `object (`[AiPlatformDeployedModelUsageFee](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#AiPlatformDeployedModelUsageFee)`)` Output only. The SKU prices usage of an AI model deployed on AI Platform.  
`flatSubscriptionFee` |  `object (`[FlatSubscriptionFee](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#FlatSubscriptionFee)`)` Output only. The SKU applies a flat subscription fee.  
  
## InactiveSkuPrice

This type has no fields.

Representation for a SKU that is not active and has no price.

## ManagedServiceMetricUsageFee

Details about a SKU pricing usage of a [partner-reported custom billing metric](https://cloud.google.com/service-infrastructure/docs/reporting-billing-metrics) defined by the partner in the Service Management API and reported using the Service Control API.

The customer's usage charge is computed by converting the customer's reported consumption to the SKU's composite price unit and applying the graduated price from the appropriate price tier.

JSON representation  
---  
      
    
    {
      "canonicalMetric": string,
    
      // Union field price_structure can be only one of the following:
      "tieredPrice": {
        object ([TieredPrice](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#TieredPrice))
      }
      // End of list of possible types for union field price_structure.
    }  
  
Fields  
---  
`canonicalMetric` |  `string` Output only. The name of the metric, in canonical format.Note that in the canonical format the first character of the path component of the metric name is always uppercase, which may differ from the metric name in the service config. For example, a metric appearing in the service config as 'example.com/example_metric' will appear here in the SKU as 'example.com/Example_metric'. In the Service Management and Service Control APIs these two metric names are considered distinct, either or both may be defined, and usage must be reported using a name matching the name of a metric defined in the service config. But for billing purposes usage reported using either name will be aggregated under the canonical metric name.Example: "example.com/Example_metric"  
Union field `price_structure`. The billing model applied to bill the customer's usage. `price_structure` can be only one of the following:  
`tieredPrice` |  `object (`[TieredPrice](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#TieredPrice)`)` Output only. [Tiered pricing](https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing) of the SKU.  
  
## TieredPrice

Price structure for a SKU charging a [tiered price](https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing).

JSON representation  
---  
      
    
    {
      "unit": string,
      "unitDescription": string,
      "priceUnitCount": {
        object ([Decimal](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Decimal))
      },
      "priceTiers": [
        {
          object ([PriceTier](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#PriceTier))
        }
      ]
    }  
  
Fields  
---  
`unit` |  `string` Output only. Usage unit used for defining price tiers and for scaling with the priceUnitCount to form the composite price unit.See <https://ucum.org/ucum.html> for the format of the price unit. A unitless dimension, such as a count, is represented as `1`.  
`unitDescription` |  `string` Output only. The display description of the unit, supplied at time of onboarding. This value is recommended to be set at least for dimensionless metrics, but may be empty if no description was provided at time of onboarding.  
`priceUnitCount` |  `object (`[Decimal](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Decimal)`)` Output only. Scaling the `unit` by the `priceUnitCount` forms the composite "price unit" which is priced by the price tiers.This scaling factor is in addition to any numerical prefix symbol on the `unit`, so the same composite "price unit" can be represented in several ways, differing only in their presentation to users.Examples:

  * $1 per 1 bytes : unit = By, priceUnitCount = 1
  * $1000 per 1 kilobytes : unit = kBy, priceUnitCount = 1
  * $5000 per 5 kilobytes : unit = kBy, priceUnitCount = 5

  
`priceTiers[]` |  `object (`[PriceTier](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#PriceTier)`)` Output only. The list of price tiers for the SKU, ordered by the startAmount.The tiers are non-overlapping and are collectively bounded below by zero and unbounded above to cover the entire range of possible metric usage. Each tier is bounded below inclusively by its startAmount and bounded above exclusively by the startAmount of the next tier, or else unbounded above if there is no next tier.Usage of the metric is aggregated by customer billing account on a monthly basis and billed in a graduated manner according to the price tiers, with each marginal unit of usage priced according to the tier in which it falls.  
  
## PriceTier

A [price tier](https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing) pricing metric usage within a range.

Each marginal unit of usage is priced according to the price tier in which it falls.

JSON representation  
---  
      
    
    {
      "startAmount": {
        object ([Decimal](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Decimal))
      },
      "price": {
        object ([Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money))
      }
    }  
  
Fields  
---  
`startAmount` |  `object (`[Decimal](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Decimal)`)` Output only. Inclusive lower bound of the tier interval, denominated in `unit`.  
`price` |  `object (`[Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money)`)` Output only. The price per `priceUnitCount` of `unit` in the tier. The price is applied fractionally if the customer's usage within the tier is not an integer multiple of `priceUnitCount`.  
  
## ComputeEngineLicenseUsageFee

Details about a SKU pricing usage of a [Compute Engine License](https://cloud.google.com/compute/docs/licenses/about).

The SKU applies to a single license, and may be further scoped to a [Compute Engine VM Instance](https://cloud.google.com/compute/docs/instances) machine resource type (e.g. "vCPU") and size range for that machine resource. Instances deployed from [Compute Engine Images](https://cloud.google.com/compute/docs/images) incorporating the target license and (if applicable) matching the machine resource type size range will be charged by the SKU. A single license may be priced by multiple SKUs covering different combinations of machine resource type and size range, allowing a single running instance to be charged by up to one SKU per machine resource type, with pricing tiered according to machine shape.

JSON representation  
---  
      
    
    {
      "licenseCode": string,
      "machineResource": enum ([MachineResource](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#MachineResource)),
      "machineResourceRange": {
        object ([MachineResourceRange](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#MachineResourceRange))
      },
      "usageCalculation": enum ([UsageCalculation](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#UsageCalculation)),
      "unit": string,
    
      // Union field price_structure can be only one of the following:
      "pricePerUnit": {
        object ([Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money))
      }
      // End of list of possible types for union field price_structure.
    }  
  
Fields  
---  
`licenseCode` |  `string` Output only. The license code of the target Compute Engine License. Note that this is the numeric license code itself in uint64 format used to reference licenses attached to images, not the resource name of the related [Compute Engine LicenseCode resource](https://cloud.google.com/compute/docs/reference/rest/v1/licenseCodes).Example: "1234567890123456789"  
`machineResource` |  `enum (`[MachineResource](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#MachineResource)`)` Output only. The machine resource type that the SKU applies to, if any. SKUs with a non-default value are referred to as "resource-based" SKUs.  
`machineResourceRange` |  `object (`[MachineResourceRange](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#MachineResourceRange)`)` Output only. The range of machine resource values that the SKU applies to. Unset when the SKU is not scoped to a particular machine resource type. The collection of SKUs in effect at any given time targeting the same license and machine resource type will cover all possible values for that machine resource type without overlap. Such a collection of SKUs form a "tiered" price structure over the possible values of the machine resource, with each SKU acting as a "tier".NOTE: This is distinct from a SKU with [tiered pricing](https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing).  
`usageCalculation` |  `enum (`[UsageCalculation](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#UsageCalculation)`)` Output only. Determines how the customer's usage is calculated.  
`unit` |  `string` Output only. The price unit of the SKU. See <https://ucum.org/ucum.html> for the format of the price unit. For linear-priced memory SKUs, the price unit is 'GiBy.h'. For all other SKUs, the price unit is 'h'. This includes linear-priced vCPU and GPU SKUs because these resources have unitless dimensions and the application of these scaling factors does not change the price unit.  
Union field `price_structure`. The billing model applied to bill the customer's usage arising from running instances covered by the scope of the SKU. `price_structure` can be only one of the following:  
`pricePerUnit` |  `object (`[Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money)`)` The price per unit of usage. The customer's usage charge is computed by measuring the customer's consumption denominated in price units and multiplying by this price.  
  
## MachineResource

The machine resource type that the SKU applies to, if any.

Enums  
---  
`MACHINE_RESOURCE_UNSPECIFIED` | The SKU applies to all instances irrespective of machine shape. This is referred to as "instance-based pricing" because the price is the same for all instances.  
`VCPU_COUNT` | The SKU applies based on the instance's vCPU count.  
`MEMORY_BYTES` | The SKU applies based on the instance's memory size in bytes.  
`GPU_COUNT` | The SKU applies based on the instance's GPU count.  
  
## MachineResourceRange

The range of machine resource values that the SKU applies to.

JSON representation  
---  
      
    
    {
      "startValue": string,
      "endValue": string
    }  
  
Fields  
---  
`startValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The inclusive lower bound of the range. While the number zero may be the start of a range, it is not a possible machine resource value. An instance cannot exist with zero vCPU or memory, and an instance with no attached accelerators lacks a GPU dimension entirely rather than having a GPU count of zero.  
`endValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The exclusive upper bound of the range. If no end value is specified, the range is unbounded from above.  
  
## UsageCalculation

Determines how the customer's usage is calculated.

Enums  
---  
`USAGE_CALCULATION_UNSPECIFIED` | Unused.  
`INSTANCE_RUNTIME` | Usage is calculated from instance runtime. The customer's usage is metered according to the [Compute Engine VM instance pricing model](https://cloud.google.com/compute/vm-instance-pricing), measured on a per-instance basis in units of hours, with a minimum duration of one minute and an increment of one second.A SKU using this usage calculation is referred to as "flat" because the customer's usage charge is independent of the instance's machine resource shape apart from determining whether the SKU applies to the instance.  
`LINEAR_RESOURCE_SCALED_INSTANCE_RUNTIME` | Usage is calculated from instance runtime and size. This calculation mode is only applicable to resource-based SKUs. Usage is calculated by measuring the instance runtime in the same manner as for `INSTANCE_RUNTIME` and multiplying by the instance's machine resource value matching the SKU's machine resource type. This converts the price from per-instance-hour to per-instance-hour-per-machine-resource, which changes the price unit for memory SKUs to 'GiBy.h'. The price unit otherwise remains 'h' because the other machine resources are dimensionless.A SKU using this usage calculation is referred to as "linear" because the customer's usage charge is linearly proportional to the instance's machine resource value.  
  
## KubernetesEnginePodUsageFee

Details about a SKU pricing usage of software running on a Kubernetes Engine pod.

The SKU applies to pods annotated with the SKU's parent service name, and may be further scoped to a [k8s pod resource type](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) (e.g. "CPU") and size range for that resource type. Running pods annotated with the parent service's service name and matching the pod resource type size range will be charged by the SKU. A service may be priced by multiple SKUs covering different combinations of pod resource type and size range, allowing a single running pod to be charged by up to one SKU per pod resource type, with pricing tiered according to pod shape.

JSON representation  
---  
      
    
    {
      "podResource": enum ([PodResource](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#PodResource)),
      "podResourceRange": {
        object ([PodResourceRange](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#PodResourceRange))
      },
      "usageCalculation": enum ([UsageCalculation](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#UsageCalculation_1)),
      "unit": string,
    
      // Union field price_structure can be only one of the following:
      "pricePerUnit": {
        object ([Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money))
      }
      // End of list of possible types for union field price_structure.
    }  
  
Fields  
---  
`podResource` |  `enum (`[PodResource](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#PodResource)`)` Output only. The pod resource type that the SKU applies to. SKUs with a non-default value are referred to as "resource-based" SKUs.  
`podResourceRange` |  `object (`[PodResourceRange](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#PodResourceRange)`)` Output only. The range of pod resource values that the SKU applies to. The collection of SKUs in effect at any given time targeting the same service annotation and pod resource type will cover all possible values for that pod resource type without overlap. Such a collection of SKUs form a "tiered" price structure over the possible values of the pod resource, with each SKU acting as a "tier".NOTE: This is distinct from a SKU with [tiered pricing](https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing).  
`usageCalculation` |  `enum (`[UsageCalculation](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#UsageCalculation_1)`)` Output only. Determines how the customer's usage is calculated.  
`unit` |  `string` Output only. The price unit of the SKU. See <https://ucum.org/ucum.html> for the format of the price unit. For linear-priced memory SKUs, the price unit is 'GiBy.h'. For all other SKUs, the price unit is 'h'. This includes linear-priced VCPU, GPU, and TPU SKUs because these resources have unitless dimensions and the application of these scaling factors does not change the price unit.  
Union field `price_structure`. The billing model applied to meter and bill the customer's usage arising from running k8s pods covered by the scope of the SKU. `price_structure` can be only one of the following:  
`pricePerUnit` |  `object (`[Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money)`)` The price per unit of usage. The customer's usage charge is computed by measuring the customer's consumption denominated in price units and multiplying by this price.  
  
## PodResource

The pod [resource type](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) that the SKU applies to.

Enums  
---  
`POD_RESOURCE_UNSPECIFIED` | Unused.  
`VCPU_COUNT` | The SKU applies based on the pod's [vCPU count](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/).  
`MEMORY_BYTES` | The SKU applies based on the pod's [memory size](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/) in bytes.  
`GPU_COUNT` | The SKU applies based on the pod's GPU count.  
`TPU_COUNT` | The SKU applies based on the pod's [TPU count](https://cloud.google.com/kubernetes-engine/docs/concepts/tpus#how_tpus_work).  
  
## PodResourceRange

The range of pod resource values that the SKU applies to.

JSON representation  
---  
      
    
    {
      "startValue": string,
      "endValue": string
    }  
  
Fields  
---  
`startValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The inclusive lower bound of the range.  
`endValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The exclusive upper bound of the range. If no end value is specified, the range is unbounded from above.  
  
## UsageCalculation

Determines how the customer's usage is calculated.

Enums  
---  
`USAGE_CALCULATION_UNSPECIFIED` | Unused.  
`POD_RUNTIME` | Usage is calculated from pod runtime. The customer's usage is metered in a manner similar to the [GKE Autopilot mode for pods without specific hardware requirements](https://cloud.google.com/kubernetes-engine/pricing), priced on a per-pod basis in units of hours and measured in one-second increments, with no minimum duration.A SKU using this usage calculation is referred to as "flat" because the customer's usage charge is independent of the pod shape apart from determining whether the SKU applies to the pod.  
`LINEAR_RESOURCE_SCALED_POD_RUNTIME` | Usage is calculated from pod runtime and size. This calculation mode is only applicable to resource-based SKUs. Usage is calculated by measuring the pod runtime in the same manner as for `POD_RUNTIME` and multiplying by the pod's resource value matching the SKU's pod resource type. This converts the price from per-pod-hour to per-pod-hour-per-resource, which changes the price unit for memory SKUs to 'GiBy.h'. The price unit otherwise remains 'h' because the other resources are dimensionless.A SKU using this usage calculation is referred to as "linear" because the customer's usage charge is linearly proportional to the pod's resource value.  
  
## AiPlatformManagedModelUsageFee

Details about a SKU pricing usage of an [AI Platform Managed Model (MaaS)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models).

JSON representation  
---  
      
    
    {
      "usageMetric": {
        object ([AiPlatformManagedModelUsageMetric](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#AiPlatformManagedModelUsageMetric))
      },
      "location": {
        object ([AiPlatformManagedModelEndpointLocation](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#AiPlatformManagedModelEndpointLocation))
      },
      "predictionMode": enum ([PredictionMode](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#PredictionMode)),
      "combinedRequestInputTokensRange": {
        object ([CombinedRequestInputTokensRange](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#CombinedRequestInputTokensRange))
      },
      "provisionedThroughputOverage": {
        object ([ProvisionedThroughputOverage](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#ProvisionedThroughputOverage))
      },
    
      // Union field price_structure can be only one of the following:
      "tieredPrice": {
        object ([TieredPrice](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#TieredPrice))
      }
      // End of list of possible types for union field price_structure.
    }  
  
Fields  
---  
`usageMetric` |  `object (`[AiPlatformManagedModelUsageMetric](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#AiPlatformManagedModelUsageMetric)`)` Output only. The usage metric that the SKU applies to.  
`location` |  `object (`[AiPlatformManagedModelEndpointLocation](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#AiPlatformManagedModelEndpointLocation)`)` Output only. The model endpoint location where usage is priced by this SKU. If no location is specified, the SKU applies to usage in all locations.  
`predictionMode` |  `enum (`[PredictionMode](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#PredictionMode)`)` Output only. The prediction mode of requests that the SKU applies to.  
`combinedRequestInputTokensRange` |  `object (`[CombinedRequestInputTokensRange](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#CombinedRequestInputTokensRange)`)` Output only. The range of aggregated input token values covered by the SKU. Unset if the SKU is not scoped to a particular range. A request is in scope for this SKU if its aggregated input token value falls within the range. The collection of SKUs in effect at any given time scoped to a particular aggregated input token value range will cover all possible values without overlap. Such a collection of SKUs form a "tiered" price structure over the possible value, with each SKU acting as a "tier".NOTE: This is distinct from a SKU with [tiered pricing](https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing).  
`provisionedThroughputOverage` |  `object (`[ProvisionedThroughputOverage](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#ProvisionedThroughputOverage)`)` Output only. Set when the SKU is a historical provisioned throughput overage SKU. Starting 2025-08-26 such SKUs have no effect, and usage in excess of provisioned throughput quota is now metered as standard usage. This field is set only in historical SKU timeline entries for overage SKUs belonging to partners that offered provisioned throughput for AI Platform managed model products prior to the unification of standard usage and provisioned throughput overage metering.  
Union field `price_structure`. The billing model applied to bill the customer's usage. `price_structure` can be only one of the following:  
`tieredPrice` |  `object (`[TieredPrice](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#TieredPrice)`)` Output only. [Tiered pricing](https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing) of the SKU.  
  
## AiPlatformManagedModelUsageMetric

The usage metric that the SKU applies to.

JSON representation  
---  
      
    
    {
    
      // Union field metric can be only one of the following:
      "inputTokensMetric": {
        object ([InputTokensMetric](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#InputTokensMetric))
      },
      "cacheReadInputTokensMetric": {
        object ([CacheReadInputTokensMetric](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#CacheReadInputTokensMetric))
      },
      "cacheWriteInputTokensMetric": {
        object ([CacheWriteInputTokensMetric](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#CacheWriteInputTokensMetric))
      },
      "outputTokensMetric": {
        object ([OutputTokensMetric](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#OutputTokensMetric))
      },
      "webSearchRequestsMetric": {
        object ([WebSearchRequestsMetric](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#WebSearchRequestsMetric))
      }
      // End of list of possible types for union field metric.
    }  
  
Fields  
---  
Union field `metric`. The usage metric that the SKU applies to. `metric` can be only one of the following:  
`inputTokensMetric` |  `object (`[InputTokensMetric](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#InputTokensMetric)`)` Output only. Input tokens read from the prediction endpoint input.  
`cacheReadInputTokensMetric` |  `object (`[CacheReadInputTokensMetric](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#CacheReadInputTokensMetric)`)` Output only. Input tokens read from the cache.  
`cacheWriteInputTokensMetric` |  `object (`[CacheWriteInputTokensMetric](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#CacheWriteInputTokensMetric)`)` Output only. Input tokens written to the cache.  
`outputTokensMetric` |  `object (`[OutputTokensMetric](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#OutputTokensMetric)`)` Output only. Output tokens returned from the prediction endpoint.  
`webSearchRequestsMetric` |  `object (`[WebSearchRequestsMetric](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#WebSearchRequestsMetric)`)` Output only. Web search requests executed by the model.  
  
## InputTokensMetric

This type has no fields.

Input tokens read from the input to the prediction endpoint. The unit for this metric is dimensionless.

## CacheReadInputTokensMetric

This type has no fields.

Input tokens read from the cache. The unit for this metric is dimensionless.

## CacheWriteInputTokensMetric

Input tokens written to the cache. The unit for this metric is dimensionless.

JSON representation  
---  
      
    
    {
      "ttl": string
    }  
  
Fields  
---  
`ttl` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The duration the write is retained in the cache.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## OutputTokensMetric

This type has no fields.

Output tokens returned from the prediction endpoint. The unit for this metric is dimensionless.

## WebSearchRequestsMetric

This type has no fields.

Web search requests executed by the model. The unit for this metric is dimensionless.

## AiPlatformManagedModelEndpointLocation

Location scope for a SKU that applies to an AI Platform Managed Model endpoint.

JSON representation  
---  
      
    
    {
    
      // Union field location can be only one of the following:
      "regionId": string,
      "globalEndpoint": boolean,
      "multiRegionId": string
      // End of list of possible types for union field location.
    }  
  
Fields  
---  
Union field `location`. The location scope of the SKU. `location` can be only one of the following:  
`regionId` |  `string` Output only. The SKU applies to a region.  
`globalEndpoint` |  `boolean` Output only. The SKU applies to a [global endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations). **Note** : This is distinct from the conventional meaning of "global" as a SKU that applies to all locations.  
`multiRegionId` |  `string` Output only. The SKU applies to a multi-region.  
  
## PredictionMode

The prediction modes of requests that the SKU applies to.

Enums  
---  
`PREDICTION_MODE_UNSPECIFIED` | The SKU does not distinguish between prediction modes.  
`ONLINE_PREDICTION` | The SKU applies to online prediction.  
`BATCH_PREDICTION` | The SKU applies to batch prediction.  
  
## CombinedRequestInputTokensRange

The range of aggregated input token values covered by the SKU.

A request to a managed model has an aggregated input token value determined by the sum of the metric values of the input token metrics.

  * input tokens
  * cache read input tokens
  * cache write input tokens

JSON representation  
---  
      
    
    {
      "startValue": string,
      "endValue": string
    }  
  
Fields  
---  
`startValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The inclusive lower bound of the range.  
`endValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The exclusive upper bound of the range. If no end value is specified, the range is unbounded from above.  
  
## ProvisionedThroughputOverage

Additional details present for historical provisioned throughput "overage" SKUs that applied charges only to usage above the customer's provisioned throughput quota threshold.

JSON representation  
---  
      
    
    {
      "service": string
    }  
  
Fields  
---  
`service` |  `string` Output only. The service whose usage the overage SKU applied to.  
  
## AiPlatformProvisionedThroughputFee

Details about a SKU pricing reservation of [AI Platform Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput).

Customers may purchase provisioned throughput reservations for AI Platform managed model products. This provides the customer with provisioned throughput quota for a particular model and location. Model usage below the provisioned throughput quota threshold is voided and is not charged by the product's managed model usage fees.

JSON representation  
---  
      
    
    {
      "location": {
        object ([AiPlatformManagedModelEndpointLocation](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#AiPlatformManagedModelEndpointLocation))
      },
      "unit": string,
    
      // Union field term can be only one of the following:
      "termDurationMonths": integer
      // End of list of possible types for union field term.
    
      // Union field price_structure can be only one of the following:
      "gsuPricePerUnit": {
        object ([Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money))
      }
      // End of list of possible types for union field price_structure.
    }  
  
Fields  
---  
`location` |  `object (`[AiPlatformManagedModelEndpointLocation](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#AiPlatformManagedModelEndpointLocation)`)` Output only. The location where provisioned throughput is priced by this SKU.  
`unit` |  `string` Output only. The price unit of the SKU. See <https://ucum.org/ucum.html> for the format of the price unit. Since provisioned throughput reservations are billed by duration, this will always be a time unit. The price unit of a provisioned throughput SKU is not necessarily the same as the reservation term. This field is unrelated to the [Generative AI Scale Unit (GSU)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/measure-provisioned-throughput).Currently the unit is always months ('mo'). Additional time units may be supported in future.The customary unit month ('mo') requires special handling to account for the variable duration of months. A price may be denominated in units of months, but the duration the reservation is active is measured in metric time and customers are billed on that basis. The exact hourly or per-second price can be calculated by dividing the monthly price by the number of hours or seconds in the desired month. A reservation active for N months is rarely billed exactly N times the monthly price. This is intended and is not a billing error.  
Union field `term`. The provisioned throughput reservation term priced by this SKU. `term` can be only one of the following:  
`termDurationMonths` |  `integer` Output only. The duration of the provisioned throughput reservation in months.  
Union field `price_structure`. The billing model applied to bill the customer's usage. `price_structure` can be only one of the following:  
`gsuPricePerUnit` |  `object (`[Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money)`)` The price per [Generative AI Scale Unit (GSU)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/measure-provisioned-throughput) per `unit`. A provisioned throughput reservation reserves a certain number of GSUs, and the customer is billed for those GSUs on a continuous basis for the duration of the reservation.  
  
## AiPlatformDeployedModelUsageFee

Details about a SKU pricing usage of an [AI Platform Self Deployed Model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/self-deployed-models).

JSON representation  
---  
      
    
    {
      "unit": string,
      "usageCalculation": enum ([UsageCalculation](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#UsageCalculation_2)),
    
      // Union field hardware_resource can be only one of the following:
      "acceleratorType": string
      // End of list of possible types for union field hardware_resource.
    
      // Union field price_structure can be only one of the following:
      "pricePerUnit": {
        object ([Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money))
      }
      // End of list of possible types for union field price_structure.
    }  
  
Fields  
---  
`unit` |  `string` Output only. The price unit of the SKU. See <https://ucum.org/ucum.html> for the format of the price unit. Currently the unit is always hours ('h'). This may change in future.  
`usageCalculation` |  `enum (`[UsageCalculation](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus#UsageCalculation_2)`)` Output only. Determines how the customer's usage is calculated.  
Union field `hardware_resource`. The type of hardware to which the SKU's licensing fee applies. Models are deployed with a customer-specified [MachineSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/MachineSpec) that determines the hardware resources used by the model. `hardware_resource` can be only one of the following:  
`acceleratorType` |  `string` Output only. The SKU applies to a specific accelerator type. Contains the name of the matching [AI Platform AcceleratorType]( <https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/MachineSpec#AcceleratorType)>. The corresponding linear scaling value is the dimensionless [`accelerator_count`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/MachineSpec#FIELDS.accelerator_count).  
Union field `price_structure`. The billing model applied to bill the customer's usage arising from running deployed models covered by the scope of the SKU. `price_structure` can be only one of the following:  
`pricePerUnit` |  `object (`[Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money)`)` Output only. The price per unit of usage. The customer's usage charge is computed by measuring the customer's consumption denominated in price units and multiplying by this price.  
  
## UsageCalculation

Determines how the customer's usage is calculated.

Enums  
---  
`USAGE_CALCULATION_UNSPECIFIED` | Unused.  
`LINEAR_RESOURCE_SCALED_DEPLOYMENT_RUNTIME` | Usage is calculated from deployment runtime and size. Usage is calculated by measuring the deployment runtime in hours and multiplying by the amount of the deployed model's hardware resource matching the SKU's hardware resource type. This results in a composite `unit` of hours ('h') multiplied by the unit that denominates the hardware resource, though note that multiplying by the dimensionless unit ("1") has no effect.  
  
## FlatSubscriptionFee

Details about a SKU charging a flat subscription fee.

JSON representation  
---  
      
    
    {
      "unit": string,
    
      // Union field price_structure can be only one of the following:
      "pricePerUnit": {
        object ([Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money))
      }
      // End of list of possible types for union field price_structure.
    }  
  
Fields  
---  
`unit` |  `string` Output only. The unit of the subscription SKU. See <https://ucum.org/ucum.html> for the format of the price unit. Since subscriptions are billed by duration, this will always be a time unit. The price unit of a subscription SKU is not necessarily the same as the subscription period of the corresponding StandardOffers.Currently the unit is always months ('mo'). Additional time units may be supported in future.The unit month ('mo') is a customary time unit and requires special handling to account for the variable duration of months. A price may be denominated in units of months, but the duration the subscription is active is measured in metric time and customers are billed on that basis. The exact hourly or per-second price can be calculated by dividing the monthly price by the number of hours or seconds in the desired month. A subscription active for N months is rarely billed exactly N times the monthly price. This is intended and is not a billing error.  
Union field `price_structure`. The billing model applied to bill the customer's subscription. `price_structure` can be only one of the following:  
`pricePerUnit` |  `object (`[Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money)`)` Output only. The price per time unit the subscription is active.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus/get)`

|  Gets details of a single Sku.  
  
### `[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services.skus/list)`

|  Lists Skus for the given parent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-15 UTC."],[],[]] 
