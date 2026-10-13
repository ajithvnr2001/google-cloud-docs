---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesGrpc.NetworkServicesFutureStub
title: Class NetworkServicesGrpc.NetworkServicesFutureStub (0.55.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:18.199363+00:00
---

# Class NetworkServicesGrpc.NetworkServicesFutureStub (0.55.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesGrpc.NetworkServicesFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NetworkServicesGrpc.NetworkServicesFutureStub (0.55.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.55.0 (latest)  0.51.0  0.50.0  0.49.0  0.47.0  0.44.0  0.43.0  0.41.0  0.39.0  0.38.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class NetworkServicesGrpc.NetworkServicesFutureStub extends AbstractFutureStub<NetworkServicesGrpc.NetworkServicesFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service NetworkServices.

Service describing handlers for resources.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > NetworkServicesGrpc.NetworkServicesFutureStub

## Inherited Members

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected NetworkServicesGrpc.NetworkServicesFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesGrpc.NetworkServicesFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesGrpc.NetworkServicesFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createAgentGateway(CreateAgentGatewayRequest request)
    
    
    public ListenableFuture<Operation> createAgentGateway(CreateAgentGatewayRequest request)

Creates a new AgentGateway in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateAgentGatewayRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEndpointPolicy(CreateEndpointPolicyRequest request)
    
    
    public ListenableFuture<Operation> createEndpointPolicy(CreateEndpointPolicyRequest request)

Creates a new EndpointPolicy in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateEndpointPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGateway(CreateGatewayRequest request)
    
    
    public ListenableFuture<Operation> createGateway(CreateGatewayRequest request)

Creates a new Gateway in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateGatewayRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGrpcRoute(CreateGrpcRouteRequest request)
    
    
    public ListenableFuture<Operation> createGrpcRoute(CreateGrpcRouteRequest request)

Creates a new GrpcRoute in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateGrpcRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createHttpRoute(CreateHttpRouteRequest request)
    
    
    public ListenableFuture<Operation> createHttpRoute(CreateHttpRouteRequest request)

Creates a new HttpRoute in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateHttpRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createMesh(CreateMeshRequest request)
    
    
    public ListenableFuture<Operation> createMesh(CreateMeshRequest request)

Creates a new Mesh in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateMeshRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createServiceBinding(CreateServiceBindingRequest request)
    
    
    public ListenableFuture<Operation> createServiceBinding(CreateServiceBindingRequest request)

Creates a new ServiceBinding in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateServiceBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createServiceLbPolicy(CreateServiceLbPolicyRequest request)
    
    
    public ListenableFuture<Operation> createServiceLbPolicy(CreateServiceLbPolicyRequest request)

Creates a new ServiceLbPolicy in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateServiceLbPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createTcpRoute(CreateTcpRouteRequest request)
    
    
    public ListenableFuture<Operation> createTcpRoute(CreateTcpRouteRequest request)

Creates a new TcpRoute in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateTcpRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createTlsRoute(CreateTlsRouteRequest request)
    
    
    public ListenableFuture<Operation> createTlsRoute(CreateTlsRouteRequest request)

Creates a new TlsRoute in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateTlsRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createWasmPlugin(CreateWasmPluginRequest request)
    
    
    public ListenableFuture<Operation> createWasmPlugin(CreateWasmPluginRequest request)

Creates a new `WasmPlugin` resource in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateWasmPluginRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createWasmPluginVersion(CreateWasmPluginVersionRequest request)
    
    
    public ListenableFuture<Operation> createWasmPluginVersion(CreateWasmPluginVersionRequest request)

Creates a new `WasmPluginVersion` resource in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateWasmPluginVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAgentGateway(DeleteAgentGatewayRequest request)
    
    
    public ListenableFuture<Operation> deleteAgentGateway(DeleteAgentGatewayRequest request)

Deletes a single AgentGateway.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteAgentGatewayRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteEndpointPolicy(DeleteEndpointPolicyRequest request)
    
    
    public ListenableFuture<Operation> deleteEndpointPolicy(DeleteEndpointPolicyRequest request)

Deletes a single EndpointPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteEndpointPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGateway(DeleteGatewayRequest request)
    
    
    public ListenableFuture<Operation> deleteGateway(DeleteGatewayRequest request)

Deletes a single Gateway.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteGatewayRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGrpcRoute(DeleteGrpcRouteRequest request)
    
    
    public ListenableFuture<Operation> deleteGrpcRoute(DeleteGrpcRouteRequest request)

Deletes a single GrpcRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteGrpcRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteHttpRoute(DeleteHttpRouteRequest request)
    
    
    public ListenableFuture<Operation> deleteHttpRoute(DeleteHttpRouteRequest request)

Deletes a single HttpRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteHttpRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteMesh(DeleteMeshRequest request)
    
    
    public ListenableFuture<Operation> deleteMesh(DeleteMeshRequest request)

Deletes a single Mesh.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteMeshRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteServiceBinding(DeleteServiceBindingRequest request)
    
    
    public ListenableFuture<Operation> deleteServiceBinding(DeleteServiceBindingRequest request)

Deletes a single ServiceBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteServiceBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteServiceLbPolicy(DeleteServiceLbPolicyRequest request)
    
    
    public ListenableFuture<Operation> deleteServiceLbPolicy(DeleteServiceLbPolicyRequest request)

Deletes a single ServiceLbPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteServiceLbPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTcpRoute(DeleteTcpRouteRequest request)
    
    
    public ListenableFuture<Operation> deleteTcpRoute(DeleteTcpRouteRequest request)

Deletes a single TcpRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteTcpRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTlsRoute(DeleteTlsRouteRequest request)
    
    
    public ListenableFuture<Operation> deleteTlsRoute(DeleteTlsRouteRequest request)

Deletes a single TlsRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteTlsRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteWasmPlugin(DeleteWasmPluginRequest request)
    
    
    public ListenableFuture<Operation> deleteWasmPlugin(DeleteWasmPluginRequest request)

Deletes the specified `WasmPlugin` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteWasmPluginRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteWasmPluginVersion(DeleteWasmPluginVersionRequest request)
    
    
    public ListenableFuture<Operation> deleteWasmPluginVersion(DeleteWasmPluginVersionRequest request)

Deletes the specified `WasmPluginVersion` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteWasmPluginVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getAgentGateway(GetAgentGatewayRequest request)
    
    
    public ListenableFuture<AgentGateway> getAgentGateway(GetAgentGatewayRequest request)

Gets details of a single AgentGateway.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetAgentGatewayRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway)>` |   
  
### getEndpointPolicy(GetEndpointPolicyRequest request)
    
    
    public ListenableFuture<EndpointPolicy> getEndpointPolicy(GetEndpointPolicyRequest request)

Gets details of a single EndpointPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetEndpointPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy)>` |   
  
