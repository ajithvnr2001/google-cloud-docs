---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SiteServiceClient
title: Class SiteServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:09:03.175930+00:00
---

# Class SiteServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SiteServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SiteServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/SiteServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `Site` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       SiteName name = SiteName.of("[NETWORK_CODE]", "[SITE]");
       Site response = siteServiceClient.getSite(name);
     }
     

Note: close() needs to be called on the SiteServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetSite |  Retrieves a `Site` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSite(GetSiteRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSite(SiteName name) 
  * getSite(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSiteCallable() 

  
ListSites |  Lists `Site` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSites(ListSitesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSites(NetworkName parent) 
  * listSites(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSitesPagedCallable() 
  * listSitesCallable() 

  
CreateSite |  Creates a `Site` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSite(CreateSiteRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createSite(NetworkName parent, Site site) 
  * createSite(String parent, Site site) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSiteCallable() 

  
BatchCreateSites |  Creates `Site` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateSites(NetworkName parent, List<CreateSiteRequest> requests) 
  * batchCreateSites(String parent, List<CreateSiteRequest> requests) 
  * batchCreateSites(BatchCreateSitesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateSitesCallable() 

  
UpdateSite |  Updates a `Site` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSite(UpdateSiteRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSite(Site site, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSiteCallable() 

  
BatchUpdateSites |  Batch updates `Site` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateSites(NetworkName parent, List<UpdateSiteRequest> requests) 
  * batchUpdateSites(String parent, List<UpdateSiteRequest> requests) 
  * batchUpdateSites(BatchUpdateSitesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateSitesCallable() 

  
BatchDeactivateSites |  Deactivates a list of `Site` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivateSites(BatchDeactivateSitesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeactivateSites(NetworkName parent, List<String> names) 
  * batchDeactivateSites(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivateSitesCallable() 

  
BatchSubmitSitesForApproval |  Submits a list of `Site` objects for approval. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchSubmitSitesForApproval(BatchSubmitSitesForApprovalRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchSubmitSitesForApproval(NetworkName parent, List<String> names) 
  * batchSubmitSitesForApproval(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchSubmitSitesForApprovalCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SiteServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SiteServiceSettings siteServiceSettings =
         SiteServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SiteServiceClient siteServiceClient = SiteServiceClient.create(siteServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SiteServiceSettings siteServiceSettings =
         SiteServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SiteServiceClient siteServiceClient = SiteServiceClient.create(siteServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SiteServiceClient

## Static Methods 

### create()
    
    
    public static final SiteServiceClient create()

Constructs an instance of SiteServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SiteServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SiteServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SiteServiceSettings settings)
    
    
    public static final SiteServiceClient create(SiteServiceSettings settings)

Constructs an instance of SiteServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SiteServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SiteServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SiteServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SiteServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SiteServiceStub stub)
    
    
    public static final SiteServiceClient create(SiteServiceStub stub)

Constructs an instance of SiteServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SiteServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SiteServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.SiteServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SiteServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SiteServiceClient)` |   
  
## Constructors 

### SiteServiceClient(SiteServiceSettings settings)
    
    
    protected SiteServiceClient(SiteServiceSettings settings)

Constructs an instance of SiteServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SiteServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SiteServiceSettings)`  
  
  
### SiteServiceClient(SiteServiceStub stub)
    
    
    protected SiteServiceClient(SiteServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SiteServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.SiteServiceStub)`  
  
  
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
  
### batchCreateSites(@Nullable NetworkName parent, List<CreateSiteRequest> requests)
    
    
    public final BatchCreateSitesResponse batchCreateSites(@Nullable NetworkName parent, List<CreateSiteRequest> requests)

Creates `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateSiteRequest> requests = new ArrayList<>();
       BatchCreateSitesResponse response = siteServiceClient.batchCreateSites(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `Sites` will be created. Format: `networks/{network_code}` The parent field in the CreateSiteRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateSiteRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateSiteRequest)>`  
Required. The `Site` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateSitesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateSitesResponse)` |   
  
### batchCreateSites(BatchCreateSitesRequest request)
    
    
    public final BatchCreateSitesResponse batchCreateSites(BatchCreateSitesRequest request)

Creates `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       BatchCreateSitesRequest request =
           BatchCreateSitesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateSiteRequest>())
               .build();
       BatchCreateSitesResponse response = siteServiceClient.batchCreateSites(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateSitesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateSitesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateSitesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateSitesResponse)` |   
  
### batchCreateSites(String parent, List<CreateSiteRequest> requests)
    
    
    public final BatchCreateSitesResponse batchCreateSites(String parent, List<CreateSiteRequest> requests)

Creates `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateSiteRequest> requests = new ArrayList<>();
       BatchCreateSitesResponse response = siteServiceClient.batchCreateSites(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `Sites` will be created. Format: `networks/{network_code}` The parent field in the CreateSiteRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateSiteRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateSiteRequest)>`  
Required. The `Site` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateSitesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateSitesResponse)` |   
  
### batchCreateSitesCallable()
    
    
    public final UnaryCallable<BatchCreateSitesRequest,BatchCreateSitesResponse> batchCreateSitesCallable()

Creates `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       BatchCreateSitesRequest request =
           BatchCreateSitesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateSiteRequest>())
               .build();
       ApiFuture<BatchCreateSitesResponse> future =
           siteServiceClient.batchCreateSitesCallable().futureCall(request);
       // Do something.
       BatchCreateSitesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateSitesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateSitesRequest),[BatchCreateSitesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateSitesResponse)>` |   
  
### batchDeactivateSites(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDeactivateSitesResponse batchDeactivateSites(@Nullable NetworkName parent, List<String> names)

Deactivates a list of `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDeactivateSitesResponse response = siteServiceClient.batchDeactivateSites(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `Site` objects to deactivate.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateSitesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateSitesResponse)` |   
  
### batchDeactivateSites(BatchDeactivateSitesRequest request)
    
    
    public final BatchDeactivateSitesResponse batchDeactivateSites(BatchDeactivateSitesRequest request)

Deactivates a list of `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       BatchDeactivateSitesRequest request =
           BatchDeactivateSitesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeactivateSitesResponse response = siteServiceClient.batchDeactivateSites(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivateSitesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateSitesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateSitesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateSitesResponse)` |   
  
### batchDeactivateSites(String parent, List<String> names)
    
    
    public final BatchDeactivateSitesResponse batchDeactivateSites(String parent, List<String> names)

Deactivates a list of `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDeactivateSitesResponse response = siteServiceClient.batchDeactivateSites(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `Site` objects to deactivate.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateSitesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateSitesResponse)` |   
  
### batchDeactivateSitesCallable()
    
    
    public final UnaryCallable<BatchDeactivateSitesRequest,BatchDeactivateSitesResponse> batchDeactivateSitesCallable()

Deactivates a list of `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       BatchDeactivateSitesRequest request =
           BatchDeactivateSitesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDeactivateSitesResponse> future =
           siteServiceClient.batchDeactivateSitesCallable().futureCall(request);
       // Do something.
       BatchDeactivateSitesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivateSitesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateSitesRequest),[BatchDeactivateSitesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateSitesResponse)>` |   
  
### batchSubmitSitesForApproval(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchSubmitSitesForApprovalResponse batchSubmitSitesForApproval(@Nullable NetworkName parent, List<String> names)

Submits a list of `Site` objects for approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchSubmitSitesForApprovalResponse response =
           siteServiceClient.batchSubmitSitesForApproval(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `Site` objects to submit for approval.  
**Returns**  
---  
**Type** | **Description**  
`[BatchSubmitSitesForApprovalResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitSitesForApprovalResponse)` |   
  
### batchSubmitSitesForApproval(BatchSubmitSitesForApprovalRequest request)
    
    
    public final BatchSubmitSitesForApprovalResponse batchSubmitSitesForApproval(BatchSubmitSitesForApprovalRequest request)

Submits a list of `Site` objects for approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       BatchSubmitSitesForApprovalRequest request =
           BatchSubmitSitesForApprovalRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchSubmitSitesForApprovalResponse response =
           siteServiceClient.batchSubmitSitesForApproval(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchSubmitSitesForApprovalRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitSitesForApprovalRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchSubmitSitesForApprovalResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitSitesForApprovalResponse)` |   
  
### batchSubmitSitesForApproval(String parent, List<String> names)
    
    
    public final BatchSubmitSitesForApprovalResponse batchSubmitSitesForApproval(String parent, List<String> names)

Submits a list of `Site` objects for approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchSubmitSitesForApprovalResponse response =
           siteServiceClient.batchSubmitSitesForApproval(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `Site` objects to submit for approval.  
**Returns**  
---  
**Type** | **Description**  
`[BatchSubmitSitesForApprovalResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitSitesForApprovalResponse)` |   
  
### batchSubmitSitesForApprovalCallable()
    
    
    public final UnaryCallable<BatchSubmitSitesForApprovalRequest,BatchSubmitSitesForApprovalResponse> batchSubmitSitesForApprovalCallable()

Submits a list of `Site` objects for approval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       BatchSubmitSitesForApprovalRequest request =
           BatchSubmitSitesForApprovalRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchSubmitSitesForApprovalResponse> future =
           siteServiceClient.batchSubmitSitesForApprovalCallable().futureCall(request);
       // Do something.
       BatchSubmitSitesForApprovalResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchSubmitSitesForApprovalRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitSitesForApprovalRequest),[BatchSubmitSitesForApprovalResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchSubmitSitesForApprovalResponse)>` |   
  
### batchUpdateSites(@Nullable NetworkName parent, List<UpdateSiteRequest> requests)
    
    
    public final BatchUpdateSitesResponse batchUpdateSites(@Nullable NetworkName parent, List<UpdateSiteRequest> requests)

Batch updates `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateSiteRequest> requests = new ArrayList<>();
       BatchUpdateSitesResponse response = siteServiceClient.batchUpdateSites(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `Sites` will be updated. Format: `networks/{network_code}` The parent field in the UpdateSiteRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateSiteRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateSiteRequest)>`  
Required. The `Site` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateSitesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateSitesResponse)` |   
  
### batchUpdateSites(BatchUpdateSitesRequest request)
    
    
    public final BatchUpdateSitesResponse batchUpdateSites(BatchUpdateSitesRequest request)

Batch updates `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       BatchUpdateSitesRequest request =
           BatchUpdateSitesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateSiteRequest>())
               .build();
       BatchUpdateSitesResponse response = siteServiceClient.batchUpdateSites(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateSitesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateSitesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateSitesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateSitesResponse)` |   
  
### batchUpdateSites(String parent, List<UpdateSiteRequest> requests)
    
    
    public final BatchUpdateSitesResponse batchUpdateSites(String parent, List<UpdateSiteRequest> requests)

Batch updates `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateSiteRequest> requests = new ArrayList<>();
       BatchUpdateSitesResponse response = siteServiceClient.batchUpdateSites(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `Sites` will be updated. Format: `networks/{network_code}` The parent field in the UpdateSiteRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateSiteRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateSiteRequest)>`  
Required. The `Site` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateSitesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateSitesResponse)` |   
  
### batchUpdateSitesCallable()
    
    
    public final UnaryCallable<BatchUpdateSitesRequest,BatchUpdateSitesResponse> batchUpdateSitesCallable()

Batch updates `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       BatchUpdateSitesRequest request =
           BatchUpdateSitesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateSiteRequest>())
               .build();
       ApiFuture<BatchUpdateSitesResponse> future =
           siteServiceClient.batchUpdateSitesCallable().futureCall(request);
       // Do something.
       BatchUpdateSitesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateSitesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateSitesRequest),[BatchUpdateSitesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateSitesResponse)>` |   
  
### close()
    
    
    public final void close()

### createSite(@Nullable NetworkName parent, Site site)
    
    
    public final Site createSite(@Nullable NetworkName parent, Site site)

Creates a `Site` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       Site site = Site.newBuilder().build();
       Site response = siteServiceClient.createSite(parent, site);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `Site` will be created. Format: `networks/{network_code}`  
`site` | `[Site](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Site)`  
Required. The `Site` to create.  
**Returns**  
---  
**Type** | **Description**  
`[Site](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Site)` |   
  
### createSite(CreateSiteRequest request)
    
    
    public final Site createSite(CreateSiteRequest request)

Creates a `Site` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       CreateSiteRequest request =
           CreateSiteRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setSite(Site.newBuilder().build())
               .build();
       Site response = siteServiceClient.createSite(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSiteRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateSiteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Site](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Site)` |   
  
### createSite(String parent, Site site)
    
    
    public final Site createSite(String parent, Site site)

Creates a `Site` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       Site site = Site.newBuilder().build();
       Site response = siteServiceClient.createSite(parent, site);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `Site` will be created. Format: `networks/{network_code}`  
`site` | `[Site](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Site)`  
Required. The `Site` to create.  
**Returns**  
---  
**Type** | **Description**  
`[Site](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Site)` |   
  
### createSiteCallable()
    
    
    public final UnaryCallable<CreateSiteRequest,Site> createSiteCallable()

Creates a `Site` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       CreateSiteRequest request =
           CreateSiteRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setSite(Site.newBuilder().build())
               .build();
       ApiFuture<Site> future = siteServiceClient.createSiteCallable().futureCall(request);
       // Do something.
       Site response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSiteRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateSiteRequest),[Site](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Site)>` |   
  
### getSettings()
    
    
    public final @Nullable SiteServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.SiteServiceSettings` |   
  
### getSite(@Nullable SiteName name)
    
    
    public final Site getSite(@Nullable SiteName name)

Retrieves a `Site` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       SiteName name = SiteName.of("[NETWORK_CODE]", "[SITE]");
       Site response = siteServiceClient.getSite(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.SiteName`  
Required. The resource name of the Site. Format: `networks/{network_code}/sites/{site_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Site](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Site)` |   
  
### getSite(GetSiteRequest request)
    
    
    public final Site getSite(GetSiteRequest request)

Retrieves a `Site` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       GetSiteRequest request =
           GetSiteRequest.newBuilder()
               .setName(SiteName.of("[NETWORK_CODE]", "[SITE]").toString())
               .build();
       Site response = siteServiceClient.getSite(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSiteRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetSiteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Site](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Site)` |   
  
### getSite(String name)
    
    
    public final Site getSite(String name)

Retrieves a `Site` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       String name = SiteName.of("[NETWORK_CODE]", "[SITE]").toString();
       Site response = siteServiceClient.getSite(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Site. Format: `networks/{network_code}/sites/{site_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Site](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Site)` |   
  
### getSiteCallable()
    
    
    public final UnaryCallable<GetSiteRequest,Site> getSiteCallable()

Retrieves a `Site` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       GetSiteRequest request =
           GetSiteRequest.newBuilder()
               .setName(SiteName.of("[NETWORK_CODE]", "[SITE]").toString())
               .build();
       ApiFuture<Site> future = siteServiceClient.getSiteCallable().futureCall(request);
       // Do something.
       Site response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSiteRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetSiteRequest),[Site](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Site)>` |   
  
### getStub()
    
    
    public SiteServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SiteServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.SiteServiceStub)` |   
  
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
  
### listSites(@Nullable NetworkName parent)
    
    
    public final SiteServiceClient.ListSitesPagedResponse listSites(@Nullable NetworkName parent)

Lists `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (Site element : siteServiceClient.listSites(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of Sites. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[SiteServiceClient.ListSitesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SiteServiceClient.ListSitesPagedResponse)` |   
  
### listSites(ListSitesRequest request)
    
    
    public final SiteServiceClient.ListSitesPagedResponse listSites(ListSitesRequest request)

Lists `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       ListSitesRequest request =
           ListSitesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (Site element : siteServiceClient.listSites(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSitesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListSitesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SiteServiceClient.ListSitesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SiteServiceClient.ListSitesPagedResponse)` |   
  
### listSites(String parent)
    
    
    public final SiteServiceClient.ListSitesPagedResponse listSites(String parent)

Lists `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (Site element : siteServiceClient.listSites(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of Sites. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[SiteServiceClient.ListSitesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SiteServiceClient.ListSitesPagedResponse)` |   
  
### listSitesCallable()
    
    
    public final UnaryCallable<ListSitesRequest,ListSitesResponse> listSitesCallable()

Lists `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       ListSitesRequest request =
           ListSitesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListSitesResponse response = siteServiceClient.listSitesCallable().call(request);
         for (Site element : response.getSitesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSitesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListSitesRequest),[ListSitesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListSitesResponse)>` |   
  
### listSitesPagedCallable()
    
    
    public final UnaryCallable<ListSitesRequest,SiteServiceClient.ListSitesPagedResponse> listSitesPagedCallable()

Lists `Site` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       ListSitesRequest request =
           ListSitesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<Site> future = siteServiceClient.listSitesPagedCallable().futureCall(request);
       // Do something.
       for (Site element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSitesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListSitesRequest),[ListSitesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SiteServiceClient.ListSitesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateSite(Site site, FieldMask updateMask)
    
    
    public final Site updateSite(Site site, FieldMask updateMask)

Updates a `Site` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       Site site = Site.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Site response = siteServiceClient.updateSite(site, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`site` | `[Site](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Site)`  
Required. The `Site` to update. The `Site`'s `name` is used to identify the `Site` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[Site](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Site)` |   
  
### updateSite(UpdateSiteRequest request)
    
    
    public final Site updateSite(UpdateSiteRequest request)

Updates a `Site` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       UpdateSiteRequest request =
           UpdateSiteRequest.newBuilder()
               .setSite(Site.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Site response = siteServiceClient.updateSite(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSiteRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateSiteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Site](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Site)` |   
  
### updateSiteCallable()
    
    
    public final UnaryCallable<UpdateSiteRequest,Site> updateSiteCallable()

Updates a `Site` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteServiceClient siteServiceClient = SiteServiceClient.create()) {
       UpdateSiteRequest request =
           UpdateSiteRequest.newBuilder()
               .setSite(Site.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Site> future = siteServiceClient.updateSiteCallable().futureCall(request);
       // Do something.
       Site response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSiteRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateSiteRequest),[Site](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.Site)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
