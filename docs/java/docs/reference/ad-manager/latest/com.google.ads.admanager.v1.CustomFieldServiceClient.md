---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomFieldServiceClient
title: Class CustomFieldServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:40.022093+00:00
---

# Class CustomFieldServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomFieldServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CustomFieldServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/CustomFieldServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `CustomField` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       CustomFieldName name = CustomFieldName.of("[NETWORK_CODE]", "[CUSTOM_FIELD]");
       CustomField response = customFieldServiceClient.getCustomField(name);
     }
     

Note: close() needs to be called on the CustomFieldServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetCustomField |  Retrieves a `CustomField` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCustomField(GetCustomFieldRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCustomField(CustomFieldName name) 
  * getCustomField(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCustomFieldCallable() 

  
ListCustomFields |  Lists `CustomField` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCustomFields(ListCustomFieldsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCustomFields(NetworkName parent) 
  * listCustomFields(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCustomFieldsPagedCallable() 
  * listCustomFieldsCallable() 

  
CreateCustomField |  Creates a `CustomField` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCustomField(CreateCustomFieldRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createCustomField(NetworkName parent, CustomField customField) 
  * createCustomField(String parent, CustomField customField) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCustomFieldCallable() 

  
BatchCreateCustomFields |  Creates `CustomField` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateCustomFields(NetworkName parent, List<CreateCustomFieldRequest> requests) 
  * batchCreateCustomFields(String parent, List<CreateCustomFieldRequest> requests) 
  * batchCreateCustomFields(BatchCreateCustomFieldsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateCustomFieldsCallable() 

  
UpdateCustomField |  Updates a `CustomField` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCustomField(UpdateCustomFieldRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateCustomField(CustomField customField, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCustomFieldCallable() 

  
BatchUpdateCustomFields |  Batch updates `CustomField` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateCustomFields(NetworkName parent, List<UpdateCustomFieldRequest> requests) 
  * batchUpdateCustomFields(String parent, List<UpdateCustomFieldRequest> requests) 
  * batchUpdateCustomFields(BatchUpdateCustomFieldsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateCustomFieldsCallable() 

  
BatchActivateCustomFields |  Activates a list of `CustomField` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateCustomFields(BatchActivateCustomFieldsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchActivateCustomFields(NetworkName parent, List<String> names) 
  * batchActivateCustomFields(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateCustomFieldsCallable() 

  
BatchDeactivateCustomFields |  Deactivates a list of `CustomField` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivateCustomFields(BatchDeactivateCustomFieldsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeactivateCustomFields(NetworkName parent, List<String> names) 
  * batchDeactivateCustomFields(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivateCustomFieldsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CustomFieldServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CustomFieldServiceSettings customFieldServiceSettings =
         CustomFieldServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CustomFieldServiceClient customFieldServiceClient =
         CustomFieldServiceClient.create(customFieldServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CustomFieldServiceSettings customFieldServiceSettings =
         CustomFieldServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CustomFieldServiceClient customFieldServiceClient =
         CustomFieldServiceClient.create(customFieldServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CustomFieldServiceClient

## Static Methods 

### create()
    
    
    public static final CustomFieldServiceClient create()

Constructs an instance of CustomFieldServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CustomFieldServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomFieldServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CustomFieldServiceSettings settings)
    
    
    public static final CustomFieldServiceClient create(CustomFieldServiceSettings settings)

Constructs an instance of CustomFieldServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CustomFieldServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomFieldServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CustomFieldServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomFieldServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CustomFieldServiceStub stub)
    
    
    public static final CustomFieldServiceClient create(CustomFieldServiceStub stub)

Constructs an instance of CustomFieldServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CustomFieldServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CustomFieldServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CustomFieldServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CustomFieldServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomFieldServiceClient)` |   
  
## Constructors 

### CustomFieldServiceClient(CustomFieldServiceSettings settings)
    
    
    protected CustomFieldServiceClient(CustomFieldServiceSettings settings)

Constructs an instance of CustomFieldServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CustomFieldServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomFieldServiceSettings)`  
  
  
### CustomFieldServiceClient(CustomFieldServiceStub stub)
    
    
    protected CustomFieldServiceClient(CustomFieldServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CustomFieldServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CustomFieldServiceStub)`  
  
  
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
  
### batchActivateCustomFields(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchActivateCustomFieldsResponse batchActivateCustomFields(@Nullable NetworkName parent, List<String> names)

Activates a list of `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchActivateCustomFieldsResponse response =
           customFieldServiceClient.batchActivateCustomFields(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CustomField` objects to activate. Format: `networks/{network_code}/customFields/{custom_field_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomFieldsResponse)` |   
  
### batchActivateCustomFields(BatchActivateCustomFieldsRequest request)
    
    
    public final BatchActivateCustomFieldsResponse batchActivateCustomFields(BatchActivateCustomFieldsRequest request)

Activates a list of `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       BatchActivateCustomFieldsRequest request =
           BatchActivateCustomFieldsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchActivateCustomFieldsResponse response =
           customFieldServiceClient.batchActivateCustomFields(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateCustomFieldsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomFieldsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomFieldsResponse)` |   
  
### batchActivateCustomFields(String parent, List<String> names)
    
    
    public final BatchActivateCustomFieldsResponse batchActivateCustomFields(String parent, List<String> names)

Activates a list of `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchActivateCustomFieldsResponse response =
           customFieldServiceClient.batchActivateCustomFields(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CustomField` objects to activate. Format: `networks/{network_code}/customFields/{custom_field_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomFieldsResponse)` |   
  
### batchActivateCustomFieldsCallable()
    
    
    public final UnaryCallable<BatchActivateCustomFieldsRequest,BatchActivateCustomFieldsResponse> batchActivateCustomFieldsCallable()

Activates a list of `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       BatchActivateCustomFieldsRequest request =
           BatchActivateCustomFieldsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchActivateCustomFieldsResponse> future =
           customFieldServiceClient.batchActivateCustomFieldsCallable().futureCall(request);
       // Do something.
       BatchActivateCustomFieldsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateCustomFieldsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomFieldsRequest),[BatchActivateCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomFieldsResponse)>` |   
  
### batchCreateCustomFields(@Nullable NetworkName parent, List<CreateCustomFieldRequest> requests)
    
    
    public final BatchCreateCustomFieldsResponse batchCreateCustomFields(@Nullable NetworkName parent, List<CreateCustomFieldRequest> requests)

Creates `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateCustomFieldRequest> requests = new ArrayList<>();
       BatchCreateCustomFieldsResponse response =
           customFieldServiceClient.batchCreateCustomFields(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `CustomFields` will be created. Format: `networks/{network_code}` The parent field in the CreateCustomFieldRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateCustomFieldRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCustomFieldRequest)>`  
Required. The `CustomField` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomFieldsResponse)` |   
  
### batchCreateCustomFields(BatchCreateCustomFieldsRequest request)
    
    
    public final BatchCreateCustomFieldsResponse batchCreateCustomFields(BatchCreateCustomFieldsRequest request)

Creates `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       BatchCreateCustomFieldsRequest request =
           BatchCreateCustomFieldsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateCustomFieldRequest>())
               .build();
       BatchCreateCustomFieldsResponse response =
           customFieldServiceClient.batchCreateCustomFields(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateCustomFieldsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomFieldsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomFieldsResponse)` |   
  
### batchCreateCustomFields(String parent, List<CreateCustomFieldRequest> requests)
    
    
    public final BatchCreateCustomFieldsResponse batchCreateCustomFields(String parent, List<CreateCustomFieldRequest> requests)

Creates `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateCustomFieldRequest> requests = new ArrayList<>();
       BatchCreateCustomFieldsResponse response =
           customFieldServiceClient.batchCreateCustomFields(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `CustomFields` will be created. Format: `networks/{network_code}` The parent field in the CreateCustomFieldRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateCustomFieldRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCustomFieldRequest)>`  
Required. The `CustomField` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomFieldsResponse)` |   
  
### batchCreateCustomFieldsCallable()
    
    
    public final UnaryCallable<BatchCreateCustomFieldsRequest,BatchCreateCustomFieldsResponse> batchCreateCustomFieldsCallable()

Creates `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       BatchCreateCustomFieldsRequest request =
           BatchCreateCustomFieldsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateCustomFieldRequest>())
               .build();
       ApiFuture<BatchCreateCustomFieldsResponse> future =
           customFieldServiceClient.batchCreateCustomFieldsCallable().futureCall(request);
       // Do something.
       BatchCreateCustomFieldsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateCustomFieldsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomFieldsRequest),[BatchCreateCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomFieldsResponse)>` |   
  
### batchDeactivateCustomFields(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDeactivateCustomFieldsResponse batchDeactivateCustomFields(@Nullable NetworkName parent, List<String> names)

Deactivates a list of `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDeactivateCustomFieldsResponse response =
           customFieldServiceClient.batchDeactivateCustomFields(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CustomField` objects to deactivate. Format: `networks/{network_code}/customFields/{custom_field_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomFieldsResponse)` |   
  
### batchDeactivateCustomFields(BatchDeactivateCustomFieldsRequest request)
    
    
    public final BatchDeactivateCustomFieldsResponse batchDeactivateCustomFields(BatchDeactivateCustomFieldsRequest request)

Deactivates a list of `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       BatchDeactivateCustomFieldsRequest request =
           BatchDeactivateCustomFieldsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeactivateCustomFieldsResponse response =
           customFieldServiceClient.batchDeactivateCustomFields(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivateCustomFieldsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomFieldsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomFieldsResponse)` |   
  
### batchDeactivateCustomFields(String parent, List<String> names)
    
    
    public final BatchDeactivateCustomFieldsResponse batchDeactivateCustomFields(String parent, List<String> names)

Deactivates a list of `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDeactivateCustomFieldsResponse response =
           customFieldServiceClient.batchDeactivateCustomFields(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CustomField` objects to deactivate. Format: `networks/{network_code}/customFields/{custom_field_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomFieldsResponse)` |   
  
### batchDeactivateCustomFieldsCallable()
    
    
    public final UnaryCallable<BatchDeactivateCustomFieldsRequest,BatchDeactivateCustomFieldsResponse> batchDeactivateCustomFieldsCallable()

Deactivates a list of `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       BatchDeactivateCustomFieldsRequest request =
           BatchDeactivateCustomFieldsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDeactivateCustomFieldsResponse> future =
           customFieldServiceClient.batchDeactivateCustomFieldsCallable().futureCall(request);
       // Do something.
       BatchDeactivateCustomFieldsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivateCustomFieldsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomFieldsRequest),[BatchDeactivateCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomFieldsResponse)>` |   
  
### batchUpdateCustomFields(@Nullable NetworkName parent, List<UpdateCustomFieldRequest> requests)
    
    
    public final BatchUpdateCustomFieldsResponse batchUpdateCustomFields(@Nullable NetworkName parent, List<UpdateCustomFieldRequest> requests)

Batch updates `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateCustomFieldRequest> requests = new ArrayList<>();
       BatchUpdateCustomFieldsResponse response =
           customFieldServiceClient.batchUpdateCustomFields(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `CustomFields` will be updated. Format: `networks/{network_code}` The parent field in the UpdateCustomFieldRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateCustomFieldRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCustomFieldRequest)>`  
Required. The `CustomField` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomFieldsResponse)` |   
  
### batchUpdateCustomFields(BatchUpdateCustomFieldsRequest request)
    
    
    public final BatchUpdateCustomFieldsResponse batchUpdateCustomFields(BatchUpdateCustomFieldsRequest request)

Batch updates `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       BatchUpdateCustomFieldsRequest request =
           BatchUpdateCustomFieldsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateCustomFieldRequest>())
               .build();
       BatchUpdateCustomFieldsResponse response =
           customFieldServiceClient.batchUpdateCustomFields(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateCustomFieldsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomFieldsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomFieldsResponse)` |   
  
### batchUpdateCustomFields(String parent, List<UpdateCustomFieldRequest> requests)
    
    
    public final BatchUpdateCustomFieldsResponse batchUpdateCustomFields(String parent, List<UpdateCustomFieldRequest> requests)

Batch updates `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateCustomFieldRequest> requests = new ArrayList<>();
       BatchUpdateCustomFieldsResponse response =
           customFieldServiceClient.batchUpdateCustomFields(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `CustomFields` will be updated. Format: `networks/{network_code}` The parent field in the UpdateCustomFieldRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateCustomFieldRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCustomFieldRequest)>`  
Required. The `CustomField` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomFieldsResponse)` |   
  
### batchUpdateCustomFieldsCallable()
    
    
    public final UnaryCallable<BatchUpdateCustomFieldsRequest,BatchUpdateCustomFieldsResponse> batchUpdateCustomFieldsCallable()

Batch updates `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       BatchUpdateCustomFieldsRequest request =
           BatchUpdateCustomFieldsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateCustomFieldRequest>())
               .build();
       ApiFuture<BatchUpdateCustomFieldsResponse> future =
           customFieldServiceClient.batchUpdateCustomFieldsCallable().futureCall(request);
       // Do something.
       BatchUpdateCustomFieldsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateCustomFieldsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomFieldsRequest),[BatchUpdateCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomFieldsResponse)>` |   
  
### close()
    
    
    public final void close()

### createCustomField(@Nullable NetworkName parent, CustomField customField)
    
    
    public final CustomField createCustomField(@Nullable NetworkName parent, CustomField customField)

Creates a `CustomField` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       CustomField customField = CustomField.newBuilder().build();
       CustomField response = customFieldServiceClient.createCustomField(parent, customField);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `CustomField` will be created. Format: `networks/{network_code}`  
`customField` | `[CustomField](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomField)`  
Required. The `CustomField` to create.  
**Returns**  
---  
**Type** | **Description**  
`[CustomField](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomField)` |   
  
### createCustomField(CreateCustomFieldRequest request)
    
    
    public final CustomField createCustomField(CreateCustomFieldRequest request)

Creates a `CustomField` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       CreateCustomFieldRequest request =
           CreateCustomFieldRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setCustomField(CustomField.newBuilder().build())
               .build();
       CustomField response = customFieldServiceClient.createCustomField(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCustomFieldRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCustomFieldRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomField](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomField)` |   
  
### createCustomField(String parent, CustomField customField)
    
    
    public final CustomField createCustomField(String parent, CustomField customField)

Creates a `CustomField` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       CustomField customField = CustomField.newBuilder().build();
       CustomField response = customFieldServiceClient.createCustomField(parent, customField);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `CustomField` will be created. Format: `networks/{network_code}`  
`customField` | `[CustomField](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomField)`  
Required. The `CustomField` to create.  
**Returns**  
---  
**Type** | **Description**  
`[CustomField](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomField)` |   
  
### createCustomFieldCallable()
    
    
    public final UnaryCallable<CreateCustomFieldRequest,CustomField> createCustomFieldCallable()

Creates a `CustomField` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       CreateCustomFieldRequest request =
           CreateCustomFieldRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setCustomField(CustomField.newBuilder().build())
               .build();
       ApiFuture<CustomField> future =
           customFieldServiceClient.createCustomFieldCallable().futureCall(request);
       // Do something.
       CustomField response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCustomFieldRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCustomFieldRequest),[CustomField](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomField)>` |   
  
### getCustomField(@Nullable CustomFieldName name)
    
    
    public final CustomField getCustomField(@Nullable CustomFieldName name)

Retrieves a `CustomField` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       CustomFieldName name = CustomFieldName.of("[NETWORK_CODE]", "[CUSTOM_FIELD]");
       CustomField response = customFieldServiceClient.getCustomField(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CustomFieldName`  
Required. The resource name of the CustomField. Format: `networks/{network_code}/customFields/{custom_field_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CustomField](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomField)` |   
  
### getCustomField(GetCustomFieldRequest request)
    
    
    public final CustomField getCustomField(GetCustomFieldRequest request)

Retrieves a `CustomField` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       GetCustomFieldRequest request =
           GetCustomFieldRequest.newBuilder()
               .setName(CustomFieldName.of("[NETWORK_CODE]", "[CUSTOM_FIELD]").toString())
               .build();
       CustomField response = customFieldServiceClient.getCustomField(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCustomFieldRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCustomFieldRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomField](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomField)` |   
  
### getCustomField(String name)
    
    
    public final CustomField getCustomField(String name)

Retrieves a `CustomField` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       String name = CustomFieldName.of("[NETWORK_CODE]", "[CUSTOM_FIELD]").toString();
       CustomField response = customFieldServiceClient.getCustomField(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the CustomField. Format: `networks/{network_code}/customFields/{custom_field_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CustomField](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomField)` |   
  
### getCustomFieldCallable()
    
    
    public final UnaryCallable<GetCustomFieldRequest,CustomField> getCustomFieldCallable()

Retrieves a `CustomField` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       GetCustomFieldRequest request =
           GetCustomFieldRequest.newBuilder()
               .setName(CustomFieldName.of("[NETWORK_CODE]", "[CUSTOM_FIELD]").toString())
               .build();
       ApiFuture<CustomField> future =
           customFieldServiceClient.getCustomFieldCallable().futureCall(request);
       // Do something.
       CustomField response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCustomFieldRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCustomFieldRequest),[CustomField](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomField)>` |   
  
### getSettings()
    
    
    public final @Nullable CustomFieldServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CustomFieldServiceSettings` |   
  
### getStub()
    
    
    public CustomFieldServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CustomFieldServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CustomFieldServiceStub)` |   
  
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
  
### listCustomFields(@Nullable NetworkName parent)
    
    
    public final CustomFieldServiceClient.ListCustomFieldsPagedResponse listCustomFields(@Nullable NetworkName parent)

Lists `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (CustomField element : customFieldServiceClient.listCustomFields(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of CustomFields. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CustomFieldServiceClient.ListCustomFieldsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomFieldServiceClient.ListCustomFieldsPagedResponse)` |   
  
### listCustomFields(ListCustomFieldsRequest request)
    
    
    public final CustomFieldServiceClient.ListCustomFieldsPagedResponse listCustomFields(ListCustomFieldsRequest request)

Lists `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       ListCustomFieldsRequest request =
           ListCustomFieldsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (CustomField element : customFieldServiceClient.listCustomFields(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCustomFieldsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCustomFieldsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomFieldServiceClient.ListCustomFieldsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomFieldServiceClient.ListCustomFieldsPagedResponse)` |   
  
### listCustomFields(String parent)
    
    
    public final CustomFieldServiceClient.ListCustomFieldsPagedResponse listCustomFields(String parent)

Lists `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (CustomField element : customFieldServiceClient.listCustomFields(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of CustomFields. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CustomFieldServiceClient.ListCustomFieldsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomFieldServiceClient.ListCustomFieldsPagedResponse)` |   
  
### listCustomFieldsCallable()
    
    
    public final UnaryCallable<ListCustomFieldsRequest,ListCustomFieldsResponse> listCustomFieldsCallable()

Lists `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       ListCustomFieldsRequest request =
           ListCustomFieldsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListCustomFieldsResponse response =
             customFieldServiceClient.listCustomFieldsCallable().call(request);
         for (CustomField element : response.getCustomFieldsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomFieldsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCustomFieldsRequest),[ListCustomFieldsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCustomFieldsResponse)>` |   
  
### listCustomFieldsPagedCallable()
    
    
    public final UnaryCallable<ListCustomFieldsRequest,CustomFieldServiceClient.ListCustomFieldsPagedResponse> listCustomFieldsPagedCallable()

Lists `CustomField` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       ListCustomFieldsRequest request =
           ListCustomFieldsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<CustomField> future =
           customFieldServiceClient.listCustomFieldsPagedCallable().futureCall(request);
       // Do something.
       for (CustomField element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomFieldsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCustomFieldsRequest),[ListCustomFieldsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomFieldServiceClient.ListCustomFieldsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateCustomField(CustomField customField, FieldMask updateMask)
    
    
    public final CustomField updateCustomField(CustomField customField, FieldMask updateMask)

Updates a `CustomField` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       CustomField customField = CustomField.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       CustomField response = customFieldServiceClient.updateCustomField(customField, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`customField` | `[CustomField](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomField)`  
Required. The `CustomField` to update. The `CustomField`'s `name` is used to identify the `CustomField` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[CustomField](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomField)` |   
  
### updateCustomField(UpdateCustomFieldRequest request)
    
    
    public final CustomField updateCustomField(UpdateCustomFieldRequest request)

Updates a `CustomField` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       UpdateCustomFieldRequest request =
           UpdateCustomFieldRequest.newBuilder()
               .setCustomField(CustomField.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       CustomField response = customFieldServiceClient.updateCustomField(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCustomFieldRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCustomFieldRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomField](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomField)` |   
  
### updateCustomFieldCallable()
    
    
    public final UnaryCallable<UpdateCustomFieldRequest,CustomField> updateCustomFieldCallable()

Updates a `CustomField` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomFieldServiceClient customFieldServiceClient = CustomFieldServiceClient.create()) {
       UpdateCustomFieldRequest request =
           UpdateCustomFieldRequest.newBuilder()
               .setCustomField(CustomField.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<CustomField> future =
           customFieldServiceClient.updateCustomFieldCallable().futureCall(request);
       // Do something.
       CustomField response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCustomFieldRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCustomFieldRequest),[CustomField](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomField)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