### getGateway(GetGatewayRequest request)
    
    
    public ListenableFuture<Gateway> getGateway(GetGatewayRequest request)

Gets details of a single Gateway.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGatewayRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway)>` |   
  
### getGatewayRouteView(GetGatewayRouteViewRequest request)
    
    
    public ListenableFuture<GatewayRouteView> getGatewayRouteView(GetGatewayRouteViewRequest request)

Get a single RouteView of a Gateway.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGatewayRouteViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGatewayRouteViewRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[GatewayRouteView](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GatewayRouteView)>` |   
  
### getGrpcRoute(GetGrpcRouteRequest request)
    
    
    public ListenableFuture<GrpcRoute> getGrpcRoute(GetGrpcRouteRequest request)

Gets details of a single GrpcRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGrpcRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute)>` |   
  
### getHttpRoute(GetHttpRouteRequest request)
    
    
    public ListenableFuture<HttpRoute> getHttpRoute(GetHttpRouteRequest request)

Gets details of a single HttpRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetHttpRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute)>` |   
  
### getMesh(GetMeshRequest request)
    
    
    public ListenableFuture<Mesh> getMesh(GetMeshRequest request)

Gets details of a single Mesh.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetMeshRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh)>` |   
  
### getMeshRouteView(GetMeshRouteViewRequest request)
    
    
    public ListenableFuture<MeshRouteView> getMeshRouteView(GetMeshRouteViewRequest request)

Get a single RouteView of a Mesh.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMeshRouteViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetMeshRouteViewRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[MeshRouteView](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.MeshRouteView)>` |   
  
### getServiceBinding(GetServiceBindingRequest request)
    
    
    public ListenableFuture<ServiceBinding> getServiceBinding(GetServiceBindingRequest request)

