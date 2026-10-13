---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryGrpc.AgentRegistryStub
title: Class AgentRegistryGrpc.AgentRegistryStub (0.6.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:16.907859+00:00
---

# Class AgentRegistryGrpc.AgentRegistryStub (0.6.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryGrpc.AgentRegistryStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AgentRegistryGrpc.AgentRegistryStub (0.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.0 (latest)  0.2.0  0.1.0 
    
    
    public static final class AgentRegistryGrpc.AgentRegistryStub extends AbstractAsyncStub<AgentRegistryGrpc.AgentRegistryStub>

A stub to allow clients to do asynchronous rpc calls to service AgentRegistry.

Service for managing Agents, Endpoints, McpServers, Services, and Bindings.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > AgentRegistryGrpc.AgentRegistryStub

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
    
    
    protected AgentRegistryGrpc.AgentRegistryStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryGrpc.AgentRegistryStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryGrpc.AgentRegistryStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createBinding(CreateBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createBinding(CreateBindingRequest request, StreamObserver<Operation> responseObserver)

Creates a new Binding in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.CreateBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createService(CreateServiceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createService(CreateServiceRequest request, StreamObserver<Operation> responseObserver)

Creates a new Service in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.CreateServiceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteBinding(DeleteBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteBinding(DeleteBindingRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.DeleteBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteService(DeleteServiceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteService(DeleteServiceRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.DeleteServiceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### fetchAvailableBindings(FetchAvailableBindingsRequest request, StreamObserver<FetchAvailableBindingsResponse> responseObserver)
    
    
    public void fetchAvailableBindings(FetchAvailableBindingsRequest request, StreamObserver<FetchAvailableBindingsResponse> responseObserver)

Fetches available Bindings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchAvailableBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.FetchAvailableBindingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchAvailableBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.FetchAvailableBindingsResponse)>`  
  
  
### getAgent(GetAgentRequest request, StreamObserver<Agent> responseObserver)
    
    
    public void getAgent(GetAgentRequest request, StreamObserver<Agent> responseObserver)

Gets details of a single Agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.GetAgentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Agent)>`  
  
  
### getBinding(GetBindingRequest request, StreamObserver<Binding> responseObserver)
    
    
    public void getBinding(GetBindingRequest request, StreamObserver<Binding> responseObserver)

Gets details of a single Binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.GetBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding)>`  
  
  
### getEndpoint(GetEndpointRequest request, StreamObserver<Endpoint> responseObserver)
    
    
    public void getEndpoint(GetEndpointRequest request, StreamObserver<Endpoint> responseObserver)

Gets details of a single Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.GetEndpointRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Endpoint)>`  
  
  
### getMcpServer(GetMcpServerRequest request, StreamObserver<McpServer> responseObserver)
    
    
    public void getMcpServer(GetMcpServerRequest request, StreamObserver<McpServer> responseObserver)

Gets details of a single McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMcpServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.GetMcpServerRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[McpServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.McpServer)>`  
  
  
### getService(GetServiceRequest request, StreamObserver<Service> responseObserver)
    
    
    public void getService(GetServiceRequest request, StreamObserver<Service> responseObserver)

Gets details of a single Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.GetServiceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Service)>`  
  
  
### listAgents(ListAgentsRequest request, StreamObserver<ListAgentsResponse> responseObserver)
    
    
    public void listAgents(ListAgentsRequest request, StreamObserver<ListAgentsResponse> responseObserver)

Lists Agents in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListAgentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAgentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListAgentsResponse)>`  
  
  
### listBindings(ListBindingsRequest request, StreamObserver<ListBindingsResponse> responseObserver)
    
    
    public void listBindings(ListBindingsRequest request, StreamObserver<ListBindingsResponse> responseObserver)

Lists Bindings in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListBindingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListBindingsResponse)>`  
  
  
### listEndpoints(ListEndpointsRequest request, StreamObserver<ListEndpointsResponse> responseObserver)
    
    
    public void listEndpoints(ListEndpointsRequest request, StreamObserver<ListEndpointsResponse> responseObserver)

Lists Endpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListEndpointsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListEndpointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListEndpointsResponse)>`  
  
  
### listMcpServers(ListMcpServersRequest request, StreamObserver<ListMcpServersResponse> responseObserver)
    
    
    public void listMcpServers(ListMcpServersRequest request, StreamObserver<ListMcpServersResponse> responseObserver)

Lists McpServers in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMcpServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListMcpServersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMcpServersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListMcpServersResponse)>`  
  
  
### listServices(ListServicesRequest request, StreamObserver<ListServicesResponse> responseObserver)
    
    
    public void listServices(ListServicesRequest request, StreamObserver<ListServicesResponse> responseObserver)

Lists Services in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListServicesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListServicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListServicesResponse)>`  
  
  
### searchAgents(SearchAgentsRequest request, StreamObserver<SearchAgentsResponse> responseObserver)
    
    
    public void searchAgents(SearchAgentsRequest request, StreamObserver<SearchAgentsResponse> responseObserver)

Searches Agents in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.SearchAgentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SearchAgentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.SearchAgentsResponse)>`  
  
  
### searchMcpServers(SearchMcpServersRequest request, StreamObserver<SearchMcpServersResponse> responseObserver)
    
    
    public void searchMcpServers(SearchMcpServersRequest request, StreamObserver<SearchMcpServersResponse> responseObserver)

Searches McpServers in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchMcpServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.SearchMcpServersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SearchMcpServersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.SearchMcpServersResponse)>`  
  
  
### updateBinding(UpdateBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateBinding(UpdateBindingRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single Binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.UpdateBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateService(UpdateServiceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateService(UpdateServiceRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single Service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.UpdateServiceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
