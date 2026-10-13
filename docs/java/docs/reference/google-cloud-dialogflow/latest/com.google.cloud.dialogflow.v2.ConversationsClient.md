---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsClient
title: Class ConversationsClient (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:35.105363+00:00
---

# Class ConversationsClient (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConversationsClient (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow/google-cloud-dialogflow/src/main/java/com/google/cloud/dialogflow/v2/ConversationsClient.java)| [Product Reference](https://cloud.google.com/dialogflow-enterprise/)  
---|---  
  
Service Description: Service for managing Conversations.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Conversation conversation = Conversation.newBuilder().build();
       Conversation response = conversationsClient.createConversation(parent, conversation);
     }
     

Note: close() needs to be called on the ConversationsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateConversation |  Creates a new conversation. Conversations are auto-completed after 24 hours.  Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.  For Automated Agent Stage, there will be a dialogflow agent responding to user queries.  For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.  If Conversation.conversation_profile is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an Intent with Intent.live_agent_handoff is triggered, conversation will transfer to Assist Stage. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createConversation(CreateConversationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createConversation(LocationName parent, Conversation conversation) 
  * createConversation(ProjectName parent, Conversation conversation) 
  * createConversation(String parent, Conversation conversation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createConversationCallable() 

  
ListConversations |  Returns the list of all conversations in the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listConversations(ListConversationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listConversations(LocationName parent) 
  * listConversations(ProjectName parent) 
  * listConversations(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listConversationsPagedCallable() 
  * listConversationsCallable() 

  
GetConversation |  Retrieves the specific conversation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getConversation(GetConversationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getConversation(ConversationName name) 
  * getConversation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getConversationCallable() 

  
CompleteConversation |  Completes the specified conversation. Finished conversations are purged from the database after 30 days. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * completeConversation(CompleteConversationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * completeConversation(ConversationName name) 
  * completeConversation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * completeConversationCallable() 

  
IngestContextReferences |  Data ingestion API. Ingests context references for an existing conversation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * ingestContextReferences(IngestContextReferencesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * ingestContextReferences(ConversationName conversation, Map<String, Conversation.ContextReference> contextReferences) 
  * ingestContextReferences(String conversation, Map<String, Conversation.ContextReference> contextReferences) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * ingestContextReferencesCallable() 

  
ListMessages |  Lists messages that belong to a given conversation. `messages` are ordered by `create_time` in descending order. To fetch updates without duplication, send request with filter `create_time_epoch_microseconds > [first item's create_time of previous request]` and empty page_token. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMessages(ListMessagesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMessages(ConversationName parent) 
  * listMessages(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMessagesPagedCallable() 
  * listMessagesCallable() 

  
SuggestConversationSummary |  Suggests summary for a conversation based on specific historical messages. The range of the messages to be used for summary can be specified in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * suggestConversationSummary(SuggestConversationSummaryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * suggestConversationSummary(ConversationName conversation) 
  * suggestConversationSummary(String conversation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * suggestConversationSummaryCallable() 

  
GenerateStatelessSummary |  Generates and returns a summary for a conversation that does not have a resource created for it. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * generateStatelessSummary(GenerateStatelessSummaryRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * generateStatelessSummaryCallable() 

  
GenerateStatelessSuggestion |  Generates and returns a suggestion for a conversation that does not have a resource created for it. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * generateStatelessSuggestion(GenerateStatelessSuggestionRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * generateStatelessSuggestionCallable() 

  
SearchKnowledge |  Get answers for the given query based on knowledge documents. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchKnowledge(SearchKnowledgeRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchKnowledgeCallable() 

  
GenerateSuggestions |  Generates all the suggestions using generators configured in the conversation profile. A generator is used only if its trigger event is matched. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * generateSuggestions(GenerateSuggestionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * generateSuggestions(ConversationName conversation) 
  * generateSuggestions(String conversation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * generateSuggestionsCallable() 

  
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

This class can be customized by passing in a custom instance of ConversationsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationsSettings conversationsSettings =
         ConversationsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ConversationsClient conversationsClient = ConversationsClient.create(conversationsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationsSettings conversationsSettings =
         ConversationsSettings.newBuilder().setEndpoint(myEndpoint).build();
     ConversationsClient conversationsClient = ConversationsClient.create(conversationsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationsSettings conversationsSettings =
         ConversationsSettings.newHttpJsonBuilder().build();
     ConversationsClient conversationsClient = ConversationsClient.create(conversationsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ConversationsClient

## Static Methods 

### create()
    
    
    public static final ConversationsClient create()

Constructs an instance of ConversationsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ConversationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConversationsSettings settings)
    
    
    public static final ConversationsClient create(ConversationsSettings settings)

Constructs an instance of ConversationsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConversationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConversationsStub stub)
    
    
    public static final ConversationsClient create(ConversationsStub stub)

Constructs an instance of ConversationsClient, using the given stub for making calls. This is for advanced usage - prefer using create(ConversationsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConversationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.ConversationsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsClient)` |   
  
## Constructors 

### ConversationsClient(ConversationsSettings settings)
    
    
    protected ConversationsClient(ConversationsSettings settings)

Constructs an instance of ConversationsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConversationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsSettings)`  
  
  
### ConversationsClient(ConversationsStub stub)
    
    
    protected ConversationsClient(ConversationsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConversationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.ConversationsStub)`  
  
  
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

### completeConversation(@Nullable ConversationName name)
    
    
    public final Conversation completeConversation(@Nullable ConversationName name)

Completes the specified conversation. Finished conversations are purged from the database after 30 days.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ConversationName name =
           ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]");
       Conversation response = conversationsClient.completeConversation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationName`  
Required. Resource identifier of the conversation to close. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation)` |   
  
### completeConversation(CompleteConversationRequest request)
    
    
    public final Conversation completeConversation(CompleteConversationRequest request)

Completes the specified conversation. Finished conversations are purged from the database after 30 days.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       CompleteConversationRequest request =
           CompleteConversationRequest.newBuilder()
               .setName(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .build();
       Conversation response = conversationsClient.completeConversation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CompleteConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompleteConversationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation)` |   
  
### completeConversation(String name)
    
    
    public final Conversation completeConversation(String name)

Completes the specified conversation. Finished conversations are purged from the database after 30 days.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       String name =
           ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]").toString();
       Conversation response = conversationsClient.completeConversation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource identifier of the conversation to close. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation)` |   
  
### completeConversationCallable()
    
    
    public final UnaryCallable<CompleteConversationRequest,Conversation> completeConversationCallable()

Completes the specified conversation. Finished conversations are purged from the database after 30 days.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       CompleteConversationRequest request =
           CompleteConversationRequest.newBuilder()
               .setName(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .build();
       ApiFuture<Conversation> future =
           conversationsClient.completeConversationCallable().futureCall(request);
       // Do something.
       Conversation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CompleteConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CompleteConversationRequest),[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation)>` |   
  
### createConversation(@Nullable LocationName parent, Conversation conversation)
    
    
    public final Conversation createConversation(@Nullable LocationName parent, Conversation conversation)

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If Conversation.conversation_profile is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an Intent with Intent.live_agent_handoff is triggered, conversation will transfer to Assist Stage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Conversation conversation = Conversation.newBuilder().build();
       Conversation response = conversationsClient.createConversation(parent, conversation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.LocationName`  
Required. Resource identifier of the project creating the conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`conversation` | `[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation)`  
Required. The conversation to create.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation)` |   
  
### createConversation(@Nullable ProjectName parent, Conversation conversation)
    
    
    public final Conversation createConversation(@Nullable ProjectName parent, Conversation conversation)

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If Conversation.conversation_profile is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an Intent with Intent.live_agent_handoff is triggered, conversation will transfer to Assist Stage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       Conversation conversation = Conversation.newBuilder().build();
       Conversation response = conversationsClient.createConversation(parent, conversation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ProjectName`  
Required. Resource identifier of the project creating the conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`conversation` | `[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation)`  
Required. The conversation to create.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation)` |   
  
### createConversation(CreateConversationRequest request)
    
    
    public final Conversation createConversation(CreateConversationRequest request)

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If Conversation.conversation_profile is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an Intent with Intent.live_agent_handoff is triggered, conversation will transfer to Assist Stage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       CreateConversationRequest request =
           CreateConversationRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setConversation(Conversation.newBuilder().build())
               .setConversationId("conversationId-1676095234")
               .build();
       Conversation response = conversationsClient.createConversation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation)` |   
  
### createConversation(String parent, Conversation conversation)
    
    
    public final Conversation createConversation(String parent, Conversation conversation)

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If Conversation.conversation_profile is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an Intent with Intent.live_agent_handoff is triggered, conversation will transfer to Assist Stage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       Conversation conversation = Conversation.newBuilder().build();
       Conversation response = conversationsClient.createConversation(parent, conversation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource identifier of the project creating the conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`conversation` | `[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation)`  
Required. The conversation to create.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation)` |   
  
### createConversationCallable()
    
    
    public final UnaryCallable<CreateConversationRequest,Conversation> createConversationCallable()

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If Conversation.conversation_profile is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an Intent with Intent.live_agent_handoff is triggered, conversation will transfer to Assist Stage.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       CreateConversationRequest request =
           CreateConversationRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setConversation(Conversation.newBuilder().build())
               .setConversationId("conversationId-1676095234")
               .build();
       ApiFuture<Conversation> future =
           conversationsClient.createConversationCallable().futureCall(request);
       // Do something.
       Conversation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateConversationRequest),[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation)>` |   
  
### generateStatelessSuggestion(GenerateStatelessSuggestionRequest request)
    
    
    public final GenerateStatelessSuggestionResponse generateStatelessSuggestion(GenerateStatelessSuggestionRequest request)

Generates and returns a suggestion for a conversation that does not have a resource created for it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       GenerateStatelessSuggestionRequest request =
           GenerateStatelessSuggestionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .putAllContextReferences(new HashMap<String, Conversation.ContextReference>())
               .setConversationContext(ConversationContext.newBuilder().build())
               .addAllTriggerEvents(new ArrayList<TriggerEvent>())
               .setSecuritySettings("securitySettings-1062971517")
               .build();
       GenerateStatelessSuggestionResponse response =
           conversationsClient.generateStatelessSuggestion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateStatelessSuggestionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GenerateStatelessSuggestionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateStatelessSuggestionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GenerateStatelessSuggestionResponse)` |   
  
### generateStatelessSuggestionCallable()
    
    
    public final UnaryCallable<GenerateStatelessSuggestionRequest,GenerateStatelessSuggestionResponse> generateStatelessSuggestionCallable()

Generates and returns a suggestion for a conversation that does not have a resource created for it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       GenerateStatelessSuggestionRequest request =
           GenerateStatelessSuggestionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .putAllContextReferences(new HashMap<String, Conversation.ContextReference>())
               .setConversationContext(ConversationContext.newBuilder().build())
               .addAllTriggerEvents(new ArrayList<TriggerEvent>())
               .setSecuritySettings("securitySettings-1062971517")
               .build();
       ApiFuture<GenerateStatelessSuggestionResponse> future =
           conversationsClient.generateStatelessSuggestionCallable().futureCall(request);
       // Do something.
       GenerateStatelessSuggestionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateStatelessSuggestionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GenerateStatelessSuggestionRequest),[GenerateStatelessSuggestionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GenerateStatelessSuggestionResponse)>` |   
  
### generateStatelessSummary(GenerateStatelessSummaryRequest request)
    
    
    public final GenerateStatelessSummaryResponse generateStatelessSummary(GenerateStatelessSummaryRequest request)

Generates and returns a summary for a conversation that does not have a resource created for it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       GenerateStatelessSummaryRequest request =
           GenerateStatelessSummaryRequest.newBuilder()
               .setStatelessConversation(
                   GenerateStatelessSummaryRequest.MinimalConversation.newBuilder().build())
               .setConversationProfile(ConversationProfile.newBuilder().build())
               .setLatestMessage(
                   MessageName.ofProjectConversationMessageName(
                           "[PROJECT]", "[CONVERSATION]", "[MESSAGE]")
                       .toString())
               .setMaxContextSize(-1134084212)
               .build();
       GenerateStatelessSummaryResponse response =
           conversationsClient.generateStatelessSummary(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateStatelessSummaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GenerateStatelessSummaryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateStatelessSummaryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GenerateStatelessSummaryResponse)` |   
  
### generateStatelessSummaryCallable()
    
    
    public final UnaryCallable<GenerateStatelessSummaryRequest,GenerateStatelessSummaryResponse> generateStatelessSummaryCallable()

Generates and returns a summary for a conversation that does not have a resource created for it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       GenerateStatelessSummaryRequest request =
           GenerateStatelessSummaryRequest.newBuilder()
               .setStatelessConversation(
                   GenerateStatelessSummaryRequest.MinimalConversation.newBuilder().build())
               .setConversationProfile(ConversationProfile.newBuilder().build())
               .setLatestMessage(
                   MessageName.ofProjectConversationMessageName(
                           "[PROJECT]", "[CONVERSATION]", "[MESSAGE]")
                       .toString())
               .setMaxContextSize(-1134084212)
               .build();
       ApiFuture<GenerateStatelessSummaryResponse> future =
           conversationsClient.generateStatelessSummaryCallable().futureCall(request);
       // Do something.
       GenerateStatelessSummaryResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateStatelessSummaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GenerateStatelessSummaryRequest),[GenerateStatelessSummaryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GenerateStatelessSummaryResponse)>` |   
  
### generateSuggestions(@Nullable ConversationName conversation)
    
    
    public final GenerateSuggestionsResponse generateSuggestions(@Nullable ConversationName conversation)

Generates all the suggestions using generators configured in the conversation profile. A generator is used only if its trigger event is matched.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ConversationName conversation =
           ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]");
       GenerateSuggestionsResponse response = conversationsClient.generateSuggestions(conversation);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`conversation` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationName`  
Required. The conversation for which the suggestions are generated. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`. The conversation must be created with a conversation profile which has generators configured in it to be able to get suggestions.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateSuggestionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GenerateSuggestionsResponse)` |   
  
### generateSuggestions(GenerateSuggestionsRequest request)
    
    
    public final GenerateSuggestionsResponse generateSuggestions(GenerateSuggestionsRequest request)

Generates all the suggestions using generators configured in the conversation profile. A generator is used only if its trigger event is matched.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       GenerateSuggestionsRequest request =
           GenerateSuggestionsRequest.newBuilder()
               .setConversation(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .setLatestMessage(
                   MessageName.ofProjectConversationMessageName(
                           "[PROJECT]", "[CONVERSATION]", "[MESSAGE]")
                       .toString())
               .addAllTriggerEvents(new ArrayList<TriggerEvent>())
               .build();
       GenerateSuggestionsResponse response = conversationsClient.generateSuggestions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateSuggestionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GenerateSuggestionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateSuggestionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GenerateSuggestionsResponse)` |   
  
### generateSuggestions(String conversation)
    
    
    public final GenerateSuggestionsResponse generateSuggestions(String conversation)

Generates all the suggestions using generators configured in the conversation profile. A generator is used only if its trigger event is matched.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       String conversation =
           ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]").toString();
       GenerateSuggestionsResponse response = conversationsClient.generateSuggestions(conversation);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`conversation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The conversation for which the suggestions are generated. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`. The conversation must be created with a conversation profile which has generators configured in it to be able to get suggestions.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateSuggestionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GenerateSuggestionsResponse)` |   
  
### generateSuggestionsCallable()
    
    
    public final UnaryCallable<GenerateSuggestionsRequest,GenerateSuggestionsResponse> generateSuggestionsCallable()

Generates all the suggestions using generators configured in the conversation profile. A generator is used only if its trigger event is matched.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       GenerateSuggestionsRequest request =
           GenerateSuggestionsRequest.newBuilder()
               .setConversation(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .setLatestMessage(
                   MessageName.ofProjectConversationMessageName(
                           "[PROJECT]", "[CONVERSATION]", "[MESSAGE]")
                       .toString())
               .addAllTriggerEvents(new ArrayList<TriggerEvent>())
               .build();
       ApiFuture<GenerateSuggestionsResponse> future =
           conversationsClient.generateSuggestionsCallable().futureCall(request);
       // Do something.
       GenerateSuggestionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateSuggestionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GenerateSuggestionsRequest),[GenerateSuggestionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GenerateSuggestionsResponse)>` |   
  
### getConversation(@Nullable ConversationName name)
    
    
    public final Conversation getConversation(@Nullable ConversationName name)

Retrieves the specific conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ConversationName name =
           ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]");
       Conversation response = conversationsClient.getConversation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationName`  
Required. The name of the conversation. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation)` |   
  
### getConversation(GetConversationRequest request)
    
    
    public final Conversation getConversation(GetConversationRequest request)

Retrieves the specific conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       GetConversationRequest request =
           GetConversationRequest.newBuilder()
               .setName(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .build();
       Conversation response = conversationsClient.getConversation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetConversationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation)` |   
  
### getConversation(String name)
    
    
    public final Conversation getConversation(String name)

Retrieves the specific conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       String name =
           ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]").toString();
       Conversation response = conversationsClient.getConversation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the conversation. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation)` |   
  
### getConversationCallable()
    
    
    public final UnaryCallable<GetConversationRequest,Conversation> getConversationCallable()

Retrieves the specific conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       GetConversationRequest request =
           GetConversationRequest.newBuilder()
               .setName(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .build();
       ApiFuture<Conversation> future =
           conversationsClient.getConversationCallable().futureCall(request);
       // Do something.
       Conversation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetConversationRequest),[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = conversationsClient.getLocation(request);
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
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = conversationsClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable ConversationsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationsSettings` |   
  
### getStub()
    
    
    public ConversationsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ConversationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.ConversationsStub)` |   
  
### ingestContextReferences(@Nullable ConversationName conversation, Map<String,Conversation.ContextReference> contextReferences)
    
    
    public final IngestContextReferencesResponse ingestContextReferences(@Nullable ConversationName conversation, Map<String,Conversation.ContextReference> contextReferences)

Data ingestion API. Ingests context references for an existing conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ConversationName conversation =
           ConversationName.ofProjectLocationConversationName(
               "[PROJECT]", "[LOCATION]", "[CONVERSATION]");
       Map<String, Conversation.ContextReference> contextReferences = new HashMap<>();
       IngestContextReferencesResponse response =
           conversationsClient.ingestContextReferences(conversation, contextReferences);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationName`  
Required. Resource identifier of the conversation to ingest context information for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`contextReferences` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[ContextReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation.ContextReference)>`  
Required. The context references to ingest. The key is the name of the context reference and the value contains the contents of the context reference. The key is used to incorporate ingested context references to enhance the generator.  
**Returns**  
---  
**Type** | **Description**  
`[IngestContextReferencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IngestContextReferencesResponse)` |   
  
### ingestContextReferences(IngestContextReferencesRequest request)
    
    
    public final IngestContextReferencesResponse ingestContextReferences(IngestContextReferencesRequest request)

Data ingestion API. Ingests context references for an existing conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       IngestContextReferencesRequest request =
           IngestContextReferencesRequest.newBuilder()
               .setConversation(
                   ConversationName.ofProjectLocationConversationName(
                           "[PROJECT]", "[LOCATION]", "[CONVERSATION]")
                       .toString())
               .putAllContextReferences(new HashMap<String, Conversation.ContextReference>())
               .build();
       IngestContextReferencesResponse response =
           conversationsClient.ingestContextReferences(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[IngestContextReferencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IngestContextReferencesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IngestContextReferencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IngestContextReferencesResponse)` |   
  
### ingestContextReferences(String conversation, Map<String,Conversation.ContextReference> contextReferences)
    
    
    public final IngestContextReferencesResponse ingestContextReferences(String conversation, Map<String,Conversation.ContextReference> contextReferences)

Data ingestion API. Ingests context references for an existing conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       String conversation =
           ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]").toString();
       Map<String, Conversation.ContextReference> contextReferences = new HashMap<>();
       IngestContextReferencesResponse response =
           conversationsClient.ingestContextReferences(conversation, contextReferences);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource identifier of the conversation to ingest context information for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`contextReferences` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[ContextReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Conversation.ContextReference)>`  
Required. The context references to ingest. The key is the name of the context reference and the value contains the contents of the context reference. The key is used to incorporate ingested context references to enhance the generator.  
**Returns**  
---  
**Type** | **Description**  
`[IngestContextReferencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IngestContextReferencesResponse)` |   
  
### ingestContextReferencesCallable()
    
    
    public final UnaryCallable<IngestContextReferencesRequest,IngestContextReferencesResponse> ingestContextReferencesCallable()

Data ingestion API. Ingests context references for an existing conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       IngestContextReferencesRequest request =
           IngestContextReferencesRequest.newBuilder()
               .setConversation(
                   ConversationName.ofProjectLocationConversationName(
                           "[PROJECT]", "[LOCATION]", "[CONVERSATION]")
                       .toString())
               .putAllContextReferences(new HashMap<String, Conversation.ContextReference>())
               .build();
       ApiFuture<IngestContextReferencesResponse> future =
           conversationsClient.ingestContextReferencesCallable().futureCall(request);
       // Do something.
       IngestContextReferencesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[IngestContextReferencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IngestContextReferencesRequest),[IngestContextReferencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IngestContextReferencesResponse)>` |   
  
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
  
### listConversations(@Nullable LocationName parent)
    
    
    public final ConversationsClient.ListConversationsPagedResponse listConversations(@Nullable LocationName parent)

Returns the list of all conversations in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Conversation element : conversationsClient.listConversations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.LocationName`  
Required. The project from which to list all conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationsClient.ListConversationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsClient.ListConversationsPagedResponse)` |   
  
### listConversations(@Nullable ProjectName parent)
    
    
    public final ConversationsClient.ListConversationsPagedResponse listConversations(@Nullable ProjectName parent)

Returns the list of all conversations in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (Conversation element : conversationsClient.listConversations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ProjectName`  
Required. The project from which to list all conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationsClient.ListConversationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsClient.ListConversationsPagedResponse)` |   
  
### listConversations(ListConversationsRequest request)
    
    
    public final ConversationsClient.ListConversationsPagedResponse listConversations(ListConversationsRequest request)

Returns the list of all conversations in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ListConversationsRequest request =
           ListConversationsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Conversation element : conversationsClient.listConversations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationsClient.ListConversationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsClient.ListConversationsPagedResponse)` |   
  
### listConversations(String parent)
    
    
    public final ConversationsClient.ListConversationsPagedResponse listConversations(String parent)

Returns the list of all conversations in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (Conversation element : conversationsClient.listConversations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project from which to list all conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationsClient.ListConversationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsClient.ListConversationsPagedResponse)` |   
  
### listConversationsCallable()
    
    
    public final UnaryCallable<ListConversationsRequest,ListConversationsResponse> listConversationsCallable()

Returns the list of all conversations in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ListConversationsRequest request =
           ListConversationsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListConversationsResponse response =
             conversationsClient.listConversationsCallable().call(request);
         for (Conversation element : response.getConversationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationsRequest),[ListConversationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationsResponse)>` |   
  
### listConversationsPagedCallable()
    
    
    public final UnaryCallable<ListConversationsRequest,ConversationsClient.ListConversationsPagedResponse> listConversationsPagedCallable()

Returns the list of all conversations in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ListConversationsRequest request =
           ListConversationsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Conversation> future =
           conversationsClient.listConversationsPagedCallable().futureCall(request);
       // Do something.
       for (Conversation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListConversationsRequest),[ListConversationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsClient.ListConversationsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final ConversationsClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : conversationsClient.listLocations(request).iterateAll()) {
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
`[ConversationsClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsClient.ListLocationsPagedResponse)` |   
  
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
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = conversationsClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,ConversationsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           conversationsClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsClient.ListLocationsPagedResponse)>` |   
  
### listMessages(@Nullable ConversationName parent)
    
    
    public final ConversationsClient.ListMessagesPagedResponse listMessages(@Nullable ConversationName parent)

Lists messages that belong to a given conversation. `messages` are ordered by `create_time` in descending order. To fetch updates without duplication, send request with filter `create_time_epoch_microseconds > [first item's create_time of previous request]` and empty page_token.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ConversationName parent =
           ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]");
       for (Message element : conversationsClient.listMessages(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationName`  
Required. The name of the conversation to list messages for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`  
**Returns**  
---  
**Type** | **Description**  
`[ConversationsClient.ListMessagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsClient.ListMessagesPagedResponse)` |   
  
### listMessages(ListMessagesRequest request)
    
    
    public final ConversationsClient.ListMessagesPagedResponse listMessages(ListMessagesRequest request)

Lists messages that belong to a given conversation. `messages` are ordered by `create_time` in descending order. To fetch updates without duplication, send request with filter `create_time_epoch_microseconds > [first item's create_time of previous request]` and empty page_token.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ListMessagesRequest request =
           ListMessagesRequest.newBuilder()
               .setParent(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Message element : conversationsClient.listMessages(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMessagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListMessagesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationsClient.ListMessagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsClient.ListMessagesPagedResponse)` |   
  
### listMessages(String parent)
    
    
    public final ConversationsClient.ListMessagesPagedResponse listMessages(String parent)

Lists messages that belong to a given conversation. `messages` are ordered by `create_time` in descending order. To fetch updates without duplication, send request with filter `create_time_epoch_microseconds > [first item's create_time of previous request]` and empty page_token.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       String parent =
           ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]").toString();
       for (Message element : conversationsClient.listMessages(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the conversation to list messages for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`  
**Returns**  
---  
**Type** | **Description**  
`[ConversationsClient.ListMessagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsClient.ListMessagesPagedResponse)` |   
  
### listMessagesCallable()
    
    
    public final UnaryCallable<ListMessagesRequest,ListMessagesResponse> listMessagesCallable()

Lists messages that belong to a given conversation. `messages` are ordered by `create_time` in descending order. To fetch updates without duplication, send request with filter `create_time_epoch_microseconds > [first item's create_time of previous request]` and empty page_token.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ListMessagesRequest request =
           ListMessagesRequest.newBuilder()
               .setParent(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListMessagesResponse response = conversationsClient.listMessagesCallable().call(request);
         for (Message element : response.getMessagesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMessagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListMessagesRequest),[ListMessagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListMessagesResponse)>` |   
  
### listMessagesPagedCallable()
    
    
    public final UnaryCallable<ListMessagesRequest,ConversationsClient.ListMessagesPagedResponse> listMessagesPagedCallable()

Lists messages that belong to a given conversation. `messages` are ordered by `create_time` in descending order. To fetch updates without duplication, send request with filter `create_time_epoch_microseconds > [first item's create_time of previous request]` and empty page_token.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ListMessagesRequest request =
           ListMessagesRequest.newBuilder()
               .setParent(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Message> future =
           conversationsClient.listMessagesPagedCallable().futureCall(request);
       // Do something.
       for (Message element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMessagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListMessagesRequest),[ListMessagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ConversationsClient.ListMessagesPagedResponse)>` |   
  
### searchKnowledge(SearchKnowledgeRequest request)
    
    
    public final SearchKnowledgeResponse searchKnowledge(SearchKnowledgeRequest request)

Get answers for the given query based on knowledge documents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       SearchKnowledgeRequest request =
           SearchKnowledgeRequest.newBuilder()
               .setParent("parent-995424086")
               .setQuery(TextInput.newBuilder().build())
               .setConversationProfile(
                   ConversationProfileName.ofProjectConversationProfileName(
                           "[PROJECT]", "[CONVERSATION_PROFILE]")
                       .toString())
               .setSessionId("sessionId607796817")
               .setConversation(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .setLatestMessage(
                   MessageName.ofProjectConversationMessageName(
                           "[PROJECT]", "[CONVERSATION]", "[MESSAGE]")
                       .toString())
               .setEndUserMetadata(Struct.newBuilder().build())
               .setSearchConfig(SearchKnowledgeRequest.SearchConfig.newBuilder().build())
               .setExactSearch(true)
               .build();
       SearchKnowledgeResponse response = conversationsClient.searchKnowledge(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchKnowledgeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SearchKnowledgeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchKnowledgeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SearchKnowledgeResponse)` |   
  
### searchKnowledgeCallable()
    
    
    public final UnaryCallable<SearchKnowledgeRequest,SearchKnowledgeResponse> searchKnowledgeCallable()

Get answers for the given query based on knowledge documents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       SearchKnowledgeRequest request =
           SearchKnowledgeRequest.newBuilder()
               .setParent("parent-995424086")
               .setQuery(TextInput.newBuilder().build())
               .setConversationProfile(
                   ConversationProfileName.ofProjectConversationProfileName(
                           "[PROJECT]", "[CONVERSATION_PROFILE]")
                       .toString())
               .setSessionId("sessionId607796817")
               .setConversation(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .setLatestMessage(
                   MessageName.ofProjectConversationMessageName(
                           "[PROJECT]", "[CONVERSATION]", "[MESSAGE]")
                       .toString())
               .setEndUserMetadata(Struct.newBuilder().build())
               .setSearchConfig(SearchKnowledgeRequest.SearchConfig.newBuilder().build())
               .setExactSearch(true)
               .build();
       ApiFuture<SearchKnowledgeResponse> future =
           conversationsClient.searchKnowledgeCallable().futureCall(request);
       // Do something.
       SearchKnowledgeResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchKnowledgeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SearchKnowledgeRequest),[SearchKnowledgeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SearchKnowledgeResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### suggestConversationSummary(@Nullable ConversationName conversation)
    
    
    public final SuggestConversationSummaryResponse suggestConversationSummary(@Nullable ConversationName conversation)

Suggests summary for a conversation based on specific historical messages. The range of the messages to be used for summary can be specified in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       ConversationName conversation =
           ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]");
       SuggestConversationSummaryResponse response =
           conversationsClient.suggestConversationSummary(conversation);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`conversation` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationName`  
Required. The conversation to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[SuggestConversationSummaryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestConversationSummaryResponse)` |   
  
### suggestConversationSummary(SuggestConversationSummaryRequest request)
    
    
    public final SuggestConversationSummaryResponse suggestConversationSummary(SuggestConversationSummaryRequest request)

Suggests summary for a conversation based on specific historical messages. The range of the messages to be used for summary can be specified in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       SuggestConversationSummaryRequest request =
           SuggestConversationSummaryRequest.newBuilder()
               .setConversation(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .setLatestMessage(
                   MessageName.ofProjectConversationMessageName(
                           "[PROJECT]", "[CONVERSATION]", "[MESSAGE]")
                       .toString())
               .setContextSize(1116903569)
               .setAssistQueryParams(AssistQueryParameters.newBuilder().build())
               .build();
       SuggestConversationSummaryResponse response =
           conversationsClient.suggestConversationSummary(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SuggestConversationSummaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestConversationSummaryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SuggestConversationSummaryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestConversationSummaryResponse)` |   
  
### suggestConversationSummary(String conversation)
    
    
    public final SuggestConversationSummaryResponse suggestConversationSummary(String conversation)

Suggests summary for a conversation based on specific historical messages. The range of the messages to be used for summary can be specified in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       String conversation =
           ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]").toString();
       SuggestConversationSummaryResponse response =
           conversationsClient.suggestConversationSummary(conversation);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`conversation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The conversation to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[SuggestConversationSummaryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestConversationSummaryResponse)` |   
  
### suggestConversationSummaryCallable()
    
    
    public final UnaryCallable<SuggestConversationSummaryRequest,SuggestConversationSummaryResponse> suggestConversationSummaryCallable()

Suggests summary for a conversation based on specific historical messages. The range of the messages to be used for summary can be specified in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationsClient conversationsClient = ConversationsClient.create()) {
       SuggestConversationSummaryRequest request =
           SuggestConversationSummaryRequest.newBuilder()
               .setConversation(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .setLatestMessage(
                   MessageName.ofProjectConversationMessageName(
                           "[PROJECT]", "[CONVERSATION]", "[MESSAGE]")
                       .toString())
               .setContextSize(1116903569)
               .setAssistQueryParams(AssistQueryParameters.newBuilder().build())
               .build();
       ApiFuture<SuggestConversationSummaryResponse> future =
           conversationsClient.suggestConversationSummaryCallable().futureCall(request);
       // Do something.
       SuggestConversationSummaryResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SuggestConversationSummaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestConversationSummaryRequest),[SuggestConversationSummaryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestConversationSummaryResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
