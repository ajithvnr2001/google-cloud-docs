---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateSingleTenantHsmInstanceProposalRequest
title: Google Cloud Key Management Service v1 API - Class CreateSingleTenantHsmInstanceProposalRequest (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:48:59.345042+00:00
---

# Google Cloud Key Management Service v1 API - Class CreateSingleTenantHsmInstanceProposalRequest (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateSingleTenantHsmInstanceProposalRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Class CreateSingleTenantHsmInstanceProposalRequest (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class CreateSingleTenantHsmInstanceProposalRequest : IMessage<CreateSingleTenantHsmInstanceProposalRequest>, IEquatable<CreateSingleTenantHsmInstanceProposalRequest>, IDeepCloneable<CreateSingleTenantHsmInstanceProposalRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Key Management Service v1 API class CreateSingleTenantHsmInstanceProposalRequest.

Request message for [HsmManagement.CreateSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstanceProposal].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateSingleTenantHsmInstanceProposalRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateSingleTenantHsmInstanceProposalRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateSingleTenantHsmInstanceProposalRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateSingleTenantHsmInstanceProposalRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Constructors 

### CreateSingleTenantHsmInstanceProposalRequest()
    
    
    public CreateSingleTenantHsmInstanceProposalRequest()

### CreateSingleTenantHsmInstanceProposalRequest(CreateSingleTenantHsmInstanceProposalRequest)
    
    
    public CreateSingleTenantHsmInstanceProposalRequest(CreateSingleTenantHsmInstanceProposalRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateSingleTenantHsmInstanceProposalRequest)`  
  
  
## Properties 

### Parent
    
    
    public string Parent { get; set; }

Required. The [name][google.cloud.kms.v1.SingleTenantHsmInstance.name] of the [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance] associated with the [SingleTenantHsmInstanceProposals][google.cloud.kms.v1.SingleTenantHsmInstanceProposal].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsSingleTenantHsmInstanceName
    
    
    public SingleTenantHsmInstanceName ParentAsSingleTenantHsmInstanceName { get; set; }

[SingleTenantHsmInstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateSingleTenantHsmInstanceProposalRequest#Google_Cloud_Kms_V1_CreateSingleTenantHsmInstanceProposalRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SingleTenantHsmInstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceName)` |   
  
### SingleTenantHsmInstanceProposal
    
    
    public SingleTenantHsmInstanceProposal SingleTenantHsmInstanceProposal { get; set; }

Required. The [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal] to create.

**Property Value**  
---  
**Type** | **Description**  
`[SingleTenantHsmInstanceProposal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal)` |   
  
### SingleTenantHsmInstanceProposalId
    
    
    public string SingleTenantHsmInstanceProposalId { get; set; }

Optional. It must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
