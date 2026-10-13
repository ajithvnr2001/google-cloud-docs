---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfilesClient
title: Class ConversationProfilesClient (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:38.003836+00:00
---

# Class ConversationProfilesClient (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfilesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConversationProfilesClient (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow/google-cloud-dialogflow/src/main/java/com/google/cloud/dialogflow/v2/ConversationProfilesClient.java)| [Product Reference](https://cloud.google.com/dialogflow-enterprise/)  
---|---  
  
Service Description: Service for managing ConversationProfiles.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       ConversationProfileName name =
           ConversationProfileName.ofProjectConversationProfileName(
               "[PROJECT]", "[CONVERSATION_PROFILE]");
       ConversationProfile response = conversationProfilesClient.getConversationProfile(name);
     }
     

Note: close() needs to be called on the ConversationProfilesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListConversationProfiles |  Returns the list of all conversation profiles in the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listConversationProfiles(ListConversationProfilesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listConversationProfiles(LocationName parent) 
  * listConversationProfiles(ProjectName parent) 
  * listConversationProfiles(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listConversationProfilesPagedCallable() 
  * listConversationProfilesCallable() 

  
GetConversationProfile |  Retrieves the specified conversation profile. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getConversationProfile(GetConversationProfileRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getConversationProfile(ConversationProfileName name) 
  * getConversationProfile(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getConversationProfileCallable() 

  
CreateConversationProfile |  Creates a conversation profile in the specified project.  ConversationProfile.create_time and ConversationProfile.update_time aren't populated in the response. You can retrieve them via GetConversationProfile API. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createConversationProfile(CreateConversationProfileRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createConversationProfile(LocationName parent, ConversationProfile conversationProfile) 
  * createConversationProfile(ProjectName parent, ConversationProfile conversationProfile) 
  * createConversationProfile(String parent, ConversationProfile conversationProfile) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createConversationProfileCallable() 

  
UpdateConversationProfile |  Updates the specified conversation profile.  ConversationProfile.create_time and ConversationProfile.update_time aren't populated in the response. You can retrieve them via GetConversationProfile API. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateConversationProfile(UpdateConversationProfileRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateConversationProfile(ConversationProfile conversationProfile, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateConversationProfileCallable() 

  
DeleteConversationProfile |  Deletes the specified conversation profile. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteConversationProfile(DeleteConversationProfileRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteConversationProfile(ConversationProfileName name) 
  * deleteConversationProfile(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteConversationProfileCallable() 

  
SetSuggestionFeatureConfig |  Adds or updates a suggestion feature in a conversation profile. If the conversation profile contains the type of suggestion feature for the participant role, it will update it. Otherwise it will insert the suggestion feature.  This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:  \- `metadata`: SetSuggestionFeatureConfigOperationMetadata \- `response`: ConversationProfile If a long running operation to add or update suggestion feature config for the same conversation profile, participant role and suggestion feature type exists, please cancel the existing long running operation before sending such request, otherwise the request will be rejected. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setSuggestionFeatureConfigAsync(SetSuggestionFeatureConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setSuggestionFeatureConfigAsync(String conversationProfile) 
  * setSuggestionFeatureConfigAsync(String conversationProfile, Participant.Role participantRole, HumanAgentAssistantConfig.SuggestionFeatureConfig suggestionFeatureConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setSuggestionFeatureConfigOperationCallable() 
  * setSuggestionFeatureConfigCallable() 

  
ClearSuggestionFeatureConfig |  Clears a suggestion feature from a conversation profile for the given participant role.  This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:  \- `metadata`: ClearSuggestionFeatureConfigOperationMetadata \- `response`: ConversationProfile |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * clearSuggestionFeatureConfigAsync(ClearSuggestionFeatureConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * clearSuggestionFeatureConfigAsync(String conversationProfile) 
  * clearSuggestionFeatureConfigAsync(String conversationProfile, Participant.Role participantRole, SuggestionFeature.Type suggestionFeatureType) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * clearSuggestionFeatureConfigOperationCallable() 
  * clearSuggestionFeatureConfigCallable() 

  
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

This class can be customized by passing in a custom instance of ConversationProfilesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationProfilesSettings conversationProfilesSettings =
         ConversationProfilesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create(conversationProfilesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationProfilesSettings conversationProfilesSettings =
         ConversationProfilesSettings.newBuilder().setEndpoint(myEndpoint).build();
     ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create(conversationProfilesSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationProfilesSettings conversationProfilesSettings =
         ConversationProfilesSettings.newHttpJsonBuilder().build();
     ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create(conversationProfilesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ConversationProfilesClient

## Static Methods 

### create()
    
    
    public static final ConversationProfilesClient create()

Constructs an instance of ConversationProfilesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ConversationProfilesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfilesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConversationProfilesSettings settings)
    
    
    public static final ConversationProfilesClient create(ConversationProfilesSettings settings)

Constructs an instance of ConversationProfilesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConversationProfilesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfilesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversationProfilesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfilesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConversationProfilesStub stub)
    
    
    public static final ConversationProfilesClient create(ConversationProfilesStub stub)

Constructs an instance of ConversationProfilesClient, using the given stub for making calls. This is for advanced usage - prefer using create(ConversationProfilesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConversationProfilesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.ConversationProfilesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversationProfilesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfilesClient)` |   
  
## Constructors 

### ConversationProfilesClient(ConversationProfilesSettings settings)
    
    
    protected ConversationProfilesClient(ConversationProfilesSettings settings)

Constructs an instance of ConversationProfilesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConversationProfilesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfilesSettings)`  
  
  
### ConversationProfilesClient(ConversationProfilesStub stub)
    
    
    protected ConversationProfilesClient(ConversationProfilesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConversationProfilesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.ConversationProfilesStub)`  
  
  
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
  
### clearSuggestionFeatureConfigAsync(ClearSuggestionFeatureConfigRequest request)
    
    
    public final OperationFuture<ConversationProfile,ClearSuggestionFeatureConfigOperationMetadata> clearSuggestionFeatureConfigAsync(ClearSuggestionFeatureConfigRequest request)

Clears a suggestion feature from a conversation profile for the given participant role.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: ClearSuggestionFeatureConfigOperationMetadata

  * `response`: ConversationProfile

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationProfilesClient conversationProfilesClient =
          ConversationProfilesClient.create()) {
        ClearSuggestionFeatureConfigRequest request =
            ClearSuggestionFeatureConfigRequest.newBuilder()
                .setConversationProfile("conversationProfile1691597734")
                .build();
        ConversationProfile response =
            conversationProfilesClient.clearSuggestionFeatureConfigAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[ClearSuggestionFeatureConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ClearSuggestionFeatureConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile),[ClearSuggestionFeatureConfigOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ClearSuggestionFeatureConfigOperationMetadata)>` |   
  
### clearSuggestionFeatureConfigAsync(String conversationProfile)
    
    
    public final OperationFuture<ConversationProfile,ClearSuggestionFeatureConfigOperationMetadata> clearSuggestionFeatureConfigAsync(String conversationProfile)

Clears a suggestion feature from a conversation profile for the given participant role.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: ClearSuggestionFeatureConfigOperationMetadata

  * `response`: ConversationProfile

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationProfilesClient conversationProfilesClient =
          ConversationProfilesClient.create()) {
        String conversationProfile = "conversationProfile1691597734";
        ConversationProfile response =
            conversationProfilesClient.clearSuggestionFeatureConfigAsync(conversationProfile).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`conversationProfile` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Conversation Profile to add or update the suggestion feature config. Format: `projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile),[ClearSuggestionFeatureConfigOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ClearSuggestionFeatureConfigOperationMetadata)>` |   
  
### clearSuggestionFeatureConfigAsync(String conversationProfile, Participant.Role participantRole, SuggestionFeature.Type suggestionFeatureType)
    
    
    public final OperationFuture<ConversationProfile,ClearSuggestionFeatureConfigOperationMetadata> clearSuggestionFeatureConfigAsync(String conversationProfile, Participant.Role participantRole, SuggestionFeature.Type suggestionFeatureType)

Clears a suggestion feature from a conversation profile for the given participant role.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: ClearSuggestionFeatureConfigOperationMetadata

  * `response`: ConversationProfile

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationProfilesClient conversationProfilesClient =
          ConversationProfilesClient.create()) {
        String conversationProfile = "conversationProfile1691597734";
        Participant.Role participantRole = Participant.Role.forNumber(0);
        SuggestionFeature.Type suggestionFeatureType = SuggestionFeature.Type.forNumber(0);
        ConversationProfile response =
            conversationProfilesClient
                .clearSuggestionFeatureConfigAsync(
                    conversationProfile, participantRole, suggestionFeatureType)
                .get();
        }
        




**Parameters**  
---  
**Name** | **Description**  
`conversationProfile` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Conversation Profile to add or update the suggestion feature config. Format: `projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>`.  
`participantRole` | `[Participant.Role](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Participant.Role)`  
Required. The participant role to remove the suggestion feature config. Only HUMAN_AGENT or END_USER can be used.  
`suggestionFeatureType` | `[SuggestionFeature.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestionFeature.Type)`  
Required. The type of the suggestion feature to remove.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile),[ClearSuggestionFeatureConfigOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ClearSuggestionFeatureConfigOperationMetadata)>` |   
  
### clearSuggestionFeatureConfigCallable()
    
    
    public final UnaryCallable<ClearSuggestionFeatureConfigRequest,Operation> clearSuggestionFeatureConfigCallable()

Clears a suggestion feature from a conversation profile for the given participant role.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: ClearSuggestionFeatureConfigOperationMetadata

  * `response`: ConversationProfile

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationProfilesClient conversationProfilesClient =
          ConversationProfilesClient.create()) {
        ClearSuggestionFeatureConfigRequest request =
            ClearSuggestionFeatureConfigRequest.newBuilder()
                .setConversationProfile("conversationProfile1691597734")
                .build();
        ApiFuture<Operation> future =
            conversationProfilesClient.clearSuggestionFeatureConfigCallable().futureCall(request);
        // Do something.
        Operation response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ClearSuggestionFeatureConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ClearSuggestionFeatureConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### clearSuggestionFeatureConfigOperationCallable()
    
    
    public final OperationCallable<ClearSuggestionFeatureConfigRequest,ConversationProfile,ClearSuggestionFeatureConfigOperationMetadata> clearSuggestionFeatureConfigOperationCallable()

Clears a suggestion feature from a conversation profile for the given participant role.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: ClearSuggestionFeatureConfigOperationMetadata

  * `response`: ConversationProfile

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationProfilesClient conversationProfilesClient =
          ConversationProfilesClient.create()) {
        ClearSuggestionFeatureConfigRequest request =
            ClearSuggestionFeatureConfigRequest.newBuilder()
                .setConversationProfile("conversationProfile1691597734")
                .build();
        OperationFuture<ConversationProfile, ClearSuggestionFeatureConfigOperationMetadata> future =
            conversationProfilesClient
                .clearSuggestionFeatureConfigOperationCallable()
                .futureCall(request);
        // Do something.
        ConversationProfile response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ClearSuggestionFeatureConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ClearSuggestionFeatureConfigRequest),[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile),[ClearSuggestionFeatureConfigOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ClearSuggestionFeatureConfigOperationMetadata)>` |   
  
### close()
    
    
    public final void close()

### createConversationProfile(@Nullable LocationName parent, ConversationProfile conversationProfile)
    
    
    public final ConversationProfile createConversationProfile(@Nullable LocationName parent, ConversationProfile conversationProfile)

Creates a conversation profile in the specified project.

ConversationProfile.create_time and ConversationProfile.update_time aren't populated in the response. You can retrieve them via GetConversationProfile API.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ConversationProfile conversationProfile = ConversationProfile.newBuilder().build();
       ConversationProfile response =
           conversationProfilesClient.createConversationProfile(parent, conversationProfile);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.LocationName`  
Required. The project to create a conversation profile for. Format: `projects/<Project ID>/locations/<Location ID>`.  
`conversationProfile` | `[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile)`  
Required. The conversation profile to create.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile)` |   
  
### createConversationProfile(@Nullable ProjectName parent, ConversationProfile conversationProfile)
    
    
    public final ConversationProfile createConversationProfile(@Nullable ProjectName parent, ConversationProfile conversationProfile)

Creates a conversation profile in the specified project.

ConversationProfile.create_time and ConversationProfile.update_time aren't populated in the response. You can retrieve them via GetConversationProfile API.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       ConversationProfile conversationProfile = ConversationProfile.newBuilder().build();
       ConversationProfile response =
           conversationProfilesClient.createConversationProfile(parent, conversationProfile);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ProjectName`  
Required. The project to create a conversation profile for. Format: `projects/<Project ID>/locations/<Location ID>`.  
`conversationProfile` | `[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile)`  
Required. The conversation profile to create.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile)` |   
  
### createConversationProfile(CreateConversationProfileRequest request)
    
    
    public final ConversationProfile createConversationProfile(CreateConversationProfileRequest request)

Creates a conversation profile in the specified project.

ConversationProfile.create_time and ConversationProfile.update_time aren't populated in the response. You can retrieve them via GetConversationProfile API.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       CreateConversationProfileRequest request =
           CreateConversationProfileRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setConversationProfile(ConversationProfile.newBuilder().build())
               .build();
       ConversationProfile response = conversationProfilesClient.createConversationProfile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateConversationProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile)` |   
  
### createConversationProfile(String parent, ConversationProfile conversationProfile)
    
    
    public final ConversationProfile createConversationProfile(String parent, ConversationProfile conversationProfile)

Creates a conversation profile in the specified project.

ConversationProfile.create_time and ConversationProfile.update_time aren't populated in the response. You can retrieve them via GetConversationProfile API.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       ConversationProfile conversationProfile = ConversationProfile.newBuilder().build();
       ConversationProfile response =
           conversationProfilesClient.createConversationProfile(parent, conversationProfile);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project to create a conversation profile for. Format: `projects/<Project ID>/locations/<Location ID>`.  
`conversationProfile` | `[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile)`  
Required. The conversation profile to create.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile)` |   
  
### createConversationProfileCallable()
    
    
    public final UnaryCallable<CreateConversationProfileRequest,ConversationProfile> createConversationProfileCallable()

Creates a conversation profile in the specified project.

ConversationProfile.create_time and ConversationProfile.update_time aren't populated in the response. You can retrieve them via GetConversationProfile API.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       CreateConversationProfileRequest request =
           CreateConversationProfileRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setConversationProfile(ConversationProfile.newBuilder().build())
               .build();
       ApiFuture<ConversationProfile> future =
           conversationProfilesClient.createConversationProfileCallable().futureCall(request);
       // Do something.
       ConversationProfile response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateConversationProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationProfileRequest),[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile)>` |   
  
### deleteConversationProfile(@Nullable ConversationProfileName name)
    
    
    public final void deleteConversationProfile(@Nullable ConversationProfileName name)

Deletes the specified conversation profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       ConversationProfileName name =
           ConversationProfileName.ofProjectConversationProfileName(
               "[PROJECT]", "[CONVERSATION_PROFILE]");
       conversationProfilesClient.deleteConversationProfile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationProfileName`  
Required. The name of the conversation profile to delete. Format: `projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>`.  
  
### deleteConversationProfile(DeleteConversationProfileRequest request)
    
    
    public final void deleteConversationProfile(DeleteConversationProfileRequest request)

Deletes the specified conversation profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       DeleteConversationProfileRequest request =
           DeleteConversationProfileRequest.newBuilder()
               .setName(
                   ConversationProfileName.ofProjectConversationProfileName(
                           "[PROJECT]", "[CONVERSATION_PROFILE]")
                       .toString())
               .build();
       conversationProfilesClient.deleteConversationProfile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteConversationProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteConversationProfileRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteConversationProfile(String name)
    
    
    public final void deleteConversationProfile(String name)

Deletes the specified conversation profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       String name =
           ConversationProfileName.ofProjectConversationProfileName(
                   "[PROJECT]", "[CONVERSATION_PROFILE]")
               .toString();
       conversationProfilesClient.deleteConversationProfile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the conversation profile to delete. Format: `projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>`.  
  
### deleteConversationProfileCallable()
    
    
    public final UnaryCallable<DeleteConversationProfileRequest,Empty> deleteConversationProfileCallable()

Deletes the specified conversation profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       DeleteConversationProfileRequest request =
           DeleteConversationProfileRequest.newBuilder()
               .setName(
                   ConversationProfileName.ofProjectConversationProfileName(
                           "[PROJECT]", "[CONVERSATION_PROFILE]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           conversationProfilesClient.deleteConversationProfileCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteConversationProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteConversationProfileRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getConversationProfile(@Nullable ConversationProfileName name)
    
    
    public final ConversationProfile getConversationProfile(@Nullable ConversationProfileName name)

Retrieves the specified conversation profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       ConversationProfileName name =
           ConversationProfileName.ofProjectConversationProfileName(
               "[PROJECT]", "[CONVERSATION_PROFILE]");
       ConversationProfile response = conversationProfilesClient.getConversationProfile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationProfileName`  
Required. The resource name of the conversation profile. Format: `projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile)` |   
  
### getConversationProfile(GetConversationProfileRequest request)
    
    
    public final ConversationProfile getConversationProfile(GetConversationProfileRequest request)

Retrieves the specified conversation profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       GetConversationProfileRequest request =
           GetConversationProfileRequest.newBuilder()
               .setName(
                   ConversationProfileName.ofProjectConversationProfileName(
                           "[PROJECT]", "[CONVERSATION_PROFILE]")
                       .toString())
               .build();
       ConversationProfile response = conversationProfilesClient.getConversationProfile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConversationProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetConversationProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile)` |   
  
### getConversationProfile(String name)
    
    
    public final ConversationProfile getConversationProfile(String name)

Retrieves the specified conversation profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       String name =
           ConversationProfileName.ofProjectConversationProfileName(
                   "[PROJECT]", "[CONVERSATION_PROFILE]")
               .toString();
       ConversationProfile response = conversationProfilesClient.getConversationProfile(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the conversation profile. Format: `projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile)` |   
  
### getConversationProfileCallable()
    
    
    public final UnaryCallable<GetConversationProfileRequest,ConversationProfile> getConversationProfileCallable()

Retrieves the specified conversation profile.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       GetConversationProfileRequest request =
           GetConversationProfileRequest.newBuilder()
               .setName(
                   ConversationProfileName.ofProjectConversationProfileName(
                           "[PROJECT]", "[CONVERSATION_PROFILE]")
                       .toString())
               .build();
       ApiFuture<ConversationProfile> future =
           conversationProfilesClient.getConversationProfileCallable().futureCall(request);
       // Do something.
       ConversationProfile response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConversationProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetConversationProfileRequest),[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile)>` |   
  
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
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = conversationProfilesClient.getLocation(request);
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
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           conversationProfilesClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable ConversationProfilesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationProfilesSettings` |   
  
### getStub()
    
    
    public ConversationProfilesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ConversationProfilesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.ConversationProfilesStub)` |   
  
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
  
### listConversationProfiles(@Nullable LocationName parent)
    
    
    public final ConversationProfilesClient.ListConversationProfilesPagedResponse listConversationProfiles(@Nullable LocationName parent)

Returns the list of all conversation profiles in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ConversationProfile element :
           conversationProfilesClient.listConversationProfiles(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.LocationName`  
Required. The project to list all conversation profiles from. Format: `projects/<Project ID>/locations/<Location ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationProfilesClient.ListConversationProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfilesClient.ListConversationProfilesPagedResponse)` |   
  
### listConversationProfiles(@Nullable ProjectName parent)
    
    
    public final ConversationProfilesClient.ListConversationProfilesPagedResponse listConversationProfiles(@Nullable ProjectName parent)

Returns the list of all conversation profiles in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (ConversationProfile element :
           conversationProfilesClient.listConversationProfiles(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ProjectName`  
Required. The project to list all conversation profiles from. Format: `projects/<Project ID>/locations/<Location ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationProfilesClient.ListConversationProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfilesClient.ListConversationProfilesPagedResponse)` |   
  
### listConversationProfiles(ListConversationProfilesRequest request)
    
    
    public final ConversationProfilesClient.ListConversationProfilesPagedResponse listConversationProfiles(ListConversationProfilesRequest request)

Returns the list of all conversation profiles in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       ListConversationProfilesRequest request =
           ListConversationProfilesRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ConversationProfile element :
           conversationProfilesClient.listConversationProfiles(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListConversationProfilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationProfilesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationProfilesClient.ListConversationProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfilesClient.ListConversationProfilesPagedResponse)` |   
  
### listConversationProfiles(String parent)
    
    
    public final ConversationProfilesClient.ListConversationProfilesPagedResponse listConversationProfiles(String parent)

Returns the list of all conversation profiles in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (ConversationProfile element :
           conversationProfilesClient.listConversationProfiles(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project to list all conversation profiles from. Format: `projects/<Project ID>/locations/<Location ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationProfilesClient.ListConversationProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfilesClient.ListConversationProfilesPagedResponse)` |   
  
### listConversationProfilesCallable()
    
    
    public final UnaryCallable<ListConversationProfilesRequest,ListConversationProfilesResponse> listConversationProfilesCallable()

Returns the list of all conversation profiles in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       ListConversationProfilesRequest request =
           ListConversationProfilesRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListConversationProfilesResponse response =
             conversationProfilesClient.listConversationProfilesCallable().call(request);
         for (ConversationProfile element : response.getConversationProfilesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversationProfilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationProfilesRequest),[ListConversationProfilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationProfilesResponse)>` |   
  
### listConversationProfilesPagedCallable()
    
    
    public final UnaryCallable<ListConversationProfilesRequest,ConversationProfilesClient.ListConversationProfilesPagedResponse> listConversationProfilesPagedCallable()

Returns the list of all conversation profiles in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       ListConversationProfilesRequest request =
           ListConversationProfilesRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ConversationProfile> future =
           conversationProfilesClient.listConversationProfilesPagedCallable().futureCall(request);
       // Do something.
       for (ConversationProfile element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversationProfilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationProfilesRequest),[ListConversationProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfilesClient.ListConversationProfilesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final ConversationProfilesClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : conversationProfilesClient.listLocations(request).iterateAll()) {
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
`[ConversationProfilesClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfilesClient.ListLocationsPagedResponse)` |   
  
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
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             conversationProfilesClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,ConversationProfilesClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           conversationProfilesClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfilesClient.ListLocationsPagedResponse)>` |   
  
### setSuggestionFeatureConfigAsync(SetSuggestionFeatureConfigRequest request)
    
    
    public final OperationFuture<ConversationProfile,SetSuggestionFeatureConfigOperationMetadata> setSuggestionFeatureConfigAsync(SetSuggestionFeatureConfigRequest request)

Adds or updates a suggestion feature in a conversation profile. If the conversation profile contains the type of suggestion feature for the participant role, it will update it. Otherwise it will insert the suggestion feature.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: SetSuggestionFeatureConfigOperationMetadata

  * `response`: ConversationProfile

If a long running operation to add or update suggestion feature config for the same conversation profile, participant role and suggestion feature type exists, please cancel the existing long running operation before sending such request, otherwise the request will be rejected.

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationProfilesClient conversationProfilesClient =
          ConversationProfilesClient.create()) {
        SetSuggestionFeatureConfigRequest request =
            SetSuggestionFeatureConfigRequest.newBuilder()
                .setConversationProfile("conversationProfile1691597734")
                .setSuggestionFeatureConfig(
                    HumanAgentAssistantConfig.SuggestionFeatureConfig.newBuilder().build())
                .build();
        ConversationProfile response =
            conversationProfilesClient.setSuggestionFeatureConfigAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetSuggestionFeatureConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SetSuggestionFeatureConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile),[SetSuggestionFeatureConfigOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SetSuggestionFeatureConfigOperationMetadata)>` |   
  
### setSuggestionFeatureConfigAsync(String conversationProfile)
    
    
    public final OperationFuture<ConversationProfile,SetSuggestionFeatureConfigOperationMetadata> setSuggestionFeatureConfigAsync(String conversationProfile)

Adds or updates a suggestion feature in a conversation profile. If the conversation profile contains the type of suggestion feature for the participant role, it will update it. Otherwise it will insert the suggestion feature.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: SetSuggestionFeatureConfigOperationMetadata

  * `response`: ConversationProfile

If a long running operation to add or update suggestion feature config for the same conversation profile, participant role and suggestion feature type exists, please cancel the existing long running operation before sending such request, otherwise the request will be rejected.

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationProfilesClient conversationProfilesClient =
          ConversationProfilesClient.create()) {
        String conversationProfile = "conversationProfile1691597734";
        ConversationProfile response =
            conversationProfilesClient.setSuggestionFeatureConfigAsync(conversationProfile).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`conversationProfile` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Conversation Profile to add or update the suggestion feature config. Format: `projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile),[SetSuggestionFeatureConfigOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SetSuggestionFeatureConfigOperationMetadata)>` |   
  
### setSuggestionFeatureConfigAsync(String conversationProfile, Participant.Role participantRole, HumanAgentAssistantConfig.SuggestionFeatureConfig suggestionFeatureConfig)
    
    
    public final OperationFuture<ConversationProfile,SetSuggestionFeatureConfigOperationMetadata> setSuggestionFeatureConfigAsync(String conversationProfile, Participant.Role participantRole, HumanAgentAssistantConfig.SuggestionFeatureConfig suggestionFeatureConfig)

Adds or updates a suggestion feature in a conversation profile. If the conversation profile contains the type of suggestion feature for the participant role, it will update it. Otherwise it will insert the suggestion feature.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: SetSuggestionFeatureConfigOperationMetadata

  * `response`: ConversationProfile

If a long running operation to add or update suggestion feature config for the same conversation profile, participant role and suggestion feature type exists, please cancel the existing long running operation before sending such request, otherwise the request will be rejected.

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationProfilesClient conversationProfilesClient =
          ConversationProfilesClient.create()) {
        String conversationProfile = "conversationProfile1691597734";
        Participant.Role participantRole = Participant.Role.forNumber(0);
        HumanAgentAssistantConfig.SuggestionFeatureConfig suggestionFeatureConfig =
            HumanAgentAssistantConfig.SuggestionFeatureConfig.newBuilder().build();
        ConversationProfile response =
            conversationProfilesClient
                .setSuggestionFeatureConfigAsync(
                    conversationProfile, participantRole, suggestionFeatureConfig)
                .get();
        }
        




**Parameters**  
---  
**Name** | **Description**  
`conversationProfile` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Conversation Profile to add or update the suggestion feature config. Format: `projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>`.  
`participantRole` | `[Participant.Role](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Participant.Role)`  
Required. The participant role to add or update the suggestion feature config. Only HUMAN_AGENT or END_USER can be used.  
`suggestionFeatureConfig` | `[HumanAgentAssistantConfig.SuggestionFeatureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionFeatureConfig)`  
Required. The suggestion feature config to add or update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile),[SetSuggestionFeatureConfigOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SetSuggestionFeatureConfigOperationMetadata)>` |   
  
### setSuggestionFeatureConfigCallable()
    
    
    public final UnaryCallable<SetSuggestionFeatureConfigRequest,Operation> setSuggestionFeatureConfigCallable()

Adds or updates a suggestion feature in a conversation profile. If the conversation profile contains the type of suggestion feature for the participant role, it will update it. Otherwise it will insert the suggestion feature.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: SetSuggestionFeatureConfigOperationMetadata

  * `response`: ConversationProfile

If a long running operation to add or update suggestion feature config for the same conversation profile, participant role and suggestion feature type exists, please cancel the existing long running operation before sending such request, otherwise the request will be rejected.

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationProfilesClient conversationProfilesClient =
          ConversationProfilesClient.create()) {
        SetSuggestionFeatureConfigRequest request =
            SetSuggestionFeatureConfigRequest.newBuilder()
                .setConversationProfile("conversationProfile1691597734")
                .setSuggestionFeatureConfig(
                    HumanAgentAssistantConfig.SuggestionFeatureConfig.newBuilder().build())
                .build();
        ApiFuture<Operation> future =
            conversationProfilesClient.setSuggestionFeatureConfigCallable().futureCall(request);
        // Do something.
        Operation response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetSuggestionFeatureConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SetSuggestionFeatureConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### setSuggestionFeatureConfigOperationCallable()
    
    
    public final OperationCallable<SetSuggestionFeatureConfigRequest,ConversationProfile,SetSuggestionFeatureConfigOperationMetadata> setSuggestionFeatureConfigOperationCallable()

Adds or updates a suggestion feature in a conversation profile. If the conversation profile contains the type of suggestion feature for the participant role, it will update it. Otherwise it will insert the suggestion feature.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

\- `metadata`: SetSuggestionFeatureConfigOperationMetadata

  * `response`: ConversationProfile

If a long running operation to add or update suggestion feature config for the same conversation profile, participant role and suggestion feature type exists, please cancel the existing long running operation before sending such request, otherwise the request will be rejected.

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ConversationProfilesClient conversationProfilesClient =
          ConversationProfilesClient.create()) {
        SetSuggestionFeatureConfigRequest request =
            SetSuggestionFeatureConfigRequest.newBuilder()
                .setConversationProfile("conversationProfile1691597734")
                .setSuggestionFeatureConfig(
                    HumanAgentAssistantConfig.SuggestionFeatureConfig.newBuilder().build())
                .build();
        OperationFuture<ConversationProfile, SetSuggestionFeatureConfigOperationMetadata> future =
            conversationProfilesClient
                .setSuggestionFeatureConfigOperationCallable()
                .futureCall(request);
        // Do something.
        ConversationProfile response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetSuggestionFeatureConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SetSuggestionFeatureConfigRequest),[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile),[SetSuggestionFeatureConfigOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SetSuggestionFeatureConfigOperationMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateConversationProfile(ConversationProfile conversationProfile, FieldMask updateMask)
    
    
    public final ConversationProfile updateConversationProfile(ConversationProfile conversationProfile, FieldMask updateMask)

Updates the specified conversation profile.

ConversationProfile.create_time and ConversationProfile.update_time aren't populated in the response. You can retrieve them via GetConversationProfile API.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       ConversationProfile conversationProfile = ConversationProfile.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ConversationProfile response =
           conversationProfilesClient.updateConversationProfile(conversationProfile, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`conversationProfile` | `[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile)`  
Required. The conversation profile to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The mask to control which fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile)` |   
  
### updateConversationProfile(UpdateConversationProfileRequest request)
    
    
    public final ConversationProfile updateConversationProfile(UpdateConversationProfileRequest request)

Updates the specified conversation profile.

ConversationProfile.create_time and ConversationProfile.update_time aren't populated in the response. You can retrieve them via GetConversationProfile API.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       UpdateConversationProfileRequest request =
           UpdateConversationProfileRequest.newBuilder()
               .setConversationProfile(ConversationProfile.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ConversationProfile response = conversationProfilesClient.updateConversationProfile(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateConversationProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateConversationProfileRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile)` |   
  
### updateConversationProfileCallable()
    
    
    public final UnaryCallable<UpdateConversationProfileRequest,ConversationProfile> updateConversationProfileCallable()

Updates the specified conversation profile.

ConversationProfile.create_time and ConversationProfile.update_time aren't populated in the response. You can retrieve them via GetConversationProfile API.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationProfilesClient conversationProfilesClient =
         ConversationProfilesClient.create()) {
       UpdateConversationProfileRequest request =
           UpdateConversationProfileRequest.newBuilder()
               .setConversationProfile(ConversationProfile.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<ConversationProfile> future =
           conversationProfilesClient.updateConversationProfileCallable().futureCall(request);
       // Do something.
       ConversationProfile response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateConversationProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateConversationProfileRequest),[ConversationProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationProfile)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
