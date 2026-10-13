---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkFirewallPolicies.NetworkFirewallPoliciesClient
title: Compute Engine v1 API - Class NetworkFirewallPolicies.NetworkFirewallPoliciesClient (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:43.637354+00:00
---

# Compute Engine v1 API - Class NetworkFirewallPolicies.NetworkFirewallPoliciesClient (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkFirewallPolicies.NetworkFirewallPoliciesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class NetworkFirewallPolicies.NetworkFirewallPoliciesClient (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public class NetworkFirewallPolicies.NetworkFirewallPoliciesClient : ClientBase<NetworkFirewallPolicies.NetworkFirewallPoliciesClient>

Reference documentation and code samples for the Compute Engine v1 API class NetworkFirewallPolicies.NetworkFirewallPoliciesClient.

Client for NetworkFirewallPolicies

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html) > [ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html)[NetworkFirewallPolicies](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkFirewallPolicies)[NetworkFirewallPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkFirewallPolicies.NetworkFirewallPoliciesClient) > NetworkFirewallPolicies.NetworkFirewallPoliciesClient

## Inherited Members

[ClientBase<NetworkFirewallPolicies.NetworkFirewallPoliciesClient>.WithHost(string)](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase-1.html#Grpc_Core_ClientBase_1_WithHost_System_String_)

[ClientBase.CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html#Grpc_Core_ClientBase_CallInvoker)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### NetworkFirewallPoliciesClient()
    
    
    protected NetworkFirewallPoliciesClient()

Protected parameterless constructor to allow creation of test doubles.

### NetworkFirewallPoliciesClient(CallInvoker)
    
    
    public NetworkFirewallPoliciesClient(CallInvoker callInvoker)

Creates a new client for NetworkFirewallPolicies that uses a custom `CallInvoker`.

**Parameter**  
---  
**Name** | **Description**  
`callInvoker` | `[CallInvoker](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallInvoker.html)`  
The callInvoker to use to make remote calls.  
  
### NetworkFirewallPoliciesClient(ChannelBase)
    
    
    public NetworkFirewallPoliciesClient(ChannelBase channel)

Creates a new client for NetworkFirewallPolicies

**Parameter**  
---  
**Name** | **Description**  
`channel` | `[ChannelBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ChannelBase.html)`  
The channel to use to make remote calls.  
  
### NetworkFirewallPoliciesClient(ClientBaseConfiguration)
    
    
    protected NetworkFirewallPoliciesClient(ClientBase.ClientBaseConfiguration configuration)

Protected constructor to allow creation of configured clients.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
The client configuration.  
  
## Methods 

### AddAssociation(AddAssociationNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual Operation AddAssociation(AddAssociationNetworkFirewallPolicyRequest request, CallOptions options)

Inserts an association for the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddAssociationNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### AddAssociation(AddAssociationNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation AddAssociation(AddAssociationNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Inserts an association for the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddAssociationNetworkFirewallPolicyRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### AddAssociationAsync(AddAssociationNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> AddAssociationAsync(AddAssociationNetworkFirewallPolicyRequest request, CallOptions options)

Inserts an association for the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddAssociationNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### AddAssociationAsync(AddAssociationNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> AddAssociationAsync(AddAssociationNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Inserts an association for the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddAssociationNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### AddPacketMirroringRule(AddPacketMirroringRuleNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual Operation AddPacketMirroringRule(AddPacketMirroringRuleNetworkFirewallPolicyRequest request, CallOptions options)

Inserts a packet mirroring rule into a firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddPacketMirroringRuleNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### AddPacketMirroringRule(AddPacketMirroringRuleNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation AddPacketMirroringRule(AddPacketMirroringRuleNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Inserts a packet mirroring rule into a firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddPacketMirroringRuleNetworkFirewallPolicyRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### AddPacketMirroringRuleAsync(AddPacketMirroringRuleNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> AddPacketMirroringRuleAsync(AddPacketMirroringRuleNetworkFirewallPolicyRequest request, CallOptions options)

Inserts a packet mirroring rule into a firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddPacketMirroringRuleNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### AddPacketMirroringRuleAsync(AddPacketMirroringRuleNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> AddPacketMirroringRuleAsync(AddPacketMirroringRuleNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Inserts a packet mirroring rule into a firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddPacketMirroringRuleNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### AddRule(AddRuleNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual Operation AddRule(AddRuleNetworkFirewallPolicyRequest request, CallOptions options)

Inserts a rule into a firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddRuleNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### AddRule(AddRuleNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation AddRule(AddRuleNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Inserts a rule into a firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddRuleNetworkFirewallPolicyRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### AddRuleAsync(AddRuleNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> AddRuleAsync(AddRuleNetworkFirewallPolicyRequest request, CallOptions options)

Inserts a rule into a firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddRuleNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### AddRuleAsync(AddRuleNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> AddRuleAsync(AddRuleNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Inserts a rule into a firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddRuleNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### AggregatedList(AggregatedListNetworkFirewallPoliciesRequest, CallOptions)
    
    
    public virtual NetworkFirewallPolicyAggregatedList AggregatedList(AggregatedListNetworkFirewallPoliciesRequest request, CallOptions options)

Retrieves an aggregated list of network firewall policies, listing network firewall policies from all applicable scopes (global and regional) and grouping the results per scope.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregatedListNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AggregatedListNetworkFirewallPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkFirewallPolicyAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkFirewallPolicyAggregatedList)` | The response received from the server.  
  
### AggregatedList(AggregatedListNetworkFirewallPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual NetworkFirewallPolicyAggregatedList AggregatedList(AggregatedListNetworkFirewallPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves an aggregated list of network firewall policies, listing network firewall policies from all applicable scopes (global and regional) and grouping the results per scope.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregatedListNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AggregatedListNetworkFirewallPoliciesRequest)`  
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
`[NetworkFirewallPolicyAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkFirewallPolicyAggregatedList)` | The response received from the server.  
  
### AggregatedListAsync(AggregatedListNetworkFirewallPoliciesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<NetworkFirewallPolicyAggregatedList> AggregatedListAsync(AggregatedListNetworkFirewallPoliciesRequest request, CallOptions options)

Retrieves an aggregated list of network firewall policies, listing network firewall policies from all applicable scopes (global and regional) and grouping the results per scope.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregatedListNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AggregatedListNetworkFirewallPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[NetworkFirewallPolicyAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkFirewallPolicyAggregatedList)` | The call object.  
  
### AggregatedListAsync(AggregatedListNetworkFirewallPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<NetworkFirewallPolicyAggregatedList> AggregatedListAsync(AggregatedListNetworkFirewallPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Retrieves an aggregated list of network firewall policies, listing network firewall policies from all applicable scopes (global and regional) and grouping the results per scope.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregatedListNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AggregatedListNetworkFirewallPoliciesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[NetworkFirewallPolicyAggregatedList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkFirewallPolicyAggregatedList)` | The call object.  
  
### CloneRules(CloneRulesNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual Operation CloneRules(CloneRulesNetworkFirewallPolicyRequest request, CallOptions options)

Copies rules to the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CloneRulesNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CloneRulesNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### CloneRules(CloneRulesNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation CloneRules(CloneRulesNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Copies rules to the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CloneRulesNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CloneRulesNetworkFirewallPolicyRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### CloneRulesAsync(CloneRulesNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> CloneRulesAsync(CloneRulesNetworkFirewallPolicyRequest request, CallOptions options)

Copies rules to the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CloneRulesNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CloneRulesNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### CloneRulesAsync(CloneRulesNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> CloneRulesAsync(CloneRulesNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Copies rules to the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CloneRulesNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CloneRulesNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### CreateOperationsClientForGlobalOperations()
    
    
    public virtual Operations.OperationsClient CreateOperationsClientForGlobalOperations()

Creates a new instance of [Operations.OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html) using the same call invoker as this client, delegating to GlobalOperations.

**Returns**  
---  
**Type** | **Description**  
`[Operations](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.html)[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsClient.html)` | A new Operations client for the same target as this client.  
  
### Delete(DeleteNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual Operation Delete(DeleteNetworkFirewallPolicyRequest request, CallOptions options)

Deletes the specified policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### Delete(DeleteNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation Delete(DeleteNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteNetworkFirewallPolicyRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### DeleteAsync(DeleteNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteAsync(DeleteNetworkFirewallPolicyRequest request, CallOptions options)

Deletes the specified policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### DeleteAsync(DeleteNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> DeleteAsync(DeleteNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes the specified policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DeleteNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### Get(GetNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual FirewallPolicy Get(GetNetworkFirewallPolicyRequest request, CallOptions options)

Returns the specified network firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicy)` | The response received from the server.  
  
### Get(GetNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FirewallPolicy Get(GetNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the specified network firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetNetworkFirewallPolicyRequest)`  
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
`[FirewallPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicy)` | The response received from the server.  
  
