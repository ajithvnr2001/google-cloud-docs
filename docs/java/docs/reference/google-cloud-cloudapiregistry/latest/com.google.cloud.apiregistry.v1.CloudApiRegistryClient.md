---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient
title: Class CloudApiRegistryClient (0.18.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:13.032067+00:00
---

# Class CloudApiRegistryClient (0.18.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudApiRegistryClient (0.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.0 (latest)  0.14.0  0.13.0  0.12.0  0.10.0  0.7.0  0.6.0  0.4.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-cloudapiregistry/google-cloud-cloudapiregistry/src/main/java/com/google/cloud/apiregistry/v1/CloudApiRegistryClient.java)| [Product Reference](https://docs.cloud.google.com/api-registry/docs/overview)  
---|---  
  
Service Description: The Cloud API Registry service provides a central registry for managing API Data.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       McpServerName name =
           McpServerName.ofProjectLocationMcpServerName("[PROJECT]", "[LOCATION]", "[MCP_SERVER]");
       McpServer response = cloudApiRegistryClient.getMcpServer(name);
     }
     

Note: close() needs to be called on the CloudApiRegistryClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetMcpServer |  Gets a single McpServer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMcpServer(GetMcpServerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMcpServer(McpServerName name) 
  * getMcpServer(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMcpServerCallable() 

  
ListMcpServers |  Lists McpServers in a given Project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMcpServers(ListMcpServersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMcpServers(LocationName parent) 
  * listMcpServers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMcpServersPagedCallable() 
  * listMcpServersCallable() 

  
GetMcpTool |  Gets a single McpTool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMcpTool(GetMcpToolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMcpTool(McpToolName name) 
  * getMcpTool(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMcpToolCallable() 

  
ListMcpTools |  Lists McpTools in a given McpServer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMcpTools(ListMcpToolsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMcpTools(McpServerName parent) 
  * listMcpTools(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMcpToolsPagedCallable() 
  * listMcpToolsCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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

This class can be customized by passing in a custom instance of CloudApiRegistrySettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudApiRegistrySettings cloudApiRegistrySettings =
         CloudApiRegistrySettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CloudApiRegistryClient cloudApiRegistryClient =
         CloudApiRegistryClient.create(cloudApiRegistrySettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudApiRegistrySettings cloudApiRegistrySettings =
         CloudApiRegistrySettings.newBuilder().setEndpoint(myEndpoint).build();
     CloudApiRegistryClient cloudApiRegistryClient =
         CloudApiRegistryClient.create(cloudApiRegistrySettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudApiRegistrySettings cloudApiRegistrySettings =
         CloudApiRegistrySettings.newHttpJsonBuilder().build();
     CloudApiRegistryClient cloudApiRegistryClient =
         CloudApiRegistryClient.create(cloudApiRegistrySettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CloudApiRegistryClient

## Static Methods 

### create()
    
    
    public static final CloudApiRegistryClient create()

Constructs an instance of CloudApiRegistryClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CloudApiRegistryClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CloudApiRegistrySettings settings)
    
    
    public static final CloudApiRegistryClient create(CloudApiRegistrySettings settings)

Constructs an instance of CloudApiRegistryClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CloudApiRegistrySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistrySettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudApiRegistryClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CloudApiRegistryStub stub)
    
    
    public static final CloudApiRegistryClient create(CloudApiRegistryStub stub)

Constructs an instance of CloudApiRegistryClient, using the given stub for making calls. This is for advanced usage - prefer using create(CloudApiRegistrySettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CloudApiRegistryStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.stub.CloudApiRegistryStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudApiRegistryClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient)` |   
  
## Constructors 

### CloudApiRegistryClient(CloudApiRegistrySettings settings)
    
    
    protected CloudApiRegistryClient(CloudApiRegistrySettings settings)

Constructs an instance of CloudApiRegistryClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CloudApiRegistrySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistrySettings)`  
  
  
### CloudApiRegistryClient(CloudApiRegistryStub stub)
    
    
    protected CloudApiRegistryClient(CloudApiRegistryStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CloudApiRegistryStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.stub.CloudApiRegistryStub)`  
  
  
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

### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = cloudApiRegistryClient.getLocation(request);
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
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = cloudApiRegistryClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getMcpServer(@Nullable McpServerName name)
    
    
    public final McpServer getMcpServer(@Nullable McpServerName name)

Gets a single McpServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       McpServerName name =
           McpServerName.ofProjectLocationMcpServerName("[PROJECT]", "[LOCATION]", "[MCP_SERVER]");
       McpServer response = cloudApiRegistryClient.getMcpServer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.apiregistry.v1.McpServerName`  
Required. Name of the resource Format: projects/{project}/locations/{location}/mcpServers/{mcp_server}  
**Returns**  
---  
**Type** | **Description**  
`[McpServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.McpServer)` |   
  
### getMcpServer(GetMcpServerRequest request)
    
    
    public final McpServer getMcpServer(GetMcpServerRequest request)

Gets a single McpServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       GetMcpServerRequest request =
           GetMcpServerRequest.newBuilder()
               .setName(
                   McpServerName.ofProjectLocationMcpServerName(
                           "[PROJECT]", "[LOCATION]", "[MCP_SERVER]")
                       .toString())
               .build();
       McpServer response = cloudApiRegistryClient.getMcpServer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMcpServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.GetMcpServerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[McpServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.McpServer)` |   
  
### getMcpServer(String name)
    
    
    public final McpServer getMcpServer(String name)

Gets a single McpServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       String name =
           McpServerName.ofProjectLocationApiNamespaceMcpServerName(
                   "[PROJECT]", "[LOCATION]", "[API_NAMESPACE]", "[MCP_SERVER]")
               .toString();
       McpServer response = cloudApiRegistryClient.getMcpServer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource Format: projects/{project}/locations/{location}/mcpServers/{mcp_server}  
**Returns**  
---  
**Type** | **Description**  
`[McpServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.McpServer)` |   
  
### getMcpServerCallable()
    
    
    public final UnaryCallable<GetMcpServerRequest,McpServer> getMcpServerCallable()

Gets a single McpServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       GetMcpServerRequest request =
           GetMcpServerRequest.newBuilder()
               .setName(
                   McpServerName.ofProjectLocationMcpServerName(
                           "[PROJECT]", "[LOCATION]", "[MCP_SERVER]")
                       .toString())
               .build();
       ApiFuture<McpServer> future =
           cloudApiRegistryClient.getMcpServerCallable().futureCall(request);
       // Do something.
       McpServer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMcpServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.GetMcpServerRequest),[McpServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.McpServer)>` |   
  
### getMcpTool(@Nullable McpToolName name)
    
    
    public final McpTool getMcpTool(@Nullable McpToolName name)

Gets a single McpTool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       McpToolName name =
           McpToolName.ofProjectLocationMcpServerMcpToolName(
               "[PROJECT]", "[LOCATION]", "[MCP_SERVER]", "[MCP_TOOL]");
       McpTool response = cloudApiRegistryClient.getMcpTool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.apiregistry.v1.McpToolName`  
Required. Name of the resource Format: projects/{project}/locations/{location}/mcpServers/{mcp_server}/mcpTools/{mcp_tool}  
**Returns**  
---  
**Type** | **Description**  
`[McpTool](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.McpTool)` |   
  
### getMcpTool(GetMcpToolRequest request)
    
    
    public final McpTool getMcpTool(GetMcpToolRequest request)

Gets a single McpTool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       GetMcpToolRequest request =
           GetMcpToolRequest.newBuilder()
               .setName(
                   McpToolName.ofProjectLocationMcpServerMcpToolName(
                           "[PROJECT]", "[LOCATION]", "[MCP_SERVER]", "[MCP_TOOL]")
                       .toString())
               .build();
       McpTool response = cloudApiRegistryClient.getMcpTool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMcpToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.GetMcpToolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[McpTool](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.McpTool)` |   
  
### getMcpTool(String name)
    
    
    public final McpTool getMcpTool(String name)

Gets a single McpTool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       String name =
           McpToolName.ofProjectLocationApiNamespaceMcpServerMcpToolName(
                   "[PROJECT]", "[LOCATION]", "[API_NAMESPACE]", "[MCP_SERVER]", "[MCP_TOOL]")
               .toString();
       McpTool response = cloudApiRegistryClient.getMcpTool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource Format: projects/{project}/locations/{location}/mcpServers/{mcp_server}/mcpTools/{mcp_tool}  
**Returns**  
---  
**Type** | **Description**  
`[McpTool](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.McpTool)` |   
  
### getMcpToolCallable()
    
    
    public final UnaryCallable<GetMcpToolRequest,McpTool> getMcpToolCallable()

Gets a single McpTool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       GetMcpToolRequest request =
           GetMcpToolRequest.newBuilder()
               .setName(
                   McpToolName.ofProjectLocationMcpServerMcpToolName(
                           "[PROJECT]", "[LOCATION]", "[MCP_SERVER]", "[MCP_TOOL]")
                       .toString())
               .build();
       ApiFuture<McpTool> future = cloudApiRegistryClient.getMcpToolCallable().futureCall(request);
       // Do something.
       McpTool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMcpToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.GetMcpToolRequest),[McpTool](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.McpTool)>` |   
  
### getSettings()
    
    
    public final @Nullable CloudApiRegistrySettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.apiregistry.v1.CloudApiRegistrySettings` |   
  
### getStub()
    
    
    public CloudApiRegistryStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CloudApiRegistryStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.stub.CloudApiRegistryStub)` |   
  
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
  
### listLocations(ListLocationsRequest request)
    
    
    public final CloudApiRegistryClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : cloudApiRegistryClient.listLocations(request).iterateAll()) {
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
`[CloudApiRegistryClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             cloudApiRegistryClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,CloudApiRegistryClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           cloudApiRegistryClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient.ListLocationsPagedResponse)>` |   
  
### listMcpServers(@Nullable LocationName parent)
    
    
    public final CloudApiRegistryClient.ListMcpServersPagedResponse listMcpServers(@Nullable LocationName parent)

Lists McpServers in a given Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (McpServer element : cloudApiRegistryClient.listMcpServers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.apiregistry.v1.LocationName`  
Required. Parent value for ListMcpServersRequest  
**Returns**  
---  
**Type** | **Description**  
`[CloudApiRegistryClient.ListMcpServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient.ListMcpServersPagedResponse)` |   
  
### listMcpServers(ListMcpServersRequest request)
    
    
    public final CloudApiRegistryClient.ListMcpServersPagedResponse listMcpServers(ListMcpServersRequest request)

Lists McpServers in a given Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       ListMcpServersRequest request =
           ListMcpServersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (McpServer element : cloudApiRegistryClient.listMcpServers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMcpServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpServersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudApiRegistryClient.ListMcpServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient.ListMcpServersPagedResponse)` |   
  
### listMcpServers(String parent)
    
    
    public final CloudApiRegistryClient.ListMcpServersPagedResponse listMcpServers(String parent)

Lists McpServers in a given Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (McpServer element : cloudApiRegistryClient.listMcpServers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListMcpServersRequest  
**Returns**  
---  
**Type** | **Description**  
`[CloudApiRegistryClient.ListMcpServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient.ListMcpServersPagedResponse)` |   
  
### listMcpServersCallable()
    
    
    public final UnaryCallable<ListMcpServersRequest,ListMcpServersResponse> listMcpServersCallable()

Lists McpServers in a given Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
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
             cloudApiRegistryClient.listMcpServersCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMcpServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpServersRequest),[ListMcpServersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpServersResponse)>` |   
  
### listMcpServersPagedCallable()
    
    
    public final UnaryCallable<ListMcpServersRequest,CloudApiRegistryClient.ListMcpServersPagedResponse> listMcpServersPagedCallable()

Lists McpServers in a given Project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       ListMcpServersRequest request =
           ListMcpServersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<McpServer> future =
           cloudApiRegistryClient.listMcpServersPagedCallable().futureCall(request);
       // Do something.
       for (McpServer element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMcpServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpServersRequest),[ListMcpServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient.ListMcpServersPagedResponse)>` |   
  
### listMcpTools(@Nullable McpServerName parent)
    
    
    public final CloudApiRegistryClient.ListMcpToolsPagedResponse listMcpTools(@Nullable McpServerName parent)

Lists McpTools in a given McpServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       McpServerName parent =
           McpServerName.ofProjectLocationMcpServerName("[PROJECT]", "[LOCATION]", "[MCP_SERVER]");
       for (McpTool element : cloudApiRegistryClient.listMcpTools(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.apiregistry.v1.McpServerName`  
Required. Parent value for ListMcpToolsRequest  
**Returns**  
---  
**Type** | **Description**  
`[CloudApiRegistryClient.ListMcpToolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient.ListMcpToolsPagedResponse)` |   
  
### listMcpTools(ListMcpToolsRequest request)
    
    
    public final CloudApiRegistryClient.ListMcpToolsPagedResponse listMcpTools(ListMcpToolsRequest request)

Lists McpTools in a given McpServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       ListMcpToolsRequest request =
           ListMcpToolsRequest.newBuilder()
               .setParent(
                   McpServerName.ofProjectLocationMcpServerName(
                           "[PROJECT]", "[LOCATION]", "[MCP_SERVER]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (McpTool element : cloudApiRegistryClient.listMcpTools(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMcpToolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpToolsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudApiRegistryClient.ListMcpToolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient.ListMcpToolsPagedResponse)` |   
  
### listMcpTools(String parent)
    
    
    public final CloudApiRegistryClient.ListMcpToolsPagedResponse listMcpTools(String parent)

Lists McpTools in a given McpServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       String parent =
           McpServerName.ofProjectLocationApiNamespaceMcpServerName(
                   "[PROJECT]", "[LOCATION]", "[API_NAMESPACE]", "[MCP_SERVER]")
               .toString();
       for (McpTool element : cloudApiRegistryClient.listMcpTools(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListMcpToolsRequest  
**Returns**  
---  
**Type** | **Description**  
`[CloudApiRegistryClient.ListMcpToolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient.ListMcpToolsPagedResponse)` |   
  
### listMcpToolsCallable()
    
    
    public final UnaryCallable<ListMcpToolsRequest,ListMcpToolsResponse> listMcpToolsCallable()

Lists McpTools in a given McpServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       ListMcpToolsRequest request =
           ListMcpToolsRequest.newBuilder()
               .setParent(
                   McpServerName.ofProjectLocationMcpServerName(
                           "[PROJECT]", "[LOCATION]", "[MCP_SERVER]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListMcpToolsResponse response = cloudApiRegistryClient.listMcpToolsCallable().call(request);
         for (McpTool element : response.getMcpToolsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMcpToolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpToolsRequest),[ListMcpToolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpToolsResponse)>` |   
  
### listMcpToolsPagedCallable()
    
    
    public final UnaryCallable<ListMcpToolsRequest,CloudApiRegistryClient.ListMcpToolsPagedResponse> listMcpToolsPagedCallable()

Lists McpTools in a given McpServer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudApiRegistryClient cloudApiRegistryClient = CloudApiRegistryClient.create()) {
       ListMcpToolsRequest request =
           ListMcpToolsRequest.newBuilder()
               .setParent(
                   McpServerName.ofProjectLocationMcpServerName(
                           "[PROJECT]", "[LOCATION]", "[MCP_SERVER]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<McpTool> future =
           cloudApiRegistryClient.listMcpToolsPagedCallable().futureCall(request);
       // Do something.
       for (McpTool element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMcpToolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpToolsRequest),[ListMcpToolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryClient.ListMcpToolsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
