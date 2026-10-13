---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client
title: Cloud Phishing Protection v1beta1 API - Class PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:24.232285+00:00
---

# Cloud Phishing Protection v1beta1 API - Class PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Phishing Protection v1beta1 API - Class PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/2.0.0-beta05/Google.Cloud.PhishingProtection.V1Beta1.PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client)
  * [ 1.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/1.0.0-beta05/Google.Cloud.PhishingProtection.V1Beta1.PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client)


    
    
    public class PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client : ClientBase<PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client>

Reference documentation and code samples for the Cloud Phishing Protection v1beta1 API class PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client.

Client for PhishingProtectionServiceV1Beta1

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[PhishingProtectionServiceV1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.PhishingProtectionServiceV1Beta1)[PhishingProtectionServiceV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client) > PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client

## Inherited Members

[ClientBase<PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.PhishingProtection.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1)

## Assembly

Google.Cloud.PhishingProtection.V1Beta1.dll

## Constructors 

### PhishingProtectionServiceV1Beta1Client()
    
    
    protected PhishingProtectionServiceV1Beta1Client()

Protected parameterless constructor to allow creation of test doubles.

### PhishingProtectionServiceV1Beta1Client(CallInvoker)
    
    
    public PhishingProtectionServiceV1Beta1Client(CallInvoker callInvoker)

Creates a new client for PhishingProtectionServiceV1Beta1 that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### PhishingProtectionServiceV1Beta1Client(ChannelBase)
    
    
    public PhishingProtectionServiceV1Beta1Client(ChannelBase channel)

Creates a new client for PhishingProtectionServiceV1Beta1

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### PhishingProtectionServiceV1Beta1Client(ClientBaseConfiguration)
    
    
    protected PhishingProtectionServiceV1Beta1Client(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### NewInstance(ClientBaseConfiguration)
    
    
    protected override PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PhishingProtectionServiceV1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.PhishingProtectionServiceV1Beta1)[PhishingProtectionServiceV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.PhishingProtection.V1Beta1.PhishingProtectionServiceV1Beta1.PhishingProtectionServiceV1Beta1Client>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### ReportPhishing(ReportPhishingRequest, CallOptions)
    
    
    public virtual ReportPhishingResponse ReportPhishing(ReportPhishingRequest request, CallOptions options)

Reports a URI suspected of containing phishing content to be reviewed. Once the report review is complete, its result can be found in the Cloud Security Command Center findings dashboard for Phishing Protection. If the result verifies the existence of malicious phishing content, the site will be added the to [Google's Social Engineering lists](https://support.google.com/webmasters/answer/6350487/) in order to protect users that could get exposed to this threat in the future.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReportPhishingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ReportPhishingResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingResponse)` | The response received from the server.  
  
### ReportPhishing(ReportPhishingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ReportPhishingResponse ReportPhishing(ReportPhishingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Reports a URI suspected of containing phishing content to be reviewed. Once the report review is complete, its result can be found in the Cloud Security Command Center findings dashboard for Phishing Protection. If the result verifies the existence of malicious phishing content, the site will be added the to [Google's Social Engineering lists](https://support.google.com/webmasters/answer/6350487/) in order to protect users that could get exposed to this threat in the future.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReportPhishingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[ReportPhishingResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingResponse)` | The response received from the server.  
  
### ReportPhishingAsync(ReportPhishingRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ReportPhishingResponse> ReportPhishingAsync(ReportPhishingRequest request, CallOptions options)

Reports a URI suspected of containing phishing content to be reviewed. Once the report review is complete, its result can be found in the Cloud Security Command Center findings dashboard for Phishing Protection. If the result verifies the existence of malicious phishing content, the site will be added the to [Google's Social Engineering lists](https://support.google.com/webmasters/answer/6350487/) in order to protect users that could get exposed to this threat in the future.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReportPhishingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReportPhishingResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingResponse)` | The call object.  
  
### ReportPhishingAsync(ReportPhishingRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ReportPhishingResponse> ReportPhishingAsync(ReportPhishingRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Reports a URI suspected of containing phishing content to be reviewed. Once the report review is complete, its result can be found in the Cloud Security Command Center findings dashboard for Phishing Protection. If the result verifies the existence of malicious phishing content, the site will be added the to [Google's Social Engineering lists](https://support.google.com/webmasters/answer/6350487/) in order to protect users that could get exposed to this threat in the future.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReportPhishingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingRequest)`  
The request to send to the server.  
`headers` | `[Metadata](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Metadata.html)`  
The initial metadata to send with the call. This parameter is optional.  
`deadline` | `System.DateTime`  
An optional deadline for the call. The call will be cancelled if deadline is hit.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
An optional token for canceling the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ReportPhishingResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingResponse)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
