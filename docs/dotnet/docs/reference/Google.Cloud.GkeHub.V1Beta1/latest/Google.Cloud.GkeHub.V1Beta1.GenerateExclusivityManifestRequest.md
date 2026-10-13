---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1Beta1/latest/Google.Cloud.GkeHub.V1Beta1.GenerateExclusivityManifestRequest
title: GKE Hub v1beta1 API - Class GenerateExclusivityManifestRequest (2.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:29.347143+00:00
---

# GKE Hub v1beta1 API - Class GenerateExclusivityManifestRequest (2.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1Beta1/latest/Google.Cloud.GkeHub.V1Beta1.GenerateExclusivityManifestRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  GKE Hub v1beta1 API - Class GenerateExclusivityManifestRequest (2.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta09 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1Beta1/latest/Google.Cloud.GkeHub.V1Beta1.GenerateExclusivityManifestRequest)
  * [ 2.0.0-beta08 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1Beta1/2.0.0-beta08/Google.Cloud.GkeHub.V1Beta1.GenerateExclusivityManifestRequest)
  * [ 1.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1Beta1/1.0.0-beta04/Google.Cloud.GkeHub.V1Beta1.GenerateExclusivityManifestRequest)


    
    
    public sealed class GenerateExclusivityManifestRequest : IMessage<GenerateExclusivityManifestRequest>, IEquatable<GenerateExclusivityManifestRequest>, IDeepCloneable<GenerateExclusivityManifestRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the GKE Hub v1beta1 API class GenerateExclusivityManifestRequest.

The request to generate the manifests for exclusivity artifacts.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GenerateExclusivityManifestRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GenerateExclusivityManifestRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1Beta1/latest/Google.Cloud.GkeHub.V1Beta1.GenerateExclusivityManifestRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GenerateExclusivityManifestRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1Beta1/latest/Google.Cloud.GkeHub.V1Beta1.GenerateExclusivityManifestRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GenerateExclusivityManifestRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1Beta1/latest/Google.Cloud.GkeHub.V1Beta1.GenerateExclusivityManifestRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GkeHub.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1Beta1/latest/Google.Cloud.GkeHub.V1Beta1)

## Assembly

Google.Cloud.GkeHub.V1Beta1.dll

## Constructors 

### GenerateExclusivityManifestRequest()
    
    
    public GenerateExclusivityManifestRequest()

### GenerateExclusivityManifestRequest(GenerateExclusivityManifestRequest)
    
    
    public GenerateExclusivityManifestRequest(GenerateExclusivityManifestRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GenerateExclusivityManifestRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1Beta1/latest/Google.Cloud.GkeHub.V1Beta1.GenerateExclusivityManifestRequest)`  
  
  
## Properties 

### CrManifest
    
    
    public string CrManifest { get; set; }

Optional. The YAML manifest of the membership CR retrieved by `kubectl get memberships membership`. Leave empty if the resource does not exist.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CrdManifest
    
    
    public string CrdManifest { get; set; }

Optional. The YAML manifest of the membership CRD retrieved by `kubectl get customresourcedefinitions membership`. Leave empty if the resource does not exist.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MembershipName
    
    
    public MembershipName MembershipName { get; set; }

[MembershipName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1Beta1/latest/Google.Cloud.GkeHub.V1Beta1.MembershipName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1Beta1/latest/Google.Cloud.GkeHub.V1Beta1.GenerateExclusivityManifestRequest#Google_Cloud_GkeHub_V1Beta1_GenerateExclusivityManifestRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[MembershipName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1Beta1/latest/Google.Cloud.GkeHub.V1Beta1.MembershipName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The Membership resource name in the format `projects/*/locations/*/memberships/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
