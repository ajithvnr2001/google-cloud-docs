---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackage.Types.ResourceBundleTag
title: Config Delivery v1beta API - Class FleetPackage.Types.ResourceBundleTag (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:11.560428+00:00
---

# Config Delivery v1beta API - Class FleetPackage.Types.ResourceBundleTag (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackage.Types.ResourceBundleTag

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Config Delivery v1beta API - Class FleetPackage.Types.ResourceBundleTag (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class FleetPackage.Types.ResourceBundleTag : IMessage<FleetPackage.Types.ResourceBundleTag>, IEquatable<FleetPackage.Types.ResourceBundleTag>, IDeepCloneable<FleetPackage.Types.ResourceBundleTag>, IBufferMessage, IMessage

Reference documentation and code samples for the Config Delivery v1beta API class FleetPackage.Types.ResourceBundleTag.

ResourceBundleTag contains the information to refer to a release for a `ResourceBundle`.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FleetPackage.Types.ResourceBundleTag

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackage)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackage.Types)[ResourceBundleTag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackage.Types.ResourceBundleTag), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackage)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackage.Types)[ResourceBundleTag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackage.Types.ResourceBundleTag), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackage)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackage.Types)[ResourceBundleTag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackage.Types.ResourceBundleTag), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ConfigDelivery.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta)

## Assembly

Google.Cloud.ConfigDelivery.V1Beta.dll

## Constructors 

### ResourceBundleTag()
    
    
    public ResourceBundleTag()

### ResourceBundleTag(ResourceBundleTag)
    
    
    public ResourceBundleTag(FleetPackage.Types.ResourceBundleTag other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackage)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackage.Types)[ResourceBundleTag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackage.Types.ResourceBundleTag)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. Name of the `ResourceBundle`. Format is projects/{p}/locations/{l}/resourceBundles/{r}.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResourceBundleName
    
    
    public ResourceBundleName ResourceBundleName { get; set; }

[ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.ResourceBundleName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackage.Types.ResourceBundleTag#Google_Cloud_ConfigDelivery_V1Beta_FleetPackage_Types_ResourceBundleTag_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.ResourceBundleName)` |   
  
### Tag
    
    
    public string Tag { get; set; }

Required. Tag refers to a version of the release in a `ResourceBundle`. This is a Git tag in the semantic version format `vX.Y.Z`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
