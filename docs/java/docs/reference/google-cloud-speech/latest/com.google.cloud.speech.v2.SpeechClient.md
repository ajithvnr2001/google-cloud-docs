---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient
title: Class SpeechClient (4.94.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:47.716373+00:00
---

# Class SpeechClient (4.94.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SpeechClient (4.94.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.94.0 (latest)  4.90.0  4.89.0  4.88.0  4.86.0  4.83.0  4.82.0  4.80.0  4.78.0  4.77.0  4.75.0  4.73.0  4.71.0  4.70.0  4.69.0  4.68.0  4.67.0  4.65.0  4.63.0  4.62.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.44.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.0.0  2.6.1  2.5.9  2.4.0  2.3.0  2.2.15 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-speech/google-cloud-speech/src/main/java/com/google/cloud/speech/v2/SpeechClient.java)| [Product Reference](https://cloud.google.com/speech-to-text/docs/)| [REST Documentation](https://cloud.google.com/speech-to-text/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/speech-to-text/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Enables speech transcription and resource management.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       RecognizerName name = RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]");
       Recognizer response = speechClient.getRecognizer(name);
     }
     

Note: close() needs to be called on the SpeechClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateRecognizer |  Creates a Recognizer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createRecognizerAsync(CreateRecognizerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createRecognizerAsync(LocationName parent, Recognizer recognizer, String recognizerId) 
  * createRecognizerAsync(String parent, Recognizer recognizer, String recognizerId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createRecognizerOperationCallable() 
  * createRecognizerCallable() 

  
ListRecognizers |  Lists Recognizers. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRecognizers(ListRecognizersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRecognizers(LocationName parent) 
  * listRecognizers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRecognizersPagedCallable() 
  * listRecognizersCallable() 

  
GetRecognizer |  Returns the requested Recognizer. Fails with NOT_FOUND if the requested Recognizer doesn't exist. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRecognizer(GetRecognizerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRecognizer(RecognizerName name) 
  * getRecognizer(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRecognizerCallable() 

  
UpdateRecognizer |  Updates the Recognizer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateRecognizerAsync(UpdateRecognizerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateRecognizerAsync(Recognizer recognizer, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateRecognizerOperationCallable() 
  * updateRecognizerCallable() 

  
DeleteRecognizer |  Deletes the Recognizer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteRecognizerAsync(DeleteRecognizerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteRecognizerAsync(RecognizerName name) 
  * deleteRecognizerAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteRecognizerOperationCallable() 
  * deleteRecognizerCallable() 

  
UndeleteRecognizer |  Undeletes the Recognizer. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * undeleteRecognizerAsync(UndeleteRecognizerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * undeleteRecognizerAsync(RecognizerName name) 
  * undeleteRecognizerAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * undeleteRecognizerOperationCallable() 
  * undeleteRecognizerCallable() 

  
Recognize |  Performs synchronous Speech recognition: receive results after all audio has been sent and processed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * recognize(RecognizeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * recognize(RecognizerName recognizer, RecognitionConfig config, FieldMask configMask, ByteString content) 
  * recognize(RecognizerName recognizer, RecognitionConfig config, FieldMask configMask, String uri) 
  * recognize(String recognizer, RecognitionConfig config, FieldMask configMask, ByteString content) 
  * recognize(String recognizer, RecognitionConfig config, FieldMask configMask, String uri) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * recognizeCallable() 

  
StreamingRecognize |  Performs bidirectional streaming speech recognition: receive results while sending audio. This method is only available via the gRPC API (not REST). |  Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * streamingRecognizeCallable() 

  
BatchRecognize |  Performs batch asynchronous speech recognition: send a request with N audio files and receive a long running operation that can be polled to see when the transcriptions are finished. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchRecognizeAsync(BatchRecognizeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * batchRecognizeAsync(RecognizerName recognizer, RecognitionConfig config, FieldMask configMask, List<BatchRecognizeFileMetadata> files) 
  * batchRecognizeAsync(String recognizer, RecognitionConfig config, FieldMask configMask, List<BatchRecognizeFileMetadata> files) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchRecognizeOperationCallable() 
  * batchRecognizeCallable() 

  
GetConfig |  Returns the requested Config. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getConfig(GetConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getConfig(ConfigName name) 
  * getConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getConfigCallable() 

  
UpdateConfig |  Updates the Config. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateConfig(UpdateConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateConfig(Config config, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateConfigCallable() 

  
CreateCustomClass |  Creates a CustomClass. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCustomClassAsync(CreateCustomClassRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createCustomClassAsync(LocationName parent, CustomClass customClass, String customClassId) 
  * createCustomClassAsync(String parent, CustomClass customClass, String customClassId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCustomClassOperationCallable() 
  * createCustomClassCallable() 

  
ListCustomClasses |  Lists CustomClasses. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCustomClasses(ListCustomClassesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCustomClasses(LocationName parent) 
  * listCustomClasses(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCustomClassesPagedCallable() 
  * listCustomClassesCallable() 

  
GetCustomClass |  Returns the requested CustomClass. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCustomClass(GetCustomClassRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCustomClass(CustomClassName name) 
  * getCustomClass(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCustomClassCallable() 

  
UpdateCustomClass |  Updates the CustomClass. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCustomClassAsync(UpdateCustomClassRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateCustomClassAsync(CustomClass customClass, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCustomClassOperationCallable() 
  * updateCustomClassCallable() 

  
DeleteCustomClass |  Deletes the CustomClass. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteCustomClassAsync(DeleteCustomClassRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteCustomClassAsync(CustomClassName name) 
  * deleteCustomClassAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCustomClassOperationCallable() 
  * deleteCustomClassCallable() 

  
UndeleteCustomClass |  Undeletes the CustomClass. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * undeleteCustomClassAsync(UndeleteCustomClassRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * undeleteCustomClassAsync(CustomClassName name) 
  * undeleteCustomClassAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * undeleteCustomClassOperationCallable() 
  * undeleteCustomClassCallable() 

  
CreatePhraseSet |  Creates a PhraseSet. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPhraseSetAsync(CreatePhraseSetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createPhraseSetAsync(LocationName parent, PhraseSet phraseSet, String phraseSetId) 
  * createPhraseSetAsync(String parent, PhraseSet phraseSet, String phraseSetId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPhraseSetOperationCallable() 
  * createPhraseSetCallable() 

  
ListPhraseSets |  Lists PhraseSets. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPhraseSets(ListPhraseSetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPhraseSets(LocationName parent) 
  * listPhraseSets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPhraseSetsPagedCallable() 
  * listPhraseSetsCallable() 

  
GetPhraseSet |  Returns the requested PhraseSet. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPhraseSet(GetPhraseSetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPhraseSet(PhraseSetName name) 
  * getPhraseSet(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPhraseSetCallable() 

  
UpdatePhraseSet |  Updates the PhraseSet. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePhraseSetAsync(UpdatePhraseSetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updatePhraseSetAsync(PhraseSet phraseSet, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePhraseSetOperationCallable() 
  * updatePhraseSetCallable() 

  
DeletePhraseSet |  Deletes the PhraseSet. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePhraseSetAsync(DeletePhraseSetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deletePhraseSetAsync(PhraseSetName name) 
  * deletePhraseSetAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePhraseSetOperationCallable() 
  * deletePhraseSetCallable() 

  
UndeletePhraseSet |  Undeletes the PhraseSet. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * undeletePhraseSetAsync(UndeletePhraseSetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * undeletePhraseSetAsync(PhraseSetName name) 
  * undeletePhraseSetAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * undeletePhraseSetOperationCallable() 
  * undeletePhraseSetCallable() 

  
ListLocations |  Lists information about the supported locations for this service.This method can be called in two ways:  * **List all public locations:** Use the path `GET /v1/locations`.* **List project-visible locations:** Use the path`GET /v1/projects/{project_id}/locations`. This may include publiclocations as well as private or other locations specifically visibleto the project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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

This class can be customized by passing in a custom instance of SpeechSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SpeechSettings speechSettings =
         SpeechSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SpeechClient speechClient = SpeechClient.create(speechSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SpeechSettings speechSettings = SpeechSettings.newBuilder().setEndpoint(myEndpoint).build();
     SpeechClient speechClient = SpeechClient.create(speechSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SpeechSettings speechSettings = SpeechSettings.newHttpJsonBuilder().build();
     SpeechClient speechClient = SpeechClient.create(speechSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SpeechClient

## Static Methods 

### create()
    
    
    public static final SpeechClient create()

Constructs an instance of SpeechClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SpeechSettings settings)
    
    
    public static final SpeechClient create(SpeechSettings settings)

Constructs an instance of SpeechClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SpeechSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SpeechStub stub)
    
    
    public static final SpeechClient create(SpeechStub stub)

Constructs an instance of SpeechClient, using the given stub for making calls. This is for advanced usage - prefer using create(SpeechSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SpeechStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.stub.SpeechStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient)` |   
  
## Constructors 

### SpeechClient(SpeechSettings settings)
    
    
    protected SpeechClient(SpeechSettings settings)

Constructs an instance of SpeechClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SpeechSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechSettings)`  
  
  
### SpeechClient(SpeechStub stub)
    
    
    protected SpeechClient(SpeechStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SpeechStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.stub.SpeechStub)`  
  
  
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
  
### batchRecognizeAsync(@Nullable RecognizerName recognizer, RecognitionConfig config, FieldMask configMask, List<BatchRecognizeFileMetadata> files)
    
    
    public final OperationFuture<BatchRecognizeResponse,OperationMetadata> batchRecognizeAsync(@Nullable RecognizerName recognizer, RecognitionConfig config, FieldMask configMask, List<BatchRecognizeFileMetadata> files)

Performs batch asynchronous speech recognition: send a request with N audio files and receive a long running operation that can be polled to see when the transcriptions are finished.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       RecognizerName recognizer = RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]");
       RecognitionConfig config = RecognitionConfig.newBuilder().build();
       FieldMask configMask = FieldMask.newBuilder().build();
       List<BatchRecognizeFileMetadata> files = new ArrayList<>();
       BatchRecognizeResponse response =
           speechClient.batchRecognizeAsync(recognizer, config, configMask, files).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`recognizer` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.RecognizerName`  
Required. The name of the Recognizer to use during recognition. The expected format is `projects/{project}/locations/{location}/recognizers/{recognizer}`. The {recognizer} segment may be set to `_` to use an empty implicit Recognizer.  
`config` | `[RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognitionConfig)`  
Features and audio metadata to use for the Automatic Speech Recognition. This field in combination with the config_mask field can be used to override parts of the default_recognition_config of the Recognizer resource.  
`configMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields in config that override the values in the default_recognition_config of the recognizer during this recognition request. If no mask is provided, all given fields in config override the values in the recognizer for this recognition request. If a mask is provided, only the fields listed in the mask override the config in the recognizer for this recognition request. If a wildcard (`*`) is provided, config completely overrides and replaces the config in the recognizer for this recognition request.  
`files` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[BatchRecognizeFileMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.BatchRecognizeFileMetadata)>`  
Audio files with file metadata for ASR. The maximum number of files allowed to be specified is 15.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchRecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.BatchRecognizeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### batchRecognizeAsync(BatchRecognizeRequest request)
    
    
    public final OperationFuture<BatchRecognizeResponse,OperationMetadata> batchRecognizeAsync(BatchRecognizeRequest request)

Performs batch asynchronous speech recognition: send a request with N audio files and receive a long running operation that can be polled to see when the transcriptions are finished.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       BatchRecognizeRequest request =
           BatchRecognizeRequest.newBuilder()
               .setRecognizer(
                   RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString())
               .setConfig(RecognitionConfig.newBuilder().build())
               .setConfigMask(FieldMask.newBuilder().build())
               .addAllFiles(new ArrayList<BatchRecognizeFileMetadata>())
               .setRecognitionOutputConfig(RecognitionOutputConfig.newBuilder().build())
               .build();
       BatchRecognizeResponse response = speechClient.batchRecognizeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchRecognizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.BatchRecognizeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchRecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.BatchRecognizeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### batchRecognizeAsync(String recognizer, RecognitionConfig config, FieldMask configMask, List<BatchRecognizeFileMetadata> files)
    
    
    public final OperationFuture<BatchRecognizeResponse,OperationMetadata> batchRecognizeAsync(String recognizer, RecognitionConfig config, FieldMask configMask, List<BatchRecognizeFileMetadata> files)

Performs batch asynchronous speech recognition: send a request with N audio files and receive a long running operation that can be polled to see when the transcriptions are finished.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String recognizer = RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString();
       RecognitionConfig config = RecognitionConfig.newBuilder().build();
       FieldMask configMask = FieldMask.newBuilder().build();
       List<BatchRecognizeFileMetadata> files = new ArrayList<>();
       BatchRecognizeResponse response =
           speechClient.batchRecognizeAsync(recognizer, config, configMask, files).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`recognizer` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Recognizer to use during recognition. The expected format is `projects/{project}/locations/{location}/recognizers/{recognizer}`. The {recognizer} segment may be set to `_` to use an empty implicit Recognizer.  
`config` | `[RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognitionConfig)`  
Features and audio metadata to use for the Automatic Speech Recognition. This field in combination with the config_mask field can be used to override parts of the default_recognition_config of the Recognizer resource.  
`configMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields in config that override the values in the default_recognition_config of the recognizer during this recognition request. If no mask is provided, all given fields in config override the values in the recognizer for this recognition request. If a mask is provided, only the fields listed in the mask override the config in the recognizer for this recognition request. If a wildcard (`*`) is provided, config completely overrides and replaces the config in the recognizer for this recognition request.  
`files` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[BatchRecognizeFileMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.BatchRecognizeFileMetadata)>`  
Audio files with file metadata for ASR. The maximum number of files allowed to be specified is 15.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchRecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.BatchRecognizeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### batchRecognizeCallable()
    
    
    public final UnaryCallable<BatchRecognizeRequest,Operation> batchRecognizeCallable()

Performs batch asynchronous speech recognition: send a request with N audio files and receive a long running operation that can be polled to see when the transcriptions are finished.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       BatchRecognizeRequest request =
           BatchRecognizeRequest.newBuilder()
               .setRecognizer(
                   RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString())
               .setConfig(RecognitionConfig.newBuilder().build())
               .setConfigMask(FieldMask.newBuilder().build())
               .addAllFiles(new ArrayList<BatchRecognizeFileMetadata>())
               .setRecognitionOutputConfig(RecognitionOutputConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future = speechClient.batchRecognizeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchRecognizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.BatchRecognizeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchRecognizeOperationCallable()
    
    
    public final OperationCallable<BatchRecognizeRequest,BatchRecognizeResponse,OperationMetadata> batchRecognizeOperationCallable()

Performs batch asynchronous speech recognition: send a request with N audio files and receive a long running operation that can be polled to see when the transcriptions are finished.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       BatchRecognizeRequest request =
           BatchRecognizeRequest.newBuilder()
               .setRecognizer(
                   RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString())
               .setConfig(RecognitionConfig.newBuilder().build())
               .setConfigMask(FieldMask.newBuilder().build())
               .addAllFiles(new ArrayList<BatchRecognizeFileMetadata>())
               .setRecognitionOutputConfig(RecognitionOutputConfig.newBuilder().build())
               .build();
       OperationFuture<BatchRecognizeResponse, OperationMetadata> future =
           speechClient.batchRecognizeOperationCallable().futureCall(request);
       // Do something.
       BatchRecognizeResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchRecognizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.BatchRecognizeRequest),[BatchRecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.BatchRecognizeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### close()
    
    
    public final void close()

### createCustomClassAsync(@Nullable LocationName parent, CustomClass customClass, String customClassId)
    
    
    public final OperationFuture<CustomClass,OperationMetadata> createCustomClassAsync(@Nullable LocationName parent, CustomClass customClass, String customClassId)

Creates a CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       CustomClass customClass = CustomClass.newBuilder().build();
       String customClassId = "customClassId1871032322";
       CustomClass response =
           speechClient.createCustomClassAsync(parent, customClass, customClassId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.LocationName`  
Required. The project and location where this CustomClass will be created. The expected format is `projects/{project}/locations/{location}`.  
`customClass` | `[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass)`  
Required. The CustomClass to create.  
`customClassId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The ID to use for the CustomClass, which will become the final component of the CustomClass's resource name. This value should be 4-63 characters, and valid characters are /a-z-/.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### createCustomClassAsync(CreateCustomClassRequest request)
    
    
    public final OperationFuture<CustomClass,OperationMetadata> createCustomClassAsync(CreateCustomClassRequest request)

Creates a CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       CreateCustomClassRequest request =
           CreateCustomClassRequest.newBuilder()
               .setCustomClass(CustomClass.newBuilder().build())
               .setValidateOnly(true)
               .setCustomClassId("customClassId1871032322")
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       CustomClass response = speechClient.createCustomClassAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCustomClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CreateCustomClassRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### createCustomClassAsync(String parent, CustomClass customClass, String customClassId)
    
    
    public final OperationFuture<CustomClass,OperationMetadata> createCustomClassAsync(String parent, CustomClass customClass, String customClassId)

Creates a CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       CustomClass customClass = CustomClass.newBuilder().build();
       String customClassId = "customClassId1871032322";
       CustomClass response =
           speechClient.createCustomClassAsync(parent, customClass, customClassId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location where this CustomClass will be created. The expected format is `projects/{project}/locations/{location}`.  
`customClass` | `[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass)`  
Required. The CustomClass to create.  
`customClassId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The ID to use for the CustomClass, which will become the final component of the CustomClass's resource name. This value should be 4-63 characters, and valid characters are /a-z-/.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### createCustomClassCallable()
    
    
    public final UnaryCallable<CreateCustomClassRequest,Operation> createCustomClassCallable()

Creates a CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       CreateCustomClassRequest request =
           CreateCustomClassRequest.newBuilder()
               .setCustomClass(CustomClass.newBuilder().build())
               .setValidateOnly(true)
               .setCustomClassId("customClassId1871032322")
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<Operation> future = speechClient.createCustomClassCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCustomClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CreateCustomClassRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createCustomClassOperationCallable()
    
    
    public final OperationCallable<CreateCustomClassRequest,CustomClass,OperationMetadata> createCustomClassOperationCallable()

Creates a CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       CreateCustomClassRequest request =
           CreateCustomClassRequest.newBuilder()
               .setCustomClass(CustomClass.newBuilder().build())
               .setValidateOnly(true)
               .setCustomClassId("customClassId1871032322")
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       OperationFuture<CustomClass, OperationMetadata> future =
           speechClient.createCustomClassOperationCallable().futureCall(request);
       // Do something.
       CustomClass response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateCustomClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CreateCustomClassRequest),[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### createPhraseSetAsync(@Nullable LocationName parent, PhraseSet phraseSet, String phraseSetId)
    
    
    public final OperationFuture<PhraseSet,OperationMetadata> createPhraseSetAsync(@Nullable LocationName parent, PhraseSet phraseSet, String phraseSetId)

Creates a PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       PhraseSet phraseSet = PhraseSet.newBuilder().build();
       String phraseSetId = "phraseSetId959902180";
       PhraseSet response = speechClient.createPhraseSetAsync(parent, phraseSet, phraseSetId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.LocationName`  
Required. The project and location where this PhraseSet will be created. The expected format is `projects/{project}/locations/{location}`.  
`phraseSet` | `[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet)`  
Required. The PhraseSet to create.  
`phraseSetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The ID to use for the PhraseSet, which will become the final component of the PhraseSet's resource name. This value should be 4-63 characters, and valid characters are /a-z-/.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### createPhraseSetAsync(CreatePhraseSetRequest request)
    
    
    public final OperationFuture<PhraseSet,OperationMetadata> createPhraseSetAsync(CreatePhraseSetRequest request)

Creates a PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       CreatePhraseSetRequest request =
           CreatePhraseSetRequest.newBuilder()
               .setPhraseSet(PhraseSet.newBuilder().build())
               .setValidateOnly(true)
               .setPhraseSetId("phraseSetId959902180")
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       PhraseSet response = speechClient.createPhraseSetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePhraseSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CreatePhraseSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### createPhraseSetAsync(String parent, PhraseSet phraseSet, String phraseSetId)
    
    
    public final OperationFuture<PhraseSet,OperationMetadata> createPhraseSetAsync(String parent, PhraseSet phraseSet, String phraseSetId)

Creates a PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       PhraseSet phraseSet = PhraseSet.newBuilder().build();
       String phraseSetId = "phraseSetId959902180";
       PhraseSet response = speechClient.createPhraseSetAsync(parent, phraseSet, phraseSetId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location where this PhraseSet will be created. The expected format is `projects/{project}/locations/{location}`.  
`phraseSet` | `[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet)`  
Required. The PhraseSet to create.  
`phraseSetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The ID to use for the PhraseSet, which will become the final component of the PhraseSet's resource name. This value should be 4-63 characters, and valid characters are /a-z-/.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### createPhraseSetCallable()
    
    
    public final UnaryCallable<CreatePhraseSetRequest,Operation> createPhraseSetCallable()

Creates a PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       CreatePhraseSetRequest request =
           CreatePhraseSetRequest.newBuilder()
               .setPhraseSet(PhraseSet.newBuilder().build())
               .setValidateOnly(true)
               .setPhraseSetId("phraseSetId959902180")
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<Operation> future = speechClient.createPhraseSetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePhraseSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CreatePhraseSetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPhraseSetOperationCallable()
    
    
    public final OperationCallable<CreatePhraseSetRequest,PhraseSet,OperationMetadata> createPhraseSetOperationCallable()

Creates a PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       CreatePhraseSetRequest request =
           CreatePhraseSetRequest.newBuilder()
               .setPhraseSet(PhraseSet.newBuilder().build())
               .setValidateOnly(true)
               .setPhraseSetId("phraseSetId959902180")
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       OperationFuture<PhraseSet, OperationMetadata> future =
           speechClient.createPhraseSetOperationCallable().futureCall(request);
       // Do something.
       PhraseSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreatePhraseSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CreatePhraseSetRequest),[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### createRecognizerAsync(@Nullable LocationName parent, Recognizer recognizer, String recognizerId)
    
    
    public final OperationFuture<Recognizer,OperationMetadata> createRecognizerAsync(@Nullable LocationName parent, Recognizer recognizer, String recognizerId)

Creates a Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Recognizer recognizer = Recognizer.newBuilder().build();
       String recognizerId = "recognizerId771963359";
       Recognizer response =
           speechClient.createRecognizerAsync(parent, recognizer, recognizerId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.LocationName`  
Required. The project and location where this Recognizer will be created. The expected format is `projects/{project}/locations/{location}`.  
`recognizer` | `[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer)`  
Required. The Recognizer to create.  
`recognizerId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The ID to use for the Recognizer, which will become the final component of the Recognizer's resource name. This value should be 4-63 characters, and valid characters are /a-z-/.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### createRecognizerAsync(CreateRecognizerRequest request)
    
    
    public final OperationFuture<Recognizer,OperationMetadata> createRecognizerAsync(CreateRecognizerRequest request)

Creates a Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       CreateRecognizerRequest request =
           CreateRecognizerRequest.newBuilder()
               .setRecognizer(Recognizer.newBuilder().build())
               .setValidateOnly(true)
               .setRecognizerId("recognizerId771963359")
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       Recognizer response = speechClient.createRecognizerAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CreateRecognizerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### createRecognizerAsync(String parent, Recognizer recognizer, String recognizerId)
    
    
    public final OperationFuture<Recognizer,OperationMetadata> createRecognizerAsync(String parent, Recognizer recognizer, String recognizerId)

Creates a Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Recognizer recognizer = Recognizer.newBuilder().build();
       String recognizerId = "recognizerId771963359";
       Recognizer response =
           speechClient.createRecognizerAsync(parent, recognizer, recognizerId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location where this Recognizer will be created. The expected format is `projects/{project}/locations/{location}`.  
`recognizer` | `[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer)`  
Required. The Recognizer to create.  
`recognizerId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The ID to use for the Recognizer, which will become the final component of the Recognizer's resource name. This value should be 4-63 characters, and valid characters are /a-z-/.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### createRecognizerCallable()
    
    
    public final UnaryCallable<CreateRecognizerRequest,Operation> createRecognizerCallable()

Creates a Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       CreateRecognizerRequest request =
           CreateRecognizerRequest.newBuilder()
               .setRecognizer(Recognizer.newBuilder().build())
               .setValidateOnly(true)
               .setRecognizerId("recognizerId771963359")
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<Operation> future = speechClient.createRecognizerCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CreateRecognizerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createRecognizerOperationCallable()
    
    
    public final OperationCallable<CreateRecognizerRequest,Recognizer,OperationMetadata> createRecognizerOperationCallable()

Creates a Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       CreateRecognizerRequest request =
           CreateRecognizerRequest.newBuilder()
               .setRecognizer(Recognizer.newBuilder().build())
               .setValidateOnly(true)
               .setRecognizerId("recognizerId771963359")
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       OperationFuture<Recognizer, OperationMetadata> future =
           speechClient.createRecognizerOperationCallable().futureCall(request);
       // Do something.
       Recognizer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CreateRecognizerRequest),[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### deleteCustomClassAsync(@Nullable CustomClassName name)
    
    
    public final OperationFuture<CustomClass,OperationMetadata> deleteCustomClassAsync(@Nullable CustomClassName name)

Deletes the CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       CustomClassName name = CustomClassName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_CLASS]");
       CustomClass response = speechClient.deleteCustomClassAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.CustomClassName`  
Required. The name of the CustomClass to delete. Format: `projects/{project}/locations/{location}/customClasses/{custom_class}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### deleteCustomClassAsync(DeleteCustomClassRequest request)
    
    
    public final OperationFuture<CustomClass,OperationMetadata> deleteCustomClassAsync(DeleteCustomClassRequest request)

Deletes the CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       DeleteCustomClassRequest request =
           DeleteCustomClassRequest.newBuilder()
               .setName(CustomClassName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_CLASS]").toString())
               .setValidateOnly(true)
               .setAllowMissing(true)
               .setEtag("etag3123477")
               .build();
       CustomClass response = speechClient.deleteCustomClassAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCustomClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.DeleteCustomClassRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### deleteCustomClassAsync(String name)
    
    
    public final OperationFuture<CustomClass,OperationMetadata> deleteCustomClassAsync(String name)

Deletes the CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String name = CustomClassName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_CLASS]").toString();
       CustomClass response = speechClient.deleteCustomClassAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the CustomClass to delete. Format: `projects/{project}/locations/{location}/customClasses/{custom_class}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### deleteCustomClassCallable()
    
    
    public final UnaryCallable<DeleteCustomClassRequest,Operation> deleteCustomClassCallable()

Deletes the CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       DeleteCustomClassRequest request =
           DeleteCustomClassRequest.newBuilder()
               .setName(CustomClassName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_CLASS]").toString())
               .setValidateOnly(true)
               .setAllowMissing(true)
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future = speechClient.deleteCustomClassCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteCustomClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.DeleteCustomClassRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteCustomClassOperationCallable()
    
    
    public final OperationCallable<DeleteCustomClassRequest,CustomClass,OperationMetadata> deleteCustomClassOperationCallable()

Deletes the CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       DeleteCustomClassRequest request =
           DeleteCustomClassRequest.newBuilder()
               .setName(CustomClassName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_CLASS]").toString())
               .setValidateOnly(true)
               .setAllowMissing(true)
               .setEtag("etag3123477")
               .build();
       OperationFuture<CustomClass, OperationMetadata> future =
           speechClient.deleteCustomClassOperationCallable().futureCall(request);
       // Do something.
       CustomClass response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteCustomClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.DeleteCustomClassRequest),[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### deletePhraseSetAsync(@Nullable PhraseSetName name)
    
    
    public final OperationFuture<PhraseSet,OperationMetadata> deletePhraseSetAsync(@Nullable PhraseSetName name)

Deletes the PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       PhraseSetName name = PhraseSetName.of("[PROJECT]", "[LOCATION]", "[PHRASE_SET]");
       PhraseSet response = speechClient.deletePhraseSetAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.PhraseSetName`  
Required. The name of the PhraseSet to delete. Format: `projects/{project}/locations/{location}/phraseSets/{phrase_set}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### deletePhraseSetAsync(DeletePhraseSetRequest request)
    
    
    public final OperationFuture<PhraseSet,OperationMetadata> deletePhraseSetAsync(DeletePhraseSetRequest request)

Deletes the PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       DeletePhraseSetRequest request =
           DeletePhraseSetRequest.newBuilder()
               .setName(PhraseSetName.of("[PROJECT]", "[LOCATION]", "[PHRASE_SET]").toString())
               .setValidateOnly(true)
               .setAllowMissing(true)
               .setEtag("etag3123477")
               .build();
       PhraseSet response = speechClient.deletePhraseSetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePhraseSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.DeletePhraseSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### deletePhraseSetAsync(String name)
    
    
    public final OperationFuture<PhraseSet,OperationMetadata> deletePhraseSetAsync(String name)

Deletes the PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String name = PhraseSetName.of("[PROJECT]", "[LOCATION]", "[PHRASE_SET]").toString();
       PhraseSet response = speechClient.deletePhraseSetAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the PhraseSet to delete. Format: `projects/{project}/locations/{location}/phraseSets/{phrase_set}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### deletePhraseSetCallable()
    
    
    public final UnaryCallable<DeletePhraseSetRequest,Operation> deletePhraseSetCallable()

Deletes the PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       DeletePhraseSetRequest request =
           DeletePhraseSetRequest.newBuilder()
               .setName(PhraseSetName.of("[PROJECT]", "[LOCATION]", "[PHRASE_SET]").toString())
               .setValidateOnly(true)
               .setAllowMissing(true)
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future = speechClient.deletePhraseSetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePhraseSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.DeletePhraseSetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePhraseSetOperationCallable()
    
    
    public final OperationCallable<DeletePhraseSetRequest,PhraseSet,OperationMetadata> deletePhraseSetOperationCallable()

Deletes the PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       DeletePhraseSetRequest request =
           DeletePhraseSetRequest.newBuilder()
               .setName(PhraseSetName.of("[PROJECT]", "[LOCATION]", "[PHRASE_SET]").toString())
               .setValidateOnly(true)
               .setAllowMissing(true)
               .setEtag("etag3123477")
               .build();
       OperationFuture<PhraseSet, OperationMetadata> future =
           speechClient.deletePhraseSetOperationCallable().futureCall(request);
       // Do something.
       PhraseSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePhraseSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.DeletePhraseSetRequest),[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### deleteRecognizerAsync(@Nullable RecognizerName name)
    
    
    public final OperationFuture<Recognizer,OperationMetadata> deleteRecognizerAsync(@Nullable RecognizerName name)

Deletes the Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       RecognizerName name = RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]");
       Recognizer response = speechClient.deleteRecognizerAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.RecognizerName`  
Required. The name of the Recognizer to delete. Format: `projects/{project}/locations/{location}/recognizers/{recognizer}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### deleteRecognizerAsync(DeleteRecognizerRequest request)
    
    
    public final OperationFuture<Recognizer,OperationMetadata> deleteRecognizerAsync(DeleteRecognizerRequest request)

Deletes the Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       DeleteRecognizerRequest request =
           DeleteRecognizerRequest.newBuilder()
               .setName(RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString())
               .setValidateOnly(true)
               .setAllowMissing(true)
               .setEtag("etag3123477")
               .build();
       Recognizer response = speechClient.deleteRecognizerAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.DeleteRecognizerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### deleteRecognizerAsync(String name)
    
    
    public final OperationFuture<Recognizer,OperationMetadata> deleteRecognizerAsync(String name)

Deletes the Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String name = RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString();
       Recognizer response = speechClient.deleteRecognizerAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Recognizer to delete. Format: `projects/{project}/locations/{location}/recognizers/{recognizer}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### deleteRecognizerCallable()
    
    
    public final UnaryCallable<DeleteRecognizerRequest,Operation> deleteRecognizerCallable()

Deletes the Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       DeleteRecognizerRequest request =
           DeleteRecognizerRequest.newBuilder()
               .setName(RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString())
               .setValidateOnly(true)
               .setAllowMissing(true)
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future = speechClient.deleteRecognizerCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.DeleteRecognizerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteRecognizerOperationCallable()
    
    
    public final OperationCallable<DeleteRecognizerRequest,Recognizer,OperationMetadata> deleteRecognizerOperationCallable()

Deletes the Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       DeleteRecognizerRequest request =
           DeleteRecognizerRequest.newBuilder()
               .setName(RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString())
               .setValidateOnly(true)
               .setAllowMissing(true)
               .setEtag("etag3123477")
               .build();
       OperationFuture<Recognizer, OperationMetadata> future =
           speechClient.deleteRecognizerOperationCallable().futureCall(request);
       // Do something.
       Recognizer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.DeleteRecognizerRequest),[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### getConfig(@Nullable ConfigName name)
    
    
    public final Config getConfig(@Nullable ConfigName name)

Returns the requested Config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       ConfigName name = ConfigName.of("[PROJECT]", "[LOCATION]");
       Config response = speechClient.getConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.ConfigName`  
Required. The name of the config to retrieve. There is exactly one config resource per project per location. The expected format is `projects/{project}/locations/{location}/config`.  
**Returns**  
---  
**Type** | **Description**  
`[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Config)` |   
  
### getConfig(GetConfigRequest request)
    
    
    public final Config getConfig(GetConfigRequest request)

Returns the requested Config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       GetConfigRequest request =
           GetConfigRequest.newBuilder()
               .setName(ConfigName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       Config response = speechClient.getConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.GetConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Config)` |   
  
### getConfig(String name)
    
    
    public final Config getConfig(String name)

Returns the requested Config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String name = ConfigName.of("[PROJECT]", "[LOCATION]").toString();
       Config response = speechClient.getConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the config to retrieve. There is exactly one config resource per project per location. The expected format is `projects/{project}/locations/{location}/config`.  
**Returns**  
---  
**Type** | **Description**  
`[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Config)` |   
  
### getConfigCallable()
    
    
    public final UnaryCallable<GetConfigRequest,Config> getConfigCallable()

Returns the requested Config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       GetConfigRequest request =
           GetConfigRequest.newBuilder()
               .setName(ConfigName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<Config> future = speechClient.getConfigCallable().futureCall(request);
       // Do something.
       Config response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.GetConfigRequest),[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Config)>` |   
  
### getCustomClass(@Nullable CustomClassName name)
    
    
    public final CustomClass getCustomClass(@Nullable CustomClassName name)

Returns the requested CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       CustomClassName name = CustomClassName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_CLASS]");
       CustomClass response = speechClient.getCustomClass(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.CustomClassName`  
Required. The name of the CustomClass to retrieve. The expected format is `projects/{project}/locations/{location}/customClasses/{custom_class}`.  
**Returns**  
---  
**Type** | **Description**  
`[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass)` |   
  
### getCustomClass(GetCustomClassRequest request)
    
    
    public final CustomClass getCustomClass(GetCustomClassRequest request)

Returns the requested CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       GetCustomClassRequest request =
           GetCustomClassRequest.newBuilder()
               .setName(CustomClassName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_CLASS]").toString())
               .build();
       CustomClass response = speechClient.getCustomClass(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCustomClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.GetCustomClassRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass)` |   
  
### getCustomClass(String name)
    
    
    public final CustomClass getCustomClass(String name)

Returns the requested CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String name = CustomClassName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_CLASS]").toString();
       CustomClass response = speechClient.getCustomClass(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the CustomClass to retrieve. The expected format is `projects/{project}/locations/{location}/customClasses/{custom_class}`.  
**Returns**  
---  
**Type** | **Description**  
`[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass)` |   
  
### getCustomClassCallable()
    
    
    public final UnaryCallable<GetCustomClassRequest,CustomClass> getCustomClassCallable()

Returns the requested CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       GetCustomClassRequest request =
           GetCustomClassRequest.newBuilder()
               .setName(CustomClassName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_CLASS]").toString())
               .build();
       ApiFuture<CustomClass> future = speechClient.getCustomClassCallable().futureCall(request);
       // Do something.
       CustomClass response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCustomClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.GetCustomClassRequest),[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass)>` |   
  
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
     try (SpeechClient speechClient = SpeechClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = speechClient.getLocation(request);
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
     try (SpeechClient speechClient = SpeechClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = speechClient.getLocationCallable().futureCall(request);
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
  
### getPhraseSet(@Nullable PhraseSetName name)
    
    
    public final PhraseSet getPhraseSet(@Nullable PhraseSetName name)

Returns the requested PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       PhraseSetName name = PhraseSetName.of("[PROJECT]", "[LOCATION]", "[PHRASE_SET]");
       PhraseSet response = speechClient.getPhraseSet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.PhraseSetName`  
Required. The name of the PhraseSet to retrieve. The expected format is `projects/{project}/locations/{location}/phraseSets/{phrase_set}`.  
**Returns**  
---  
**Type** | **Description**  
`[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet)` |   
  
### getPhraseSet(GetPhraseSetRequest request)
    
    
    public final PhraseSet getPhraseSet(GetPhraseSetRequest request)

Returns the requested PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       GetPhraseSetRequest request =
           GetPhraseSetRequest.newBuilder()
               .setName(PhraseSetName.of("[PROJECT]", "[LOCATION]", "[PHRASE_SET]").toString())
               .build();
       PhraseSet response = speechClient.getPhraseSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPhraseSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.GetPhraseSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet)` |   
  
### getPhraseSet(String name)
    
    
    public final PhraseSet getPhraseSet(String name)

Returns the requested PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String name = PhraseSetName.of("[PROJECT]", "[LOCATION]", "[PHRASE_SET]").toString();
       PhraseSet response = speechClient.getPhraseSet(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the PhraseSet to retrieve. The expected format is `projects/{project}/locations/{location}/phraseSets/{phrase_set}`.  
**Returns**  
---  
**Type** | **Description**  
`[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet)` |   
  
### getPhraseSetCallable()
    
    
    public final UnaryCallable<GetPhraseSetRequest,PhraseSet> getPhraseSetCallable()

Returns the requested PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       GetPhraseSetRequest request =
           GetPhraseSetRequest.newBuilder()
               .setName(PhraseSetName.of("[PROJECT]", "[LOCATION]", "[PHRASE_SET]").toString())
               .build();
       ApiFuture<PhraseSet> future = speechClient.getPhraseSetCallable().futureCall(request);
       // Do something.
       PhraseSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPhraseSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.GetPhraseSetRequest),[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet)>` |   
  
### getRecognizer(@Nullable RecognizerName name)
    
    
    public final Recognizer getRecognizer(@Nullable RecognizerName name)

Returns the requested Recognizer. Fails with NOT_FOUND if the requested Recognizer doesn't exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       RecognizerName name = RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]");
       Recognizer response = speechClient.getRecognizer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.RecognizerName`  
Required. The name of the Recognizer to retrieve. The expected format is `projects/{project}/locations/{location}/recognizers/{recognizer}`.  
**Returns**  
---  
**Type** | **Description**  
`[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer)` |   
  
### getRecognizer(GetRecognizerRequest request)
    
    
    public final Recognizer getRecognizer(GetRecognizerRequest request)

Returns the requested Recognizer. Fails with NOT_FOUND if the requested Recognizer doesn't exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       GetRecognizerRequest request =
           GetRecognizerRequest.newBuilder()
               .setName(RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString())
               .build();
       Recognizer response = speechClient.getRecognizer(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.GetRecognizerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer)` |   
  
### getRecognizer(String name)
    
    
    public final Recognizer getRecognizer(String name)

Returns the requested Recognizer. Fails with NOT_FOUND if the requested Recognizer doesn't exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String name = RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString();
       Recognizer response = speechClient.getRecognizer(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Recognizer to retrieve. The expected format is `projects/{project}/locations/{location}/recognizers/{recognizer}`.  
**Returns**  
---  
**Type** | **Description**  
`[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer)` |   
  
### getRecognizerCallable()
    
    
    public final UnaryCallable<GetRecognizerRequest,Recognizer> getRecognizerCallable()

Returns the requested Recognizer. Fails with NOT_FOUND if the requested Recognizer doesn't exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       GetRecognizerRequest request =
           GetRecognizerRequest.newBuilder()
               .setName(RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString())
               .build();
       ApiFuture<Recognizer> future = speechClient.getRecognizerCallable().futureCall(request);
       // Do something.
       Recognizer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.GetRecognizerRequest),[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer)>` |   
  
### getSettings()
    
    
    public final @Nullable SpeechSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.SpeechSettings` |   
  
### getStub()
    
    
    public SpeechStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SpeechStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.stub.SpeechStub)` |   
  
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
  
### listCustomClasses(@Nullable LocationName parent)
    
    
    public final SpeechClient.ListCustomClassesPagedResponse listCustomClasses(@Nullable LocationName parent)

Lists CustomClasses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (CustomClass element : speechClient.listCustomClasses(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.LocationName`  
Required. The project and location of CustomClass resources to list. The expected format is `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[SpeechClient.ListCustomClassesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.ListCustomClassesPagedResponse)` |   
  
### listCustomClasses(ListCustomClassesRequest request)
    
    
    public final SpeechClient.ListCustomClassesPagedResponse listCustomClasses(ListCustomClassesRequest request)

Lists CustomClasses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       ListCustomClassesRequest request =
           ListCustomClassesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setShowDeleted(true)
               .build();
       for (CustomClass element : speechClient.listCustomClasses(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCustomClassesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.ListCustomClassesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SpeechClient.ListCustomClassesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.ListCustomClassesPagedResponse)` |   
  
### listCustomClasses(String parent)
    
    
    public final SpeechClient.ListCustomClassesPagedResponse listCustomClasses(String parent)

Lists CustomClasses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (CustomClass element : speechClient.listCustomClasses(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location of CustomClass resources to list. The expected format is `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[SpeechClient.ListCustomClassesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.ListCustomClassesPagedResponse)` |   
  
### listCustomClassesCallable()
    
    
    public final UnaryCallable<ListCustomClassesRequest,ListCustomClassesResponse> listCustomClassesCallable()

Lists CustomClasses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       ListCustomClassesRequest request =
           ListCustomClassesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setShowDeleted(true)
               .build();
       while (true) {
         ListCustomClassesResponse response = speechClient.listCustomClassesCallable().call(request);
         for (CustomClass element : response.getCustomClassesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomClassesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.ListCustomClassesRequest),[ListCustomClassesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.ListCustomClassesResponse)>` |   
  
### listCustomClassesPagedCallable()
    
    
    public final UnaryCallable<ListCustomClassesRequest,SpeechClient.ListCustomClassesPagedResponse> listCustomClassesPagedCallable()

Lists CustomClasses.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       ListCustomClassesRequest request =
           ListCustomClassesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setShowDeleted(true)
               .build();
       ApiFuture<CustomClass> future =
           speechClient.listCustomClassesPagedCallable().futureCall(request);
       // Do something.
       for (CustomClass element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomClassesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.ListCustomClassesRequest),[ListCustomClassesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.ListCustomClassesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final SpeechClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.This method can be called in two ways:

* **List all public locations:** Use the path `GET /v1/locations`.* **List project-visible locations:** Use the path`GET /v1/projects/{project_id}/locations`. This may include publiclocations as well as private or other locations specifically visibleto the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : speechClient.listLocations(request).iterateAll()) {
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
`[SpeechClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.This method can be called in two ways:

* **List all public locations:** Use the path `GET /v1/locations`.* **List project-visible locations:** Use the path`GET /v1/projects/{project_id}/locations`. This may include publiclocations as well as private or other locations specifically visibleto the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = speechClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,SpeechClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.This method can be called in two ways:

* **List all public locations:** Use the path `GET /v1/locations`.* **List project-visible locations:** Use the path`GET /v1/projects/{project_id}/locations`. This may include publiclocations as well as private or other locations specifically visibleto the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future = speechClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.ListLocationsPagedResponse)>` |   
  
### listPhraseSets(@Nullable LocationName parent)
    
    
    public final SpeechClient.ListPhraseSetsPagedResponse listPhraseSets(@Nullable LocationName parent)

Lists PhraseSets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (PhraseSet element : speechClient.listPhraseSets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.LocationName`  
Required. The project and location of PhraseSet resources to list. The expected format is `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[SpeechClient.ListPhraseSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.ListPhraseSetsPagedResponse)` |   
  
### listPhraseSets(ListPhraseSetsRequest request)
    
    
    public final SpeechClient.ListPhraseSetsPagedResponse listPhraseSets(ListPhraseSetsRequest request)

Lists PhraseSets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       ListPhraseSetsRequest request =
           ListPhraseSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setShowDeleted(true)
               .build();
       for (PhraseSet element : speechClient.listPhraseSets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPhraseSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.ListPhraseSetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SpeechClient.ListPhraseSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.ListPhraseSetsPagedResponse)` |   
  
### listPhraseSets(String parent)
    
    
    public final SpeechClient.ListPhraseSetsPagedResponse listPhraseSets(String parent)

Lists PhraseSets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (PhraseSet element : speechClient.listPhraseSets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location of PhraseSet resources to list. The expected format is `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[SpeechClient.ListPhraseSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.ListPhraseSetsPagedResponse)` |   
  
### listPhraseSetsCallable()
    
    
    public final UnaryCallable<ListPhraseSetsRequest,ListPhraseSetsResponse> listPhraseSetsCallable()

Lists PhraseSets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       ListPhraseSetsRequest request =
           ListPhraseSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setShowDeleted(true)
               .build();
       while (true) {
         ListPhraseSetsResponse response = speechClient.listPhraseSetsCallable().call(request);
         for (PhraseSet element : response.getPhraseSetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPhraseSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.ListPhraseSetsRequest),[ListPhraseSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.ListPhraseSetsResponse)>` |   
  
### listPhraseSetsPagedCallable()
    
    
    public final UnaryCallable<ListPhraseSetsRequest,SpeechClient.ListPhraseSetsPagedResponse> listPhraseSetsPagedCallable()

Lists PhraseSets.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       ListPhraseSetsRequest request =
           ListPhraseSetsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setShowDeleted(true)
               .build();
       ApiFuture<PhraseSet> future = speechClient.listPhraseSetsPagedCallable().futureCall(request);
       // Do something.
       for (PhraseSet element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPhraseSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.ListPhraseSetsRequest),[ListPhraseSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.ListPhraseSetsPagedResponse)>` |   
  
### listRecognizers(@Nullable LocationName parent)
    
    
    public final SpeechClient.ListRecognizersPagedResponse listRecognizers(@Nullable LocationName parent)

Lists Recognizers.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Recognizer element : speechClient.listRecognizers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.LocationName`  
Required. The project and location of Recognizers to list. The expected format is `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[SpeechClient.ListRecognizersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.ListRecognizersPagedResponse)` |   
  
### listRecognizers(ListRecognizersRequest request)
    
    
    public final SpeechClient.ListRecognizersPagedResponse listRecognizers(ListRecognizersRequest request)

Lists Recognizers.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       ListRecognizersRequest request =
           ListRecognizersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setShowDeleted(true)
               .build();
       for (Recognizer element : speechClient.listRecognizers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRecognizersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.ListRecognizersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SpeechClient.ListRecognizersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.ListRecognizersPagedResponse)` |   
  
### listRecognizers(String parent)
    
    
    public final SpeechClient.ListRecognizersPagedResponse listRecognizers(String parent)

Lists Recognizers.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Recognizer element : speechClient.listRecognizers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location of Recognizers to list. The expected format is `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[SpeechClient.ListRecognizersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.ListRecognizersPagedResponse)` |   
  
### listRecognizersCallable()
    
    
    public final UnaryCallable<ListRecognizersRequest,ListRecognizersResponse> listRecognizersCallable()

Lists Recognizers.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       ListRecognizersRequest request =
           ListRecognizersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setShowDeleted(true)
               .build();
       while (true) {
         ListRecognizersResponse response = speechClient.listRecognizersCallable().call(request);
         for (Recognizer element : response.getRecognizersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRecognizersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.ListRecognizersRequest),[ListRecognizersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.ListRecognizersResponse)>` |   
  
### listRecognizersPagedCallable()
    
    
    public final UnaryCallable<ListRecognizersRequest,SpeechClient.ListRecognizersPagedResponse> listRecognizersPagedCallable()

Lists Recognizers.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       ListRecognizersRequest request =
           ListRecognizersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setShowDeleted(true)
               .build();
       ApiFuture<Recognizer> future =
           speechClient.listRecognizersPagedCallable().futureCall(request);
       // Do something.
       for (Recognizer element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRecognizersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.ListRecognizersRequest),[ListRecognizersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.SpeechClient.ListRecognizersPagedResponse)>` |   
  
### recognize(@Nullable RecognizerName recognizer, RecognitionConfig config, FieldMask configMask, ByteString content)
    
    
    public final RecognizeResponse recognize(@Nullable RecognizerName recognizer, RecognitionConfig config, FieldMask configMask, ByteString content)

Performs synchronous Speech recognition: receive results after all audio has been sent and processed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       RecognizerName recognizer = RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]");
       RecognitionConfig config = RecognitionConfig.newBuilder().build();
       FieldMask configMask = FieldMask.newBuilder().build();
       ByteString content = ByteString.EMPTY;
       RecognizeResponse response = speechClient.recognize(recognizer, config, configMask, content);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`recognizer` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.RecognizerName`  
Required. The name of the Recognizer to use during recognition. The expected format is `projects/{project}/locations/{location}/recognizers/{recognizer}`. The {recognizer} segment may be set to `_` to use an empty implicit Recognizer.  
`config` | `[RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognitionConfig)`  
Features and audio metadata to use for the Automatic Speech Recognition. This field in combination with the config_mask field can be used to override parts of the default_recognition_config of the Recognizer resource.  
`configMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields in config that override the values in the default_recognition_config of the recognizer during this recognition request. If no mask is provided, all non-default valued fields in config override the values in the recognizer for this recognition request. If a mask is provided, only the fields listed in the mask override the config in the recognizer for this recognition request. If a wildcard (`*`) is provided, config completely overrides and replaces the config in the recognizer for this recognition request.  
`content` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The audio data bytes encoded as specified in RecognitionConfig. As with all bytes fields, proto buffers use a pure binary representation, whereas JSON representations use base64.  
**Returns**  
---  
**Type** | **Description**  
`[RecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognizeResponse)` |   
  
### recognize(@Nullable RecognizerName recognizer, RecognitionConfig config, FieldMask configMask, String uri)
    
    
    public final RecognizeResponse recognize(@Nullable RecognizerName recognizer, RecognitionConfig config, FieldMask configMask, String uri)

Performs synchronous Speech recognition: receive results after all audio has been sent and processed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       RecognizerName recognizer = RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]");
       RecognitionConfig config = RecognitionConfig.newBuilder().build();
       FieldMask configMask = FieldMask.newBuilder().build();
       String uri = "uri116076";
       RecognizeResponse response = speechClient.recognize(recognizer, config, configMask, uri);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`recognizer` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.RecognizerName`  
Required. The name of the Recognizer to use during recognition. The expected format is `projects/{project}/locations/{location}/recognizers/{recognizer}`. The {recognizer} segment may be set to `_` to use an empty implicit Recognizer.  
`config` | `[RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognitionConfig)`  
Features and audio metadata to use for the Automatic Speech Recognition. This field in combination with the config_mask field can be used to override parts of the default_recognition_config of the Recognizer resource.  
`configMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields in config that override the values in the default_recognition_config of the recognizer during this recognition request. If no mask is provided, all non-default valued fields in config override the values in the recognizer for this recognition request. If a mask is provided, only the fields listed in the mask override the config in the recognizer for this recognition request. If a wildcard (`*`) is provided, config completely overrides and replaces the config in the recognizer for this recognition request.  
`uri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
URI that points to a file that contains audio data bytes as specified in RecognitionConfig. The file must not be compressed (for example, gzip). Currently, only Google Cloud Storage URIs are supported, which must be specified in the following format: `gs://bucket_name/object_name` (other URI formats return INVALID_ARGUMENT). For more information, see [Request URIs](https://cloud.google.com/storage/docs/reference-uris).  
**Returns**  
---  
**Type** | **Description**  
`[RecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognizeResponse)` |   
  
### recognize(RecognizeRequest request)
    
    
    public final RecognizeResponse recognize(RecognizeRequest request)

Performs synchronous Speech recognition: receive results after all audio has been sent and processed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       RecognizeRequest request =
           RecognizeRequest.newBuilder()
               .setRecognizer(
                   RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString())
               .setConfig(RecognitionConfig.newBuilder().build())
               .setConfigMask(FieldMask.newBuilder().build())
               .build();
       RecognizeResponse response = speechClient.recognize(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RecognizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognizeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognizeResponse)` |   
  
### recognize(String recognizer, RecognitionConfig config, FieldMask configMask, ByteString content)
    
    
    public final RecognizeResponse recognize(String recognizer, RecognitionConfig config, FieldMask configMask, ByteString content)

Performs synchronous Speech recognition: receive results after all audio has been sent and processed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String recognizer = RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString();
       RecognitionConfig config = RecognitionConfig.newBuilder().build();
       FieldMask configMask = FieldMask.newBuilder().build();
       ByteString content = ByteString.EMPTY;
       RecognizeResponse response = speechClient.recognize(recognizer, config, configMask, content);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`recognizer` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Recognizer to use during recognition. The expected format is `projects/{project}/locations/{location}/recognizers/{recognizer}`. The {recognizer} segment may be set to `_` to use an empty implicit Recognizer.  
`config` | `[RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognitionConfig)`  
Features and audio metadata to use for the Automatic Speech Recognition. This field in combination with the config_mask field can be used to override parts of the default_recognition_config of the Recognizer resource.  
`configMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields in config that override the values in the default_recognition_config of the recognizer during this recognition request. If no mask is provided, all non-default valued fields in config override the values in the recognizer for this recognition request. If a mask is provided, only the fields listed in the mask override the config in the recognizer for this recognition request. If a wildcard (`*`) is provided, config completely overrides and replaces the config in the recognizer for this recognition request.  
`content` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The audio data bytes encoded as specified in RecognitionConfig. As with all bytes fields, proto buffers use a pure binary representation, whereas JSON representations use base64.  
**Returns**  
---  
**Type** | **Description**  
`[RecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognizeResponse)` |   
  
### recognize(String recognizer, RecognitionConfig config, FieldMask configMask, String uri)
    
    
    public final RecognizeResponse recognize(String recognizer, RecognitionConfig config, FieldMask configMask, String uri)

Performs synchronous Speech recognition: receive results after all audio has been sent and processed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String recognizer = RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString();
       RecognitionConfig config = RecognitionConfig.newBuilder().build();
       FieldMask configMask = FieldMask.newBuilder().build();
       String uri = "uri116076";
       RecognizeResponse response = speechClient.recognize(recognizer, config, configMask, uri);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`recognizer` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Recognizer to use during recognition. The expected format is `projects/{project}/locations/{location}/recognizers/{recognizer}`. The {recognizer} segment may be set to `_` to use an empty implicit Recognizer.  
`config` | `[RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognitionConfig)`  
Features and audio metadata to use for the Automatic Speech Recognition. This field in combination with the config_mask field can be used to override parts of the default_recognition_config of the Recognizer resource.  
`configMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields in config that override the values in the default_recognition_config of the recognizer during this recognition request. If no mask is provided, all non-default valued fields in config override the values in the recognizer for this recognition request. If a mask is provided, only the fields listed in the mask override the config in the recognizer for this recognition request. If a wildcard (`*`) is provided, config completely overrides and replaces the config in the recognizer for this recognition request.  
`uri` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
URI that points to a file that contains audio data bytes as specified in RecognitionConfig. The file must not be compressed (for example, gzip). Currently, only Google Cloud Storage URIs are supported, which must be specified in the following format: `gs://bucket_name/object_name` (other URI formats return INVALID_ARGUMENT). For more information, see [Request URIs](https://cloud.google.com/storage/docs/reference-uris).  
**Returns**  
---  
**Type** | **Description**  
`[RecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognizeResponse)` |   
  
### recognizeCallable()
    
    
    public final UnaryCallable<RecognizeRequest,RecognizeResponse> recognizeCallable()

Performs synchronous Speech recognition: receive results after all audio has been sent and processed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       RecognizeRequest request =
           RecognizeRequest.newBuilder()
               .setRecognizer(
                   RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString())
               .setConfig(RecognitionConfig.newBuilder().build())
               .setConfigMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<RecognizeResponse> future = speechClient.recognizeCallable().futureCall(request);
       // Do something.
       RecognizeResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RecognizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognizeRequest),[RecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.RecognizeResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### streamingRecognizeCallable()
    
    
    public final BidiStreamingCallable<StreamingRecognizeRequest,StreamingRecognizeResponse> streamingRecognizeCallable()

Performs bidirectional streaming speech recognition: receive results while sending audio. This method is only available via the gRPC API (not REST).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       BidiStream<StreamingRecognizeRequest, StreamingRecognizeResponse> bidiStream =
           speechClient.streamingRecognizeCallable().call();
       StreamingRecognizeRequest request =
           StreamingRecognizeRequest.newBuilder()
               .setRecognizer(
                   RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString())
               .build();
       bidiStream.send(request);
       for (StreamingRecognizeResponse response : bidiStream) {
         // Do something when a response is received.
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[BidiStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable.html)<[StreamingRecognizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.StreamingRecognizeRequest),[StreamingRecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.StreamingRecognizeResponse)>` |   
  
### undeleteCustomClassAsync(@Nullable CustomClassName name)
    
    
    public final OperationFuture<CustomClass,OperationMetadata> undeleteCustomClassAsync(@Nullable CustomClassName name)

Undeletes the CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       CustomClassName name = CustomClassName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_CLASS]");
       CustomClass response = speechClient.undeleteCustomClassAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.CustomClassName`  
Required. The name of the CustomClass to undelete. Format: `projects/{project}/locations/{location}/customClasses/{custom_class}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### undeleteCustomClassAsync(UndeleteCustomClassRequest request)
    
    
    public final OperationFuture<CustomClass,OperationMetadata> undeleteCustomClassAsync(UndeleteCustomClassRequest request)

Undeletes the CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UndeleteCustomClassRequest request =
           UndeleteCustomClassRequest.newBuilder()
               .setName(CustomClassName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_CLASS]").toString())
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       CustomClass response = speechClient.undeleteCustomClassAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UndeleteCustomClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UndeleteCustomClassRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### undeleteCustomClassAsync(String name)
    
    
    public final OperationFuture<CustomClass,OperationMetadata> undeleteCustomClassAsync(String name)

Undeletes the CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String name = CustomClassName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_CLASS]").toString();
       CustomClass response = speechClient.undeleteCustomClassAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the CustomClass to undelete. Format: `projects/{project}/locations/{location}/customClasses/{custom_class}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### undeleteCustomClassCallable()
    
    
    public final UnaryCallable<UndeleteCustomClassRequest,Operation> undeleteCustomClassCallable()

Undeletes the CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UndeleteCustomClassRequest request =
           UndeleteCustomClassRequest.newBuilder()
               .setName(CustomClassName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_CLASS]").toString())
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future = speechClient.undeleteCustomClassCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UndeleteCustomClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UndeleteCustomClassRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### undeleteCustomClassOperationCallable()
    
    
    public final OperationCallable<UndeleteCustomClassRequest,CustomClass,OperationMetadata> undeleteCustomClassOperationCallable()

Undeletes the CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UndeleteCustomClassRequest request =
           UndeleteCustomClassRequest.newBuilder()
               .setName(CustomClassName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_CLASS]").toString())
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       OperationFuture<CustomClass, OperationMetadata> future =
           speechClient.undeleteCustomClassOperationCallable().futureCall(request);
       // Do something.
       CustomClass response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UndeleteCustomClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UndeleteCustomClassRequest),[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### undeletePhraseSetAsync(@Nullable PhraseSetName name)
    
    
    public final OperationFuture<PhraseSet,OperationMetadata> undeletePhraseSetAsync(@Nullable PhraseSetName name)

Undeletes the PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       PhraseSetName name = PhraseSetName.of("[PROJECT]", "[LOCATION]", "[PHRASE_SET]");
       PhraseSet response = speechClient.undeletePhraseSetAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.PhraseSetName`  
Required. The name of the PhraseSet to undelete. Format: `projects/{project}/locations/{location}/phraseSets/{phrase_set}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### undeletePhraseSetAsync(UndeletePhraseSetRequest request)
    
    
    public final OperationFuture<PhraseSet,OperationMetadata> undeletePhraseSetAsync(UndeletePhraseSetRequest request)

Undeletes the PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UndeletePhraseSetRequest request =
           UndeletePhraseSetRequest.newBuilder()
               .setName(PhraseSetName.of("[PROJECT]", "[LOCATION]", "[PHRASE_SET]").toString())
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       PhraseSet response = speechClient.undeletePhraseSetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UndeletePhraseSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UndeletePhraseSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### undeletePhraseSetAsync(String name)
    
    
    public final OperationFuture<PhraseSet,OperationMetadata> undeletePhraseSetAsync(String name)

Undeletes the PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String name = PhraseSetName.of("[PROJECT]", "[LOCATION]", "[PHRASE_SET]").toString();
       PhraseSet response = speechClient.undeletePhraseSetAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the PhraseSet to undelete. Format: `projects/{project}/locations/{location}/phraseSets/{phrase_set}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### undeletePhraseSetCallable()
    
    
    public final UnaryCallable<UndeletePhraseSetRequest,Operation> undeletePhraseSetCallable()

Undeletes the PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UndeletePhraseSetRequest request =
           UndeletePhraseSetRequest.newBuilder()
               .setName(PhraseSetName.of("[PROJECT]", "[LOCATION]", "[PHRASE_SET]").toString())
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future = speechClient.undeletePhraseSetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UndeletePhraseSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UndeletePhraseSetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### undeletePhraseSetOperationCallable()
    
    
    public final OperationCallable<UndeletePhraseSetRequest,PhraseSet,OperationMetadata> undeletePhraseSetOperationCallable()

Undeletes the PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UndeletePhraseSetRequest request =
           UndeletePhraseSetRequest.newBuilder()
               .setName(PhraseSetName.of("[PROJECT]", "[LOCATION]", "[PHRASE_SET]").toString())
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       OperationFuture<PhraseSet, OperationMetadata> future =
           speechClient.undeletePhraseSetOperationCallable().futureCall(request);
       // Do something.
       PhraseSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UndeletePhraseSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UndeletePhraseSetRequest),[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### undeleteRecognizerAsync(@Nullable RecognizerName name)
    
    
    public final OperationFuture<Recognizer,OperationMetadata> undeleteRecognizerAsync(@Nullable RecognizerName name)

Undeletes the Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       RecognizerName name = RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]");
       Recognizer response = speechClient.undeleteRecognizerAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.speech.v2.RecognizerName`  
Required. The name of the Recognizer to undelete. Format: `projects/{project}/locations/{location}/recognizers/{recognizer}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### undeleteRecognizerAsync(UndeleteRecognizerRequest request)
    
    
    public final OperationFuture<Recognizer,OperationMetadata> undeleteRecognizerAsync(UndeleteRecognizerRequest request)

Undeletes the Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UndeleteRecognizerRequest request =
           UndeleteRecognizerRequest.newBuilder()
               .setName(RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString())
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       Recognizer response = speechClient.undeleteRecognizerAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UndeleteRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UndeleteRecognizerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### undeleteRecognizerAsync(String name)
    
    
    public final OperationFuture<Recognizer,OperationMetadata> undeleteRecognizerAsync(String name)

Undeletes the Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       String name = RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString();
       Recognizer response = speechClient.undeleteRecognizerAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Recognizer to undelete. Format: `projects/{project}/locations/{location}/recognizers/{recognizer}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### undeleteRecognizerCallable()
    
    
    public final UnaryCallable<UndeleteRecognizerRequest,Operation> undeleteRecognizerCallable()

Undeletes the Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UndeleteRecognizerRequest request =
           UndeleteRecognizerRequest.newBuilder()
               .setName(RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString())
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future = speechClient.undeleteRecognizerCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UndeleteRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UndeleteRecognizerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### undeleteRecognizerOperationCallable()
    
    
    public final OperationCallable<UndeleteRecognizerRequest,Recognizer,OperationMetadata> undeleteRecognizerOperationCallable()

Undeletes the Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UndeleteRecognizerRequest request =
           UndeleteRecognizerRequest.newBuilder()
               .setName(RecognizerName.of("[PROJECT]", "[LOCATION]", "[RECOGNIZER]").toString())
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       OperationFuture<Recognizer, OperationMetadata> future =
           speechClient.undeleteRecognizerOperationCallable().futureCall(request);
       // Do something.
       Recognizer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UndeleteRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UndeleteRecognizerRequest),[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### updateConfig(Config config, FieldMask updateMask)
    
    
    public final Config updateConfig(Config config, FieldMask updateMask)

Updates the Config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       Config config = Config.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Config response = speechClient.updateConfig(config, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`config` | `[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Config)`  
Required. The config to update. The config's `name` field is used to identify the config to be updated. The expected format is `projects/{project}/locations/{location}/config`.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields to be updated.  
**Returns**  
---  
**Type** | **Description**  
`[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Config)` |   
  
### updateConfig(UpdateConfigRequest request)
    
    
    public final Config updateConfig(UpdateConfigRequest request)

Updates the Config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UpdateConfigRequest request =
           UpdateConfigRequest.newBuilder()
               .setConfig(Config.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Config response = speechClient.updateConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UpdateConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Config)` |   
  
### updateConfigCallable()
    
    
    public final UnaryCallable<UpdateConfigRequest,Config> updateConfigCallable()

Updates the Config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UpdateConfigRequest request =
           UpdateConfigRequest.newBuilder()
               .setConfig(Config.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Config> future = speechClient.updateConfigCallable().futureCall(request);
       // Do something.
       Config response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UpdateConfigRequest),[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Config)>` |   
  
### updateCustomClassAsync(CustomClass customClass, FieldMask updateMask)
    
    
    public final OperationFuture<CustomClass,OperationMetadata> updateCustomClassAsync(CustomClass customClass, FieldMask updateMask)

Updates the CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       CustomClass customClass = CustomClass.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       CustomClass response = speechClient.updateCustomClassAsync(customClass, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`customClass` | `[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass)`  
Required. The CustomClass to update. The CustomClass's `name` field is used to identify the CustomClass to update. Format: `projects/{project}/locations/{location}/customClasses/{custom_class}`.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields to be updated. If empty, all fields are considered for update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### updateCustomClassAsync(UpdateCustomClassRequest request)
    
    
    public final OperationFuture<CustomClass,OperationMetadata> updateCustomClassAsync(UpdateCustomClassRequest request)

Updates the CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UpdateCustomClassRequest request =
           UpdateCustomClassRequest.newBuilder()
               .setCustomClass(CustomClass.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       CustomClass response = speechClient.updateCustomClassAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCustomClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UpdateCustomClassRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### updateCustomClassCallable()
    
    
    public final UnaryCallable<UpdateCustomClassRequest,Operation> updateCustomClassCallable()

Updates the CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UpdateCustomClassRequest request =
           UpdateCustomClassRequest.newBuilder()
               .setCustomClass(CustomClass.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = speechClient.updateCustomClassCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCustomClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UpdateCustomClassRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateCustomClassOperationCallable()
    
    
    public final OperationCallable<UpdateCustomClassRequest,CustomClass,OperationMetadata> updateCustomClassOperationCallable()

Updates the CustomClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UpdateCustomClassRequest request =
           UpdateCustomClassRequest.newBuilder()
               .setCustomClass(CustomClass.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<CustomClass, OperationMetadata> future =
           speechClient.updateCustomClassOperationCallable().futureCall(request);
       // Do something.
       CustomClass response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateCustomClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UpdateCustomClassRequest),[CustomClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.CustomClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### updatePhraseSetAsync(PhraseSet phraseSet, FieldMask updateMask)
    
    
    public final OperationFuture<PhraseSet,OperationMetadata> updatePhraseSetAsync(PhraseSet phraseSet, FieldMask updateMask)

Updates the PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       PhraseSet phraseSet = PhraseSet.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       PhraseSet response = speechClient.updatePhraseSetAsync(phraseSet, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`phraseSet` | `[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet)`  
Required. The PhraseSet to update. The PhraseSet's `name` field is used to identify the PhraseSet to update. Format: `projects/{project}/locations/{location}/phraseSets/{phrase_set}`.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields to update. If empty, all non-default valued fields are considered for update. Use `*` to update the entire PhraseSet resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### updatePhraseSetAsync(UpdatePhraseSetRequest request)
    
    
    public final OperationFuture<PhraseSet,OperationMetadata> updatePhraseSetAsync(UpdatePhraseSetRequest request)

Updates the PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UpdatePhraseSetRequest request =
           UpdatePhraseSetRequest.newBuilder()
               .setPhraseSet(PhraseSet.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       PhraseSet response = speechClient.updatePhraseSetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePhraseSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UpdatePhraseSetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### updatePhraseSetCallable()
    
    
    public final UnaryCallable<UpdatePhraseSetRequest,Operation> updatePhraseSetCallable()

Updates the PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UpdatePhraseSetRequest request =
           UpdatePhraseSetRequest.newBuilder()
               .setPhraseSet(PhraseSet.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = speechClient.updatePhraseSetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePhraseSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UpdatePhraseSetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updatePhraseSetOperationCallable()
    
    
    public final OperationCallable<UpdatePhraseSetRequest,PhraseSet,OperationMetadata> updatePhraseSetOperationCallable()

Updates the PhraseSet.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UpdatePhraseSetRequest request =
           UpdatePhraseSetRequest.newBuilder()
               .setPhraseSet(PhraseSet.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<PhraseSet, OperationMetadata> future =
           speechClient.updatePhraseSetOperationCallable().futureCall(request);
       // Do something.
       PhraseSet response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdatePhraseSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UpdatePhraseSetRequest),[PhraseSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.PhraseSet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### updateRecognizerAsync(Recognizer recognizer, FieldMask updateMask)
    
    
    public final OperationFuture<Recognizer,OperationMetadata> updateRecognizerAsync(Recognizer recognizer, FieldMask updateMask)

Updates the Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       Recognizer recognizer = Recognizer.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Recognizer response = speechClient.updateRecognizerAsync(recognizer, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`recognizer` | `[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer)`  
Required. The Recognizer to update. The Recognizer's `name` field is used to identify the Recognizer to update. Format: `projects/{project}/locations/{location}/recognizers/{recognizer}`.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields to update. If empty, all non-default valued fields are considered for update. Use `*` to update the entire Recognizer resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### updateRecognizerAsync(UpdateRecognizerRequest request)
    
    
    public final OperationFuture<Recognizer,OperationMetadata> updateRecognizerAsync(UpdateRecognizerRequest request)

Updates the Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UpdateRecognizerRequest request =
           UpdateRecognizerRequest.newBuilder()
               .setRecognizer(Recognizer.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       Recognizer response = speechClient.updateRecognizerAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UpdateRecognizerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
### updateRecognizerCallable()
    
    
    public final UnaryCallable<UpdateRecognizerRequest,Operation> updateRecognizerCallable()

Updates the Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UpdateRecognizerRequest request =
           UpdateRecognizerRequest.newBuilder()
               .setRecognizer(Recognizer.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = speechClient.updateRecognizerCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UpdateRecognizerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateRecognizerOperationCallable()
    
    
    public final OperationCallable<UpdateRecognizerRequest,Recognizer,OperationMetadata> updateRecognizerOperationCallable()

Updates the Recognizer.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpeechClient speechClient = SpeechClient.create()) {
       UpdateRecognizerRequest request =
           UpdateRecognizerRequest.newBuilder()
               .setRecognizer(Recognizer.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<Recognizer, OperationMetadata> future =
           speechClient.updateRecognizerOperationCallable().futureCall(request);
       // Do something.
       Recognizer response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateRecognizerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.UpdateRecognizerRequest),[Recognizer](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.Recognizer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v2.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
