---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.PredictionServiceClient
title: Class PredictionServiceClient (2.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:42.699005+00:00
---

# Class PredictionServiceClient (2.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.PredictionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PredictionServiceClient (2.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.95.0 (latest)  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.18  2.2.3  2.1.23 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-automl/google-cloud-automl/src/main/java/com/google/cloud/automl/v1/PredictionServiceClient.java)| [Product Reference](https://cloud.google.com/automl/docs/)| [REST Documentation](https://cloud.google.com/automl/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/automl/docs/reference/rpc)  
---|---|---|---  
  
Service Description: AutoML Prediction API.

On any input that is documented to expect a string parameter in snake_case or dash-case, either of those cases is accepted.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       ExamplePayload payload = ExamplePayload.newBuilder().build();
       Map<String, String> params = new HashMap<>();
       PredictResponse response = predictionServiceClient.predict(name, payload, params);
     }
     

Note: close() needs to be called on the PredictionServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Predict |  Perform an online prediction. The prediction result is directly returned in the response. Available for following ML scenarios, and their expected request payloads:  AutoML Vision Classification 

  * An image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB. 

AutoML Vision Object Detection 

  * An image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB. 

AutoML Natural Language Classification 

  * A TextSnippet up to 60,000 characters, UTF-8 encoded or a document in .PDF, .TIF or .TIFF format with size upto 2MB. 

AutoML Natural Language Entity Extraction 

  * A TextSnippet up to 10,000 characters, UTF-8 NFC encoded or a document in .PDF, .TIF or .TIFF format with size upto 20MB. 

AutoML Natural Language Sentiment Analysis 

  * A TextSnippet up to 60,000 characters, UTF-8 encoded or a document in .PDF, .TIF or .TIFF format with size upto 2MB. 

AutoML Translation 

  * A TextSnippet up to 25,000 characters, UTF-8 encoded. 