### GetAssociation(GetAssociationNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual FirewallPolicyAssociation GetAssociation(GetAssociationNetworkFirewallPolicyRequest request, CallOptions options)

Gets an association with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetAssociationNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicyAssociation)` | The response received from the server.  
  
### GetAssociation(GetAssociationNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FirewallPolicyAssociation GetAssociation(GetAssociationNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets an association with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetAssociationNetworkFirewallPolicyRequest)`  
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
`[FirewallPolicyAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicyAssociation)` | The response received from the server.  
  
### GetAssociationAsync(GetAssociationNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FirewallPolicyAssociation> GetAssociationAsync(GetAssociationNetworkFirewallPolicyRequest request, CallOptions options)

Gets an association with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetAssociationNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FirewallPolicyAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicyAssociation)` | The call object.  
  
### GetAssociationAsync(GetAssociationNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FirewallPolicyAssociation> GetAssociationAsync(GetAssociationNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets an association with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetAssociationNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FirewallPolicyAssociation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicyAssociation)` | The call object.  
  
### GetAsync(GetNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FirewallPolicy> GetAsync(GetNetworkFirewallPolicyRequest request, CallOptions options)

Returns the specified network firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FirewallPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicy)` | The call object.  
  
### GetAsync(GetNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FirewallPolicy> GetAsync(GetNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns the specified network firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FirewallPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicy)` | The call object.  
  
