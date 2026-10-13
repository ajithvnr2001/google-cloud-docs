---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.QuorumParameters
title: Google Cloud Key Management Service v1 API - Class SingleTenantHsmInstanceProposal.Types.QuorumParameters (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:49:22.386091+00:00
---

# Google Cloud Key Management Service v1 API - Class SingleTenantHsmInstanceProposal.Types.QuorumParameters (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.QuorumParameters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Class SingleTenantHsmInstanceProposal.Types.QuorumParameters (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class SingleTenantHsmInstanceProposal.Types.QuorumParameters : IMessage<SingleTenantHsmInstanceProposal.Types.QuorumParameters>, IEquatable<SingleTenantHsmInstanceProposal.Types.QuorumParameters>, IDeepCloneable<SingleTenantHsmInstanceProposal.Types.QuorumParameters>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Key Management Service v1 API class SingleTenantHsmInstanceProposal.Types.QuorumParameters.

Parameters of quorum approval for the [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SingleTenantHsmInstanceProposal.Types.QuorumParameters

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SingleTenantHsmInstanceProposal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types)[QuorumParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.QuorumParameters), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SingleTenantHsmInstanceProposal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types)[QuorumParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.QuorumParameters), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SingleTenantHsmInstanceProposal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types)[QuorumParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.QuorumParameters), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Constructors 

### QuorumParameters()
    
    
    public QuorumParameters()

### QuorumParameters(QuorumParameters)
    
    
    public QuorumParameters(SingleTenantHsmInstanceProposal.Types.QuorumParameters other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SingleTenantHsmInstanceProposal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types)[QuorumParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.QuorumParameters)`  
  
  
## Properties 

### ApprovedTwoFactorPublicKeyPems
    
    
    public RepeatedField<string> ApprovedTwoFactorPublicKeyPems { get; }

Output only. The public keys associated with the 2FA keys that have already approved the [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal] by signing the challenge.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Challenges
    
    
    public RepeatedField<Challenge> Challenges { get; }

Output only. The challenges to be signed by 2FA keys for quorum auth. M of N of these challenges are required to be signed to approve the operation.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.Challenge)` |   
  
### RequiredApproverCount
    
    
    public int RequiredApproverCount { get; set; }

Output only. The required numbers of approvers. This is the M value used for M of N quorum auth. It is less than the number of public keys.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
