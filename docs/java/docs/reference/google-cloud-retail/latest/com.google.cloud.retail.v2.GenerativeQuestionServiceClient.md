---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionServiceClient
title: Class GenerativeQuestionServiceClient (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:24.214641+00:00
---

# Class GenerativeQuestionServiceClient (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GenerativeQuestionServiceClient (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-retail/google-cloud-retail/src/main/java/com/google/cloud/retail/v2/GenerativeQuestionServiceClient.java)| [Product Reference](https://cloud.google.com/solutions/retail)  
---|---  
  
Service Description: Service for managing LLM generated questions in search serving.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       GenerativeQuestionsFeatureConfig generativeQuestionsFeatureConfig =
           GenerativeQuestionsFeatureConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       GenerativeQuestionsFeatureConfig response =
           generativeQuestionServiceClient.updateGenerativeQuestionsFeatureConfig(
               generativeQuestionsFeatureConfig, updateMask);
     }
     

Note: close() needs to be called on the GenerativeQuestionServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
UpdateGenerativeQuestionsFeatureConfig |  Manages overal generative question feature state -- enables toggling feature on and off. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateGenerativeQuestionsFeatureConfig(UpdateGenerativeQuestionsFeatureConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateGenerativeQuestionsFeatureConfig(GenerativeQuestionsFeatureConfig generativeQuestionsFeatureConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateGenerativeQuestionsFeatureConfigCallable() 

  
GetGenerativeQuestionsFeatureConfig |  Manages overal generative question feature state -- enables toggling feature on and off. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getGenerativeQuestionsFeatureConfig(GetGenerativeQuestionsFeatureConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getGenerativeQuestionsFeatureConfig(CatalogName catalog) 
  * getGenerativeQuestionsFeatureConfig(String catalog) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getGenerativeQuestionsFeatureConfigCallable() 

  
ListGenerativeQuestionConfigs |  Returns all questions for a given catalog. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGenerativeQuestionConfigs(ListGenerativeQuestionConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGenerativeQuestionConfigs(CatalogName parent) 
  * listGenerativeQuestionConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGenerativeQuestionConfigsCallable() 

  
UpdateGenerativeQuestionConfig |  Allows management of individual questions. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateGenerativeQuestionConfig(UpdateGenerativeQuestionConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateGenerativeQuestionConfig(GenerativeQuestionConfig generativeQuestionConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateGenerativeQuestionConfigCallable() 

  
BatchUpdateGenerativeQuestionConfigs |  Allows management of multiple questions. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateGenerativeQuestionConfigs(CatalogName parent, List<UpdateGenerativeQuestionConfigRequest> requests) 
  * batchUpdateGenerativeQuestionConfigs(String parent, List<UpdateGenerativeQuestionConfigRequest> requests) 
  * batchUpdateGenerativeQuestionConfigs(BatchUpdateGenerativeQuestionConfigsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateGenerativeQuestionConfigsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of GenerativeQuestionServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GenerativeQuestionServiceSettings generativeQuestionServiceSettings =
         GenerativeQuestionServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create(generativeQuestionServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GenerativeQuestionServiceSettings generativeQuestionServiceSettings =
         GenerativeQuestionServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create(generativeQuestionServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GenerativeQuestionServiceSettings generativeQuestionServiceSettings =
         GenerativeQuestionServiceSettings.newHttpJsonBuilder().build();
     GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create(generativeQuestionServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GenerativeQuestionServiceClient

## Static Methods 

### create()
    
    
    public static final GenerativeQuestionServiceClient create()

Constructs an instance of GenerativeQuestionServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[GenerativeQuestionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GenerativeQuestionServiceSettings settings)
    
    
    public static final GenerativeQuestionServiceClient create(GenerativeQuestionServiceSettings settings)

Constructs an instance of GenerativeQuestionServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GenerativeQuestionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeQuestionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GenerativeQuestionServiceStub stub)
    
    
    public static final GenerativeQuestionServiceClient create(GenerativeQuestionServiceStub stub)

Constructs an instance of GenerativeQuestionServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(GenerativeQuestionServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GenerativeQuestionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.GenerativeQuestionServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeQuestionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionServiceClient)` |   
  
## Constructors 

### GenerativeQuestionServiceClient(GenerativeQuestionServiceSettings settings)
    
    
    protected GenerativeQuestionServiceClient(GenerativeQuestionServiceSettings settings)

Constructs an instance of GenerativeQuestionServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GenerativeQuestionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionServiceSettings)`  
  
  
### GenerativeQuestionServiceClient(GenerativeQuestionServiceStub stub)
    
    
    protected GenerativeQuestionServiceClient(GenerativeQuestionServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GenerativeQuestionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.GenerativeQuestionServiceStub)`  
  
  
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
  
### batchUpdateGenerativeQuestionConfigs(@Nullable CatalogName parent, List<UpdateGenerativeQuestionConfigRequest> requests)
    
    
    public final BatchUpdateGenerativeQuestionConfigsResponse batchUpdateGenerativeQuestionConfigs(@Nullable CatalogName parent, List<UpdateGenerativeQuestionConfigRequest> requests)

Allows management of multiple questions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       CatalogName parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       List<UpdateGenerativeQuestionConfigRequest> requests = new ArrayList<>();
       BatchUpdateGenerativeQuestionConfigsResponse response =
           generativeQuestionServiceClient.batchUpdateGenerativeQuestionConfigs(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.CatalogName`  
Optional. Resource name of the parent catalog. Format: projects/{project}/locations/{location}/catalogs/{catalog}  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateGenerativeQuestionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateGenerativeQuestionConfigRequest)>`  
Required. The updates question configs.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateGenerativeQuestionConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.BatchUpdateGenerativeQuestionConfigsResponse)` |   
  
### batchUpdateGenerativeQuestionConfigs(BatchUpdateGenerativeQuestionConfigsRequest request)
    
    
    public final BatchUpdateGenerativeQuestionConfigsResponse batchUpdateGenerativeQuestionConfigs(BatchUpdateGenerativeQuestionConfigsRequest request)

Allows management of multiple questions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       BatchUpdateGenerativeQuestionConfigsRequest request =
           BatchUpdateGenerativeQuestionConfigsRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .addAllRequests(new ArrayList<UpdateGenerativeQuestionConfigRequest>())
               .build();
       BatchUpdateGenerativeQuestionConfigsResponse response =
           generativeQuestionServiceClient.batchUpdateGenerativeQuestionConfigs(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.BatchUpdateGenerativeQuestionConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateGenerativeQuestionConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.BatchUpdateGenerativeQuestionConfigsResponse)` |   
  
### batchUpdateGenerativeQuestionConfigs(String parent, List<UpdateGenerativeQuestionConfigRequest> requests)
    
    
    public final BatchUpdateGenerativeQuestionConfigsResponse batchUpdateGenerativeQuestionConfigs(String parent, List<UpdateGenerativeQuestionConfigRequest> requests)

Allows management of multiple questions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       String parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString();
       List<UpdateGenerativeQuestionConfigRequest> requests = new ArrayList<>();
       BatchUpdateGenerativeQuestionConfigsResponse response =
           generativeQuestionServiceClient.batchUpdateGenerativeQuestionConfigs(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Resource name of the parent catalog. Format: projects/{project}/locations/{location}/catalogs/{catalog}  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateGenerativeQuestionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateGenerativeQuestionConfigRequest)>`  
Required. The updates question configs.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateGenerativeQuestionConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.BatchUpdateGenerativeQuestionConfigsResponse)` |   
  
### batchUpdateGenerativeQuestionConfigsCallable()
    
    
    public final UnaryCallable<BatchUpdateGenerativeQuestionConfigsRequest,BatchUpdateGenerativeQuestionConfigsResponse> batchUpdateGenerativeQuestionConfigsCallable()

Allows management of multiple questions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       BatchUpdateGenerativeQuestionConfigsRequest request =
           BatchUpdateGenerativeQuestionConfigsRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .addAllRequests(new ArrayList<UpdateGenerativeQuestionConfigRequest>())
               .build();
       ApiFuture<BatchUpdateGenerativeQuestionConfigsResponse> future =
           generativeQuestionServiceClient
               .batchUpdateGenerativeQuestionConfigsCallable()
               .futureCall(request);
       // Do something.
       BatchUpdateGenerativeQuestionConfigsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.BatchUpdateGenerativeQuestionConfigsRequest),[BatchUpdateGenerativeQuestionConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.BatchUpdateGenerativeQuestionConfigsResponse)>` |   
  
### close()
    
    
    public final void close()

### getGenerativeQuestionsFeatureConfig(@Nullable CatalogName catalog)
    
    
    public final GenerativeQuestionsFeatureConfig getGenerativeQuestionsFeatureConfig(@Nullable CatalogName catalog)

Manages overal generative question feature state -- enables toggling feature on and off.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       CatalogName catalog = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       GenerativeQuestionsFeatureConfig response =
           generativeQuestionServiceClient.getGenerativeQuestionsFeatureConfig(catalog);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`catalog` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.CatalogName`  
Required. Resource name of the parent catalog. Format: projects/{project}/locations/{location}/catalogs/{catalog}  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionsFeatureConfig)` |   
  
### getGenerativeQuestionsFeatureConfig(GetGenerativeQuestionsFeatureConfigRequest request)
    
    
    public final GenerativeQuestionsFeatureConfig getGenerativeQuestionsFeatureConfig(GetGenerativeQuestionsFeatureConfigRequest request)

Manages overal generative question feature state -- enables toggling feature on and off.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       GetGenerativeQuestionsFeatureConfigRequest request =
           GetGenerativeQuestionsFeatureConfigRequest.newBuilder()
               .setCatalog(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .build();
       GenerativeQuestionsFeatureConfig response =
           generativeQuestionServiceClient.getGenerativeQuestionsFeatureConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGenerativeQuestionsFeatureConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetGenerativeQuestionsFeatureConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionsFeatureConfig)` |   
  
### getGenerativeQuestionsFeatureConfig(String catalog)
    
    
    public final GenerativeQuestionsFeatureConfig getGenerativeQuestionsFeatureConfig(String catalog)

Manages overal generative question feature state -- enables toggling feature on and off.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       String catalog = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString();
       GenerativeQuestionsFeatureConfig response =
           generativeQuestionServiceClient.getGenerativeQuestionsFeatureConfig(catalog);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`catalog` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the parent catalog. Format: projects/{project}/locations/{location}/catalogs/{catalog}  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionsFeatureConfig)` |   
  
### getGenerativeQuestionsFeatureConfigCallable()
    
    
    public final UnaryCallable<GetGenerativeQuestionsFeatureConfigRequest,GenerativeQuestionsFeatureConfig> getGenerativeQuestionsFeatureConfigCallable()

Manages overal generative question feature state -- enables toggling feature on and off.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       GetGenerativeQuestionsFeatureConfigRequest request =
           GetGenerativeQuestionsFeatureConfigRequest.newBuilder()
               .setCatalog(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .build();
       ApiFuture<GenerativeQuestionsFeatureConfig> future =
           generativeQuestionServiceClient
               .getGenerativeQuestionsFeatureConfigCallable()
               .futureCall(request);
       // Do something.
       GenerativeQuestionsFeatureConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGenerativeQuestionsFeatureConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GetGenerativeQuestionsFeatureConfigRequest),[GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionsFeatureConfig)>` |   
  
### getSettings()
    
    
    public final @Nullable GenerativeQuestionServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.GenerativeQuestionServiceSettings` |   
  
### getStub()
    
    
    public GenerativeQuestionServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[GenerativeQuestionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.stub.GenerativeQuestionServiceStub)` |   
  
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
  
### listGenerativeQuestionConfigs(@Nullable CatalogName parent)
    
    
    public final ListGenerativeQuestionConfigsResponse listGenerativeQuestionConfigs(@Nullable CatalogName parent)

Returns all questions for a given catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       CatalogName parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]");
       ListGenerativeQuestionConfigsResponse response =
           generativeQuestionServiceClient.listGenerativeQuestionConfigs(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.retail.v2.CatalogName`  
Required. Resource name of the parent catalog. Format: projects/{project}/locations/{location}/catalogs/{catalog}  
**Returns**  
---  
**Type** | **Description**  
`[ListGenerativeQuestionConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListGenerativeQuestionConfigsResponse)` |   
  
### listGenerativeQuestionConfigs(ListGenerativeQuestionConfigsRequest request)
    
    
    public final ListGenerativeQuestionConfigsResponse listGenerativeQuestionConfigs(ListGenerativeQuestionConfigsRequest request)

Returns all questions for a given catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       ListGenerativeQuestionConfigsRequest request =
           ListGenerativeQuestionConfigsRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .build();
       ListGenerativeQuestionConfigsResponse response =
           generativeQuestionServiceClient.listGenerativeQuestionConfigs(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListGenerativeQuestionConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ListGenerativeQuestionConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListGenerativeQuestionConfigsResponse)` |   
  
### listGenerativeQuestionConfigs(String parent)
    
    
    public final ListGenerativeQuestionConfigsResponse listGenerativeQuestionConfigs(String parent)

Returns all questions for a given catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       String parent = CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString();
       ListGenerativeQuestionConfigsResponse response =
           generativeQuestionServiceClient.listGenerativeQuestionConfigs(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the parent catalog. Format: projects/{project}/locations/{location}/catalogs/{catalog}  
**Returns**  
---  
**Type** | **Description**  
`[ListGenerativeQuestionConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListGenerativeQuestionConfigsResponse)` |   
  
### listGenerativeQuestionConfigsCallable()
    
    
    public final UnaryCallable<ListGenerativeQuestionConfigsRequest,ListGenerativeQuestionConfigsResponse> listGenerativeQuestionConfigsCallable()

Returns all questions for a given catalog.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       ListGenerativeQuestionConfigsRequest request =
           ListGenerativeQuestionConfigsRequest.newBuilder()
               .setParent(CatalogName.of("[PROJECT]", "[LOCATION]", "[CATALOG]").toString())
               .build();
       ApiFuture<ListGenerativeQuestionConfigsResponse> future =
           generativeQuestionServiceClient
               .listGenerativeQuestionConfigsCallable()
               .futureCall(request);
       // Do something.
       ListGenerativeQuestionConfigsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListGenerativeQuestionConfigsRequest),[ListGenerativeQuestionConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.ListGenerativeQuestionConfigsResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateGenerativeQuestionConfig(GenerativeQuestionConfig generativeQuestionConfig, FieldMask updateMask)
    
    
    public final GenerativeQuestionConfig updateGenerativeQuestionConfig(GenerativeQuestionConfig generativeQuestionConfig, FieldMask updateMask)

Allows management of individual questions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       GenerativeQuestionConfig generativeQuestionConfig =
           GenerativeQuestionConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       GenerativeQuestionConfig response =
           generativeQuestionServiceClient.updateGenerativeQuestionConfig(
               generativeQuestionConfig, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`generativeQuestionConfig` | `[GenerativeQuestionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionConfig)`  
Required. The question to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Indicates which fields in the provided GenerativeQuestionConfig to update. The following are NOT supported: 

  * GenerativeQuestionConfig.frequency

If not set or empty, all supported fields are updated.  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeQuestionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionConfig)` |   
  
### updateGenerativeQuestionConfig(UpdateGenerativeQuestionConfigRequest request)
    
    
    public final GenerativeQuestionConfig updateGenerativeQuestionConfig(UpdateGenerativeQuestionConfigRequest request)

Allows management of individual questions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       UpdateGenerativeQuestionConfigRequest request =
           UpdateGenerativeQuestionConfigRequest.newBuilder()
               .setGenerativeQuestionConfig(GenerativeQuestionConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       GenerativeQuestionConfig response =
           generativeQuestionServiceClient.updateGenerativeQuestionConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGenerativeQuestionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateGenerativeQuestionConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeQuestionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionConfig)` |   
  
### updateGenerativeQuestionConfigCallable()
    
    
    public final UnaryCallable<UpdateGenerativeQuestionConfigRequest,GenerativeQuestionConfig> updateGenerativeQuestionConfigCallable()

Allows management of individual questions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       UpdateGenerativeQuestionConfigRequest request =
           UpdateGenerativeQuestionConfigRequest.newBuilder()
               .setGenerativeQuestionConfig(GenerativeQuestionConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<GenerativeQuestionConfig> future =
           generativeQuestionServiceClient
               .updateGenerativeQuestionConfigCallable()
               .futureCall(request);
       // Do something.
       GenerativeQuestionConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGenerativeQuestionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateGenerativeQuestionConfigRequest),[GenerativeQuestionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionConfig)>` |   
  
### updateGenerativeQuestionsFeatureConfig(GenerativeQuestionsFeatureConfig generativeQuestionsFeatureConfig, FieldMask updateMask)
    
    
    public final GenerativeQuestionsFeatureConfig updateGenerativeQuestionsFeatureConfig(GenerativeQuestionsFeatureConfig generativeQuestionsFeatureConfig, FieldMask updateMask)

Manages overal generative question feature state -- enables toggling feature on and off.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       GenerativeQuestionsFeatureConfig generativeQuestionsFeatureConfig =
           GenerativeQuestionsFeatureConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       GenerativeQuestionsFeatureConfig response =
           generativeQuestionServiceClient.updateGenerativeQuestionsFeatureConfig(
               generativeQuestionsFeatureConfig, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`generativeQuestionsFeatureConfig` | `[GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionsFeatureConfig)`  
Required. The configuration managing the feature state.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Indicates which fields in the provided GenerativeQuestionsFeatureConfig to update. If not set or empty, all supported fields are updated.  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionsFeatureConfig)` |   
  
### updateGenerativeQuestionsFeatureConfig(UpdateGenerativeQuestionsFeatureConfigRequest request)
    
    
    public final GenerativeQuestionsFeatureConfig updateGenerativeQuestionsFeatureConfig(UpdateGenerativeQuestionsFeatureConfigRequest request)

Manages overal generative question feature state -- enables toggling feature on and off.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       UpdateGenerativeQuestionsFeatureConfigRequest request =
           UpdateGenerativeQuestionsFeatureConfigRequest.newBuilder()
               .setGenerativeQuestionsFeatureConfig(
                   GenerativeQuestionsFeatureConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       GenerativeQuestionsFeatureConfig response =
           generativeQuestionServiceClient.updateGenerativeQuestionsFeatureConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGenerativeQuestionsFeatureConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateGenerativeQuestionsFeatureConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionsFeatureConfig)` |   
  
### updateGenerativeQuestionsFeatureConfigCallable()
    
    
    public final UnaryCallable<UpdateGenerativeQuestionsFeatureConfigRequest,GenerativeQuestionsFeatureConfig> updateGenerativeQuestionsFeatureConfigCallable()

Manages overal generative question feature state -- enables toggling feature on and off.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GenerativeQuestionServiceClient generativeQuestionServiceClient =
         GenerativeQuestionServiceClient.create()) {
       UpdateGenerativeQuestionsFeatureConfigRequest request =
           UpdateGenerativeQuestionsFeatureConfigRequest.newBuilder()
               .setGenerativeQuestionsFeatureConfig(
                   GenerativeQuestionsFeatureConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<GenerativeQuestionsFeatureConfig> future =
           generativeQuestionServiceClient
               .updateGenerativeQuestionsFeatureConfigCallable()
               .futureCall(request);
       // Do something.
       GenerativeQuestionsFeatureConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGenerativeQuestionsFeatureConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.UpdateGenerativeQuestionsFeatureConfigRequest),[GenerativeQuestionsFeatureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.GenerativeQuestionsFeatureConfig)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