Gets details of a single ServiceBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetServiceBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding)>` |   
  
### getServiceLbPolicy(GetServiceLbPolicyRequest request)
    
    
    public ListenableFuture<ServiceLbPolicy> getServiceLbPolicy(GetServiceLbPolicyRequest request)

Gets details of a single ServiceLbPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetServiceLbPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy)>` |   
  
### getTcpRoute(GetTcpRouteRequest request)
    
    
    public ListenableFuture<TcpRoute> getTcpRoute(GetTcpRouteRequest request)

Gets details of a single TcpRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetTcpRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute)>` |   
  
### getTlsRoute(GetTlsRouteRequest request)
    
    
    public ListenableFuture<TlsRoute> getTlsRoute(GetTlsRouteRequest request)

Gets details of a single TlsRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetTlsRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute)>` |   
  
### getWasmPlugin(GetWasmPluginRequest request)
    
    
    public ListenableFuture<WasmPlugin> getWasmPlugin(GetWasmPluginRequest request)

Gets details of the specified `WasmPlugin` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetWasmPluginRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin)>` |   
  
### getWasmPluginVersion(GetWasmPluginVersionRequest request)
    
    
    public ListenableFuture<WasmPluginVersion> getWasmPluginVersion(GetWasmPluginVersionRequest request)

Gets details of the specified `WasmPluginVersion` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetWasmPluginVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[WasmPluginVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginVersion)>` |   
  
### listAgentGateways(ListAgentGatewaysRequest request)
    
    
    public ListenableFuture<ListAgentGatewaysResponse> listAgentGateways(ListAgentGatewaysRequest request)

Lists AgentGateways in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAgentGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListAgentGatewaysRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListAgentGatewaysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListAgentGatewaysResponse)>` |   
  
### listEndpointPolicies(ListEndpointPoliciesRequest request)
    
    
    public ListenableFuture<ListEndpointPoliciesResponse> listEndpointPolicies(ListEndpointPoliciesRequest request)

Lists EndpointPolicies in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEndpointPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListEndpointPoliciesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListEndpointPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListEndpointPoliciesResponse)>` |   
  
### listGatewayRouteViews(ListGatewayRouteViewsRequest request)
    
    
    public ListenableFuture<ListGatewayRouteViewsResponse> listGatewayRouteViews(ListGatewayRouteViewsRequest request)

Lists RouteViews

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGatewayRouteViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewayRouteViewsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListGatewayRouteViewsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewayRouteViewsResponse)>` |   
  
### listGateways(ListGatewaysRequest request)
    
    
    public ListenableFuture<ListGatewaysResponse> listGateways(ListGatewaysRequest request)

Lists Gateways in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewaysRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListGatewaysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewaysResponse)>` |   
  
### listGrpcRoutes(ListGrpcRoutesRequest request)
    
    
    public ListenableFuture<ListGrpcRoutesResponse> listGrpcRoutes(ListGrpcRoutesRequest request)

Lists GrpcRoutes in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGrpcRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGrpcRoutesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListGrpcRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGrpcRoutesResponse)>` |   
  
### listHttpRoutes(ListHttpRoutesRequest request)
    
    
    public ListenableFuture<ListHttpRoutesResponse> listHttpRoutes(ListHttpRoutesRequest request)

Lists HttpRoute in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHttpRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListHttpRoutesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListHttpRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListHttpRoutesResponse)>` |   
  
### listMeshRouteViews(ListMeshRouteViewsRequest request)
    
    
    public ListenableFuture<ListMeshRouteViewsResponse> listMeshRouteViews(ListMeshRouteViewsRequest request)

Lists RouteViews

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMeshRouteViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshRouteViewsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListMeshRouteViewsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshRouteViewsResponse)>` |   
  
### listMeshes(ListMeshesRequest request)
    
    
    public ListenableFuture<ListMeshesResponse> listMeshes(ListMeshesRequest request)

Lists Meshes in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMeshesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListMeshesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshesResponse)>` |   
  
### listServiceBindings(ListServiceBindingsRequest request)
    
    
    public ListenableFuture<ListServiceBindingsResponse> listServiceBindings(ListServiceBindingsRequest request)

