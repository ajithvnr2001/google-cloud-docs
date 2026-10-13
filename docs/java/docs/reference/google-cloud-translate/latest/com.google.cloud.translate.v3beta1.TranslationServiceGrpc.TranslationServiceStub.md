---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.TranslationServiceGrpc.TranslationServiceStub
title: Class TranslationServiceGrpc.TranslationServiceStub (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:10.882499+00:00
---

# Class TranslationServiceGrpc.TranslationServiceStub (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.TranslationServiceGrpc.TranslationServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TranslationServiceGrpc.TranslationServiceStub (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.5  2.2.0  2.1.13 
    
    
    public static final class TranslationServiceGrpc.TranslationServiceStub extends AbstractAsyncStub<TranslationServiceGrpc.TranslationServiceStub>

A stub to allow clients to do asynchronous rpc calls to service TranslationService.

Provides natural language translation operations.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > TranslationServiceGrpc.TranslationServiceStub

## Inherited Members

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

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

## Methods 

### batchTranslateDocument(BatchTranslateDocumentRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void batchTranslateDocument(BatchTranslateDocumentRequest request, StreamObserver<Operation> responseObserver)

Translates a large volume of document in asynchronous batch mode. This function provides real-time output as the inputs are being processed. If caller cancels a request, the partial results (for an input file, it's all or nothing) may still be available on the specified output location. This call returns immediately and you can use google.longrunning.Operation.name to poll the status of the call.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchTranslateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.BatchTranslateDocumentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### batchTranslateText(BatchTranslateTextRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void batchTranslateText(BatchTranslateTextRequest request, StreamObserver<Operation> responseObserver)

Translates a large volume of text in asynchronous batch mode. This function provides real-time output as the inputs are being processed. If caller cancels a request, the partial results (for an input file, it's all or nothing) may still be available on the specified output location. This call returns immediately and you can use google.longrunning.Operation.name to poll the status of the call.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchTranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.BatchTranslateTextRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected TranslationServiceGrpc.TranslationServiceStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[TranslationServiceGrpc.TranslationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.TranslationServiceGrpc.TranslationServiceStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createGlossary(CreateGlossaryRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createGlossary(CreateGlossaryRequest request, StreamObserver<Operation> responseObserver)

Creates a glossary and returns the long-running operation. Returns NOT_FOUND, if the project doesn't exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.CreateGlossaryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteGlossary(DeleteGlossaryRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteGlossary(DeleteGlossaryRequest request, StreamObserver<Operation> responseObserver)

Deletes a glossary, or cancels glossary construction if the glossary isn't created yet. Returns NOT_FOUND, if the glossary doesn't exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.DeleteGlossaryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### detectLanguage(DetectLanguageRequest request, StreamObserver<DetectLanguageResponse> responseObserver)
    
    
    public void detectLanguage(DetectLanguageRequest request, StreamObserver<DetectLanguageResponse> responseObserver)

Detects the language of text within a request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DetectLanguageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.DetectLanguageRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DetectLanguageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.DetectLanguageResponse)>`  
  
  
### getGlossary(GetGlossaryRequest request, StreamObserver<Glossary> responseObserver)
    
    
    public void getGlossary(GetGlossaryRequest request, StreamObserver<Glossary> responseObserver)

Gets a glossary. Returns NOT_FOUND, if the glossary doesn't exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.GetGlossaryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.Glossary)>`  
  
  
### getSupportedLanguages(GetSupportedLanguagesRequest request, StreamObserver<SupportedLanguages> responseObserver)
    
    
    public void getSupportedLanguages(GetSupportedLanguagesRequest request, StreamObserver<SupportedLanguages> responseObserver)

Returns a list of supported languages for translation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSupportedLanguagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.GetSupportedLanguagesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SupportedLanguages](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.SupportedLanguages)>`  
  
  
### listGlossaries(ListGlossariesRequest request, StreamObserver<ListGlossariesResponse> responseObserver)
    
    
    public void listGlossaries(ListGlossariesRequest request, StreamObserver<ListGlossariesResponse> responseObserver)

Lists glossaries in a project. Returns NOT_FOUND, if the project doesn't exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGlossariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.ListGlossariesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListGlossariesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.ListGlossariesResponse)>`  
  
  
### refineText(RefineTextRequest request, StreamObserver<RefineTextResponse> responseObserver)
    
    
    public void refineText(RefineTextRequest request, StreamObserver<RefineTextResponse> responseObserver)

Refines the input translated text to improve the quality.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RefineTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.RefineTextRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RefineTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.RefineTextResponse)>`  
  
  
### translateDocument(TranslateDocumentRequest request, StreamObserver<TranslateDocumentResponse> responseObserver)
    
    
    public void translateDocument(TranslateDocumentRequest request, StreamObserver<TranslateDocumentResponse> responseObserver)

Translates documents in synchronous mode.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TranslateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.TranslateDocumentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[TranslateDocumentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.TranslateDocumentResponse)>`  
  
  
### translateText(TranslateTextRequest request, StreamObserver<TranslateTextResponse> responseObserver)
    
    
    public void translateText(TranslateTextRequest request, StreamObserver<TranslateTextResponse> responseObserver)

Translates input text and returns translated text.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.TranslateTextRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[TranslateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.TranslateTextResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
