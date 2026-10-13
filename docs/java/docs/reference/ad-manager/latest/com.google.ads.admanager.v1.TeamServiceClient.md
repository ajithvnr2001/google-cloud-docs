---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TeamServiceClient
title: Class TeamServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:09:07.889274+00:00
---

# Class TeamServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TeamServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TeamServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/TeamServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `Team` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       TeamName name = TeamName.of("[NETWORK_CODE]", "[TEAM]");
       Team response = teamServiceClient.getTeam(name);
     }
     

Note: close() needs to be called on the TeamServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetTeam |  Retrieves a `Team` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTeam(GetTeamRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTeam(TeamName name) 
  * getTeam(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTeamCallable() 

  
ListTeams |  Lists `Team` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTeams(ListTeamsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTeams(NetworkName parent) 
  * listTeams(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTeamsPagedCallable() 
  * listTeamsCallable() 

  
CreateTeam |  Creates a `Team` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTeam(CreateTeamRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createTeam(NetworkName parent, Team team) 
  * createTeam(String parent, Team team) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTeamCallable() 

  
BatchCreateTeams |  Creates `Team` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateTeams(NetworkName parent, List<CreateTeamRequest> requests) 
  * batchCreateTeams(String parent, List<CreateTeamRequest> requests) 
  * batchCreateTeams(BatchCreateTeamsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateTeamsCallable() 

  
UpdateTeam |  Updates a `Team` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTeam(UpdateTeamRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateTeam(Team team, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTeamCallable() 

  
BatchUpdateTeams |  Batch updates `Team` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateTeams(NetworkName parent, List<UpdateTeamRequest> requests) 
  * batchUpdateTeams(String parent, List<UpdateTeamRequest> requests) 
  * batchUpdateTeams(BatchUpdateTeamsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateTeamsCallable() 

  
BatchActivateTeams |  Batch activates `Team` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateTeams(BatchActivateTeamsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchActivateTeams(NetworkName parent, List<String> names) 
  * batchActivateTeams(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateTeamsCallable() 

  
BatchDeactivateTeams |  Batch deactivates `Team` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivateTeams(BatchDeactivateTeamsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeactivateTeams(NetworkName parent, List<String> names) 
  * batchDeactivateTeams(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivateTeamsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of TeamServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TeamServiceSettings teamServiceSettings =
         TeamServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     TeamServiceClient teamServiceClient = TeamServiceClient.create(teamServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TeamServiceSettings teamServiceSettings =
         TeamServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     TeamServiceClient teamServiceClient = TeamServiceClient.create(teamServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TeamServiceClient

## Static Methods 

### create()
    
    
    public static final TeamServiceClient create()

Constructs an instance of TeamServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[TeamServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TeamServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TeamServiceSettings settings)
    
    
    public static final TeamServiceClient create(TeamServiceSettings settings)

Constructs an instance of TeamServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TeamServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TeamServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TeamServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TeamServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TeamServiceStub stub)
    
    
    public static final TeamServiceClient create(TeamServiceStub stub)

Constructs an instance of TeamServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(TeamServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TeamServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.TeamServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TeamServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TeamServiceClient)` |   
  
## Constructors 

### TeamServiceClient(TeamServiceSettings settings)
    
    
    protected TeamServiceClient(TeamServiceSettings settings)

Constructs an instance of TeamServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TeamServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TeamServiceSettings)`  
  
  
### TeamServiceClient(TeamServiceStub stub)
    
    
    protected TeamServiceClient(TeamServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TeamServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.TeamServiceStub)`  
  
  
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
  
### batchActivateTeams(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchActivateTeamsResponse batchActivateTeams(@Nullable NetworkName parent, List<String> names)

Batch activates `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchActivateTeamsResponse response = teamServiceClient.batchActivateTeams(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `Team`s to activate. Format: `networks/{network_code}/teams/{team_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateTeamsResponse)` |   
  
### batchActivateTeams(BatchActivateTeamsRequest request)
    
    
    public final BatchActivateTeamsResponse batchActivateTeams(BatchActivateTeamsRequest request)

Batch activates `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       BatchActivateTeamsRequest request =
           BatchActivateTeamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchActivateTeamsResponse response = teamServiceClient.batchActivateTeams(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateTeamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateTeamsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateTeamsResponse)` |   
  
### batchActivateTeams(String parent, List<String> names)
    
    
    public final BatchActivateTeamsResponse batchActivateTeams(String parent, List<String> names)

Batch activates `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchActivateTeamsResponse response = teamServiceClient.batchActivateTeams(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `Team`s to activate. Format: `networks/{network_code}/teams/{team_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateTeamsResponse)` |   
  
### batchActivateTeamsCallable()
    
    
    public final UnaryCallable<BatchActivateTeamsRequest,BatchActivateTeamsResponse> batchActivateTeamsCallable()

Batch activates `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       BatchActivateTeamsRequest request =
           BatchActivateTeamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchActivateTeamsResponse> future =
           teamServiceClient.batchActivateTeamsCallable().futureCall(request);
       // Do something.
       BatchActivateTeamsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateTeamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateTeamsRequest),[BatchActivateTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateTeamsResponse)>` |   
  
### batchCreateTeams(@Nullable NetworkName parent, List<CreateTeamRequest> requests)
    
    
    public final BatchCreateTeamsResponse batchCreateTeams(@Nullable NetworkName parent, List<CreateTeamRequest> requests)

Creates `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateTeamRequest> requests = new ArrayList<>();
       BatchCreateTeamsResponse response = teamServiceClient.batchCreateTeams(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `Teams` will be created. Format: `networks/{network_code}` The parent field in the CreateTeamRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateTeamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateTeamRequest)>`  
Required. The `Team` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateTeamsResponse)` |   
  
### batchCreateTeams(BatchCreateTeamsRequest request)
    
    
    public final BatchCreateTeamsResponse batchCreateTeams(BatchCreateTeamsRequest request)

Creates `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       BatchCreateTeamsRequest request =
           BatchCreateTeamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateTeamRequest>())
               .build();
       BatchCreateTeamsResponse response = teamServiceClient.batchCreateTeams(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateTeamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateTeamsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateTeamsResponse)` |   
  
### batchCreateTeams(String parent, List<CreateTeamRequest> requests)
    
    
    public final BatchCreateTeamsResponse batchCreateTeams(String parent, List<CreateTeamRequest> requests)

Creates `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateTeamRequest> requests = new ArrayList<>();
       BatchCreateTeamsResponse response = teamServiceClient.batchCreateTeams(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `Teams` will be created. Format: `networks/{network_code}` The parent field in the CreateTeamRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateTeamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateTeamRequest)>`  
Required. The `Team` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateTeamsResponse)` |   
  
### batchCreateTeamsCallable()
    
    
    public final UnaryCallable<BatchCreateTeamsRequest,BatchCreateTeamsResponse> batchCreateTeamsCallable()

Creates `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       BatchCreateTeamsRequest request =
           BatchCreateTeamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateTeamRequest>())
               .build();
       ApiFuture<BatchCreateTeamsResponse> future =
           teamServiceClient.batchCreateTeamsCallable().futureCall(request);
       // Do something.
       BatchCreateTeamsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateTeamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateTeamsRequest),[BatchCreateTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateTeamsResponse)>` |   
  
### batchDeactivateTeams(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDeactivateTeamsResponse batchDeactivateTeams(@Nullable NetworkName parent, List<String> names)

Batch deactivates `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDeactivateTeamsResponse response = teamServiceClient.batchDeactivateTeams(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `Team`s to deactivate. Format: `networks/{network_code}/teams/{team_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateTeamsResponse)` |   
  
### batchDeactivateTeams(BatchDeactivateTeamsRequest request)
    
    
    public final BatchDeactivateTeamsResponse batchDeactivateTeams(BatchDeactivateTeamsRequest request)

Batch deactivates `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       BatchDeactivateTeamsRequest request =
           BatchDeactivateTeamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeactivateTeamsResponse response = teamServiceClient.batchDeactivateTeams(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivateTeamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateTeamsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateTeamsResponse)` |   
  
### batchDeactivateTeams(String parent, List<String> names)
    
    
    public final BatchDeactivateTeamsResponse batchDeactivateTeams(String parent, List<String> names)

Batch deactivates `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDeactivateTeamsResponse response = teamServiceClient.batchDeactivateTeams(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `Team`s to deactivate. Format: `networks/{network_code}/teams/{team_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateTeamsResponse)` |   
  
### batchDeactivateTeamsCallable()
    
    
    public final UnaryCallable<BatchDeactivateTeamsRequest,BatchDeactivateTeamsResponse> batchDeactivateTeamsCallable()

Batch deactivates `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       BatchDeactivateTeamsRequest request =
           BatchDeactivateTeamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDeactivateTeamsResponse> future =
           teamServiceClient.batchDeactivateTeamsCallable().futureCall(request);
       // Do something.
       BatchDeactivateTeamsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivateTeamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateTeamsRequest),[BatchDeactivateTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateTeamsResponse)>` |   
  
### batchUpdateTeams(@Nullable NetworkName parent, List<UpdateTeamRequest> requests)
    
    
    public final BatchUpdateTeamsResponse batchUpdateTeams(@Nullable NetworkName parent, List<UpdateTeamRequest> requests)

Batch updates `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateTeamRequest> requests = new ArrayList<>();
       BatchUpdateTeamsResponse response = teamServiceClient.batchUpdateTeams(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `Teams` will be updated. Format: `networks/{network_code}` The parent field in the UpdateTeamRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateTeamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateTeamRequest)>`  
Required. The `Team` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateTeamsResponse)` |   
  
### batchUpdateTeams(BatchUpdateTeamsRequest request)
    
    
    public final BatchUpdateTeamsResponse batchUpdateTeams(BatchUpdateTeamsRequest request)

Batch updates `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       BatchUpdateTeamsRequest request =
           BatchUpdateTeamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateTeamRequest>())
               .build();
       BatchUpdateTeamsResponse response = teamServiceClient.batchUpdateTeams(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateTeamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateTeamsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateTeamsResponse)` |   
  
### batchUpdateTeams(String parent, List<UpdateTeamRequest> requests)
    
    
    public final BatchUpdateTeamsResponse batchUpdateTeams(String parent, List<UpdateTeamRequest> requests)

Batch updates `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateTeamRequest> requests = new ArrayList<>();
       BatchUpdateTeamsResponse response = teamServiceClient.batchUpdateTeams(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `Teams` will be updated. Format: `networks/{network_code}` The parent field in the UpdateTeamRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateTeamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateTeamRequest)>`  
Required. The `Team` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateTeamsResponse)` |   
  
### batchUpdateTeamsCallable()
    
    
    public final UnaryCallable<BatchUpdateTeamsRequest,BatchUpdateTeamsResponse> batchUpdateTeamsCallable()

Batch updates `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       BatchUpdateTeamsRequest request =
           BatchUpdateTeamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateTeamRequest>())
               .build();
       ApiFuture<BatchUpdateTeamsResponse> future =
           teamServiceClient.batchUpdateTeamsCallable().futureCall(request);
       // Do something.
       BatchUpdateTeamsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateTeamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateTeamsRequest),[BatchUpdateTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateTeamsResponse)>` |   
  
### close()
    
    
    public final void close()

### createTeam(@Nullable NetworkName parent, Team team)
    
    
    public final Team createTeam(@Nullable NetworkName parent, Team team)

Creates a `Team` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       Team team = Team.newBuilder().build();
       Team response = teamServiceClient.createTeam(parent, team);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `Team` will be created. Format: `networks/{network_code}`  
`team` | `[Team](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Team)`  
Required. The `Team` to create.  
**Returns**  
---  
**Type** | **Description**  
`[Team](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Team)` |   
  
### createTeam(CreateTeamRequest request)
    
    
    public final Team createTeam(CreateTeamRequest request)

Creates a `Team` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       CreateTeamRequest request =
           CreateTeamRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setTeam(Team.newBuilder().build())
               .build();
       Team response = teamServiceClient.createTeam(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTeamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateTeamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Team](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Team)` |   
  
### createTeam(String parent, Team team)
    
    
    public final Team createTeam(String parent, Team team)

Creates a `Team` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       Team team = Team.newBuilder().build();
       Team response = teamServiceClient.createTeam(parent, team);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `Team` will be created. Format: `networks/{network_code}`  
`team` | `[Team](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Team)`  
Required. The `Team` to create.  
**Returns**  
---  
**Type** | **Description**  
`[Team](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Team)` |   
  
### createTeamCallable()
    
    
    public final UnaryCallable<CreateTeamRequest,Team> createTeamCallable()

Creates a `Team` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       CreateTeamRequest request =
           CreateTeamRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setTeam(Team.newBuilder().build())
               .build();
       ApiFuture<Team> future = teamServiceClient.createTeamCallable().futureCall(request);
       // Do something.
       Team response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTeamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateTeamRequest),[Team](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Team)>` |   
  
### getSettings()
    
    
    public final @Nullable TeamServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.TeamServiceSettings` |   
  
### getStub()
    
    
    public TeamServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[TeamServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.TeamServiceStub)` |   
  
### getTeam(@Nullable TeamName name)
    
    
    public final Team getTeam(@Nullable TeamName name)

Retrieves a `Team` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       TeamName name = TeamName.of("[NETWORK_CODE]", "[TEAM]");
       Team response = teamServiceClient.getTeam(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.TeamName`  
Required. The resource name of the Team. Format: `networks/{network_code}/teams/{team_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Team](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Team)` |   
  
### getTeam(GetTeamRequest request)
    
    
    public final Team getTeam(GetTeamRequest request)

Retrieves a `Team` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       GetTeamRequest request =
           GetTeamRequest.newBuilder()
               .setName(TeamName.of("[NETWORK_CODE]", "[TEAM]").toString())
               .build();
       Team response = teamServiceClient.getTeam(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTeamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetTeamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Team](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Team)` |   
  
### getTeam(String name)
    
    
    public final Team getTeam(String name)

Retrieves a `Team` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       String name = TeamName.of("[NETWORK_CODE]", "[TEAM]").toString();
       Team response = teamServiceClient.getTeam(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Team. Format: `networks/{network_code}/teams/{team_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Team](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Team)` |   
  
### getTeamCallable()
    
    
    public final UnaryCallable<GetTeamRequest,Team> getTeamCallable()

Retrieves a `Team` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       GetTeamRequest request =
           GetTeamRequest.newBuilder()
               .setName(TeamName.of("[NETWORK_CODE]", "[TEAM]").toString())
               .build();
       ApiFuture<Team> future = teamServiceClient.getTeamCallable().futureCall(request);
       // Do something.
       Team response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTeamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetTeamRequest),[Team](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Team)>` |   
  
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
  
### listTeams(@Nullable NetworkName parent)
    
    
    public final TeamServiceClient.ListTeamsPagedResponse listTeams(@Nullable NetworkName parent)

Lists `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (Team element : teamServiceClient.listTeams(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Teams. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[TeamServiceClient.ListTeamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TeamServiceClient.ListTeamsPagedResponse)` |   
  
### listTeams(ListTeamsRequest request)
    
    
    public final TeamServiceClient.ListTeamsPagedResponse listTeams(ListTeamsRequest request)

Lists `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       ListTeamsRequest request =
           ListTeamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (Team element : teamServiceClient.listTeams(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTeamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListTeamsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TeamServiceClient.ListTeamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TeamServiceClient.ListTeamsPagedResponse)` |   
  
### listTeams(String parent)
    
    
    public final TeamServiceClient.ListTeamsPagedResponse listTeams(String parent)

Lists `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (Team element : teamServiceClient.listTeams(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Teams. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[TeamServiceClient.ListTeamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TeamServiceClient.ListTeamsPagedResponse)` |   
  
### listTeamsCallable()
    
    
    public final UnaryCallable<ListTeamsRequest,ListTeamsResponse> listTeamsCallable()

Lists `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       ListTeamsRequest request =
           ListTeamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListTeamsResponse response = teamServiceClient.listTeamsCallable().call(request);
         for (Team element : response.getTeamsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTeamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListTeamsRequest),[ListTeamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListTeamsResponse)>` |   
  
### listTeamsPagedCallable()
    
    
    public final UnaryCallable<ListTeamsRequest,TeamServiceClient.ListTeamsPagedResponse> listTeamsPagedCallable()

Lists `Team` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       ListTeamsRequest request =
           ListTeamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<Team> future = teamServiceClient.listTeamsPagedCallable().futureCall(request);
       // Do something.
       for (Team element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTeamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListTeamsRequest),[ListTeamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TeamServiceClient.ListTeamsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateTeam(Team team, FieldMask updateMask)
    
    
    public final Team updateTeam(Team team, FieldMask updateMask)

Updates a `Team` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       Team team = Team.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Team response = teamServiceClient.updateTeam(team, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`team` | `[Team](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Team)`  
Required. The `Team` to update. The `Team`'s `name` is used to identify the `Team` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[Team](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Team)` |   
  
### updateTeam(UpdateTeamRequest request)
    
    
    public final Team updateTeam(UpdateTeamRequest request)

Updates a `Team` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       UpdateTeamRequest request =
           UpdateTeamRequest.newBuilder()
               .setTeam(Team.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Team response = teamServiceClient.updateTeam(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTeamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateTeamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Team](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Team)` |   
  
### updateTeamCallable()
    
    
    public final UnaryCallable<UpdateTeamRequest,Team> updateTeamCallable()

Updates a `Team` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TeamServiceClient teamServiceClient = TeamServiceClient.create()) {
       UpdateTeamRequest request =
           UpdateTeamRequest.newBuilder()
               .setTeam(Team.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Team> future = teamServiceClient.updateTeamCallable().futureCall(request);
       // Do something.
       Team response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTeamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateTeamRequest),[Team](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Team)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