Lists ServiceBinding in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServiceBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceBindingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListServiceBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceBindingsResponse)>` |   
  
### listServiceLbPolicies(ListServiceLbPoliciesRequest request)
    
    
    public ListenableFuture<ListServiceLbPoliciesResponse> listServiceLbPolicies(ListServiceLbPoliciesRequest request)

Lists ServiceLbPolicies in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServiceLbPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceLbPoliciesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListServiceLbPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceLbPoliciesResponse)>` |   
  
### listTcpRoutes(ListTcpRoutesRequest request)
    
    
    public ListenableFuture<ListTcpRoutesResponse> listTcpRoutes(ListTcpRoutesRequest request)

Lists TcpRoute in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTcpRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTcpRoutesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListTcpRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTcpRoutesResponse)>` |   
  
### listTlsRoutes(ListTlsRoutesRequest request)
    
    
    public ListenableFuture<ListTlsRoutesResponse> listTlsRoutes(ListTlsRoutesRequest request)

Lists TlsRoute in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTlsRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTlsRoutesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListTlsRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTlsRoutesResponse)>` |   
  
### listWasmPluginVersions(ListWasmPluginVersionsRequest request)
    
    
    public ListenableFuture<ListWasmPluginVersionsResponse> listWasmPluginVersions(ListWasmPluginVersionsRequest request)

Lists `WasmPluginVersion` resources in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListWasmPluginVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginVersionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListWasmPluginVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginVersionsResponse)>` |   
  
### listWasmPlugins(ListWasmPluginsRequest request)
    
    
    public ListenableFuture<ListWasmPluginsResponse> listWasmPlugins(ListWasmPluginsRequest request)

Lists `WasmPlugin` resources in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListWasmPluginsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListWasmPluginsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginsResponse)>` |   
  
### updateAgentGateway(UpdateAgentGatewayRequest request)
    
    
    public ListenableFuture<Operation> updateAgentGateway(UpdateAgentGatewayRequest request)

Updates the parameters of a single AgentGateway.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateAgentGatewayRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateEndpointPolicy(UpdateEndpointPolicyRequest request)
    
    
    public ListenableFuture<Operation> updateEndpointPolicy(UpdateEndpointPolicyRequest request)

Updates the parameters of a single EndpointPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateEndpointPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateGateway(UpdateGatewayRequest request)
    
    
    public ListenableFuture<Operation> updateGateway(UpdateGatewayRequest request)

Updates the parameters of a single Gateway.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateGatewayRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateGrpcRoute(UpdateGrpcRouteRequest request)
    
    
    public ListenableFuture<Operation> updateGrpcRoute(UpdateGrpcRouteRequest request)

Updates the parameters of a single GrpcRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateGrpcRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateHttpRoute(UpdateHttpRouteRequest request)
    
    
    public ListenableFuture<Operation> updateHttpRoute(UpdateHttpRouteRequest request)

Updates the parameters of a single HttpRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateHttpRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateMesh(UpdateMeshRequest request)
    
    
    public ListenableFuture<Operation> updateMesh(UpdateMeshRequest request)

Updates the parameters of a single Mesh.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateMeshRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateServiceBinding(UpdateServiceBindingRequest request)
    
    
    public ListenableFuture<Operation> updateServiceBinding(UpdateServiceBindingRequest request)

Updates the parameters of a single ServiceBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateServiceBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateServiceLbPolicy(UpdateServiceLbPolicyRequest request)
    
    
    public ListenableFuture<Operation> updateServiceLbPolicy(UpdateServiceLbPolicyRequest request)

Updates the parameters of a single ServiceLbPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateServiceLbPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateTcpRoute(UpdateTcpRouteRequest request)
    
    
    public ListenableFuture<Operation> updateTcpRoute(UpdateTcpRouteRequest request)

Updates the parameters of a single TcpRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateTcpRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateTlsRoute(UpdateTlsRouteRequest request)
    
    
    public ListenableFuture<Operation> updateTlsRoute(UpdateTlsRouteRequest request)

Updates the parameters of a single TlsRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateTlsRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateWasmPlugin(UpdateWasmPluginRequest request)
    
    
    public ListenableFuture<Operation> updateWasmPlugin(UpdateWasmPluginRequest request)

Updates the parameters of the specified `WasmPlugin` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateWasmPluginRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