AutoML Tables 

  * A row with column values matching the columns of the model, up to 5MB. Not available for FORECASTING `prediction_type`. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * predict(PredictRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * predict(ModelName name, ExamplePayload payload, Map<String, String> params) 
  * predict(String name, ExamplePayload payload, Map<String, String> params) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * predictCallable() 

  
BatchPredict |  Perform a batch prediction. Unlike the online Predict, batch prediction result won't be immediately available in the response. Instead, a long running operation object is returned. User can poll the operation result via GetOperation method. Once the operation is done, BatchPredictResult is returned in the response field. Available for following ML scenarios: 

  * AutoML Vision Classification 
  * AutoML Vision Object Detection 
  * AutoML Video Intelligence Classification 
  * AutoML Video Intelligence Object Tracking * AutoML Natural Language Classification 
  * AutoML Natural Language Entity Extraction 
  * AutoML Natural Language Sentiment Analysis 
  * AutoML Tables 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchPredictAsync(BatchPredictRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * batchPredictAsync(ModelName name, BatchPredictInputConfig inputConfig, BatchPredictOutputConfig outputConfig, Map<String, String> params) 
  * batchPredictAsync(String name, BatchPredictInputConfig inputConfig, BatchPredictOutputConfig outputConfig, Map<String, String> params) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchPredictOperationCallable() 
  * batchPredictCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of PredictionServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PredictionServiceSettings predictionServiceSettings =
         PredictionServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     PredictionServiceClient predictionServiceClient =
         PredictionServiceClient.create(predictionServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PredictionServiceSettings predictionServiceSettings =
         PredictionServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     PredictionServiceClient predictionServiceClient =
         PredictionServiceClient.create(predictionServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PredictionServiceSettings predictionServiceSettings =
         PredictionServiceSettings.newHttpJsonBuilder().build();
     PredictionServiceClient predictionServiceClient =
         PredictionServiceClient.create(predictionServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PredictionServiceClient

## Static Methods 

### create()
    
    
    public static final PredictionServiceClient create()

Constructs an instance of PredictionServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.PredictionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PredictionServiceSettings settings)
    
    
    public static final PredictionServiceClient create(PredictionServiceSettings settings)

Constructs an instance of PredictionServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.PredictionServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.PredictionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PredictionServiceStub stub)
    
    
    public static final PredictionServiceClient create(PredictionServiceStub stub)

Constructs an instance of PredictionServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(PredictionServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PredictionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.stub.PredictionServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PredictionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.PredictionServiceClient)` |   
  
## Constructors 

### PredictionServiceClient(PredictionServiceSettings settings)
    
    
    protected PredictionServiceClient(PredictionServiceSettings settings)

Constructs an instance of PredictionServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PredictionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.PredictionServiceSettings)`  
  
  
### PredictionServiceClient(PredictionServiceStub stub)
    
    
    protected PredictionServiceClient(PredictionServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PredictionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.stub.PredictionServiceStub)`  
  
  
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
  
### batchPredictAsync(@Nullable ModelName name, BatchPredictInputConfig inputConfig, BatchPredictOutputConfig outputConfig, Map<String,String> params)
    
    
    public final OperationFuture<BatchPredictResult,OperationMetadata> batchPredictAsync(@Nullable ModelName name, BatchPredictInputConfig inputConfig, BatchPredictOutputConfig outputConfig, Map<String,String> params)

Perform a batch prediction. Unlike the online Predict, batch prediction result won't be immediately available in the response. Instead, a long running operation object is returned. User can poll the operation result via GetOperation method. Once the operation is done, BatchPredictResult is returned in the response field. Available for following ML scenarios:

  * AutoML Vision Classification 
  * AutoML Vision Object Detection 
  * AutoML Video Intelligence Classification 
  * AutoML Video Intelligence Object Tracking * AutoML Natural Language Classification 
  * AutoML Natural Language Entity Extraction 
  * AutoML Natural Language Sentiment Analysis 
  * AutoML Tables 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       BatchPredictInputConfig inputConfig = BatchPredictInputConfig.newBuilder().build();
       BatchPredictOutputConfig outputConfig = BatchPredictOutputConfig.newBuilder().build();
       Map<String, String> params = new HashMap<>();
       BatchPredictResult response =
           predictionServiceClient.batchPredictAsync(name, inputConfig, outputConfig, params).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.ModelName`  
Required. Name of the model requested to serve the batch prediction.  
`inputConfig` | `[BatchPredictInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.BatchPredictInputConfig)`  
Required. The input configuration for batch prediction.  
`outputConfig` | `[BatchPredictOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.BatchPredictOutputConfig)`  
Required. The Configuration specifying where output predictions should be written.  
`params` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Additional domain-specific parameters for the predictions, any string must be up to 25000 characters long. AutoML Natural Language Classification `score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for a text snippet, it will only produce results that have at least this confidence score. The default is 0.5. AutoML Vision Classification `score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for an image, it will only produce results that have at least this confidence score. The default is 0.5. AutoML Vision Object Detection `score_threshold` : (float) When Model detects objects on the image, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5. `max_bounding_box_count` : (int64) The maximum number of bounding boxes returned per image. The default is 100, the number of bounding boxes returned might be limited by the server. AutoML Video Intelligence Classification `score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for a video, it will only produce results that have at least this confidence score. The default is 0.5. `segment_classification` : (boolean) Set to true to request segment-level classification. AutoML Video Intelligence returns labels and their confidence scores for the entire segment of the video that user specified in the request configuration. The default is true. `shot_classification` : (boolean) Set to true to request shot-level classification. AutoML Video Intelligence determines the boundaries for each camera shot in the entire segment of the video that user specified in the request configuration. AutoML Video Intelligence then returns labels and their confidence scores for each detected shot, along with the start and end time of the shot. The default is false. WARNING: Model evaluation is not done for this classification type, the quality of it depends on training data, but there are no metrics provided to describe that quality. `1s_interval_classification` : (boolean) Set to true to request classification for a video at one-second intervals. AutoML Video Intelligence returns labels and their confidence scores for each second of the entire segment of the video that user specified in the request configuration. The default is false. WARNING: Model evaluation is not done for this classification type, the quality of it depends on training data, but there are no metrics provided to describe that quality. AutoML Video Intelligence Object Tracking `score_threshold` : (float) When Model detects objects on video frames, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5. `max_bounding_box_count` : (int64) The maximum number of bounding boxes returned per image. The default is 100, the number of bounding boxes returned might be limited by the server. `min_bounding_box_size` : (float) Only bounding boxes with shortest edge at least that long as a relative value of video frame size are returned. Value in 0 to 1 range. Default is 0.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchPredictResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.BatchPredictResult),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### batchPredictAsync(BatchPredictRequest request)
    
    
    public final OperationFuture<BatchPredictResult,OperationMetadata> batchPredictAsync(BatchPredictRequest request)

Perform a batch prediction. Unlike the online Predict, batch prediction result won't be immediately available in the response. Instead, a long running operation object is returned. User can poll the operation result via GetOperation method. Once the operation is done, BatchPredictResult is returned in the response field. Available for following ML scenarios:

  * AutoML Vision Classification 
  * AutoML Vision Object Detection 
  * AutoML Video Intelligence Classification 
  * AutoML Video Intelligence Object Tracking * AutoML Natural Language Classification 
  * AutoML Natural Language Entity Extraction 
  * AutoML Natural Language Sentiment Analysis 
  * AutoML Tables 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       BatchPredictRequest request =
           BatchPredictRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setInputConfig(BatchPredictInputConfig.newBuilder().build())
               .setOutputConfig(BatchPredictOutputConfig.newBuilder().build())
               .putAllParams(new HashMap<String, String>())
               .build();
       BatchPredictResult response = predictionServiceClient.batchPredictAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchPredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.BatchPredictRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchPredictResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.BatchPredictResult),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### batchPredictAsync(String name, BatchPredictInputConfig inputConfig, BatchPredictOutputConfig outputConfig, Map<String,String> params)
    
    
    public final OperationFuture<BatchPredictResult,OperationMetadata> batchPredictAsync(String name, BatchPredictInputConfig inputConfig, BatchPredictOutputConfig outputConfig, Map<String,String> params)

Perform a batch prediction. Unlike the online Predict, batch prediction result won't be immediately available in the response. Instead, a long running operation object is returned. User can poll the operation result via GetOperation method. Once the operation is done, BatchPredictResult is returned in the response field. Available for following ML scenarios:

  * AutoML Vision Classification 
  * AutoML Vision Object Detection 
  * AutoML Video Intelligence Classification 
  * AutoML Video Intelligence Object Tracking * AutoML Natural Language Classification 
  * AutoML Natural Language Entity Extraction 
  * AutoML Natural Language Sentiment Analysis 
  * AutoML Tables 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       BatchPredictInputConfig inputConfig = BatchPredictInputConfig.newBuilder().build();
       BatchPredictOutputConfig outputConfig = BatchPredictOutputConfig.newBuilder().build();
       Map<String, String> params = new HashMap<>();
       BatchPredictResult response =
           predictionServiceClient.batchPredictAsync(name, inputConfig, outputConfig, params).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the model requested to serve the batch prediction.  
`inputConfig` | `[BatchPredictInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.BatchPredictInputConfig)`  
Required. The input configuration for batch prediction.  
`outputConfig` | `[BatchPredictOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.BatchPredictOutputConfig)`  
Required. The Configuration specifying where output predictions should be written.  
`params` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Additional domain-specific parameters for the predictions, any string must be up to 25000 characters long. AutoML Natural Language Classification `score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for a text snippet, it will only produce results that have at least this confidence score. The default is 0.5. AutoML Vision Classification `score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for an image, it will only produce results that have at least this confidence score. The default is 0.5. AutoML Vision Object Detection `score_threshold` : (float) When Model detects objects on the image, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5. `max_bounding_box_count` : (int64) The maximum number of bounding boxes returned per image. The default is 100, the number of bounding boxes returned might be limited by the server. AutoML Video Intelligence Classification `score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for a video, it will only produce results that have at least this confidence score. The default is 0.5. `segment_classification` : (boolean) Set to true to request segment-level classification. AutoML Video Intelligence returns labels and their confidence scores for the entire segment of the video that user specified in the request configuration. The default is true. `shot_classification` : (boolean) Set to true to request shot-level classification. AutoML Video Intelligence determines the boundaries for each camera shot in the entire segment of the video that user specified in the request configuration. AutoML Video Intelligence then returns labels and their confidence scores for each detected shot, along with the start and end time of the shot. The default is false. WARNING: Model evaluation is not done for this classification type, the quality of it depends on training data, but there are no metrics provided to describe that quality. `1s_interval_classification` : (boolean) Set to true to request classification for a video at one-second intervals. AutoML Video Intelligence returns labels and their confidence scores for each second of the entire segment of the video that user specified in the request configuration. The default is false. WARNING: Model evaluation is not done for this classification type, the quality of it depends on training data, but there are no metrics provided to describe that quality. AutoML Video Intelligence Object Tracking `score_threshold` : (float) When Model detects objects on video frames, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5. `max_bounding_box_count` : (int64) The maximum number of bounding boxes returned per image. The default is 100, the number of bounding boxes returned might be limited by the server. `min_bounding_box_size` : (float) Only bounding boxes with shortest edge at least that long as a relative value of video frame size are returned. Value in 0 to 1 range. Default is 0.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchPredictResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.BatchPredictResult),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### batchPredictCallable()
    
    
    public final UnaryCallable<BatchPredictRequest,Operation> batchPredictCallable()

Perform a batch prediction. Unlike the online Predict, batch prediction result won't be immediately available in the response. Instead, a long running operation object is returned. User can poll the operation result via GetOperation method. Once the operation is done, BatchPredictResult is returned in the response field. Available for following ML scenarios:

  * AutoML Vision Classification 
  * AutoML Vision Object Detection 
  * AutoML Video Intelligence Classification 
  * AutoML Video Intelligence Object Tracking * AutoML Natural Language Classification 
  * AutoML Natural Language Entity Extraction 
  * AutoML Natural Language Sentiment Analysis 
  * AutoML Tables 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       BatchPredictRequest request =
           BatchPredictRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setInputConfig(BatchPredictInputConfig.newBuilder().build())
               .setOutputConfig(BatchPredictOutputConfig.newBuilder().build())
               .putAllParams(new HashMap<String, String>())
               .build();
       ApiFuture<Operation> future =
           predictionServiceClient.batchPredictCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchPredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.BatchPredictRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchPredictOperationCallable()
    
    
    public final OperationCallable<BatchPredictRequest,BatchPredictResult,OperationMetadata> batchPredictOperationCallable()

Perform a batch prediction. Unlike the online Predict, batch prediction result won't be immediately available in the response. Instead, a long running operation object is returned. User can poll the operation result via GetOperation method. Once the operation is done, BatchPredictResult is returned in the response field. Available for following ML scenarios:

  * AutoML Vision Classification 
  * AutoML Vision Object Detection 
  * AutoML Video Intelligence Classification 
  * AutoML Video Intelligence Object Tracking * AutoML Natural Language Classification 
  * AutoML Natural Language Entity Extraction 
  * AutoML Natural Language Sentiment Analysis 
  * AutoML Tables 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       BatchPredictRequest request =
           BatchPredictRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setInputConfig(BatchPredictInputConfig.newBuilder().build())
               .setOutputConfig(BatchPredictOutputConfig.newBuilder().build())
               .putAllParams(new HashMap<String, String>())
               .build();
       OperationFuture<BatchPredictResult, OperationMetadata> future =
           predictionServiceClient.batchPredictOperationCallable().futureCall(request);
       // Do something.
       BatchPredictResult response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchPredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.BatchPredictRequest),[BatchPredictResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.BatchPredictResult),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.OperationMetadata)>` |   
  
### close()
    
    
    public final void close()

### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable PredictionServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.PredictionServiceSettings` |   
  
