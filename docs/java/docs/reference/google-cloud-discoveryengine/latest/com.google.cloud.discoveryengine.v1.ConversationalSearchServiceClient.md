---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceClient
title: Class ConversationalSearchServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:34.793772+00:00
---

# Class ConversationalSearchServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConversationalSearchServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-discoveryengine/google-cloud-discoveryengine/src/main/java/com/google/cloud/discoveryengine/v1/ConversationalSearchServiceClient.java)| [Product Reference](https://cloud.google.com/discovery-engine/media/docs)  
---|---  
  
Service Description: Service for conversational search.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       ConversationName name =
           ConversationName.ofProjectLocationDataStoreConversationName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONVERSATION]");
       TextInput query = TextInput.newBuilder().build();
       ConverseConversationResponse response =
           conversationalSearchServiceClient.converseConversation(name, query);
     }
     

Note: close() needs to be called on the ConversationalSearchServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ConverseConversation |  Converses a conversation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * converseConversation(ConverseConversationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * converseConversation(ConversationName name, TextInput query) 
  * converseConversation(String name, TextInput query) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * converseConversationCallable() 

  
CreateConversation |  Creates a Conversation.  If the Conversation to create already exists, an ALREADY_EXISTS error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createConversation(CreateConversationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createConversation(DataStoreName parent, Conversation conversation) 
  * createConversation(String parent, Conversation conversation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createConversationCallable() 

  
DeleteConversation |  Deletes a Conversation.  If the Conversation to delete does not exist, a NOT_FOUND error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteConversation(DeleteConversationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteConversation(ConversationName name) 
  * deleteConversation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteConversationCallable() 

  
UpdateConversation |  Updates a Conversation.  Conversation action type cannot be changed. If the Conversation to update does not exist, a NOT_FOUND error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateConversation(UpdateConversationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateConversation(Conversation conversation, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateConversationCallable() 

  
GetConversation |  Gets a Conversation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getConversation(GetConversationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getConversation(ConversationName name) 
  * getConversation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getConversationCallable() 

  
ListConversations |  Lists all Conversations by their parent DataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listConversations(ListConversationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listConversations(DataStoreName parent) 
  * listConversations(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listConversationsPagedCallable() 
  * listConversationsCallable() 

  
AnswerQuery |  Answer query method. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * answerQuery(AnswerQueryRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * answerQueryCallable() 

  
StreamAnswerQuery |  Answer query method (streaming).  It takes one AnswerQueryRequest and returns multiple AnswerQueryResponse messages in a stream. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * streamAnswerQueryCallable() 

  
GetAnswer |  Gets a Answer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAnswer(GetAnswerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAnswer(AnswerName name) 
  * getAnswer(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAnswerCallable() 

  
CreateSession |  Creates a Session.  If the Session to create already exists, an ALREADY_EXISTS error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSession(CreateSessionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createSession(DataStoreName parent, Session session) 
  * createSession(String parent, Session session) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSessionCallable() 

  
DeleteSession |  Deletes a Session.  If the Session to delete does not exist, a NOT_FOUND error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSession(DeleteSessionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteSession(SessionName name) 
  * deleteSession(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSessionCallable() 

  
UpdateSession |  Updates a Session.  Session action type cannot be changed. If the Session to update does not exist, a NOT_FOUND error is returned. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSession(UpdateSessionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSession(Session session, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSessionCallable() 

  
GetSession |  Gets a Session. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSession(GetSessionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSession(SessionName name) 
  * getSession(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSessionCallable() 

  
ListSessions |  Lists all Sessions by their parent DataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSessions(ListSessionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSessions(DataStoreName parent) 
  * listSessions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSessionsPagedCallable() 
  * listSessionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ConversationalSearchServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationalSearchServiceSettings conversationalSearchServiceSettings =
         ConversationalSearchServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create(conversationalSearchServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationalSearchServiceSettings conversationalSearchServiceSettings =
         ConversationalSearchServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create(conversationalSearchServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConversationalSearchServiceSettings conversationalSearchServiceSettings =
         ConversationalSearchServiceSettings.newHttpJsonBuilder().build();
     ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create(conversationalSearchServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ConversationalSearchServiceClient

## Static Methods 

### create()
    
    
    public static final ConversationalSearchServiceClient create()

Constructs an instance of ConversationalSearchServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ConversationalSearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConversationalSearchServiceSettings settings)
    
    
    public static final ConversationalSearchServiceClient create(ConversationalSearchServiceSettings settings)

Constructs an instance of ConversationalSearchServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConversationalSearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversationalSearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ConversationalSearchServiceStub stub)
    
    
    public static final ConversationalSearchServiceClient create(ConversationalSearchServiceStub stub)

Constructs an instance of ConversationalSearchServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ConversationalSearchServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConversationalSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.ConversationalSearchServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversationalSearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceClient)` |   
  
## Constructors 

### ConversationalSearchServiceClient(ConversationalSearchServiceSettings settings)
    
    
    protected ConversationalSearchServiceClient(ConversationalSearchServiceSettings settings)

Constructs an instance of ConversationalSearchServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ConversationalSearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceSettings)`  
  
  
### ConversationalSearchServiceClient(ConversationalSearchServiceStub stub)
    
    
    protected ConversationalSearchServiceClient(ConversationalSearchServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConversationalSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.ConversationalSearchServiceStub)`  
  
  
## Methods 

### answerQuery(AnswerQueryRequest request)
    
    
    public final AnswerQueryResponse answerQuery(AnswerQueryRequest request)

Answer query method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       AnswerQueryRequest request =
           AnswerQueryRequest.newBuilder()
               .setServingConfig(
                   ServingConfigName.ofProjectLocationDataStoreServingConfigName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]")
                       .toString())
               .setQuery(Query.newBuilder().build())
               .setSession(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .setSafetySpec(AnswerQueryRequest.SafetySpec.newBuilder().build())
               .setRelatedQuestionsSpec(AnswerQueryRequest.RelatedQuestionsSpec.newBuilder().build())
               .setGroundingSpec(AnswerQueryRequest.GroundingSpec.newBuilder().build())
               .setAnswerGenerationSpec(AnswerQueryRequest.AnswerGenerationSpec.newBuilder().build())
               .setSearchSpec(AnswerQueryRequest.SearchSpec.newBuilder().build())
               .setQueryUnderstandingSpec(
                   AnswerQueryRequest.QueryUnderstandingSpec.newBuilder().build())
               .setAsynchronousMode(true)
               .setUserPseudoId("userPseudoId-1155274652")
               .putAllUserLabels(new HashMap<String, String>())
               .setEndUserSpec(AnswerQueryRequest.EndUserSpec.newBuilder().build())
               .build();
       AnswerQueryResponse response = conversationalSearchServiceClient.answerQuery(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AnswerQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AnswerQueryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AnswerQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AnswerQueryResponse)` |   
  
### answerQueryCallable()
    
    
    public final UnaryCallable<AnswerQueryRequest,AnswerQueryResponse> answerQueryCallable()

Answer query method.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       AnswerQueryRequest request =
           AnswerQueryRequest.newBuilder()
               .setServingConfig(
                   ServingConfigName.ofProjectLocationDataStoreServingConfigName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]")
                       .toString())
               .setQuery(Query.newBuilder().build())
               .setSession(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .setSafetySpec(AnswerQueryRequest.SafetySpec.newBuilder().build())
               .setRelatedQuestionsSpec(AnswerQueryRequest.RelatedQuestionsSpec.newBuilder().build())
               .setGroundingSpec(AnswerQueryRequest.GroundingSpec.newBuilder().build())
               .setAnswerGenerationSpec(AnswerQueryRequest.AnswerGenerationSpec.newBuilder().build())
               .setSearchSpec(AnswerQueryRequest.SearchSpec.newBuilder().build())
               .setQueryUnderstandingSpec(
                   AnswerQueryRequest.QueryUnderstandingSpec.newBuilder().build())
               .setAsynchronousMode(true)
               .setUserPseudoId("userPseudoId-1155274652")
               .putAllUserLabels(new HashMap<String, String>())
               .setEndUserSpec(AnswerQueryRequest.EndUserSpec.newBuilder().build())
               .build();
       ApiFuture<AnswerQueryResponse> future =
           conversationalSearchServiceClient.answerQueryCallable().futureCall(request);
       // Do something.
       AnswerQueryResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AnswerQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AnswerQueryRequest),[AnswerQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AnswerQueryResponse)>` |   
  
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

### converseConversation(@Nullable ConversationName name, TextInput query)
    
    
    public final ConverseConversationResponse converseConversation(@Nullable ConversationName name, TextInput query)

Converses a conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       ConversationName name =
           ConversationName.ofProjectLocationDataStoreConversationName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONVERSATION]");
       TextInput query = TextInput.newBuilder().build();
       ConverseConversationResponse response =
           conversationalSearchServiceClient.converseConversation(name, query);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.ConversationName`  
Required. The resource name of the Conversation to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}`. Use `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/-` to activate auto session mode, which automatically creates a new conversation inside a ConverseConversation session.  
`query` | `[TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TextInput)`  
Required. Current user input.  
**Returns**  
---  
**Type** | **Description**  
`[ConverseConversationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConverseConversationResponse)` |   
  
### converseConversation(ConverseConversationRequest request)
    
    
    public final ConverseConversationResponse converseConversation(ConverseConversationRequest request)

Converses a conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       ConverseConversationRequest request =
           ConverseConversationRequest.newBuilder()
               .setName(
                   ConversationName.ofProjectLocationDataStoreConversationName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONVERSATION]")
                       .toString())
               .setQuery(TextInput.newBuilder().build())
               .setServingConfig(
                   ServingConfigName.ofProjectLocationDataStoreServingConfigName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]")
                       .toString())
               .setConversation(Conversation.newBuilder().build())
               .setSafeSearch(true)
               .putAllUserLabels(new HashMap<String, String>())
               .setSummarySpec(SearchRequest.ContentSearchSpec.SummarySpec.newBuilder().build())
               .setFilter("filter-1274492040")
               .setBoostSpec(SearchRequest.BoostSpec.newBuilder().build())
               .build();
       ConverseConversationResponse response =
           conversationalSearchServiceClient.converseConversation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ConverseConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConverseConversationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConverseConversationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConverseConversationResponse)` |   
  
### converseConversation(String name, TextInput query)
    
    
    public final ConverseConversationResponse converseConversation(String name, TextInput query)

Converses a conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       String name =
           ConversationName.ofProjectLocationDataStoreConversationName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONVERSATION]")
               .toString();
       TextInput query = TextInput.newBuilder().build();
       ConverseConversationResponse response =
           conversationalSearchServiceClient.converseConversation(name, query);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Conversation to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}`. Use `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/-` to activate auto session mode, which automatically creates a new conversation inside a ConverseConversation session.  
`query` | `[TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TextInput)`  
Required. Current user input.  
**Returns**  
---  
**Type** | **Description**  
`[ConverseConversationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConverseConversationResponse)` |   
  
### converseConversationCallable()
    
    
    public final UnaryCallable<ConverseConversationRequest,ConverseConversationResponse> converseConversationCallable()

Converses a conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       ConverseConversationRequest request =
           ConverseConversationRequest.newBuilder()
               .setName(
                   ConversationName.ofProjectLocationDataStoreConversationName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONVERSATION]")
                       .toString())
               .setQuery(TextInput.newBuilder().build())
               .setServingConfig(
                   ServingConfigName.ofProjectLocationDataStoreServingConfigName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]")
                       .toString())
               .setConversation(Conversation.newBuilder().build())
               .setSafeSearch(true)
               .putAllUserLabels(new HashMap<String, String>())
               .setSummarySpec(SearchRequest.ContentSearchSpec.SummarySpec.newBuilder().build())
               .setFilter("filter-1274492040")
               .setBoostSpec(SearchRequest.BoostSpec.newBuilder().build())
               .build();
       ApiFuture<ConverseConversationResponse> future =
           conversationalSearchServiceClient.converseConversationCallable().futureCall(request);
       // Do something.
       ConverseConversationResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ConverseConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConverseConversationRequest),[ConverseConversationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConverseConversationResponse)>` |   
  
### createConversation(@Nullable DataStoreName parent, Conversation conversation)
    
    
    public final Conversation createConversation(@Nullable DataStoreName parent, Conversation conversation)

Creates a Conversation.

If the Conversation to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       DataStoreName parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       Conversation conversation = Conversation.newBuilder().build();
       Conversation response =
           conversationalSearchServiceClient.createConversation(parent, conversation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.DataStoreName`  
Required. Full resource name of parent data store. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}`  
`conversation` | `[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)`  
Required. The conversation to create.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)` |   
  
### createConversation(CreateConversationRequest request)
    
    
    public final Conversation createConversation(CreateConversationRequest request)

Creates a Conversation.

If the Conversation to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       CreateConversationRequest request =
           CreateConversationRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setConversation(Conversation.newBuilder().build())
               .build();
       Conversation response = conversationalSearchServiceClient.createConversation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateConversationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)` |   
  
### createConversation(String parent, Conversation conversation)
    
    
    public final Conversation createConversation(String parent, Conversation conversation)

Creates a Conversation.

If the Conversation to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       String parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]")
               .toString();
       Conversation conversation = Conversation.newBuilder().build();
       Conversation response =
           conversationalSearchServiceClient.createConversation(parent, conversation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of parent data store. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}`  
`conversation` | `[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)`  
Required. The conversation to create.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)` |   
  
### createConversationCallable()
    
    
    public final UnaryCallable<CreateConversationRequest,Conversation> createConversationCallable()

Creates a Conversation.

If the Conversation to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       CreateConversationRequest request =
           CreateConversationRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setConversation(Conversation.newBuilder().build())
               .build();
       ApiFuture<Conversation> future =
           conversationalSearchServiceClient.createConversationCallable().futureCall(request);
       // Do something.
       Conversation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateConversationRequest),[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)>` |   
  
### createSession(@Nullable DataStoreName parent, Session session)
    
    
    public final Session createSession(@Nullable DataStoreName parent, Session session)

Creates a Session.

If the Session to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       DataStoreName parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       Session session = Session.newBuilder().build();
       Session response = conversationalSearchServiceClient.createSession(parent, session);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.DataStoreName`  
Required. Full resource name of parent data store. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}`  
`session` | `[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)`  
Required. The session to create.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)` |   
  
### createSession(CreateSessionRequest request)
    
    
    public final Session createSession(CreateSessionRequest request)

Creates a Session.

If the Session to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       CreateSessionRequest request =
           CreateSessionRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setSession(Session.newBuilder().build())
               .build();
       Session response = conversationalSearchServiceClient.createSession(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateSessionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)` |   
  
### createSession(String parent, Session session)
    
    
    public final Session createSession(String parent, Session session)

Creates a Session.

If the Session to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       String parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]")
               .toString();
       Session session = Session.newBuilder().build();
       Session response = conversationalSearchServiceClient.createSession(parent, session);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of parent data store. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}`  
`session` | `[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)`  
Required. The session to create.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)` |   
  
### createSessionCallable()
    
    
    public final UnaryCallable<CreateSessionRequest,Session> createSessionCallable()

Creates a Session.

If the Session to create already exists, an ALREADY_EXISTS error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       CreateSessionRequest request =
           CreateSessionRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setSession(Session.newBuilder().build())
               .build();
       ApiFuture<Session> future =
           conversationalSearchServiceClient.createSessionCallable().futureCall(request);
       // Do something.
       Session response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateSessionRequest),[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)>` |   
  
### deleteConversation(@Nullable ConversationName name)
    
    
    public final void deleteConversation(@Nullable ConversationName name)

Deletes a Conversation.

If the Conversation to delete does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       ConversationName name =
           ConversationName.ofProjectLocationDataStoreConversationName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONVERSATION]");
       conversationalSearchServiceClient.deleteConversation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.ConversationName`  
Required. The resource name of the Conversation to delete. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}`  
  
### deleteConversation(DeleteConversationRequest request)
    
    
    public final void deleteConversation(DeleteConversationRequest request)

Deletes a Conversation.

If the Conversation to delete does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       DeleteConversationRequest request =
           DeleteConversationRequest.newBuilder()
               .setName(
                   ConversationName.ofProjectLocationDataStoreConversationName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONVERSATION]")
                       .toString())
               .build();
       conversationalSearchServiceClient.deleteConversation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteConversationRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteConversation(String name)
    
    
    public final void deleteConversation(String name)

Deletes a Conversation.

If the Conversation to delete does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       String name =
           ConversationName.ofProjectLocationDataStoreConversationName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONVERSATION]")
               .toString();
       conversationalSearchServiceClient.deleteConversation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Conversation to delete. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}`  
  
### deleteConversationCallable()
    
    
    public final UnaryCallable<DeleteConversationRequest,Empty> deleteConversationCallable()

Deletes a Conversation.

If the Conversation to delete does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       DeleteConversationRequest request =
           DeleteConversationRequest.newBuilder()
               .setName(
                   ConversationName.ofProjectLocationDataStoreConversationName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONVERSATION]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           conversationalSearchServiceClient.deleteConversationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteConversationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteSession(@Nullable SessionName name)
    
    
    public final void deleteSession(@Nullable SessionName name)

Deletes a Session.

If the Session to delete does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       SessionName name =
           SessionName.ofProjectLocationDataStoreSessionName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]");
       conversationalSearchServiceClient.deleteSession(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.SessionName`  
Required. The resource name of the Session to delete. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/sessions/{session_id}`  
  
### deleteSession(DeleteSessionRequest request)
    
    
    public final void deleteSession(DeleteSessionRequest request)

Deletes a Session.

If the Session to delete does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       DeleteSessionRequest request =
           DeleteSessionRequest.newBuilder()
               .setName(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .build();
       conversationalSearchServiceClient.deleteSession(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteSessionRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteSession(String name)
    
    
    public final void deleteSession(String name)

Deletes a Session.

If the Session to delete does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       String name =
           SessionName.ofProjectLocationDataStoreSessionName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
               .toString();
       conversationalSearchServiceClient.deleteSession(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Session to delete. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/sessions/{session_id}`  
  
### deleteSessionCallable()
    
    
    public final UnaryCallable<DeleteSessionRequest,Empty> deleteSessionCallable()

Deletes a Session.

If the Session to delete does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       DeleteSessionRequest request =
           DeleteSessionRequest.newBuilder()
               .setName(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           conversationalSearchServiceClient.deleteSessionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteSessionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getAnswer(@Nullable AnswerName name)
    
    
    public final Answer getAnswer(@Nullable AnswerName name)

Gets a Answer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       AnswerName name =
           AnswerName.ofProjectLocationDataStoreSessionAnswerName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]", "[ANSWER]");
       Answer response = conversationalSearchServiceClient.getAnswer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.AnswerName`  
Required. The resource name of the Answer to get. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine_id}/sessions/{session_id}/answers/{answer_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Answer](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Answer)` |   
  
### getAnswer(GetAnswerRequest request)
    
    
    public final Answer getAnswer(GetAnswerRequest request)

Gets a Answer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       GetAnswerRequest request =
           GetAnswerRequest.newBuilder()
               .setName(
                   AnswerName.ofProjectLocationDataStoreSessionAnswerName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]", "[ANSWER]")
                       .toString())
               .build();
       Answer response = conversationalSearchServiceClient.getAnswer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAnswerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetAnswerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Answer](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Answer)` |   
  
### getAnswer(String name)
    
    
    public final Answer getAnswer(String name)

Gets a Answer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       String name =
           AnswerName.ofProjectLocationDataStoreSessionAnswerName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]", "[ANSWER]")
               .toString();
       Answer response = conversationalSearchServiceClient.getAnswer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Answer to get. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine_id}/sessions/{session_id}/answers/{answer_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Answer](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Answer)` |   
  
### getAnswerCallable()
    
    
    public final UnaryCallable<GetAnswerRequest,Answer> getAnswerCallable()

Gets a Answer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       GetAnswerRequest request =
           GetAnswerRequest.newBuilder()
               .setName(
                   AnswerName.ofProjectLocationDataStoreSessionAnswerName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]", "[ANSWER]")
                       .toString())
               .build();
       ApiFuture<Answer> future =
           conversationalSearchServiceClient.getAnswerCallable().futureCall(request);
       // Do something.
       Answer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAnswerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetAnswerRequest),[Answer](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Answer)>` |   
  
### getConversation(@Nullable ConversationName name)
    
    
    public final Conversation getConversation(@Nullable ConversationName name)

Gets a Conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       ConversationName name =
           ConversationName.ofProjectLocationDataStoreConversationName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONVERSATION]");
       Conversation response = conversationalSearchServiceClient.getConversation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.ConversationName`  
Required. The resource name of the Conversation to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)` |   
  
### getConversation(GetConversationRequest request)
    
    
    public final Conversation getConversation(GetConversationRequest request)

Gets a Conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       GetConversationRequest request =
           GetConversationRequest.newBuilder()
               .setName(
                   ConversationName.ofProjectLocationDataStoreConversationName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONVERSATION]")
                       .toString())
               .build();
       Conversation response = conversationalSearchServiceClient.getConversation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetConversationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)` |   
  
### getConversation(String name)
    
    
    public final Conversation getConversation(String name)

Gets a Conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       String name =
           ConversationName.ofProjectLocationDataStoreConversationName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONVERSATION]")
               .toString();
       Conversation response = conversationalSearchServiceClient.getConversation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Conversation to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)` |   
  
### getConversationCallable()
    
    
    public final UnaryCallable<GetConversationRequest,Conversation> getConversationCallable()

Gets a Conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       GetConversationRequest request =
           GetConversationRequest.newBuilder()
               .setName(
                   ConversationName.ofProjectLocationDataStoreConversationName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[CONVERSATION]")
                       .toString())
               .build();
       ApiFuture<Conversation> future =
           conversationalSearchServiceClient.getConversationCallable().futureCall(request);
       // Do something.
       Conversation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetConversationRequest),[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)>` |   
  
### getSession(@Nullable SessionName name)
    
    
    public final Session getSession(@Nullable SessionName name)

Gets a Session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       SessionName name =
           SessionName.ofProjectLocationDataStoreSessionName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]");
       Session response = conversationalSearchServiceClient.getSession(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.SessionName`  
Required. The resource name of the Session to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/sessions/{session_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)` |   
  
### getSession(GetSessionRequest request)
    
    
    public final Session getSession(GetSessionRequest request)

Gets a Session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       GetSessionRequest request =
           GetSessionRequest.newBuilder()
               .setName(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .setIncludeAnswerDetails(true)
               .build();
       Session response = conversationalSearchServiceClient.getSession(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetSessionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)` |   
  
### getSession(String name)
    
    
    public final Session getSession(String name)

Gets a Session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       String name =
           SessionName.ofProjectLocationDataStoreSessionName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
               .toString();
       Session response = conversationalSearchServiceClient.getSession(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Session to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/sessions/{session_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)` |   
  
### getSessionCallable()
    
    
    public final UnaryCallable<GetSessionRequest,Session> getSessionCallable()

Gets a Session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       GetSessionRequest request =
           GetSessionRequest.newBuilder()
               .setName(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .setIncludeAnswerDetails(true)
               .build();
       ApiFuture<Session> future =
           conversationalSearchServiceClient.getSessionCallable().futureCall(request);
       // Do something.
       Session response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetSessionRequest),[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)>` |   
  
### getSettings()
    
    
    public final @Nullable ConversationalSearchServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.ConversationalSearchServiceSettings` |   
  
### getStub()
    
    
    public ConversationalSearchServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ConversationalSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.ConversationalSearchServiceStub)` |   
  
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
  
### listConversations(@Nullable DataStoreName parent)
    
    
    public final ConversationalSearchServiceClient.ListConversationsPagedResponse listConversations(@Nullable DataStoreName parent)

Lists all Conversations by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       DataStoreName parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       for (Conversation element :
           conversationalSearchServiceClient.listConversations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.DataStoreName`  
Required. The data store resource name. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ConversationalSearchServiceClient.ListConversationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceClient.ListConversationsPagedResponse)` |   
  
### listConversations(ListConversationsRequest request)
    
    
    public final ConversationalSearchServiceClient.ListConversationsPagedResponse listConversations(ListConversationsRequest request)

Lists all Conversations by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       ListConversationsRequest request =
           ListConversationsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Conversation element :
           conversationalSearchServiceClient.listConversations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListConversationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationalSearchServiceClient.ListConversationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceClient.ListConversationsPagedResponse)` |   
  
