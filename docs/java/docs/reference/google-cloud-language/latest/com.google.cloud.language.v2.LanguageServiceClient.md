---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.LanguageServiceClient
title: Class LanguageServiceClient (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:46.488096+00:00
---

# Class LanguageServiceClient (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.LanguageServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LanguageServiceClient (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.1  2.3.4  2.2.0  2.1.10 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-language/google-cloud-language/src/main/java/com/google/cloud/language/v2/LanguageServiceClient.java)| [Product Reference](https://cloud.google.com/natural-language/docs/)| [REST Documentation](https://cloud.google.com/natural-language/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/natural-language/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Provides text analysis operations such as sentiment analysis and entity recognition.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       Document document = Document.newBuilder().build();
       AnalyzeSentimentResponse response = languageServiceClient.analyzeSentiment(document);
     }
     

Note: close() needs to be called on the LanguageServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AnalyzeSentiment |  Analyzes the sentiment of the provided text. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * analyzeSentiment(AnalyzeSentimentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * analyzeSentiment(Document document) 
  * analyzeSentiment(Document document, EncodingType encodingType) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * analyzeSentimentCallable() 

  
AnalyzeEntities |  Finds named entities (currently proper names and common nouns) in the text along with entity types, probability, mentions for each entity, and other properties. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * analyzeEntities(AnalyzeEntitiesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * analyzeEntities(Document document) 
  * analyzeEntities(Document document, EncodingType encodingType) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * analyzeEntitiesCallable() 

  
ClassifyText |  Classifies a document into categories. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * classifyText(ClassifyTextRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * classifyText(Document document) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * classifyTextCallable() 

  
ModerateText |  Moderates a document for harmful and sensitive categories. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * moderateText(ModerateTextRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * moderateText(Document document) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * moderateTextCallable() 

  
AnnotateText |  A convenience method that provides all features in one call. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * annotateText(AnnotateTextRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * annotateText(Document document, AnnotateTextRequest.Features features) 
  * annotateText(Document document, AnnotateTextRequest.Features features, EncodingType encodingType) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * annotateTextCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of LanguageServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LanguageServiceSettings languageServiceSettings =
         LanguageServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     LanguageServiceClient languageServiceClient =
         LanguageServiceClient.create(languageServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LanguageServiceSettings languageServiceSettings =
         LanguageServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     LanguageServiceClient languageServiceClient =
         LanguageServiceClient.create(languageServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LanguageServiceSettings languageServiceSettings =
         LanguageServiceSettings.newHttpJsonBuilder().build();
     LanguageServiceClient languageServiceClient =
         LanguageServiceClient.create(languageServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LanguageServiceClient

## Static Methods 

### create()
    
    
    public static final LanguageServiceClient create()

Constructs an instance of LanguageServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[LanguageServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.LanguageServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LanguageServiceSettings settings)
    
    
    public static final LanguageServiceClient create(LanguageServiceSettings settings)

Constructs an instance of LanguageServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LanguageServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.LanguageServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LanguageServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.LanguageServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LanguageServiceStub stub)
    
    
    public static final LanguageServiceClient create(LanguageServiceStub stub)

Constructs an instance of LanguageServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(LanguageServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LanguageServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.stub.LanguageServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LanguageServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.LanguageServiceClient)` |   
  
## Constructors 

### LanguageServiceClient(LanguageServiceSettings settings)
    
    
    protected LanguageServiceClient(LanguageServiceSettings settings)

Constructs an instance of LanguageServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LanguageServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.LanguageServiceSettings)`  
  
  
### LanguageServiceClient(LanguageServiceStub stub)
    
    
    protected LanguageServiceClient(LanguageServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LanguageServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.stub.LanguageServiceStub)`  
  
  
## Methods 

### analyzeEntities(AnalyzeEntitiesRequest request)
    
    
    public final AnalyzeEntitiesResponse analyzeEntities(AnalyzeEntitiesRequest request)

Finds named entities (currently proper names and common nouns) in the text along with entity types, probability, mentions for each entity, and other properties.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       AnalyzeEntitiesRequest request =
           AnalyzeEntitiesRequest.newBuilder()
               .setDocument(Document.newBuilder().build())
               .setEncodingType(EncodingType.forNumber(0))
               .build();
       AnalyzeEntitiesResponse response = languageServiceClient.analyzeEntities(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AnalyzeEntitiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnalyzeEntitiesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeEntitiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnalyzeEntitiesResponse)` |   
  
### analyzeEntities(Document document)
    
    
    public final AnalyzeEntitiesResponse analyzeEntities(Document document)

Finds named entities (currently proper names and common nouns) in the text along with entity types, probability, mentions for each entity, and other properties.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       Document document = Document.newBuilder().build();
       AnalyzeEntitiesResponse response = languageServiceClient.analyzeEntities(document);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Document)`  
Required. Input document.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeEntitiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnalyzeEntitiesResponse)` |   
  
### analyzeEntities(Document document, EncodingType encodingType)
    
    
    public final AnalyzeEntitiesResponse analyzeEntities(Document document, EncodingType encodingType)

Finds named entities (currently proper names and common nouns) in the text along with entity types, probability, mentions for each entity, and other properties.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       Document document = Document.newBuilder().build();
       EncodingType encodingType = EncodingType.forNumber(0);
       AnalyzeEntitiesResponse response =
           languageServiceClient.analyzeEntities(document, encodingType);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Document)`  
Required. Input document.  
`encodingType` | `[EncodingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EncodingType)`  
The encoding type used by the API to calculate offsets.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeEntitiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnalyzeEntitiesResponse)` |   
  
### analyzeEntitiesCallable()
    
    
    public final UnaryCallable<AnalyzeEntitiesRequest,AnalyzeEntitiesResponse> analyzeEntitiesCallable()

Finds named entities (currently proper names and common nouns) in the text along with entity types, probability, mentions for each entity, and other properties.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       AnalyzeEntitiesRequest request =
           AnalyzeEntitiesRequest.newBuilder()
               .setDocument(Document.newBuilder().build())
               .setEncodingType(EncodingType.forNumber(0))
               .build();
       ApiFuture<AnalyzeEntitiesResponse> future =
           languageServiceClient.analyzeEntitiesCallable().futureCall(request);
       // Do something.
       AnalyzeEntitiesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AnalyzeEntitiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnalyzeEntitiesRequest),[AnalyzeEntitiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnalyzeEntitiesResponse)>` |   
  
### analyzeSentiment(AnalyzeSentimentRequest request)
    
    
    public final AnalyzeSentimentResponse analyzeSentiment(AnalyzeSentimentRequest request)

Analyzes the sentiment of the provided text.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       AnalyzeSentimentRequest request =
           AnalyzeSentimentRequest.newBuilder()
               .setDocument(Document.newBuilder().build())
               .setEncodingType(EncodingType.forNumber(0))
               .build();
       AnalyzeSentimentResponse response = languageServiceClient.analyzeSentiment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AnalyzeSentimentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnalyzeSentimentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeSentimentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnalyzeSentimentResponse)` |   
  
### analyzeSentiment(Document document)
    
    
    public final AnalyzeSentimentResponse analyzeSentiment(Document document)

Analyzes the sentiment of the provided text.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       Document document = Document.newBuilder().build();
       AnalyzeSentimentResponse response = languageServiceClient.analyzeSentiment(document);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Document)`  
Required. Input document.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeSentimentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnalyzeSentimentResponse)` |   
  
### analyzeSentiment(Document document, EncodingType encodingType)
    
    
    public final AnalyzeSentimentResponse analyzeSentiment(Document document, EncodingType encodingType)

Analyzes the sentiment of the provided text.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       Document document = Document.newBuilder().build();
       EncodingType encodingType = EncodingType.forNumber(0);
       AnalyzeSentimentResponse response =
           languageServiceClient.analyzeSentiment(document, encodingType);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Document)`  
Required. Input document.  
`encodingType` | `[EncodingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EncodingType)`  
The encoding type used by the API to calculate sentence offsets.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeSentimentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnalyzeSentimentResponse)` |   
  
### analyzeSentimentCallable()
    
    
    public final UnaryCallable<AnalyzeSentimentRequest,AnalyzeSentimentResponse> analyzeSentimentCallable()

Analyzes the sentiment of the provided text.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       AnalyzeSentimentRequest request =
           AnalyzeSentimentRequest.newBuilder()
               .setDocument(Document.newBuilder().build())
               .setEncodingType(EncodingType.forNumber(0))
               .build();
       ApiFuture<AnalyzeSentimentResponse> future =
           languageServiceClient.analyzeSentimentCallable().futureCall(request);
       // Do something.
       AnalyzeSentimentResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AnalyzeSentimentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnalyzeSentimentRequest),[AnalyzeSentimentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnalyzeSentimentResponse)>` |   
  
### annotateText(AnnotateTextRequest request)
    
    
    public final AnnotateTextResponse annotateText(AnnotateTextRequest request)

A convenience method that provides all features in one call.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       AnnotateTextRequest request =
           AnnotateTextRequest.newBuilder()
               .setDocument(Document.newBuilder().build())
               .setFeatures(AnnotateTextRequest.Features.newBuilder().build())
               .setEncodingType(EncodingType.forNumber(0))
               .build();
       AnnotateTextResponse response = languageServiceClient.annotateText(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AnnotateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnnotateTextRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnnotateTextResponse)` |   
  
### annotateText(Document document, AnnotateTextRequest.Features features)
    
    
    public final AnnotateTextResponse annotateText(Document document, AnnotateTextRequest.Features features)

A convenience method that provides all features in one call.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       Document document = Document.newBuilder().build();
       AnnotateTextRequest.Features features = AnnotateTextRequest.Features.newBuilder().build();
       AnnotateTextResponse response = languageServiceClient.annotateText(document, features);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Document)`  
Required. Input document.  
`features` | `[AnnotateTextRequest.Features](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnnotateTextRequest.Features)`  
Required. The enabled features.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnnotateTextResponse)` |   
  