### getStub()
    
    
    public PredictionServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[PredictionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.stub.PredictionServiceStub)` |   
  
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
  
### predict(@Nullable ModelName name, ExamplePayload payload, Map<String,String> params)
    
    
    public final PredictResponse predict(@Nullable ModelName name, ExamplePayload payload, Map<String,String> params)

Perform an online prediction. The prediction result is directly returned in the response. Available for following ML scenarios, and their expected request payloads:

AutoML Vision Classification

  * An image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB. 



AutoML Vision Object Detection

  * An image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB. 



AutoML Natural Language Classification

  * A TextSnippet up to 60,000 characters, UTF-8 encoded or a document in .PDF, .TIF or .TIFF format with size upto 2MB. 



AutoML Natural Language Entity Extraction

  * A TextSnippet up to 10,000 characters, UTF-8 NFC encoded or a document in .PDF, .TIF or .TIFF format with size upto 20MB. 



AutoML Natural Language Sentiment Analysis

  * A TextSnippet up to 60,000 characters, UTF-8 encoded or a document in .PDF, .TIF or .TIFF format with size upto 2MB. 



AutoML Translation

  * A TextSnippet up to 25,000 characters, UTF-8 encoded. 



AutoML Tables

  * A row with column values matching the columns of the model, up to 5MB. Not available for FORECASTING `prediction_type`. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       ModelName name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]");
       ExamplePayload payload = ExamplePayload.newBuilder().build();
       Map<String, String> params = new HashMap<>();
       PredictResponse response = predictionServiceClient.predict(name, payload, params);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.automl.v1.ModelName`  
