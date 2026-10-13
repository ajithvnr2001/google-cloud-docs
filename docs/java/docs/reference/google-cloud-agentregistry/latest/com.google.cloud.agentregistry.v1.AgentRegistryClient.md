---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient
title: Class AgentRegistryClient (0.6.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:20.373611+00:00
---

# Class AgentRegistryClient (0.6.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AgentRegistryClient (0.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.0 (latest)  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-agentregistry/google-cloud-agentregistry/src/main/java/com/google/cloud/agentregistry/v1/AgentRegistryClient.java)| [Product Reference](https://docs.cloud.google.com/agent-registry/overview)  
---|---  
  
Service Description: Service for managing Agents, Endpoints, McpServers, Services, and Bindings.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       AgentName name = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       Agent response = agentRegistryClient.getAgent(name);
     }
     

Note: close() needs to be called on the AgentRegistryClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListAgents |  Lists Agents in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAgents(ListAgentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAgents(LocationName parent) 
  * listAgents(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAgentsPagedCallable() 
  * listAgentsCallable() 

  
SearchAgents |  Searches Agents in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchAgents(SearchAgentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * searchAgents(LocationName parent) 
  * searchAgents(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchAgentsPagedCallable() 
  * searchAgentsCallable() 

  
GetAgent |  Gets details of a single Agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAgent(GetAgentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAgent(AgentName name) 
  * getAgent(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAgentCallable() 

  
ListEndpoints |  Lists Endpoints in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEndpoints(ListEndpointsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEndpoints(LocationName parent) 
  * listEndpoints(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEndpointsPagedCallable() 
  * listEndpointsCallable() 

  
GetEndpoint |  Gets details of a single Endpoint. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEndpoint(GetEndpointRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEndpoint(EndpointName name) 
  * getEndpoint(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEndpointCallable() 

  
ListMcpServers |  Lists McpServers in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMcpServers(ListMcpServersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMcpServers(LocationName parent) 
  * listMcpServers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMcpServersPagedCallable() 
  * listMcpServersCallable() 

  
SearchMcpServers |  Searches McpServers in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchMcpServers(SearchMcpServersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * searchMcpServers(LocationName parent) 
  * searchMcpServers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchMcpServersPagedCallable() 
  * searchMcpServersCallable() 

  
GetMcpServer |  Gets details of a single McpServer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMcpServer(GetMcpServerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMcpServer(McpServerName name) 
  * getMcpServer(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMcpServerCallable() 

  
ListServices |  Lists Services in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listServices(ListServicesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listServices(LocationName parent) 
  * listServices(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listServicesPagedCallable() 
  * listServicesCallable() 

  
GetService |  Gets details of a single Service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getService(GetServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getService(ServiceName name) 
  * getService(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getServiceCallable() 

  
CreateService |  Creates a new Service in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createServiceAsync(CreateServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createServiceAsync(LocationName parent, Service service, String serviceId) 
  * createServiceAsync(String parent, Service service, String serviceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createServiceOperationCallable() 
  * createServiceCallable() 

  
UpdateService |  Updates the parameters of a single Service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateServiceAsync(UpdateServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateServiceAsync(Service service, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateServiceOperationCallable() 
  * updateServiceCallable() 

  
DeleteService |  Deletes a single Service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteServiceAsync(DeleteServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteServiceAsync(ServiceName name) 
  * deleteServiceAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteServiceOperationCallable() 
  * deleteServiceCallable() 

  
ListBindings |  Lists Bindings in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBindings(ListBindingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBindings(LocationName parent) 
  * listBindings(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBindingsPagedCallable() 
  * listBindingsCallable() 

  
GetBinding |  Gets details of a single Binding. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBinding(GetBindingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBinding(BindingName name) 
  * getBinding(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBindingCallable() 

  
CreateBinding |  Creates a new Binding in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createBindingAsync(CreateBindingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createBindingAsync(LocationName parent, Binding binding, String bindingId) 
  * createBindingAsync(String parent, Binding binding, String bindingId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createBindingOperationCallable() 
  * createBindingCallable() 

  
UpdateBinding |  Updates the parameters of a single Binding. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateBindingAsync(UpdateBindingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateBindingAsync(Binding binding, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateBindingOperationCallable() 
  * updateBindingCallable() 

  
DeleteBinding |  Deletes a single Binding. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBindingAsync(DeleteBindingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteBindingAsync(BindingName name) 
  * deleteBindingAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBindingOperationCallable() 
  * deleteBindingCallable() 

  
FetchAvailableBindings |  Fetches available Bindings. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchAvailableBindings(FetchAvailableBindingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * fetchAvailableBindings(LocationName parent) 
  * fetchAvailableBindings(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchAvailableBindingsPagedCallable() 
  * fetchAvailableBindingsCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AgentRegistrySettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AgentRegistrySettings agentRegistrySettings =
         AgentRegistrySettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AgentRegistryClient agentRegistryClient = AgentRegistryClient.create(agentRegistrySettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AgentRegistrySettings agentRegistrySettings =
         AgentRegistrySettings.newBuilder().setEndpoint(myEndpoint).build();
     AgentRegistryClient agentRegistryClient = AgentRegistryClient.create(agentRegistrySettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AgentRegistrySettings agentRegistrySettings =
         AgentRegistrySettings.newHttpJsonBuilder().build();
     AgentRegistryClient agentRegistryClient = AgentRegistryClient.create(agentRegistrySettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AgentRegistryClient

## Static Methods 

### create()
    
    
    public static final AgentRegistryClient create()

Constructs an instance of AgentRegistryClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AgentRegistrySettings settings)
    
    
    public static final AgentRegistryClient create(AgentRegistrySettings settings)

Constructs an instance of AgentRegistryClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AgentRegistrySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistrySettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AgentRegistryStub stub)
    
    
    public static final AgentRegistryClient create(AgentRegistryStub stub)

Constructs an instance of AgentRegistryClient, using the given stub for making calls. This is for advanced usage - prefer using create(AgentRegistrySettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AgentRegistryStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.stub.AgentRegistryStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient)` |   
  
## Constructors 

### AgentRegistryClient(AgentRegistrySettings settings)
    
    
    protected AgentRegistryClient(AgentRegistrySettings settings)

Constructs an instance of AgentRegistryClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AgentRegistrySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistrySettings)`  
  
  
### AgentRegistryClient(AgentRegistryStub stub)
    
    
    protected AgentRegistryClient(AgentRegistryStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AgentRegistryStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.stub.AgentRegistryStub)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### close()
    
    
    public final void close()

### createBindingAsync(@Nullable LocationName parent, Binding binding, String bindingId)
    
    
    public final OperationFuture<Binding,OperationMetadata> createBindingAsync(@Nullable LocationName parent, Binding binding, String bindingId)

Creates a new Binding in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Binding binding = Binding.newBuilder().build();
       String bindingId = "bindingId-920966528";
       Binding response = agentRegistryClient.createBindingAsync(parent, binding, bindingId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.LocationName`  
Required. The project and location to create the Binding in. Expected format: `projects/{project}/locations/{location}`.  
`binding` | `[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding)`  
Required. The Binding resource that is being created.  
`bindingId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the binding, which will become the final component of the binding's resource name. This value should be 4-63 characters, and must conform to RFC-1034. Specifically, it must match the regular expression `^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### createBindingAsync(CreateBindingRequest request)
    
    
    public final OperationFuture<Binding,OperationMetadata> createBindingAsync(CreateBindingRequest request)

Creates a new Binding in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       CreateBindingRequest request =
           CreateBindingRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBindingId("bindingId-920966528")
               .setBinding(Binding.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Binding response = agentRegistryClient.createBindingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.CreateBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### createBindingAsync(String parent, Binding binding, String bindingId)
    
    
    public final OperationFuture<Binding,OperationMetadata> createBindingAsync(String parent, Binding binding, String bindingId)

Creates a new Binding in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Binding binding = Binding.newBuilder().build();
       String bindingId = "bindingId-920966528";
       Binding response = agentRegistryClient.createBindingAsync(parent, binding, bindingId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location to create the Binding in. Expected format: `projects/{project}/locations/{location}`.  
`binding` | `[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding)`  
Required. The Binding resource that is being created.  
`bindingId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the binding, which will become the final component of the binding's resource name. This value should be 4-63 characters, and must conform to RFC-1034. Specifically, it must match the regular expression `^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### createBindingCallable()
    
    
    public final UnaryCallable<CreateBindingRequest,Operation> createBindingCallable()

Creates a new Binding in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       CreateBindingRequest request =
           CreateBindingRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBindingId("bindingId-920966528")
               .setBinding(Binding.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = agentRegistryClient.createBindingCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.CreateBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createBindingOperationCallable()
    
    
    public final OperationCallable<CreateBindingRequest,Binding,OperationMetadata> createBindingOperationCallable()

Creates a new Binding in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       CreateBindingRequest request =
           CreateBindingRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBindingId("bindingId-920966528")
               .setBinding(Binding.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Binding, OperationMetadata> future =
           agentRegistryClient.createBindingOperationCallable().futureCall(request);
       // Do something.
       Binding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.CreateBindingRequest),[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### createServiceAsync(@Nullable LocationName parent, Service service, String serviceId)
    
    
    public final OperationFuture<Service,OperationMetadata> createServiceAsync(@Nullable LocationName parent, Service service, String serviceId)

Creates a new Service in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Service service = Service.newBuilder().build();
       String serviceId = "serviceId-194185552";
       Service response = agentRegistryClient.createServiceAsync(parent, service, serviceId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.LocationName`  
Required. The project and location to create the Service in. Expected format: `projects/{project}/locations/{location}`.  
`service` | `[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Service)`  
Required. The Service resource that is being created. Format: `projects/{project}/locations/{location}/services/{service}`.  
`serviceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the service, which will become the final component of the service's resource name. This value should be 4-63 characters, and valid characters are `/a-z-/`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Service),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### createServiceAsync(CreateServiceRequest request)
    
    
    public final OperationFuture<Service,OperationMetadata> createServiceAsync(CreateServiceRequest request)

Creates a new Service in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       CreateServiceRequest request =
           CreateServiceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceId("serviceId-194185552")
               .setService(Service.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Service response = agentRegistryClient.createServiceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.CreateServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Service),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### createServiceAsync(String parent, Service service, String serviceId)
    
    
    public final OperationFuture<Service,OperationMetadata> createServiceAsync(String parent, Service service, String serviceId)

Creates a new Service in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Service service = Service.newBuilder().build();
       String serviceId = "serviceId-194185552";
       Service response = agentRegistryClient.createServiceAsync(parent, service, serviceId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location to create the Service in. Expected format: `projects/{project}/locations/{location}`.  
`service` | `[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Service)`  
Required. The Service resource that is being created. Format: `projects/{project}/locations/{location}/services/{service}`.  
`serviceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the service, which will become the final component of the service's resource name. This value should be 4-63 characters, and valid characters are `/a-z-/`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Service),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### createServiceCallable()
    
    
    public final UnaryCallable<CreateServiceRequest,Operation> createServiceCallable()

Creates a new Service in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       CreateServiceRequest request =
           CreateServiceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceId("serviceId-194185552")
               .setService(Service.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = agentRegistryClient.createServiceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.CreateServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createServiceOperationCallable()
    
    
    public final OperationCallable<CreateServiceRequest,Service,OperationMetadata> createServiceOperationCallable()

Creates a new Service in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       CreateServiceRequest request =
           CreateServiceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceId("serviceId-194185552")
               .setService(Service.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Service, OperationMetadata> future =
           agentRegistryClient.createServiceOperationCallable().futureCall(request);
       // Do something.
       Service response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.CreateServiceRequest),[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Service),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### deleteBindingAsync(@Nullable BindingName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBindingAsync(@Nullable BindingName name)

Deletes a single Binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       BindingName name = BindingName.of("[PROJECT]", "[LOCATION]", "[BINDING]");
       agentRegistryClient.deleteBindingAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.BindingName`  
Required. The name of the Binding. Format: `projects/{project}/locations/{location}/bindings/{binding}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### deleteBindingAsync(DeleteBindingRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBindingAsync(DeleteBindingRequest request)

Deletes a single Binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       DeleteBindingRequest request =
           DeleteBindingRequest.newBuilder()
               .setName(BindingName.of("[PROJECT]", "[LOCATION]", "[BINDING]").toString())
               .setRequestId("requestId693933066")
               .build();
       agentRegistryClient.deleteBindingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.DeleteBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### deleteBindingAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBindingAsync(String name)

Deletes a single Binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String name = BindingName.of("[PROJECT]", "[LOCATION]", "[BINDING]").toString();
       agentRegistryClient.deleteBindingAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Binding. Format: `projects/{project}/locations/{location}/bindings/{binding}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### deleteBindingCallable()
    
    
    public final UnaryCallable<DeleteBindingRequest,Operation> deleteBindingCallable()

Deletes a single Binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       DeleteBindingRequest request =
           DeleteBindingRequest.newBuilder()
               .setName(BindingName.of("[PROJECT]", "[LOCATION]", "[BINDING]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = agentRegistryClient.deleteBindingCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.DeleteBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteBindingOperationCallable()
    
    
    public final OperationCallable<DeleteBindingRequest,Empty,OperationMetadata> deleteBindingOperationCallable()

Deletes a single Binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       DeleteBindingRequest request =
           DeleteBindingRequest.newBuilder()
               .setName(BindingName.of("[PROJECT]", "[LOCATION]", "[BINDING]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           agentRegistryClient.deleteBindingOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.DeleteBindingRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### deleteServiceAsync(@Nullable ServiceName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceAsync(@Nullable ServiceName name)

Deletes a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ServiceName name = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]");
       agentRegistryClient.deleteServiceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.ServiceName`  
Required. The name of the Service. Format: `projects/{project}/locations/{location}/services/{service}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### deleteServiceAsync(DeleteServiceRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceAsync(DeleteServiceRequest request)

Deletes a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       DeleteServiceRequest request =
           DeleteServiceRequest.newBuilder()
               .setName(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setRequestId("requestId693933066")
               .build();
       agentRegistryClient.deleteServiceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.DeleteServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### deleteServiceAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceAsync(String name)

Deletes a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String name = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString();
       agentRegistryClient.deleteServiceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Service. Format: `projects/{project}/locations/{location}/services/{service}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### deleteServiceCallable()
    
    
    public final UnaryCallable<DeleteServiceRequest,Operation> deleteServiceCallable()

Deletes a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       DeleteServiceRequest request =
           DeleteServiceRequest.newBuilder()
               .setName(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = agentRegistryClient.deleteServiceCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.DeleteServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteServiceOperationCallable()
    
    
    public final OperationCallable<DeleteServiceRequest,Empty,OperationMetadata> deleteServiceOperationCallable()

Deletes a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       DeleteServiceRequest request =
           DeleteServiceRequest.newBuilder()
               .setName(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           agentRegistryClient.deleteServiceOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.DeleteServiceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### fetchAvailableBindings(@Nullable LocationName parent)
    
    
    public final AgentRegistryClient.FetchAvailableBindingsPagedResponse fetchAvailableBindings(@Nullable LocationName parent)

Fetches available Bindings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Binding element : agentRegistryClient.fetchAvailableBindings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.LocationName`  
Required. The parent, in the format `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.FetchAvailableBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.FetchAvailableBindingsPagedResponse)` |   
  
### fetchAvailableBindings(FetchAvailableBindingsRequest request)
    
    
    public final AgentRegistryClient.FetchAvailableBindingsPagedResponse fetchAvailableBindings(FetchAvailableBindingsRequest request)

Fetches available Bindings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       FetchAvailableBindingsRequest request =
           FetchAvailableBindingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Binding element : agentRegistryClient.fetchAvailableBindings(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchAvailableBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.FetchAvailableBindingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.FetchAvailableBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.FetchAvailableBindingsPagedResponse)` |   
  
### fetchAvailableBindings(String parent)
    
    
    public final AgentRegistryClient.FetchAvailableBindingsPagedResponse fetchAvailableBindings(String parent)

Fetches available Bindings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Binding element : agentRegistryClient.fetchAvailableBindings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, in the format `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.FetchAvailableBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.FetchAvailableBindingsPagedResponse)` |   
  
### fetchAvailableBindingsCallable()
    
    
    public final UnaryCallable<FetchAvailableBindingsRequest,FetchAvailableBindingsResponse> fetchAvailableBindingsCallable()

Fetches available Bindings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       FetchAvailableBindingsRequest request =
           FetchAvailableBindingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         FetchAvailableBindingsResponse response =
             agentRegistryClient.fetchAvailableBindingsCallable().call(request);
         for (Binding element : response.getBindingsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchAvailableBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.FetchAvailableBindingsRequest),[FetchAvailableBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.FetchAvailableBindingsResponse)>` |   
  
### fetchAvailableBindingsPagedCallable()
    
    
    public final UnaryCallable<FetchAvailableBindingsRequest,AgentRegistryClient.FetchAvailableBindingsPagedResponse> fetchAvailableBindingsPagedCallable()

Fetches available Bindings.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       FetchAvailableBindingsRequest request =
           FetchAvailableBindingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Binding> future =
           agentRegistryClient.fetchAvailableBindingsPagedCallable().futureCall(request);
       // Do something.
       for (Binding element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchAvailableBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.FetchAvailableBindingsRequest),[FetchAvailableBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.FetchAvailableBindingsPagedResponse)>` |   
  
### getAgent(@Nullable AgentName name)
    
    
    public final Agent getAgent(@Nullable AgentName name)

Gets details of a single Agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       AgentName name = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       Agent response = agentRegistryClient.getAgent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.AgentName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Agent)` |   
  
### getAgent(GetAgentRequest request)
    
    
    public final Agent getAgent(GetAgentRequest request)

Gets details of a single Agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       GetAgentRequest request =
           GetAgentRequest.newBuilder()
               .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .build();
       Agent response = agentRegistryClient.getAgent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.GetAgentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Agent)` |   
  
### getAgent(String name)
    
    
    public final Agent getAgent(String name)

Gets details of a single Agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String name = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString();
       Agent response = agentRegistryClient.getAgent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Agent)` |   
  
### getAgentCallable()
    
    
    public final UnaryCallable<GetAgentRequest,Agent> getAgentCallable()

Gets details of a single Agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       GetAgentRequest request =
           GetAgentRequest.newBuilder()
               .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .build();
       ApiFuture<Agent> future = agentRegistryClient.getAgentCallable().futureCall(request);
       // Do something.
       Agent response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.GetAgentRequest),[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Agent)>` |   
  
### getBinding(@Nullable BindingName name)
    
    
    public final Binding getBinding(@Nullable BindingName name)

Gets details of a single Binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       BindingName name = BindingName.of("[PROJECT]", "[LOCATION]", "[BINDING]");
       Binding response = agentRegistryClient.getBinding(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.BindingName`  
Required. The name of the Binding. Format: `projects/{project}/locations/{location}/bindings/{binding}`.  
**Returns**  
---  
**Type** | **Description**  
`[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding)` |   
  
### getBinding(GetBindingRequest request)
    
    
    public final Binding getBinding(GetBindingRequest request)

Gets details of a single Binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       GetBindingRequest request =
           GetBindingRequest.newBuilder()
               .setName(BindingName.of("[PROJECT]", "[LOCATION]", "[BINDING]").toString())
               .build();
       Binding response = agentRegistryClient.getBinding(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.GetBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding)` |   
  
### getBinding(String name)
    
    
    public final Binding getBinding(String name)

Gets details of a single Binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String name = BindingName.of("[PROJECT]", "[LOCATION]", "[BINDING]").toString();
       Binding response = agentRegistryClient.getBinding(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Binding. Format: `projects/{project}/locations/{location}/bindings/{binding}`.  
**Returns**  
---  
**Type** | **Description**  
`[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding)` |   
  
### getBindingCallable()
    
    
    public final UnaryCallable<GetBindingRequest,Binding> getBindingCallable()

Gets details of a single Binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       GetBindingRequest request =
           GetBindingRequest.newBuilder()
               .setName(BindingName.of("[PROJECT]", "[LOCATION]", "[BINDING]").toString())
               .build();
       ApiFuture<Binding> future = agentRegistryClient.getBindingCallable().futureCall(request);
       // Do something.
       Binding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.GetBindingRequest),[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding)>` |   
  
### getEndpoint(@Nullable EndpointName name)
    
    
    public final Endpoint getEndpoint(@Nullable EndpointName name)

Gets details of a single Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       EndpointName name = EndpointName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
       Endpoint response = agentRegistryClient.getEndpoint(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.EndpointName`  
Required. The name of the endpoint to retrieve. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Endpoint)` |   
  
### getEndpoint(GetEndpointRequest request)
    
    
    public final Endpoint getEndpoint(GetEndpointRequest request)

Gets details of a single Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       GetEndpointRequest request =
           GetEndpointRequest.newBuilder()
               .setName(EndpointName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT]").toString())
               .build();
       Endpoint response = agentRegistryClient.getEndpoint(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.GetEndpointRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Endpoint)` |   
  
### getEndpoint(String name)
    
    
    public final Endpoint getEndpoint(String name)

Gets details of a single Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String name = EndpointName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT]").toString();
       Endpoint response = agentRegistryClient.getEndpoint(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the endpoint to retrieve. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Endpoint)` |   
  
### getEndpointCallable()
    
    
    public final UnaryCallable<GetEndpointRequest,Endpoint> getEndpointCallable()

Gets details of a single Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       GetEndpointRequest request =
           GetEndpointRequest.newBuilder()
               .setName(EndpointName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT]").toString())
               .build();
       ApiFuture<Endpoint> future = agentRegistryClient.getEndpointCallable().futureCall(request);
       // Do something.
       Endpoint response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.GetEndpointRequest),[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Endpoint)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = agentRegistryClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = agentRegistryClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getMcpServer(@Nullable McpServerName name)
    
    
    public final McpServer getMcpServer(@Nullable McpServerName name)

Gets details of a single McpServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       McpServerName name = McpServerName.of("[PROJECT]", "[LOCATION]", "[MCP_SERVER]");
       McpServer response = agentRegistryClient.getMcpServer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.McpServerName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[McpServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.McpServer)` |   
  
### getMcpServer(GetMcpServerRequest request)
    
    
    public final McpServer getMcpServer(GetMcpServerRequest request)

Gets details of a single McpServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       GetMcpServerRequest request =
           GetMcpServerRequest.newBuilder()
               .setName(McpServerName.of("[PROJECT]", "[LOCATION]", "[MCP_SERVER]").toString())
               .build();
       McpServer response = agentRegistryClient.getMcpServer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMcpServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.GetMcpServerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[McpServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.McpServer)` |   
  
### getMcpServer(String name)
    
    
    public final McpServer getMcpServer(String name)

Gets details of a single McpServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String name = McpServerName.of("[PROJECT]", "[LOCATION]", "[MCP_SERVER]").toString();
       McpServer response = agentRegistryClient.getMcpServer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[McpServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.McpServer)` |   
  
### getMcpServerCallable()
    
    
    public final UnaryCallable<GetMcpServerRequest,McpServer> getMcpServerCallable()

Gets details of a single McpServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       GetMcpServerRequest request =
           GetMcpServerRequest.newBuilder()
               .setName(McpServerName.of("[PROJECT]", "[LOCATION]", "[MCP_SERVER]").toString())
               .build();
       ApiFuture<McpServer> future = agentRegistryClient.getMcpServerCallable().futureCall(request);
       // Do something.
       McpServer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMcpServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.GetMcpServerRequest),[McpServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.McpServer)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getService(@Nullable ServiceName name)
    
    
    public final Service getService(@Nullable ServiceName name)

Gets details of a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ServiceName name = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]");
       Service response = agentRegistryClient.getService(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.ServiceName`  
Required. The name of the Service. Format: `projects/{project}/locations/{location}/services/{service}`.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Service)` |   
  
### getService(GetServiceRequest request)
    
    
    public final Service getService(GetServiceRequest request)

Gets details of a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       GetServiceRequest request =
           GetServiceRequest.newBuilder()
               .setName(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .build();
       Service response = agentRegistryClient.getService(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.GetServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Service)` |   
  
### getService(String name)
    
    
    public final Service getService(String name)

Gets details of a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String name = ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString();
       Service response = agentRegistryClient.getService(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Service. Format: `projects/{project}/locations/{location}/services/{service}`.  
**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Service)` |   
  
### getServiceCallable()
    
    
    public final UnaryCallable<GetServiceRequest,Service> getServiceCallable()

Gets details of a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       GetServiceRequest request =
           GetServiceRequest.newBuilder()
               .setName(ServiceName.of("[PROJECT]", "[LOCATION]", "[SERVICE]").toString())
               .build();
       ApiFuture<Service> future = agentRegistryClient.getServiceCallable().futureCall(request);
       // Do something.
       Service response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.GetServiceRequest),[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Service)>` |   
  
### getSettings()
    
    
    public final @Nullable AgentRegistrySettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.AgentRegistrySettings` |   
  
### getStub()
    
    
    public AgentRegistryStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.stub.AgentRegistryStub)` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listAgents(@Nullable LocationName parent)
    
    
    public final AgentRegistryClient.ListAgentsPagedResponse listAgents(@Nullable LocationName parent)

Lists Agents in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Agent element : agentRegistryClient.listAgents(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.LocationName`  
Required. Parent value for ListAgentsRequest  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.ListAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListAgentsPagedResponse)` |   
  
### listAgents(ListAgentsRequest request)
    
    
    public final AgentRegistryClient.ListAgentsPagedResponse listAgents(ListAgentsRequest request)

Lists Agents in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListAgentsRequest request =
           ListAgentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Agent element : agentRegistryClient.listAgents(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListAgentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.ListAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListAgentsPagedResponse)` |   
  
### listAgents(String parent)
    
    
    public final AgentRegistryClient.ListAgentsPagedResponse listAgents(String parent)

Lists Agents in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Agent element : agentRegistryClient.listAgents(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListAgentsRequest  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.ListAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListAgentsPagedResponse)` |   
  
### listAgentsCallable()
    
    
    public final UnaryCallable<ListAgentsRequest,ListAgentsResponse> listAgentsCallable()

Lists Agents in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListAgentsRequest request =
           ListAgentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListAgentsResponse response = agentRegistryClient.listAgentsCallable().call(request);
         for (Agent element : response.getAgentsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListAgentsRequest),[ListAgentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListAgentsResponse)>` |   
  
### listAgentsPagedCallable()
    
    
    public final UnaryCallable<ListAgentsRequest,AgentRegistryClient.ListAgentsPagedResponse> listAgentsPagedCallable()

Lists Agents in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListAgentsRequest request =
           ListAgentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Agent> future = agentRegistryClient.listAgentsPagedCallable().futureCall(request);
       // Do something.
       for (Agent element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListAgentsRequest),[ListAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListAgentsPagedResponse)>` |   
  
### listBindings(@Nullable LocationName parent)
    
    
    public final AgentRegistryClient.ListBindingsPagedResponse listBindings(@Nullable LocationName parent)

Lists Bindings in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Binding element : agentRegistryClient.listBindings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.LocationName`  
Required. The project and location to list bindings in. Expected format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.ListBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListBindingsPagedResponse)` |   
  
### listBindings(ListBindingsRequest request)
    
    
    public final AgentRegistryClient.ListBindingsPagedResponse listBindings(ListBindingsRequest request)

Lists Bindings in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListBindingsRequest request =
           ListBindingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Binding element : agentRegistryClient.listBindings(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListBindingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.ListBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListBindingsPagedResponse)` |   
  
### listBindings(String parent)
    
    
    public final AgentRegistryClient.ListBindingsPagedResponse listBindings(String parent)

Lists Bindings in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Binding element : agentRegistryClient.listBindings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location to list bindings in. Expected format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.ListBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListBindingsPagedResponse)` |   
  
### listBindingsCallable()
    
    
    public final UnaryCallable<ListBindingsRequest,ListBindingsResponse> listBindingsCallable()

Lists Bindings in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListBindingsRequest request =
           ListBindingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListBindingsResponse response = agentRegistryClient.listBindingsCallable().call(request);
         for (Binding element : response.getBindingsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListBindingsRequest),[ListBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListBindingsResponse)>` |   
  
### listBindingsPagedCallable()
    
    
    public final UnaryCallable<ListBindingsRequest,AgentRegistryClient.ListBindingsPagedResponse> listBindingsPagedCallable()

Lists Bindings in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListBindingsRequest request =
           ListBindingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Binding> future =
           agentRegistryClient.listBindingsPagedCallable().futureCall(request);
       // Do something.
       for (Binding element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListBindingsRequest),[ListBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListBindingsPagedResponse)>` |   
  
### listEndpoints(@Nullable LocationName parent)
    
    
    public final AgentRegistryClient.ListEndpointsPagedResponse listEndpoints(@Nullable LocationName parent)

Lists Endpoints in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Endpoint element : agentRegistryClient.listEndpoints(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.LocationName`  
Required. The project and location to list endpoints in. Expected format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.ListEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListEndpointsPagedResponse)` |   
  
### listEndpoints(ListEndpointsRequest request)
    
    
    public final AgentRegistryClient.ListEndpointsPagedResponse listEndpoints(ListEndpointsRequest request)

Lists Endpoints in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListEndpointsRequest request =
           ListEndpointsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Endpoint element : agentRegistryClient.listEndpoints(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListEndpointsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.ListEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListEndpointsPagedResponse)` |   
  
### listEndpoints(String parent)
    
    
    public final AgentRegistryClient.ListEndpointsPagedResponse listEndpoints(String parent)

Lists Endpoints in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Endpoint element : agentRegistryClient.listEndpoints(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location to list endpoints in. Expected format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.ListEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListEndpointsPagedResponse)` |   
  
### listEndpointsCallable()
    
    
    public final UnaryCallable<ListEndpointsRequest,ListEndpointsResponse> listEndpointsCallable()

Lists Endpoints in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListEndpointsRequest request =
           ListEndpointsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListEndpointsResponse response = agentRegistryClient.listEndpointsCallable().call(request);
         for (Endpoint element : response.getEndpointsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListEndpointsRequest),[ListEndpointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListEndpointsResponse)>` |   
  
### listEndpointsPagedCallable()
    
    
    public final UnaryCallable<ListEndpointsRequest,AgentRegistryClient.ListEndpointsPagedResponse> listEndpointsPagedCallable()

Lists Endpoints in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListEndpointsRequest request =
           ListEndpointsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Endpoint> future =
           agentRegistryClient.listEndpointsPagedCallable().futureCall(request);
       // Do something.
       for (Endpoint element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListEndpointsRequest),[ListEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListEndpointsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final AgentRegistryClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : agentRegistryClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = agentRegistryClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,AgentRegistryClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           agentRegistryClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListLocationsPagedResponse)>` |   
  
### listMcpServers(@Nullable LocationName parent)
    
    
    public final AgentRegistryClient.ListMcpServersPagedResponse listMcpServers(@Nullable LocationName parent)

Lists McpServers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (McpServer element : agentRegistryClient.listMcpServers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.LocationName`  
Required. Parent value for ListMcpServersRequest. Format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.ListMcpServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListMcpServersPagedResponse)` |   
  
### listMcpServers(ListMcpServersRequest request)
    
    
    public final AgentRegistryClient.ListMcpServersPagedResponse listMcpServers(ListMcpServersRequest request)

Lists McpServers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListMcpServersRequest request =
           ListMcpServersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (McpServer element : agentRegistryClient.listMcpServers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMcpServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListMcpServersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.ListMcpServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListMcpServersPagedResponse)` |   
  
### listMcpServers(String parent)
    
    
    public final AgentRegistryClient.ListMcpServersPagedResponse listMcpServers(String parent)

Lists McpServers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (McpServer element : agentRegistryClient.listMcpServers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListMcpServersRequest. Format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.ListMcpServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListMcpServersPagedResponse)` |   
  
### listMcpServersCallable()
    
    
    public final UnaryCallable<ListMcpServersRequest,ListMcpServersResponse> listMcpServersCallable()

Lists McpServers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListMcpServersRequest request =
           ListMcpServersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListMcpServersResponse response =
             agentRegistryClient.listMcpServersCallable().call(request);
         for (McpServer element : response.getMcpServersList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMcpServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListMcpServersRequest),[ListMcpServersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListMcpServersResponse)>` |   
  
### listMcpServersPagedCallable()
    
    
    public final UnaryCallable<ListMcpServersRequest,AgentRegistryClient.ListMcpServersPagedResponse> listMcpServersPagedCallable()

Lists McpServers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListMcpServersRequest request =
           ListMcpServersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<McpServer> future =
           agentRegistryClient.listMcpServersPagedCallable().futureCall(request);
       // Do something.
       for (McpServer element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMcpServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListMcpServersRequest),[ListMcpServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListMcpServersPagedResponse)>` |   
  
### listServices(@Nullable LocationName parent)
    
    
    public final AgentRegistryClient.ListServicesPagedResponse listServices(@Nullable LocationName parent)

Lists Services in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Service element : agentRegistryClient.listServices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.LocationName`  
Required. The project and location to list services in. Expected format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListServicesPagedResponse)` |   
  
### listServices(ListServicesRequest request)
    
    
    public final AgentRegistryClient.ListServicesPagedResponse listServices(ListServicesRequest request)

Lists Services in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListServicesRequest request =
           ListServicesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Service element : agentRegistryClient.listServices(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListServicesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListServicesPagedResponse)` |   
  
### listServices(String parent)
    
    
    public final AgentRegistryClient.ListServicesPagedResponse listServices(String parent)

Lists Services in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Service element : agentRegistryClient.listServices(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location to list services in. Expected format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListServicesPagedResponse)` |   
  
### listServicesCallable()
    
    
    public final UnaryCallable<ListServicesRequest,ListServicesResponse> listServicesCallable()

Lists Services in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListServicesRequest request =
           ListServicesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListServicesResponse response = agentRegistryClient.listServicesCallable().call(request);
         for (Service element : response.getServicesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListServicesRequest),[ListServicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListServicesResponse)>` |   
  
### listServicesPagedCallable()
    
    
    public final UnaryCallable<ListServicesRequest,AgentRegistryClient.ListServicesPagedResponse> listServicesPagedCallable()

Lists Services in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       ListServicesRequest request =
           ListServicesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Service> future =
           agentRegistryClient.listServicesPagedCallable().futureCall(request);
       // Do something.
       for (Service element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.ListServicesRequest),[ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.ListServicesPagedResponse)>` |   
  
### searchAgents(@Nullable LocationName parent)
    
    
    public final AgentRegistryClient.SearchAgentsPagedResponse searchAgents(@Nullable LocationName parent)

Searches Agents in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Agent element : agentRegistryClient.searchAgents(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.LocationName`  
Required. Parent value for SearchAgentsRequest. Format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.SearchAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.SearchAgentsPagedResponse)` |   
  
### searchAgents(SearchAgentsRequest request)
    
    
    public final AgentRegistryClient.SearchAgentsPagedResponse searchAgents(SearchAgentsRequest request)

Searches Agents in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       SearchAgentsRequest request =
           SearchAgentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSearchString("searchString120312793")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Agent element : agentRegistryClient.searchAgents(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.SearchAgentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.SearchAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.SearchAgentsPagedResponse)` |   
  
### searchAgents(String parent)
    
    
    public final AgentRegistryClient.SearchAgentsPagedResponse searchAgents(String parent)

Searches Agents in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Agent element : agentRegistryClient.searchAgents(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for SearchAgentsRequest. Format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.SearchAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.SearchAgentsPagedResponse)` |   
  
### searchAgentsCallable()
    
    
    public final UnaryCallable<SearchAgentsRequest,SearchAgentsResponse> searchAgentsCallable()

Searches Agents in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       SearchAgentsRequest request =
           SearchAgentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSearchString("searchString120312793")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         SearchAgentsResponse response = agentRegistryClient.searchAgentsCallable().call(request);
         for (Agent element : response.getAgentsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.SearchAgentsRequest),[SearchAgentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.SearchAgentsResponse)>` |   
  
### searchAgentsPagedCallable()
    
    
    public final UnaryCallable<SearchAgentsRequest,AgentRegistryClient.SearchAgentsPagedResponse> searchAgentsPagedCallable()

Searches Agents in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       SearchAgentsRequest request =
           SearchAgentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSearchString("searchString120312793")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Agent> future = agentRegistryClient.searchAgentsPagedCallable().futureCall(request);
       // Do something.
       for (Agent element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.SearchAgentsRequest),[SearchAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.SearchAgentsPagedResponse)>` |   
  
### searchMcpServers(@Nullable LocationName parent)
    
    
    public final AgentRegistryClient.SearchMcpServersPagedResponse searchMcpServers(@Nullable LocationName parent)

Searches McpServers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (McpServer element : agentRegistryClient.searchMcpServers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.agentregistry.v1.LocationName`  
Required. Parent value for SearchMcpServersRequest. Format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.SearchMcpServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.SearchMcpServersPagedResponse)` |   
  
### searchMcpServers(SearchMcpServersRequest request)
    
    
    public final AgentRegistryClient.SearchMcpServersPagedResponse searchMcpServers(SearchMcpServersRequest request)

Searches McpServers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       SearchMcpServersRequest request =
           SearchMcpServersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSearchString("searchString120312793")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (McpServer element : agentRegistryClient.searchMcpServers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchMcpServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.SearchMcpServersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.SearchMcpServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.SearchMcpServersPagedResponse)` |   
  
### searchMcpServers(String parent)
    
    
    public final AgentRegistryClient.SearchMcpServersPagedResponse searchMcpServers(String parent)

Searches McpServers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (McpServer element : agentRegistryClient.searchMcpServers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for SearchMcpServersRequest. Format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentRegistryClient.SearchMcpServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.SearchMcpServersPagedResponse)` |   
  
### searchMcpServersCallable()
    
    
    public final UnaryCallable<SearchMcpServersRequest,SearchMcpServersResponse> searchMcpServersCallable()

Searches McpServers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       SearchMcpServersRequest request =
           SearchMcpServersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSearchString("searchString120312793")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         SearchMcpServersResponse response =
             agentRegistryClient.searchMcpServersCallable().call(request);
         for (McpServer element : response.getMcpServersList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchMcpServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.SearchMcpServersRequest),[SearchMcpServersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.SearchMcpServersResponse)>` |   
  
### searchMcpServersPagedCallable()
    
    
    public final UnaryCallable<SearchMcpServersRequest,AgentRegistryClient.SearchMcpServersPagedResponse> searchMcpServersPagedCallable()

Searches McpServers in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       SearchMcpServersRequest request =
           SearchMcpServersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSearchString("searchString120312793")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<McpServer> future =
           agentRegistryClient.searchMcpServersPagedCallable().futureCall(request);
       // Do something.
       for (McpServer element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchMcpServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.SearchMcpServersRequest),[SearchMcpServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.AgentRegistryClient.SearchMcpServersPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateBindingAsync(Binding binding, FieldMask updateMask)
    
    
    public final OperationFuture<Binding,OperationMetadata> updateBindingAsync(Binding binding, FieldMask updateMask)

Updates the parameters of a single Binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       Binding binding = Binding.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Binding response = agentRegistryClient.updateBindingAsync(binding, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`binding` | `[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding)`  
Required. The Binding resource that is being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Binding resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields present in the request will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### updateBindingAsync(UpdateBindingRequest request)
    
    
    public final OperationFuture<Binding,OperationMetadata> updateBindingAsync(UpdateBindingRequest request)

Updates the parameters of a single Binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       UpdateBindingRequest request =
           UpdateBindingRequest.newBuilder()
               .setBinding(Binding.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Binding response = agentRegistryClient.updateBindingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.UpdateBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### updateBindingCallable()
    
    
    public final UnaryCallable<UpdateBindingRequest,Operation> updateBindingCallable()

Updates the parameters of a single Binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       UpdateBindingRequest request =
           UpdateBindingRequest.newBuilder()
               .setBinding(Binding.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = agentRegistryClient.updateBindingCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.UpdateBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateBindingOperationCallable()
    
    
    public final OperationCallable<UpdateBindingRequest,Binding,OperationMetadata> updateBindingOperationCallable()

Updates the parameters of a single Binding.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       UpdateBindingRequest request =
           UpdateBindingRequest.newBuilder()
               .setBinding(Binding.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Binding, OperationMetadata> future =
           agentRegistryClient.updateBindingOperationCallable().futureCall(request);
       // Do something.
       Binding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.UpdateBindingRequest),[Binding](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Binding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### updateServiceAsync(Service service, FieldMask updateMask)
    
    
    public final OperationFuture<Service,OperationMetadata> updateServiceAsync(Service service, FieldMask updateMask)

Updates the parameters of a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       Service service = Service.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Service response = agentRegistryClient.updateServiceAsync(service, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`service` | `[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Service)`  
Required. The Service resource that is being updated. Format: `projects/{project}/locations/{location}/services/{service}`.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Service resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields present in the request will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Service),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### updateServiceAsync(UpdateServiceRequest request)
    
    
    public final OperationFuture<Service,OperationMetadata> updateServiceAsync(UpdateServiceRequest request)

Updates the parameters of a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       UpdateServiceRequest request =
           UpdateServiceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setService(Service.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Service response = agentRegistryClient.updateServiceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.UpdateServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Service),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
### updateServiceCallable()
    
    
    public final UnaryCallable<UpdateServiceRequest,Operation> updateServiceCallable()

Updates the parameters of a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       UpdateServiceRequest request =
           UpdateServiceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setService(Service.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = agentRegistryClient.updateServiceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.UpdateServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateServiceOperationCallable()
    
    
    public final OperationCallable<UpdateServiceRequest,Service,OperationMetadata> updateServiceOperationCallable()

Updates the parameters of a single Service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentRegistryClient agentRegistryClient = AgentRegistryClient.create()) {
       UpdateServiceRequest request =
           UpdateServiceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setService(Service.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Service, OperationMetadata> future =
           agentRegistryClient.updateServiceOperationCallable().futureCall(request);
       // Do something.
       Service response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.UpdateServiceRequest),[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.Service),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentregistry/latest/com.google.cloud.agentregistry.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
