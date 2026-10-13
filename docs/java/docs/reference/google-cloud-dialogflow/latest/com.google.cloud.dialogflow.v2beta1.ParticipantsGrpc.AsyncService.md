---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ParticipantsGrpc.AsyncService
title: Interface ParticipantsGrpc.AsyncService (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:36.782085+00:00
---

# Interface ParticipantsGrpc.AsyncService (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ParticipantsGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ParticipantsGrpc.AsyncService (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 
    
    
    public static interface ParticipantsGrpc.AsyncService

Service for managing Participants.

## Methods 

### analyzeContent(AnalyzeContentRequest request, StreamObserver<AnalyzeContentResponse> responseObserver)
    
    
    public default void analyzeContent(AnalyzeContentRequest request, StreamObserver<AnalyzeContentResponse> responseObserver)

Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation. Note: Always use agent versions for production traffic sent to virtual agents. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AnalyzeContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.AnalyzeContentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AnalyzeContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.AnalyzeContentResponse)>`  
  
  
### bidiStreamingAnalyzeContent(StreamObserver<BidiStreamingAnalyzeContentResponse> responseObserver)
    
    
    public default StreamObserver<BidiStreamingAnalyzeContentRequest> bidiStreamingAnalyzeContent(StreamObserver<BidiStreamingAnalyzeContentResponse> responseObserver)

Bidirectional endless streaming version of StreamingAnalyzeContent.

**Parameter**  
---  
**Name** | **Description**  
`responseObserver` | `io.grpc.stub.StreamObserver<[BidiStreamingAnalyzeContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.BidiStreamingAnalyzeContentResponse)>`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.stub.StreamObserver<[BidiStreamingAnalyzeContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.BidiStreamingAnalyzeContentRequest)>` |   
  
### compileSuggestion(CompileSuggestionRequest request, StreamObserver<CompileSuggestionResponse> responseObserver) (deprecated)
    
    
    public default void compileSuggestion(CompileSuggestionRequest request, StreamObserver<CompileSuggestionResponse> responseObserver)

Deprecated. use SuggestArticles and SuggestFaqAnswers instead. Gets suggestions for a participant based on specific historical messages. Note that ListSuggestions will only list the auto-generated suggestions, while CompileSuggestion will try to compile suggestion based on the provided conversation context in the real time.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CompileSuggestionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.CompileSuggestionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CompileSuggestionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.CompileSuggestionResponse)>`  
  
  
### createParticipant(CreateParticipantRequest request, StreamObserver<Participant> responseObserver)
    
    
    public default void createParticipant(CreateParticipantRequest request, StreamObserver<Participant> responseObserver)

Creates a new participant in a conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateParticipantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.CreateParticipantRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.Participant)>`  
  
  
### getParticipant(GetParticipantRequest request, StreamObserver<Participant> responseObserver)
    
    
    public default void getParticipant(GetParticipantRequest request, StreamObserver<Participant> responseObserver)

Retrieves a conversation participant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetParticipantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.GetParticipantRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.Participant)>`  
  
  
### listParticipants(ListParticipantsRequest request, StreamObserver<ListParticipantsResponse> responseObserver)
    
    
    public default void listParticipants(ListParticipantsRequest request, StreamObserver<ListParticipantsResponse> responseObserver)

Returns the list of all participants in the specified conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListParticipantsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ListParticipantsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListParticipantsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ListParticipantsResponse)>`  
  
  
### listSuggestions(ListSuggestionsRequest request, StreamObserver<ListSuggestionsResponse> responseObserver) (deprecated)
    
    
    public default void listSuggestions(ListSuggestionsRequest request, StreamObserver<ListSuggestionsResponse> responseObserver)

