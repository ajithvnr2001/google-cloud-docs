---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient
title: Class AgentsClient (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:33:57.335659+00:00
---

# Class AgentsClient (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AgentsClient (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow-cx/google-cloud-dialogflow-cx/src/main/java/com/google/cloud/dialogflow/cx/v3/AgentsClient.java)| [Product Reference](https://cloud.google.com/dialogflow/cx/docs)| [REST Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Service for managing Agents.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       AgentName name = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       Agent response = agentsClient.getAgent(name);
     }
     

Note: close() needs to be called on the AgentsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListAgents |  Returns the list of all agents in the specified location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAgents(ListAgentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAgents(LocationName parent) 
  * listAgents(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAgentsPagedCallable() 
  * listAgentsCallable() 

  
GetAgent |  Retrieves the specified agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAgent(GetAgentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAgent(AgentName name) 
  * getAgent(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAgentCallable() 

  
CreateAgent |  Creates an agent in the specified location.  Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAgent(CreateAgentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createAgent(LocationName parent, Agent agent) 
  * createAgent(String parent, Agent agent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAgentCallable() 

  
UpdateAgent |  Updates the specified agent.  Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAgent(UpdateAgentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateAgent(Agent agent, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAgentCallable() 

  
DeleteAgent |  Deletes the specified agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAgent(DeleteAgentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteAgent(AgentName name) 
  * deleteAgent(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAgentCallable() 

  
ExportAgent |  Exports the specified agent to a binary file.  This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:  \- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) \- `response`: ExportAgentResponse |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportAgentAsync(ExportAgentRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportAgentOperationCallable() 
  * exportAgentCallable() 

  
RestoreAgent |  Restores the specified agent from a binary file.  Replaces the current agent with a new one. Note that all existing resources in agent (e.g. intents, entity types, flows) will be removed.  This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:  \- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) \- `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restoreAgentAsync(RestoreAgentRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restoreAgentOperationCallable() 
  * restoreAgentCallable() 

  
ValidateAgent |  Validates the specified agent and creates or updates validation results. The agent in draft version is validated. Please call this API after the training is completed to get the complete validation results. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * validateAgent(ValidateAgentRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * validateAgentCallable() 

  
GetAgentValidationResult |  Gets the latest agent validation result. Agent validation is performed when ValidateAgent is called. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAgentValidationResult(GetAgentValidationResultRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAgentValidationResult(AgentValidationResultName name) 
  * getAgentValidationResult(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAgentValidationResultCallable() 

  
GetGenerativeSettings |  Gets the generative settings for the agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getGenerativeSettings(GetGenerativeSettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getGenerativeSettings(AgentGenerativeSettingsName name, String languageCode) 
  * getGenerativeSettings(String name, String languageCode) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getGenerativeSettingsCallable() 

  
UpdateGenerativeSettings |  Updates the generative settings for the agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateGenerativeSettings(UpdateGenerativeSettingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateGenerativeSettings(GenerativeSettings generativeSettings, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateGenerativeSettingsCallable() 

  
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

This class can be customized by passing in a custom instance of AgentsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AgentsSettings agentsSettings =
         AgentsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AgentsClient agentsClient = AgentsClient.create(agentsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AgentsSettings agentsSettings = AgentsSettings.newBuilder().setEndpoint(myEndpoint).build();
     AgentsClient agentsClient = AgentsClient.create(agentsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AgentsSettings agentsSettings = AgentsSettings.newHttpJsonBuilder().build();
     AgentsClient agentsClient = AgentsClient.create(agentsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AgentsClient

## Static Methods 

### create()
    
    
    public static final AgentsClient create()

Constructs an instance of AgentsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AgentsSettings settings)
    
    
    public static final AgentsClient create(AgentsSettings settings)

Constructs an instance of AgentsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AgentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AgentsStub stub)
    
    
    public static final AgentsClient create(AgentsStub stub)

Constructs an instance of AgentsClient, using the given stub for making calls. This is for advanced usage - prefer using create(AgentsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AgentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.AgentsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient)` |   
  
## Constructors 

### AgentsClient(AgentsSettings settings)
    
    
    protected AgentsClient(AgentsSettings settings)

Constructs an instance of AgentsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AgentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsSettings)`  
  
  
### AgentsClient(AgentsStub stub)
    
    
    protected AgentsClient(AgentsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AgentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.AgentsStub)`  
  
  
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

### createAgent(@Nullable LocationName parent, Agent agent)
    
    
    public final Agent createAgent(@Nullable LocationName parent, Agent agent)

Creates an agent in the specified location.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Agent agent = Agent.newBuilder().build();
       Agent response = agentsClient.createAgent(parent, agent);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.LocationName`  
Required. The location to create a agent for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
`agent` | `[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent)`  
Required. The agent to create.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent)` |   
  
### createAgent(CreateAgentRequest request)
    
    
    public final Agent createAgent(CreateAgentRequest request)

Creates an agent in the specified location.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       CreateAgentRequest request =
           CreateAgentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAgent(Agent.newBuilder().build())
               .build();
       Agent response = agentsClient.createAgent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreateAgentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent)` |   
  
### createAgent(String parent, Agent agent)
    
    
    public final Agent createAgent(String parent, Agent agent)

Creates an agent in the specified location.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Agent agent = Agent.newBuilder().build();
       Agent response = agentsClient.createAgent(parent, agent);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location to create a agent for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
`agent` | `[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent)`  
Required. The agent to create.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent)` |   
  
### createAgentCallable()
    
    
    public final UnaryCallable<CreateAgentRequest,Agent> createAgentCallable()

Creates an agent in the specified location.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       CreateAgentRequest request =
           CreateAgentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAgent(Agent.newBuilder().build())
               .build();
       ApiFuture<Agent> future = agentsClient.createAgentCallable().futureCall(request);
       // Do something.
       Agent response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreateAgentRequest),[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent)>` |   
  
### deleteAgent(@Nullable AgentName name)
    
    
    public final void deleteAgent(@Nullable AgentName name)

Deletes the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       AgentName name = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       agentsClient.deleteAgent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.AgentName`  
Required. The name of the agent to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
  
### deleteAgent(DeleteAgentRequest request)
    
    
    public final void deleteAgent(DeleteAgentRequest request)

Deletes the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       DeleteAgentRequest request =
           DeleteAgentRequest.newBuilder()
               .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .build();
       agentsClient.deleteAgent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeleteAgentRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteAgent(String name)
    
    
    public final void deleteAgent(String name)

Deletes the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       String name = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString();
       agentsClient.deleteAgent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the agent to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
  
### deleteAgentCallable()
    
    
    public final UnaryCallable<DeleteAgentRequest,Empty> deleteAgentCallable()

Deletes the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       DeleteAgentRequest request =
           DeleteAgentRequest.newBuilder()
               .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .build();
       ApiFuture<Empty> future = agentsClient.deleteAgentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeleteAgentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### exportAgentAsync(ExportAgentRequest request)
    
    
    public final OperationFuture<ExportAgentResponse,Struct> exportAgentAsync(ExportAgentRequest request)

Exports the specified agent to a binary file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: ExportAgentResponse

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (AgentsClient agentsClient = AgentsClient.create()) {
        ExportAgentRequest request =
            ExportAgentRequest.newBuilder()
                .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
                .setAgentUri("agentUri1469149223")
                .setEnvironment(
                    EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                        .toString())
                .setGitDestination(ExportAgentRequest.GitDestination.newBuilder().build())
                .setIncludeBigqueryExportSettings(true)
                .build();
        ExportAgentResponse response = agentsClient.exportAgentAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportAgentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportAgentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportAgentResponse),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### exportAgentCallable()
    
    
    public final UnaryCallable<ExportAgentRequest,Operation> exportAgentCallable()

Exports the specified agent to a binary file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: ExportAgentResponse

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (AgentsClient agentsClient = AgentsClient.create()) {
        ExportAgentRequest request =
            ExportAgentRequest.newBuilder()
                .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
                .setAgentUri("agentUri1469149223")
                .setEnvironment(
                    EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                        .toString())
                .setGitDestination(ExportAgentRequest.GitDestination.newBuilder().build())
                .setIncludeBigqueryExportSettings(true)
                .build();
        ApiFuture<Operation> future = agentsClient.exportAgentCallable().futureCall(request);
        // Do something.
        Operation response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportAgentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportAgentOperationCallable()
    
    
    public final OperationCallable<ExportAgentRequest,ExportAgentResponse,Struct> exportAgentOperationCallable()

Exports the specified agent to a binary file.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: ExportAgentResponse

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (AgentsClient agentsClient = AgentsClient.create()) {
        ExportAgentRequest request =
            ExportAgentRequest.newBuilder()
                .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
                .setAgentUri("agentUri1469149223")
                .setEnvironment(
                    EnvironmentName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[ENVIRONMENT]")
                        .toString())
                .setGitDestination(ExportAgentRequest.GitDestination.newBuilder().build())
                .setIncludeBigqueryExportSettings(true)
                .build();
        OperationFuture<ExportAgentResponse, Struct> future =
            agentsClient.exportAgentOperationCallable().futureCall(request);
        // Do something.
        ExportAgentResponse response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportAgentRequest),[ExportAgentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportAgentResponse),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### getAgent(@Nullable AgentName name)
    
    
    public final Agent getAgent(@Nullable AgentName name)

Retrieves the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       AgentName name = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       Agent response = agentsClient.getAgent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.AgentName`  
Required. The name of the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent)` |   
  
### getAgent(GetAgentRequest request)
    
    
    public final Agent getAgent(GetAgentRequest request)

Retrieves the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       GetAgentRequest request =
           GetAgentRequest.newBuilder()
               .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .build();
       Agent response = agentsClient.getAgent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetAgentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent)` |   
  
### getAgent(String name)
    
    
    public final Agent getAgent(String name)

Retrieves the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       String name = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString();
       Agent response = agentsClient.getAgent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent)` |   
  
### getAgentCallable()
    
    
    public final UnaryCallable<GetAgentRequest,Agent> getAgentCallable()

Retrieves the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       GetAgentRequest request =
           GetAgentRequest.newBuilder()
               .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .build();
       ApiFuture<Agent> future = agentsClient.getAgentCallable().futureCall(request);
       // Do something.
       Agent response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetAgentRequest),[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent)>` |   
  
### getAgentValidationResult(@Nullable AgentValidationResultName name)
    
    
    public final AgentValidationResult getAgentValidationResult(@Nullable AgentValidationResultName name)

Gets the latest agent validation result. Agent validation is performed when ValidateAgent is called.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       AgentValidationResultName name =
           AgentValidationResultName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       AgentValidationResult response = agentsClient.getAgentValidationResult(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.AgentValidationResultName`  
Required. The agent name. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/validationResult`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentValidationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentValidationResult)` |   
  
### getAgentValidationResult(GetAgentValidationResultRequest request)
    
    
    public final AgentValidationResult getAgentValidationResult(GetAgentValidationResultRequest request)

Gets the latest agent validation result. Agent validation is performed when ValidateAgent is called.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       GetAgentValidationResultRequest request =
           GetAgentValidationResultRequest.newBuilder()
               .setName(
                   AgentValidationResultName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setLanguageCode("languageCode-2092349083")
               .build();
       AgentValidationResult response = agentsClient.getAgentValidationResult(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAgentValidationResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetAgentValidationResultRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentValidationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentValidationResult)` |   
  
### getAgentValidationResult(String name)
    
    
    public final AgentValidationResult getAgentValidationResult(String name)

Gets the latest agent validation result. Agent validation is performed when ValidateAgent is called.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       String name = AgentValidationResultName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString();
       AgentValidationResult response = agentsClient.getAgentValidationResult(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The agent name. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/validationResult`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentValidationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentValidationResult)` |   
  
### getAgentValidationResultCallable()
    
    
    public final UnaryCallable<GetAgentValidationResultRequest,AgentValidationResult> getAgentValidationResultCallable()

Gets the latest agent validation result. Agent validation is performed when ValidateAgent is called.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       GetAgentValidationResultRequest request =
           GetAgentValidationResultRequest.newBuilder()
               .setName(
                   AgentValidationResultName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<AgentValidationResult> future =
           agentsClient.getAgentValidationResultCallable().futureCall(request);
       // Do something.
       AgentValidationResult response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAgentValidationResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetAgentValidationResultRequest),[AgentValidationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentValidationResult)>` |   
  
### getGenerativeSettings(@Nullable AgentGenerativeSettingsName name, String languageCode)
    
    
    public final GenerativeSettings getGenerativeSettings(@Nullable AgentGenerativeSettingsName name, String languageCode)

Gets the generative settings for the agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       AgentGenerativeSettingsName name =
           AgentGenerativeSettingsName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       String languageCode = "languageCode-2092349083";
       GenerativeSettings response = agentsClient.getGenerativeSettings(name, languageCode);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.AgentGenerativeSettingsName`  
Required. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generativeSettings`.  
`languageCode` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Language code of the generative settings.  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GenerativeSettings)` |   
  
### getGenerativeSettings(GetGenerativeSettingsRequest request)
    
    
    public final GenerativeSettings getGenerativeSettings(GetGenerativeSettingsRequest request)

Gets the generative settings for the agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       GetGenerativeSettingsRequest request =
           GetGenerativeSettingsRequest.newBuilder()
               .setName(
                   AgentGenerativeSettingsName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setLanguageCode("languageCode-2092349083")
               .build();
       GenerativeSettings response = agentsClient.getGenerativeSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGenerativeSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetGenerativeSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GenerativeSettings)` |   
  
### getGenerativeSettings(String name, String languageCode)
    
    
    public final GenerativeSettings getGenerativeSettings(String name, String languageCode)

Gets the generative settings for the agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       String name = AgentGenerativeSettingsName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString();
       String languageCode = "languageCode-2092349083";
       GenerativeSettings response = agentsClient.getGenerativeSettings(name, languageCode);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generativeSettings`.  
`languageCode` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Language code of the generative settings.  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GenerativeSettings)` |   
  
### getGenerativeSettingsCallable()
    
    
    public final UnaryCallable<GetGenerativeSettingsRequest,GenerativeSettings> getGenerativeSettingsCallable()

Gets the generative settings for the agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       GetGenerativeSettingsRequest request =
           GetGenerativeSettingsRequest.newBuilder()
               .setName(
                   AgentGenerativeSettingsName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<GenerativeSettings> future =
           agentsClient.getGenerativeSettingsCallable().futureCall(request);
       // Do something.
       GenerativeSettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGenerativeSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetGenerativeSettingsRequest),[GenerativeSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GenerativeSettings)>` |   
  
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
     try (AgentsClient agentsClient = AgentsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = agentsClient.getLocation(request);
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
     try (AgentsClient agentsClient = AgentsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = agentsClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable AgentsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.AgentsSettings` |   
  
### getStub()
    
    
    public AgentsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AgentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.AgentsStub)` |   
  
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
    
    
    public final AgentsClient.ListAgentsPagedResponse listAgents(@Nullable LocationName parent)

Returns the list of all agents in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Agent element : agentsClient.listAgents(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.LocationName`  
Required. The location to list all agents for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentsClient.ListAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient.ListAgentsPagedResponse)` |   
  
### listAgents(ListAgentsRequest request)
    
    
    public final AgentsClient.ListAgentsPagedResponse listAgents(ListAgentsRequest request)

Returns the list of all agents in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       ListAgentsRequest request =
           ListAgentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Agent element : agentsClient.listAgents(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListAgentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentsClient.ListAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient.ListAgentsPagedResponse)` |   
  
### listAgents(String parent)
    
    
    public final AgentsClient.ListAgentsPagedResponse listAgents(String parent)

Returns the list of all agents in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Agent element : agentsClient.listAgents(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location to list all agents for. Format: `projects/<ProjectID>/locations/<LocationID>`.  
**Returns**  
---  
**Type** | **Description**  
`[AgentsClient.ListAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient.ListAgentsPagedResponse)` |   
  
### listAgentsCallable()
    
    
    public final UnaryCallable<ListAgentsRequest,ListAgentsResponse> listAgentsCallable()

Returns the list of all agents in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       ListAgentsRequest request =
           ListAgentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListAgentsResponse response = agentsClient.listAgentsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListAgentsRequest),[ListAgentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListAgentsResponse)>` |   
  
### listAgentsPagedCallable()
    
    
    public final UnaryCallable<ListAgentsRequest,AgentsClient.ListAgentsPagedResponse> listAgentsPagedCallable()

Returns the list of all agents in the specified location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       ListAgentsRequest request =
           ListAgentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Agent> future = agentsClient.listAgentsPagedCallable().futureCall(request);
       // Do something.
       for (Agent element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListAgentsRequest),[ListAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient.ListAgentsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final AgentsClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : agentsClient.listLocations(request).iterateAll()) {
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
`[AgentsClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient.ListLocationsPagedResponse)` |   
  
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
     try (AgentsClient agentsClient = AgentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = agentsClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,AgentsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future = agentsClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentsClient.ListLocationsPagedResponse)>` |   
  
### restoreAgentAsync(RestoreAgentRequest request)
    
    
    public final OperationFuture<Empty,Struct> restoreAgentAsync(RestoreAgentRequest request)

Restores the specified agent from a binary file.

Replaces the current agent with a new one. Note that all existing resources in agent (e.g. intents, entity types, flows) will be removed.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (AgentsClient agentsClient = AgentsClient.create()) {
        RestoreAgentRequest request =
            RestoreAgentRequest.newBuilder()
                .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
                .build();
        agentsClient.restoreAgentAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestoreAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestoreAgentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### restoreAgentCallable()
    
    
    public final UnaryCallable<RestoreAgentRequest,Operation> restoreAgentCallable()

Restores the specified agent from a binary file.

Replaces the current agent with a new one. Note that all existing resources in agent (e.g. intents, entity types, flows) will be removed.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (AgentsClient agentsClient = AgentsClient.create()) {
        RestoreAgentRequest request =
            RestoreAgentRequest.newBuilder()
                .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
                .build();
        ApiFuture<Operation> future = agentsClient.restoreAgentCallable().futureCall(request);
        // Do something.
        future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RestoreAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestoreAgentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restoreAgentOperationCallable()
    
    
    public final OperationCallable<RestoreAgentRequest,Empty,Struct> restoreAgentOperationCallable()

Restores the specified agent from a binary file.

Replaces the current agent with a new one. Note that all existing resources in agent (e.g. intents, entity types, flows) will be removed.

This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields:

\- `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct)

  * `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty)

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (AgentsClient agentsClient = AgentsClient.create()) {
        RestoreAgentRequest request =
            RestoreAgentRequest.newBuilder()
                .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
                .build();
        OperationFuture<Empty, Struct> future =
            agentsClient.restoreAgentOperationCallable().futureCall(request);
        // Do something.
        future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RestoreAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestoreAgentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateAgent(Agent agent, FieldMask updateMask)
    
    
    public final Agent updateAgent(Agent agent, FieldMask updateMask)

Updates the specified agent.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       Agent agent = Agent.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Agent response = agentsClient.updateAgent(agent, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`agent` | `[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent)`  
Required. The agent to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The mask to control which fields get updated. If the mask is not present, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent)` |   
  
### updateAgent(UpdateAgentRequest request)
    
    
    public final Agent updateAgent(UpdateAgentRequest request)

Updates the specified agent.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       UpdateAgentRequest request =
           UpdateAgentRequest.newBuilder()
               .setAgent(Agent.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Agent response = agentsClient.updateAgent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateAgentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent)` |   
  
### updateAgentCallable()
    
    
    public final UnaryCallable<UpdateAgentRequest,Agent> updateAgentCallable()

Updates the specified agent.

Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       UpdateAgentRequest request =
           UpdateAgentRequest.newBuilder()
               .setAgent(Agent.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Agent> future = agentsClient.updateAgentCallable().futureCall(request);
       // Do something.
       Agent response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateAgentRequest),[Agent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Agent)>` |   
  
### updateGenerativeSettings(GenerativeSettings generativeSettings, FieldMask updateMask)
    
    
    public final GenerativeSettings updateGenerativeSettings(GenerativeSettings generativeSettings, FieldMask updateMask)

Updates the generative settings for the agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       GenerativeSettings generativeSettings = GenerativeSettings.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       GenerativeSettings response =
           agentsClient.updateGenerativeSettings(generativeSettings, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`generativeSettings` | `[GenerativeSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GenerativeSettings)`  
Required. Generative settings to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The mask to control which fields get updated. If the mask is not present, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GenerativeSettings)` |   
  
### updateGenerativeSettings(UpdateGenerativeSettingsRequest request)
    
    
    public final GenerativeSettings updateGenerativeSettings(UpdateGenerativeSettingsRequest request)

Updates the generative settings for the agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       UpdateGenerativeSettingsRequest request =
           UpdateGenerativeSettingsRequest.newBuilder()
               .setGenerativeSettings(GenerativeSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       GenerativeSettings response = agentsClient.updateGenerativeSettings(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGenerativeSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateGenerativeSettingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GenerativeSettings)` |   
  
### updateGenerativeSettingsCallable()
    
    
    public final UnaryCallable<UpdateGenerativeSettingsRequest,GenerativeSettings> updateGenerativeSettingsCallable()

Updates the generative settings for the agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       UpdateGenerativeSettingsRequest request =
           UpdateGenerativeSettingsRequest.newBuilder()
               .setGenerativeSettings(GenerativeSettings.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<GenerativeSettings> future =
           agentsClient.updateGenerativeSettingsCallable().futureCall(request);
       // Do something.
       GenerativeSettings response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGenerativeSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateGenerativeSettingsRequest),[GenerativeSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GenerativeSettings)>` |   
  
### validateAgent(ValidateAgentRequest request)
    
    
    public final AgentValidationResult validateAgent(ValidateAgentRequest request)

Validates the specified agent and creates or updates validation results. The agent in draft version is validated. Please call this API after the training is completed to get the complete validation results.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       ValidateAgentRequest request =
           ValidateAgentRequest.newBuilder()
               .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setLanguageCode("languageCode-2092349083")
               .build();
       AgentValidationResult response = agentsClient.validateAgent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ValidateAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ValidateAgentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AgentValidationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentValidationResult)` |   
  
### validateAgentCallable()
    
    
    public final UnaryCallable<ValidateAgentRequest,AgentValidationResult> validateAgentCallable()

Validates the specified agent and creates or updates validation results. The agent in draft version is validated. Please call this API after the training is completed to get the complete validation results.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AgentsClient agentsClient = AgentsClient.create()) {
       ValidateAgentRequest request =
           ValidateAgentRequest.newBuilder()
               .setName(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<AgentValidationResult> future =
           agentsClient.validateAgentCallable().futureCall(request);
       // Do something.
       AgentValidationResult response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ValidateAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ValidateAgentRequest),[AgentValidationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.AgentValidationResult)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
