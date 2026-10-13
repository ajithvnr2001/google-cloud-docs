---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsClient
title: Class ToolsClient (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:34:13.739101+00:00
---

# Class ToolsClient (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ToolsClient (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow-cx/google-cloud-dialogflow-cx/src/main/java/com/google/cloud/dialogflow/cx/v3/ToolsClient.java)| [Product Reference](https://cloud.google.com/dialogflow/cx/docs)| [REST Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Service for managing Tools.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       AgentName parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       Tool tool = Tool.newBuilder().build();
       Tool response = toolsClient.createTool(parent, tool);
     }
     

Note: close() needs to be called on the ToolsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateTool |  Creates a Tool in the specified agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTool(CreateToolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createTool(AgentName parent, Tool tool) 
  * createTool(String parent, Tool tool) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createToolCallable() 

  
ListTools |  Returns a list of Tools in the specified agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTools(ListToolsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTools(AgentName parent) 
  * listTools(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listToolsPagedCallable() 
  * listToolsCallable() 

  
GetTool |  Retrieves the specified Tool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTool(GetToolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTool(ToolName name) 
  * getTool(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getToolCallable() 

  
UpdateTool |  Update the specified Tool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTool(UpdateToolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateTool(Tool tool, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateToolCallable() 

  
DeleteTool |  Deletes a specified Tool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTool(DeleteToolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteTool(ToolName name) 
  * deleteTool(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteToolCallable() 

  
ListToolVersions |  List versions of the specified Tool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listToolVersions(ListToolVersionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listToolVersions(ToolName parent) 
  * listToolVersions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listToolVersionsPagedCallable() 
  * listToolVersionsCallable() 

  
CreateToolVersion |  Creates a version for the specified Tool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createToolVersion(CreateToolVersionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createToolVersion(ToolName parent, ToolVersion toolVersion) 
  * createToolVersion(String parent, ToolVersion toolVersion) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createToolVersionCallable() 

  
GetToolVersion |  Retrieves the specified version of the Tool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getToolVersion(GetToolVersionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getToolVersion(ToolVersionName name) 
  * getToolVersion(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getToolVersionCallable() 

  
DeleteToolVersion |  Deletes the specified version of the Tool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteToolVersion(DeleteToolVersionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteToolVersion(ToolVersionName name) 
  * deleteToolVersion(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteToolVersionCallable() 

  
RestoreToolVersion |  Retrieves the specified version of the Tool and stores it as the current tool draft, returning the tool with resources updated. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restoreToolVersion(RestoreToolVersionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * restoreToolVersion(ToolVersionName name) 
  * restoreToolVersion(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restoreToolVersionCallable() 

  
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

This class can be customized by passing in a custom instance of ToolsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ToolsSettings toolsSettings =
         ToolsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ToolsClient toolsClient = ToolsClient.create(toolsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ToolsSettings toolsSettings = ToolsSettings.newBuilder().setEndpoint(myEndpoint).build();
     ToolsClient toolsClient = ToolsClient.create(toolsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ToolsSettings toolsSettings = ToolsSettings.newHttpJsonBuilder().build();
     ToolsClient toolsClient = ToolsClient.create(toolsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ToolsClient

## Static Methods 

### create()
    
    
    public static final ToolsClient create()

Constructs an instance of ToolsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ToolsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ToolsSettings settings)
    
    
    public static final ToolsClient create(ToolsSettings settings)

Constructs an instance of ToolsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ToolsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ToolsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ToolsStub stub)
    
    
    public static final ToolsClient create(ToolsStub stub)

Constructs an instance of ToolsClient, using the given stub for making calls. This is for advanced usage - prefer using create(ToolsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ToolsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.ToolsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ToolsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsClient)` |   
  
## Constructors 

### ToolsClient(ToolsSettings settings)
    
    
    protected ToolsClient(ToolsSettings settings)

Constructs an instance of ToolsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ToolsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsSettings)`  
  
  
### ToolsClient(ToolsStub stub)
    
    
    protected ToolsClient(ToolsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ToolsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.ToolsStub)`  
  
  
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

### createTool(@Nullable AgentName parent, Tool tool)
    
    
    public final Tool createTool(@Nullable AgentName parent, Tool tool)

Creates a Tool in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       AgentName parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       Tool tool = Tool.newBuilder().build();
       Tool response = toolsClient.createTool(parent, tool);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.AgentName`  
Required. The agent to create a Tool for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`tool` | `[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Tool)`  
Required. The Tool to be created.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Tool)` |   
  
### createTool(CreateToolRequest request)
    
    
    public final Tool createTool(CreateToolRequest request)

Creates a Tool in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       CreateToolRequest request =
           CreateToolRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setTool(Tool.newBuilder().build())
               .build();
       Tool response = toolsClient.createTool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreateToolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Tool)` |   
  
### createTool(String parent, Tool tool)
    
    
    public final Tool createTool(String parent, Tool tool)

Creates a Tool in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       String parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString();
       Tool tool = Tool.newBuilder().build();
       Tool response = toolsClient.createTool(parent, tool);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The agent to create a Tool for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`tool` | `[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Tool)`  
Required. The Tool to be created.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Tool)` |   
  
### createToolCallable()
    
    
    public final UnaryCallable<CreateToolRequest,Tool> createToolCallable()

Creates a Tool in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       CreateToolRequest request =
           CreateToolRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setTool(Tool.newBuilder().build())
               .build();
       ApiFuture<Tool> future = toolsClient.createToolCallable().futureCall(request);
       // Do something.
       Tool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreateToolRequest),[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Tool)>` |   
  
### createToolVersion(@Nullable ToolName parent, ToolVersion toolVersion)
    
    
    public final ToolVersion createToolVersion(@Nullable ToolName parent, ToolVersion toolVersion)

Creates a version for the specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       ToolName parent = ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]");
       ToolVersion toolVersion = ToolVersion.newBuilder().build();
       ToolVersion response = toolsClient.createToolVersion(parent, toolVersion);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.ToolName`  
Required. The tool to create a version for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>`.  
`toolVersion` | `[ToolVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolVersion)`  
Required. The tool version to create.  
**Returns**  
---  
**Type** | **Description**  
`[ToolVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolVersion)` |   
  
### createToolVersion(CreateToolVersionRequest request)
    
    
    public final ToolVersion createToolVersion(CreateToolVersionRequest request)

Creates a version for the specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       CreateToolVersionRequest request =
           CreateToolVersionRequest.newBuilder()
               .setParent(ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]").toString())
               .setToolVersion(ToolVersion.newBuilder().build())
               .build();
       ToolVersion response = toolsClient.createToolVersion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateToolVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreateToolVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ToolVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolVersion)` |   
  
### createToolVersion(String parent, ToolVersion toolVersion)
    
    
    public final ToolVersion createToolVersion(String parent, ToolVersion toolVersion)

Creates a version for the specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       String parent = ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]").toString();
       ToolVersion toolVersion = ToolVersion.newBuilder().build();
       ToolVersion response = toolsClient.createToolVersion(parent, toolVersion);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The tool to create a version for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>`.  
`toolVersion` | `[ToolVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolVersion)`  
Required. The tool version to create.  
**Returns**  
---  
**Type** | **Description**  
`[ToolVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolVersion)` |   
  
### createToolVersionCallable()
    
    
    public final UnaryCallable<CreateToolVersionRequest,ToolVersion> createToolVersionCallable()

Creates a version for the specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       CreateToolVersionRequest request =
           CreateToolVersionRequest.newBuilder()
               .setParent(ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]").toString())
               .setToolVersion(ToolVersion.newBuilder().build())
               .build();
       ApiFuture<ToolVersion> future = toolsClient.createToolVersionCallable().futureCall(request);
       // Do something.
       ToolVersion response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateToolVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreateToolVersionRequest),[ToolVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolVersion)>` |   
  
### deleteTool(@Nullable ToolName name)
    
    
    public final void deleteTool(@Nullable ToolName name)

Deletes a specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       ToolName name = ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]");
       toolsClient.deleteTool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.ToolName`  
Required. The name of the Tool to be deleted. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>`.  
  
### deleteTool(DeleteToolRequest request)
    
    
    public final void deleteTool(DeleteToolRequest request)

Deletes a specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       DeleteToolRequest request =
           DeleteToolRequest.newBuilder()
               .setName(ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]").toString())
               .setForce(true)
               .build();
       toolsClient.deleteTool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeleteToolRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteTool(String name)
    
    
    public final void deleteTool(String name)

Deletes a specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       String name = ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]").toString();
       toolsClient.deleteTool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Tool to be deleted. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>`.  
  
### deleteToolCallable()
    
    
    public final UnaryCallable<DeleteToolRequest,Empty> deleteToolCallable()

Deletes a specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       DeleteToolRequest request =
           DeleteToolRequest.newBuilder()
               .setName(ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]").toString())
               .setForce(true)
               .build();
       ApiFuture<Empty> future = toolsClient.deleteToolCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeleteToolRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteToolVersion(@Nullable ToolVersionName name)
    
    
    public final void deleteToolVersion(@Nullable ToolVersionName name)

Deletes the specified version of the Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       ToolVersionName name =
           ToolVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]", "[VERSION]");
       toolsClient.deleteToolVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.ToolVersionName`  
Required. The name of the tool version to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>/versions/<VersionID>`.  
  
### deleteToolVersion(DeleteToolVersionRequest request)
    
    
    public final void deleteToolVersion(DeleteToolVersionRequest request)

Deletes the specified version of the Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       DeleteToolVersionRequest request =
           DeleteToolVersionRequest.newBuilder()
               .setName(
                   ToolVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]", "[VERSION]")
                       .toString())
               .setForce(true)
               .build();
       toolsClient.deleteToolVersion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteToolVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeleteToolVersionRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteToolVersion(String name)
    
    
    public final void deleteToolVersion(String name)

Deletes the specified version of the Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       String name =
           ToolVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]", "[VERSION]")
               .toString();
       toolsClient.deleteToolVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the tool version to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>/versions/<VersionID>`.  
  
### deleteToolVersionCallable()
    
    
    public final UnaryCallable<DeleteToolVersionRequest,Empty> deleteToolVersionCallable()

Deletes the specified version of the Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       DeleteToolVersionRequest request =
           DeleteToolVersionRequest.newBuilder()
               .setName(
                   ToolVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]", "[VERSION]")
                       .toString())
               .setForce(true)
               .build();
       ApiFuture<Empty> future = toolsClient.deleteToolVersionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteToolVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeleteToolVersionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = toolsClient.getLocation(request);
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
     try (ToolsClient toolsClient = ToolsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = toolsClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable ToolsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.ToolsSettings` |   
  
### getStub()
    
    
    public ToolsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ToolsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.ToolsStub)` |   
  
### getTool(@Nullable ToolName name)
    
    
    public final Tool getTool(@Nullable ToolName name)

Retrieves the specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       ToolName name = ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]");
       Tool response = toolsClient.getTool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.ToolName`  
Required. The name of the Tool. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Tool)` |   
  
### getTool(GetToolRequest request)
    
    
    public final Tool getTool(GetToolRequest request)

Retrieves the specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       GetToolRequest request =
           GetToolRequest.newBuilder()
               .setName(ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]").toString())
               .build();
       Tool response = toolsClient.getTool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetToolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Tool)` |   
  
### getTool(String name)
    
    
    public final Tool getTool(String name)

Retrieves the specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       String name = ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]").toString();
       Tool response = toolsClient.getTool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Tool. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Tool)` |   
  
### getToolCallable()
    
    
    public final UnaryCallable<GetToolRequest,Tool> getToolCallable()

Retrieves the specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       GetToolRequest request =
           GetToolRequest.newBuilder()
               .setName(ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]").toString())
               .build();
       ApiFuture<Tool> future = toolsClient.getToolCallable().futureCall(request);
       // Do something.
       Tool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetToolRequest),[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Tool)>` |   
  
### getToolVersion(@Nullable ToolVersionName name)
    
    
    public final ToolVersion getToolVersion(@Nullable ToolVersionName name)

Retrieves the specified version of the Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       ToolVersionName name =
           ToolVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]", "[VERSION]");
       ToolVersion response = toolsClient.getToolVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.ToolVersionName`  
Required. The name of the tool version. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>/versions/<VersionID>`.  
**Returns**  
---  
**Type** | **Description**  
`[ToolVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolVersion)` |   
  
### getToolVersion(GetToolVersionRequest request)
    
    
    public final ToolVersion getToolVersion(GetToolVersionRequest request)

Retrieves the specified version of the Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       GetToolVersionRequest request =
           GetToolVersionRequest.newBuilder()
               .setName(
                   ToolVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]", "[VERSION]")
                       .toString())
               .build();
       ToolVersion response = toolsClient.getToolVersion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetToolVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetToolVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ToolVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolVersion)` |   
  
### getToolVersion(String name)
    
    
    public final ToolVersion getToolVersion(String name)

Retrieves the specified version of the Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       String name =
           ToolVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]", "[VERSION]")
               .toString();
       ToolVersion response = toolsClient.getToolVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the tool version. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>/versions/<VersionID>`.  
**Returns**  
---  
**Type** | **Description**  
`[ToolVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolVersion)` |   
  
### getToolVersionCallable()
    
    
    public final UnaryCallable<GetToolVersionRequest,ToolVersion> getToolVersionCallable()

Retrieves the specified version of the Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       GetToolVersionRequest request =
           GetToolVersionRequest.newBuilder()
               .setName(
                   ToolVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]", "[VERSION]")
                       .toString())
               .build();
       ApiFuture<ToolVersion> future = toolsClient.getToolVersionCallable().futureCall(request);
       // Do something.
       ToolVersion response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetToolVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetToolVersionRequest),[ToolVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolVersion)>` |   
  
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
    
    
    public final ToolsClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : toolsClient.listLocations(request).iterateAll()) {
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
`[ToolsClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsClient.ListLocationsPagedResponse)` |   
  
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
     try (ToolsClient toolsClient = ToolsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = toolsClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,ToolsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future = toolsClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsClient.ListLocationsPagedResponse)>` |   
  
### listToolVersions(@Nullable ToolName parent)
    
    
    public final ToolsClient.ListToolVersionsPagedResponse listToolVersions(@Nullable ToolName parent)

List versions of the specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       ToolName parent = ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]");
       for (ToolVersion element : toolsClient.listToolVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.ToolName`  
Required. The parent of the tool versions. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>`.  
**Returns**  
---  
**Type** | **Description**  
`[ToolsClient.ListToolVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsClient.ListToolVersionsPagedResponse)` |   
  
### listToolVersions(ListToolVersionsRequest request)
    
    
    public final ToolsClient.ListToolVersionsPagedResponse listToolVersions(ListToolVersionsRequest request)

List versions of the specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       ListToolVersionsRequest request =
           ListToolVersionsRequest.newBuilder()
               .setParent(ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ToolVersion element : toolsClient.listToolVersions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListToolVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListToolVersionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ToolsClient.ListToolVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsClient.ListToolVersionsPagedResponse)` |   
  
### listToolVersions(String parent)
    
    
    public final ToolsClient.ListToolVersionsPagedResponse listToolVersions(String parent)

List versions of the specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       String parent = ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]").toString();
       for (ToolVersion element : toolsClient.listToolVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the tool versions. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>`.  
**Returns**  
---  
**Type** | **Description**  
`[ToolsClient.ListToolVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsClient.ListToolVersionsPagedResponse)` |   
  
### listToolVersionsCallable()
    
    
    public final UnaryCallable<ListToolVersionsRequest,ListToolVersionsResponse> listToolVersionsCallable()

List versions of the specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       ListToolVersionsRequest request =
           ListToolVersionsRequest.newBuilder()
               .setParent(ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListToolVersionsResponse response = toolsClient.listToolVersionsCallable().call(request);
         for (ToolVersion element : response.getToolVersionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListToolVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListToolVersionsRequest),[ListToolVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListToolVersionsResponse)>` |   
  
### listToolVersionsPagedCallable()
    
    
    public final UnaryCallable<ListToolVersionsRequest,ToolsClient.ListToolVersionsPagedResponse> listToolVersionsPagedCallable()

List versions of the specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       ListToolVersionsRequest request =
           ListToolVersionsRequest.newBuilder()
               .setParent(ToolName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ToolVersion> future =
           toolsClient.listToolVersionsPagedCallable().futureCall(request);
       // Do something.
       for (ToolVersion element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListToolVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListToolVersionsRequest),[ListToolVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsClient.ListToolVersionsPagedResponse)>` |   
  
### listTools(@Nullable AgentName parent)
    
    
    public final ToolsClient.ListToolsPagedResponse listTools(@Nullable AgentName parent)

Returns a list of Tools in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       AgentName parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       for (Tool element : toolsClient.listTools(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.AgentName`  
Required. The agent to list the Tools from. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[ToolsClient.ListToolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsClient.ListToolsPagedResponse)` |   
  
### listTools(ListToolsRequest request)
    
    
    public final ToolsClient.ListToolsPagedResponse listTools(ListToolsRequest request)

Returns a list of Tools in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       ListToolsRequest request =
           ListToolsRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Tool element : toolsClient.listTools(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListToolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListToolsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ToolsClient.ListToolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsClient.ListToolsPagedResponse)` |   
  
### listTools(String parent)
    
    
    public final ToolsClient.ListToolsPagedResponse listTools(String parent)

Returns a list of Tools in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       String parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString();
       for (Tool element : toolsClient.listTools(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The agent to list the Tools from. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[ToolsClient.ListToolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsClient.ListToolsPagedResponse)` |   
  
### listToolsCallable()
    
    
    public final UnaryCallable<ListToolsRequest,ListToolsResponse> listToolsCallable()

Returns a list of Tools in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       ListToolsRequest request =
           ListToolsRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListToolsResponse response = toolsClient.listToolsCallable().call(request);
         for (Tool element : response.getToolsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListToolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListToolsRequest),[ListToolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListToolsResponse)>` |   
  
### listToolsPagedCallable()
    
    
    public final UnaryCallable<ListToolsRequest,ToolsClient.ListToolsPagedResponse> listToolsPagedCallable()

Returns a list of Tools in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       ListToolsRequest request =
           ListToolsRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Tool> future = toolsClient.listToolsPagedCallable().futureCall(request);
       // Do something.
       for (Tool element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListToolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListToolsRequest),[ListToolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ToolsClient.ListToolsPagedResponse)>` |   
  
### restoreToolVersion(@Nullable ToolVersionName name)
    
    
    public final RestoreToolVersionResponse restoreToolVersion(@Nullable ToolVersionName name)

Retrieves the specified version of the Tool and stores it as the current tool draft, returning the tool with resources updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       ToolVersionName name =
           ToolVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]", "[VERSION]");
       RestoreToolVersionResponse response = toolsClient.restoreToolVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.ToolVersionName`  
Required. The name of the tool version. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>/versions/<VersionID>`.  
**Returns**  
---  
**Type** | **Description**  
`[RestoreToolVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestoreToolVersionResponse)` |   
  
### restoreToolVersion(RestoreToolVersionRequest request)
    
    
    public final RestoreToolVersionResponse restoreToolVersion(RestoreToolVersionRequest request)

Retrieves the specified version of the Tool and stores it as the current tool draft, returning the tool with resources updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       RestoreToolVersionRequest request =
           RestoreToolVersionRequest.newBuilder()
               .setName(
                   ToolVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]", "[VERSION]")
                       .toString())
               .build();
       RestoreToolVersionResponse response = toolsClient.restoreToolVersion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestoreToolVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestoreToolVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RestoreToolVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestoreToolVersionResponse)` |   
  
### restoreToolVersion(String name)
    
    
    public final RestoreToolVersionResponse restoreToolVersion(String name)

Retrieves the specified version of the Tool and stores it as the current tool draft, returning the tool with resources updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       String name =
           ToolVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]", "[VERSION]")
               .toString();
       RestoreToolVersionResponse response = toolsClient.restoreToolVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the tool version. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>/versions/<VersionID>`.  
**Returns**  
---  
**Type** | **Description**  
`[RestoreToolVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestoreToolVersionResponse)` |   
  
### restoreToolVersionCallable()
    
    
    public final UnaryCallable<RestoreToolVersionRequest,RestoreToolVersionResponse> restoreToolVersionCallable()

Retrieves the specified version of the Tool and stores it as the current tool draft, returning the tool with resources updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       RestoreToolVersionRequest request =
           RestoreToolVersionRequest.newBuilder()
               .setName(
                   ToolVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[TOOL]", "[VERSION]")
                       .toString())
               .build();
       ApiFuture<RestoreToolVersionResponse> future =
           toolsClient.restoreToolVersionCallable().futureCall(request);
       // Do something.
       RestoreToolVersionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RestoreToolVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestoreToolVersionRequest),[RestoreToolVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestoreToolVersionResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateTool(Tool tool, FieldMask updateMask)
    
    
    public final Tool updateTool(Tool tool, FieldMask updateMask)

Update the specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       Tool tool = Tool.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Tool response = toolsClient.updateTool(tool, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tool` | `[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Tool)`  
Required. The Tool to be updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The mask to control which fields get updated. If the mask is not present, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Tool)` |   
  
### updateTool(UpdateToolRequest request)
    
    
    public final Tool updateTool(UpdateToolRequest request)

Update the specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       UpdateToolRequest request =
           UpdateToolRequest.newBuilder()
               .setTool(Tool.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Tool response = toolsClient.updateTool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateToolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Tool)` |   
  
### updateToolCallable()
    
    
    public final UnaryCallable<UpdateToolRequest,Tool> updateToolCallable()

Update the specified Tool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ToolsClient toolsClient = ToolsClient.create()) {
       UpdateToolRequest request =
           UpdateToolRequest.newBuilder()
               .setTool(Tool.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Tool> future = toolsClient.updateToolCallable().futureCall(request);
       // Do something.
       Tool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateToolRequest),[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Tool)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