### GetIamPolicy(GetIamPolicyNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual Policy GetIamPolicy(GetIamPolicyNetworkFirewallPolicyRequest request, CallOptions options)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetIamPolicyNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The response received from the server.  
  
### GetIamPolicy(GetIamPolicyNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Policy GetIamPolicy(GetIamPolicyNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetIamPolicyNetworkFirewallPolicyRequest)`  
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
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The response received from the server.  
  
### GetIamPolicyAsync(GetIamPolicyNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Policy> GetIamPolicyAsync(GetIamPolicyNetworkFirewallPolicyRequest request, CallOptions options)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetIamPolicyNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The call object.  
  
### GetIamPolicyAsync(GetIamPolicyNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Policy> GetIamPolicyAsync(GetIamPolicyNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetIamPolicyNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The call object.  
  
### GetPacketMirroringRule(GetPacketMirroringRuleNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual FirewallPolicyRule GetPacketMirroringRule(GetPacketMirroringRuleNetworkFirewallPolicyRequest request, CallOptions options)

Gets a packet mirroring rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetPacketMirroringRuleNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicyRule)` | The response received from the server.  
  
### GetPacketMirroringRule(GetPacketMirroringRuleNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FirewallPolicyRule GetPacketMirroringRule(GetPacketMirroringRuleNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a packet mirroring rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetPacketMirroringRuleNetworkFirewallPolicyRequest)`  
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
`[FirewallPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicyRule)` | The response received from the server.  
  
### GetPacketMirroringRuleAsync(GetPacketMirroringRuleNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FirewallPolicyRule> GetPacketMirroringRuleAsync(GetPacketMirroringRuleNetworkFirewallPolicyRequest request, CallOptions options)

Gets a packet mirroring rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetPacketMirroringRuleNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FirewallPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicyRule)` | The call object.  
  
### GetPacketMirroringRuleAsync(GetPacketMirroringRuleNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FirewallPolicyRule> GetPacketMirroringRuleAsync(GetPacketMirroringRuleNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a packet mirroring rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetPacketMirroringRuleNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FirewallPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicyRule)` | The call object.  
  
### GetRule(GetRuleNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual FirewallPolicyRule GetRule(GetRuleNetworkFirewallPolicyRequest request, CallOptions options)

Gets a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetRuleNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicyRule)` | The response received from the server.  
  
### GetRule(GetRuleNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FirewallPolicyRule GetRule(GetRuleNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetRuleNetworkFirewallPolicyRequest)`  
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
`[FirewallPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicyRule)` | The response received from the server.  
  
### GetRuleAsync(GetRuleNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FirewallPolicyRule> GetRuleAsync(GetRuleNetworkFirewallPolicyRequest request, CallOptions options)

Gets a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetRuleNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FirewallPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicyRule)` | The call object.  
  
### GetRuleAsync(GetRuleNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FirewallPolicyRule> GetRuleAsync(GetRuleNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Gets a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GetRuleNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FirewallPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicyRule)` | The call object.  
  
### Insert(InsertNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual Operation Insert(InsertNetworkFirewallPolicyRequest request, CallOptions options)

Creates a new policy in the specified project using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### Insert(InsertNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation Insert(InsertNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new policy in the specified project using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertNetworkFirewallPolicyRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### InsertAsync(InsertNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> InsertAsync(InsertNetworkFirewallPolicyRequest request, CallOptions options)

