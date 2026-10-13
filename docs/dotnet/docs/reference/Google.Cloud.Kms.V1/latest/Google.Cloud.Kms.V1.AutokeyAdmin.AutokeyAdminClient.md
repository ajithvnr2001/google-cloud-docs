---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdmin.AutokeyAdminClient
title: Google Cloud Key Management Service v1 API - Class AutokeyAdmin.AutokeyAdminClient (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:48:55.621359+00:00
---

# Google Cloud Key Management Service v1 API - Class AutokeyAdmin.AutokeyAdminClient (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdmin.AutokeyAdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Class AutokeyAdmin.AutokeyAdminClient (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public class AutokeyAdmin.AutokeyAdminClient : ClientBase<AutokeyAdmin.AutokeyAdminClient>

Reference documentation and code samples for the Google Cloud Key Management Service v1 API class AutokeyAdmin.AutokeyAdminClient.

Client for AutokeyAdmin

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[AutokeyAdmin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdmin)[AutokeyAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdmin.AutokeyAdminClient) > AutokeyAdmin.AutokeyAdminClient

## Inherited Members

[ClientBase<AutokeyAdmin.AutokeyAdminClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Constructors 

### AutokeyAdminClient()
    
    
    protected AutokeyAdminClient()

Protected parameterless constructor to allow creation of test doubles.

### AutokeyAdminClient(CallInvoker)
    
    
    public AutokeyAdminClient(CallInvoker callInvoker)

Creates a new client for AutokeyAdmin that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### AutokeyAdminClient(ChannelBase)
    
    
    public AutokeyAdminClient(ChannelBase channel)

Creates a new client for AutokeyAdmin

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### AutokeyAdminClient(ClientBaseConfiguration)
    
    
    protected AutokeyAdminClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### CreateIAMPolicyClient()
    
    
    public virtual IAMPolicy.IAMPolicyClient CreateIAMPolicyClient()

Creates a new instance of [IAMPolicy.IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[IAMPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.html)[IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html)` | A new [IAMPolicy.IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.IAMPolicy.IAMPolicyClient.html) for the same target as this client.  
  
### CreateLocationsClient()
    
    
    public virtual Locations.LocationsClient CreateLocationsClient()

Creates a new instance of [Locations.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) using the same call invoker as this client.

**Returns**  
---  
**Type** | **Description**  
`[Locations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.html)[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html)` | A new [Locations.LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.Locations.LocationsClient.html) for the same target as this client.  
  
### GetAutokeyConfig(GetAutokeyConfigRequest, CallOptions)
    
    
    public virtual AutokeyConfig GetAutokeyConfig(GetAutokeyConfigRequest request, CallOptions options)

Returns the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetAutokeyConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | The response received from the server.  
  
### GetAutokeyConfig(GetAutokeyConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AutokeyConfig GetAutokeyConfig(GetAutokeyConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetAutokeyConfigRequest)`  
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
`[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | The response received from the server.  
  
### GetAutokeyConfigAsync(GetAutokeyConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AutokeyConfig> GetAutokeyConfigAsync(GetAutokeyConfigRequest request, CallOptions options)

Returns the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetAutokeyConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | The call object.  
  
### GetAutokeyConfigAsync(GetAutokeyConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AutokeyConfig> GetAutokeyConfigAsync(GetAutokeyConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetAutokeyConfigRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override AutokeyAdmin.AutokeyAdminClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutokeyAdmin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdmin)[AutokeyAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdmin.AutokeyAdminClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Kms.V1.AutokeyAdmin.AutokeyAdminClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### ShowEffectiveAutokeyConfig(ShowEffectiveAutokeyConfigRequest, CallOptions)
    
    
    public virtual ShowEffectiveAutokeyConfigResponse ShowEffectiveAutokeyConfig(ShowEffectiveAutokeyConfigRequest request, CallOptions options)

Returns the effective Cloud KMS Autokey configuration for a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ShowEffectiveAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigResponse)` | The response received from the server.  
  
### ShowEffectiveAutokeyConfig(ShowEffectiveAutokeyConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual ShowEffectiveAutokeyConfigResponse ShowEffectiveAutokeyConfig(ShowEffectiveAutokeyConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the effective Cloud KMS Autokey configuration for a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ShowEffectiveAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigRequest)`  
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
`[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigResponse)` | The response received from the server.  
  
### ShowEffectiveAutokeyConfigAsync(ShowEffectiveAutokeyConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<ShowEffectiveAutokeyConfigResponse> ShowEffectiveAutokeyConfigAsync(ShowEffectiveAutokeyConfigRequest request, CallOptions options)

Returns the effective Cloud KMS Autokey configuration for a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ShowEffectiveAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigResponse)` | The call object.  
  
### ShowEffectiveAutokeyConfigAsync(ShowEffectiveAutokeyConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<ShowEffectiveAutokeyConfigResponse> ShowEffectiveAutokeyConfigAsync(ShowEffectiveAutokeyConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the effective Cloud KMS Autokey configuration for a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ShowEffectiveAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigResponse)` | The call object.  
  
### UpdateAutokeyConfig(UpdateAutokeyConfigRequest, CallOptions)
    
    
    public virtual AutokeyConfig UpdateAutokeyConfig(UpdateAutokeyConfigRequest request, CallOptions options)

Updates the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or a project. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A [KeyHandle][google.cloud.kms.v1.KeyHandle] creation in the folder's descendant projects will use this configuration to determine where to create the resulting [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.UpdateAutokeyConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | The response received from the server.  
  
### UpdateAutokeyConfig(UpdateAutokeyConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AutokeyConfig UpdateAutokeyConfig(UpdateAutokeyConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or a project. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A [KeyHandle][google.cloud.kms.v1.KeyHandle] creation in the folder's descendant projects will use this configuration to determine where to create the resulting [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.UpdateAutokeyConfigRequest)`  
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
`[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | The response received from the server.  
  
### UpdateAutokeyConfigAsync(UpdateAutokeyConfigRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<AutokeyConfig> UpdateAutokeyConfigAsync(UpdateAutokeyConfigRequest request, CallOptions options)

Updates the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or a project. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A [KeyHandle][google.cloud.kms.v1.KeyHandle] creation in the folder's descendant projects will use this configuration to determine where to create the resulting [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.UpdateAutokeyConfigRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | The call object.  
  
### UpdateAutokeyConfigAsync(UpdateAutokeyConfigRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<AutokeyConfig> UpdateAutokeyConfigAsync(UpdateAutokeyConfigRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Updates the [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] for a folder or a project. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A [KeyHandle][google.cloud.kms.v1.KeyHandle] creation in the folder's descendant projects will use this configuration to determine where to create the resulting [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.UpdateAutokeyConfigRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