Deprecated: Use inline suggestion, event based suggestion or Suggestion* API instead. See HumanAgentAssistantConfig.name for more details. Removal Date: 2020-09-01. Retrieves suggestions for live agents. This method should be used by human agent client software to fetch auto generated suggestions in real-time, while the conversation with an end user is in progress. The functionality is implemented in terms of the [list pagination](https://cloud.google.com/apis/design/design_patterns#list_pagination) design pattern. The client app should use the `next_page_token` field to fetch the next batch of suggestions. `suggestions` are sorted by `create_time` in descending order. To fetch latest suggestion, just set `page_size` to 1. To fetch new suggestions without duplication, send request with filter `create_time_epoch_microseconds > [first item's create_time of previous request]` and empty page_token.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSuggestionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ListSuggestionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSuggestionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ListSuggestionsResponse)>`  
  
  
### streamingAnalyzeContent(StreamObserver<StreamingAnalyzeContentResponse> responseObserver)
    
    
    public default StreamObserver<StreamingAnalyzeContentRequest> streamingAnalyzeContent(StreamObserver<StreamingAnalyzeContentResponse> responseObserver)

Adds a text (e.g., chat) or audio (e.g., phone recording) message from a participant into the conversation. Note: This method is only available through the gRPC API (not REST). The top-level message sent to the client by the server is `StreamingAnalyzeContentResponse`. Multiple response messages can be returned in order. The first one or more messages contain the `recognition_result` field. Each result represents a more complete transcript of what the user said. The next message contains the `reply_text` field, and potentially the `reply_audio` and/or the `automated_agent_reply` fields. Note: Always use agent versions for production traffic sent to virtual agents. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions).

**Parameter**  
---  
**Name** | **Description**  
`responseObserver` | `io.grpc.stub.StreamObserver<[StreamingAnalyzeContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentResponse)>`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.stub.StreamObserver<[StreamingAnalyzeContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentRequest)>` |   
  
### suggestArticles(SuggestArticlesRequest request, StreamObserver<SuggestArticlesResponse> responseObserver)
    
    
    public default void suggestArticles(SuggestArticlesRequest request, StreamObserver<SuggestArticlesResponse> responseObserver)

Gets suggested articles for a participant based on specific historical messages. Note that ListSuggestions will only list the auto-generated suggestions, while CompileSuggestion will try to compile suggestion based on the provided conversation context in the real time.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SuggestArticlesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SuggestArticlesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SuggestArticlesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SuggestArticlesResponse)>`  
  
  
### suggestFaqAnswers(SuggestFaqAnswersRequest request, StreamObserver<SuggestFaqAnswersResponse> responseObserver)
    
    
    public default void suggestFaqAnswers(SuggestFaqAnswersRequest request, StreamObserver<SuggestFaqAnswersResponse> responseObserver)

Gets suggested faq answers for a participant based on specific historical messages.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SuggestFaqAnswersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SuggestFaqAnswersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SuggestFaqAnswersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SuggestFaqAnswersResponse)>`  
  
  
### suggestKnowledgeAssist(SuggestKnowledgeAssistRequest request, StreamObserver<SuggestKnowledgeAssistResponse> responseObserver)
    
    
    public default void suggestKnowledgeAssist(SuggestKnowledgeAssistRequest request, StreamObserver<SuggestKnowledgeAssistResponse> responseObserver)

Gets knowledge assist suggestions based on historical messages.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SuggestKnowledgeAssistRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SuggestKnowledgeAssistRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SuggestKnowledgeAssistResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SuggestKnowledgeAssistResponse)>`  
  
  
### suggestSmartReplies(SuggestSmartRepliesRequest request, StreamObserver<SuggestSmartRepliesResponse> responseObserver)
    
    
    public default void suggestSmartReplies(SuggestSmartRepliesRequest request, StreamObserver<SuggestSmartRepliesResponse> responseObserver)

Gets smart replies for a participant based on specific historical messages.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SuggestSmartRepliesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SuggestSmartRepliesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SuggestSmartRepliesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SuggestSmartRepliesResponse)>`  
  
  
### updateParticipant(UpdateParticipantRequest request, StreamObserver<Participant> responseObserver)
    
    
    public default void updateParticipant(UpdateParticipantRequest request, StreamObserver<Participant> responseObserver)

Updates the specified participant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateParticipantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.UpdateParticipantRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.Participant)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
