---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplateServiceClient
title: Class BreakTemplateServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:28.275734+00:00
---

# Class BreakTemplateServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplateServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BreakTemplateServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/BreakTemplateServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `BreakTemplate` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       BreakTemplateName name = BreakTemplateName.of("[NETWORK_CODE]", "[BREAK_TEMPLATE]");
       BreakTemplate response = breakTemplateServiceClient.getBreakTemplate(name);
     }
     

Note: close() needs to be called on the BreakTemplateServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetBreakTemplate |  Retrieves a `BreakTemplate` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBreakTemplate(GetBreakTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBreakTemplate(BreakTemplateName name) 
  * getBreakTemplate(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBreakTemplateCallable() 

  
ListBreakTemplates |  Lists `BreakTemplate` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBreakTemplates(ListBreakTemplatesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBreakTemplates(NetworkName parent) 
  * listBreakTemplates(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBreakTemplatesPagedCallable() 
  * listBreakTemplatesCallable() 

  
CreateBreakTemplate |  Creates a `BreakTemplate` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createBreakTemplate(CreateBreakTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createBreakTemplate(NetworkName parent, BreakTemplate breakTemplate) 
  * createBreakTemplate(String parent, BreakTemplate breakTemplate) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createBreakTemplateCallable() 

  
BatchCreateBreakTemplates |  Batch creates `BreakTemplate` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateBreakTemplates(NetworkName parent, List<CreateBreakTemplateRequest> requests) 
  * batchCreateBreakTemplates(String parent, List<CreateBreakTemplateRequest> requests) 
  * batchCreateBreakTemplates(BatchCreateBreakTemplatesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateBreakTemplatesCallable() 

  
UpdateBreakTemplate |  Updates a `BreakTemplate` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateBreakTemplate(UpdateBreakTemplateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateBreakTemplate(BreakTemplate breakTemplate, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateBreakTemplateCallable() 

  
BatchUpdateBreakTemplates |  Batch updates `BreakTemplate` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateBreakTemplates(NetworkName parent, List<UpdateBreakTemplateRequest> requests) 
  * batchUpdateBreakTemplates(String parent, List<UpdateBreakTemplateRequest> requests) 
  * batchUpdateBreakTemplates(BatchUpdateBreakTemplatesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateBreakTemplatesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of BreakTemplateServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BreakTemplateServiceSettings breakTemplateServiceSettings =
         BreakTemplateServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create(breakTemplateServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BreakTemplateServiceSettings breakTemplateServiceSettings =
         BreakTemplateServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create(breakTemplateServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BreakTemplateServiceClient

## Static Methods 

### create()
    
    
    public static final BreakTemplateServiceClient create()

Constructs an instance of BreakTemplateServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[BreakTemplateServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplateServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BreakTemplateServiceSettings settings)
    
    
    public static final BreakTemplateServiceClient create(BreakTemplateServiceSettings settings)

Constructs an instance of BreakTemplateServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BreakTemplateServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplateServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BreakTemplateServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplateServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BreakTemplateServiceStub stub)
    
    
    public static final BreakTemplateServiceClient create(BreakTemplateServiceStub stub)

Constructs an instance of BreakTemplateServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(BreakTemplateServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BreakTemplateServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.BreakTemplateServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BreakTemplateServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplateServiceClient)` |   
  
## Constructors 

### BreakTemplateServiceClient(BreakTemplateServiceSettings settings)
    
    
    protected BreakTemplateServiceClient(BreakTemplateServiceSettings settings)

Constructs an instance of BreakTemplateServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BreakTemplateServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplateServiceSettings)`  
  
  
### BreakTemplateServiceClient(BreakTemplateServiceStub stub)
    
    
    protected BreakTemplateServiceClient(BreakTemplateServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BreakTemplateServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.BreakTemplateServiceStub)`  
  
  
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
  
### batchCreateBreakTemplates(@Nullable NetworkName parent, List<CreateBreakTemplateRequest> requests)
    
    
    public final BatchCreateBreakTemplatesResponse batchCreateBreakTemplates(@Nullable NetworkName parent, List<CreateBreakTemplateRequest> requests)

Batch creates `BreakTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateBreakTemplateRequest> requests = new ArrayList<>();
       BatchCreateBreakTemplatesResponse response =
           breakTemplateServiceClient.batchCreateBreakTemplates(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `BreakTemplates` will be created. Format: `networks/{network_code}` The parent field in the `CreateBreakTemplateRequest` must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateBreakTemplateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateBreakTemplateRequest)>`  
Required. The `BreakTemplate` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateBreakTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateBreakTemplatesResponse)` |   
  
### batchCreateBreakTemplates(BatchCreateBreakTemplatesRequest request)
    
    
    public final BatchCreateBreakTemplatesResponse batchCreateBreakTemplates(BatchCreateBreakTemplatesRequest request)

Batch creates `BreakTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       BatchCreateBreakTemplatesRequest request =
           BatchCreateBreakTemplatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateBreakTemplateRequest>())
               .build();
       BatchCreateBreakTemplatesResponse response =
           breakTemplateServiceClient.batchCreateBreakTemplates(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateBreakTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateBreakTemplatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateBreakTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateBreakTemplatesResponse)` |   
  
### batchCreateBreakTemplates(String parent, List<CreateBreakTemplateRequest> requests)
    
    
    public final BatchCreateBreakTemplatesResponse batchCreateBreakTemplates(String parent, List<CreateBreakTemplateRequest> requests)

Batch creates `BreakTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateBreakTemplateRequest> requests = new ArrayList<>();
       BatchCreateBreakTemplatesResponse response =
           breakTemplateServiceClient.batchCreateBreakTemplates(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `BreakTemplates` will be created. Format: `networks/{network_code}` The parent field in the `CreateBreakTemplateRequest` must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateBreakTemplateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateBreakTemplateRequest)>`  
Required. The `BreakTemplate` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateBreakTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateBreakTemplatesResponse)` |   
  
### batchCreateBreakTemplatesCallable()
    
    
    public final UnaryCallable<BatchCreateBreakTemplatesRequest,BatchCreateBreakTemplatesResponse> batchCreateBreakTemplatesCallable()

Batch creates `BreakTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       BatchCreateBreakTemplatesRequest request =
           BatchCreateBreakTemplatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateBreakTemplateRequest>())
               .build();
       ApiFuture<BatchCreateBreakTemplatesResponse> future =
           breakTemplateServiceClient.batchCreateBreakTemplatesCallable().futureCall(request);
       // Do something.
       BatchCreateBreakTemplatesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateBreakTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateBreakTemplatesRequest),[BatchCreateBreakTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateBreakTemplatesResponse)>` |   
  
### batchUpdateBreakTemplates(@Nullable NetworkName parent, List<UpdateBreakTemplateRequest> requests)
    
    
    public final BatchUpdateBreakTemplatesResponse batchUpdateBreakTemplates(@Nullable NetworkName parent, List<UpdateBreakTemplateRequest> requests)

Batch updates `BreakTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateBreakTemplateRequest> requests = new ArrayList<>();
       BatchUpdateBreakTemplatesResponse response =
           breakTemplateServiceClient.batchUpdateBreakTemplates(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `BreakTemplates` will be updated. Format: `networks/{network_code}` The parent field in the `UpdateBreakTemplateRequest` must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateBreakTemplateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateBreakTemplateRequest)>`  
Required. The `BreakTemplate` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateBreakTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateBreakTemplatesResponse)` |   
  
### batchUpdateBreakTemplates(BatchUpdateBreakTemplatesRequest request)
    
    
    public final BatchUpdateBreakTemplatesResponse batchUpdateBreakTemplates(BatchUpdateBreakTemplatesRequest request)

Batch updates `BreakTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       BatchUpdateBreakTemplatesRequest request =
           BatchUpdateBreakTemplatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateBreakTemplateRequest>())
               .build();
       BatchUpdateBreakTemplatesResponse response =
           breakTemplateServiceClient.batchUpdateBreakTemplates(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateBreakTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateBreakTemplatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateBreakTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateBreakTemplatesResponse)` |   
  
### batchUpdateBreakTemplates(String parent, List<UpdateBreakTemplateRequest> requests)
    
    
    public final BatchUpdateBreakTemplatesResponse batchUpdateBreakTemplates(String parent, List<UpdateBreakTemplateRequest> requests)

Batch updates `BreakTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateBreakTemplateRequest> requests = new ArrayList<>();
       BatchUpdateBreakTemplatesResponse response =
           breakTemplateServiceClient.batchUpdateBreakTemplates(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `BreakTemplates` will be updated. Format: `networks/{network_code}` The parent field in the `UpdateBreakTemplateRequest` must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateBreakTemplateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateBreakTemplateRequest)>`  
Required. The `BreakTemplate` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateBreakTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateBreakTemplatesResponse)` |   
  
### batchUpdateBreakTemplatesCallable()
    
    
    public final UnaryCallable<BatchUpdateBreakTemplatesRequest,BatchUpdateBreakTemplatesResponse> batchUpdateBreakTemplatesCallable()

Batch updates `BreakTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       BatchUpdateBreakTemplatesRequest request =
           BatchUpdateBreakTemplatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateBreakTemplateRequest>())
               .build();
       ApiFuture<BatchUpdateBreakTemplatesResponse> future =
           breakTemplateServiceClient.batchUpdateBreakTemplatesCallable().futureCall(request);
       // Do something.
       BatchUpdateBreakTemplatesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateBreakTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateBreakTemplatesRequest),[BatchUpdateBreakTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateBreakTemplatesResponse)>` |   
  
### close()
    
    
    public final void close()

### createBreakTemplate(@Nullable NetworkName parent, BreakTemplate breakTemplate)
    
    
    public final BreakTemplate createBreakTemplate(@Nullable NetworkName parent, BreakTemplate breakTemplate)

Creates a `BreakTemplate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       BreakTemplate breakTemplate = BreakTemplate.newBuilder().build();
       BreakTemplate response =
           breakTemplateServiceClient.createBreakTemplate(parent, breakTemplate);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `BreakTemplate` will be created. Format: `networks/{network_code}`  
`breakTemplate` | `[BreakTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplate)`  
Required. The `BreakTemplate` to create.  
**Returns**  
---  
**Type** | **Description**  
`[BreakTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplate)` |   
  
### createBreakTemplate(CreateBreakTemplateRequest request)
    
    
    public final BreakTemplate createBreakTemplate(CreateBreakTemplateRequest request)

Creates a `BreakTemplate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       CreateBreakTemplateRequest request =
           CreateBreakTemplateRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setBreakTemplate(BreakTemplate.newBuilder().build())
               .build();
       BreakTemplate response = breakTemplateServiceClient.createBreakTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBreakTemplateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateBreakTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BreakTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplate)` |   
  
### createBreakTemplate(String parent, BreakTemplate breakTemplate)
    
    
    public final BreakTemplate createBreakTemplate(String parent, BreakTemplate breakTemplate)

Creates a `BreakTemplate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       BreakTemplate breakTemplate = BreakTemplate.newBuilder().build();
       BreakTemplate response =
           breakTemplateServiceClient.createBreakTemplate(parent, breakTemplate);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `BreakTemplate` will be created. Format: `networks/{network_code}`  
`breakTemplate` | `[BreakTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplate)`  
Required. The `BreakTemplate` to create.  
**Returns**  
---  
**Type** | **Description**  
`[BreakTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplate)` |   
  
### createBreakTemplateCallable()
    
    
    public final UnaryCallable<CreateBreakTemplateRequest,BreakTemplate> createBreakTemplateCallable()

Creates a `BreakTemplate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       CreateBreakTemplateRequest request =
           CreateBreakTemplateRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setBreakTemplate(BreakTemplate.newBuilder().build())
               .build();
       ApiFuture<BreakTemplate> future =
           breakTemplateServiceClient.createBreakTemplateCallable().futureCall(request);
       // Do something.
       BreakTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateBreakTemplateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateBreakTemplateRequest),[BreakTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplate)>` |   
  
### getBreakTemplate(@Nullable BreakTemplateName name)
    
    
    public final BreakTemplate getBreakTemplate(@Nullable BreakTemplateName name)

Retrieves a `BreakTemplate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       BreakTemplateName name = BreakTemplateName.of("[NETWORK_CODE]", "[BREAK_TEMPLATE]");
       BreakTemplate response = breakTemplateServiceClient.getBreakTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.BreakTemplateName`  
Required. The resource name of the `BreakTemplate`. Format: `networks/{network_code}/breakTemplates/{break_template_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BreakTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplate)` |   
  
### getBreakTemplate(GetBreakTemplateRequest request)
    
    
    public final BreakTemplate getBreakTemplate(GetBreakTemplateRequest request)

Retrieves a `BreakTemplate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       GetBreakTemplateRequest request =
           GetBreakTemplateRequest.newBuilder()
               .setName(BreakTemplateName.of("[NETWORK_CODE]", "[BREAK_TEMPLATE]").toString())
               .build();
       BreakTemplate response = breakTemplateServiceClient.getBreakTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBreakTemplateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetBreakTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BreakTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplate)` |   
  
### getBreakTemplate(String name)
    
    
    public final BreakTemplate getBreakTemplate(String name)

Retrieves a `BreakTemplate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       String name = BreakTemplateName.of("[NETWORK_CODE]", "[BREAK_TEMPLATE]").toString();
       BreakTemplate response = breakTemplateServiceClient.getBreakTemplate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the `BreakTemplate`. Format: `networks/{network_code}/breakTemplates/{break_template_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BreakTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplate)` |   
  
### getBreakTemplateCallable()
    
    
    public final UnaryCallable<GetBreakTemplateRequest,BreakTemplate> getBreakTemplateCallable()

Retrieves a `BreakTemplate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       GetBreakTemplateRequest request =
           GetBreakTemplateRequest.newBuilder()
               .setName(BreakTemplateName.of("[NETWORK_CODE]", "[BREAK_TEMPLATE]").toString())
               .build();
       ApiFuture<BreakTemplate> future =
           breakTemplateServiceClient.getBreakTemplateCallable().futureCall(request);
       // Do something.
       BreakTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBreakTemplateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetBreakTemplateRequest),[BreakTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplate)>` |   
  
### getSettings()
    
    
    public final @Nullable BreakTemplateServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.BreakTemplateServiceSettings` |   
  
### getStub()
    
    
    public BreakTemplateServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[BreakTemplateServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.BreakTemplateServiceStub)` |   
  
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
  
### listBreakTemplates(@Nullable NetworkName parent)
    
    
    public final BreakTemplateServiceClient.ListBreakTemplatesPagedResponse listBreakTemplates(@Nullable NetworkName parent)

Lists `BreakTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (BreakTemplate element :
           breakTemplateServiceClient.listBreakTemplates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of `BreakTemplates`. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[BreakTemplateServiceClient.ListBreakTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplateServiceClient.ListBreakTemplatesPagedResponse)` |   
  
### listBreakTemplates(ListBreakTemplatesRequest request)
    
    
    public final BreakTemplateServiceClient.ListBreakTemplatesPagedResponse listBreakTemplates(ListBreakTemplatesRequest request)

Lists `BreakTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       ListBreakTemplatesRequest request =
           ListBreakTemplatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (BreakTemplate element :
           breakTemplateServiceClient.listBreakTemplates(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBreakTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListBreakTemplatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BreakTemplateServiceClient.ListBreakTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplateServiceClient.ListBreakTemplatesPagedResponse)` |   
  
### listBreakTemplates(String parent)
    
    
    public final BreakTemplateServiceClient.ListBreakTemplatesPagedResponse listBreakTemplates(String parent)

Lists `BreakTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (BreakTemplate element :
           breakTemplateServiceClient.listBreakTemplates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of `BreakTemplates`. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[BreakTemplateServiceClient.ListBreakTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplateServiceClient.ListBreakTemplatesPagedResponse)` |   
  
### listBreakTemplatesCallable()
    
    
    public final UnaryCallable<ListBreakTemplatesRequest,ListBreakTemplatesResponse> listBreakTemplatesCallable()

Lists `BreakTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       ListBreakTemplatesRequest request =
           ListBreakTemplatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListBreakTemplatesResponse response =
             breakTemplateServiceClient.listBreakTemplatesCallable().call(request);
         for (BreakTemplate element : response.getBreakTemplatesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBreakTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListBreakTemplatesRequest),[ListBreakTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListBreakTemplatesResponse)>` |   
  
### listBreakTemplatesPagedCallable()
    
    
    public final UnaryCallable<ListBreakTemplatesRequest,BreakTemplateServiceClient.ListBreakTemplatesPagedResponse> listBreakTemplatesPagedCallable()

Lists `BreakTemplate` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       ListBreakTemplatesRequest request =
           ListBreakTemplatesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<BreakTemplate> future =
           breakTemplateServiceClient.listBreakTemplatesPagedCallable().futureCall(request);
       // Do something.
       for (BreakTemplate element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBreakTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListBreakTemplatesRequest),[ListBreakTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplateServiceClient.ListBreakTemplatesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateBreakTemplate(BreakTemplate breakTemplate, FieldMask updateMask)
    
    
    public final BreakTemplate updateBreakTemplate(BreakTemplate breakTemplate, FieldMask updateMask)

Updates a `BreakTemplate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       BreakTemplate breakTemplate = BreakTemplate.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       BreakTemplate response =
           breakTemplateServiceClient.updateBreakTemplate(breakTemplate, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`breakTemplate` | `[BreakTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplate)`  
Required. The `BreakTemplate` to update. The `BreakTemplate`'s `name` is used to identify the `BreakTemplate` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[BreakTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplate)` |   
  
### updateBreakTemplate(UpdateBreakTemplateRequest request)
    
    
    public final BreakTemplate updateBreakTemplate(UpdateBreakTemplateRequest request)

Updates a `BreakTemplate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       UpdateBreakTemplateRequest request =
           UpdateBreakTemplateRequest.newBuilder()
               .setBreakTemplate(BreakTemplate.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       BreakTemplate response = breakTemplateServiceClient.updateBreakTemplate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBreakTemplateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateBreakTemplateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BreakTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplate)` |   
  
### updateBreakTemplateCallable()
    
    
    public final UnaryCallable<UpdateBreakTemplateRequest,BreakTemplate> updateBreakTemplateCallable()

Updates a `BreakTemplate` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BreakTemplateServiceClient breakTemplateServiceClient =
         BreakTemplateServiceClient.create()) {
       UpdateBreakTemplateRequest request =
           UpdateBreakTemplateRequest.newBuilder()
               .setBreakTemplate(BreakTemplate.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<BreakTemplate> future =
           breakTemplateServiceClient.updateBreakTemplateCallable().futureCall(request);
       // Do something.
       BreakTemplate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateBreakTemplateRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateBreakTemplateRequest),[BreakTemplate](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BreakTemplate)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
