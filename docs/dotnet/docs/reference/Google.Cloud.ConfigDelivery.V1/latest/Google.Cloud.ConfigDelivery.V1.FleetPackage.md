---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage
title: Config Delivery v1 API - Class FleetPackage (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:51.287009+00:00
---

# Config Delivery v1 API - Class FleetPackage (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Config Delivery v1 API - Class FleetPackage (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class FleetPackage : IMessage<FleetPackage>, IEquatable<FleetPackage>, IDeepCloneable<FleetPackage>, IBufferMessage, IMessage

Reference documentation and code samples for the Config Delivery v1 API class FleetPackage.

A `FleetPackage` resource in the Config Delivery API.

A `FleetPackage` defines a package through which kubernetes configuration is deployed to a fleet of kubernetes clusters.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FleetPackage

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ConfigDelivery.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1)

## Assembly

Google.Cloud.ConfigDelivery.V1.dll

## Constructors 

### FleetPackage()
    
    
    public FleetPackage()

### FleetPackage(FleetPackage)
    
    
    public FleetPackage(FleetPackage other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage)`  
  
  
## Properties 

### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Time at which the `FleetPackage` was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DeletionPropagationPolicy
    
    
    public DeletionPropagationPolicy DeletionPropagationPolicy { get; set; }

Optional. Information around how to handle kubernetes resources at the target clusters when the `FleetPackage` is deleted.

**Property Value**  
---  
**Type** | **Description**  
`[DeletionPropagationPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.DeletionPropagationPolicy)` |   
  
### FleetPackageName
    
    
    public FleetPackageName FleetPackageName { get; set; }

[FleetPackageName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackageName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage#Google_Cloud_ConfigDelivery_V1_FleetPackage_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[FleetPackageName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackageName)` |   
  
### Info
    
    
    public FleetPackageInfo Info { get; set; }

Output only. Information containing the rollout status of the `FleetPackage` across all the target clusters.

**Property Value**  
---  
**Type** | **Description**  
`[FleetPackageInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackageInfo)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional. Labels are attributes that can be set and used by both the user and by Config Delivery. Labels must meet the following constraints:

  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
  * All characters must use UTF-8 encoding, and international characters are allowed.
  * Keys must start with a lowercase letter or international character.
  * Each resource is limited to a maximum of 64 labels.



Both keys and values are additionally constrained to be <= 128 bytes.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. Name of the `FleetPackage`. Format is `projects/{project}/locations/{location}/fleetPackages/{fleetPackage}`. The `fleetPackage` component must match `[a-z][a-z0-9\-]{0,62}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResourceBundleSelector
    
    
    public FleetPackage.Types.ResourceBundleSelector ResourceBundleSelector { get; set; }

Required. Information specifying the source of kubernetes configuration to deploy.

**Property Value**  
---  
**Type** | **Description**  
`[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage.Types)[ResourceBundleSelector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage.Types.ResourceBundleSelector)` |   
  
### RolloutStrategy
    
    
    public RolloutStrategy RolloutStrategy { get; set; }

Optional. The strategy to use to deploy kubernetes configuration to clusters.

**Property Value**  
---  
**Type** | **Description**  
`[RolloutStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.RolloutStrategy)` |   
  
### State
    
    
    public FleetPackage.Types.State State { get; set; }

Optional. The desired state of the fleet package.

**Property Value**  
---  
**Type** | **Description**  
`[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage.Types.State)` |   
  
### Target
    
    
    public FleetPackage.Types.Target Target { get; set; }

Optional. Configuration to select target clusters to deploy kubernetes configuration to.

**Property Value**  
---  
**Type** | **Description**  
`[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage.Types)[Target](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage.Types.Target)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Most recent time at which the `FleetPackage` was updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### VariantSelector
    
    
    public FleetPackage.Types.VariantSelector VariantSelector { get; set; }

Required. Information specifying how to map a `ResourceBundle` variant to a target cluster.

**Property Value**  
---  
**Type** | **Description**  
`[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage.Types)[VariantSelector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.FleetPackage.Types.VariantSelector)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
