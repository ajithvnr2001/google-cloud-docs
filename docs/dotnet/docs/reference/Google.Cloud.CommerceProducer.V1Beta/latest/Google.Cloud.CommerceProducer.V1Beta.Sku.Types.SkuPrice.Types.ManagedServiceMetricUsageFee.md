---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee
title: Cloud Commerce Producer v1beta API - Class Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee (1.0.0-beta03) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:04.022714+00:00
---

# Cloud Commerce Producer v1beta API - Class Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee (1.0.0-beta03)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Commerce Producer v1beta API - Class Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee (1.0.0-beta03) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta03 (latest)  1.0.0-beta02 
    
    
    public sealed class Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee : IMessage<Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee>, IEquatable<Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee>, IDeepCloneable<Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Commerce Producer v1beta API class Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee.

Details about a SKU pricing usage of a [partner-reported custom billing metric](https://cloud.google.com/service-infrastructure/docs/reporting-billing-metrics) defined by the partner in the Service Management API and reported using the Service Control API.

The customer's usage charge is computed by converting the customer's reported consumption to the SKU's composite price unit and applying the graduated price from the appropriate price tier.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Sku](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types)[SkuPrice](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice.Types)[ManagedServiceMetricUsageFee](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Sku](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types)[SkuPrice](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice.Types)[ManagedServiceMetricUsageFee](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Sku](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types)[SkuPrice](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice.Types)[ManagedServiceMetricUsageFee](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CommerceProducer.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta)

## Assembly

Google.Cloud.CommerceProducer.V1Beta.dll

## Constructors 

### ManagedServiceMetricUsageFee()
    
    
    public ManagedServiceMetricUsageFee()

### ManagedServiceMetricUsageFee(ManagedServiceMetricUsageFee)
    
    
    public ManagedServiceMetricUsageFee(Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Sku](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types)[SkuPrice](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice.Types)[ManagedServiceMetricUsageFee](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee)`  
  
  
## Properties 

### CanonicalMetric
    
    
    public string CanonicalMetric { get; set; }

Output only. The name of the metric, in canonical format.

Note that in the canonical format the first character of the path component of the metric name is always uppercase, which may differ from the metric name in the service config. For example, a metric appearing in the service config as 'example.com/example_metric' will appear here in the SKU as 'example.com/Example_metric'. In the Service Management and Service Control APIs these two metric names are considered distinct, either or both may be defined, and usage must be reported using a name matching the name of a metric defined in the service config. But for billing purposes usage reported using either name will be aggregated under the canonical metric name.

Example: "example.com/Example_metric"

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PriceStructureCase
    
    
    public Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee.PriceStructureOneofCase PriceStructureCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Sku](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types)[SkuPrice](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice.Types)[ManagedServiceMetricUsageFee](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee)[PriceStructureOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice.Types.ManagedServiceMetricUsageFee.PriceStructureOneofCase)` |   
  
### TieredPrice
    
    
    public Sku.Types.SkuPrice.Types.TieredPrice TieredPrice { get; set; }

Output only. [Tiered pricing](https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing) of the SKU.

**Property Value**  
---  
**Type** | **Description**  
`[Sku](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types)[SkuPrice](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice.Types)[TieredPrice](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.Sku.Types.SkuPrice.Types.TieredPrice)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