### listConversations(String parent)
    
    
    public final ConversationalSearchServiceClient.ListConversationsPagedResponse listConversations(String parent)

Lists all Conversations by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       String parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]")
               .toString();
       for (Conversation element :
           conversationalSearchServiceClient.listConversations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The data store resource name. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ConversationalSearchServiceClient.ListConversationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceClient.ListConversationsPagedResponse)` |   
  
### listConversationsCallable()
    
    
    public final UnaryCallable<ListConversationsRequest,ListConversationsResponse> listConversationsCallable()

Lists all Conversations by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       ListConversationsRequest request =
           ListConversationsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListConversationsResponse response =
             conversationalSearchServiceClient.listConversationsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListConversationsRequest),[ListConversationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListConversationsResponse)>` |   
  
### listConversationsPagedCallable()
    
    
    public final UnaryCallable<ListConversationsRequest,ConversationalSearchServiceClient.ListConversationsPagedResponse> listConversationsPagedCallable()

Lists all Conversations by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       ListConversationsRequest request =
           ListConversationsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Conversation> future =
           conversationalSearchServiceClient.listConversationsPagedCallable().futureCall(request);
       // Do something.
       for (Conversation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListConversationsRequest),[ListConversationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceClient.ListConversationsPagedResponse)>` |   
  
### listSessions(@Nullable DataStoreName parent)
    
    
    public final ConversationalSearchServiceClient.ListSessionsPagedResponse listSessions(@Nullable DataStoreName parent)

Lists all Sessions by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       DataStoreName parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       for (Session element : conversationalSearchServiceClient.listSessions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.DataStoreName`  
Required. The data store resource name. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ConversationalSearchServiceClient.ListSessionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceClient.ListSessionsPagedResponse)` |   
  
### listSessions(ListSessionsRequest request)
    
    
    public final ConversationalSearchServiceClient.ListSessionsPagedResponse listSessions(ListSessionsRequest request)

Lists all Sessions by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       ListSessionsRequest request =
           ListSessionsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Session element : conversationalSearchServiceClient.listSessions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSessionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListSessionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ConversationalSearchServiceClient.ListSessionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceClient.ListSessionsPagedResponse)` |   
  