### annotateText(Document document, AnnotateTextRequest.Features features, EncodingType encodingType)
    
    
    public final AnnotateTextResponse annotateText(Document document, AnnotateTextRequest.Features features, EncodingType encodingType)

A convenience method that provides all features in one call.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       Document document = Document.newBuilder().build();
       AnnotateTextRequest.Features features = AnnotateTextRequest.Features.newBuilder().build();
       EncodingType encodingType = EncodingType.forNumber(0);
       AnnotateTextResponse response =
           languageServiceClient.annotateText(document, features, encodingType);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Document)`  
Required. Input document.  
`features` | `[AnnotateTextRequest.Features](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnnotateTextRequest.Features)`  
Required. The enabled features.  
`encodingType` | `[EncodingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EncodingType)`  
The encoding type used by the API to calculate offsets.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnnotateTextResponse)` |   
  
### annotateTextCallable()
    
    
    public final UnaryCallable<AnnotateTextRequest,AnnotateTextResponse> annotateTextCallable()

A convenience method that provides all features in one call.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       AnnotateTextRequest request =
           AnnotateTextRequest.newBuilder()
               .setDocument(Document.newBuilder().build())
               .setFeatures(AnnotateTextRequest.Features.newBuilder().build())
               .setEncodingType(EncodingType.forNumber(0))
               .build();
       ApiFuture<AnnotateTextResponse> future =
           languageServiceClient.annotateTextCallable().futureCall(request);
       // Do something.
       AnnotateTextResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AnnotateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnnotateTextRequest),[AnnotateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.AnnotateTextResponse)>` |   
  
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
  
### classifyText(ClassifyTextRequest request)
    
    
    public final ClassifyTextResponse classifyText(ClassifyTextRequest request)

Classifies a document into categories.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       ClassifyTextRequest request =
           ClassifyTextRequest.newBuilder().setDocument(Document.newBuilder().build()).build();
       ClassifyTextResponse response = languageServiceClient.classifyText(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ClassifyTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.ClassifyTextRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ClassifyTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.ClassifyTextResponse)` |   
  
