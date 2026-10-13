---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesGrpc.NetworkServicesBlockingV2Stub
title: Class NetworkServicesGrpc.NetworkServicesBlockingV2Stub (0.55.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:07.685607+00:00
---

# Class NetworkServicesGrpc.NetworkServicesBlockingV2Stub (0.55.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesGrpc.NetworkServicesBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NetworkServicesGrpc.NetworkServicesBlockingV2Stub (0.55.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.55.0 (latest)  0.51.0  0.50.0  0.49.0  0.47.0  0.44.0  0.43.0  0.41.0  0.39.0  0.38.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class NetworkServicesGrpc.NetworkServicesBlockingV2Stub extends AbstractBlockingStub<NetworkServicesGrpc.NetworkServicesBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service NetworkServices.

Service describing handlers for resources.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > NetworkServicesGrpc.NetworkServicesBlockingV2Stub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected NetworkServicesGrpc.NetworkServicesBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesGrpc.NetworkServicesBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesGrpc.NetworkServicesBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createAgentGateway(CreateAgentGatewayRequest request)
    
    
    public Operation createAgentGateway(CreateAgentGatewayRequest request)

Creates a new AgentGateway in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateAgentGatewayRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createEndpointPolicy(CreateEndpointPolicyRequest request)
    
    
    public Operation createEndpointPolicy(CreateEndpointPolicyRequest request)

Creates a new EndpointPolicy in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateEndpointPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createGateway(CreateGatewayRequest request)
    
    
    public Operation createGateway(CreateGatewayRequest request)

Creates a new Gateway in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateGatewayRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createGrpcRoute(CreateGrpcRouteRequest request)
    
    
    public Operation createGrpcRoute(CreateGrpcRouteRequest request)

Creates a new GrpcRoute in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateGrpcRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createHttpRoute(CreateHttpRouteRequest request)
    
    
    public Operation createHttpRoute(CreateHttpRouteRequest request)

Creates a new HttpRoute in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateHttpRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createMesh(CreateMeshRequest request)
    
    
    public Operation createMesh(CreateMeshRequest request)

Creates a new Mesh in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateMeshRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createServiceBinding(CreateServiceBindingRequest request)
    
    
    public Operation createServiceBinding(CreateServiceBindingRequest request)

Creates a new ServiceBinding in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateServiceBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createServiceLbPolicy(CreateServiceLbPolicyRequest request)
    
    
    public Operation createServiceLbPolicy(CreateServiceLbPolicyRequest request)

Creates a new ServiceLbPolicy in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateServiceLbPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createTcpRoute(CreateTcpRouteRequest request)
    
    
    public Operation createTcpRoute(CreateTcpRouteRequest request)

Creates a new TcpRoute in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateTcpRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createTlsRoute(CreateTlsRouteRequest request)
    
    
    public Operation createTlsRoute(CreateTlsRouteRequest request)

Creates a new TlsRoute in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateTlsRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createWasmPlugin(CreateWasmPluginRequest request)
    
    
    public Operation createWasmPlugin(CreateWasmPluginRequest request)

Creates a new `WasmPlugin` resource in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateWasmPluginRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createWasmPluginVersion(CreateWasmPluginVersionRequest request)
    
    
    public Operation createWasmPluginVersion(CreateWasmPluginVersionRequest request)

Creates a new `WasmPluginVersion` resource in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateWasmPluginVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteAgentGateway(DeleteAgentGatewayRequest request)
    
    
    public Operation deleteAgentGateway(DeleteAgentGatewayRequest request)

Deletes a single AgentGateway.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteAgentGatewayRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteEndpointPolicy(DeleteEndpointPolicyRequest request)
    
    
    public Operation deleteEndpointPolicy(DeleteEndpointPolicyRequest request)

Deletes a single EndpointPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteEndpointPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteGateway(DeleteGatewayRequest request)
    
    
    public Operation deleteGateway(DeleteGatewayRequest request)

Deletes a single Gateway.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteGatewayRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteGrpcRoute(DeleteGrpcRouteRequest request)
    
    
    public Operation deleteGrpcRoute(DeleteGrpcRouteRequest request)

Deletes a single GrpcRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteGrpcRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteHttpRoute(DeleteHttpRouteRequest request)
    
    
    public Operation deleteHttpRoute(DeleteHttpRouteRequest request)

Deletes a single HttpRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteHttpRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteMesh(DeleteMeshRequest request)
    
    
    public Operation deleteMesh(DeleteMeshRequest request)

Deletes a single Mesh.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteMeshRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteServiceBinding(DeleteServiceBindingRequest request)
    
    
    public Operation deleteServiceBinding(DeleteServiceBindingRequest request)

Deletes a single ServiceBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteServiceBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteServiceLbPolicy(DeleteServiceLbPolicyRequest request)
    
    
    public Operation deleteServiceLbPolicy(DeleteServiceLbPolicyRequest request)

Deletes a single ServiceLbPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteServiceLbPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteTcpRoute(DeleteTcpRouteRequest request)
    
    
    public Operation deleteTcpRoute(DeleteTcpRouteRequest request)

Deletes a single TcpRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteTcpRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteTlsRoute(DeleteTlsRouteRequest request)
    
    
    public Operation deleteTlsRoute(DeleteTlsRouteRequest request)

Deletes a single TlsRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteTlsRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteWasmPlugin(DeleteWasmPluginRequest request)
    
    
    public Operation deleteWasmPlugin(DeleteWasmPluginRequest request)

Deletes the specified `WasmPlugin` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteWasmPluginRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteWasmPluginVersion(DeleteWasmPluginVersionRequest request)
    
    
    public Operation deleteWasmPluginVersion(DeleteWasmPluginVersionRequest request)

Deletes the specified `WasmPluginVersion` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteWasmPluginVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getAgentGateway(GetAgentGatewayRequest request)
    
    
    public AgentGateway getAgentGateway(GetAgentGatewayRequest request)

Gets details of a single AgentGateway.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetAgentGatewayRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getEndpointPolicy(GetEndpointPolicyRequest request)
    
    
    public EndpointPolicy getEndpointPolicy(GetEndpointPolicyRequest request)

Gets details of a single EndpointPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetEndpointPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getGateway(GetGatewayRequest request)
    
    
    public Gateway getGateway(GetGatewayRequest request)

Gets details of a single Gateway.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGatewayRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getGatewayRouteView(GetGatewayRouteViewRequest request)
    
    
    public GatewayRouteView getGatewayRouteView(GetGatewayRouteViewRequest request)

Get a single RouteView of a Gateway.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGatewayRouteViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGatewayRouteViewRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GatewayRouteView](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GatewayRouteView)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getGrpcRoute(GetGrpcRouteRequest request)
    
    
    public GrpcRoute getGrpcRoute(GetGrpcRouteRequest request)

