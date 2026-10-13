---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.CreateWorkstationRequest
title: Cloud Workstations v1 API - Class CreateWorkstationRequest (1.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:47:45.871437+00:00
---

# Cloud Workstations v1 API - Class CreateWorkstationRequest (1.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.CreateWorkstationRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Workstations v1 API - Class CreateWorkstationRequest (1.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.0 (latest)  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class CreateWorkstationRequest : IMessage<CreateWorkstationRequest>, IEquatable<CreateWorkstationRequest>, IDeepCloneable<CreateWorkstationRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Workstations v1 API class CreateWorkstationRequest.

Message for creating a CreateWorkstation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateWorkstationRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateWorkstationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.CreateWorkstationRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateWorkstationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.CreateWorkstationRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateWorkstationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.CreateWorkstationRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Workstations.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1)

## Assembly

Google.Cloud.Workstations.V1.dll

## Constructors 

### CreateWorkstationRequest()
    
    
    public CreateWorkstationRequest()

### CreateWorkstationRequest(CreateWorkstationRequest)
    
    
    public CreateWorkstationRequest(CreateWorkstationRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateWorkstationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.CreateWorkstationRequest)`  
  
  
## Properties 

### Parent
    
    
    public string Parent { get; set; }

Required. Parent resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsWorkstationConfigName
    
    
    public WorkstationConfigName ParentAsWorkstationConfigName { get; set; }

[WorkstationConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationConfigName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.CreateWorkstationRequest#Google_Cloud_Workstations_V1_CreateWorkstationRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[WorkstationConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationConfigName)` |   
  
### ValidateOnly
    
    
    public bool ValidateOnly { get; set; }

Optional. If set, validate the request and preview the result, but do not actually apply it.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Workstation
    
    
    public Workstation Workstation { get; set; }

Required. Workstation to create. If source_workstation is specified, the user must have `workstations.workstations.use` permission on the source workstation, and the Cloud Workstations Service Agent for the project where you are creating the new workstation must have compute.disks.createSnapshot and compute.snapshots.useReadOnly on the source project.

**Property Value**  
---  
**Type** | **Description**  
`[Workstation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.Workstation)` |   
  
### WorkstationId
    
    
    public string WorkstationId { get; set; }

Required. ID to use for the workstation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-08 UTC."],[],[]] 