Required. Name of the model requested to serve the prediction.  
`payload` | `[ExamplePayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ExamplePayload)`  
Required. Payload to perform a prediction on. The payload must match the problem type that the model was trained to solve.  
`params` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Additional domain-specific parameters, any string must be up to 25000 characters long. AutoML Vision Classification `score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for an image, it will only produce results that have at least this confidence score. The default is 0.5. AutoML Vision Object Detection `score_threshold` : (float) When Model detects objects on the image, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5. `max_bounding_box_count` : (int64) The maximum number of bounding boxes returned. The default is 100. The number of returned bounding boxes might be limited by the server. AutoML Tables `feature_importance` : (boolean) Whether feature_importance is populated in the returned list of TablesAnnotation objects. The default is false.  
**Returns**  
---  
**Type** | **Description**  
`[PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.PredictResponse)` |   
  
### predict(PredictRequest request)
    
    
    public final PredictResponse predict(PredictRequest request)

Perform an online prediction. The prediction result is directly returned in the response. Available for following ML scenarios, and their expected request payloads:

AutoML Vision Classification

  * An image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB. 



AutoML Vision Object Detection

  * An image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB. 



AutoML Natural Language Classification

  * A TextSnippet up to 60,000 characters, UTF-8 encoded or a document in .PDF, .TIF or .TIFF format with size upto 2MB. 



AutoML Natural Language Entity Extraction

  * A TextSnippet up to 10,000 characters, UTF-8 NFC encoded or a document in .PDF, .TIF or .TIFF format with size upto 20MB. 



AutoML Natural Language Sentiment Analysis

  * A TextSnippet up to 60,000 characters, UTF-8 encoded or a document in .PDF, .TIF or .TIFF format with size upto 2MB. 



AutoML Translation

  * A TextSnippet up to 25,000 characters, UTF-8 encoded. 



AutoML Tables

  * A row with column values matching the columns of the model, up to 5MB. Not available for FORECASTING `prediction_type`. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       PredictRequest request =
           PredictRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setPayload(ExamplePayload.newBuilder().build())
               .putAllParams(new HashMap<String, String>())
               .build();
       PredictResponse response = predictionServiceClient.predict(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.PredictRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.PredictResponse)` |   
  