Creates a new policy in the specified project using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### InsertAsync(InsertNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> InsertAsync(InsertNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Creates a new policy in the specified project using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InsertNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### List(ListNetworkFirewallPoliciesRequest, CallOptions)
    
    
    public virtual FirewallPolicyList List(ListNetworkFirewallPoliciesRequest request, CallOptions options)

Lists all the policies that have been configured for the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListNetworkFirewallPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicyList)` | The response received from the server.  
  
### List(ListNetworkFirewallPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual FirewallPolicyList List(ListNetworkFirewallPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the policies that have been configured for the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListNetworkFirewallPoliciesRequest)`  
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
`[FirewallPolicyList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicyList)` | The response received from the server.  
  
### ListAsync(ListNetworkFirewallPoliciesRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<FirewallPolicyList> ListAsync(ListNetworkFirewallPoliciesRequest request, CallOptions options)

Lists all the policies that have been configured for the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListNetworkFirewallPoliciesRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FirewallPolicyList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicyList)` | The call object.  
  
### ListAsync(ListNetworkFirewallPoliciesRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<FirewallPolicyList> ListAsync(ListNetworkFirewallPoliciesRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Lists all the policies that have been configured for the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ListNetworkFirewallPoliciesRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[FirewallPolicyList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPolicyList)` | The call object.  
  
### NewInstance(ClientBaseConfiguration)
    
    
    protected override NetworkFirewallPolicies.NetworkFirewallPoliciesClient NewInstance(ClientBase.ClientBaseConfiguration configuration)

Creates a new instance of client from given `ClientBaseConfiguration`.

**Parameter**  
---  
**Name** | **Description**  
`configuration` | `[ClientBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.html)[ClientBaseConfiguration](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ClientBase.ClientBaseConfiguration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkFirewallPolicies](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkFirewallPolicies)[NetworkFirewallPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkFirewallPolicies.NetworkFirewallPoliciesClient)` |   
**Overrides**

Grpc.Core.ClientBase<Google.Cloud.Compute.V1.NetworkFirewallPolicies.NetworkFirewallPoliciesClient>.NewInstance(Grpc.Core.ClientBase.ClientBaseConfiguration)

### Patch(PatchNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual Operation Patch(PatchNetworkFirewallPolicyRequest request, CallOptions options)

Patches the specified policy with the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### Patch(PatchNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation Patch(PatchNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Patches the specified policy with the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchNetworkFirewallPolicyRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### PatchAsync(PatchNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> PatchAsync(PatchNetworkFirewallPolicyRequest request, CallOptions options)

Patches the specified policy with the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### PatchAsync(PatchNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> PatchAsync(PatchNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Patches the specified policy with the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### PatchPacketMirroringRule(PatchPacketMirroringRuleNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual Operation PatchPacketMirroringRule(PatchPacketMirroringRuleNetworkFirewallPolicyRequest request, CallOptions options)

Patches a packet mirroring rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchPacketMirroringRuleNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### PatchPacketMirroringRule(PatchPacketMirroringRuleNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation PatchPacketMirroringRule(PatchPacketMirroringRuleNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Patches a packet mirroring rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchPacketMirroringRuleNetworkFirewallPolicyRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### PatchPacketMirroringRuleAsync(PatchPacketMirroringRuleNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> PatchPacketMirroringRuleAsync(PatchPacketMirroringRuleNetworkFirewallPolicyRequest request, CallOptions options)

Patches a packet mirroring rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchPacketMirroringRuleNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### PatchPacketMirroringRuleAsync(PatchPacketMirroringRuleNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> PatchPacketMirroringRuleAsync(PatchPacketMirroringRuleNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Patches a packet mirroring rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchPacketMirroringRuleNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### PatchRule(PatchRuleNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual Operation PatchRule(PatchRuleNetworkFirewallPolicyRequest request, CallOptions options)

Patches a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchRuleNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### PatchRule(PatchRuleNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation PatchRule(PatchRuleNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Patches a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchRuleNetworkFirewallPolicyRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### PatchRuleAsync(PatchRuleNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> PatchRuleAsync(PatchRuleNetworkFirewallPolicyRequest request, CallOptions options)

Patches a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchRuleNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### PatchRuleAsync(PatchRuleNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> PatchRuleAsync(PatchRuleNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Patches a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PatchRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PatchRuleNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### RemoveAssociation(RemoveAssociationNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual Operation RemoveAssociation(RemoveAssociationNetworkFirewallPolicyRequest request, CallOptions options)

