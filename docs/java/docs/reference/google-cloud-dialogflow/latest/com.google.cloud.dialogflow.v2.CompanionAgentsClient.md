---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgentsClient
title: Class CompanionAgentsClient (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:27.049075+00:00
---

# Class CompanionAgentsClient (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgentsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CompanionAgentsClient (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow/google-cloud-dialogflow/src/main/java/com/google/cloud/dialogflow/v2/CompanionAgentsClient.java)| [Product Reference](https://cloud.google.com/dialogflow-enterprise/)  
---|---  
  
Service Description: Service for managing companion agents.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       CompanionAgent companionAgent = CompanionAgent.newBuilder().build();
       String companionAgentId = "companionAgentId-580252076";
       CompanionAgent response =
           companionAgentsClient.createCompanionAgent(parent, companionAgent, companionAgentId);
     }
     

Note: close() needs to be called on the CompanionAgentsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateCompanionAgent |  Creates a companion agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCompanionAgent(CreateCompanionAgentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createCompanionAgent(LocationName parent, CompanionAgent companionAgent, String companionAgentId) 
  * createCompanionAgent(String parent, CompanionAgent companionAgent, String companionAgentId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCompanionAgentCallable() 

  
GetCompanionAgent |  Gets a companion agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCompanionAgent(GetCompanionAgentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCompanionAgent(CompanionAgentName name) 
  * getCompanionAgent(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCompanionAgentCallable() 

  
UpdateCompanionAgent |  Updates a companion agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCompanionAgent(UpdateCompanionAgentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateCompanionAgent(CompanionAgent companionAgent, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCompanionAgentCallable() 

  
DeleteCompanionAgent |  Deletes a companion agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteCompanionAgent(DeleteCompanionAgentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteCompanionAgent(CompanionAgentName name) 
  * deleteCompanionAgent(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCompanionAgentCallable() 

  
ListCompanionAgents |  Lists companion agents. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCompanionAgents(ListCompanionAgentsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCompanionAgents(LocationName parent) 
  * listCompanionAgents(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCompanionAgentsPagedCallable() 
  * listCompanionAgentsCallable() 

  
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

This class can be customized by passing in a custom instance of CompanionAgentsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CompanionAgentsSettings companionAgentsSettings =
         CompanionAgentsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CompanionAgentsClient companionAgentsClient =
         CompanionAgentsClient.create(companionAgentsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CompanionAgentsSettings companionAgentsSettings =
         CompanionAgentsSettings.newBuilder().setEndpoint(myEndpoint).build();
     CompanionAgentsClient companionAgentsClient =
         CompanionAgentsClient.create(companionAgentsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CompanionAgentsSettings companionAgentsSettings =
         CompanionAgentsSettings.newHttpJsonBuilder().build();
     CompanionAgentsClient companionAgentsClient =
         CompanionAgentsClient.create(companionAgentsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CompanionAgentsClient

## Static Methods 

### create()
    
    
    public static final CompanionAgentsClient create()

Constructs an instance of CompanionAgentsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CompanionAgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgentsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CompanionAgentsSettings settings)
    
    
    public static final CompanionAgentsClient create(CompanionAgentsSettings settings)

Constructs an instance of CompanionAgentsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CompanionAgentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgentsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgentsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CompanionAgentsStub stub)
    
    
    public static final CompanionAgentsClient create(CompanionAgentsStub stub)

Constructs an instance of CompanionAgentsClient, using the given stub for making calls. This is for advanced usage - prefer using create(CompanionAgentsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CompanionAgentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.CompanionAgentsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgentsClient)` |   
  
## Constructors 

### CompanionAgentsClient(CompanionAgentsSettings settings)
    
    
    protected CompanionAgentsClient(CompanionAgentsSettings settings)

Constructs an instance of CompanionAgentsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CompanionAgentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgentsSettings)`  
  
  
### CompanionAgentsClient(CompanionAgentsStub stub)
    
    
    protected CompanionAgentsClient(CompanionAgentsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CompanionAgentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.CompanionAgentsStub)`  
  
  
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

### createCompanionAgent(@Nullable LocationName parent, CompanionAgent companionAgent, String companionAgentId)
    
    
    public final CompanionAgent createCompanionAgent(@Nullable LocationName parent, CompanionAgent companionAgent, String companionAgentId)

Creates a companion agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       CompanionAgent companionAgent = CompanionAgent.newBuilder().build();
       String companionAgentId = "companionAgentId-580252076";
       CompanionAgent response =
           companionAgentsClient.createCompanionAgent(parent, companionAgent, companionAgentId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.LocationName`  
Required. Resource identifier of the project creating the companion agent. Format: `projects/{project}/locations/{location}`  
`companionAgent` | `[CompanionAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent)`  
Required. The companion agent to create.  
`companionAgentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The resource ID of the companion agent to create. If not provided, the server will auto-generate a resource ID.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent)` |   
  
### createCompanionAgent(CreateCompanionAgentRequest request)
    
    
    public final CompanionAgent createCompanionAgent(CreateCompanionAgentRequest request)

Creates a companion agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       CreateCompanionAgentRequest request =
           CreateCompanionAgentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setCompanionAgent(CompanionAgent.newBuilder().build())
               .setCompanionAgentId("companionAgentId-580252076")
               .build();
       CompanionAgent response = companionAgentsClient.createCompanionAgent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCompanionAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateCompanionAgentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent)` |   
  
### createCompanionAgent(String parent, CompanionAgent companionAgent, String companionAgentId)
    
    
    public final CompanionAgent createCompanionAgent(String parent, CompanionAgent companionAgent, String companionAgentId)

Creates a companion agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       CompanionAgent companionAgent = CompanionAgent.newBuilder().build();
       String companionAgentId = "companionAgentId-580252076";
       CompanionAgent response =
           companionAgentsClient.createCompanionAgent(parent, companionAgent, companionAgentId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource identifier of the project creating the companion agent. Format: `projects/{project}/locations/{location}`  
`companionAgent` | `[CompanionAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent)`  
Required. The companion agent to create.  
`companionAgentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. The resource ID of the companion agent to create. If not provided, the server will auto-generate a resource ID.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent)` |   
  
### createCompanionAgentCallable()
    
    
    public final UnaryCallable<CreateCompanionAgentRequest,CompanionAgent> createCompanionAgentCallable()

Creates a companion agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       CreateCompanionAgentRequest request =
           CreateCompanionAgentRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setCompanionAgent(CompanionAgent.newBuilder().build())
               .setCompanionAgentId("companionAgentId-580252076")
               .build();
       ApiFuture<CompanionAgent> future =
           companionAgentsClient.createCompanionAgentCallable().futureCall(request);
       // Do something.
       CompanionAgent response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCompanionAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateCompanionAgentRequest),[CompanionAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent)>` |   
  
### deleteCompanionAgent(@Nullable CompanionAgentName name)
    
    
    public final void deleteCompanionAgent(@Nullable CompanionAgentName name)

Deletes a companion agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       CompanionAgentName name =
           CompanionAgentName.of("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]");
       companionAgentsClient.deleteCompanionAgent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.CompanionAgentName`  
Required. The unique resource identifier of the CompanionAgent to delete. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`.  
  
### deleteCompanionAgent(DeleteCompanionAgentRequest request)
    
    
    public final void deleteCompanionAgent(DeleteCompanionAgentRequest request)

Deletes a companion agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       DeleteCompanionAgentRequest request =
           DeleteCompanionAgentRequest.newBuilder()
               .setName(
                   CompanionAgentName.of("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]").toString())
               .build();
       companionAgentsClient.deleteCompanionAgent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCompanionAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteCompanionAgentRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteCompanionAgent(String name)
    
    
    public final void deleteCompanionAgent(String name)

Deletes a companion agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       String name =
           CompanionAgentName.of("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]").toString();
       companionAgentsClient.deleteCompanionAgent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The unique resource identifier of the CompanionAgent to delete. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`.  
  
### deleteCompanionAgentCallable()
    
    
    public final UnaryCallable<DeleteCompanionAgentRequest,Empty> deleteCompanionAgentCallable()

Deletes a companion agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       DeleteCompanionAgentRequest request =
           DeleteCompanionAgentRequest.newBuilder()
               .setName(
                   CompanionAgentName.of("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]").toString())
               .build();
       ApiFuture<Empty> future =
           companionAgentsClient.deleteCompanionAgentCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteCompanionAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteCompanionAgentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getCompanionAgent(@Nullable CompanionAgentName name)
    
    
    public final CompanionAgent getCompanionAgent(@Nullable CompanionAgentName name)

Gets a companion agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       CompanionAgentName name =
           CompanionAgentName.of("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]");
       CompanionAgent response = companionAgentsClient.getCompanionAgent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.CompanionAgentName`  
Required. The unique resource identifier of the CompanionAgent to get all information for. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`. Contains the information about the {project}, {location}, and {companion_agent}.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent)` |   
  
### getCompanionAgent(GetCompanionAgentRequest request)
    
    
    public final CompanionAgent getCompanionAgent(GetCompanionAgentRequest request)

Gets a companion agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       GetCompanionAgentRequest request =
           GetCompanionAgentRequest.newBuilder()
               .setName(
                   CompanionAgentName.of("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]").toString())
               .build();
       CompanionAgent response = companionAgentsClient.getCompanionAgent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCompanionAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetCompanionAgentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent)` |   
  
### getCompanionAgent(String name)
    
    
    public final CompanionAgent getCompanionAgent(String name)

Gets a companion agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       String name =
           CompanionAgentName.of("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]").toString();
       CompanionAgent response = companionAgentsClient.getCompanionAgent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The unique resource identifier of the CompanionAgent to get all information for. Format: `projects/{project}/locations/{location}/companionAgents/{companion_agent}`. Contains the information about the {project}, {location}, and {companion_agent}.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent)` |   
  
### getCompanionAgentCallable()
    
    
    public final UnaryCallable<GetCompanionAgentRequest,CompanionAgent> getCompanionAgentCallable()

Gets a companion agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       GetCompanionAgentRequest request =
           GetCompanionAgentRequest.newBuilder()
               .setName(
                   CompanionAgentName.of("[PROJECT]", "[LOCATION]", "[COMPANION_AGENT]").toString())
               .build();
       ApiFuture<CompanionAgent> future =
           companionAgentsClient.getCompanionAgentCallable().futureCall(request);
       // Do something.
       CompanionAgent response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCompanionAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetCompanionAgentRequest),[CompanionAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = companionAgentsClient.getLocation(request);
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
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = companionAgentsClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable CompanionAgentsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.CompanionAgentsSettings` |   
  
### getStub()
    
    
    public CompanionAgentsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CompanionAgentsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.CompanionAgentsStub)` |   
  
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
  
### listCompanionAgents(@Nullable LocationName parent)
    
    
    public final CompanionAgentsClient.ListCompanionAgentsPagedResponse listCompanionAgents(@Nullable LocationName parent)

Lists companion agents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (CompanionAgent element :
           companionAgentsClient.listCompanionAgents(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.LocationName`  
Required. The parent resource name to list the companion agents for. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgentsClient.ListCompanionAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgentsClient.ListCompanionAgentsPagedResponse)` |   
  
### listCompanionAgents(ListCompanionAgentsRequest request)
    
    
    public final CompanionAgentsClient.ListCompanionAgentsPagedResponse listCompanionAgents(ListCompanionAgentsRequest request)

Lists companion agents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       ListCompanionAgentsRequest request =
           ListCompanionAgentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (CompanionAgent element :
           companionAgentsClient.listCompanionAgents(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCompanionAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListCompanionAgentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgentsClient.ListCompanionAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgentsClient.ListCompanionAgentsPagedResponse)` |   
  
### listCompanionAgents(String parent)
    
    
    public final CompanionAgentsClient.ListCompanionAgentsPagedResponse listCompanionAgents(String parent)

Lists companion agents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (CompanionAgent element :
           companionAgentsClient.listCompanionAgents(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name to list the companion agents for. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgentsClient.ListCompanionAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgentsClient.ListCompanionAgentsPagedResponse)` |   
  
### listCompanionAgentsCallable()
    
    
    public final UnaryCallable<ListCompanionAgentsRequest,ListCompanionAgentsResponse> listCompanionAgentsCallable()

Lists companion agents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       ListCompanionAgentsRequest request =
           ListCompanionAgentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListCompanionAgentsResponse response =
             companionAgentsClient.listCompanionAgentsCallable().call(request);
         for (CompanionAgent element : response.getCompanionAgentsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCompanionAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListCompanionAgentsRequest),[ListCompanionAgentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListCompanionAgentsResponse)>` |   
  
### listCompanionAgentsPagedCallable()
    
    
    public final UnaryCallable<ListCompanionAgentsRequest,CompanionAgentsClient.ListCompanionAgentsPagedResponse> listCompanionAgentsPagedCallable()

Lists companion agents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       ListCompanionAgentsRequest request =
           ListCompanionAgentsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<CompanionAgent> future =
           companionAgentsClient.listCompanionAgentsPagedCallable().futureCall(request);
       // Do something.
       for (CompanionAgent element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCompanionAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListCompanionAgentsRequest),[ListCompanionAgentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgentsClient.ListCompanionAgentsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final CompanionAgentsClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : companionAgentsClient.listLocations(request).iterateAll()) {
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
`[CompanionAgentsClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgentsClient.ListLocationsPagedResponse)` |   
  
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
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             companionAgentsClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,CompanionAgentsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           companionAgentsClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgentsClient.ListLocationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateCompanionAgent(CompanionAgent companionAgent, FieldMask updateMask)
    
    
    public final CompanionAgent updateCompanionAgent(CompanionAgent companionAgent, FieldMask updateMask)

Updates a companion agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       CompanionAgent companionAgent = CompanionAgent.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       CompanionAgent response =
           companionAgentsClient.updateCompanionAgent(companionAgent, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`companionAgent` | `[CompanionAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent)`  
Required. The Companion Agent to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Update mask for Companion Agent.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent)` |   
  
### updateCompanionAgent(UpdateCompanionAgentRequest request)
    
    
    public final CompanionAgent updateCompanionAgent(UpdateCompanionAgentRequest request)

Updates a companion agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       UpdateCompanionAgentRequest request =
           UpdateCompanionAgentRequest.newBuilder()
               .setCompanionAgent(CompanionAgent.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       CompanionAgent response = companionAgentsClient.updateCompanionAgent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCompanionAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateCompanionAgentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CompanionAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent)` |   
  
### updateCompanionAgentCallable()
    
    
    public final UnaryCallable<UpdateCompanionAgentRequest,CompanionAgent> updateCompanionAgentCallable()

Updates a companion agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CompanionAgentsClient companionAgentsClient = CompanionAgentsClient.create()) {
       UpdateCompanionAgentRequest request =
           UpdateCompanionAgentRequest.newBuilder()
               .setCompanionAgent(CompanionAgent.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<CompanionAgent> future =
           companionAgentsClient.updateCompanionAgentCallable().futureCall(request);
       // Do something.
       CompanionAgent response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCompanionAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateCompanionAgentRequest),[CompanionAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompanionAgent)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
