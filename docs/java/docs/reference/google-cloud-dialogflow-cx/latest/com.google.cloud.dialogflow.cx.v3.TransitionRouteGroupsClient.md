---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupsClient
title: Class TransitionRouteGroupsClient (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:34:15.172867+00:00
---

# Class TransitionRouteGroupsClient (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TransitionRouteGroupsClient (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow-cx/google-cloud-dialogflow-cx/src/main/java/com/google/cloud/dialogflow/cx/v3/TransitionRouteGroupsClient.java)| [Product Reference](https://cloud.google.com/dialogflow/cx/docs)| [REST Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Service for managing TransitionRouteGroups.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       TransitionRouteGroupName name =
           TransitionRouteGroupName.ofProjectLocationAgentFlowTransitionRouteGroupName(
               "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[TRANSITION_ROUTE_GROUP]");
       TransitionRouteGroup response = transitionRouteGroupsClient.getTransitionRouteGroup(name);
     }
     

Note: close() needs to be called on the TransitionRouteGroupsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListTransitionRouteGroups |  Returns the list of all transition route groups in the specified flow. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTransitionRouteGroups(ListTransitionRouteGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTransitionRouteGroups(AgentName parent) 
  * listTransitionRouteGroups(FlowName parent) 
  * listTransitionRouteGroups(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTransitionRouteGroupsPagedCallable() 
  * listTransitionRouteGroupsCallable() 

  
GetTransitionRouteGroup |  Retrieves the specified TransitionRouteGroup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTransitionRouteGroup(GetTransitionRouteGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTransitionRouteGroup(TransitionRouteGroupName name) 
  * getTransitionRouteGroup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTransitionRouteGroupCallable() 

  
CreateTransitionRouteGroup |  Creates an TransitionRouteGroup in the specified flow.  Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTransitionRouteGroup(CreateTransitionRouteGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createTransitionRouteGroup(AgentName parent, TransitionRouteGroup transitionRouteGroup) 
  * createTransitionRouteGroup(FlowName parent, TransitionRouteGroup transitionRouteGroup) 
  * createTransitionRouteGroup(String parent, TransitionRouteGroup transitionRouteGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTransitionRouteGroupCallable() 

  
UpdateTransitionRouteGroup |  Updates the specified TransitionRouteGroup.  Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTransitionRouteGroup(UpdateTransitionRouteGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateTransitionRouteGroup(TransitionRouteGroup transitionRouteGroup, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTransitionRouteGroupCallable() 

  
DeleteTransitionRouteGroup |  Deletes the specified TransitionRouteGroup.  Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTransitionRouteGroup(DeleteTransitionRouteGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteTransitionRouteGroup(TransitionRouteGroupName name) 
  * deleteTransitionRouteGroup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTransitionRouteGroupCallable() 

  
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

This class can be customized by passing in a custom instance of TransitionRouteGroupsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TransitionRouteGroupsSettings transitionRouteGroupsSettings =
         TransitionRouteGroupsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create(transitionRouteGroupsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TransitionRouteGroupsSettings transitionRouteGroupsSettings =
         TransitionRouteGroupsSettings.newBuilder().setEndpoint(myEndpoint).build();
     TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create(transitionRouteGroupsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TransitionRouteGroupsSettings transitionRouteGroupsSettings =
         TransitionRouteGroupsSettings.newHttpJsonBuilder().build();
     TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create(transitionRouteGroupsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TransitionRouteGroupsClient

## Static Methods 

### create()
    
    
    public static final TransitionRouteGroupsClient create()

Constructs an instance of TransitionRouteGroupsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TransitionRouteGroupsSettings settings)
    
    
    public static final TransitionRouteGroupsClient create(TransitionRouteGroupsSettings settings)

Constructs an instance of TransitionRouteGroupsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TransitionRouteGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TransitionRouteGroupsStub stub)
    
    
    public static final TransitionRouteGroupsClient create(TransitionRouteGroupsStub stub)

Constructs an instance of TransitionRouteGroupsClient, using the given stub for making calls. This is for advanced usage - prefer using create(TransitionRouteGroupsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TransitionRouteGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.TransitionRouteGroupsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupsClient)` |   
  
## Constructors 

### TransitionRouteGroupsClient(TransitionRouteGroupsSettings settings)
    
    
    protected TransitionRouteGroupsClient(TransitionRouteGroupsSettings settings)

Constructs an instance of TransitionRouteGroupsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TransitionRouteGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupsSettings)`  
  
  
### TransitionRouteGroupsClient(TransitionRouteGroupsStub stub)
    
    
    protected TransitionRouteGroupsClient(TransitionRouteGroupsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TransitionRouteGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.TransitionRouteGroupsStub)`  
  
  
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

### createTransitionRouteGroup(@Nullable AgentName parent, TransitionRouteGroup transitionRouteGroup)
    
    
    public final TransitionRouteGroup createTransitionRouteGroup(@Nullable AgentName parent, TransitionRouteGroup transitionRouteGroup)

Creates an TransitionRouteGroup in the specified flow.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       AgentName parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       TransitionRouteGroup transitionRouteGroup = TransitionRouteGroup.newBuilder().build();
       TransitionRouteGroup response =
           transitionRouteGroupsClient.createTransitionRouteGroup(parent, transitionRouteGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.AgentName`  
Required. The flow to create an TransitionRouteGroup for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>` for agent-level groups.  
`transitionRouteGroup` | `[TransitionRouteGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroup)`  
Required. The transition route group to create.  
**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroup)` |   
  
### createTransitionRouteGroup(@Nullable FlowName parent, TransitionRouteGroup transitionRouteGroup)
    
    
    public final TransitionRouteGroup createTransitionRouteGroup(@Nullable FlowName parent, TransitionRouteGroup transitionRouteGroup)

Creates an TransitionRouteGroup in the specified flow.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       FlowName parent = FlowName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]");
       TransitionRouteGroup transitionRouteGroup = TransitionRouteGroup.newBuilder().build();
       TransitionRouteGroup response =
           transitionRouteGroupsClient.createTransitionRouteGroup(parent, transitionRouteGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.FlowName`  
Required. The flow to create an TransitionRouteGroup for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>` for agent-level groups.  
`transitionRouteGroup` | `[TransitionRouteGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroup)`  
Required. The transition route group to create.  
**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroup)` |   
  
### createTransitionRouteGroup(CreateTransitionRouteGroupRequest request)
    
    
    public final TransitionRouteGroup createTransitionRouteGroup(CreateTransitionRouteGroupRequest request)

Creates an TransitionRouteGroup in the specified flow.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       CreateTransitionRouteGroupRequest request =
           CreateTransitionRouteGroupRequest.newBuilder()
               .setParent(FlowName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]").toString())
               .setTransitionRouteGroup(TransitionRouteGroup.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .build();
       TransitionRouteGroup response =
           transitionRouteGroupsClient.createTransitionRouteGroup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTransitionRouteGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreateTransitionRouteGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroup)` |   
  
### createTransitionRouteGroup(String parent, TransitionRouteGroup transitionRouteGroup)
    
    
    public final TransitionRouteGroup createTransitionRouteGroup(String parent, TransitionRouteGroup transitionRouteGroup)

Creates an TransitionRouteGroup in the specified flow.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       String parent = FlowName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]").toString();
       TransitionRouteGroup transitionRouteGroup = TransitionRouteGroup.newBuilder().build();
       TransitionRouteGroup response =
           transitionRouteGroupsClient.createTransitionRouteGroup(parent, transitionRouteGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The flow to create an TransitionRouteGroup for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>` for agent-level groups.  
`transitionRouteGroup` | `[TransitionRouteGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroup)`  
Required. The transition route group to create.  
**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroup)` |   
  
### createTransitionRouteGroupCallable()
    
    
    public final UnaryCallable<CreateTransitionRouteGroupRequest,TransitionRouteGroup> createTransitionRouteGroupCallable()

Creates an TransitionRouteGroup in the specified flow.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       CreateTransitionRouteGroupRequest request =
           CreateTransitionRouteGroupRequest.newBuilder()
               .setParent(FlowName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]").toString())
               .setTransitionRouteGroup(TransitionRouteGroup.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<TransitionRouteGroup> future =
           transitionRouteGroupsClient.createTransitionRouteGroupCallable().futureCall(request);
       // Do something.
       TransitionRouteGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTransitionRouteGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreateTransitionRouteGroupRequest),[TransitionRouteGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroup)>` |   
  
### deleteTransitionRouteGroup(@Nullable TransitionRouteGroupName name)
    
    
    public final void deleteTransitionRouteGroup(@Nullable TransitionRouteGroupName name)

Deletes the specified TransitionRouteGroup.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       TransitionRouteGroupName name =
           TransitionRouteGroupName.ofProjectLocationAgentFlowTransitionRouteGroupName(
               "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[TRANSITION_ROUTE_GROUP]");
       transitionRouteGroupsClient.deleteTransitionRouteGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupName`  
Required. The name of the TransitionRouteGroup to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/transitionRouteGroups/<TransitionRouteGroupID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/transitionRouteGroups/<TransitionRouteGroupID>`.  
  
### deleteTransitionRouteGroup(DeleteTransitionRouteGroupRequest request)
    
    
    public final void deleteTransitionRouteGroup(DeleteTransitionRouteGroupRequest request)

Deletes the specified TransitionRouteGroup.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       DeleteTransitionRouteGroupRequest request =
           DeleteTransitionRouteGroupRequest.newBuilder()
               .setName(
                   TransitionRouteGroupName.ofProjectLocationAgentFlowTransitionRouteGroupName(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[AGENT]",
                           "[FLOW]",
                           "[TRANSITION_ROUTE_GROUP]")
                       .toString())
               .setForce(true)
               .build();
       transitionRouteGroupsClient.deleteTransitionRouteGroup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTransitionRouteGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeleteTransitionRouteGroupRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteTransitionRouteGroup(String name)
    
    
    public final void deleteTransitionRouteGroup(String name)

Deletes the specified TransitionRouteGroup.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       String name =
           TransitionRouteGroupName.ofProjectLocationAgentFlowTransitionRouteGroupName(
                   "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[TRANSITION_ROUTE_GROUP]")
               .toString();
       transitionRouteGroupsClient.deleteTransitionRouteGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the TransitionRouteGroup to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/transitionRouteGroups/<TransitionRouteGroupID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/transitionRouteGroups/<TransitionRouteGroupID>`.  
  
### deleteTransitionRouteGroupCallable()
    
    
    public final UnaryCallable<DeleteTransitionRouteGroupRequest,Empty> deleteTransitionRouteGroupCallable()

Deletes the specified TransitionRouteGroup.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       DeleteTransitionRouteGroupRequest request =
           DeleteTransitionRouteGroupRequest.newBuilder()
               .setName(
                   TransitionRouteGroupName.ofProjectLocationAgentFlowTransitionRouteGroupName(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[AGENT]",
                           "[FLOW]",
                           "[TRANSITION_ROUTE_GROUP]")
                       .toString())
               .setForce(true)
               .build();
       ApiFuture<Empty> future =
           transitionRouteGroupsClient.deleteTransitionRouteGroupCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTransitionRouteGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeleteTransitionRouteGroupRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = transitionRouteGroupsClient.getLocation(request);
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
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           transitionRouteGroupsClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable TransitionRouteGroupsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupsSettings` |   
  
### getStub()
    
    
    public TransitionRouteGroupsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.TransitionRouteGroupsStub)` |   
  
### getTransitionRouteGroup(@Nullable TransitionRouteGroupName name)
    
    
    public final TransitionRouteGroup getTransitionRouteGroup(@Nullable TransitionRouteGroupName name)

Retrieves the specified TransitionRouteGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       TransitionRouteGroupName name =
           TransitionRouteGroupName.ofProjectLocationAgentFlowTransitionRouteGroupName(
               "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[TRANSITION_ROUTE_GROUP]");
       TransitionRouteGroup response = transitionRouteGroupsClient.getTransitionRouteGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupName`  
Required. The name of the TransitionRouteGroup. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/transitionRouteGroups/<TransitionRouteGroupID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/transitionRouteGroups/<TransitionRouteGroupID>`.  
**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroup)` |   
  
### getTransitionRouteGroup(GetTransitionRouteGroupRequest request)
    
    
    public final TransitionRouteGroup getTransitionRouteGroup(GetTransitionRouteGroupRequest request)

Retrieves the specified TransitionRouteGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       GetTransitionRouteGroupRequest request =
           GetTransitionRouteGroupRequest.newBuilder()
               .setName(
                   TransitionRouteGroupName.ofProjectLocationAgentFlowTransitionRouteGroupName(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[AGENT]",
                           "[FLOW]",
                           "[TRANSITION_ROUTE_GROUP]")
                       .toString())
               .setLanguageCode("languageCode-2092349083")
               .build();
       TransitionRouteGroup response = transitionRouteGroupsClient.getTransitionRouteGroup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTransitionRouteGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetTransitionRouteGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroup)` |   
  
### getTransitionRouteGroup(String name)
    
    
    public final TransitionRouteGroup getTransitionRouteGroup(String name)

Retrieves the specified TransitionRouteGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       String name =
           TransitionRouteGroupName.ofProjectLocationAgentFlowTransitionRouteGroupName(
                   "[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]", "[TRANSITION_ROUTE_GROUP]")
               .toString();
       TransitionRouteGroup response = transitionRouteGroupsClient.getTransitionRouteGroup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the TransitionRouteGroup. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/transitionRouteGroups/<TransitionRouteGroupID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/transitionRouteGroups/<TransitionRouteGroupID>`.  
**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroup)` |   
  
### getTransitionRouteGroupCallable()
    
    
    public final UnaryCallable<GetTransitionRouteGroupRequest,TransitionRouteGroup> getTransitionRouteGroupCallable()

Retrieves the specified TransitionRouteGroup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       GetTransitionRouteGroupRequest request =
           GetTransitionRouteGroupRequest.newBuilder()
               .setName(
                   TransitionRouteGroupName.ofProjectLocationAgentFlowTransitionRouteGroupName(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[AGENT]",
                           "[FLOW]",
                           "[TRANSITION_ROUTE_GROUP]")
                       .toString())
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<TransitionRouteGroup> future =
           transitionRouteGroupsClient.getTransitionRouteGroupCallable().futureCall(request);
       // Do something.
       TransitionRouteGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTransitionRouteGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetTransitionRouteGroupRequest),[TransitionRouteGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroup)>` |   
  
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
    
    
    public final TransitionRouteGroupsClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : transitionRouteGroupsClient.listLocations(request).iterateAll()) {
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
`[TransitionRouteGroupsClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupsClient.ListLocationsPagedResponse)` |   
  
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
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             transitionRouteGroupsClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,TransitionRouteGroupsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           transitionRouteGroupsClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupsClient.ListLocationsPagedResponse)>` |   
  
### listTransitionRouteGroups(@Nullable AgentName parent)
    
    
    public final TransitionRouteGroupsClient.ListTransitionRouteGroupsPagedResponse listTransitionRouteGroups(@Nullable AgentName parent)

Returns the list of all transition route groups in the specified flow.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       AgentName parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       for (TransitionRouteGroup element :
           transitionRouteGroupsClient.listTransitionRouteGroups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.AgentName`  
Required. The flow to list all transition route groups for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>.  
**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroupsClient.ListTransitionRouteGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupsClient.ListTransitionRouteGroupsPagedResponse)` |   
  
### listTransitionRouteGroups(@Nullable FlowName parent)
    
    
    public final TransitionRouteGroupsClient.ListTransitionRouteGroupsPagedResponse listTransitionRouteGroups(@Nullable FlowName parent)

Returns the list of all transition route groups in the specified flow.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       FlowName parent = FlowName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]");
       for (TransitionRouteGroup element :
           transitionRouteGroupsClient.listTransitionRouteGroups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.FlowName`  
Required. The flow to list all transition route groups for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>.  
**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroupsClient.ListTransitionRouteGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupsClient.ListTransitionRouteGroupsPagedResponse)` |   
  
### listTransitionRouteGroups(ListTransitionRouteGroupsRequest request)
    
    
    public final TransitionRouteGroupsClient.ListTransitionRouteGroupsPagedResponse listTransitionRouteGroups(ListTransitionRouteGroupsRequest request)

Returns the list of all transition route groups in the specified flow.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       ListTransitionRouteGroupsRequest request =
           ListTransitionRouteGroupsRequest.newBuilder()
               .setParent(FlowName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       for (TransitionRouteGroup element :
           transitionRouteGroupsClient.listTransitionRouteGroups(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTransitionRouteGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListTransitionRouteGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroupsClient.ListTransitionRouteGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupsClient.ListTransitionRouteGroupsPagedResponse)` |   
  
### listTransitionRouteGroups(String parent)
    
    
    public final TransitionRouteGroupsClient.ListTransitionRouteGroupsPagedResponse listTransitionRouteGroups(String parent)

Returns the list of all transition route groups in the specified flow.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       String parent = FlowName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]").toString();
       for (TransitionRouteGroup element :
           transitionRouteGroupsClient.listTransitionRouteGroups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The flow to list all transition route groups for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>.  
**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroupsClient.ListTransitionRouteGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupsClient.ListTransitionRouteGroupsPagedResponse)` |   
  
### listTransitionRouteGroupsCallable()
    
    
    public final UnaryCallable<ListTransitionRouteGroupsRequest,ListTransitionRouteGroupsResponse> listTransitionRouteGroupsCallable()

Returns the list of all transition route groups in the specified flow.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       ListTransitionRouteGroupsRequest request =
           ListTransitionRouteGroupsRequest.newBuilder()
               .setParent(FlowName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       while (true) {
         ListTransitionRouteGroupsResponse response =
             transitionRouteGroupsClient.listTransitionRouteGroupsCallable().call(request);
         for (TransitionRouteGroup element : response.getTransitionRouteGroupsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTransitionRouteGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListTransitionRouteGroupsRequest),[ListTransitionRouteGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListTransitionRouteGroupsResponse)>` |   
  
### listTransitionRouteGroupsPagedCallable()
    
    
    public final UnaryCallable<ListTransitionRouteGroupsRequest,TransitionRouteGroupsClient.ListTransitionRouteGroupsPagedResponse> listTransitionRouteGroupsPagedCallable()

Returns the list of all transition route groups in the specified flow.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       ListTransitionRouteGroupsRequest request =
           ListTransitionRouteGroupsRequest.newBuilder()
               .setParent(FlowName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[FLOW]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<TransitionRouteGroup> future =
           transitionRouteGroupsClient.listTransitionRouteGroupsPagedCallable().futureCall(request);
       // Do something.
       for (TransitionRouteGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTransitionRouteGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListTransitionRouteGroupsRequest),[ListTransitionRouteGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroupsClient.ListTransitionRouteGroupsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateTransitionRouteGroup(TransitionRouteGroup transitionRouteGroup, FieldMask updateMask)
    
    
    public final TransitionRouteGroup updateTransitionRouteGroup(TransitionRouteGroup transitionRouteGroup, FieldMask updateMask)

Updates the specified TransitionRouteGroup.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       TransitionRouteGroup transitionRouteGroup = TransitionRouteGroup.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       TransitionRouteGroup response =
           transitionRouteGroupsClient.updateTransitionRouteGroup(transitionRouteGroup, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`transitionRouteGroup` | `[TransitionRouteGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroup)`  
Required. The transition route group to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The mask to control which fields get updated.  
**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroup)` |   
  
### updateTransitionRouteGroup(UpdateTransitionRouteGroupRequest request)
    
    
    public final TransitionRouteGroup updateTransitionRouteGroup(UpdateTransitionRouteGroupRequest request)

Updates the specified TransitionRouteGroup.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       UpdateTransitionRouteGroupRequest request =
           UpdateTransitionRouteGroupRequest.newBuilder()
               .setTransitionRouteGroup(TransitionRouteGroup.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .build();
       TransitionRouteGroup response =
           transitionRouteGroupsClient.updateTransitionRouteGroup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTransitionRouteGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateTransitionRouteGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TransitionRouteGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroup)` |   
  
### updateTransitionRouteGroupCallable()
    
    
    public final UnaryCallable<UpdateTransitionRouteGroupRequest,TransitionRouteGroup> updateTransitionRouteGroupCallable()

Updates the specified TransitionRouteGroup.

Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TransitionRouteGroupsClient transitionRouteGroupsClient =
         TransitionRouteGroupsClient.create()) {
       UpdateTransitionRouteGroupRequest request =
           UpdateTransitionRouteGroupRequest.newBuilder()
               .setTransitionRouteGroup(TransitionRouteGroup.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLanguageCode("languageCode-2092349083")
               .build();
       ApiFuture<TransitionRouteGroup> future =
           transitionRouteGroupsClient.updateTransitionRouteGroupCallable().futureCall(request);
       // Do something.
       TransitionRouteGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTransitionRouteGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdateTransitionRouteGroupRequest),[TransitionRouteGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.TransitionRouteGroup)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
