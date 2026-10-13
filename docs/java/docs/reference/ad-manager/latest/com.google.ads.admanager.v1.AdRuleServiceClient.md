---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRuleServiceClient
title: Class AdRuleServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:21.066345+00:00
---

# Class AdRuleServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRuleServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AdRuleServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/AdRuleServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `AdRule` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       AdRuleName name = AdRuleName.of("[NETWORK_CODE]", "[AD_RULE]");
       AdRule response = adRuleServiceClient.getAdRule(name);
     }
     

Note: close() needs to be called on the AdRuleServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetAdRule |  Retrieves an `AdRule` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAdRule(GetAdRuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAdRule(AdRuleName name) 
  * getAdRule(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAdRuleCallable() 

  
ListAdRules |  Lists `AdRule` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAdRules(ListAdRulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAdRules(NetworkName parent) 
  * listAdRules(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAdRulesPagedCallable() 
  * listAdRulesCallable() 

  
CreateAdRule |  Creates a `AdRule` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAdRule(CreateAdRuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createAdRule(NetworkName parent, AdRule adRule) 
  * createAdRule(String parent, AdRule adRule) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAdRuleCallable() 

  
BatchCreateAdRules |  Batch creates `AdRule` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateAdRules(NetworkName parent, List<CreateAdRuleRequest> requests) 
  * batchCreateAdRules(String parent, List<CreateAdRuleRequest> requests) 
  * batchCreateAdRules(BatchCreateAdRulesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateAdRulesCallable() 

  
UpdateAdRule |  Updates a `AdRule` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAdRule(UpdateAdRuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateAdRule(AdRule adRule, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAdRuleCallable() 

  
BatchUpdateAdRules |  Batch updates `AdRule` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateAdRules(NetworkName parent, List<UpdateAdRuleRequest> requests) 
  * batchUpdateAdRules(String parent, List<UpdateAdRuleRequest> requests) 
  * batchUpdateAdRules(BatchUpdateAdRulesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateAdRulesCallable() 

  
BatchActivateAdRules |  Activates a list of `AdRule` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateAdRules(BatchActivateAdRulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchActivateAdRules(NetworkName parent, List<String> names) 
  * batchActivateAdRules(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateAdRulesCallable() 

  
BatchDeactivateAdRules |  Deactivates a list of `AdRule` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivateAdRules(BatchDeactivateAdRulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeactivateAdRules(NetworkName parent, List<String> names) 
  * batchDeactivateAdRules(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivateAdRulesCallable() 

  
BatchDeleteAdRules |  Deletes a list of `AdRule` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeleteAdRules(BatchDeleteAdRulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeleteAdRules(NetworkName parent, List<String> names) 
  * batchDeleteAdRules(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeleteAdRulesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AdRuleServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AdRuleServiceSettings adRuleServiceSettings =
         AdRuleServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create(adRuleServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AdRuleServiceSettings adRuleServiceSettings =
         AdRuleServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create(adRuleServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AdRuleServiceClient

## Static Methods 

### create()
    
    
    public static final AdRuleServiceClient create()

Constructs an instance of AdRuleServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AdRuleServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRuleServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AdRuleServiceSettings settings)
    
    
    public static final AdRuleServiceClient create(AdRuleServiceSettings settings)

Constructs an instance of AdRuleServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AdRuleServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRuleServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdRuleServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRuleServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AdRuleServiceStub stub)
    
    
    public static final AdRuleServiceClient create(AdRuleServiceStub stub)

Constructs an instance of AdRuleServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(AdRuleServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AdRuleServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AdRuleServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdRuleServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRuleServiceClient)` |   
  
## Constructors 

### AdRuleServiceClient(AdRuleServiceSettings settings)
    
    
    protected AdRuleServiceClient(AdRuleServiceSettings settings)

Constructs an instance of AdRuleServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AdRuleServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRuleServiceSettings)`  
  
  
### AdRuleServiceClient(AdRuleServiceStub stub)
    
    
    protected AdRuleServiceClient(AdRuleServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AdRuleServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AdRuleServiceStub)`  
  
  
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
  
### batchActivateAdRules(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchActivateAdRulesResponse batchActivateAdRules(@Nullable NetworkName parent, List<String> names)

Activates a list of `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchActivateAdRulesResponse response =
           adRuleServiceClient.batchActivateAdRules(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the AdRule. Format: `networks/{network_code}/adRules/{ad_rule}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAdRulesResponse)` |   
  
### batchActivateAdRules(BatchActivateAdRulesRequest request)
    
    
    public final BatchActivateAdRulesResponse batchActivateAdRules(BatchActivateAdRulesRequest request)

Activates a list of `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       BatchActivateAdRulesRequest request =
           BatchActivateAdRulesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchActivateAdRulesResponse response = adRuleServiceClient.batchActivateAdRules(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateAdRulesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAdRulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAdRulesResponse)` |   
  
### batchActivateAdRules(String parent, List<String> names)
    
    
    public final BatchActivateAdRulesResponse batchActivateAdRules(String parent, List<String> names)

Activates a list of `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchActivateAdRulesResponse response =
           adRuleServiceClient.batchActivateAdRules(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the AdRule. Format: `networks/{network_code}/adRules/{ad_rule}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAdRulesResponse)` |   
  
### batchActivateAdRulesCallable()
    
    
    public final UnaryCallable<BatchActivateAdRulesRequest,BatchActivateAdRulesResponse> batchActivateAdRulesCallable()

Activates a list of `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       BatchActivateAdRulesRequest request =
           BatchActivateAdRulesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchActivateAdRulesResponse> future =
           adRuleServiceClient.batchActivateAdRulesCallable().futureCall(request);
       // Do something.
       BatchActivateAdRulesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateAdRulesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAdRulesRequest),[BatchActivateAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAdRulesResponse)>` |   
  
### batchCreateAdRules(@Nullable NetworkName parent, List<CreateAdRuleRequest> requests)
    
    
    public final BatchCreateAdRulesResponse batchCreateAdRules(@Nullable NetworkName parent, List<CreateAdRuleRequest> requests)

Batch creates `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateAdRuleRequest> requests = new ArrayList<>();
       BatchCreateAdRulesResponse response =
           adRuleServiceClient.batchCreateAdRules(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `AdRules` will be created. Format: `networks/{network_code}` The parent field in the CreateAdRuleRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateAdRuleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAdRuleRequest)>`  
Required. The `AdRule` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdRulesResponse)` |   
  
### batchCreateAdRules(BatchCreateAdRulesRequest request)
    
    
    public final BatchCreateAdRulesResponse batchCreateAdRules(BatchCreateAdRulesRequest request)

Batch creates `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       BatchCreateAdRulesRequest request =
           BatchCreateAdRulesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateAdRuleRequest>())
               .build();
       BatchCreateAdRulesResponse response = adRuleServiceClient.batchCreateAdRules(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateAdRulesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdRulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdRulesResponse)` |   
  
### batchCreateAdRules(String parent, List<CreateAdRuleRequest> requests)
    
    
    public final BatchCreateAdRulesResponse batchCreateAdRules(String parent, List<CreateAdRuleRequest> requests)

Batch creates `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateAdRuleRequest> requests = new ArrayList<>();
       BatchCreateAdRulesResponse response =
           adRuleServiceClient.batchCreateAdRules(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `AdRules` will be created. Format: `networks/{network_code}` The parent field in the CreateAdRuleRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateAdRuleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAdRuleRequest)>`  
Required. The `AdRule` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdRulesResponse)` |   
  
### batchCreateAdRulesCallable()
    
    
    public final UnaryCallable<BatchCreateAdRulesRequest,BatchCreateAdRulesResponse> batchCreateAdRulesCallable()

Batch creates `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       BatchCreateAdRulesRequest request =
           BatchCreateAdRulesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateAdRuleRequest>())
               .build();
       ApiFuture<BatchCreateAdRulesResponse> future =
           adRuleServiceClient.batchCreateAdRulesCallable().futureCall(request);
       // Do something.
       BatchCreateAdRulesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateAdRulesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdRulesRequest),[BatchCreateAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdRulesResponse)>` |   
  
### batchDeactivateAdRules(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDeactivateAdRulesResponse batchDeactivateAdRules(@Nullable NetworkName parent, List<String> names)

Deactivates a list of `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDeactivateAdRulesResponse response =
           adRuleServiceClient.batchDeactivateAdRules(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the AdRule. Format: `networks/{network_code}/adRules/{ad_rule}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAdRulesResponse)` |   
  
### batchDeactivateAdRules(BatchDeactivateAdRulesRequest request)
    
    
    public final BatchDeactivateAdRulesResponse batchDeactivateAdRules(BatchDeactivateAdRulesRequest request)

Deactivates a list of `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       BatchDeactivateAdRulesRequest request =
           BatchDeactivateAdRulesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeactivateAdRulesResponse response = adRuleServiceClient.batchDeactivateAdRules(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivateAdRulesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAdRulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAdRulesResponse)` |   
  
### batchDeactivateAdRules(String parent, List<String> names)
    
    
    public final BatchDeactivateAdRulesResponse batchDeactivateAdRules(String parent, List<String> names)

Deactivates a list of `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDeactivateAdRulesResponse response =
           adRuleServiceClient.batchDeactivateAdRules(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the AdRule. Format: `networks/{network_code}/adRules/{ad_rule}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAdRulesResponse)` |   
  
### batchDeactivateAdRulesCallable()
    
    
    public final UnaryCallable<BatchDeactivateAdRulesRequest,BatchDeactivateAdRulesResponse> batchDeactivateAdRulesCallable()

Deactivates a list of `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       BatchDeactivateAdRulesRequest request =
           BatchDeactivateAdRulesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDeactivateAdRulesResponse> future =
           adRuleServiceClient.batchDeactivateAdRulesCallable().futureCall(request);
       // Do something.
       BatchDeactivateAdRulesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivateAdRulesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAdRulesRequest),[BatchDeactivateAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAdRulesResponse)>` |   
  
### batchDeleteAdRules(@Nullable NetworkName parent, List<String> names)
    
    
    public final void batchDeleteAdRules(@Nullable NetworkName parent, List<String> names)

Deletes a list of `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       adRuleServiceClient.batchDeleteAdRules(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the AdRule. Format: `networks/{network_code}/adRules/{ad_rule}`  
  
### batchDeleteAdRules(BatchDeleteAdRulesRequest request)
    
    
    public final void batchDeleteAdRules(BatchDeleteAdRulesRequest request)

Deletes a list of `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       BatchDeleteAdRulesRequest request =
           BatchDeleteAdRulesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       adRuleServiceClient.batchDeleteAdRules(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteAdRulesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeleteAdRulesRequest)`  
The request object containing all of the parameters for the API call.  
  
### batchDeleteAdRules(String parent, List<String> names)
    
    
    public final void batchDeleteAdRules(String parent, List<String> names)

Deletes a list of `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       adRuleServiceClient.batchDeleteAdRules(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the AdRule. Format: `networks/{network_code}/adRules/{ad_rule}`  
  
### batchDeleteAdRulesCallable()
    
    
    public final UnaryCallable<BatchDeleteAdRulesRequest,Empty> batchDeleteAdRulesCallable()

Deletes a list of `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       BatchDeleteAdRulesRequest request =
           BatchDeleteAdRulesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<Empty> future =
           adRuleServiceClient.batchDeleteAdRulesCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeleteAdRulesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeleteAdRulesRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### batchUpdateAdRules(@Nullable NetworkName parent, List<UpdateAdRuleRequest> requests)
    
    
    public final BatchUpdateAdRulesResponse batchUpdateAdRules(@Nullable NetworkName parent, List<UpdateAdRuleRequest> requests)

Batch updates `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateAdRuleRequest> requests = new ArrayList<>();
       BatchUpdateAdRulesResponse response =
           adRuleServiceClient.batchUpdateAdRules(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `AdRules` will be updated. Format: `networks/{network_code}` The parent field in the UpdateAdRuleRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateAdRuleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateAdRuleRequest)>`  
Required. The `AdRule` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdRulesResponse)` |   
  
### batchUpdateAdRules(BatchUpdateAdRulesRequest request)
    
    
    public final BatchUpdateAdRulesResponse batchUpdateAdRules(BatchUpdateAdRulesRequest request)

Batch updates `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       BatchUpdateAdRulesRequest request =
           BatchUpdateAdRulesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateAdRuleRequest>())
               .build();
       BatchUpdateAdRulesResponse response = adRuleServiceClient.batchUpdateAdRules(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateAdRulesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdRulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdRulesResponse)` |   
  
### batchUpdateAdRules(String parent, List<UpdateAdRuleRequest> requests)
    
    
    public final BatchUpdateAdRulesResponse batchUpdateAdRules(String parent, List<UpdateAdRuleRequest> requests)

Batch updates `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateAdRuleRequest> requests = new ArrayList<>();
       BatchUpdateAdRulesResponse response =
           adRuleServiceClient.batchUpdateAdRules(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `AdRules` will be updated. Format: `networks/{network_code}` The parent field in the UpdateAdRuleRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateAdRuleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateAdRuleRequest)>`  
Required. The `AdRule` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdRulesResponse)` |   
  
### batchUpdateAdRulesCallable()
    
    
    public final UnaryCallable<BatchUpdateAdRulesRequest,BatchUpdateAdRulesResponse> batchUpdateAdRulesCallable()

Batch updates `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       BatchUpdateAdRulesRequest request =
           BatchUpdateAdRulesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateAdRuleRequest>())
               .build();
       ApiFuture<BatchUpdateAdRulesResponse> future =
           adRuleServiceClient.batchUpdateAdRulesCallable().futureCall(request);
       // Do something.
       BatchUpdateAdRulesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateAdRulesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdRulesRequest),[BatchUpdateAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdRulesResponse)>` |   
  
### close()
    
    
    public final void close()

### createAdRule(@Nullable NetworkName parent, AdRule adRule)
    
    
    public final AdRule createAdRule(@Nullable NetworkName parent, AdRule adRule)

Creates a `AdRule` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       AdRule adRule = AdRule.newBuilder().build();
       AdRule response = adRuleServiceClient.createAdRule(parent, adRule);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `AdRule` will be created. Format: `networks/{network_code}`  
`adRule` | `[AdRule](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRule)`  
Required. The `AdRule` to create.  
**Returns**  
---  
**Type** | **Description**  
`[AdRule](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRule)` |   
  
### createAdRule(CreateAdRuleRequest request)
    
    
    public final AdRule createAdRule(CreateAdRuleRequest request)

Creates a `AdRule` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       CreateAdRuleRequest request =
           CreateAdRuleRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setAdRule(AdRule.newBuilder().build())
               .build();
       AdRule response = adRuleServiceClient.createAdRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAdRuleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAdRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdRule](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRule)` |   
  
### createAdRule(String parent, AdRule adRule)
    
    
    public final AdRule createAdRule(String parent, AdRule adRule)

Creates a `AdRule` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       AdRule adRule = AdRule.newBuilder().build();
       AdRule response = adRuleServiceClient.createAdRule(parent, adRule);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `AdRule` will be created. Format: `networks/{network_code}`  
`adRule` | `[AdRule](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRule)`  
Required. The `AdRule` to create.  
**Returns**  
---  
**Type** | **Description**  
`[AdRule](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRule)` |   
  
### createAdRuleCallable()
    
    
    public final UnaryCallable<CreateAdRuleRequest,AdRule> createAdRuleCallable()

Creates a `AdRule` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       CreateAdRuleRequest request =
           CreateAdRuleRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setAdRule(AdRule.newBuilder().build())
               .build();
       ApiFuture<AdRule> future = adRuleServiceClient.createAdRuleCallable().futureCall(request);
       // Do something.
       AdRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAdRuleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAdRuleRequest),[AdRule](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRule)>` |   
  
### getAdRule(@Nullable AdRuleName name)
    
    
    public final AdRule getAdRule(@Nullable AdRuleName name)

Retrieves an `AdRule` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       AdRuleName name = AdRuleName.of("[NETWORK_CODE]", "[AD_RULE]");
       AdRule response = adRuleServiceClient.getAdRule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.AdRuleName`  
Required. The resource name of the AdRule. Format: `networks/{network_code}/adRules/{ad_rule_id}`  
**Returns**  
---  
**Type** | **Description**  
`[AdRule](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRule)` |   
  
### getAdRule(GetAdRuleRequest request)
    
    
    public final AdRule getAdRule(GetAdRuleRequest request)

Retrieves an `AdRule` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       GetAdRuleRequest request =
           GetAdRuleRequest.newBuilder()
               .setName(AdRuleName.of("[NETWORK_CODE]", "[AD_RULE]").toString())
               .build();
       AdRule response = adRuleServiceClient.getAdRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAdRuleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetAdRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdRule](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRule)` |   
  
### getAdRule(String name)
    
    
    public final AdRule getAdRule(String name)

Retrieves an `AdRule` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       String name = AdRuleName.of("[NETWORK_CODE]", "[AD_RULE]").toString();
       AdRule response = adRuleServiceClient.getAdRule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the AdRule. Format: `networks/{network_code}/adRules/{ad_rule_id}`  
**Returns**  
---  
**Type** | **Description**  
`[AdRule](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRule)` |   
  
### getAdRuleCallable()
    
    
    public final UnaryCallable<GetAdRuleRequest,AdRule> getAdRuleCallable()

Retrieves an `AdRule` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       GetAdRuleRequest request =
           GetAdRuleRequest.newBuilder()
               .setName(AdRuleName.of("[NETWORK_CODE]", "[AD_RULE]").toString())
               .build();
       ApiFuture<AdRule> future = adRuleServiceClient.getAdRuleCallable().futureCall(request);
       // Do something.
       AdRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAdRuleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetAdRuleRequest),[AdRule](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRule)>` |   
  
### getSettings()
    
    
    public final @Nullable AdRuleServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.AdRuleServiceSettings` |   
  
### getStub()
    
    
    public AdRuleServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AdRuleServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AdRuleServiceStub)` |   
  
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
  
### listAdRules(@Nullable NetworkName parent)
    
    
    public final AdRuleServiceClient.ListAdRulesPagedResponse listAdRules(@Nullable NetworkName parent)

Lists `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (AdRule element : adRuleServiceClient.listAdRules(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of AdRules. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[AdRuleServiceClient.ListAdRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRuleServiceClient.ListAdRulesPagedResponse)` |   
  
### listAdRules(ListAdRulesRequest request)
    
    
    public final AdRuleServiceClient.ListAdRulesPagedResponse listAdRules(ListAdRulesRequest request)

Lists `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       ListAdRulesRequest request =
           ListAdRulesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (AdRule element : adRuleServiceClient.listAdRules(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAdRulesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdRulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdRuleServiceClient.ListAdRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRuleServiceClient.ListAdRulesPagedResponse)` |   
  
### listAdRules(String parent)
    
    
    public final AdRuleServiceClient.ListAdRulesPagedResponse listAdRules(String parent)

Lists `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (AdRule element : adRuleServiceClient.listAdRules(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of AdRules. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[AdRuleServiceClient.ListAdRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRuleServiceClient.ListAdRulesPagedResponse)` |   
  
### listAdRulesCallable()
    
    
    public final UnaryCallable<ListAdRulesRequest,ListAdRulesResponse> listAdRulesCallable()

Lists `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       ListAdRulesRequest request =
           ListAdRulesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListAdRulesResponse response = adRuleServiceClient.listAdRulesCallable().call(request);
         for (AdRule element : response.getAdRulesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAdRulesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdRulesRequest),[ListAdRulesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdRulesResponse)>` |   
  
### listAdRulesPagedCallable()
    
    
    public final UnaryCallable<ListAdRulesRequest,AdRuleServiceClient.ListAdRulesPagedResponse> listAdRulesPagedCallable()

Lists `AdRule` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       ListAdRulesRequest request =
           ListAdRulesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<AdRule> future = adRuleServiceClient.listAdRulesPagedCallable().futureCall(request);
       // Do something.
       for (AdRule element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAdRulesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdRulesRequest),[ListAdRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRuleServiceClient.ListAdRulesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateAdRule(AdRule adRule, FieldMask updateMask)
    
    
    public final AdRule updateAdRule(AdRule adRule, FieldMask updateMask)

Updates a `AdRule` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       AdRule adRule = AdRule.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AdRule response = adRuleServiceClient.updateAdRule(adRule, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`adRule` | `[AdRule](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRule)`  
Required. The `AdRule` to update. The `AdRule`'s `name` is used to identify the `AdRule` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[AdRule](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRule)` |   
  
### updateAdRule(UpdateAdRuleRequest request)
    
    
    public final AdRule updateAdRule(UpdateAdRuleRequest request)

Updates a `AdRule` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       UpdateAdRuleRequest request =
           UpdateAdRuleRequest.newBuilder()
               .setAdRule(AdRule.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       AdRule response = adRuleServiceClient.updateAdRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAdRuleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateAdRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdRule](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRule)` |   
  
### updateAdRuleCallable()
    
    
    public final UnaryCallable<UpdateAdRuleRequest,AdRule> updateAdRuleCallable()

Updates a `AdRule` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdRuleServiceClient adRuleServiceClient = AdRuleServiceClient.create()) {
       UpdateAdRuleRequest request =
           UpdateAdRuleRequest.newBuilder()
               .setAdRule(AdRule.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<AdRule> future = adRuleServiceClient.updateAdRuleCallable().futureCall(request);
       // Do something.
       AdRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAdRuleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateAdRuleRequest),[AdRule](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdRule)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
