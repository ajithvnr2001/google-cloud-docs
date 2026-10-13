---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceGrpc.TranslationServiceBlockingV2Stub
title: Class TranslationServiceGrpc.TranslationServiceBlockingV2Stub (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:48.318883+00:00
---

# Class TranslationServiceGrpc.TranslationServiceBlockingV2Stub (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceGrpc.TranslationServiceBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TranslationServiceGrpc.TranslationServiceBlockingV2Stub (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.5  2.2.0  2.1.13 
    
    
    public static final class TranslationServiceGrpc.TranslationServiceBlockingV2Stub extends AbstractBlockingStub<TranslationServiceGrpc.TranslationServiceBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service TranslationService.

Provides natural language translation operations.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > TranslationServiceGrpc.TranslationServiceBlockingV2Stub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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

### adaptiveMtTranslate(AdaptiveMtTranslateRequest request)
    
    
    public AdaptiveMtTranslateResponse adaptiveMtTranslate(AdaptiveMtTranslateRequest request)

Translate text using Adaptive MT.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AdaptiveMtTranslateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.AdaptiveMtTranslateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdaptiveMtTranslateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.AdaptiveMtTranslateResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### batchTranslateDocument(BatchTranslateDocumentRequest request)
    
    
    public Operation batchTranslateDocument(BatchTranslateDocumentRequest request)

Translates a large volume of document in asynchronous batch mode. This function provides real-time output as the inputs are being processed. If caller cancels a request, the partial results (for an input file, it's all or nothing) may still be available on the specified output location. This call returns immediately and you can use google.longrunning.Operation.name to poll the status of the call.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchTranslateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateDocumentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### batchTranslateText(BatchTranslateTextRequest request)
    
    
    public Operation batchTranslateText(BatchTranslateTextRequest request)

Translates a large volume of text in asynchronous batch mode. This function provides real-time output as the inputs are being processed. If caller cancels a request, the partial results (for an input file, it's all or nothing) may still be available on the specified output location. This call returns immediately and you can use google.longrunning.Operation.name to poll the status of the call.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchTranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.BatchTranslateTextRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected TranslationServiceGrpc.TranslationServiceBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[TranslationServiceGrpc.TranslationServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceGrpc.TranslationServiceBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createAdaptiveMtDataset(CreateAdaptiveMtDatasetRequest request)
    
    
    public AdaptiveMtDataset createAdaptiveMtDataset(CreateAdaptiveMtDatasetRequest request)

Creates an Adaptive MT dataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAdaptiveMtDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.CreateAdaptiveMtDatasetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdaptiveMtDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.AdaptiveMtDataset)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createDataset(CreateDatasetRequest request)
    
    
    public Operation createDataset(CreateDatasetRequest request)

Creates a Dataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.CreateDatasetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createGlossary(CreateGlossaryRequest request)
    
    
    public Operation createGlossary(CreateGlossaryRequest request)

Creates a glossary and returns the long-running operation. Returns NOT_FOUND, if the project doesn't exist.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.CreateGlossaryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createGlossaryEntry(CreateGlossaryEntryRequest request)
    
    
    public GlossaryEntry createGlossaryEntry(CreateGlossaryEntryRequest request)

Creates a glossary entry.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGlossaryEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.CreateGlossaryEntryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryEntry)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createModel(CreateModelRequest request)
    
    
    public Operation createModel(CreateModelRequest request)

Creates a Model.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.CreateModelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteAdaptiveMtDataset(DeleteAdaptiveMtDatasetRequest request)
    
    
    public Empty deleteAdaptiveMtDataset(DeleteAdaptiveMtDatasetRequest request)

Deletes an Adaptive MT dataset, including all its entries and associated metadata.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAdaptiveMtDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DeleteAdaptiveMtDatasetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteAdaptiveMtFile(DeleteAdaptiveMtFileRequest request)
    
    
    public Empty deleteAdaptiveMtFile(DeleteAdaptiveMtFileRequest request)

Deletes an AdaptiveMtFile along with its sentences.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAdaptiveMtFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DeleteAdaptiveMtFileRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteDataset(DeleteDatasetRequest request)
    
    
    public Operation deleteDataset(DeleteDatasetRequest request)

Deletes a dataset and all of its contents.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DeleteDatasetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteGlossary(DeleteGlossaryRequest request)
    
    
    public Operation deleteGlossary(DeleteGlossaryRequest request)

Deletes a glossary, or cancels glossary construction if the glossary isn't created yet. Returns NOT_FOUND, if the glossary doesn't exist.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DeleteGlossaryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteGlossaryEntry(DeleteGlossaryEntryRequest request)
    
    
    public Empty deleteGlossaryEntry(DeleteGlossaryEntryRequest request)

Deletes a single entry from the glossary

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGlossaryEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DeleteGlossaryEntryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteModel(DeleteModelRequest request)
    
    
    public Operation deleteModel(DeleteModelRequest request)

Deletes a model.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DeleteModelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### detectLanguage(DetectLanguageRequest request)
    
    
    public DetectLanguageResponse detectLanguage(DetectLanguageRequest request)

Detects the language of text within a request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DetectLanguageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DetectLanguageRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DetectLanguageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DetectLanguageResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### exportData(ExportDataRequest request)
    
    
    public Operation exportData(ExportDataRequest request)

Exports dataset's data to the provided output location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ExportDataRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getAdaptiveMtDataset(GetAdaptiveMtDatasetRequest request)
    
    
    public AdaptiveMtDataset getAdaptiveMtDataset(GetAdaptiveMtDatasetRequest request)

Gets the Adaptive MT dataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAdaptiveMtDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetAdaptiveMtDatasetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdaptiveMtDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.AdaptiveMtDataset)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getAdaptiveMtFile(GetAdaptiveMtFileRequest request)
    
    
    public AdaptiveMtFile getAdaptiveMtFile(GetAdaptiveMtFileRequest request)

