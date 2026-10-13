---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LabelServiceClient
title: Class LabelServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:47.532421+00:00
---

# Class LabelServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LabelServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LabelServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/LabelServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `Label` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       LabelName name = LabelName.of("[NETWORK_CODE]", "[LABEL]");
       Label response = labelServiceClient.getLabel(name);
     }
     

Note: close() needs to be called on the LabelServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetLabel |  Retrieves a `Label` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLabel(GetLabelRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getLabel(LabelName name) 
  * getLabel(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLabelCallable() 

  
ListLabels |  Lists `Label` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLabels(ListLabelsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLabels(NetworkName parent) 
  * listLabels(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLabelsPagedCallable() 
  * listLabelsCallable() 

  
CreateLabel |  Creates a `Label` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createLabel(CreateLabelRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createLabel(NetworkName parent, Label label) 
  * createLabel(String parent, Label label) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createLabelCallable() 

  
BatchCreateLabels |  Creates `Label` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateLabels(NetworkName parent, List<CreateLabelRequest> requests) 
  * batchCreateLabels(String parent, List<CreateLabelRequest> requests) 
  * batchCreateLabels(BatchCreateLabelsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateLabelsCallable() 

  
UpdateLabel |  Updates a `Label` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateLabel(UpdateLabelRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateLabel(Label label, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateLabelCallable() 

  
BatchUpdateLabels |  Batch updates `Label` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateLabels(NetworkName parent, List<UpdateLabelRequest> requests) 
  * batchUpdateLabels(String parent, List<UpdateLabelRequest> requests) 
  * batchUpdateLabels(BatchUpdateLabelsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateLabelsCallable() 

  
BatchActivateLabels |  Activates `Label` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateLabels(BatchActivateLabelsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchActivateLabels(NetworkName parent, List<String> names) 
  * batchActivateLabels(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateLabelsCallable() 

  
BatchDeactivateLabels |  Deactivates `Label` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivateLabels(BatchDeactivateLabelsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeactivateLabels(NetworkName parent, List<String> names) 
  * batchDeactivateLabels(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivateLabelsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of LabelServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LabelServiceSettings labelServiceSettings =
         LabelServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     LabelServiceClient labelServiceClient = LabelServiceClient.create(labelServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LabelServiceSettings labelServiceSettings =
         LabelServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     LabelServiceClient labelServiceClient = LabelServiceClient.create(labelServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LabelServiceClient

## Static Methods 

### create()
    
    
    public static final LabelServiceClient create()

Constructs an instance of LabelServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[LabelServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LabelServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LabelServiceSettings settings)
    
    
    public static final LabelServiceClient create(LabelServiceSettings settings)

Constructs an instance of LabelServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LabelServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LabelServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LabelServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LabelServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LabelServiceStub stub)
    
    
    public static final LabelServiceClient create(LabelServiceStub stub)

Constructs an instance of LabelServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(LabelServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LabelServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.LabelServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LabelServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LabelServiceClient)` |   
  
## Constructors 

### LabelServiceClient(LabelServiceSettings settings)
    
    
    protected LabelServiceClient(LabelServiceSettings settings)

Constructs an instance of LabelServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LabelServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LabelServiceSettings)`  
  
  
### LabelServiceClient(LabelServiceStub stub)
    
    
    protected LabelServiceClient(LabelServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LabelServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.LabelServiceStub)`  
  
  
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
  
### batchActivateLabels(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchActivateLabelsResponse batchActivateLabels(@Nullable NetworkName parent, List<String> names)

Activates `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchActivateLabelsResponse response = labelServiceClient.batchActivateLabels(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the Label. Format: `networks/{network_code}/labels/{label_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateLabelsResponse)` |   
  
### batchActivateLabels(BatchActivateLabelsRequest request)
    
    
    public final BatchActivateLabelsResponse batchActivateLabels(BatchActivateLabelsRequest request)

Activates `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       BatchActivateLabelsRequest request =
           BatchActivateLabelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchActivateLabelsResponse response = labelServiceClient.batchActivateLabels(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateLabelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateLabelsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateLabelsResponse)` |   
  
### batchActivateLabels(String parent, List<String> names)
    
    
    public final BatchActivateLabelsResponse batchActivateLabels(String parent, List<String> names)

Activates `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchActivateLabelsResponse response = labelServiceClient.batchActivateLabels(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the Label. Format: `networks/{network_code}/labels/{label_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateLabelsResponse)` |   
  
### batchActivateLabelsCallable()
    
    
    public final UnaryCallable<BatchActivateLabelsRequest,BatchActivateLabelsResponse> batchActivateLabelsCallable()

Activates `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       BatchActivateLabelsRequest request =
           BatchActivateLabelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchActivateLabelsResponse> future =
           labelServiceClient.batchActivateLabelsCallable().futureCall(request);
       // Do something.
       BatchActivateLabelsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateLabelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateLabelsRequest),[BatchActivateLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateLabelsResponse)>` |   
  
### batchCreateLabels(@Nullable NetworkName parent, List<CreateLabelRequest> requests)
    
    
    public final BatchCreateLabelsResponse batchCreateLabels(@Nullable NetworkName parent, List<CreateLabelRequest> requests)

Creates `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateLabelRequest> requests = new ArrayList<>();
       BatchCreateLabelsResponse response = labelServiceClient.batchCreateLabels(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `Labels` will be created. Format: `networks/{network_code}` The parent field in the CreateLabelRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateLabelRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateLabelRequest)>`  
Required. The `Label` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateLabelsResponse)` |   
  
### batchCreateLabels(BatchCreateLabelsRequest request)
    
    
    public final BatchCreateLabelsResponse batchCreateLabels(BatchCreateLabelsRequest request)

Creates `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       BatchCreateLabelsRequest request =
           BatchCreateLabelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateLabelRequest>())
               .build();
       BatchCreateLabelsResponse response = labelServiceClient.batchCreateLabels(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateLabelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateLabelsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateLabelsResponse)` |   
  
### batchCreateLabels(String parent, List<CreateLabelRequest> requests)
    
    
    public final BatchCreateLabelsResponse batchCreateLabels(String parent, List<CreateLabelRequest> requests)

Creates `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateLabelRequest> requests = new ArrayList<>();
       BatchCreateLabelsResponse response = labelServiceClient.batchCreateLabels(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `Labels` will be created. Format: `networks/{network_code}` The parent field in the CreateLabelRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateLabelRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateLabelRequest)>`  
Required. The `Label` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateLabelsResponse)` |   
  
### batchCreateLabelsCallable()
    
    
    public final UnaryCallable<BatchCreateLabelsRequest,BatchCreateLabelsResponse> batchCreateLabelsCallable()

Creates `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       BatchCreateLabelsRequest request =
           BatchCreateLabelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateLabelRequest>())
               .build();
       ApiFuture<BatchCreateLabelsResponse> future =
           labelServiceClient.batchCreateLabelsCallable().futureCall(request);
       // Do something.
       BatchCreateLabelsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateLabelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateLabelsRequest),[BatchCreateLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateLabelsResponse)>` |   
  
### batchDeactivateLabels(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDeactivateLabelsResponse batchDeactivateLabels(@Nullable NetworkName parent, List<String> names)

Deactivates `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDeactivateLabelsResponse response =
           labelServiceClient.batchDeactivateLabels(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the Label. Format: `networks/{network_code}/labels/{label_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateLabelsResponse)` |   
  
### batchDeactivateLabels(BatchDeactivateLabelsRequest request)
    
    
    public final BatchDeactivateLabelsResponse batchDeactivateLabels(BatchDeactivateLabelsRequest request)

Deactivates `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       BatchDeactivateLabelsRequest request =
           BatchDeactivateLabelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeactivateLabelsResponse response = labelServiceClient.batchDeactivateLabels(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivateLabelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateLabelsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateLabelsResponse)` |   
  
### batchDeactivateLabels(String parent, List<String> names)
    
    
    public final BatchDeactivateLabelsResponse batchDeactivateLabels(String parent, List<String> names)

Deactivates `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDeactivateLabelsResponse response =
           labelServiceClient.batchDeactivateLabels(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the Label. Format: `networks/{network_code}/labels/{label_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateLabelsResponse)` |   
  
### batchDeactivateLabelsCallable()
    
    
    public final UnaryCallable<BatchDeactivateLabelsRequest,BatchDeactivateLabelsResponse> batchDeactivateLabelsCallable()

Deactivates `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       BatchDeactivateLabelsRequest request =
           BatchDeactivateLabelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDeactivateLabelsResponse> future =
           labelServiceClient.batchDeactivateLabelsCallable().futureCall(request);
       // Do something.
       BatchDeactivateLabelsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivateLabelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateLabelsRequest),[BatchDeactivateLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateLabelsResponse)>` |   
  
### batchUpdateLabels(@Nullable NetworkName parent, List<UpdateLabelRequest> requests)
    
    
    public final BatchUpdateLabelsResponse batchUpdateLabels(@Nullable NetworkName parent, List<UpdateLabelRequest> requests)

Batch updates `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateLabelRequest> requests = new ArrayList<>();
       BatchUpdateLabelsResponse response = labelServiceClient.batchUpdateLabels(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `Labels` will be updated. Format: `networks/{network_code}` The parent field in the UpdateLabelRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateLabelRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateLabelRequest)>`  
Required. The `Label` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateLabelsResponse)` |   
  
### batchUpdateLabels(BatchUpdateLabelsRequest request)
    
    
    public final BatchUpdateLabelsResponse batchUpdateLabels(BatchUpdateLabelsRequest request)

Batch updates `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       BatchUpdateLabelsRequest request =
           BatchUpdateLabelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateLabelRequest>())
               .build();
       BatchUpdateLabelsResponse response = labelServiceClient.batchUpdateLabels(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateLabelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateLabelsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateLabelsResponse)` |   
  
### batchUpdateLabels(String parent, List<UpdateLabelRequest> requests)
    
    
    public final BatchUpdateLabelsResponse batchUpdateLabels(String parent, List<UpdateLabelRequest> requests)

Batch updates `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateLabelRequest> requests = new ArrayList<>();
       BatchUpdateLabelsResponse response = labelServiceClient.batchUpdateLabels(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `Labels` will be updated. Format: `networks/{network_code}` The parent field in the UpdateLabelRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateLabelRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateLabelRequest)>`  
Required. The `Label` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateLabelsResponse)` |   
  
### batchUpdateLabelsCallable()
    
    
    public final UnaryCallable<BatchUpdateLabelsRequest,BatchUpdateLabelsResponse> batchUpdateLabelsCallable()

Batch updates `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       BatchUpdateLabelsRequest request =
           BatchUpdateLabelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateLabelRequest>())
               .build();
       ApiFuture<BatchUpdateLabelsResponse> future =
           labelServiceClient.batchUpdateLabelsCallable().futureCall(request);
       // Do something.
       BatchUpdateLabelsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateLabelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateLabelsRequest),[BatchUpdateLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateLabelsResponse)>` |   
  
### close()
    
    
    public final void close()

### createLabel(@Nullable NetworkName parent, Label label)
    
    
    public final Label createLabel(@Nullable NetworkName parent, Label label)

Creates a `Label` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       Label label = Label.newBuilder().build();
       Label response = labelServiceClient.createLabel(parent, label);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `Label` will be created. Format: `networks/{network_code}`  
`label` | `[Label](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Label)`  
Required. The `Label` to create.  
**Returns**  
---  
**Type** | **Description**  
`[Label](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Label)` |   
  
### createLabel(CreateLabelRequest request)
    
    
    public final Label createLabel(CreateLabelRequest request)

Creates a `Label` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       CreateLabelRequest request =
           CreateLabelRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setLabel(Label.newBuilder().build())
               .build();
       Label response = labelServiceClient.createLabel(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateLabelRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateLabelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Label](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Label)` |   
  
### createLabel(String parent, Label label)
    
    
    public final Label createLabel(String parent, Label label)

Creates a `Label` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       Label label = Label.newBuilder().build();
       Label response = labelServiceClient.createLabel(parent, label);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `Label` will be created. Format: `networks/{network_code}`  
`label` | `[Label](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Label)`  
Required. The `Label` to create.  
**Returns**  
---  
**Type** | **Description**  
`[Label](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Label)` |   
  
### createLabelCallable()
    
    
    public final UnaryCallable<CreateLabelRequest,Label> createLabelCallable()

Creates a `Label` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       CreateLabelRequest request =
           CreateLabelRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setLabel(Label.newBuilder().build())
               .build();
       ApiFuture<Label> future = labelServiceClient.createLabelCallable().futureCall(request);
       // Do something.
       Label response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateLabelRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateLabelRequest),[Label](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Label)>` |   
  
### getLabel(@Nullable LabelName name)
    
    
    public final Label getLabel(@Nullable LabelName name)

Retrieves a `Label` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       LabelName name = LabelName.of("[NETWORK_CODE]", "[LABEL]");
       Label response = labelServiceClient.getLabel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.LabelName`  
Required. The resource name of the Label. Format: `networks/{network_code}/labels/{label_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Label](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Label)` |   
  
### getLabel(GetLabelRequest request)
    
    
    public final Label getLabel(GetLabelRequest request)

Retrieves a `Label` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       GetLabelRequest request =
           GetLabelRequest.newBuilder()
               .setName(LabelName.of("[NETWORK_CODE]", "[LABEL]").toString())
               .build();
       Label response = labelServiceClient.getLabel(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLabelRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetLabelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Label](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Label)` |   
  
### getLabel(String name)
    
    
    public final Label getLabel(String name)

Retrieves a `Label` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       String name = LabelName.of("[NETWORK_CODE]", "[LABEL]").toString();
       Label response = labelServiceClient.getLabel(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Label. Format: `networks/{network_code}/labels/{label_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Label](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Label)` |   
  
### getLabelCallable()
    
    
    public final UnaryCallable<GetLabelRequest,Label> getLabelCallable()

Retrieves a `Label` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       GetLabelRequest request =
           GetLabelRequest.newBuilder()
               .setName(LabelName.of("[NETWORK_CODE]", "[LABEL]").toString())
               .build();
       ApiFuture<Label> future = labelServiceClient.getLabelCallable().futureCall(request);
       // Do something.
       Label response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLabelRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetLabelRequest),[Label](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Label)>` |   
  
### getSettings()
    
    
    public final @Nullable LabelServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.LabelServiceSettings` |   
  
### getStub()
    
    
    public LabelServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[LabelServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.LabelServiceStub)` |   
  
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
  
### listLabels(@Nullable NetworkName parent)
    
    
    public final LabelServiceClient.ListLabelsPagedResponse listLabels(@Nullable NetworkName parent)

Lists `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (Label element : labelServiceClient.listLabels(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Labels. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[LabelServiceClient.ListLabelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LabelServiceClient.ListLabelsPagedResponse)` |   
  
### listLabels(ListLabelsRequest request)
    
    
    public final LabelServiceClient.ListLabelsPagedResponse listLabels(ListLabelsRequest request)

Lists `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       ListLabelsRequest request =
           ListLabelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (Label element : labelServiceClient.listLabels(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLabelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListLabelsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LabelServiceClient.ListLabelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LabelServiceClient.ListLabelsPagedResponse)` |   
  
### listLabels(String parent)
    
    
    public final LabelServiceClient.ListLabelsPagedResponse listLabels(String parent)

Lists `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (Label element : labelServiceClient.listLabels(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Labels. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[LabelServiceClient.ListLabelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LabelServiceClient.ListLabelsPagedResponse)` |   
  
### listLabelsCallable()
    
    
    public final UnaryCallable<ListLabelsRequest,ListLabelsResponse> listLabelsCallable()

Lists `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       ListLabelsRequest request =
           ListLabelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListLabelsResponse response = labelServiceClient.listLabelsCallable().call(request);
         for (Label element : response.getLabelsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLabelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListLabelsRequest),[ListLabelsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListLabelsResponse)>` |   
  
### listLabelsPagedCallable()
    
    
    public final UnaryCallable<ListLabelsRequest,LabelServiceClient.ListLabelsPagedResponse> listLabelsPagedCallable()

Lists `Label` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       ListLabelsRequest request =
           ListLabelsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<Label> future = labelServiceClient.listLabelsPagedCallable().futureCall(request);
       // Do something.
       for (Label element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLabelsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListLabelsRequest),[ListLabelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LabelServiceClient.ListLabelsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateLabel(Label label, FieldMask updateMask)
    
    
    public final Label updateLabel(Label label, FieldMask updateMask)

Updates a `Label` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       Label label = Label.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Label response = labelServiceClient.updateLabel(label, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`label` | `[Label](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Label)`  
Required. The `Label` to update. The `Label`'s `name` is used to identify the `Label` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[Label](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Label)` |   
  
### updateLabel(UpdateLabelRequest request)
    
    
    public final Label updateLabel(UpdateLabelRequest request)

Updates a `Label` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       UpdateLabelRequest request =
           UpdateLabelRequest.newBuilder()
               .setLabel(Label.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Label response = labelServiceClient.updateLabel(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateLabelRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateLabelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Label](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Label)` |   
  
### updateLabelCallable()
    
    
    public final UnaryCallable<UpdateLabelRequest,Label> updateLabelCallable()

Updates a `Label` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LabelServiceClient labelServiceClient = LabelServiceClient.create()) {
       UpdateLabelRequest request =
           UpdateLabelRequest.newBuilder()
               .setLabel(Label.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Label> future = labelServiceClient.updateLabelCallable().futureCall(request);
       // Do something.
       Label response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateLabelRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateLabelRequest),[Label](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Label)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