### listSessions(String parent)
    
    
    public final ConversationalSearchServiceClient.ListSessionsPagedResponse listSessions(String parent)

Lists all Sessions by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       String parent =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]")
               .toString();
       for (Session element : conversationalSearchServiceClient.listSessions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The data store resource name. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ConversationalSearchServiceClient.ListSessionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceClient.ListSessionsPagedResponse)` |   
  
### listSessionsCallable()
    
    
    public final UnaryCallable<ListSessionsRequest,ListSessionsResponse> listSessionsCallable()

Lists all Sessions by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       ListSessionsRequest request =
           ListSessionsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListSessionsResponse response =
             conversationalSearchServiceClient.listSessionsCallable().call(request);
         for (Session element : response.getSessionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSessionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListSessionsRequest),[ListSessionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListSessionsResponse)>` |   
  
### listSessionsPagedCallable()
    
    
    public final UnaryCallable<ListSessionsRequest,ConversationalSearchServiceClient.ListSessionsPagedResponse> listSessionsPagedCallable()

Lists all Sessions by their parent DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       ListSessionsRequest request =
           ListSessionsRequest.newBuilder()
               .setParent(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Session> future =
           conversationalSearchServiceClient.listSessionsPagedCallable().futureCall(request);
       // Do something.
       for (Session element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSessionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListSessionsRequest),[ListSessionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceClient.ListSessionsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### streamAnswerQueryCallable()
    
    
    public final ServerStreamingCallable<AnswerQueryRequest,AnswerQueryResponse> streamAnswerQueryCallable()

Answer query method (streaming).

It takes one AnswerQueryRequest and returns multiple AnswerQueryResponse messages in a stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       AnswerQueryRequest request =
           AnswerQueryRequest.newBuilder()
               .setServingConfig(
                   ServingConfigName.ofProjectLocationDataStoreServingConfigName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SERVING_CONFIG]")
                       .toString())
               .setQuery(Query.newBuilder().build())
               .setSession(
                   SessionName.ofProjectLocationDataStoreSessionName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SESSION]")
                       .toString())
               .setSafetySpec(AnswerQueryRequest.SafetySpec.newBuilder().build())
               .setRelatedQuestionsSpec(AnswerQueryRequest.RelatedQuestionsSpec.newBuilder().build())
               .setGroundingSpec(AnswerQueryRequest.GroundingSpec.newBuilder().build())
               .setAnswerGenerationSpec(AnswerQueryRequest.AnswerGenerationSpec.newBuilder().build())
               .setSearchSpec(AnswerQueryRequest.SearchSpec.newBuilder().build())
               .setQueryUnderstandingSpec(
                   AnswerQueryRequest.QueryUnderstandingSpec.newBuilder().build())
               .setAsynchronousMode(true)
               .setUserPseudoId("userPseudoId-1155274652")
               .putAllUserLabels(new HashMap<String, String>())
               .setEndUserSpec(AnswerQueryRequest.EndUserSpec.newBuilder().build())
               .build();
       ServerStream<AnswerQueryResponse> stream =
           conversationalSearchServiceClient.streamAnswerQueryCallable().call(request);
       for (AnswerQueryResponse response : stream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable.html)<[AnswerQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AnswerQueryRequest),[AnswerQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AnswerQueryResponse)>` |   
  
### updateConversation(Conversation conversation, FieldMask updateMask)
    
    
    public final Conversation updateConversation(Conversation conversation, FieldMask updateMask)

Updates a Conversation.

Conversation action type cannot be changed. If the Conversation to update does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       Conversation conversation = Conversation.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Conversation response =
           conversationalSearchServiceClient.updateConversation(conversation, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)`  
