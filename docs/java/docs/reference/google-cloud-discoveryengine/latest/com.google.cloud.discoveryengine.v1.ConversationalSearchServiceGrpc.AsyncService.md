---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceGrpc.AsyncService
title: Interface ConversationalSearchServiceGrpc.AsyncService (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:58.585208+00:00
---

# Interface ConversationalSearchServiceGrpc.AsyncService (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConversationalSearchServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ConversationalSearchServiceGrpc.AsyncService (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface ConversationalSearchServiceGrpc.AsyncService

Service for conversational search.

## Methods 

### answerQuery(AnswerQueryRequest request, StreamObserver<AnswerQueryResponse> responseObserver)
    
    
    public default void answerQuery(AnswerQueryRequest request, StreamObserver<AnswerQueryResponse> responseObserver)

Answer query method.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AnswerQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AnswerQueryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AnswerQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AnswerQueryResponse)>`  
  
  
### converseConversation(ConverseConversationRequest request, StreamObserver<ConverseConversationResponse> responseObserver)
    
    
    public default void converseConversation(ConverseConversationRequest request, StreamObserver<ConverseConversationResponse> responseObserver)

Converses a conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ConverseConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConverseConversationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ConverseConversationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ConverseConversationResponse)>`  
  
  
### createConversation(CreateConversationRequest request, StreamObserver<Conversation> responseObserver)
    
    
    public default void createConversation(CreateConversationRequest request, StreamObserver<Conversation> responseObserver)

Creates a Conversation. If the Conversation to create already exists, an ALREADY_EXISTS error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateConversationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)>`  
  
  
### createSession(CreateSessionRequest request, StreamObserver<Session> responseObserver)
    
    
    public default void createSession(CreateSessionRequest request, StreamObserver<Session> responseObserver)

Creates a Session. If the Session to create already exists, an ALREADY_EXISTS error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateSessionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)>`  
  
  
### deleteConversation(DeleteConversationRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteConversation(DeleteConversationRequest request, StreamObserver<Empty> responseObserver)

Deletes a Conversation. If the Conversation to delete does not exist, a NOT_FOUND error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteConversationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteSession(DeleteSessionRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteSession(DeleteSessionRequest request, StreamObserver<Empty> responseObserver)

Deletes a Session. If the Session to delete does not exist, a NOT_FOUND error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteSessionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### getAnswer(GetAnswerRequest request, StreamObserver<Answer> responseObserver)
    
    
    public default void getAnswer(GetAnswerRequest request, StreamObserver<Answer> responseObserver)

Gets a Answer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnswerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetAnswerRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Answer](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Answer)>`  
  
  
### getConversation(GetConversationRequest request, StreamObserver<Conversation> responseObserver)
    
    
    public default void getConversation(GetConversationRequest request, StreamObserver<Conversation> responseObserver)

Gets a Conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetConversationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)>`  
  
  
### getSession(GetSessionRequest request, StreamObserver<Session> responseObserver)
    
    
    public default void getSession(GetSessionRequest request, StreamObserver<Session> responseObserver)

Gets a Session.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetSessionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)>`  
  
  
### listConversations(ListConversationsRequest request, StreamObserver<ListConversationsResponse> responseObserver)
    
    
    public default void listConversations(ListConversationsRequest request, StreamObserver<ListConversationsResponse> responseObserver)

Lists all Conversations by their parent DataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListConversationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListConversationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListConversationsResponse)>`  
  
  
### listSessions(ListSessionsRequest request, StreamObserver<ListSessionsResponse> responseObserver)
    
    
    public default void listSessions(ListSessionsRequest request, StreamObserver<ListSessionsResponse> responseObserver)

Lists all Sessions by their parent DataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSessionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListSessionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSessionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListSessionsResponse)>`  
  
  
### streamAnswerQuery(AnswerQueryRequest request, StreamObserver<AnswerQueryResponse> responseObserver)
    
    
    public default void streamAnswerQuery(AnswerQueryRequest request, StreamObserver<AnswerQueryResponse> responseObserver)

Answer query method (streaming). It takes one AnswerQueryRequest and returns multiple AnswerQueryResponse messages in a stream.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AnswerQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AnswerQueryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AnswerQueryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.AnswerQueryResponse)>`  
  
  
### updateConversation(UpdateConversationRequest request, StreamObserver<Conversation> responseObserver)
    
    
    public default void updateConversation(UpdateConversationRequest request, StreamObserver<Conversation> responseObserver)

Updates a Conversation. Conversation action type cannot be changed. If the Conversation to update does not exist, a NOT_FOUND error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateConversationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Conversation)>`  
  
  
### updateSession(UpdateSessionRequest request, StreamObserver<Session> responseObserver)
    
    
    public default void updateSession(UpdateSessionRequest request, StreamObserver<Session> responseObserver)

Updates a Session. Session action type cannot be changed. If the Session to update does not exist, a NOT_FOUND error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateSessionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Session](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Session)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