Removes an association for the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RemoveAssociationNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### RemoveAssociation(RemoveAssociationNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation RemoveAssociation(RemoveAssociationNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Removes an association for the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RemoveAssociationNetworkFirewallPolicyRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### RemoveAssociationAsync(RemoveAssociationNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> RemoveAssociationAsync(RemoveAssociationNetworkFirewallPolicyRequest request, CallOptions options)

Removes an association for the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RemoveAssociationNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### RemoveAssociationAsync(RemoveAssociationNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> RemoveAssociationAsync(RemoveAssociationNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Removes an association for the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RemoveAssociationNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### RemovePacketMirroringRule(RemovePacketMirroringRuleNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual Operation RemovePacketMirroringRule(RemovePacketMirroringRuleNetworkFirewallPolicyRequest request, CallOptions options)

Deletes a packet mirroring rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemovePacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RemovePacketMirroringRuleNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### RemovePacketMirroringRule(RemovePacketMirroringRuleNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation RemovePacketMirroringRule(RemovePacketMirroringRuleNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a packet mirroring rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemovePacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RemovePacketMirroringRuleNetworkFirewallPolicyRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### RemovePacketMirroringRuleAsync(RemovePacketMirroringRuleNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> RemovePacketMirroringRuleAsync(RemovePacketMirroringRuleNetworkFirewallPolicyRequest request, CallOptions options)

Deletes a packet mirroring rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemovePacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RemovePacketMirroringRuleNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### RemovePacketMirroringRuleAsync(RemovePacketMirroringRuleNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> RemovePacketMirroringRuleAsync(RemovePacketMirroringRuleNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a packet mirroring rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemovePacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RemovePacketMirroringRuleNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### RemoveRule(RemoveRuleNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual Operation RemoveRule(RemoveRuleNetworkFirewallPolicyRequest request, CallOptions options)

Deletes a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RemoveRuleNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### RemoveRule(RemoveRuleNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Operation RemoveRule(RemoveRuleNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RemoveRuleNetworkFirewallPolicyRequest)`  
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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The response received from the server.  
  
### RemoveRuleAsync(RemoveRuleNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Operation> RemoveRuleAsync(RemoveRuleNetworkFirewallPolicyRequest request, CallOptions options)

Deletes a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RemoveRuleNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### RemoveRuleAsync(RemoveRuleNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Operation> RemoveRuleAsync(RemoveRuleNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Deletes a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RemoveRuleNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Operation)` | The call object.  
  
### SetIamPolicy(SetIamPolicyNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual Policy SetIamPolicy(SetIamPolicyNetworkFirewallPolicyRequest request, CallOptions options)

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetIamPolicyNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The response received from the server.  
  
### SetIamPolicy(SetIamPolicyNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual Policy SetIamPolicy(SetIamPolicyNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetIamPolicyNetworkFirewallPolicyRequest)`  
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
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The response received from the server.  
  
### SetIamPolicyAsync(SetIamPolicyNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<Policy> SetIamPolicyAsync(SetIamPolicyNetworkFirewallPolicyRequest request, CallOptions options)

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetIamPolicyNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The call object.  
  
### SetIamPolicyAsync(SetIamPolicyNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<Policy> SetIamPolicyAsync(SetIamPolicyNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SetIamPolicyNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Policy)` | The call object.  
  
### TestIamPermissions(TestIamPermissionsNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual TestPermissionsResponse TestIamPermissions(TestIamPermissionsNetworkFirewallPolicyRequest request, CallOptions options)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | The response received from the server.  
  
### TestIamPermissions(TestIamPermissionsNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual TestPermissionsResponse TestIamPermissions(TestIamPermissionsNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsNetworkFirewallPolicyRequest)`  
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
`[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | The response received from the server.  
  
### TestIamPermissionsAsync(TestIamPermissionsNetworkFirewallPolicyRequest, CallOptions)
    
    
    public virtual AsyncUnaryCall<TestPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsNetworkFirewallPolicyRequest request, CallOptions options)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsNetworkFirewallPolicyRequest)`  
The request to send to the server.  
`options` | `[CallOptions](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.CallOptions.html)`  
The options for the call.  
**Returns**  
---  
**Type** | **Description**  
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | The call object.  
  
### TestIamPermissionsAsync(TestIamPermissionsNetworkFirewallPolicyRequest, Metadata, DateTime?, CancellationToken)
    
    
    public virtual AsyncUnaryCall<TestPermissionsResponse> TestIamPermissionsAsync(TestIamPermissionsNetworkFirewallPolicyRequest request, Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default)

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsNetworkFirewallPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestIamPermissionsNetworkFirewallPolicyRequest)`  
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
`[AsyncUnaryCall](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.AsyncUnaryCall-1.html)[TestPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TestPermissionsResponse)` | The call object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
