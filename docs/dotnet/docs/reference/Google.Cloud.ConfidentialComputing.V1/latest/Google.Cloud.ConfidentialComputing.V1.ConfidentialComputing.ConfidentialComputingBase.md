---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputing.ConfidentialComputingBase
title: Confidential Computing v1 API - Class ConfidentialComputing.ConfidentialComputingBase (1.13.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:56:35.474815+00:00
---

# Confidential Computing v1 API - Class ConfidentialComputing.ConfidentialComputingBase (1.13.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputing.ConfidentialComputingBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Confidential Computing v1 API - Class ConfidentialComputing.ConfidentialComputingBase (1.13.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.13.0 (latest)  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    [BindServiceMethod(typeof(ConfidentialComputing), "BindService")]
    public abstract class ConfidentialComputing.ConfidentialComputingBase

Reference documentation and code samples for the Confidential Computing v1 API class ConfidentialComputing.ConfidentialComputingBase.

Base class for server-side implementations of ConfidentialComputing

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ConfidentialComputing.ConfidentialComputingBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ConfidentialComputing.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1)

## Assembly

Google.Cloud.ConfidentialComputing.V1.dll

## Methods 

### CreateChallenge(CreateChallengeRequest, ServerCallContext)
    
    
    public virtual Task<Challenge> CreateChallenge(CreateChallengeRequest request, ServerCallContext context)

Creates a new Challenge in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateChallengeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.CreateChallengeRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.Challenge)` | The response to send back to the client (wrapped by a task).  
  
### VerifyAttestation(VerifyAttestationRequest, ServerCallContext)
    
    
    public virtual Task<VerifyAttestationResponse> VerifyAttestation(VerifyAttestationRequest request, ServerCallContext context)

Verifies the provided attestation info, returning a signed attestation token.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[VerifyAttestationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyAttestationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VerifyAttestationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyAttestationResponse)` | The response to send back to the client (wrapped by a task).  
  
### VerifyConfidentialGke(VerifyConfidentialGkeRequest, ServerCallContext)
    
    
    public virtual Task<VerifyConfidentialGkeResponse> VerifyConfidentialGke(VerifyConfidentialGkeRequest request, ServerCallContext context)

Verifies the provided Confidential GKE attestation info, returning a signed OIDC token.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[VerifyConfidentialGkeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyConfidentialGkeRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VerifyConfidentialGkeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyConfidentialGkeResponse)` | The response to send back to the client (wrapped by a task).  
  
### VerifyConfidentialSpace(VerifyConfidentialSpaceRequest, ServerCallContext)
    
    
    public virtual Task<VerifyConfidentialSpaceResponse> VerifyConfidentialSpace(VerifyConfidentialSpaceRequest request, ServerCallContext context)

Verifies whether the provided attestation info is valid, returning a signed attestation token if so.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyConfidentialSpaceRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VerifyConfidentialSpaceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyConfidentialSpaceResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