Gets details of a single GrpcRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGrpcRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getHttpRoute(GetHttpRouteRequest request)
    
    
    public HttpRoute getHttpRoute(GetHttpRouteRequest request)

Gets details of a single HttpRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetHttpRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getMesh(GetMeshRequest request)
    
    
    public Mesh getMesh(GetMeshRequest request)

Gets details of a single Mesh.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetMeshRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getMeshRouteView(GetMeshRouteViewRequest request)
    
    
    public MeshRouteView getMeshRouteView(GetMeshRouteViewRequest request)

Get a single RouteView of a Mesh.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMeshRouteViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetMeshRouteViewRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MeshRouteView](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.MeshRouteView)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getServiceBinding(GetServiceBindingRequest request)
    
    
    public ServiceBinding getServiceBinding(GetServiceBindingRequest request)

Gets details of a single ServiceBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetServiceBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getServiceLbPolicy(GetServiceLbPolicyRequest request)
    
    
    public ServiceLbPolicy getServiceLbPolicy(GetServiceLbPolicyRequest request)

Gets details of a single ServiceLbPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetServiceLbPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getTcpRoute(GetTcpRouteRequest request)
    
    
    public TcpRoute getTcpRoute(GetTcpRouteRequest request)

Gets details of a single TcpRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetTcpRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getTlsRoute(GetTlsRouteRequest request)
    
    
    public TlsRoute getTlsRoute(GetTlsRouteRequest request)

Gets details of a single TlsRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetTlsRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getWasmPlugin(GetWasmPluginRequest request)
    
    
    public WasmPlugin getWasmPlugin(GetWasmPluginRequest request)

Gets details of the specified `WasmPlugin` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetWasmPluginRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getWasmPluginVersion(GetWasmPluginVersionRequest request)
    
    
    public WasmPluginVersion getWasmPluginVersion(GetWasmPluginVersionRequest request)

Gets details of the specified `WasmPluginVersion` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetWasmPluginVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WasmPluginVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginVersion)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listAgentGateways(ListAgentGatewaysRequest request)
    
    
    public ListAgentGatewaysResponse listAgentGateways(ListAgentGatewaysRequest request)

Lists AgentGateways in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAgentGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListAgentGatewaysRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListAgentGatewaysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListAgentGatewaysResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listEndpointPolicies(ListEndpointPoliciesRequest request)
    
    
    public ListEndpointPoliciesResponse listEndpointPolicies(ListEndpointPoliciesRequest request)

Lists EndpointPolicies in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEndpointPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListEndpointPoliciesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListEndpointPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListEndpointPoliciesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listGatewayRouteViews(ListGatewayRouteViewsRequest request)
    
    
    public ListGatewayRouteViewsResponse listGatewayRouteViews(ListGatewayRouteViewsRequest request)

Lists RouteViews

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGatewayRouteViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewayRouteViewsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListGatewayRouteViewsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewayRouteViewsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listGateways(ListGatewaysRequest request)
    
    
    public ListGatewaysResponse listGateways(ListGatewaysRequest request)