Gets and AdaptiveMtFile

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAdaptiveMtFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetAdaptiveMtFileRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdaptiveMtFile](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.AdaptiveMtFile)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getDataset(GetDatasetRequest request)
    
    
    public Dataset getDataset(GetDatasetRequest request)

Gets a Dataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetDatasetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Dataset)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getGlossary(GetGlossaryRequest request)
    
    
    public Glossary getGlossary(GetGlossaryRequest request)

Gets a glossary. Returns NOT_FOUND, if the glossary doesn't exist.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetGlossaryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getGlossaryEntry(GetGlossaryEntryRequest request)
    
    
    public GlossaryEntry getGlossaryEntry(GetGlossaryEntryRequest request)

Gets a single glossary entry by the given id.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGlossaryEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetGlossaryEntryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryEntry)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getModel(GetModelRequest request)
    
    
    public Model getModel(GetModelRequest request)

Gets a model.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetModelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Model)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getSupportedLanguages(GetSupportedLanguagesRequest request)
    
    
    public SupportedLanguages getSupportedLanguages(GetSupportedLanguagesRequest request)

Returns a list of supported languages for translation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSupportedLanguagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetSupportedLanguagesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SupportedLanguages](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.SupportedLanguages)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### importAdaptiveMtFile(ImportAdaptiveMtFileRequest request)
    
    
    public ImportAdaptiveMtFileResponse importAdaptiveMtFile(ImportAdaptiveMtFileRequest request)

Imports an AdaptiveMtFile and adds all of its sentences into the AdaptiveMtDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportAdaptiveMtFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ImportAdaptiveMtFileRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ImportAdaptiveMtFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ImportAdaptiveMtFileResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### importData(ImportDataRequest request)
    
    
    public Operation importData(ImportDataRequest request)

Import sentence pairs into translation Dataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ImportDataRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listAdaptiveMtDatasets(ListAdaptiveMtDatasetsRequest request)
    
    
    public ListAdaptiveMtDatasetsResponse listAdaptiveMtDatasets(ListAdaptiveMtDatasetsRequest request)

Lists all Adaptive MT datasets for which the caller has read permission.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAdaptiveMtDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListAdaptiveMtDatasetsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListAdaptiveMtDatasetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListAdaptiveMtDatasetsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listAdaptiveMtFiles(ListAdaptiveMtFilesRequest request)
    
    
    public ListAdaptiveMtFilesResponse listAdaptiveMtFiles(ListAdaptiveMtFilesRequest request)

Lists all AdaptiveMtFiles associated to an AdaptiveMtDataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAdaptiveMtFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListAdaptiveMtFilesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListAdaptiveMtFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListAdaptiveMtFilesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listAdaptiveMtSentences(ListAdaptiveMtSentencesRequest request)
    
    
    public ListAdaptiveMtSentencesResponse listAdaptiveMtSentences(ListAdaptiveMtSentencesRequest request)

Lists all AdaptiveMtSentences under a given file/dataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAdaptiveMtSentencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListAdaptiveMtSentencesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListAdaptiveMtSentencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListAdaptiveMtSentencesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listDatasets(ListDatasetsRequest request)
    
    
    public ListDatasetsResponse listDatasets(ListDatasetsRequest request)

Lists datasets.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListDatasetsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListDatasetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListDatasetsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listExamples(ListExamplesRequest request)
    
    
    public ListExamplesResponse listExamples(ListExamplesRequest request)

Lists sentence pairs in the dataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListExamplesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListExamplesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListExamplesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListExamplesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listGlossaries(ListGlossariesRequest request)
    
    
    public ListGlossariesResponse listGlossaries(ListGlossariesRequest request)

Lists glossaries in a project. Returns NOT_FOUND, if the project doesn't exist.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGlossariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListGlossariesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListGlossariesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListGlossariesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listGlossaryEntries(ListGlossaryEntriesRequest request)
    
    
    public ListGlossaryEntriesResponse listGlossaryEntries(ListGlossaryEntriesRequest request)

List the entries for the glossary.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGlossaryEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListGlossaryEntriesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListGlossaryEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListGlossaryEntriesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listModels(ListModelsRequest request)
    
    
    public ListModelsResponse listModels(ListModelsRequest request)

Lists models.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListModelsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListModelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListModelsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### romanizeText(RomanizeTextRequest request)
    
    
    public RomanizeTextResponse romanizeText(RomanizeTextRequest request)

Romanize input text written in non-Latin scripts to Latin text.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RomanizeTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.RomanizeTextRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RomanizeTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.RomanizeTextResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### translateDocument(TranslateDocumentRequest request)
    
    
    public TranslateDocumentResponse translateDocument(TranslateDocumentRequest request)

Translates documents in synchronous mode.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TranslateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateDocumentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TranslateDocumentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateDocumentResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### translateText(TranslateTextRequest request)
    
    
    public TranslateTextResponse translateText(TranslateTextRequest request)

Translates input text and returns translated text.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TranslateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateGlossary(UpdateGlossaryRequest request)
    
    
    public Operation updateGlossary(UpdateGlossaryRequest request)

Updates a glossary. A LRO is used since the update can be async if the glossary's entry file is updated.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.UpdateGlossaryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateGlossaryEntry(UpdateGlossaryEntryRequest request)
    
    
    public GlossaryEntry updateGlossaryEntry(UpdateGlossaryEntryRequest request)

Updates a glossary entry.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGlossaryEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.UpdateGlossaryEntryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GlossaryEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryEntry)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