### predict(String name, ExamplePayload payload, Map<String,String> params)
    
    
    public final PredictResponse predict(String name, ExamplePayload payload, Map<String,String> params)

Perform an online prediction. The prediction result is directly returned in the response. Available for following ML scenarios, and their expected request payloads:

AutoML Vision Classification

  * An image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB. 



AutoML Vision Object Detection

  * An image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB. 



AutoML Natural Language Classification

  * A TextSnippet up to 60,000 characters, UTF-8 encoded or a document in .PDF, .TIF or .TIFF format with size upto 2MB. 



AutoML Natural Language Entity Extraction

  * A TextSnippet up to 10,000 characters, UTF-8 NFC encoded or a document in .PDF, .TIF or .TIFF format with size upto 20MB. 



AutoML Natural Language Sentiment Analysis

  * A TextSnippet up to 60,000 characters, UTF-8 encoded or a document in .PDF, .TIF or .TIFF format with size upto 2MB. 



AutoML Translation

  * A TextSnippet up to 25,000 characters, UTF-8 encoded. 



AutoML Tables

  * A row with column values matching the columns of the model, up to 5MB. Not available for FORECASTING `prediction_type`. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       String name = ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString();
       ExamplePayload payload = ExamplePayload.newBuilder().build();
       Map<String, String> params = new HashMap<>();
       PredictResponse response = predictionServiceClient.predict(name, payload, params);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the model requested to serve the prediction.  
