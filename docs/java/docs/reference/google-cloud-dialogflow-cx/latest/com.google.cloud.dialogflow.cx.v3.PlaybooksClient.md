---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksClient
title: Class PlaybooksClient (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:34:10.075249+00:00
---

# Class PlaybooksClient (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PlaybooksClient (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow-cx/google-cloud-dialogflow-cx/src/main/java/com/google/cloud/dialogflow/cx/v3/PlaybooksClient.java)| [Product Reference](https://cloud.google.com/dialogflow/cx/docs)| [REST Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Service for managing Playbooks.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       AgentName parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       Playbook playbook = Playbook.newBuilder().build();
       Playbook response = playbooksClient.createPlaybook(parent, playbook);
     }
     

Note: close() needs to be called on the PlaybooksClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreatePlaybook |  Creates a playbook in a specified agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPlaybook(CreatePlaybookRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createPlaybook(AgentName parent, Playbook playbook) 
  * createPlaybook(String parent, Playbook playbook) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPlaybookCallable() 

  
DeletePlaybook |  Deletes a specified playbook. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePlaybook(DeletePlaybookRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deletePlaybook(PlaybookName name) 
  * deletePlaybook(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePlaybookCallable() 

  
ListPlaybooks |  Returns a list of playbooks in the specified agent. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPlaybooks(ListPlaybooksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPlaybooks(AgentName parent) 
  * listPlaybooks(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPlaybooksPagedCallable() 
  * listPlaybooksCallable() 

  
GetPlaybook |  Retrieves the specified Playbook. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPlaybook(GetPlaybookRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPlaybook(PlaybookName name) 
  * getPlaybook(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPlaybookCallable() 

  
ExportPlaybook |  Exports the specified playbook to a binary file.  Note that resources (e.g. examples, tools) that the playbook references will also be exported. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportPlaybookAsync(ExportPlaybookRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportPlaybookOperationCallable() 
  * exportPlaybookCallable() 

  
ImportPlaybook |  Imports the specified playbook to the specified agent from a binary file. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importPlaybookAsync(ImportPlaybookRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importPlaybookOperationCallable() 
  * importPlaybookCallable() 

  
UpdatePlaybook |  Updates the specified Playbook. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePlaybook(UpdatePlaybookRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updatePlaybook(Playbook playbook, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePlaybookCallable() 

  
CreatePlaybookVersion |  Creates a version for the specified Playbook. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPlaybookVersion(CreatePlaybookVersionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createPlaybookVersion(PlaybookName parent, PlaybookVersion playbookVersion) 
  * createPlaybookVersion(String parent, PlaybookVersion playbookVersion) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPlaybookVersionCallable() 

  
GetPlaybookVersion |  Retrieves the specified version of the Playbook. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPlaybookVersion(GetPlaybookVersionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPlaybookVersion(PlaybookVersionName name) 
  * getPlaybookVersion(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPlaybookVersionCallable() 

  
RestorePlaybookVersion |  Retrieves the specified version of the Playbook and stores it as the current playbook draft, returning the playbook with resources updated. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restorePlaybookVersion(RestorePlaybookVersionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * restorePlaybookVersion(PlaybookVersionName name) 
  * restorePlaybookVersion(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restorePlaybookVersionCallable() 

  
ListPlaybookVersions |  Lists versions for the specified Playbook. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPlaybookVersions(ListPlaybookVersionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPlaybookVersions(PlaybookName parent) 
  * listPlaybookVersions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPlaybookVersionsPagedCallable() 
  * listPlaybookVersionsCallable() 

  
DeletePlaybookVersion |  Deletes the specified version of the Playbook. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePlaybookVersion(DeletePlaybookVersionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deletePlaybookVersion(PlaybookVersionName name) 
  * deletePlaybookVersion(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePlaybookVersionCallable() 

  
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

This class can be customized by passing in a custom instance of PlaybooksSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PlaybooksSettings playbooksSettings =
         PlaybooksSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     PlaybooksClient playbooksClient = PlaybooksClient.create(playbooksSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PlaybooksSettings playbooksSettings =
         PlaybooksSettings.newBuilder().setEndpoint(myEndpoint).build();
     PlaybooksClient playbooksClient = PlaybooksClient.create(playbooksSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PlaybooksSettings playbooksSettings = PlaybooksSettings.newHttpJsonBuilder().build();
     PlaybooksClient playbooksClient = PlaybooksClient.create(playbooksSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PlaybooksClient

## Static Methods 

### create()
    
    
    public static final PlaybooksClient create()

Constructs an instance of PlaybooksClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[PlaybooksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PlaybooksSettings settings)
    
    
    public static final PlaybooksClient create(PlaybooksSettings settings)

Constructs an instance of PlaybooksClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PlaybooksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PlaybooksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PlaybooksStub stub)
    
    
    public static final PlaybooksClient create(PlaybooksStub stub)

Constructs an instance of PlaybooksClient, using the given stub for making calls. This is for advanced usage - prefer using create(PlaybooksSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PlaybooksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.PlaybooksStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PlaybooksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksClient)` |   
  
## Constructors 

### PlaybooksClient(PlaybooksSettings settings)
    
    
    protected PlaybooksClient(PlaybooksSettings settings)

Constructs an instance of PlaybooksClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PlaybooksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksSettings)`  
  
  
### PlaybooksClient(PlaybooksStub stub)
    
    
    protected PlaybooksClient(PlaybooksStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PlaybooksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.PlaybooksStub)`  
  
  
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

### createPlaybook(@Nullable AgentName parent, Playbook playbook)
    
    
    public final Playbook createPlaybook(@Nullable AgentName parent, Playbook playbook)

Creates a playbook in a specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       AgentName parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       Playbook playbook = Playbook.newBuilder().build();
       Playbook response = playbooksClient.createPlaybook(parent, playbook);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.AgentName`  
Required. The agent to create a playbook for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`playbook` | `[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)`  
Required. The playbook to create.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)` |   
  
### createPlaybook(CreatePlaybookRequest request)
    
    
    public final Playbook createPlaybook(CreatePlaybookRequest request)

Creates a playbook in a specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       CreatePlaybookRequest request =
           CreatePlaybookRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setPlaybook(Playbook.newBuilder().build())
               .build();
       Playbook response = playbooksClient.createPlaybook(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreatePlaybookRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)` |   
  
### createPlaybook(String parent, Playbook playbook)
    
    
    public final Playbook createPlaybook(String parent, Playbook playbook)

Creates a playbook in a specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       String parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString();
       Playbook playbook = Playbook.newBuilder().build();
       Playbook response = playbooksClient.createPlaybook(parent, playbook);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The agent to create a playbook for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`playbook` | `[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)`  
Required. The playbook to create.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)` |   
  
### createPlaybookCallable()
    
    
    public final UnaryCallable<CreatePlaybookRequest,Playbook> createPlaybookCallable()

Creates a playbook in a specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       CreatePlaybookRequest request =
           CreatePlaybookRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setPlaybook(Playbook.newBuilder().build())
               .build();
       ApiFuture<Playbook> future = playbooksClient.createPlaybookCallable().futureCall(request);
       // Do something.
       Playbook response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreatePlaybookRequest),[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)>` |   
  
### createPlaybookVersion(@Nullable PlaybookName parent, PlaybookVersion playbookVersion)
    
    
    public final PlaybookVersion createPlaybookVersion(@Nullable PlaybookName parent, PlaybookVersion playbookVersion)

Creates a version for the specified Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       PlaybookName parent = PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]");
       PlaybookVersion playbookVersion = PlaybookVersion.newBuilder().build();
       PlaybookVersion response = playbooksClient.createPlaybookVersion(parent, playbookVersion);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.PlaybookName`  
Required. The playbook to create a version for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.  
`playbookVersion` | `[PlaybookVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybookVersion)`  
Required. The playbook version to create.  
**Returns**  
---  
**Type** | **Description**  
`[PlaybookVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybookVersion)` |   
  
### createPlaybookVersion(CreatePlaybookVersionRequest request)
    
    
    public final PlaybookVersion createPlaybookVersion(CreatePlaybookVersionRequest request)

Creates a version for the specified Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       CreatePlaybookVersionRequest request =
           CreatePlaybookVersionRequest.newBuilder()
               .setParent(
                   PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]").toString())
               .setPlaybookVersion(PlaybookVersion.newBuilder().build())
               .build();
       PlaybookVersion response = playbooksClient.createPlaybookVersion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePlaybookVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreatePlaybookVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PlaybookVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybookVersion)` |   
  
### createPlaybookVersion(String parent, PlaybookVersion playbookVersion)
    
    
    public final PlaybookVersion createPlaybookVersion(String parent, PlaybookVersion playbookVersion)

Creates a version for the specified Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       String parent =
           PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]").toString();
       PlaybookVersion playbookVersion = PlaybookVersion.newBuilder().build();
       PlaybookVersion response = playbooksClient.createPlaybookVersion(parent, playbookVersion);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The playbook to create a version for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.  
`playbookVersion` | `[PlaybookVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybookVersion)`  
Required. The playbook version to create.  
**Returns**  
---  
**Type** | **Description**  
`[PlaybookVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybookVersion)` |   
  
### createPlaybookVersionCallable()
    
    
    public final UnaryCallable<CreatePlaybookVersionRequest,PlaybookVersion> createPlaybookVersionCallable()

Creates a version for the specified Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       CreatePlaybookVersionRequest request =
           CreatePlaybookVersionRequest.newBuilder()
               .setParent(
                   PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]").toString())
               .setPlaybookVersion(PlaybookVersion.newBuilder().build())
               .build();
       ApiFuture<PlaybookVersion> future =
           playbooksClient.createPlaybookVersionCallable().futureCall(request);
       // Do something.
       PlaybookVersion response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePlaybookVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreatePlaybookVersionRequest),[PlaybookVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybookVersion)>` |   
  
### deletePlaybook(@Nullable PlaybookName name)
    
    
    public final void deletePlaybook(@Nullable PlaybookName name)

Deletes a specified playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       PlaybookName name = PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]");
       playbooksClient.deletePlaybook(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.PlaybookName`  
Required. The name of the playbook to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.  
  
### deletePlaybook(DeletePlaybookRequest request)
    
    
    public final void deletePlaybook(DeletePlaybookRequest request)

Deletes a specified playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       DeletePlaybookRequest request =
           DeletePlaybookRequest.newBuilder()
               .setName(
                   PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]").toString())
               .build();
       playbooksClient.deletePlaybook(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeletePlaybookRequest)`  
The request object containing all of the parameters for the API call.  
  
### deletePlaybook(String name)
    
    
    public final void deletePlaybook(String name)

Deletes a specified playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       String name = PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]").toString();
       playbooksClient.deletePlaybook(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the playbook to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.  
  
### deletePlaybookCallable()
    
    
    public final UnaryCallable<DeletePlaybookRequest,Empty> deletePlaybookCallable()

Deletes a specified playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       DeletePlaybookRequest request =
           DeletePlaybookRequest.newBuilder()
               .setName(
                   PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]").toString())
               .build();
       ApiFuture<Empty> future = playbooksClient.deletePlaybookCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeletePlaybookRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deletePlaybookVersion(@Nullable PlaybookVersionName name)
    
    
    public final void deletePlaybookVersion(@Nullable PlaybookVersionName name)

Deletes the specified version of the Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       PlaybookVersionName name =
           PlaybookVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]", "[VERSION]");
       playbooksClient.deletePlaybookVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.PlaybookVersionName`  
Required. The name of the playbook version to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>/versions/<VersionID>`.  
  
### deletePlaybookVersion(DeletePlaybookVersionRequest request)
    
    
    public final void deletePlaybookVersion(DeletePlaybookVersionRequest request)

Deletes the specified version of the Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       DeletePlaybookVersionRequest request =
           DeletePlaybookVersionRequest.newBuilder()
               .setName(
                   PlaybookVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]", "[VERSION]")
                       .toString())
               .build();
       playbooksClient.deletePlaybookVersion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePlaybookVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeletePlaybookVersionRequest)`  
The request object containing all of the parameters for the API call.  
  
### deletePlaybookVersion(String name)
    
    
    public final void deletePlaybookVersion(String name)

Deletes the specified version of the Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       String name =
           PlaybookVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]", "[VERSION]")
               .toString();
       playbooksClient.deletePlaybookVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the playbook version to delete. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>/versions/<VersionID>`.  
  
### deletePlaybookVersionCallable()
    
    
    public final UnaryCallable<DeletePlaybookVersionRequest,Empty> deletePlaybookVersionCallable()

Deletes the specified version of the Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       DeletePlaybookVersionRequest request =
           DeletePlaybookVersionRequest.newBuilder()
               .setName(
                   PlaybookVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]", "[VERSION]")
                       .toString())
               .build();
       ApiFuture<Empty> future = playbooksClient.deletePlaybookVersionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePlaybookVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeletePlaybookVersionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### exportPlaybookAsync(ExportPlaybookRequest request)
    
    
    public final OperationFuture<ExportPlaybookResponse,Struct> exportPlaybookAsync(ExportPlaybookRequest request)

Exports the specified playbook to a binary file.

Note that resources (e.g. examples, tools) that the playbook references will also be exported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       ExportPlaybookRequest request =
           ExportPlaybookRequest.newBuilder()
               .setName(
                   PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]").toString())
               .setPlaybookUri("playbookUri2118184975")
               .build();
       ExportPlaybookResponse response = playbooksClient.exportPlaybookAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportPlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportPlaybookRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportPlaybookResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportPlaybookResponse),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### exportPlaybookCallable()
    
    
    public final UnaryCallable<ExportPlaybookRequest,Operation> exportPlaybookCallable()

Exports the specified playbook to a binary file.

Note that resources (e.g. examples, tools) that the playbook references will also be exported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       ExportPlaybookRequest request =
           ExportPlaybookRequest.newBuilder()
               .setName(
                   PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]").toString())
               .setPlaybookUri("playbookUri2118184975")
               .build();
       ApiFuture<Operation> future = playbooksClient.exportPlaybookCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportPlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportPlaybookRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportPlaybookOperationCallable()
    
    
    public final OperationCallable<ExportPlaybookRequest,ExportPlaybookResponse,Struct> exportPlaybookOperationCallable()

Exports the specified playbook to a binary file.

Note that resources (e.g. examples, tools) that the playbook references will also be exported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       ExportPlaybookRequest request =
           ExportPlaybookRequest.newBuilder()
               .setName(
                   PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]").toString())
               .setPlaybookUri("playbookUri2118184975")
               .build();
       OperationFuture<ExportPlaybookResponse, Struct> future =
           playbooksClient.exportPlaybookOperationCallable().futureCall(request);
       // Do something.
       ExportPlaybookResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportPlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportPlaybookRequest),[ExportPlaybookResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportPlaybookResponse),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
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
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = playbooksClient.getLocation(request);
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
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = playbooksClient.getLocationCallable().futureCall(request);
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
  
### getPlaybook(@Nullable PlaybookName name)
    
    
    public final Playbook getPlaybook(@Nullable PlaybookName name)

Retrieves the specified Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       PlaybookName name = PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]");
       Playbook response = playbooksClient.getPlaybook(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.PlaybookName`  
Required. The name of the playbook. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)` |   
  
### getPlaybook(GetPlaybookRequest request)
    
    
    public final Playbook getPlaybook(GetPlaybookRequest request)

Retrieves the specified Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       GetPlaybookRequest request =
           GetPlaybookRequest.newBuilder()
               .setName(
                   PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]").toString())
               .build();
       Playbook response = playbooksClient.getPlaybook(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetPlaybookRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)` |   
  
### getPlaybook(String name)
    
    
    public final Playbook getPlaybook(String name)

Retrieves the specified Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       String name = PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]").toString();
       Playbook response = playbooksClient.getPlaybook(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the playbook. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)` |   
  
### getPlaybookCallable()
    
    
    public final UnaryCallable<GetPlaybookRequest,Playbook> getPlaybookCallable()

Retrieves the specified Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       GetPlaybookRequest request =
           GetPlaybookRequest.newBuilder()
               .setName(
                   PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]").toString())
               .build();
       ApiFuture<Playbook> future = playbooksClient.getPlaybookCallable().futureCall(request);
       // Do something.
       Playbook response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetPlaybookRequest),[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)>` |   
  
### getPlaybookVersion(@Nullable PlaybookVersionName name)
    
    
    public final PlaybookVersion getPlaybookVersion(@Nullable PlaybookVersionName name)

Retrieves the specified version of the Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       PlaybookVersionName name =
           PlaybookVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]", "[VERSION]");
       PlaybookVersion response = playbooksClient.getPlaybookVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.PlaybookVersionName`  
Required. The name of the playbook version. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>/versions/<VersionID>`.  
**Returns**  
---  
**Type** | **Description**  
`[PlaybookVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybookVersion)` |   
  
### getPlaybookVersion(GetPlaybookVersionRequest request)
    
    
    public final PlaybookVersion getPlaybookVersion(GetPlaybookVersionRequest request)

Retrieves the specified version of the Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       GetPlaybookVersionRequest request =
           GetPlaybookVersionRequest.newBuilder()
               .setName(
                   PlaybookVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]", "[VERSION]")
                       .toString())
               .build();
       PlaybookVersion response = playbooksClient.getPlaybookVersion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPlaybookVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetPlaybookVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PlaybookVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybookVersion)` |   
  
### getPlaybookVersion(String name)
    
    
    public final PlaybookVersion getPlaybookVersion(String name)

Retrieves the specified version of the Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       String name =
           PlaybookVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]", "[VERSION]")
               .toString();
       PlaybookVersion response = playbooksClient.getPlaybookVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the playbook version. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>/versions/<VersionID>`.  
**Returns**  
---  
**Type** | **Description**  
`[PlaybookVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybookVersion)` |   
  
### getPlaybookVersionCallable()
    
    
    public final UnaryCallable<GetPlaybookVersionRequest,PlaybookVersion> getPlaybookVersionCallable()

Retrieves the specified version of the Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       GetPlaybookVersionRequest request =
           GetPlaybookVersionRequest.newBuilder()
               .setName(
                   PlaybookVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]", "[VERSION]")
                       .toString())
               .build();
       ApiFuture<PlaybookVersion> future =
           playbooksClient.getPlaybookVersionCallable().futureCall(request);
       // Do something.
       PlaybookVersion response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPlaybookVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetPlaybookVersionRequest),[PlaybookVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybookVersion)>` |   
  
### getSettings()
    
    
    public final @Nullable PlaybooksSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.PlaybooksSettings` |   
  
### getStub()
    
    
    public PlaybooksStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[PlaybooksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.stub.PlaybooksStub)` |   
  
### importPlaybookAsync(ImportPlaybookRequest request)
    
    
    public final OperationFuture<ImportPlaybookResponse,Struct> importPlaybookAsync(ImportPlaybookRequest request)

Imports the specified playbook to the specified agent from a binary file.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       ImportPlaybookRequest request =
           ImportPlaybookRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setImportStrategy(PlaybookImportStrategy.newBuilder().build())
               .build();
       ImportPlaybookResponse response = playbooksClient.importPlaybookAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportPlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ImportPlaybookRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportPlaybookResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ImportPlaybookResponse),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### importPlaybookCallable()
    
    
    public final UnaryCallable<ImportPlaybookRequest,Operation> importPlaybookCallable()

Imports the specified playbook to the specified agent from a binary file.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       ImportPlaybookRequest request =
           ImportPlaybookRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setImportStrategy(PlaybookImportStrategy.newBuilder().build())
               .build();
       ApiFuture<Operation> future = playbooksClient.importPlaybookCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportPlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ImportPlaybookRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importPlaybookOperationCallable()
    
    
    public final OperationCallable<ImportPlaybookRequest,ImportPlaybookResponse,Struct> importPlaybookOperationCallable()

Imports the specified playbook to the specified agent from a binary file.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       ImportPlaybookRequest request =
           ImportPlaybookRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setImportStrategy(PlaybookImportStrategy.newBuilder().build())
               .build();
       OperationFuture<ImportPlaybookResponse, Struct> future =
           playbooksClient.importPlaybookOperationCallable().futureCall(request);
       // Do something.
       ImportPlaybookResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportPlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ImportPlaybookRequest),[ImportPlaybookResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ImportPlaybookResponse),[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
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
    
    
    public final PlaybooksClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : playbooksClient.listLocations(request).iterateAll()) {
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
`[PlaybooksClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksClient.ListLocationsPagedResponse)` |   
  
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
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = playbooksClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,PlaybooksClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future = playbooksClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksClient.ListLocationsPagedResponse)>` |   
  
### listPlaybookVersions(@Nullable PlaybookName parent)
    
    
    public final PlaybooksClient.ListPlaybookVersionsPagedResponse listPlaybookVersions(@Nullable PlaybookName parent)

Lists versions for the specified Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       PlaybookName parent = PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]");
       for (PlaybookVersion element : playbooksClient.listPlaybookVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.PlaybookName`  
Required. The playbook to list versions for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.  
**Returns**  
---  
**Type** | **Description**  
`[PlaybooksClient.ListPlaybookVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksClient.ListPlaybookVersionsPagedResponse)` |   
  
### listPlaybookVersions(ListPlaybookVersionsRequest request)
    
    
    public final PlaybooksClient.ListPlaybookVersionsPagedResponse listPlaybookVersions(ListPlaybookVersionsRequest request)

Lists versions for the specified Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       ListPlaybookVersionsRequest request =
           ListPlaybookVersionsRequest.newBuilder()
               .setParent(
                   PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (PlaybookVersion element : playbooksClient.listPlaybookVersions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPlaybookVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListPlaybookVersionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PlaybooksClient.ListPlaybookVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksClient.ListPlaybookVersionsPagedResponse)` |   
  
### listPlaybookVersions(String parent)
    
    
    public final PlaybooksClient.ListPlaybookVersionsPagedResponse listPlaybookVersions(String parent)

Lists versions for the specified Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       String parent =
           PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]").toString();
       for (PlaybookVersion element : playbooksClient.listPlaybookVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The playbook to list versions for. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.  
**Returns**  
---  
**Type** | **Description**  
`[PlaybooksClient.ListPlaybookVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksClient.ListPlaybookVersionsPagedResponse)` |   
  
### listPlaybookVersionsCallable()
    
    
    public final UnaryCallable<ListPlaybookVersionsRequest,ListPlaybookVersionsResponse> listPlaybookVersionsCallable()

Lists versions for the specified Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       ListPlaybookVersionsRequest request =
           ListPlaybookVersionsRequest.newBuilder()
               .setParent(
                   PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListPlaybookVersionsResponse response =
             playbooksClient.listPlaybookVersionsCallable().call(request);
         for (PlaybookVersion element : response.getPlaybookVersionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPlaybookVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListPlaybookVersionsRequest),[ListPlaybookVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListPlaybookVersionsResponse)>` |   
  
### listPlaybookVersionsPagedCallable()
    
    
    public final UnaryCallable<ListPlaybookVersionsRequest,PlaybooksClient.ListPlaybookVersionsPagedResponse> listPlaybookVersionsPagedCallable()

Lists versions for the specified Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       ListPlaybookVersionsRequest request =
           ListPlaybookVersionsRequest.newBuilder()
               .setParent(
                   PlaybookName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<PlaybookVersion> future =
           playbooksClient.listPlaybookVersionsPagedCallable().futureCall(request);
       // Do something.
       for (PlaybookVersion element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPlaybookVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListPlaybookVersionsRequest),[ListPlaybookVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksClient.ListPlaybookVersionsPagedResponse)>` |   
  
### listPlaybooks(@Nullable AgentName parent)
    
    
    public final PlaybooksClient.ListPlaybooksPagedResponse listPlaybooks(@Nullable AgentName parent)

Returns a list of playbooks in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       AgentName parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]");
       for (Playbook element : playbooksClient.listPlaybooks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.AgentName`  
Required. The agent to list playbooks from. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[PlaybooksClient.ListPlaybooksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksClient.ListPlaybooksPagedResponse)` |   
  
### listPlaybooks(ListPlaybooksRequest request)
    
    
    public final PlaybooksClient.ListPlaybooksPagedResponse listPlaybooks(ListPlaybooksRequest request)

Returns a list of playbooks in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       ListPlaybooksRequest request =
           ListPlaybooksRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Playbook element : playbooksClient.listPlaybooks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPlaybooksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListPlaybooksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PlaybooksClient.ListPlaybooksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksClient.ListPlaybooksPagedResponse)` |   
  
### listPlaybooks(String parent)
    
    
    public final PlaybooksClient.ListPlaybooksPagedResponse listPlaybooks(String parent)

Returns a list of playbooks in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       String parent = AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString();
       for (Playbook element : playbooksClient.listPlaybooks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The agent to list playbooks from. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
**Returns**  
---  
**Type** | **Description**  
`[PlaybooksClient.ListPlaybooksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksClient.ListPlaybooksPagedResponse)` |   
  
### listPlaybooksCallable()
    
    
    public final UnaryCallable<ListPlaybooksRequest,ListPlaybooksResponse> listPlaybooksCallable()

Returns a list of playbooks in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       ListPlaybooksRequest request =
           ListPlaybooksRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListPlaybooksResponse response = playbooksClient.listPlaybooksCallable().call(request);
         for (Playbook element : response.getPlaybooksList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPlaybooksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListPlaybooksRequest),[ListPlaybooksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListPlaybooksResponse)>` |   
  
### listPlaybooksPagedCallable()
    
    
    public final UnaryCallable<ListPlaybooksRequest,PlaybooksClient.ListPlaybooksPagedResponse> listPlaybooksPagedCallable()

Returns a list of playbooks in the specified agent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       ListPlaybooksRequest request =
           ListPlaybooksRequest.newBuilder()
               .setParent(AgentName.of("[PROJECT]", "[LOCATION]", "[AGENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Playbook> future = playbooksClient.listPlaybooksPagedCallable().futureCall(request);
       // Do something.
       for (Playbook element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPlaybooksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListPlaybooksRequest),[ListPlaybooksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksClient.ListPlaybooksPagedResponse)>` |   
  
### restorePlaybookVersion(@Nullable PlaybookVersionName name)
    
    
    public final RestorePlaybookVersionResponse restorePlaybookVersion(@Nullable PlaybookVersionName name)

Retrieves the specified version of the Playbook and stores it as the current playbook draft, returning the playbook with resources updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       PlaybookVersionName name =
           PlaybookVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]", "[VERSION]");
       RestorePlaybookVersionResponse response = playbooksClient.restorePlaybookVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.cx.v3.PlaybookVersionName`  
Required. The name of the playbook version. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>/versions/<VersionID>`.  
**Returns**  
---  
**Type** | **Description**  
`[RestorePlaybookVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestorePlaybookVersionResponse)` |   
  
### restorePlaybookVersion(RestorePlaybookVersionRequest request)
    
    
    public final RestorePlaybookVersionResponse restorePlaybookVersion(RestorePlaybookVersionRequest request)

Retrieves the specified version of the Playbook and stores it as the current playbook draft, returning the playbook with resources updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       RestorePlaybookVersionRequest request =
           RestorePlaybookVersionRequest.newBuilder()
               .setName(
                   PlaybookVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]", "[VERSION]")
                       .toString())
               .build();
       RestorePlaybookVersionResponse response = playbooksClient.restorePlaybookVersion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestorePlaybookVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestorePlaybookVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RestorePlaybookVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestorePlaybookVersionResponse)` |   
  
### restorePlaybookVersion(String name)
    
    
    public final RestorePlaybookVersionResponse restorePlaybookVersion(String name)

Retrieves the specified version of the Playbook and stores it as the current playbook draft, returning the playbook with resources updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       String name =
           PlaybookVersionName.of("[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]", "[VERSION]")
               .toString();
       RestorePlaybookVersionResponse response = playbooksClient.restorePlaybookVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the playbook version. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>/versions/<VersionID>`.  
**Returns**  
---  
**Type** | **Description**  
`[RestorePlaybookVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestorePlaybookVersionResponse)` |   
  
### restorePlaybookVersionCallable()
    
    
    public final UnaryCallable<RestorePlaybookVersionRequest,RestorePlaybookVersionResponse> restorePlaybookVersionCallable()

Retrieves the specified version of the Playbook and stores it as the current playbook draft, returning the playbook with resources updated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       RestorePlaybookVersionRequest request =
           RestorePlaybookVersionRequest.newBuilder()
               .setName(
                   PlaybookVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[AGENT]", "[PLAYBOOK]", "[VERSION]")
                       .toString())
               .build();
       ApiFuture<RestorePlaybookVersionResponse> future =
           playbooksClient.restorePlaybookVersionCallable().futureCall(request);
       // Do something.
       RestorePlaybookVersionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RestorePlaybookVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestorePlaybookVersionRequest),[RestorePlaybookVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestorePlaybookVersionResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updatePlaybook(Playbook playbook, FieldMask updateMask)
    
    
    public final Playbook updatePlaybook(Playbook playbook, FieldMask updateMask)

Updates the specified Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       Playbook playbook = Playbook.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Playbook response = playbooksClient.updatePlaybook(playbook, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`playbook` | `[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)`  
Required. The playbook to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The mask to control which fields get updated. If the mask is not present, all fields will be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)` |   
  
### updatePlaybook(UpdatePlaybookRequest request)
    
    
    public final Playbook updatePlaybook(UpdatePlaybookRequest request)

Updates the specified Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       UpdatePlaybookRequest request =
           UpdatePlaybookRequest.newBuilder()
               .setPlaybook(Playbook.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Playbook response = playbooksClient.updatePlaybook(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdatePlaybookRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)` |   
  
### updatePlaybookCallable()
    
    
    public final UnaryCallable<UpdatePlaybookRequest,Playbook> updatePlaybookCallable()

Updates the specified Playbook.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PlaybooksClient playbooksClient = PlaybooksClient.create()) {
       UpdatePlaybookRequest request =
           UpdatePlaybookRequest.newBuilder()
               .setPlaybook(Playbook.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Playbook> future = playbooksClient.updatePlaybookCallable().futureCall(request);
       // Do something.
       Playbook response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdatePlaybookRequest),[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