Lists Gateways in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewaysRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListGatewaysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewaysResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listGrpcRoutes(ListGrpcRoutesRequest request)
    
    
    public ListGrpcRoutesResponse listGrpcRoutes(ListGrpcRoutesRequest request)

Lists GrpcRoutes in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGrpcRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGrpcRoutesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListGrpcRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGrpcRoutesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listHttpRoutes(ListHttpRoutesRequest request)
    
    
    public ListHttpRoutesResponse listHttpRoutes(ListHttpRoutesRequest request)

Lists HttpRoute in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHttpRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListHttpRoutesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListHttpRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListHttpRoutesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listMeshRouteViews(ListMeshRouteViewsRequest request)
    
    
    public ListMeshRouteViewsResponse listMeshRouteViews(ListMeshRouteViewsRequest request)

Lists RouteViews

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMeshRouteViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshRouteViewsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListMeshRouteViewsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshRouteViewsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listMeshes(ListMeshesRequest request)
    
    
    public ListMeshesResponse listMeshes(ListMeshesRequest request)

Lists Meshes in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMeshesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListMeshesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listServiceBindings(ListServiceBindingsRequest request)
    
    
    public ListServiceBindingsResponse listServiceBindings(ListServiceBindingsRequest request)

Lists ServiceBinding in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServiceBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceBindingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListServiceBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceBindingsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listServiceLbPolicies(ListServiceLbPoliciesRequest request)
    
    
    public ListServiceLbPoliciesResponse listServiceLbPolicies(ListServiceLbPoliciesRequest request)

Lists ServiceLbPolicies in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServiceLbPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceLbPoliciesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListServiceLbPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceLbPoliciesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listTcpRoutes(ListTcpRoutesRequest request)
    
    
    public ListTcpRoutesResponse listTcpRoutes(ListTcpRoutesRequest request)

Lists TcpRoute in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTcpRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTcpRoutesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListTcpRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTcpRoutesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listTlsRoutes(ListTlsRoutesRequest request)
    
    
    public ListTlsRoutesResponse listTlsRoutes(ListTlsRoutesRequest request)

Lists TlsRoute in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTlsRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTlsRoutesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListTlsRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTlsRoutesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listWasmPluginVersions(ListWasmPluginVersionsRequest request)
    
    
    public ListWasmPluginVersionsResponse listWasmPluginVersions(ListWasmPluginVersionsRequest request)

Lists `WasmPluginVersion` resources in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListWasmPluginVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginVersionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListWasmPluginVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginVersionsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listWasmPlugins(ListWasmPluginsRequest request)
    
    
    public ListWasmPluginsResponse listWasmPlugins(ListWasmPluginsRequest request)

Lists `WasmPlugin` resources in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListWasmPluginsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListWasmPluginsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateAgentGateway(UpdateAgentGatewayRequest request)
    
    
    public Operation updateAgentGateway(UpdateAgentGatewayRequest request)

Updates the parameters of a single AgentGateway.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateAgentGatewayRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateEndpointPolicy(UpdateEndpointPolicyRequest request)
    
    
    public Operation updateEndpointPolicy(UpdateEndpointPolicyRequest request)

Updates the parameters of a single EndpointPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateEndpointPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateGateway(UpdateGatewayRequest request)
    
    
    public Operation updateGateway(UpdateGatewayRequest request)

Updates the parameters of a single Gateway.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateGatewayRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateGrpcRoute(UpdateGrpcRouteRequest request)
    
    
    public Operation updateGrpcRoute(UpdateGrpcRouteRequest request)

Updates the parameters of a single GrpcRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateGrpcRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateHttpRoute(UpdateHttpRouteRequest request)
    
    
    public Operation updateHttpRoute(UpdateHttpRouteRequest request)

Updates the parameters of a single HttpRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateHttpRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateMesh(UpdateMeshRequest request)
    
    
    public Operation updateMesh(UpdateMeshRequest request)

Updates the parameters of a single Mesh.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateMeshRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateServiceBinding(UpdateServiceBindingRequest request)
    
    
    public Operation updateServiceBinding(UpdateServiceBindingRequest request)

Updates the parameters of a single ServiceBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateServiceBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateServiceLbPolicy(UpdateServiceLbPolicyRequest request)
    
    
    public Operation updateServiceLbPolicy(UpdateServiceLbPolicyRequest request)

Updates the parameters of a single ServiceLbPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateServiceLbPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateTcpRoute(UpdateTcpRouteRequest request)
    
    
    public Operation updateTcpRoute(UpdateTcpRouteRequest request)

Updates the parameters of a single TcpRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateTcpRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateTlsRoute(UpdateTlsRouteRequest request)
    
    
    public Operation updateTlsRoute(UpdateTlsRouteRequest request)

Updates the parameters of a single TlsRoute.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateTlsRouteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateWasmPlugin(UpdateWasmPluginRequest request)
    
    
    public Operation updateWasmPlugin(UpdateWasmPluginRequest request)

Updates the parameters of the specified `WasmPlugin` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateWasmPluginRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
