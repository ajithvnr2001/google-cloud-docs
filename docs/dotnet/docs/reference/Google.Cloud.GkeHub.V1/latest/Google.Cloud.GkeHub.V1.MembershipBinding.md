---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.MembershipBinding
title: GKE Hub v1 API - Class MembershipBinding (2.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:46.525806+00:00
---

# GKE Hub v1 API - Class MembershipBinding (2.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.MembershipBinding

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  GKE Hub v1 API - Class MembershipBinding (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.MembershipBinding)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.7.0/Google.Cloud.GkeHub.V1.MembershipBinding)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.6.0/Google.Cloud.GkeHub.V1.MembershipBinding)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.5.0/Google.Cloud.GkeHub.V1.MembershipBinding)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.4.0/Google.Cloud.GkeHub.V1.MembershipBinding)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.3.0/Google.Cloud.GkeHub.V1.MembershipBinding)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.2.0/Google.Cloud.GkeHub.V1.MembershipBinding)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.1.0/Google.Cloud.GkeHub.V1.MembershipBinding)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.0.0/Google.Cloud.GkeHub.V1.MembershipBinding)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/1.2.0/Google.Cloud.GkeHub.V1.MembershipBinding)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/1.1.0/Google.Cloud.GkeHub.V1.MembershipBinding)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/1.0.0/Google.Cloud.GkeHub.V1.MembershipBinding)


    
    
    public sealed class MembershipBinding : IMessage<MembershipBinding>, IEquatable<MembershipBinding>, IDeepCloneable<MembershipBinding>, IBufferMessage, IMessage

Reference documentation and code samples for the GKE Hub v1 API class MembershipBinding.

MembershipBinding is a subresource of a Membership, representing what Fleet Scopes (or other, future Fleet resources) a Membership is bound to.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MembershipBinding

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[MembershipBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.MembershipBinding), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[MembershipBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.MembershipBinding), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[MembershipBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.MembershipBinding), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GkeHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1)

## Assembly

Google.Cloud.GkeHub.V1.dll

## Constructors 

### MembershipBinding()
    
    
    public MembershipBinding()

### MembershipBinding(MembershipBinding)
    
    
    public MembershipBinding(MembershipBinding other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[MembershipBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.MembershipBinding)`  
  
  
## Properties 

### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. When the membership binding was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DeleteTime
    
    
    public Timestamp DeleteTime { get; set; }

Output only. When the membership binding was deleted.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### HasScope
    
    
    public bool HasScope { get; }

Gets whether the "scope" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional. Labels for this MembershipBinding.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MembershipBindingName
    
    
    public MembershipBindingName MembershipBindingName { get; set; }

[MembershipBindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.MembershipBindingName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.MembershipBinding#Google_Cloud_GkeHub_V1_MembershipBinding_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[MembershipBindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.MembershipBindingName)` |   
  
### Name
    
    
    public string Name { get; set; }

The resource name for the membershipbinding itself `projects/{project}/locations/{location}/memberships/{membership}/bindings/{membershipbinding}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Scope
    
    
    public string Scope { get; set; }

A Scope resource name in the format `projects/*/locations/*/scopes/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ScopeAsScopeName
    
    
    public ScopeName ScopeAsScopeName { get; set; }

[ScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ScopeName)-typed view over the [Scope](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.MembershipBinding#Google_Cloud_GkeHub_V1_MembershipBinding_Scope) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ScopeName)` |   
  
### State
    
    
    public MembershipBindingLifecycleState State { get; set; }

Output only. State of the membership binding resource.

**Property Value**  
---  
**Type** | **Description**  
`[MembershipBindingLifecycleState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.MembershipBindingLifecycleState)` |   
  
### TargetCase
    
    
    public MembershipBinding.TargetOneofCase TargetCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MembershipBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.MembershipBinding)[TargetOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.MembershipBinding.TargetOneofCase)` |   
  
### Uid
    
    
    public string Uid { get; set; }

Output only. Google-generated UUID for this resource. This is unique across all membershipbinding resources. If a membershipbinding resource is deleted and another resource with the same name is created, it gets a different uid.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. When the membership binding was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
