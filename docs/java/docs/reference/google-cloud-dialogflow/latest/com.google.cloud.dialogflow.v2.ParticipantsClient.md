---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ParticipantsClient
title: Class ParticipantsClient (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:44.562171+00:00
---

# Class ParticipantsClient (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ParticipantsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ParticipantsClient (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dialogflow/google-cloud-dialogflow/src/main/java/com/google/cloud/dialogflow/v2/ParticipantsClient.java)| [Product Reference](https://cloud.google.com/dialogflow-enterprise/)  
---|---  
  
Service Description: Service for managing Participants.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       ConversationName parent =
           ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]");
       Participant participant = Participant.newBuilder().build();
       Participant response = participantsClient.createParticipant(parent, participant);
     }
     

Note: close() needs to be called on the ParticipantsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateParticipant |  Creates a new participant in a conversation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createParticipant(CreateParticipantRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createParticipant(ConversationName parent, Participant participant) 
  * createParticipant(String parent, Participant participant) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createParticipantCallable() 

  
GetParticipant |  Retrieves a conversation participant. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getParticipant(GetParticipantRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getParticipant(ParticipantName name) 
  * getParticipant(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getParticipantCallable() 

  
ListParticipants |  Returns the list of all participants in the specified conversation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listParticipants(ListParticipantsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listParticipants(ConversationName parent) 
  * listParticipants(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listParticipantsPagedCallable() 
  * listParticipantsCallable() 

  
UpdateParticipant |  Updates the specified participant. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateParticipant(UpdateParticipantRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateParticipant(Participant participant, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateParticipantCallable() 

  
AnalyzeContent |  Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation.  Note: Always use agent versions for production traffic sent to virtual agents. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * analyzeContent(AnalyzeContentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * analyzeContent(ParticipantName participant, AudioInput audioInput) 
  * analyzeContent(ParticipantName participant, EventInput eventInput) 
  * analyzeContent(ParticipantName participant, TextInput textInput) 
  * analyzeContent(String participant, AudioInput audioInput) 
  * analyzeContent(String participant, EventInput eventInput) 
  * analyzeContent(String participant, TextInput textInput) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * analyzeContentCallable() 

  
StreamingAnalyzeContent |  Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation. Note: This method is only available through the gRPC API (not REST).  The top-level message sent to the client by the server is `StreamingAnalyzeContentResponse`. Multiple response messages can be returned in order. The first one or more messages contain the `recognition_result` field. Each result represents a more complete transcript of what the user said. The next message contains the `reply_text` field and potentially the `reply_audio` field. The message can also contain the `automated_agent_reply` field.  Note: Always use agent versions for production traffic sent to virtual agents. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions). |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * streamingAnalyzeContentCallable() 

  
BidiStreamingAnalyzeContent |  Bidirectional endless streaming version of StreamingAnalyzeContent. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * bidiStreamingAnalyzeContentCallable() 

  
StreamingReactiveCompanionSuggestions |  External streaming API for direct human-agent-to-bot chats. |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * streamingReactiveCompanionSuggestionsCallable() 

  
SuggestArticles |  Gets suggested articles for a participant based on specific historical messages. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * suggestArticles(SuggestArticlesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * suggestArticles(ParticipantName parent) 
  * suggestArticles(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * suggestArticlesCallable() 

  
SuggestFaqAnswers |  Gets suggested faq answers for a participant based on specific historical messages. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * suggestFaqAnswers(SuggestFaqAnswersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * suggestFaqAnswers(ParticipantName parent) 
  * suggestFaqAnswers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * suggestFaqAnswersCallable() 

  
SuggestSmartReplies |  Gets smart replies for a participant based on specific historical messages. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * suggestSmartReplies(SuggestSmartRepliesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * suggestSmartReplies(ParticipantName parent) 
  * suggestSmartReplies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * suggestSmartRepliesCallable() 

  
SuggestKnowledgeAssist |  Gets knowledge assist suggestions based on historical messages. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * suggestKnowledgeAssist(SuggestKnowledgeAssistRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * suggestKnowledgeAssistCallable() 

  
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

This class can be customized by passing in a custom instance of ParticipantsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ParticipantsSettings participantsSettings =
         ParticipantsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ParticipantsClient participantsClient = ParticipantsClient.create(participantsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ParticipantsSettings participantsSettings =
         ParticipantsSettings.newBuilder().setEndpoint(myEndpoint).build();
     ParticipantsClient participantsClient = ParticipantsClient.create(participantsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ParticipantsSettings participantsSettings = ParticipantsSettings.newHttpJsonBuilder().build();
     ParticipantsClient participantsClient = ParticipantsClient.create(participantsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ParticipantsClient

## Static Methods 

### create()
    
    
    public static final ParticipantsClient create()

Constructs an instance of ParticipantsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ParticipantsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ParticipantsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ParticipantsSettings settings)
    
    
    public static final ParticipantsClient create(ParticipantsSettings settings)

Constructs an instance of ParticipantsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ParticipantsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ParticipantsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParticipantsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ParticipantsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ParticipantsStub stub)
    
    
    public static final ParticipantsClient create(ParticipantsStub stub)

Constructs an instance of ParticipantsClient, using the given stub for making calls. This is for advanced usage - prefer using create(ParticipantsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ParticipantsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.ParticipantsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParticipantsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ParticipantsClient)` |   
  
## Constructors 

### ParticipantsClient(ParticipantsSettings settings)
    
    
    protected ParticipantsClient(ParticipantsSettings settings)

Constructs an instance of ParticipantsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ParticipantsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ParticipantsSettings)`  
  
  
### ParticipantsClient(ParticipantsStub stub)
    
    
    protected ParticipantsClient(ParticipantsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ParticipantsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.ParticipantsStub)`  
  
  
## Methods 

### analyzeContent(@Nullable ParticipantName participant, AudioInput audioInput)
    
    
    public final AnalyzeContentResponse analyzeContent(@Nullable ParticipantName participant, AudioInput audioInput)

Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation.

Note: Always use agent versions for production traffic sent to virtual agents. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       ParticipantName participant =
           ParticipantName.ofProjectConversationParticipantName(
               "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]");
       AudioInput audioInput = AudioInput.newBuilder().build();
       AnalyzeContentResponse response = participantsClient.analyzeContent(participant, audioInput);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`participant` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ParticipantName`  
Required. The name of the participant this text comes from. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`.  
`audioInput` | `[AudioInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AudioInput)`  
The natural language speech audio to be processed.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AnalyzeContentResponse)` |   
  
### analyzeContent(@Nullable ParticipantName participant, EventInput eventInput)
    
    
    public final AnalyzeContentResponse analyzeContent(@Nullable ParticipantName participant, EventInput eventInput)

Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation.

Note: Always use agent versions for production traffic sent to virtual agents. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       ParticipantName participant =
           ParticipantName.ofProjectConversationParticipantName(
               "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]");
       EventInput eventInput = EventInput.newBuilder().build();
       AnalyzeContentResponse response = participantsClient.analyzeContent(participant, eventInput);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`participant` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ParticipantName`  
Required. The name of the participant this text comes from. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`.  
`eventInput` | `[EventInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.EventInput)`  
An input event to send to Dialogflow.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AnalyzeContentResponse)` |   
  
### analyzeContent(@Nullable ParticipantName participant, TextInput textInput)
    
    
    public final AnalyzeContentResponse analyzeContent(@Nullable ParticipantName participant, TextInput textInput)

Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation.

Note: Always use agent versions for production traffic sent to virtual agents. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       ParticipantName participant =
           ParticipantName.ofProjectConversationParticipantName(
               "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]");
       TextInput textInput = TextInput.newBuilder().build();
       AnalyzeContentResponse response = participantsClient.analyzeContent(participant, textInput);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`participant` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ParticipantName`  
Required. The name of the participant this text comes from. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`.  
`textInput` | `[TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.TextInput)`  
The natural language text to be processed.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AnalyzeContentResponse)` |   
  
### analyzeContent(AnalyzeContentRequest request)
    
    
    public final AnalyzeContentResponse analyzeContent(AnalyzeContentRequest request)

Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation.

Note: Always use agent versions for production traffic sent to virtual agents. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       AnalyzeContentRequest request =
           AnalyzeContentRequest.newBuilder()
               .setParticipant(
                   ParticipantName.ofProjectConversationParticipantName(
                           "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
                       .toString())
               .setReplyAudioConfig(OutputAudioConfig.newBuilder().build())
               .setQueryParams(QueryParameters.newBuilder().build())
               .setAssistQueryParams(AssistQueryParameters.newBuilder().build())
               .setCxParameters(Struct.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       AnalyzeContentResponse response = participantsClient.analyzeContent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AnalyzeContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AnalyzeContentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AnalyzeContentResponse)` |   
  
### analyzeContent(String participant, AudioInput audioInput)
    
    
    public final AnalyzeContentResponse analyzeContent(String participant, AudioInput audioInput)

Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation.

Note: Always use agent versions for production traffic sent to virtual agents. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       String participant =
           ParticipantName.ofProjectConversationParticipantName(
                   "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
               .toString();
       AudioInput audioInput = AudioInput.newBuilder().build();
       AnalyzeContentResponse response = participantsClient.analyzeContent(participant, audioInput);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`participant` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the participant this text comes from. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`.  
`audioInput` | `[AudioInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AudioInput)`  
The natural language speech audio to be processed.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AnalyzeContentResponse)` |   
  
### analyzeContent(String participant, EventInput eventInput)
    
    
    public final AnalyzeContentResponse analyzeContent(String participant, EventInput eventInput)

Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation.

Note: Always use agent versions for production traffic sent to virtual agents. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       String participant =
           ParticipantName.ofProjectConversationParticipantName(
                   "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
               .toString();
       EventInput eventInput = EventInput.newBuilder().build();
       AnalyzeContentResponse response = participantsClient.analyzeContent(participant, eventInput);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`participant` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the participant this text comes from. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`.  
`eventInput` | `[EventInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.EventInput)`  
An input event to send to Dialogflow.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AnalyzeContentResponse)` |   
  
### analyzeContent(String participant, TextInput textInput)
    
    
    public final AnalyzeContentResponse analyzeContent(String participant, TextInput textInput)

Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation.

Note: Always use agent versions for production traffic sent to virtual agents. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       String participant =
           ParticipantName.ofProjectConversationParticipantName(
                   "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
               .toString();
       TextInput textInput = TextInput.newBuilder().build();
       AnalyzeContentResponse response = participantsClient.analyzeContent(participant, textInput);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`participant` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the participant this text comes from. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`.  
`textInput` | `[TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.TextInput)`  
The natural language text to be processed.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AnalyzeContentResponse)` |   
  
### analyzeContentCallable()
    
    
    public final UnaryCallable<AnalyzeContentRequest,AnalyzeContentResponse> analyzeContentCallable()

Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation.

Note: Always use agent versions for production traffic sent to virtual agents. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       AnalyzeContentRequest request =
           AnalyzeContentRequest.newBuilder()
               .setParticipant(
                   ParticipantName.ofProjectConversationParticipantName(
                           "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
                       .toString())
               .setReplyAudioConfig(OutputAudioConfig.newBuilder().build())
               .setQueryParams(QueryParameters.newBuilder().build())
               .setAssistQueryParams(AssistQueryParameters.newBuilder().build())
               .setCxParameters(Struct.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<AnalyzeContentResponse> future =
           participantsClient.analyzeContentCallable().futureCall(request);
       // Do something.
       AnalyzeContentResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AnalyzeContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AnalyzeContentRequest),[AnalyzeContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.AnalyzeContentResponse)>` |   
  
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
  
### bidiStreamingAnalyzeContentCallable()
    
    
    public final BidiStreamingCallable<BidiStreamingAnalyzeContentRequest,BidiStreamingAnalyzeContentResponse> bidiStreamingAnalyzeContentCallable()

Bidirectional endless streaming version of StreamingAnalyzeContent.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       BidiStream<BidiStreamingAnalyzeContentRequest, BidiStreamingAnalyzeContentResponse>
           bidiStream = participantsClient.bidiStreamingAnalyzeContentCallable().call();
       BidiStreamingAnalyzeContentRequest request =
           BidiStreamingAnalyzeContentRequest.newBuilder().build();
       bidiStream.send(request);
       for (BidiStreamingAnalyzeContentResponse response : bidiStream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[BidiStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable.html)<[BidiStreamingAnalyzeContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.BidiStreamingAnalyzeContentRequest),[BidiStreamingAnalyzeContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.BidiStreamingAnalyzeContentResponse)>` |   
  
### close()
    
    
    public final void close()

### createParticipant(@Nullable ConversationName parent, Participant participant)
    
    
    public final Participant createParticipant(@Nullable ConversationName parent, Participant participant)

Creates a new participant in a conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       ConversationName parent =
           ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]");
       Participant participant = Participant.newBuilder().build();
       Participant response = participantsClient.createParticipant(parent, participant);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationName`  
Required. Resource identifier of the conversation adding the participant. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`participant` | `[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Participant)`  
Required. The participant to create.  
**Returns**  
---  
**Type** | **Description**  
`[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Participant)` |   
  
### createParticipant(CreateParticipantRequest request)
    
    
    public final Participant createParticipant(CreateParticipantRequest request)

Creates a new participant in a conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       CreateParticipantRequest request =
           CreateParticipantRequest.newBuilder()
               .setParent(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .setParticipant(Participant.newBuilder().build())
               .build();
       Participant response = participantsClient.createParticipant(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateParticipantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateParticipantRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Participant)` |   
  
### createParticipant(String parent, Participant participant)
    
    
    public final Participant createParticipant(String parent, Participant participant)

Creates a new participant in a conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       String parent =
           ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]").toString();
       Participant participant = Participant.newBuilder().build();
       Participant response = participantsClient.createParticipant(parent, participant);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource identifier of the conversation adding the participant. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`participant` | `[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Participant)`  
Required. The participant to create.  
**Returns**  
---  
**Type** | **Description**  
`[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Participant)` |   
  
### createParticipantCallable()
    
    
    public final UnaryCallable<CreateParticipantRequest,Participant> createParticipantCallable()

Creates a new participant in a conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       CreateParticipantRequest request =
           CreateParticipantRequest.newBuilder()
               .setParent(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .setParticipant(Participant.newBuilder().build())
               .build();
       ApiFuture<Participant> future =
           participantsClient.createParticipantCallable().futureCall(request);
       // Do something.
       Participant response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateParticipantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateParticipantRequest),[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Participant)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = participantsClient.getLocation(request);
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
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = participantsClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getParticipant(@Nullable ParticipantName name)
    
    
    public final Participant getParticipant(@Nullable ParticipantName name)

Retrieves a conversation participant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       ParticipantName name =
           ParticipantName.ofProjectConversationParticipantName(
               "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]");
       Participant response = participantsClient.getParticipant(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ParticipantName`  
Required. The name of the participant. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Participant)` |   
  
### getParticipant(GetParticipantRequest request)
    
    
    public final Participant getParticipant(GetParticipantRequest request)

Retrieves a conversation participant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       GetParticipantRequest request =
           GetParticipantRequest.newBuilder()
               .setName(
                   ParticipantName.ofProjectConversationParticipantName(
                           "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
                       .toString())
               .build();
       Participant response = participantsClient.getParticipant(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetParticipantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetParticipantRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Participant)` |   
  
### getParticipant(String name)
    
    
    public final Participant getParticipant(String name)

Retrieves a conversation participant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       String name =
           ParticipantName.ofProjectConversationParticipantName(
                   "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
               .toString();
       Participant response = participantsClient.getParticipant(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the participant. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Participant)` |   
  
### getParticipantCallable()
    
    
    public final UnaryCallable<GetParticipantRequest,Participant> getParticipantCallable()

Retrieves a conversation participant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       GetParticipantRequest request =
           GetParticipantRequest.newBuilder()
               .setName(
                   ParticipantName.ofProjectConversationParticipantName(
                           "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
                       .toString())
               .build();
       ApiFuture<Participant> future =
           participantsClient.getParticipantCallable().futureCall(request);
       // Do something.
       Participant response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetParticipantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetParticipantRequest),[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Participant)>` |   
  
### getSettings()
    
    
    public final @Nullable ParticipantsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ParticipantsSettings` |   
  
### getStub()
    
    
    public ParticipantsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ParticipantsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.stub.ParticipantsStub)` |   
  
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
    
    
    public final ParticipantsClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : participantsClient.listLocations(request).iterateAll()) {
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
`[ParticipantsClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ParticipantsClient.ListLocationsPagedResponse)` |   
  
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
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = participantsClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,ParticipantsClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           participantsClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ParticipantsClient.ListLocationsPagedResponse)>` |   
  
### listParticipants(@Nullable ConversationName parent)
    
    
    public final ParticipantsClient.ListParticipantsPagedResponse listParticipants(@Nullable ConversationName parent)

Returns the list of all participants in the specified conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       ConversationName parent =
           ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]");
       for (Participant element : participantsClient.listParticipants(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ConversationName`  
Required. The conversation to list all participants from. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[ParticipantsClient.ListParticipantsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ParticipantsClient.ListParticipantsPagedResponse)` |   
  
### listParticipants(ListParticipantsRequest request)
    
    
    public final ParticipantsClient.ListParticipantsPagedResponse listParticipants(ListParticipantsRequest request)

Returns the list of all participants in the specified conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       ListParticipantsRequest request =
           ListParticipantsRequest.newBuilder()
               .setParent(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Participant element : participantsClient.listParticipants(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListParticipantsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListParticipantsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ParticipantsClient.ListParticipantsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ParticipantsClient.ListParticipantsPagedResponse)` |   
  
### listParticipants(String parent)
    
    
    public final ParticipantsClient.ListParticipantsPagedResponse listParticipants(String parent)

Returns the list of all participants in the specified conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       String parent =
           ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]").toString();
       for (Participant element : participantsClient.listParticipants(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The conversation to list all participants from. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[ParticipantsClient.ListParticipantsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ParticipantsClient.ListParticipantsPagedResponse)` |   
  
### listParticipantsCallable()
    
    
    public final UnaryCallable<ListParticipantsRequest,ListParticipantsResponse> listParticipantsCallable()

Returns the list of all participants in the specified conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       ListParticipantsRequest request =
           ListParticipantsRequest.newBuilder()
               .setParent(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListParticipantsResponse response =
             participantsClient.listParticipantsCallable().call(request);
         for (Participant element : response.getParticipantsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListParticipantsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListParticipantsRequest),[ListParticipantsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListParticipantsResponse)>` |   
  
### listParticipantsPagedCallable()
    
    
    public final UnaryCallable<ListParticipantsRequest,ParticipantsClient.ListParticipantsPagedResponse> listParticipantsPagedCallable()

Returns the list of all participants in the specified conversation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       ListParticipantsRequest request =
           ListParticipantsRequest.newBuilder()
               .setParent(
                   ConversationName.ofProjectConversationName("[PROJECT]", "[CONVERSATION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Participant> future =
           participantsClient.listParticipantsPagedCallable().futureCall(request);
       // Do something.
       for (Participant element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListParticipantsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListParticipantsRequest),[ListParticipantsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ParticipantsClient.ListParticipantsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### streamingAnalyzeContentCallable()
    
    
    public final BidiStreamingCallable<StreamingAnalyzeContentRequest,StreamingAnalyzeContentResponse> streamingAnalyzeContentCallable()

Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation. Note: This method is only available through the gRPC API (not REST).

The top-level message sent to the client by the server is `StreamingAnalyzeContentResponse`. Multiple response messages can be returned in order. The first one or more messages contain the `recognition_result` field. Each result represents a more complete transcript of what the user said. The next message contains the `reply_text` field and potentially the `reply_audio` field. The message can also contain the `automated_agent_reply` field.

Note: Always use agent versions for production traffic sent to virtual agents. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       BidiStream<StreamingAnalyzeContentRequest, StreamingAnalyzeContentResponse> bidiStream =
           participantsClient.streamingAnalyzeContentCallable().call();
       StreamingAnalyzeContentRequest request =
           StreamingAnalyzeContentRequest.newBuilder()
               .setParticipant(
                   ParticipantName.ofProjectConversationParticipantName(
                           "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
                       .toString())
               .setReplyAudioConfig(OutputAudioConfig.newBuilder().build())
               .setQueryParams(QueryParameters.newBuilder().build())
               .setAssistQueryParams(AssistQueryParameters.newBuilder().build())
               .setCxParameters(Struct.newBuilder().build())
               .setEnableExtendedStreaming(true)
               .setEnablePartialAutomatedAgentReply(true)
               .setOutputMultipleUtterances(true)
               .setEnableDebuggingInfo(true)
               .build();
       bidiStream.send(request);
       for (StreamingAnalyzeContentResponse response : bidiStream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[BidiStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable.html)<[StreamingAnalyzeContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.StreamingAnalyzeContentRequest),[StreamingAnalyzeContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.StreamingAnalyzeContentResponse)>` |   
  
### streamingReactiveCompanionSuggestionsCallable()
    
    
    public final BidiStreamingCallable<StreamingReactiveCompanionSuggestionsRequest,StreamingReactiveCompanionSuggestionsResponse> streamingReactiveCompanionSuggestionsCallable()

External streaming API for direct human-agent-to-bot chats.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       BidiStream< streamingreactivecompanionsuggestionsrequest,="" streamingreactivecompanionsuggestionsresponse="">
           bidiStream = participantsClient.streamingReactiveCompanionSuggestionsCallable().call();
       StreamingReactiveCompanionSuggestionsRequest request =
           StreamingReactiveCompanionSuggestionsRequest.newBuilder()
               .setParticipant(
                   ParticipantName.ofProjectConversationParticipantName(
                           "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
                       .toString())
               .build();
       bidiStream.send(request);
       for (StreamingReactiveCompanionSuggestionsResponse response : bidiStream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[BidiStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable.html)<[StreamingReactiveCompanionSuggestionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.StreamingReactiveCompanionSuggestionsRequest),[StreamingReactiveCompanionSuggestionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.StreamingReactiveCompanionSuggestionsResponse)>` |   
  
### suggestArticles(@Nullable ParticipantName parent)
    
    
    public final SuggestArticlesResponse suggestArticles(@Nullable ParticipantName parent)

Gets suggested articles for a participant based on specific historical messages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       ParticipantName parent =
           ParticipantName.ofProjectConversationParticipantName(
               "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]");
       SuggestArticlesResponse response = participantsClient.suggestArticles(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ParticipantName`  
Required. The name of the participant to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[SuggestArticlesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestArticlesResponse)` |   
  
### suggestArticles(SuggestArticlesRequest request)
    
    
    public final SuggestArticlesResponse suggestArticles(SuggestArticlesRequest request)

Gets suggested articles for a participant based on specific historical messages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       SuggestArticlesRequest request =
           SuggestArticlesRequest.newBuilder()
               .setParent(
                   ParticipantName.ofProjectConversationParticipantName(
                           "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
                       .toString())
               .setLatestMessage(
                   MessageName.ofProjectConversationMessageName(
                           "[PROJECT]", "[CONVERSATION]", "[MESSAGE]")
                       .toString())
               .setContextSize(1116903569)
               .setAssistQueryParams(AssistQueryParameters.newBuilder().build())
               .build();
       SuggestArticlesResponse response = participantsClient.suggestArticles(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SuggestArticlesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestArticlesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SuggestArticlesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestArticlesResponse)` |   
  
### suggestArticles(String parent)
    
    
    public final SuggestArticlesResponse suggestArticles(String parent)

Gets suggested articles for a participant based on specific historical messages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       String parent =
           ParticipantName.ofProjectConversationParticipantName(
                   "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
               .toString();
       SuggestArticlesResponse response = participantsClient.suggestArticles(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the participant to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[SuggestArticlesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestArticlesResponse)` |   
  
### suggestArticlesCallable()
    
    
    public final UnaryCallable<SuggestArticlesRequest,SuggestArticlesResponse> suggestArticlesCallable()

Gets suggested articles for a participant based on specific historical messages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       SuggestArticlesRequest request =
           SuggestArticlesRequest.newBuilder()
               .setParent(
                   ParticipantName.ofProjectConversationParticipantName(
                           "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
                       .toString())
               .setLatestMessage(
                   MessageName.ofProjectConversationMessageName(
                           "[PROJECT]", "[CONVERSATION]", "[MESSAGE]")
                       .toString())
               .setContextSize(1116903569)
               .setAssistQueryParams(AssistQueryParameters.newBuilder().build())
               .build();
       ApiFuture<SuggestArticlesResponse> future =
           participantsClient.suggestArticlesCallable().futureCall(request);
       // Do something.
       SuggestArticlesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SuggestArticlesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestArticlesRequest),[SuggestArticlesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestArticlesResponse)>` |   
  
### suggestFaqAnswers(@Nullable ParticipantName parent)
    
    
    public final SuggestFaqAnswersResponse suggestFaqAnswers(@Nullable ParticipantName parent)

Gets suggested faq answers for a participant based on specific historical messages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       ParticipantName parent =
           ParticipantName.ofProjectConversationParticipantName(
               "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]");
       SuggestFaqAnswersResponse response = participantsClient.suggestFaqAnswers(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ParticipantName`  
Required. The name of the participant to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[SuggestFaqAnswersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestFaqAnswersResponse)` |   
  
### suggestFaqAnswers(SuggestFaqAnswersRequest request)
    
    
    public final SuggestFaqAnswersResponse suggestFaqAnswers(SuggestFaqAnswersRequest request)

Gets suggested faq answers for a participant based on specific historical messages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       SuggestFaqAnswersRequest request =
           SuggestFaqAnswersRequest.newBuilder()
               .setParent(
                   ParticipantName.ofProjectConversationParticipantName(
                           "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
                       .toString())
               .setLatestMessage(
                   MessageName.ofProjectConversationMessageName(
                           "[PROJECT]", "[CONVERSATION]", "[MESSAGE]")
                       .toString())
               .setContextSize(1116903569)
               .setAssistQueryParams(AssistQueryParameters.newBuilder().build())
               .build();
       SuggestFaqAnswersResponse response = participantsClient.suggestFaqAnswers(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SuggestFaqAnswersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestFaqAnswersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SuggestFaqAnswersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestFaqAnswersResponse)` |   
  
### suggestFaqAnswers(String parent)
    
    
    public final SuggestFaqAnswersResponse suggestFaqAnswers(String parent)

Gets suggested faq answers for a participant based on specific historical messages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       String parent =
           ParticipantName.ofProjectConversationParticipantName(
                   "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
               .toString();
       SuggestFaqAnswersResponse response = participantsClient.suggestFaqAnswers(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the participant to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[SuggestFaqAnswersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestFaqAnswersResponse)` |   
  
### suggestFaqAnswersCallable()
    
    
    public final UnaryCallable<SuggestFaqAnswersRequest,SuggestFaqAnswersResponse> suggestFaqAnswersCallable()

Gets suggested faq answers for a participant based on specific historical messages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       SuggestFaqAnswersRequest request =
           SuggestFaqAnswersRequest.newBuilder()
               .setParent(
                   ParticipantName.ofProjectConversationParticipantName(
                           "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
                       .toString())
               .setLatestMessage(
                   MessageName.ofProjectConversationMessageName(
                           "[PROJECT]", "[CONVERSATION]", "[MESSAGE]")
                       .toString())
               .setContextSize(1116903569)
               .setAssistQueryParams(AssistQueryParameters.newBuilder().build())
               .build();
       ApiFuture<SuggestFaqAnswersResponse> future =
           participantsClient.suggestFaqAnswersCallable().futureCall(request);
       // Do something.
       SuggestFaqAnswersResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SuggestFaqAnswersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestFaqAnswersRequest),[SuggestFaqAnswersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestFaqAnswersResponse)>` |   
  
### suggestKnowledgeAssist(SuggestKnowledgeAssistRequest request)
    
    
    public final SuggestKnowledgeAssistResponse suggestKnowledgeAssist(SuggestKnowledgeAssistRequest request)

Gets knowledge assist suggestions based on historical messages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       SuggestKnowledgeAssistRequest request =
           SuggestKnowledgeAssistRequest.newBuilder()
               .setParent(
                   ParticipantName.ofProjectConversationParticipantName(
                           "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
                       .toString())
               .setLatestMessage(
                   MessageName.ofProjectConversationMessageName(
                           "[PROJECT]", "[CONVERSATION]", "[MESSAGE]")
                       .toString())
               .setContextSize(1116903569)
               .setPreviousSuggestedQuery("previousSuggestedQuery-1914206660")
               .build();
       SuggestKnowledgeAssistResponse response = participantsClient.suggestKnowledgeAssist(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SuggestKnowledgeAssistRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestKnowledgeAssistRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SuggestKnowledgeAssistResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestKnowledgeAssistResponse)` |   
  
### suggestKnowledgeAssistCallable()
    
    
    public final UnaryCallable<SuggestKnowledgeAssistRequest,SuggestKnowledgeAssistResponse> suggestKnowledgeAssistCallable()

Gets knowledge assist suggestions based on historical messages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       SuggestKnowledgeAssistRequest request =
           SuggestKnowledgeAssistRequest.newBuilder()
               .setParent(
                   ParticipantName.ofProjectConversationParticipantName(
                           "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
                       .toString())
               .setLatestMessage(
                   MessageName.ofProjectConversationMessageName(
                           "[PROJECT]", "[CONVERSATION]", "[MESSAGE]")
                       .toString())
               .setContextSize(1116903569)
               .setPreviousSuggestedQuery("previousSuggestedQuery-1914206660")
               .build();
       ApiFuture<SuggestKnowledgeAssistResponse> future =
           participantsClient.suggestKnowledgeAssistCallable().futureCall(request);
       // Do something.
       SuggestKnowledgeAssistResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SuggestKnowledgeAssistRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestKnowledgeAssistRequest),[SuggestKnowledgeAssistResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestKnowledgeAssistResponse)>` |   
  
### suggestSmartReplies(@Nullable ParticipantName parent)
    
    
    public final SuggestSmartRepliesResponse suggestSmartReplies(@Nullable ParticipantName parent)

Gets smart replies for a participant based on specific historical messages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       ParticipantName parent =
           ParticipantName.ofProjectConversationParticipantName(
               "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]");
       SuggestSmartRepliesResponse response = participantsClient.suggestSmartReplies(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dialogflow.v2.ParticipantName`  
Required. The name of the participant to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[SuggestSmartRepliesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestSmartRepliesResponse)` |   
  
### suggestSmartReplies(SuggestSmartRepliesRequest request)
    
    
    public final SuggestSmartRepliesResponse suggestSmartReplies(SuggestSmartRepliesRequest request)

Gets smart replies for a participant based on specific historical messages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       SuggestSmartRepliesRequest request =
           SuggestSmartRepliesRequest.newBuilder()
               .setParent(
                   ParticipantName.ofProjectConversationParticipantName(
                           "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
                       .toString())
               .setCurrentTextInput(TextInput.newBuilder().build())
               .setLatestMessage(
                   MessageName.ofProjectConversationMessageName(
                           "[PROJECT]", "[CONVERSATION]", "[MESSAGE]")
                       .toString())
               .setContextSize(1116903569)
               .build();
       SuggestSmartRepliesResponse response = participantsClient.suggestSmartReplies(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SuggestSmartRepliesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestSmartRepliesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SuggestSmartRepliesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestSmartRepliesResponse)` |   
  
### suggestSmartReplies(String parent)
    
    
    public final SuggestSmartRepliesResponse suggestSmartReplies(String parent)

Gets smart replies for a participant based on specific historical messages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       String parent =
           ParticipantName.ofProjectConversationParticipantName(
                   "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
               .toString();
       SuggestSmartRepliesResponse response = participantsClient.suggestSmartReplies(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the participant to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`.  
**Returns**  
---  
**Type** | **Description**  
`[SuggestSmartRepliesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestSmartRepliesResponse)` |   
  
### suggestSmartRepliesCallable()
    
    
    public final UnaryCallable<SuggestSmartRepliesRequest,SuggestSmartRepliesResponse> suggestSmartRepliesCallable()

Gets smart replies for a participant based on specific historical messages.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       SuggestSmartRepliesRequest request =
           SuggestSmartRepliesRequest.newBuilder()
               .setParent(
                   ParticipantName.ofProjectConversationParticipantName(
                           "[PROJECT]", "[CONVERSATION]", "[PARTICIPANT]")
                       .toString())
               .setCurrentTextInput(TextInput.newBuilder().build())
               .setLatestMessage(
                   MessageName.ofProjectConversationMessageName(
                           "[PROJECT]", "[CONVERSATION]", "[MESSAGE]")
                       .toString())
               .setContextSize(1116903569)
               .build();
       ApiFuture<SuggestSmartRepliesResponse> future =
           participantsClient.suggestSmartRepliesCallable().futureCall(request);
       // Do something.
       SuggestSmartRepliesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SuggestSmartRepliesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestSmartRepliesRequest),[SuggestSmartRepliesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SuggestSmartRepliesResponse)>` |   
  
### updateParticipant(Participant participant, FieldMask updateMask)
    
    
    public final Participant updateParticipant(Participant participant, FieldMask updateMask)

Updates the specified participant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       Participant participant = Participant.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Participant response = participantsClient.updateParticipant(participant, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`participant` | `[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Participant)`  
Required. The participant to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The mask to specify which fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Participant)` |   
  
### updateParticipant(UpdateParticipantRequest request)
    
    
    public final Participant updateParticipant(UpdateParticipantRequest request)

Updates the specified participant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       UpdateParticipantRequest request =
           UpdateParticipantRequest.newBuilder()
               .setParticipant(Participant.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Participant response = participantsClient.updateParticipant(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateParticipantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateParticipantRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Participant)` |   
  
### updateParticipantCallable()
    
    
    public final UnaryCallable<UpdateParticipantRequest,Participant> updateParticipantCallable()

Updates the specified participant.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ParticipantsClient participantsClient = ParticipantsClient.create()) {
       UpdateParticipantRequest request =
           UpdateParticipantRequest.newBuilder()
               .setParticipant(Participant.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Participant> future =
           participantsClient.updateParticipantCallable().futureCall(request);
       // Do something.
       Participant response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateParticipantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateParticipantRequest),[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Participant)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
