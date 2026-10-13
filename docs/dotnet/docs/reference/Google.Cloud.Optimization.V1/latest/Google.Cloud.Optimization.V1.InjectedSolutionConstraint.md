---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.InjectedSolutionConstraint
title: Cloud Optimization v1 API - Class InjectedSolutionConstraint (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:38.843715+00:00
---

# Cloud Optimization v1 API - Class InjectedSolutionConstraint (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.InjectedSolutionConstraint

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Optimization v1 API - Class InjectedSolutionConstraint (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.InjectedSolutionConstraint)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.6.0/Google.Cloud.Optimization.V1.InjectedSolutionConstraint)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.5.0/Google.Cloud.Optimization.V1.InjectedSolutionConstraint)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.4.0/Google.Cloud.Optimization.V1.InjectedSolutionConstraint)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.3.0/Google.Cloud.Optimization.V1.InjectedSolutionConstraint)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.2.0/Google.Cloud.Optimization.V1.InjectedSolutionConstraint)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.1.0/Google.Cloud.Optimization.V1.InjectedSolutionConstraint)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.0.0/Google.Cloud.Optimization.V1.InjectedSolutionConstraint)
  * [ 1.0.0-beta01 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/1.0.0-beta01/Google.Cloud.Optimization.V1.InjectedSolutionConstraint)


    
    
    public sealed class InjectedSolutionConstraint : IMessage<InjectedSolutionConstraint>, IEquatable<InjectedSolutionConstraint>, IDeepCloneable<InjectedSolutionConstraint>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Optimization v1 API class InjectedSolutionConstraint.

Solution injected in the request including information about which visits must be constrained and how they must be constrained.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > InjectedSolutionConstraint

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[InjectedSolutionConstraint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.InjectedSolutionConstraint), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[InjectedSolutionConstraint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.InjectedSolutionConstraint), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[InjectedSolutionConstraint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.InjectedSolutionConstraint), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Optimization.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1)

## Assembly

Google.Cloud.Optimization.V1.dll

## Constructors 

### InjectedSolutionConstraint()
    
    
    public InjectedSolutionConstraint()

### InjectedSolutionConstraint(InjectedSolutionConstraint)
    
    
    public InjectedSolutionConstraint(InjectedSolutionConstraint other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[InjectedSolutionConstraint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.InjectedSolutionConstraint)`  
  
  
## Properties 

### ConstraintRelaxations
    
    
    public RepeatedField<InjectedSolutionConstraint.Types.ConstraintRelaxation> ConstraintRelaxations { get; }

For zero or more groups of vehicles, specifies when and how much to relax constraints. If this field is empty, all non-empty vehicle routes are fully constrained.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[InjectedSolutionConstraint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.InjectedSolutionConstraint)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.InjectedSolutionConstraint.Types)[ConstraintRelaxation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.InjectedSolutionConstraint.Types.ConstraintRelaxation)` |   
  
### Routes
    
    
    public RepeatedField<ShipmentRoute> Routes { get; }

Routes of the solution to inject. Some routes may be omitted from the original solution. The routes and skipped shipments must satisfy the basic validity assumptions listed for `injected_first_solution_routes`.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ShipmentRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.ShipmentRoute)` |   
  
### SkippedShipments
    
    
    public RepeatedField<SkippedShipment> SkippedShipments { get; }

Skipped shipments of the solution to inject. Some may be omitted from the original solution. See the `routes` field.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SkippedShipment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.SkippedShipment)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