Required. The Conversation to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Indicates which fields in the provided Conversation to update. The following are NOT supported: 

  * Conversation.name

If not set or empty, all supported fields are updated.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)` |   
  
### updateConversation(UpdateConversationRequest request)
    
    
    public final Conversation updateConversation(UpdateConversationRequest request)

Updates a Conversation.

Conversation action type cannot be changed. If the Conversation to update does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       UpdateConversationRequest request =
           UpdateConversationRequest.newBuilder()
               .setConversation(Conversation.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Conversation response = conversationalSearchServiceClient.updateConversation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateConversationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)` |   
  
### updateConversationCallable()
    
    
    public final UnaryCallable<UpdateConversationRequest,Conversation> updateConversationCallable()

Updates a Conversation.

Conversation action type cannot be changed. If the Conversation to update does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       UpdateConversationRequest request =
           UpdateConversationRequest.newBuilder()
               .setConversation(Conversation.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Conversation> future =
           conversationalSearchServiceClient.updateConversationCallable().futureCall(request);
       // Do something.
       Conversation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateConversationRequest),[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)>` |   
  
### updateSession(Session session, FieldMask updateMask)
    
    
    public final Session updateSession(Session session, FieldMask updateMask)

Updates a Session.

Session action type cannot be changed. If the Session to update does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       Session session = Session.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Session response = conversationalSearchServiceClient.updateSession(session, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`session` | `[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)`  
Required. The Session to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Indicates which fields in the provided Session to update. The following are NOT supported: 

  * Session.name

If not set or empty, all supported fields are updated.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)` |   
  
### updateSession(UpdateSessionRequest request)
    
    
    public final Session updateSession(UpdateSessionRequest request)

Updates a Session.

Session action type cannot be changed. If the Session to update does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       UpdateSessionRequest request =
           UpdateSessionRequest.newBuilder()
               .setSession(Session.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Session response = conversationalSearchServiceClient.updateSession(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateSessionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)` |   
  
### updateSessionCallable()
    
    
    public final UnaryCallable<UpdateSessionRequest,Session> updateSessionCallable()

Updates a Session.

Session action type cannot be changed. If the Session to update does not exist, a NOT_FOUND error is returned.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ConversationalSearchServiceClient conversationalSearchServiceClient =
         ConversationalSearchServiceClient.create()) {
       UpdateSessionRequest request =
           UpdateSessionRequest.newBuilder()
               .setSession(Session.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Session> future =
           conversationalSearchServiceClient.updateSessionCallable().futureCall(request);
       // Do something.
       Session response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateSessionRequest),[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
