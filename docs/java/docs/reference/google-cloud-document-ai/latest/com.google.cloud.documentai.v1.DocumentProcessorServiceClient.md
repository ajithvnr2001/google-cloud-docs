---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient
title: Class DocumentProcessorServiceClient (2.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:14.475127+00:00
---

# Class DocumentProcessorServiceClient (2.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DocumentProcessorServiceClient (2.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.103.0 (latest)  2.99.0  2.98.0  2.97.0  2.95.0  2.92.0  2.91.0  2.89.0  2.87.0  2.86.0  2.85.0  2.84.0  2.82.0  2.80.0  2.79.0  2.78.0  2.77.0  2.76.0  2.74.0  2.72.0  2.71.0  2.68.0  2.67.0  2.66.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.5  2.6.2  2.5.1  2.4.3  2.3.1  2.2.1  2.1.9 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-document-ai/google-cloud-document-ai/src/main/java/com/google/cloud/documentai/v1/DocumentProcessorServiceClient.java)| [Product Reference](https://cloud.google.com/compute/docs/documentai/)  
---|---  
  
Service Description: Service to call Document AI to process documents according to the processor's definition. Processors are built using state-of-the-art Google AI such as natural language, computer vision, and translation to extract structured information from unstructured or semi-structured documents.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ResourceName name = ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]");
       ProcessResponse response = documentProcessorServiceClient.processDocument(name);
     }
     

