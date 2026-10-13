---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.Fleet
title: Config Delivery v1beta API - Class Fleet (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:35.920280+00:00
---

# Config Delivery v1beta API - Class Fleet (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.Fleet

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Config Delivery v1beta API - Class Fleet (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class Fleet : IMessage<Fleet>, IEquatable<Fleet>, IDeepCloneable<Fleet>, IBufferMessage, IMessage

Reference documentation and code samples for the Config Delivery v1beta API class Fleet.

The fleet where the `FleetPackage` should be deployed.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Fleet

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Fleet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.Fleet), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Fleet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.Fleet), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Fleet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.Fleet), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ConfigDelivery.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta)

## Assembly

Google.Cloud.ConfigDelivery.V1Beta.dll

## Constructors 

### Fleet()
    
    
    public Fleet()

### Fleet(Fleet)
    
    
    public Fleet(Fleet other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Fleet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.Fleet)`  
  
  
## Properties 

### Project
    
    
    public string Project { get; set; }

Required. The host project for the GKE fleet. Format is `projects/{project}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProjectAsProjectName
    
    
    public ProjectName ProjectAsProjectName { get; set; }

[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)-typed view over the [Project](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.Fleet#Google_Cloud_ConfigDelivery_V1Beta_Fleet_Project) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)` |   
  
### Selector
    
    
    public Fleet.Types.LabelSelector Selector { get; set; }

Optional. selector allows targeting a subset of fleet members using their labels.

**Property Value**  
---  
**Type** | **Description**  
`[Fleet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.Fleet)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.Fleet.Types)[LabelSelector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.Fleet.Types.LabelSelector)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
