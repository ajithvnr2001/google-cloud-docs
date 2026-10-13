---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentTypeRequirement
title: Cloud Optimization v1 API - Class ShipmentTypeRequirement (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:03.770185+00:00
---

# Cloud Optimization v1 API - Class ShipmentTypeRequirement (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentTypeRequirement

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Optimization v1 API - Class ShipmentTypeRequirement (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentTypeRequirement)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.6.0/Google.Cloud.Optimization.V1.ShipmentTypeRequirement)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.5.0/Google.Cloud.Optimization.V1.ShipmentTypeRequirement)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.4.0/Google.Cloud.Optimization.V1.ShipmentTypeRequirement)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.3.0/Google.Cloud.Optimization.V1.ShipmentTypeRequirement)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.2.0/Google.Cloud.Optimization.V1.ShipmentTypeRequirement)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.1.0/Google.Cloud.Optimization.V1.ShipmentTypeRequirement)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.0.0/Google.Cloud.Optimization.V1.ShipmentTypeRequirement)
  * [ 1.0.0-beta01 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/1.0.0-beta01/Google.Cloud.Optimization.V1.ShipmentTypeRequirement)


    
    
    public sealed class ShipmentTypeRequirement : IMessage<ShipmentTypeRequirement>, IEquatable<ShipmentTypeRequirement>, IDeepCloneable<ShipmentTypeRequirement>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Optimization v1 API class ShipmentTypeRequirement.

Specifies requirements between shipments based on their shipment_type. The specifics of the requirement are defined by the requirement mode.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ShipmentTypeRequirement

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ShipmentTypeRequirement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentTypeRequirement), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ShipmentTypeRequirement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentTypeRequirement), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ShipmentTypeRequirement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentTypeRequirement), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Optimization.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1)

## Assembly

Google.Cloud.Optimization.V1.dll

## Constructors 

### ShipmentTypeRequirement()
    
    
    public ShipmentTypeRequirement()

### ShipmentTypeRequirement(ShipmentTypeRequirement)
    
    
    public ShipmentTypeRequirement(ShipmentTypeRequirement other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ShipmentTypeRequirement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentTypeRequirement)`  
  
  
## Properties 

### DependentShipmentTypes
    
    
    public RepeatedField<string> DependentShipmentTypes { get; }

All shipments with a type in the `dependent_shipment_types` field require at least one shipment of type `required_shipment_type_alternatives` to be visited on the same route.

NOTE: Chains of requirements such that a `shipment_type` depends on itself are not allowed.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RequiredShipmentTypeAlternatives
    
    
    public RepeatedField<string> RequiredShipmentTypeAlternatives { get; }

List of alternative shipment types required by the `dependent_shipment_types`.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RequirementMode
    
    
    public ShipmentTypeRequirement.Types.RequirementMode RequirementMode { get; set; }

Mode applied to the requirement.

**Property Value**  
---  
**Type** | **Description**  
`[ShipmentTypeRequirement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentTypeRequirement)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentTypeRequirement.Types)[RequirementMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentTypeRequirement.Types.RequirementMode)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