### classifyText(Document document)
    
    
    public final ClassifyTextResponse classifyText(Document document)

Classifies a document into categories.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       Document document = Document.newBuilder().build();
       ClassifyTextResponse response = languageServiceClient.classifyText(document);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Document)`  
Required. Input document.  
**Returns**  
---  
**Type** | **Description**  
`[ClassifyTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.ClassifyTextResponse)` |   
  
### classifyTextCallable()
    
    
    public final UnaryCallable<ClassifyTextRequest,ClassifyTextResponse> classifyTextCallable()

Classifies a document into categories.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       ClassifyTextRequest request =
           ClassifyTextRequest.newBuilder().setDocument(Document.newBuilder().build()).build();
       ApiFuture<ClassifyTextResponse> future =
           languageServiceClient.classifyTextCallable().futureCall(request);
       // Do something.
       ClassifyTextResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ClassifyTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.ClassifyTextRequest),[ClassifyTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.ClassifyTextResponse)>` |   
  
### close()
    
    
    public final void close()

### getSettings()
    
    
    public final @Nullable LanguageServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.language.v2.LanguageServiceSettings` |   
  
### getStub()
    
    
    public LanguageServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[LanguageServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.stub.LanguageServiceStub)` |   
  
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
  
### moderateText(Document document)
    
    
    public final ModerateTextResponse moderateText(Document document)

Moderates a document for harmful and sensitive categories.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       Document document = Document.newBuilder().build();
       ModerateTextResponse response = languageServiceClient.moderateText(document);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`document` | `[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Document)`  
Required. Input document.  
**Returns**  
---  
**Type** | **Description**  
`[ModerateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.ModerateTextResponse)` |   
  
### moderateText(ModerateTextRequest request)
    
    
    public final ModerateTextResponse moderateText(ModerateTextRequest request)

Moderates a document for harmful and sensitive categories.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       ModerateTextRequest request =
           ModerateTextRequest.newBuilder().setDocument(Document.newBuilder().build()).build();
       ModerateTextResponse response = languageServiceClient.moderateText(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ModerateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.ModerateTextRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ModerateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.ModerateTextResponse)` |   
  
### moderateTextCallable()
    
    
    public final UnaryCallable<ModerateTextRequest,ModerateTextResponse> moderateTextCallable()

Moderates a document for harmful and sensitive categories.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LanguageServiceClient languageServiceClient = LanguageServiceClient.create()) {
       ModerateTextRequest request =
           ModerateTextRequest.newBuilder().setDocument(Document.newBuilder().build()).build();
       ApiFuture<ModerateTextResponse> future =
           languageServiceClient.moderateTextCallable().futureCall(request);
       // Do something.
       ModerateTextResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ModerateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.ModerateTextRequest),[ModerateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.ModerateTextResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