`payload` | `[ExamplePayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.ExamplePayload)`  
Required. Payload to perform a prediction on. The payload must match the problem type that the model was trained to solve.  
`params` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Additional domain-specific parameters, any string must be up to 25000 characters long. AutoML Vision Classification `score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for an image, it will only produce results that have at least this confidence score. The default is 0.5. AutoML Vision Object Detection `score_threshold` : (float) When Model detects objects on the image, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5. `max_bounding_box_count` : (int64) The maximum number of bounding boxes returned. The default is 100. The number of returned bounding boxes might be limited by the server. AutoML Tables `feature_importance` : (boolean) Whether feature_importance is populated in the returned list of TablesAnnotation objects. The default is false.  
**Returns**  
---  
**Type** | **Description**  
`[PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.PredictResponse)` |   
  
### predictCallable()
    
    
    public final UnaryCallable<PredictRequest,PredictResponse> predictCallable()

Perform an online prediction. The prediction result is directly returned in the response. Available for following ML scenarios, and their expected request payloads:

AutoML Vision Classification

  * An image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB. 



AutoML Vision Object Detection

  * An image in .JPEG, .GIF or .PNG format, image_bytes up to 30MB. 



AutoML Natural Language Classification

  * A TextSnippet up to 60,000 characters, UTF-8 encoded or a document in .PDF, .TIF or .TIFF format with size upto 2MB. 



AutoML Natural Language Entity Extraction

  * A TextSnippet up to 10,000 characters, UTF-8 NFC encoded or a document in .PDF, .TIF or .TIFF format with size upto 20MB. 



AutoML Natural Language Sentiment Analysis

  * A TextSnippet up to 60,000 characters, UTF-8 encoded or a document in .PDF, .TIF or .TIFF format with size upto 2MB. 



AutoML Translation

  * A TextSnippet up to 25,000 characters, UTF-8 encoded. 



AutoML Tables

  * A row with column values matching the columns of the model, up to 5MB. Not available for FORECASTING `prediction_type`. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PredictionServiceClient predictionServiceClient = PredictionServiceClient.create()) {
       PredictRequest request =
           PredictRequest.newBuilder()
               .setName(ModelName.of("[PROJECT]", "[LOCATION]", "[MODEL]").toString())
               .setPayload(ExamplePayload.newBuilder().build())
               .putAllParams(new HashMap<String, String>())
               .build();
       ApiFuture<PredictResponse> future =
           predictionServiceClient.predictCallable().futureCall(request);
       // Do something.
       PredictResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PredictRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.PredictRequest),[PredictResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1.PredictResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-06 UTC."],[],[]] 
