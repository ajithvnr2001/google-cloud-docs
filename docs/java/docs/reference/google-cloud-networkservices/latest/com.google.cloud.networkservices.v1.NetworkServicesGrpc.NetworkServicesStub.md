---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesGrpc.NetworkServicesStub
title: Class NetworkServicesGrpc.NetworkServicesStub (0.55.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:57.224615+00:00
---

# Class NetworkServicesGrpc.NetworkServicesStub (0.55.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesGrpc.NetworkServicesStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NetworkServicesGrpc.NetworkServicesStub (0.55.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.55.0 (latest)  0.51.0  0.50.0  0.49.0  0.47.0  0.44.0  0.43.0  0.41.0  0.39.0  0.38.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class NetworkServicesGrpc.NetworkServicesStub extends AbstractAsyncStub<NetworkServicesGrpc.NetworkServicesStub>

A stub to allow clients to do asynchronous rpc calls to service NetworkServices.

Service describing handlers for resources.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > NetworkServicesGrpc.NetworkServicesStub

## Inherited Members

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected NetworkServicesGrpc.NetworkServicesStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesGrpc.NetworkServicesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesGrpc.NetworkServicesStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createAgentGateway(CreateAgentGatewayRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createAgentGateway(CreateAgentGatewayRequest request, StreamObserver<Operation> responseObserver)

Creates a new AgentGateway in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateAgentGatewayRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createEndpointPolicy(CreateEndpointPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createEndpointPolicy(CreateEndpointPolicyRequest request, StreamObserver<Operation> responseObserver)

Creates a new EndpointPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateEndpointPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createGateway(CreateGatewayRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createGateway(CreateGatewayRequest request, StreamObserver<Operation> responseObserver)

Creates a new Gateway in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateGatewayRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createGrpcRoute(CreateGrpcRouteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createGrpcRoute(CreateGrpcRouteRequest request, StreamObserver<Operation> responseObserver)

Creates a new GrpcRoute in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateGrpcRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createHttpRoute(CreateHttpRouteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createHttpRoute(CreateHttpRouteRequest request, StreamObserver<Operation> responseObserver)

Creates a new HttpRoute in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateHttpRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createMesh(CreateMeshRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createMesh(CreateMeshRequest request, StreamObserver<Operation> responseObserver)

Creates a new Mesh in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateMeshRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createServiceBinding(CreateServiceBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createServiceBinding(CreateServiceBindingRequest request, StreamObserver<Operation> responseObserver)

Creates a new ServiceBinding in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateServiceBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createServiceLbPolicy(CreateServiceLbPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createServiceLbPolicy(CreateServiceLbPolicyRequest request, StreamObserver<Operation> responseObserver)

Creates a new ServiceLbPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateServiceLbPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createTcpRoute(CreateTcpRouteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createTcpRoute(CreateTcpRouteRequest request, StreamObserver<Operation> responseObserver)

Creates a new TcpRoute in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateTcpRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createTlsRoute(CreateTlsRouteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createTlsRoute(CreateTlsRouteRequest request, StreamObserver<Operation> responseObserver)

Creates a new TlsRoute in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateTlsRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createWasmPlugin(CreateWasmPluginRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createWasmPlugin(CreateWasmPluginRequest request, StreamObserver<Operation> responseObserver)

Creates a new `WasmPlugin` resource in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateWasmPluginRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createWasmPluginVersion(CreateWasmPluginVersionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createWasmPluginVersion(CreateWasmPluginVersionRequest request, StreamObserver<Operation> responseObserver)

Creates a new `WasmPluginVersion` resource in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateWasmPluginVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteAgentGateway(DeleteAgentGatewayRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteAgentGateway(DeleteAgentGatewayRequest request, StreamObserver<Operation> responseObserver)

Deletes a single AgentGateway.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteAgentGatewayRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteEndpointPolicy(DeleteEndpointPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteEndpointPolicy(DeleteEndpointPolicyRequest request, StreamObserver<Operation> responseObserver)

Deletes a single EndpointPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteEndpointPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteGateway(DeleteGatewayRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteGateway(DeleteGatewayRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Gateway.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteGatewayRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteGrpcRoute(DeleteGrpcRouteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteGrpcRoute(DeleteGrpcRouteRequest request, StreamObserver<Operation> responseObserver)

Deletes a single GrpcRoute.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteGrpcRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteHttpRoute(DeleteHttpRouteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteHttpRoute(DeleteHttpRouteRequest request, StreamObserver<Operation> responseObserver)

Deletes a single HttpRoute.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteHttpRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteMesh(DeleteMeshRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteMesh(DeleteMeshRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Mesh.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteMeshRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteServiceBinding(DeleteServiceBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteServiceBinding(DeleteServiceBindingRequest request, StreamObserver<Operation> responseObserver)

Deletes a single ServiceBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteServiceBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteServiceLbPolicy(DeleteServiceLbPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteServiceLbPolicy(DeleteServiceLbPolicyRequest request, StreamObserver<Operation> responseObserver)

Deletes a single ServiceLbPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteServiceLbPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteTcpRoute(DeleteTcpRouteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteTcpRoute(DeleteTcpRouteRequest request, StreamObserver<Operation> responseObserver)

Deletes a single TcpRoute.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteTcpRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteTlsRoute(DeleteTlsRouteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteTlsRoute(DeleteTlsRouteRequest request, StreamObserver<Operation> responseObserver)

Deletes a single TlsRoute.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteTlsRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteWasmPlugin(DeleteWasmPluginRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteWasmPlugin(DeleteWasmPluginRequest request, StreamObserver<Operation> responseObserver)

Deletes the specified `WasmPlugin` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteWasmPluginRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteWasmPluginVersion(DeleteWasmPluginVersionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteWasmPluginVersion(DeleteWasmPluginVersionRequest request, StreamObserver<Operation> responseObserver)

Deletes the specified `WasmPluginVersion` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteWasmPluginVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getAgentGateway(GetAgentGatewayRequest request, StreamObserver<AgentGateway> responseObserver)
    
    
    public void getAgentGateway(GetAgentGatewayRequest request, StreamObserver<AgentGateway> responseObserver)

Gets details of a single AgentGateway.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetAgentGatewayRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway)>`  
  
  
### getEndpointPolicy(GetEndpointPolicyRequest request, StreamObserver<EndpointPolicy> responseObserver)
    
    
    public void getEndpointPolicy(GetEndpointPolicyRequest request, StreamObserver<EndpointPolicy> responseObserver)

Gets details of a single EndpointPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetEndpointPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy)>`  
  
  
### getGateway(GetGatewayRequest request, StreamObserver<Gateway> responseObserver)
    
    
    public void getGateway(GetGatewayRequest request, StreamObserver<Gateway> responseObserver)

Gets details of a single Gateway.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGatewayRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway)>`  
  
  
### getGatewayRouteView(GetGatewayRouteViewRequest request, StreamObserver<GatewayRouteView> responseObserver)
    
    
    public void getGatewayRouteView(GetGatewayRouteViewRequest request, StreamObserver<GatewayRouteView> responseObserver)

Get a single RouteView of a Gateway.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGatewayRouteViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGatewayRouteViewRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[GatewayRouteView](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GatewayRouteView)>`  
  
  
### getGrpcRoute(GetGrpcRouteRequest request, StreamObserver<GrpcRoute> responseObserver)
    
    
    public void getGrpcRoute(GetGrpcRouteRequest request, StreamObserver<GrpcRoute> responseObserver)

Gets details of a single GrpcRoute.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGrpcRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute)>`  
  
  
### getHttpRoute(GetHttpRouteRequest request, StreamObserver<HttpRoute> responseObserver)
    
    
    public void getHttpRoute(GetHttpRouteRequest request, StreamObserver<HttpRoute> responseObserver)

Gets details of a single HttpRoute.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetHttpRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute)>`  
  
  
### getMesh(GetMeshRequest request, StreamObserver<Mesh> responseObserver)
    
    
    public void getMesh(GetMeshRequest request, StreamObserver<Mesh> responseObserver)

Gets details of a single Mesh.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetMeshRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh)>`  
  
  
### getMeshRouteView(GetMeshRouteViewRequest request, StreamObserver<MeshRouteView> responseObserver)
    
    
    public void getMeshRouteView(GetMeshRouteViewRequest request, StreamObserver<MeshRouteView> responseObserver)

Get a single RouteView of a Mesh.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMeshRouteViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetMeshRouteViewRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[MeshRouteView](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.MeshRouteView)>`  
  
  
### getServiceBinding(GetServiceBindingRequest request, StreamObserver<ServiceBinding> responseObserver)
    
    
    public void getServiceBinding(GetServiceBindingRequest request, StreamObserver<ServiceBinding> responseObserver)

Gets details of a single ServiceBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetServiceBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding)>`  
  
  
### getServiceLbPolicy(GetServiceLbPolicyRequest request, StreamObserver<ServiceLbPolicy> responseObserver)
    
    
    public void getServiceLbPolicy(GetServiceLbPolicyRequest request, StreamObserver<ServiceLbPolicy> responseObserver)

Gets details of a single ServiceLbPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetServiceLbPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy)>`  
  
  
### getTcpRoute(GetTcpRouteRequest request, StreamObserver<TcpRoute> responseObserver)
    
    
    public void getTcpRoute(GetTcpRouteRequest request, StreamObserver<TcpRoute> responseObserver)

Gets details of a single TcpRoute.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetTcpRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute)>`  
  
  
### getTlsRoute(GetTlsRouteRequest request, StreamObserver<TlsRoute> responseObserver)
    
    
    public void getTlsRoute(GetTlsRouteRequest request, StreamObserver<TlsRoute> responseObserver)

Gets details of a single TlsRoute.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetTlsRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute)>`  
  
  
### getWasmPlugin(GetWasmPluginRequest request, StreamObserver<WasmPlugin> responseObserver)
    
    
    public void getWasmPlugin(GetWasmPluginRequest request, StreamObserver<WasmPlugin> responseObserver)

Gets details of the specified `WasmPlugin` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetWasmPluginRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin)>`  
  
  
### getWasmPluginVersion(GetWasmPluginVersionRequest request, StreamObserver<WasmPluginVersion> responseObserver)
    
    
    public void getWasmPluginVersion(GetWasmPluginVersionRequest request, StreamObserver<WasmPluginVersion> responseObserver)

Gets details of the specified `WasmPluginVersion` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetWasmPluginVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[WasmPluginVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginVersion)>`  
  
  
### listAgentGateways(ListAgentGatewaysRequest request, StreamObserver<ListAgentGatewaysResponse> responseObserver)
    
    
    public void listAgentGateways(ListAgentGatewaysRequest request, StreamObserver<ListAgentGatewaysResponse> responseObserver)

Lists AgentGateways in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAgentGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListAgentGatewaysRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAgentGatewaysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListAgentGatewaysResponse)>`  
  
  
### listEndpointPolicies(ListEndpointPoliciesRequest request, StreamObserver<ListEndpointPoliciesResponse> responseObserver)
    
    
    public void listEndpointPolicies(ListEndpointPoliciesRequest request, StreamObserver<ListEndpointPoliciesResponse> responseObserver)

Lists EndpointPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEndpointPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListEndpointPoliciesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListEndpointPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListEndpointPoliciesResponse)>`  
  
  
### listGatewayRouteViews(ListGatewayRouteViewsRequest request, StreamObserver<ListGatewayRouteViewsResponse> responseObserver)
    
    
    public void listGatewayRouteViews(ListGatewayRouteViewsRequest request, StreamObserver<ListGatewayRouteViewsResponse> responseObserver)

Lists RouteViews

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGatewayRouteViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewayRouteViewsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListGatewayRouteViewsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewayRouteViewsResponse)>`  
  
  
### listGateways(ListGatewaysRequest request, StreamObserver<ListGatewaysResponse> responseObserver)
    
    
    public void listGateways(ListGatewaysRequest request, StreamObserver<ListGatewaysResponse> responseObserver)

Lists Gateways in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewaysRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListGatewaysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewaysResponse)>`  
  
  
### listGrpcRoutes(ListGrpcRoutesRequest request, StreamObserver<ListGrpcRoutesResponse> responseObserver)
    
    
    public void listGrpcRoutes(ListGrpcRoutesRequest request, StreamObserver<ListGrpcRoutesResponse> responseObserver)

Lists GrpcRoutes in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGrpcRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGrpcRoutesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListGrpcRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGrpcRoutesResponse)>`  
  
  
### listHttpRoutes(ListHttpRoutesRequest request, StreamObserver<ListHttpRoutesResponse> responseObserver)
    
    
    public void listHttpRoutes(ListHttpRoutesRequest request, StreamObserver<ListHttpRoutesResponse> responseObserver)

Lists HttpRoute in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListHttpRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListHttpRoutesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListHttpRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListHttpRoutesResponse)>`  
  
  
### listMeshRouteViews(ListMeshRouteViewsRequest request, StreamObserver<ListMeshRouteViewsResponse> responseObserver)
    
    
    public void listMeshRouteViews(ListMeshRouteViewsRequest request, StreamObserver<ListMeshRouteViewsResponse> responseObserver)

Lists RouteViews

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMeshRouteViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshRouteViewsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMeshRouteViewsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshRouteViewsResponse)>`  
  
  
### listMeshes(ListMeshesRequest request, StreamObserver<ListMeshesResponse> responseObserver)
    
    
    public void listMeshes(ListMeshesRequest request, StreamObserver<ListMeshesResponse> responseObserver)

Lists Meshes in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMeshesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMeshesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshesResponse)>`  
  
  
### listServiceBindings(ListServiceBindingsRequest request, StreamObserver<ListServiceBindingsResponse> responseObserver)
    
    
    public void listServiceBindings(ListServiceBindingsRequest request, StreamObserver<ListServiceBindingsResponse> responseObserver)

Lists ServiceBinding in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServiceBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceBindingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListServiceBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceBindingsResponse)>`  
  
  
### listServiceLbPolicies(ListServiceLbPoliciesRequest request, StreamObserver<ListServiceLbPoliciesResponse> responseObserver)
    
    
    public void listServiceLbPolicies(ListServiceLbPoliciesRequest request, StreamObserver<ListServiceLbPoliciesResponse> responseObserver)

Lists ServiceLbPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServiceLbPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceLbPoliciesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListServiceLbPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceLbPoliciesResponse)>`  
  
  
### listTcpRoutes(ListTcpRoutesRequest request, StreamObserver<ListTcpRoutesResponse> responseObserver)
    
    
    public void listTcpRoutes(ListTcpRoutesRequest request, StreamObserver<ListTcpRoutesResponse> responseObserver)

Lists TcpRoute in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTcpRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTcpRoutesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListTcpRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTcpRoutesResponse)>`  
  
  
### listTlsRoutes(ListTlsRoutesRequest request, StreamObserver<ListTlsRoutesResponse> responseObserver)
    
    
    public void listTlsRoutes(ListTlsRoutesRequest request, StreamObserver<ListTlsRoutesResponse> responseObserver)

Lists TlsRoute in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTlsRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTlsRoutesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListTlsRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTlsRoutesResponse)>`  
  
  
### listWasmPluginVersions(ListWasmPluginVersionsRequest request, StreamObserver<ListWasmPluginVersionsResponse> responseObserver)
    
    
    public void listWasmPluginVersions(ListWasmPluginVersionsRequest request, StreamObserver<ListWasmPluginVersionsResponse> responseObserver)

Lists `WasmPluginVersion` resources in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWasmPluginVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginVersionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListWasmPluginVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginVersionsResponse)>`  
  
  
### listWasmPlugins(ListWasmPluginsRequest request, StreamObserver<ListWasmPluginsResponse> responseObserver)
    
    
    public void listWasmPlugins(ListWasmPluginsRequest request, StreamObserver<ListWasmPluginsResponse> responseObserver)

Lists `WasmPlugin` resources in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWasmPluginsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListWasmPluginsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginsResponse)>`  
  
  
### updateAgentGateway(UpdateAgentGatewayRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateAgentGateway(UpdateAgentGatewayRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single AgentGateway.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateAgentGatewayRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateEndpointPolicy(UpdateEndpointPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateEndpointPolicy(UpdateEndpointPolicyRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single EndpointPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateEndpointPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateGateway(UpdateGatewayRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateGateway(UpdateGatewayRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single Gateway.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateGatewayRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateGrpcRoute(UpdateGrpcRouteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateGrpcRoute(UpdateGrpcRouteRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single GrpcRoute.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateGrpcRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateHttpRoute(UpdateHttpRouteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateHttpRoute(UpdateHttpRouteRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single HttpRoute.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateHttpRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateMesh(UpdateMeshRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateMesh(UpdateMeshRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single Mesh.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateMeshRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateServiceBinding(UpdateServiceBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateServiceBinding(UpdateServiceBindingRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single ServiceBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateServiceBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateServiceLbPolicy(UpdateServiceLbPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateServiceLbPolicy(UpdateServiceLbPolicyRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single ServiceLbPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateServiceLbPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateTcpRoute(UpdateTcpRouteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateTcpRoute(UpdateTcpRouteRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single TcpRoute.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateTcpRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateTlsRoute(UpdateTlsRouteRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateTlsRoute(UpdateTlsRouteRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single TlsRoute.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateTlsRouteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateWasmPlugin(UpdateWasmPluginRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateWasmPlugin(UpdateWasmPluginRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of the specified `WasmPlugin` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateWasmPluginRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
