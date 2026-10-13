---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.CreateFindingRequest
title: Google Cloud Security Command Center v1p1beta1 API - Class CreateFindingRequest (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:22.870383+00:00
---

# Google Cloud Security Command Center v1p1beta1 API - Class CreateFindingRequest (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.CreateFindingRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Security Command Center v1p1beta1 API - Class CreateFindingRequest (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.CreateFindingRequest)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/3.0.0-beta05/Google.Cloud.SecurityCenter.V1P1Beta1.CreateFindingRequest)
  * [ 2.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/2.0.0-beta07/Google.Cloud.SecurityCenter.V1P1Beta1.CreateFindingRequest)


    
    
    public sealed class CreateFindingRequest : IMessage<CreateFindingRequest>, IEquatable<CreateFindingRequest>, IDeepCloneable<CreateFindingRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Security Command Center v1p1beta1 API class CreateFindingRequest.

Request message for creating a finding.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateFindingRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateFindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.CreateFindingRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateFindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.CreateFindingRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateFindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.CreateFindingRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenter.V1P1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1)

## Assembly

Google.Cloud.SecurityCenter.V1P1Beta1.dll

## Constructors 

### CreateFindingRequest()
    
    
    public CreateFindingRequest()

### CreateFindingRequest(CreateFindingRequest)
    
    
    public CreateFindingRequest(CreateFindingRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateFindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.CreateFindingRequest)`  
  
  
## Properties 

### Finding
    
    
    public Finding Finding { get; set; }

Required. The Finding being created. The name and security_marks will be ignored as they are both output only fields on this resource.

**Property Value**  
---  
**Type** | **Description**  
`[Finding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.Finding)` |   
  
### FindingId
    
    
    public string FindingId { get; set; }

Required. Unique identifier provided by the client within the parent scope.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. Resource name of the new finding's parent. Its format should be "organizations/[organization_id]/sources/[source_id]".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsSourceName
    
    
    public SourceName ParentAsSourceName { get; set; }

[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SourceName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.CreateFindingRequest#Google_Cloud_SecurityCenter_V1P1Beta1_CreateFindingRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SourceName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