Note: close() needs to be called on the DocumentProcessorServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ProcessDocument |  Processes a single document. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * processDocument(ProcessRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * processDocument(ResourceName name) 
  * processDocument(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * processDocumentCallable() 

  
BatchProcessDocuments |  LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchProcessDocumentsAsync(BatchProcessRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * batchProcessDocumentsAsync(ResourceName name) 
  * batchProcessDocumentsAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchProcessDocumentsOperationCallable() 
  * batchProcessDocumentsCallable() 

  
FetchProcessorTypes |  Fetches processor types. Note that we don't use ListProcessorTypes here, because it isn't paginated. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchProcessorTypes(FetchProcessorTypesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * fetchProcessorTypes(LocationName parent) 
  * fetchProcessorTypes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchProcessorTypesCallable() 

  
ListProcessorTypes |  Lists the processor types that exist. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listProcessorTypes(ListProcessorTypesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listProcessorTypes(LocationName parent) 
  * listProcessorTypes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listProcessorTypesPagedCallable() 
  * listProcessorTypesCallable() 

  
GetProcessorType |  Gets a processor type detail. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getProcessorType(GetProcessorTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getProcessorType(ProcessorTypeName name) 
  * getProcessorType(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getProcessorTypeCallable() 

  
ListProcessors |  Lists all processors which belong to this project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listProcessors(ListProcessorsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listProcessors(LocationName parent) 
  * listProcessors(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listProcessorsPagedCallable() 
  * listProcessorsCallable() 

  
GetProcessor |  Gets a processor detail. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getProcessor(GetProcessorRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getProcessor(ProcessorName name) 
  * getProcessor(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getProcessorCallable() 

  
TrainProcessorVersion |  Trains a new processor version. Operation metadata is returned as TrainProcessorVersionMetadata. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * trainProcessorVersionAsync(TrainProcessorVersionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * trainProcessorVersionAsync(ProcessorName parent, ProcessorVersion processorVersion) 
  * trainProcessorVersionAsync(String parent, ProcessorVersion processorVersion) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * trainProcessorVersionOperationCallable() 
  * trainProcessorVersionCallable() 

  
GetProcessorVersion |  Gets a processor version detail. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getProcessorVersion(GetProcessorVersionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getProcessorVersion(ProcessorVersionName name) 
  * getProcessorVersion(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getProcessorVersionCallable() 

  
ListProcessorVersions |  Lists all versions of a processor. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listProcessorVersions(ListProcessorVersionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listProcessorVersions(ProcessorName parent) 
  * listProcessorVersions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listProcessorVersionsPagedCallable() 
  * listProcessorVersionsCallable() 

  
DeleteProcessorVersion |  Deletes the processor version, all artifacts under the processor version will be deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteProcessorVersionAsync(DeleteProcessorVersionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteProcessorVersionAsync(ProcessorVersionName name) 
  * deleteProcessorVersionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteProcessorVersionOperationCallable() 
  * deleteProcessorVersionCallable() 

  
DeployProcessorVersion |  Deploys the processor version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deployProcessorVersionAsync(DeployProcessorVersionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deployProcessorVersionAsync(ProcessorVersionName name) 
  * deployProcessorVersionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deployProcessorVersionOperationCallable() 
  * deployProcessorVersionCallable() 

  
UndeployProcessorVersion |  Undeploys the processor version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * undeployProcessorVersionAsync(UndeployProcessorVersionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * undeployProcessorVersionAsync(ProcessorVersionName name) 
  * undeployProcessorVersionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * undeployProcessorVersionOperationCallable() 
  * undeployProcessorVersionCallable() 

  
CreateProcessor |  Creates a processor from the ProcessorType provided. The processor will be at `ENABLED` state by default after its creation. Note that this method requires the `documentai.processors.create` permission on the project, which is highly privileged. A user or service account with this permission can create new processors that can interact with any gcs bucket in your project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createProcessor(CreateProcessorRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createProcessor(LocationName parent, Processor processor) 
  * createProcessor(String parent, Processor processor) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createProcessorCallable() 

  
DeleteProcessor |  Deletes the processor, unloads all deployed model artifacts if it was enabled and then deletes all artifacts associated with this processor. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteProcessorAsync(DeleteProcessorRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteProcessorAsync(ProcessorName name) 
  * deleteProcessorAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteProcessorOperationCallable() 
  * deleteProcessorCallable() 

  
EnableProcessor |  Enables a processor |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * enableProcessorAsync(EnableProcessorRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * enableProcessorOperationCallable() 
  * enableProcessorCallable() 

  
DisableProcessor |  Disables a processor |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * disableProcessorAsync(DisableProcessorRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * disableProcessorOperationCallable() 
  * disableProcessorCallable() 

  
SetDefaultProcessorVersion |  Set the default (active) version of a Processor that will be used in ProcessDocument and BatchProcessDocuments. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setDefaultProcessorVersionAsync(SetDefaultProcessorVersionRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setDefaultProcessorVersionOperationCallable() 
  * setDefaultProcessorVersionCallable() 

  
ReviewDocument |  Send a document for Human Review. The input document should be processed by the specified processor. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * reviewDocumentAsync(ReviewDocumentRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * reviewDocumentAsync(HumanReviewConfigName humanReviewConfig) 
  * reviewDocumentAsync(String humanReviewConfig) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * reviewDocumentOperationCallable() 
  * reviewDocumentCallable() 

  
EvaluateProcessorVersion |  Evaluates a ProcessorVersion against annotated documents, producing an Evaluation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * evaluateProcessorVersionAsync(EvaluateProcessorVersionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * evaluateProcessorVersionAsync(ProcessorVersionName processorVersion) 
  * evaluateProcessorVersionAsync(String processorVersion) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * evaluateProcessorVersionOperationCallable() 
  * evaluateProcessorVersionCallable() 

  
GetEvaluation |  Retrieves a specific evaluation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEvaluation(GetEvaluationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEvaluation(EvaluationName name) 
  * getEvaluation(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEvaluationCallable() 

  
ListEvaluations |  Retrieves a set of evaluations for a given processor version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEvaluations(ListEvaluationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEvaluations(ProcessorVersionName parent) 
  * listEvaluations(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEvaluationsPagedCallable() 
  * listEvaluationsCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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

This class can be customized by passing in a custom instance of DocumentProcessorServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DocumentProcessorServiceSettings documentProcessorServiceSettings =
         DocumentProcessorServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create(documentProcessorServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DocumentProcessorServiceSettings documentProcessorServiceSettings =
         DocumentProcessorServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create(documentProcessorServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DocumentProcessorServiceSettings documentProcessorServiceSettings =
         DocumentProcessorServiceSettings.newHttpJsonBuilder().build();
     DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create(documentProcessorServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DocumentProcessorServiceClient

## Static Methods 

### create()
    
    
    public static final DocumentProcessorServiceClient create()

Constructs an instance of DocumentProcessorServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DocumentProcessorServiceSettings settings)
    
    
    public static final DocumentProcessorServiceClient create(DocumentProcessorServiceSettings settings)

Constructs an instance of DocumentProcessorServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DocumentProcessorServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DocumentProcessorServiceStub stub)
    
    
    public static final DocumentProcessorServiceClient create(DocumentProcessorServiceStub stub)

Constructs an instance of DocumentProcessorServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DocumentProcessorServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DocumentProcessorServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.stub.DocumentProcessorServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient)` |   
  
## Constructors 

### DocumentProcessorServiceClient(DocumentProcessorServiceSettings settings)
    
    
    protected DocumentProcessorServiceClient(DocumentProcessorServiceSettings settings)

Constructs an instance of DocumentProcessorServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DocumentProcessorServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceSettings)`  
  
  
### DocumentProcessorServiceClient(DocumentProcessorServiceStub stub)
    
    
    protected DocumentProcessorServiceClient(DocumentProcessorServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DocumentProcessorServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.stub.DocumentProcessorServiceStub)`  
  
  
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
  
### batchProcessDocumentsAsync(@Nullable ResourceName name)
    
    
    public final OperationFuture<BatchProcessResponse,BatchProcessMetadata> batchProcessDocumentsAsync(@Nullable ResourceName name)

LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ResourceName name = ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]");
       BatchProcessResponse response =
           documentProcessorServiceClient.batchProcessDocumentsAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.api.resourcenames.ResourceName`  
Required. The resource name of Processor or ProcessorVersion. Format: `projects/{project}/locations/{location}/processors/{processor}`, or `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchProcessResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessResponse),[BatchProcessMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessMetadata)>` |   
  
### batchProcessDocumentsAsync(BatchProcessRequest request)
    
    
    public final OperationFuture<BatchProcessResponse,BatchProcessMetadata> batchProcessDocumentsAsync(BatchProcessRequest request)

LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       BatchProcessRequest request =
           BatchProcessRequest.newBuilder()
               .setName(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setInputDocuments(BatchDocumentsInputConfig.newBuilder().build())
               .setDocumentOutputConfig(DocumentOutputConfig.newBuilder().build())
               .setSkipHumanReview(true)
               .setProcessOptions(ProcessOptions.newBuilder().build())
               .putAllLabels(new HashMap<String, String>())
               .build();
       BatchProcessResponse response =
           documentProcessorServiceClient.batchProcessDocumentsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchProcessResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessResponse),[BatchProcessMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessMetadata)>` |   
  
### batchProcessDocumentsAsync(String name)
    
    
    public final OperationFuture<BatchProcessResponse,BatchProcessMetadata> batchProcessDocumentsAsync(String name)

LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String name =
           EvaluationName.of(
                   "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]", "[EVALUATION]")
               .toString();
       BatchProcessResponse response =
           documentProcessorServiceClient.batchProcessDocumentsAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of Processor or ProcessorVersion. Format: `projects/{project}/locations/{location}/processors/{processor}`, or `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchProcessResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessResponse),[BatchProcessMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessMetadata)>` |   
  
### batchProcessDocumentsCallable()
    
    
    public final UnaryCallable<BatchProcessRequest,Operation> batchProcessDocumentsCallable()

LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       BatchProcessRequest request =
           BatchProcessRequest.newBuilder()
               .setName(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setInputDocuments(BatchDocumentsInputConfig.newBuilder().build())
               .setDocumentOutputConfig(DocumentOutputConfig.newBuilder().build())
               .setSkipHumanReview(true)
               .setProcessOptions(ProcessOptions.newBuilder().build())
               .putAllLabels(new HashMap<String, String>())
               .build();
       ApiFuture<Operation> future =
           documentProcessorServiceClient.batchProcessDocumentsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchProcessDocumentsOperationCallable()
    
    
    public final OperationCallable<BatchProcessRequest,BatchProcessResponse,BatchProcessMetadata> batchProcessDocumentsOperationCallable()

LRO endpoint to batch process many documents. The output is written to Cloud Storage as JSON in the [Document] format.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       BatchProcessRequest request =
           BatchProcessRequest.newBuilder()
               .setName(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setInputDocuments(BatchDocumentsInputConfig.newBuilder().build())
               .setDocumentOutputConfig(DocumentOutputConfig.newBuilder().build())
               .setSkipHumanReview(true)
               .setProcessOptions(ProcessOptions.newBuilder().build())
               .putAllLabels(new HashMap<String, String>())
               .build();
       OperationFuture<BatchProcessResponse, BatchProcessMetadata> future =
           documentProcessorServiceClient
               .batchProcessDocumentsOperationCallable()
               .futureCall(request);
       // Do something.
       BatchProcessResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessRequest),[BatchProcessResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessResponse),[BatchProcessMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.BatchProcessMetadata)>` |   
  
### close()
    
    
    public final void close()

### createProcessor(@Nullable LocationName parent, Processor processor)
    
    
    public final Processor createProcessor(@Nullable LocationName parent, Processor processor)

Creates a processor from the ProcessorType provided. The processor will be at `ENABLED` state by default after its creation. Note that this method requires the `documentai.processors.create` permission on the project, which is highly privileged. A user or service account with this permission can create new processors that can interact with any gcs bucket in your project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Processor processor = Processor.newBuilder().build();
       Processor response = documentProcessorServiceClient.createProcessor(parent, processor);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.LocationName`  
Required. The parent (project and location) under which to create the processor. Format: `projects/{project}/locations/{location}`  
`processor` | `[Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor)`  
Required. The processor to be created, requires Processor.type and Processor.display_name to be set. Also, the Processor.kms_key_name field must be set if the processor is under CMEK.  
**Returns**  
---  
**Type** | **Description**  
`[Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor)` |   
  
### createProcessor(CreateProcessorRequest request)
    
    
    public final Processor createProcessor(CreateProcessorRequest request)

Creates a processor from the ProcessorType provided. The processor will be at `ENABLED` state by default after its creation. Note that this method requires the `documentai.processors.create` permission on the project, which is highly privileged. A user or service account with this permission can create new processors that can interact with any gcs bucket in your project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       CreateProcessorRequest request =
           CreateProcessorRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setProcessor(Processor.newBuilder().build())
               .build();
       Processor response = documentProcessorServiceClient.createProcessor(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.CreateProcessorRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor)` |   
  
### createProcessor(String parent, Processor processor)
    
    
    public final Processor createProcessor(String parent, Processor processor)

Creates a processor from the ProcessorType provided. The processor will be at `ENABLED` state by default after its creation. Note that this method requires the `documentai.processors.create` permission on the project, which is highly privileged. A user or service account with this permission can create new processors that can interact with any gcs bucket in your project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Processor processor = Processor.newBuilder().build();
       Processor response = documentProcessorServiceClient.createProcessor(parent, processor);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent (project and location) under which to create the processor. Format: `projects/{project}/locations/{location}`  
`processor` | `[Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor)`  
Required. The processor to be created, requires Processor.type and Processor.display_name to be set. Also, the Processor.kms_key_name field must be set if the processor is under CMEK.  
**Returns**  
---  
**Type** | **Description**  
`[Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor)` |   
  
### createProcessorCallable()
    
    
    public final UnaryCallable<CreateProcessorRequest,Processor> createProcessorCallable()

Creates a processor from the ProcessorType provided. The processor will be at `ENABLED` state by default after its creation. Note that this method requires the `documentai.processors.create` permission on the project, which is highly privileged. A user or service account with this permission can create new processors that can interact with any gcs bucket in your project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       CreateProcessorRequest request =
           CreateProcessorRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setProcessor(Processor.newBuilder().build())
               .build();
       ApiFuture<Processor> future =
           documentProcessorServiceClient.createProcessorCallable().futureCall(request);
       // Do something.
       Processor response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.CreateProcessorRequest),[Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor)>` |   
  
### deleteProcessorAsync(@Nullable ProcessorName name)
    
    
    public final OperationFuture<Empty,DeleteProcessorMetadata> deleteProcessorAsync(@Nullable ProcessorName name)

Deletes the processor, unloads all deployed model artifacts if it was enabled and then deletes all artifacts associated with this processor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ProcessorName name = ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]");
       documentProcessorServiceClient.deleteProcessorAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.ProcessorName`  
Required. The processor resource name to be deleted.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteProcessorMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorMetadata)>` |   
  
### deleteProcessorAsync(DeleteProcessorRequest request)
    
    
    public final OperationFuture<Empty,DeleteProcessorMetadata> deleteProcessorAsync(DeleteProcessorRequest request)

Deletes the processor, unloads all deployed model artifacts if it was enabled and then deletes all artifacts associated with this processor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       DeleteProcessorRequest request =
           DeleteProcessorRequest.newBuilder()
               .setName(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .build();
       documentProcessorServiceClient.deleteProcessorAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteProcessorMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorMetadata)>` |   
  
### deleteProcessorAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteProcessorMetadata> deleteProcessorAsync(String name)

Deletes the processor, unloads all deployed model artifacts if it was enabled and then deletes all artifacts associated with this processor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String name = ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString();
       documentProcessorServiceClient.deleteProcessorAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The processor resource name to be deleted.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteProcessorMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorMetadata)>` |   
  
### deleteProcessorCallable()
    
    
    public final UnaryCallable<DeleteProcessorRequest,Operation> deleteProcessorCallable()

Deletes the processor, unloads all deployed model artifacts if it was enabled and then deletes all artifacts associated with this processor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       DeleteProcessorRequest request =
           DeleteProcessorRequest.newBuilder()
               .setName(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .build();
       ApiFuture<Operation> future =
           documentProcessorServiceClient.deleteProcessorCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteProcessorOperationCallable()
    
    
    public final OperationCallable<DeleteProcessorRequest,Empty,DeleteProcessorMetadata> deleteProcessorOperationCallable()

Deletes the processor, unloads all deployed model artifacts if it was enabled and then deletes all artifacts associated with this processor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       DeleteProcessorRequest request =
           DeleteProcessorRequest.newBuilder()
               .setName(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .build();
       OperationFuture<Empty, DeleteProcessorMetadata> future =
           documentProcessorServiceClient.deleteProcessorOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteProcessorMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorMetadata)>` |   
  
### deleteProcessorVersionAsync(@Nullable ProcessorVersionName name)
    
    
    public final OperationFuture<Empty,DeleteProcessorVersionMetadata> deleteProcessorVersionAsync(@Nullable ProcessorVersionName name)

Deletes the processor version, all artifacts under the processor version will be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ProcessorVersionName name =
           ProcessorVersionName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]");
       documentProcessorServiceClient.deleteProcessorVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.ProcessorVersionName`  
Required. The processor version resource name to be deleted.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorVersionMetadata)>` |   
  
### deleteProcessorVersionAsync(DeleteProcessorVersionRequest request)
    
    
    public final OperationFuture<Empty,DeleteProcessorVersionMetadata> deleteProcessorVersionAsync(DeleteProcessorVersionRequest request)

Deletes the processor version, all artifacts under the processor version will be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       DeleteProcessorVersionRequest request =
           DeleteProcessorVersionRequest.newBuilder()
               .setName(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .build();
       documentProcessorServiceClient.deleteProcessorVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorVersionMetadata)>` |   
  
### deleteProcessorVersionAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteProcessorVersionMetadata> deleteProcessorVersionAsync(String name)

Deletes the processor version, all artifacts under the processor version will be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String name =
           ProcessorVersionName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
               .toString();
       documentProcessorServiceClient.deleteProcessorVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The processor version resource name to be deleted.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorVersionMetadata)>` |   
  
### deleteProcessorVersionCallable()
    
    
    public final UnaryCallable<DeleteProcessorVersionRequest,Operation> deleteProcessorVersionCallable()

Deletes the processor version, all artifacts under the processor version will be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       DeleteProcessorVersionRequest request =
           DeleteProcessorVersionRequest.newBuilder()
               .setName(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           documentProcessorServiceClient.deleteProcessorVersionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorVersionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteProcessorVersionOperationCallable()
    
    
    public final OperationCallable<DeleteProcessorVersionRequest,Empty,DeleteProcessorVersionMetadata> deleteProcessorVersionOperationCallable()

Deletes the processor version, all artifacts under the processor version will be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       DeleteProcessorVersionRequest request =
           DeleteProcessorVersionRequest.newBuilder()
               .setName(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteProcessorVersionMetadata> future =
           documentProcessorServiceClient
               .deleteProcessorVersionOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorVersionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeleteProcessorVersionMetadata)>` |   
  
### deployProcessorVersionAsync(@Nullable ProcessorVersionName name)
    
    
    public final OperationFuture<DeployProcessorVersionResponse,DeployProcessorVersionMetadata> deployProcessorVersionAsync(@Nullable ProcessorVersionName name)

Deploys the processor version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ProcessorVersionName name =
           ProcessorVersionName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]");
       DeployProcessorVersionResponse response =
           documentProcessorServiceClient.deployProcessorVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.ProcessorVersionName`  
Required. The processor version resource name to be deployed.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeployProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeployProcessorVersionResponse),[DeployProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeployProcessorVersionMetadata)>` |   
  
### deployProcessorVersionAsync(DeployProcessorVersionRequest request)
    
    
    public final OperationFuture<DeployProcessorVersionResponse,DeployProcessorVersionMetadata> deployProcessorVersionAsync(DeployProcessorVersionRequest request)

Deploys the processor version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       DeployProcessorVersionRequest request =
           DeployProcessorVersionRequest.newBuilder()
               .setName(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .build();
       DeployProcessorVersionResponse response =
           documentProcessorServiceClient.deployProcessorVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeployProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeployProcessorVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeployProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeployProcessorVersionResponse),[DeployProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeployProcessorVersionMetadata)>` |   
  
### deployProcessorVersionAsync(String name)
    
    
    public final OperationFuture<DeployProcessorVersionResponse,DeployProcessorVersionMetadata> deployProcessorVersionAsync(String name)

Deploys the processor version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String name =
           ProcessorVersionName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
               .toString();
       DeployProcessorVersionResponse response =
           documentProcessorServiceClient.deployProcessorVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The processor version resource name to be deployed.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeployProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeployProcessorVersionResponse),[DeployProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeployProcessorVersionMetadata)>` |   
  
### deployProcessorVersionCallable()
    
    
    public final UnaryCallable<DeployProcessorVersionRequest,Operation> deployProcessorVersionCallable()

Deploys the processor version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       DeployProcessorVersionRequest request =
           DeployProcessorVersionRequest.newBuilder()
               .setName(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           documentProcessorServiceClient.deployProcessorVersionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeployProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeployProcessorVersionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deployProcessorVersionOperationCallable()
    
    
    public final OperationCallable<DeployProcessorVersionRequest,DeployProcessorVersionResponse,DeployProcessorVersionMetadata> deployProcessorVersionOperationCallable()

Deploys the processor version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       DeployProcessorVersionRequest request =
           DeployProcessorVersionRequest.newBuilder()
               .setName(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .build();
       OperationFuture<DeployProcessorVersionResponse, DeployProcessorVersionMetadata> future =
           documentProcessorServiceClient
               .deployProcessorVersionOperationCallable()
               .futureCall(request);
       // Do something.
       DeployProcessorVersionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeployProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeployProcessorVersionRequest),[DeployProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeployProcessorVersionResponse),[DeployProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DeployProcessorVersionMetadata)>` |   
  
### disableProcessorAsync(DisableProcessorRequest request)
    
    
    public final OperationFuture<DisableProcessorResponse,DisableProcessorMetadata> disableProcessorAsync(DisableProcessorRequest request)

Disables a processor

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       DisableProcessorRequest request =
           DisableProcessorRequest.newBuilder()
               .setName(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .build();
       DisableProcessorResponse response =
           documentProcessorServiceClient.disableProcessorAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DisableProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DisableProcessorRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DisableProcessorResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DisableProcessorResponse),[DisableProcessorMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DisableProcessorMetadata)>` |   
  
### disableProcessorCallable()
    
    
    public final UnaryCallable<DisableProcessorRequest,Operation> disableProcessorCallable()

Disables a processor

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       DisableProcessorRequest request =
           DisableProcessorRequest.newBuilder()
               .setName(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .build();
       ApiFuture<Operation> future =
           documentProcessorServiceClient.disableProcessorCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DisableProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DisableProcessorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### disableProcessorOperationCallable()
    
    
    public final OperationCallable<DisableProcessorRequest,DisableProcessorResponse,DisableProcessorMetadata> disableProcessorOperationCallable()

Disables a processor

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       DisableProcessorRequest request =
           DisableProcessorRequest.newBuilder()
               .setName(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .build();
       OperationFuture<DisableProcessorResponse, DisableProcessorMetadata> future =
           documentProcessorServiceClient.disableProcessorOperationCallable().futureCall(request);
       // Do something.
       DisableProcessorResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DisableProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DisableProcessorRequest),[DisableProcessorResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DisableProcessorResponse),[DisableProcessorMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DisableProcessorMetadata)>` |   
  
### enableProcessorAsync(EnableProcessorRequest request)
    
    
    public final OperationFuture<EnableProcessorResponse,EnableProcessorMetadata> enableProcessorAsync(EnableProcessorRequest request)

Enables a processor

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       EnableProcessorRequest request =
           EnableProcessorRequest.newBuilder()
               .setName(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .build();
       EnableProcessorResponse response =
           documentProcessorServiceClient.enableProcessorAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EnableProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EnableProcessorRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EnableProcessorResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EnableProcessorResponse),[EnableProcessorMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EnableProcessorMetadata)>` |   
  
### enableProcessorCallable()
    
    
    public final UnaryCallable<EnableProcessorRequest,Operation> enableProcessorCallable()

Enables a processor

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       EnableProcessorRequest request =
           EnableProcessorRequest.newBuilder()
               .setName(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .build();
       ApiFuture<Operation> future =
           documentProcessorServiceClient.enableProcessorCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[EnableProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EnableProcessorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### enableProcessorOperationCallable()
    
    
    public final OperationCallable<EnableProcessorRequest,EnableProcessorResponse,EnableProcessorMetadata> enableProcessorOperationCallable()

Enables a processor

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       EnableProcessorRequest request =
           EnableProcessorRequest.newBuilder()
               .setName(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .build();
       OperationFuture<EnableProcessorResponse, EnableProcessorMetadata> future =
           documentProcessorServiceClient.enableProcessorOperationCallable().futureCall(request);
       // Do something.
       EnableProcessorResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[EnableProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EnableProcessorRequest),[EnableProcessorResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EnableProcessorResponse),[EnableProcessorMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EnableProcessorMetadata)>` |   
  
### evaluateProcessorVersionAsync(@Nullable ProcessorVersionName processorVersion)
    
    
    public final OperationFuture<EvaluateProcessorVersionResponse,EvaluateProcessorVersionMetadata> evaluateProcessorVersionAsync(@Nullable ProcessorVersionName processorVersion)

Evaluates a ProcessorVersion against annotated documents, producing an Evaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ProcessorVersionName processorVersion =
           ProcessorVersionName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]");
       EvaluateProcessorVersionResponse response =
           documentProcessorServiceClient.evaluateProcessorVersionAsync(processorVersion).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`processorVersion` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.ProcessorVersionName`  
Required. The resource name of the ProcessorVersion to evaluate. `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EvaluateProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluateProcessorVersionResponse),[EvaluateProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluateProcessorVersionMetadata)>` |   
  
### evaluateProcessorVersionAsync(EvaluateProcessorVersionRequest request)
    
    
    public final OperationFuture<EvaluateProcessorVersionResponse,EvaluateProcessorVersionMetadata> evaluateProcessorVersionAsync(EvaluateProcessorVersionRequest request)

Evaluates a ProcessorVersion against annotated documents, producing an Evaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       EvaluateProcessorVersionRequest request =
           EvaluateProcessorVersionRequest.newBuilder()
               .setProcessorVersion(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .setEvaluationDocuments(BatchDocumentsInputConfig.newBuilder().build())
               .build();
       EvaluateProcessorVersionResponse response =
           documentProcessorServiceClient.evaluateProcessorVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EvaluateProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluateProcessorVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EvaluateProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluateProcessorVersionResponse),[EvaluateProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluateProcessorVersionMetadata)>` |   
  
### evaluateProcessorVersionAsync(String processorVersion)
    
    
    public final OperationFuture<EvaluateProcessorVersionResponse,EvaluateProcessorVersionMetadata> evaluateProcessorVersionAsync(String processorVersion)

Evaluates a ProcessorVersion against annotated documents, producing an Evaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String processorVersion =
           ProcessorVersionName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
               .toString();
       EvaluateProcessorVersionResponse response =
           documentProcessorServiceClient.evaluateProcessorVersionAsync(processorVersion).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`processorVersion` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ProcessorVersion to evaluate. `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EvaluateProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluateProcessorVersionResponse),[EvaluateProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluateProcessorVersionMetadata)>` |   
  
### evaluateProcessorVersionCallable()
    
    
    public final UnaryCallable<EvaluateProcessorVersionRequest,Operation> evaluateProcessorVersionCallable()

Evaluates a ProcessorVersion against annotated documents, producing an Evaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       EvaluateProcessorVersionRequest request =
           EvaluateProcessorVersionRequest.newBuilder()
               .setProcessorVersion(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .setEvaluationDocuments(BatchDocumentsInputConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           documentProcessorServiceClient.evaluateProcessorVersionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[EvaluateProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluateProcessorVersionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### evaluateProcessorVersionOperationCallable()
    
    
    public final OperationCallable<EvaluateProcessorVersionRequest,EvaluateProcessorVersionResponse,EvaluateProcessorVersionMetadata> evaluateProcessorVersionOperationCallable()

Evaluates a ProcessorVersion against annotated documents, producing an Evaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       EvaluateProcessorVersionRequest request =
           EvaluateProcessorVersionRequest.newBuilder()
               .setProcessorVersion(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .setEvaluationDocuments(BatchDocumentsInputConfig.newBuilder().build())
               .build();
       OperationFuture<EvaluateProcessorVersionResponse, EvaluateProcessorVersionMetadata> future =
           documentProcessorServiceClient
               .evaluateProcessorVersionOperationCallable()
               .futureCall(request);
       // Do something.
       EvaluateProcessorVersionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[EvaluateProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluateProcessorVersionRequest),[EvaluateProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluateProcessorVersionResponse),[EvaluateProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluateProcessorVersionMetadata)>` |   
  
### fetchProcessorTypes(@Nullable LocationName parent)
    
    
    public final FetchProcessorTypesResponse fetchProcessorTypes(@Nullable LocationName parent)

Fetches processor types. Note that we don't use ListProcessorTypes here, because it isn't paginated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       FetchProcessorTypesResponse response =
           documentProcessorServiceClient.fetchProcessorTypes(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.LocationName`  
Required. The location of processor types to list. Format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[FetchProcessorTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.FetchProcessorTypesResponse)` |   
  
### fetchProcessorTypes(FetchProcessorTypesRequest request)
    
    
    public final FetchProcessorTypesResponse fetchProcessorTypes(FetchProcessorTypesRequest request)

Fetches processor types. Note that we don't use ListProcessorTypes here, because it isn't paginated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       FetchProcessorTypesRequest request =
           FetchProcessorTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       FetchProcessorTypesResponse response =
           documentProcessorServiceClient.fetchProcessorTypes(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchProcessorTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.FetchProcessorTypesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchProcessorTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.FetchProcessorTypesResponse)` |   
  
### fetchProcessorTypes(String parent)
    
    
    public final FetchProcessorTypesResponse fetchProcessorTypes(String parent)

Fetches processor types. Note that we don't use ListProcessorTypes here, because it isn't paginated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       FetchProcessorTypesResponse response =
           documentProcessorServiceClient.fetchProcessorTypes(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location of processor types to list. Format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[FetchProcessorTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.FetchProcessorTypesResponse)` |   
  
### fetchProcessorTypesCallable()
    
    
    public final UnaryCallable<FetchProcessorTypesRequest,FetchProcessorTypesResponse> fetchProcessorTypesCallable()

Fetches processor types. Note that we don't use ListProcessorTypes here, because it isn't paginated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       FetchProcessorTypesRequest request =
           FetchProcessorTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<FetchProcessorTypesResponse> future =
           documentProcessorServiceClient.fetchProcessorTypesCallable().futureCall(request);
       // Do something.
       FetchProcessorTypesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchProcessorTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.FetchProcessorTypesRequest),[FetchProcessorTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.FetchProcessorTypesResponse)>` |   
  
### getEvaluation(@Nullable EvaluationName name)
    
    
    public final Evaluation getEvaluation(@Nullable EvaluationName name)

Retrieves a specific evaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       EvaluationName name =
           EvaluationName.of(
               "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]", "[EVALUATION]");
       Evaluation response = documentProcessorServiceClient.getEvaluation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.EvaluationName`  
Required. The resource name of the Evaluation to get. `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}/evaluations/{evaluation}`  
**Returns**  
---  
**Type** | **Description**  
`[Evaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Evaluation)` |   
  
### getEvaluation(GetEvaluationRequest request)
    
    
    public final Evaluation getEvaluation(GetEvaluationRequest request)

Retrieves a specific evaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       GetEvaluationRequest request =
           GetEvaluationRequest.newBuilder()
               .setName(
                   EvaluationName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[PROCESSOR]",
                           "[PROCESSOR_VERSION]",
                           "[EVALUATION]")
                       .toString())
               .build();
       Evaluation response = documentProcessorServiceClient.getEvaluation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GetEvaluationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Evaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Evaluation)` |   
  
### getEvaluation(String name)
    
    
    public final Evaluation getEvaluation(String name)

Retrieves a specific evaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String name =
           EvaluationName.of(
                   "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]", "[EVALUATION]")
               .toString();
       Evaluation response = documentProcessorServiceClient.getEvaluation(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Evaluation to get. `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}/evaluations/{evaluation}`  
**Returns**  
---  
**Type** | **Description**  
`[Evaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Evaluation)` |   
  
### getEvaluationCallable()
    
    
    public final UnaryCallable<GetEvaluationRequest,Evaluation> getEvaluationCallable()

Retrieves a specific evaluation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       GetEvaluationRequest request =
           GetEvaluationRequest.newBuilder()
               .setName(
                   EvaluationName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[PROCESSOR]",
                           "[PROCESSOR_VERSION]",
                           "[EVALUATION]")
                       .toString())
               .build();
       ApiFuture<Evaluation> future =
           documentProcessorServiceClient.getEvaluationCallable().futureCall(request);
       // Do something.
       Evaluation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GetEvaluationRequest),[Evaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Evaluation)>` |   
  
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
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = documentProcessorServiceClient.getLocation(request);
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
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           documentProcessorServiceClient.getLocationCallable().futureCall(request);
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
  
### getProcessor(@Nullable ProcessorName name)
    
    
    public final Processor getProcessor(@Nullable ProcessorName name)

Gets a processor detail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ProcessorName name = ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]");
       Processor response = documentProcessorServiceClient.getProcessor(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.ProcessorName`  
Required. The processor resource name.  
**Returns**  
---  
**Type** | **Description**  
`[Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor)` |   
  
### getProcessor(GetProcessorRequest request)
    
    
    public final Processor getProcessor(GetProcessorRequest request)

Gets a processor detail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       GetProcessorRequest request =
           GetProcessorRequest.newBuilder()
               .setName(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .build();
       Processor response = documentProcessorServiceClient.getProcessor(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GetProcessorRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor)` |   
  
### getProcessor(String name)
    
    
    public final Processor getProcessor(String name)

Gets a processor detail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String name = ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString();
       Processor response = documentProcessorServiceClient.getProcessor(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The processor resource name.  
**Returns**  
---  
**Type** | **Description**  
`[Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor)` |   
  
### getProcessorCallable()
    
    
    public final UnaryCallable<GetProcessorRequest,Processor> getProcessorCallable()

Gets a processor detail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       GetProcessorRequest request =
           GetProcessorRequest.newBuilder()
               .setName(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .build();
       ApiFuture<Processor> future =
           documentProcessorServiceClient.getProcessorCallable().futureCall(request);
       // Do something.
       Processor response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetProcessorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GetProcessorRequest),[Processor](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Processor)>` |   
  
### getProcessorType(@Nullable ProcessorTypeName name)
    
    
    public final ProcessorType getProcessorType(@Nullable ProcessorTypeName name)

Gets a processor type detail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ProcessorTypeName name = ProcessorTypeName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR_TYPE]");
       ProcessorType response = documentProcessorServiceClient.getProcessorType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.ProcessorTypeName`  
Required. The processor type resource name.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorType](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorType)` |   
  
### getProcessorType(GetProcessorTypeRequest request)
    
    
    public final ProcessorType getProcessorType(GetProcessorTypeRequest request)

Gets a processor type detail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       GetProcessorTypeRequest request =
           GetProcessorTypeRequest.newBuilder()
               .setName(
                   ProcessorTypeName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR_TYPE]").toString())
               .build();
       ProcessorType response = documentProcessorServiceClient.getProcessorType(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetProcessorTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GetProcessorTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorType](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorType)` |   
  
### getProcessorType(String name)
    
    
    public final ProcessorType getProcessorType(String name)

Gets a processor type detail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String name = ProcessorTypeName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR_TYPE]").toString();
       ProcessorType response = documentProcessorServiceClient.getProcessorType(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The processor type resource name.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorType](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorType)` |   
  
### getProcessorTypeCallable()
    
    
    public final UnaryCallable<GetProcessorTypeRequest,ProcessorType> getProcessorTypeCallable()

Gets a processor type detail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       GetProcessorTypeRequest request =
           GetProcessorTypeRequest.newBuilder()
               .setName(
                   ProcessorTypeName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR_TYPE]").toString())
               .build();
       ApiFuture<ProcessorType> future =
           documentProcessorServiceClient.getProcessorTypeCallable().futureCall(request);
       // Do something.
       ProcessorType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetProcessorTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GetProcessorTypeRequest),[ProcessorType](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorType)>` |   
  
### getProcessorVersion(@Nullable ProcessorVersionName name)
    
    
    public final ProcessorVersion getProcessorVersion(@Nullable ProcessorVersionName name)

Gets a processor version detail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ProcessorVersionName name =
           ProcessorVersionName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]");
       ProcessorVersion response = documentProcessorServiceClient.getProcessorVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.ProcessorVersionName`  
Required. The processor resource name.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion)` |   
  
### getProcessorVersion(GetProcessorVersionRequest request)
    
    
    public final ProcessorVersion getProcessorVersion(GetProcessorVersionRequest request)

Gets a processor version detail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       GetProcessorVersionRequest request =
           GetProcessorVersionRequest.newBuilder()
               .setName(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .build();
       ProcessorVersion response = documentProcessorServiceClient.getProcessorVersion(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GetProcessorVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion)` |   
  
### getProcessorVersion(String name)
    
    
    public final ProcessorVersion getProcessorVersion(String name)

Gets a processor version detail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String name =
           ProcessorVersionName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
               .toString();
       ProcessorVersion response = documentProcessorServiceClient.getProcessorVersion(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The processor resource name.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion)` |   
  
### getProcessorVersionCallable()
    
    
    public final UnaryCallable<GetProcessorVersionRequest,ProcessorVersion> getProcessorVersionCallable()

Gets a processor version detail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       GetProcessorVersionRequest request =
           GetProcessorVersionRequest.newBuilder()
               .setName(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .build();
       ApiFuture<ProcessorVersion> future =
           documentProcessorServiceClient.getProcessorVersionCallable().futureCall(request);
       // Do something.
       ProcessorVersion response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.GetProcessorVersionRequest),[ProcessorVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion)>` |   
  
### getSettings()
    
    
    public final @Nullable DocumentProcessorServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.DocumentProcessorServiceSettings` |   
  
### getStub()
    
    
    public DocumentProcessorServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.stub.DocumentProcessorServiceStub)` |   
  
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
  
### listEvaluations(@Nullable ProcessorVersionName parent)
    
    
    public final DocumentProcessorServiceClient.ListEvaluationsPagedResponse listEvaluations(@Nullable ProcessorVersionName parent)

Retrieves a set of evaluations for a given processor version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ProcessorVersionName parent =
           ProcessorVersionName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]");
       for (Evaluation element :
           documentProcessorServiceClient.listEvaluations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.ProcessorVersionName`  
Required. The resource name of the ProcessorVersion to list evaluations for. `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}`  
**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorServiceClient.ListEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListEvaluationsPagedResponse)` |   
  
### listEvaluations(ListEvaluationsRequest request)
    
    
    public final DocumentProcessorServiceClient.ListEvaluationsPagedResponse listEvaluations(ListEvaluationsRequest request)

Retrieves a set of evaluations for a given processor version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ListEvaluationsRequest request =
           ListEvaluationsRequest.newBuilder()
               .setParent(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Evaluation element :
           documentProcessorServiceClient.listEvaluations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListEvaluationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorServiceClient.ListEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListEvaluationsPagedResponse)` |   
  
### listEvaluations(String parent)
    
    
    public final DocumentProcessorServiceClient.ListEvaluationsPagedResponse listEvaluations(String parent)

Retrieves a set of evaluations for a given processor version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String parent =
           ProcessorVersionName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
               .toString();
       for (Evaluation element :
           documentProcessorServiceClient.listEvaluations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ProcessorVersion to list evaluations for. `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}`  
**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorServiceClient.ListEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListEvaluationsPagedResponse)` |   
  
### listEvaluationsCallable()
    
    
    public final UnaryCallable<ListEvaluationsRequest,ListEvaluationsResponse> listEvaluationsCallable()

Retrieves a set of evaluations for a given processor version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ListEvaluationsRequest request =
           ListEvaluationsRequest.newBuilder()
               .setParent(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListEvaluationsResponse response =
             documentProcessorServiceClient.listEvaluationsCallable().call(request);
         for (Evaluation element : response.getEvaluationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListEvaluationsRequest),[ListEvaluationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListEvaluationsResponse)>` |   
  
### listEvaluationsPagedCallable()
    
    
    public final UnaryCallable<ListEvaluationsRequest,DocumentProcessorServiceClient.ListEvaluationsPagedResponse> listEvaluationsPagedCallable()

Retrieves a set of evaluations for a given processor version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ListEvaluationsRequest request =
           ListEvaluationsRequest.newBuilder()
               .setParent(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Evaluation> future =
           documentProcessorServiceClient.listEvaluationsPagedCallable().futureCall(request);
       // Do something.
       for (Evaluation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListEvaluationsRequest),[ListEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListEvaluationsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final DocumentProcessorServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : documentProcessorServiceClient.listLocations(request).iterateAll()) {
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
`[DocumentProcessorServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             documentProcessorServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,DocumentProcessorServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           documentProcessorServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListLocationsPagedResponse)>` |   
  
### listProcessorTypes(@Nullable LocationName parent)
    
    
    public final DocumentProcessorServiceClient.ListProcessorTypesPagedResponse listProcessorTypes(@Nullable LocationName parent)

Lists the processor types that exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ProcessorType element :
           documentProcessorServiceClient.listProcessorTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.LocationName`  
Required. The location of processor types to list. Format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorServiceClient.ListProcessorTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListProcessorTypesPagedResponse)` |   
  
### listProcessorTypes(ListProcessorTypesRequest request)
    
    
    public final DocumentProcessorServiceClient.ListProcessorTypesPagedResponse listProcessorTypes(ListProcessorTypesRequest request)

Lists the processor types that exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ListProcessorTypesRequest request =
           ListProcessorTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ProcessorType element :
           documentProcessorServiceClient.listProcessorTypes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListProcessorTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListProcessorTypesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorServiceClient.ListProcessorTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListProcessorTypesPagedResponse)` |   
  
### listProcessorTypes(String parent)
    
    
    public final DocumentProcessorServiceClient.ListProcessorTypesPagedResponse listProcessorTypes(String parent)

Lists the processor types that exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ProcessorType element :
           documentProcessorServiceClient.listProcessorTypes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location of processor types to list. Format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorServiceClient.ListProcessorTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListProcessorTypesPagedResponse)` |   
  
### listProcessorTypesCallable()
    
    
    public final UnaryCallable<ListProcessorTypesRequest,ListProcessorTypesResponse> listProcessorTypesCallable()

Lists the processor types that exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ListProcessorTypesRequest request =
           ListProcessorTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListProcessorTypesResponse response =
             documentProcessorServiceClient.listProcessorTypesCallable().call(request);
         for (ProcessorType element : response.getProcessorTypesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProcessorTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListProcessorTypesRequest),[ListProcessorTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListProcessorTypesResponse)>` |   
  
### listProcessorTypesPagedCallable()
    
    
    public final UnaryCallable<ListProcessorTypesRequest,DocumentProcessorServiceClient.ListProcessorTypesPagedResponse> listProcessorTypesPagedCallable()

Lists the processor types that exist.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ListProcessorTypesRequest request =
           ListProcessorTypesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ProcessorType> future =
           documentProcessorServiceClient.listProcessorTypesPagedCallable().futureCall(request);
       // Do something.
       for (ProcessorType element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProcessorTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListProcessorTypesRequest),[ListProcessorTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListProcessorTypesPagedResponse)>` |   
  
### listProcessorVersions(@Nullable ProcessorName parent)
    
    
    public final DocumentProcessorServiceClient.ListProcessorVersionsPagedResponse listProcessorVersions(@Nullable ProcessorName parent)

Lists all versions of a processor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ProcessorName parent = ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]");
       for (ProcessorVersion element :
           documentProcessorServiceClient.listProcessorVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.ProcessorName`  
Required. The parent (project, location and processor) to list all versions. Format: `projects/{project}/locations/{location}/processors/{processor}`  
**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorServiceClient.ListProcessorVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListProcessorVersionsPagedResponse)` |   
  
### listProcessorVersions(ListProcessorVersionsRequest request)
    
    
    public final DocumentProcessorServiceClient.ListProcessorVersionsPagedResponse listProcessorVersions(ListProcessorVersionsRequest request)

Lists all versions of a processor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ListProcessorVersionsRequest request =
           ListProcessorVersionsRequest.newBuilder()
               .setParent(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ProcessorVersion element :
           documentProcessorServiceClient.listProcessorVersions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListProcessorVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListProcessorVersionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorServiceClient.ListProcessorVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListProcessorVersionsPagedResponse)` |   
  
### listProcessorVersions(String parent)
    
    
    public final DocumentProcessorServiceClient.ListProcessorVersionsPagedResponse listProcessorVersions(String parent)

Lists all versions of a processor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String parent = ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString();
       for (ProcessorVersion element :
           documentProcessorServiceClient.listProcessorVersions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent (project, location and processor) to list all versions. Format: `projects/{project}/locations/{location}/processors/{processor}`  
**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorServiceClient.ListProcessorVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListProcessorVersionsPagedResponse)` |   
  
### listProcessorVersionsCallable()
    
    
    public final UnaryCallable<ListProcessorVersionsRequest,ListProcessorVersionsResponse> listProcessorVersionsCallable()

Lists all versions of a processor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ListProcessorVersionsRequest request =
           ListProcessorVersionsRequest.newBuilder()
               .setParent(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListProcessorVersionsResponse response =
             documentProcessorServiceClient.listProcessorVersionsCallable().call(request);
         for (ProcessorVersion element : response.getProcessorVersionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProcessorVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListProcessorVersionsRequest),[ListProcessorVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListProcessorVersionsResponse)>` |   
  
### listProcessorVersionsPagedCallable()
    
    
    public final UnaryCallable<ListProcessorVersionsRequest,DocumentProcessorServiceClient.ListProcessorVersionsPagedResponse> listProcessorVersionsPagedCallable()

Lists all versions of a processor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ListProcessorVersionsRequest request =
           ListProcessorVersionsRequest.newBuilder()
               .setParent(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ProcessorVersion> future =
           documentProcessorServiceClient.listProcessorVersionsPagedCallable().futureCall(request);
       // Do something.
       for (ProcessorVersion element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProcessorVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListProcessorVersionsRequest),[ListProcessorVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListProcessorVersionsPagedResponse)>` |   
  
### listProcessors(@Nullable LocationName parent)
    
    
    public final DocumentProcessorServiceClient.ListProcessorsPagedResponse listProcessors(@Nullable LocationName parent)

Lists all processors which belong to this project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Processor element : documentProcessorServiceClient.listProcessors(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.LocationName`  
Required. The parent (project and location) which owns this collection of Processors. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorServiceClient.ListProcessorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListProcessorsPagedResponse)` |   
  
### listProcessors(ListProcessorsRequest request)
    
    
    public final DocumentProcessorServiceClient.ListProcessorsPagedResponse listProcessors(ListProcessorsRequest request)

Lists all processors which belong to this project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ListProcessorsRequest request =
           ListProcessorsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Processor element :
           documentProcessorServiceClient.listProcessors(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListProcessorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListProcessorsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorServiceClient.ListProcessorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListProcessorsPagedResponse)` |   
  
### listProcessors(String parent)
    
    
    public final DocumentProcessorServiceClient.ListProcessorsPagedResponse listProcessors(String parent)

Lists all processors which belong to this project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Processor element : documentProcessorServiceClient.listProcessors(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent (project and location) which owns this collection of Processors. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorServiceClient.ListProcessorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListProcessorsPagedResponse)` |   
  
### listProcessorsCallable()
    
    
    public final UnaryCallable<ListProcessorsRequest,ListProcessorsResponse> listProcessorsCallable()

Lists all processors which belong to this project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ListProcessorsRequest request =
           ListProcessorsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListProcessorsResponse response =
             documentProcessorServiceClient.listProcessorsCallable().call(request);
         for (Processor element : response.getProcessorsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProcessorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListProcessorsRequest),[ListProcessorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListProcessorsResponse)>` |   
  
### listProcessorsPagedCallable()
    
    
    public final UnaryCallable<ListProcessorsRequest,DocumentProcessorServiceClient.ListProcessorsPagedResponse> listProcessorsPagedCallable()

Lists all processors which belong to this project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ListProcessorsRequest request =
           ListProcessorsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Processor> future =
           documentProcessorServiceClient.listProcessorsPagedCallable().futureCall(request);
       // Do something.
       for (Processor element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListProcessorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ListProcessorsRequest),[ListProcessorsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentProcessorServiceClient.ListProcessorsPagedResponse)>` |   
  
### processDocument(@Nullable ResourceName name)
    
    
    public final ProcessResponse processDocument(@Nullable ResourceName name)

Processes a single document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ResourceName name = ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]");
       ProcessResponse response = documentProcessorServiceClient.processDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.api.resourcenames.ResourceName`  
Required. The resource name of the Processor or ProcessorVersion to use for processing. If a Processor is specified, the server will use its default version. Format: `projects/{project}/locations/{location}/processors/{processor}`, or `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}`  
**Returns**  
---  
**Type** | **Description**  
`[ProcessResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessResponse)` |   
  
### processDocument(ProcessRequest request)
    
    
    public final ProcessResponse processDocument(ProcessRequest request)

Processes a single document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ProcessRequest request =
           ProcessRequest.newBuilder()
               .setName(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setSkipHumanReview(true)
               .setFieldMask(FieldMask.newBuilder().build())
               .setProcessOptions(ProcessOptions.newBuilder().build())
               .putAllLabels(new HashMap<String, String>())
               .setImagelessMode(true)
               .build();
       ProcessResponse response = documentProcessorServiceClient.processDocument(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessResponse)` |   
  
### processDocument(String name)
    
    
    public final ProcessResponse processDocument(String name)

Processes a single document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String name =
           EvaluationName.of(
                   "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]", "[EVALUATION]")
               .toString();
       ProcessResponse response = documentProcessorServiceClient.processDocument(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Processor or ProcessorVersion to use for processing. If a Processor is specified, the server will use its default version. Format: `projects/{project}/locations/{location}/processors/{processor}`, or `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}`  
**Returns**  
---  
**Type** | **Description**  
`[ProcessResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessResponse)` |   
  
### processDocumentCallable()
    
    
    public final UnaryCallable<ProcessRequest,ProcessResponse> processDocumentCallable()

Processes a single document.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ProcessRequest request =
           ProcessRequest.newBuilder()
               .setName(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setSkipHumanReview(true)
               .setFieldMask(FieldMask.newBuilder().build())
               .setProcessOptions(ProcessOptions.newBuilder().build())
               .putAllLabels(new HashMap<String, String>())
               .setImagelessMode(true)
               .build();
       ApiFuture<ProcessResponse> future =
           documentProcessorServiceClient.processDocumentCallable().futureCall(request);
       // Do something.
       ProcessResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessRequest),[ProcessResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessResponse)>` |   
  
### reviewDocumentAsync(@Nullable HumanReviewConfigName humanReviewConfig)
    
    
    public final OperationFuture<ReviewDocumentResponse,ReviewDocumentOperationMetadata> reviewDocumentAsync(@Nullable HumanReviewConfigName humanReviewConfig)

Send a document for Human Review. The input document should be processed by the specified processor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       HumanReviewConfigName humanReviewConfig =
           HumanReviewConfigName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]");
       ReviewDocumentResponse response =
           documentProcessorServiceClient.reviewDocumentAsync(humanReviewConfig).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`humanReviewConfig` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.HumanReviewConfigName`  
Required. The resource name of the HumanReviewConfig that the document will be reviewed with.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ReviewDocumentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ReviewDocumentResponse),[ReviewDocumentOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ReviewDocumentOperationMetadata)>` |   
  
### reviewDocumentAsync(ReviewDocumentRequest request)
    
    
    public final OperationFuture<ReviewDocumentResponse,ReviewDocumentOperationMetadata> reviewDocumentAsync(ReviewDocumentRequest request)

Send a document for Human Review. The input document should be processed by the specified processor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ReviewDocumentRequest request =
           ReviewDocumentRequest.newBuilder()
               .setHumanReviewConfig(
                   HumanReviewConfigName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setEnableSchemaValidation(true)
               .setDocumentSchema(DocumentSchema.newBuilder().build())
               .build();
       ReviewDocumentResponse response =
           documentProcessorServiceClient.reviewDocumentAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReviewDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ReviewDocumentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ReviewDocumentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ReviewDocumentResponse),[ReviewDocumentOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ReviewDocumentOperationMetadata)>` |   
  
### reviewDocumentAsync(String humanReviewConfig)
    
    
    public final OperationFuture<ReviewDocumentResponse,ReviewDocumentOperationMetadata> reviewDocumentAsync(String humanReviewConfig)

Send a document for Human Review. The input document should be processed by the specified processor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String humanReviewConfig =
           HumanReviewConfigName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString();
       ReviewDocumentResponse response =
           documentProcessorServiceClient.reviewDocumentAsync(humanReviewConfig).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`humanReviewConfig` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the HumanReviewConfig that the document will be reviewed with.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ReviewDocumentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ReviewDocumentResponse),[ReviewDocumentOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ReviewDocumentOperationMetadata)>` |   
  
### reviewDocumentCallable()
    
    
    public final UnaryCallable<ReviewDocumentRequest,Operation> reviewDocumentCallable()

Send a document for Human Review. The input document should be processed by the specified processor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ReviewDocumentRequest request =
           ReviewDocumentRequest.newBuilder()
               .setHumanReviewConfig(
                   HumanReviewConfigName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setEnableSchemaValidation(true)
               .setDocumentSchema(DocumentSchema.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           documentProcessorServiceClient.reviewDocumentCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReviewDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ReviewDocumentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### reviewDocumentOperationCallable()
    
    
    public final OperationCallable<ReviewDocumentRequest,ReviewDocumentResponse,ReviewDocumentOperationMetadata> reviewDocumentOperationCallable()

Send a document for Human Review. The input document should be processed by the specified processor.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ReviewDocumentRequest request =
           ReviewDocumentRequest.newBuilder()
               .setHumanReviewConfig(
                   HumanReviewConfigName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setEnableSchemaValidation(true)
               .setDocumentSchema(DocumentSchema.newBuilder().build())
               .build();
       OperationFuture<ReviewDocumentResponse, ReviewDocumentOperationMetadata> future =
           documentProcessorServiceClient.reviewDocumentOperationCallable().futureCall(request);
       // Do something.
       ReviewDocumentResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ReviewDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ReviewDocumentRequest),[ReviewDocumentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ReviewDocumentResponse),[ReviewDocumentOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ReviewDocumentOperationMetadata)>` |   
  
### setDefaultProcessorVersionAsync(SetDefaultProcessorVersionRequest request)
    
    
    public final OperationFuture<SetDefaultProcessorVersionResponse,SetDefaultProcessorVersionMetadata> setDefaultProcessorVersionAsync(SetDefaultProcessorVersionRequest request)

Set the default (active) version of a Processor that will be used in ProcessDocument and BatchProcessDocuments.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       SetDefaultProcessorVersionRequest request =
           SetDefaultProcessorVersionRequest.newBuilder()
               .setProcessor(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setDefaultProcessorVersion(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .build();
       SetDefaultProcessorVersionResponse response =
           documentProcessorServiceClient.setDefaultProcessorVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetDefaultProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.SetDefaultProcessorVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[SetDefaultProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.SetDefaultProcessorVersionResponse),[SetDefaultProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.SetDefaultProcessorVersionMetadata)>` |   
  
### setDefaultProcessorVersionCallable()
    
    
    public final UnaryCallable<SetDefaultProcessorVersionRequest,Operation> setDefaultProcessorVersionCallable()

Set the default (active) version of a Processor that will be used in ProcessDocument and BatchProcessDocuments.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       SetDefaultProcessorVersionRequest request =
           SetDefaultProcessorVersionRequest.newBuilder()
               .setProcessor(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setDefaultProcessorVersion(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           documentProcessorServiceClient.setDefaultProcessorVersionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetDefaultProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.SetDefaultProcessorVersionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### setDefaultProcessorVersionOperationCallable()
    
    
    public final OperationCallable<SetDefaultProcessorVersionRequest,SetDefaultProcessorVersionResponse,SetDefaultProcessorVersionMetadata> setDefaultProcessorVersionOperationCallable()

Set the default (active) version of a Processor that will be used in ProcessDocument and BatchProcessDocuments.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       SetDefaultProcessorVersionRequest request =
           SetDefaultProcessorVersionRequest.newBuilder()
               .setProcessor(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setDefaultProcessorVersion(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .build();
       OperationFuture<SetDefaultProcessorVersionResponse, SetDefaultProcessorVersionMetadata>
           future =
               documentProcessorServiceClient
                   .setDefaultProcessorVersionOperationCallable()
                   .futureCall(request);
       // Do something.
       SetDefaultProcessorVersionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetDefaultProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.SetDefaultProcessorVersionRequest),[SetDefaultProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.SetDefaultProcessorVersionResponse),[SetDefaultProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.SetDefaultProcessorVersionMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### trainProcessorVersionAsync(@Nullable ProcessorName parent, ProcessorVersion processorVersion)
    
    
    public final OperationFuture<TrainProcessorVersionResponse,TrainProcessorVersionMetadata> trainProcessorVersionAsync(@Nullable ProcessorName parent, ProcessorVersion processorVersion)

Trains a new processor version. Operation metadata is returned as TrainProcessorVersionMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ProcessorName parent = ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]");
       ProcessorVersion processorVersion = ProcessorVersion.newBuilder().build();
       TrainProcessorVersionResponse response =
           documentProcessorServiceClient.trainProcessorVersionAsync(parent, processorVersion).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.ProcessorName`  
Required. The parent (project, location and processor) to create the new version for. Format: `projects/{project}/locations/{location}/processors/{processor}`.  
`processorVersion` | `[ProcessorVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion)`  
Required. The processor version to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TrainProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.TrainProcessorVersionResponse),[TrainProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.TrainProcessorVersionMetadata)>` |   
  
### trainProcessorVersionAsync(TrainProcessorVersionRequest request)
    
    
    public final OperationFuture<TrainProcessorVersionResponse,TrainProcessorVersionMetadata> trainProcessorVersionAsync(TrainProcessorVersionRequest request)

Trains a new processor version. Operation metadata is returned as TrainProcessorVersionMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       TrainProcessorVersionRequest request =
           TrainProcessorVersionRequest.newBuilder()
               .setParent(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setProcessorVersion(ProcessorVersion.newBuilder().build())
               .setDocumentSchema(DocumentSchema.newBuilder().build())
               .setInputData(TrainProcessorVersionRequest.InputData.newBuilder().build())
               .setBaseProcessorVersion("baseProcessorVersion337709271")
               .build();
       TrainProcessorVersionResponse response =
           documentProcessorServiceClient.trainProcessorVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TrainProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.TrainProcessorVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TrainProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.TrainProcessorVersionResponse),[TrainProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.TrainProcessorVersionMetadata)>` |   
  
### trainProcessorVersionAsync(String parent, ProcessorVersion processorVersion)
    
    
    public final OperationFuture<TrainProcessorVersionResponse,TrainProcessorVersionMetadata> trainProcessorVersionAsync(String parent, ProcessorVersion processorVersion)

Trains a new processor version. Operation metadata is returned as TrainProcessorVersionMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String parent = ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString();
       ProcessorVersion processorVersion = ProcessorVersion.newBuilder().build();
       TrainProcessorVersionResponse response =
           documentProcessorServiceClient.trainProcessorVersionAsync(parent, processorVersion).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent (project, location and processor) to create the new version for. Format: `projects/{project}/locations/{location}/processors/{processor}`.  
`processorVersion` | `[ProcessorVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion)`  
Required. The processor version to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TrainProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.TrainProcessorVersionResponse),[TrainProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.TrainProcessorVersionMetadata)>` |   
  
### trainProcessorVersionCallable()
    
    
    public final UnaryCallable<TrainProcessorVersionRequest,Operation> trainProcessorVersionCallable()

Trains a new processor version. Operation metadata is returned as TrainProcessorVersionMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       TrainProcessorVersionRequest request =
           TrainProcessorVersionRequest.newBuilder()
               .setParent(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setProcessorVersion(ProcessorVersion.newBuilder().build())
               .setDocumentSchema(DocumentSchema.newBuilder().build())
               .setInputData(TrainProcessorVersionRequest.InputData.newBuilder().build())
               .setBaseProcessorVersion("baseProcessorVersion337709271")
               .build();
       ApiFuture<Operation> future =
           documentProcessorServiceClient.trainProcessorVersionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TrainProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.TrainProcessorVersionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### trainProcessorVersionOperationCallable()
    
    
    public final OperationCallable<TrainProcessorVersionRequest,TrainProcessorVersionResponse,TrainProcessorVersionMetadata> trainProcessorVersionOperationCallable()

Trains a new processor version. Operation metadata is returned as TrainProcessorVersionMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       TrainProcessorVersionRequest request =
           TrainProcessorVersionRequest.newBuilder()
               .setParent(ProcessorName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]").toString())
               .setProcessorVersion(ProcessorVersion.newBuilder().build())
               .setDocumentSchema(DocumentSchema.newBuilder().build())
               .setInputData(TrainProcessorVersionRequest.InputData.newBuilder().build())
               .setBaseProcessorVersion("baseProcessorVersion337709271")
               .build();
       OperationFuture<TrainProcessorVersionResponse, TrainProcessorVersionMetadata> future =
           documentProcessorServiceClient
               .trainProcessorVersionOperationCallable()
               .futureCall(request);
       // Do something.
       TrainProcessorVersionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[TrainProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.TrainProcessorVersionRequest),[TrainProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.TrainProcessorVersionResponse),[TrainProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.TrainProcessorVersionMetadata)>` |   
  
### undeployProcessorVersionAsync(@Nullable ProcessorVersionName name)
    
    
    public final OperationFuture<UndeployProcessorVersionResponse,UndeployProcessorVersionMetadata> undeployProcessorVersionAsync(@Nullable ProcessorVersionName name)

Undeploys the processor version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       ProcessorVersionName name =
           ProcessorVersionName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]");
       UndeployProcessorVersionResponse response =
           documentProcessorServiceClient.undeployProcessorVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.documentai.v1.ProcessorVersionName`  
Required. The processor version resource name to be undeployed.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UndeployProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.UndeployProcessorVersionResponse),[UndeployProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.UndeployProcessorVersionMetadata)>` |   
  
### undeployProcessorVersionAsync(UndeployProcessorVersionRequest request)
    
    
    public final OperationFuture<UndeployProcessorVersionResponse,UndeployProcessorVersionMetadata> undeployProcessorVersionAsync(UndeployProcessorVersionRequest request)

Undeploys the processor version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       UndeployProcessorVersionRequest request =
           UndeployProcessorVersionRequest.newBuilder()
               .setName(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .build();
       UndeployProcessorVersionResponse response =
           documentProcessorServiceClient.undeployProcessorVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UndeployProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.UndeployProcessorVersionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UndeployProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.UndeployProcessorVersionResponse),[UndeployProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.UndeployProcessorVersionMetadata)>` |   
  
### undeployProcessorVersionAsync(String name)
    
    
    public final OperationFuture<UndeployProcessorVersionResponse,UndeployProcessorVersionMetadata> undeployProcessorVersionAsync(String name)

Undeploys the processor version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       String name =
           ProcessorVersionName.of("[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
               .toString();
       UndeployProcessorVersionResponse response =
           documentProcessorServiceClient.undeployProcessorVersionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The processor version resource name to be undeployed.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UndeployProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.UndeployProcessorVersionResponse),[UndeployProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.UndeployProcessorVersionMetadata)>` |   
  
### undeployProcessorVersionCallable()
    
    
    public final UnaryCallable<UndeployProcessorVersionRequest,Operation> undeployProcessorVersionCallable()

Undeploys the processor version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       UndeployProcessorVersionRequest request =
           UndeployProcessorVersionRequest.newBuilder()
               .setName(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           documentProcessorServiceClient.undeployProcessorVersionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UndeployProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.UndeployProcessorVersionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### undeployProcessorVersionOperationCallable()
    
    
    public final OperationCallable<UndeployProcessorVersionRequest,UndeployProcessorVersionResponse,UndeployProcessorVersionMetadata> undeployProcessorVersionOperationCallable()

Undeploys the processor version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DocumentProcessorServiceClient documentProcessorServiceClient =
         DocumentProcessorServiceClient.create()) {
       UndeployProcessorVersionRequest request =
           UndeployProcessorVersionRequest.newBuilder()
               .setName(
                   ProcessorVersionName.of(
                           "[PROJECT]", "[LOCATION]", "[PROCESSOR]", "[PROCESSOR_VERSION]")
                       .toString())
               .build();
       OperationFuture<UndeployProcessorVersionResponse, UndeployProcessorVersionMetadata> future =
           documentProcessorServiceClient
               .undeployProcessorVersionOperationCallable()
               .futureCall(request);
       // Do something.
       UndeployProcessorVersionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UndeployProcessorVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.UndeployProcessorVersionRequest),[UndeployProcessorVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.UndeployProcessorVersionResponse),[UndeployProcessorVersionMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.UndeployProcessorVersionMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
