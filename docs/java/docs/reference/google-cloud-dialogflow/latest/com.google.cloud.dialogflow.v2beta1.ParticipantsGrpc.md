---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ParticipantsGrpc
title: Class ParticipantsGrpc (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:41.207476+00:00
---

# Class ParticipantsGrpc (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ParticipantsGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ParticipantsGrpc (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 
    
    
    public final class ParticipantsGrpc

Service for managing Participants.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ParticipantsGrpc

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields 

### SERVICE_NAME
    
    
    public static final String SERVICE_NAME

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### bindService(ParticipantsGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(ParticipantsGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[ParticipantsGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ParticipantsGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getAnalyzeContentMethod()
    
    
    public static MethodDescriptor<AnalyzeContentRequest,AnalyzeContentResponse> getAnalyzeContentMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[AnalyzeContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.AnalyzeContentRequest),[AnalyzeContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.AnalyzeContentResponse)>` |   
  
### getBidiStreamingAnalyzeContentMethod()
    
    
    public static MethodDescriptor<BidiStreamingAnalyzeContentRequest,BidiStreamingAnalyzeContentResponse> getBidiStreamingAnalyzeContentMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BidiStreamingAnalyzeContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.BidiStreamingAnalyzeContentRequest),[BidiStreamingAnalyzeContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.BidiStreamingAnalyzeContentResponse)>` |   
  
### getCompileSuggestionMethod()
    
    
    public static MethodDescriptor<CompileSuggestionRequest,CompileSuggestionResponse> getCompileSuggestionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CompileSuggestionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.CompileSuggestionRequest),[CompileSuggestionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.CompileSuggestionResponse)>` |   
  
### getCreateParticipantMethod()
    
    
    public static MethodDescriptor<CreateParticipantRequest,Participant> getCreateParticipantMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateParticipantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.CreateParticipantRequest),[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.Participant)>` |   
  
### getGetParticipantMethod()
    
    
    public static MethodDescriptor<GetParticipantRequest,Participant> getGetParticipantMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetParticipantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.GetParticipantRequest),[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.Participant)>` |   
  
### getListParticipantsMethod()
    
    
    public static MethodDescriptor<ListParticipantsRequest,ListParticipantsResponse> getListParticipantsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListParticipantsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ListParticipantsRequest),[ListParticipantsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ListParticipantsResponse)>` |   
  
### getListSuggestionsMethod()
    
    
    public static MethodDescriptor<ListSuggestionsRequest,ListSuggestionsResponse> getListSuggestionsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListSuggestionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ListSuggestionsRequest),[ListSuggestionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ListSuggestionsResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getStreamingAnalyzeContentMethod()
    
    
    public static MethodDescriptor<StreamingAnalyzeContentRequest,StreamingAnalyzeContentResponse> getStreamingAnalyzeContentMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[StreamingAnalyzeContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentRequest),[StreamingAnalyzeContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentResponse)>` |   
  
### getSuggestArticlesMethod()
    
    
    public static MethodDescriptor<SuggestArticlesRequest,SuggestArticlesResponse> getSuggestArticlesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SuggestArticlesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SuggestArticlesRequest),[SuggestArticlesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SuggestArticlesResponse)>` |   
  
### getSuggestFaqAnswersMethod()
    
    
    public static MethodDescriptor<SuggestFaqAnswersRequest,SuggestFaqAnswersResponse> getSuggestFaqAnswersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SuggestFaqAnswersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SuggestFaqAnswersRequest),[SuggestFaqAnswersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SuggestFaqAnswersResponse)>` |   
  
### getSuggestKnowledgeAssistMethod()
    
    
    public static MethodDescriptor<SuggestKnowledgeAssistRequest,SuggestKnowledgeAssistResponse> getSuggestKnowledgeAssistMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SuggestKnowledgeAssistRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SuggestKnowledgeAssistRequest),[SuggestKnowledgeAssistResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SuggestKnowledgeAssistResponse)>` |   
  
### getSuggestSmartRepliesMethod()
    
    
    public static MethodDescriptor<SuggestSmartRepliesRequest,SuggestSmartRepliesResponse> getSuggestSmartRepliesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SuggestSmartRepliesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SuggestSmartRepliesRequest),[SuggestSmartRepliesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SuggestSmartRepliesResponse)>` |   
  
### getUpdateParticipantMethod()
    
    
    public static MethodDescriptor<UpdateParticipantRequest,Participant> getUpdateParticipantMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateParticipantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.UpdateParticipantRequest),[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.Participant)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static ParticipantsGrpc.ParticipantsBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParticipantsGrpc.ParticipantsBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ParticipantsGrpc.ParticipantsBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static ParticipantsGrpc.ParticipantsBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParticipantsGrpc.ParticipantsBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ParticipantsGrpc.ParticipantsBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static ParticipantsGrpc.ParticipantsFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParticipantsGrpc.ParticipantsFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ParticipantsGrpc.ParticipantsFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static ParticipantsGrpc.ParticipantsStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParticipantsGrpc.ParticipantsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ParticipantsGrpc.ParticipantsStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
