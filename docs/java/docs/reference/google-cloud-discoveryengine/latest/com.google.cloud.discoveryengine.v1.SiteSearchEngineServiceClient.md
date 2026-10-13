---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngineServiceClient
title: Class SiteSearchEngineServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:51.891801+00:00
---

# Class SiteSearchEngineServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngineServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SiteSearchEngineServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-discoveryengine/google-cloud-discoveryengine/src/main/java/com/google/cloud/discoveryengine/v1/SiteSearchEngineServiceClient.java)| [Product Reference](https://cloud.google.com/discovery-engine/media/docs)  
---|---  
  
Service Description: Service for managing site search related resources.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       SiteSearchEngineName name =
           SiteSearchEngineName.ofProjectLocationDataStoreName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       SiteSearchEngine response = siteSearchEngineServiceClient.getSiteSearchEngine(name);
     }
     

Note: close() needs to be called on the SiteSearchEngineServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetSiteSearchEngine |  Gets the SiteSearchEngine. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSiteSearchEngine(GetSiteSearchEngineRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSiteSearchEngine(SiteSearchEngineName name) 
  * getSiteSearchEngine(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSiteSearchEngineCallable() 

  
CreateTargetSite |  Creates a TargetSite. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTargetSiteAsync(CreateTargetSiteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createTargetSiteAsync(SiteSearchEngineName parent, TargetSite targetSite) 
  * createTargetSiteAsync(String parent, TargetSite targetSite) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTargetSiteOperationCallable() 
  * createTargetSiteCallable() 

  
BatchCreateTargetSites |  Creates TargetSite in a batch. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateTargetSitesAsync(BatchCreateTargetSitesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateTargetSitesOperationCallable() 
  * batchCreateTargetSitesCallable() 

  
GetTargetSite |  Gets a TargetSite. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTargetSite(GetTargetSiteRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTargetSite(TargetSiteName name) 
  * getTargetSite(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTargetSiteCallable() 

  
UpdateTargetSite |  Updates a TargetSite. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTargetSiteAsync(UpdateTargetSiteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateTargetSiteAsync(TargetSite targetSite) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTargetSiteOperationCallable() 
  * updateTargetSiteCallable() 

  
DeleteTargetSite |  Deletes a TargetSite. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTargetSiteAsync(DeleteTargetSiteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteTargetSiteAsync(TargetSiteName name) 
  * deleteTargetSiteAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTargetSiteOperationCallable() 
  * deleteTargetSiteCallable() 

  
ListTargetSites |  Gets a list of TargetSites. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTargetSites(ListTargetSitesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTargetSites(SiteSearchEngineName parent) 
  * listTargetSites(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTargetSitesPagedCallable() 
  * listTargetSitesCallable() 

  
CreateSitemap |  Creates a Sitemap. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSitemapAsync(CreateSitemapRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createSitemapAsync(SiteSearchEngineName parent, Sitemap sitemap) 
  * createSitemapAsync(String parent, Sitemap sitemap) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSitemapOperationCallable() 
  * createSitemapCallable() 

  
DeleteSitemap |  Deletes a Sitemap. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSitemapAsync(DeleteSitemapRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteSitemapAsync(SitemapName name) 
  * deleteSitemapAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSitemapOperationCallable() 
  * deleteSitemapCallable() 

  
FetchSitemaps |  Fetch Sitemaps in a DataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchSitemaps(FetchSitemapsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * fetchSitemaps(SiteSearchEngineName parent) 
  * fetchSitemaps(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchSitemapsCallable() 

  
EnableAdvancedSiteSearch |  Upgrade from basic site search to advanced site search. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * enableAdvancedSiteSearchAsync(EnableAdvancedSiteSearchRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * enableAdvancedSiteSearchOperationCallable() 
  * enableAdvancedSiteSearchCallable() 

  
DisableAdvancedSiteSearch |  Downgrade from advanced site search to basic site search. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * disableAdvancedSiteSearchAsync(DisableAdvancedSiteSearchRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * disableAdvancedSiteSearchOperationCallable() 
  * disableAdvancedSiteSearchCallable() 

  
RecrawlUris |  Request on-demand recrawl for a list of URIs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * recrawlUrisAsync(RecrawlUrisRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * recrawlUrisOperationCallable() 
  * recrawlUrisCallable() 

  
BatchVerifyTargetSites |  Verify target sites' ownership and validity. This API sends all the target sites under site search engine for verification. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchVerifyTargetSitesAsync(BatchVerifyTargetSitesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchVerifyTargetSitesOperationCallable() 
  * batchVerifyTargetSitesCallable() 

  
FetchDomainVerificationStatus |  Returns list of target sites with its domain verification status. This method can only be called under data store with BASIC_SITE_SEARCH state at the moment. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * fetchDomainVerificationStatus(FetchDomainVerificationStatusRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * fetchDomainVerificationStatusPagedCallable() 
  * fetchDomainVerificationStatusCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SiteSearchEngineServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SiteSearchEngineServiceSettings siteSearchEngineServiceSettings =
         SiteSearchEngineServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create(siteSearchEngineServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SiteSearchEngineServiceSettings siteSearchEngineServiceSettings =
         SiteSearchEngineServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create(siteSearchEngineServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SiteSearchEngineServiceSettings siteSearchEngineServiceSettings =
         SiteSearchEngineServiceSettings.newHttpJsonBuilder().build();
     SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create(siteSearchEngineServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SiteSearchEngineServiceClient

## Static Methods 

### create()
    
    
    public static final SiteSearchEngineServiceClient create()

Constructs an instance of SiteSearchEngineServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SiteSearchEngineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngineServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SiteSearchEngineServiceSettings settings)
    
    
    public static final SiteSearchEngineServiceClient create(SiteSearchEngineServiceSettings settings)

Constructs an instance of SiteSearchEngineServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SiteSearchEngineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngineServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SiteSearchEngineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngineServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SiteSearchEngineServiceStub stub)
    
    
    public static final SiteSearchEngineServiceClient create(SiteSearchEngineServiceStub stub)

Constructs an instance of SiteSearchEngineServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SiteSearchEngineServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SiteSearchEngineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.SiteSearchEngineServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SiteSearchEngineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngineServiceClient)` |   
  
## Constructors 

### SiteSearchEngineServiceClient(SiteSearchEngineServiceSettings settings)
    
    
    protected SiteSearchEngineServiceClient(SiteSearchEngineServiceSettings settings)

Constructs an instance of SiteSearchEngineServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SiteSearchEngineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngineServiceSettings)`  
  
  
### SiteSearchEngineServiceClient(SiteSearchEngineServiceStub stub)
    
    
    protected SiteSearchEngineServiceClient(SiteSearchEngineServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SiteSearchEngineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.SiteSearchEngineServiceStub)`  
  
  
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
  
### batchCreateTargetSitesAsync(BatchCreateTargetSitesRequest request)
    
    
    public final OperationFuture<BatchCreateTargetSitesResponse,BatchCreateTargetSiteMetadata> batchCreateTargetSitesAsync(BatchCreateTargetSitesRequest request)

Creates TargetSite in a batch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       BatchCreateTargetSitesRequest request =
           BatchCreateTargetSitesRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .addAllRequests(new ArrayList<CreateTargetSiteRequest>())
               .build();
       BatchCreateTargetSitesResponse response =
           siteSearchEngineServiceClient.batchCreateTargetSitesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateTargetSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchCreateTargetSitesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchCreateTargetSitesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchCreateTargetSitesResponse),[BatchCreateTargetSiteMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchCreateTargetSiteMetadata)>` |   
  
### batchCreateTargetSitesCallable()
    
    
    public final UnaryCallable<BatchCreateTargetSitesRequest,Operation> batchCreateTargetSitesCallable()

Creates TargetSite in a batch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       BatchCreateTargetSitesRequest request =
           BatchCreateTargetSitesRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .addAllRequests(new ArrayList<CreateTargetSiteRequest>())
               .build();
       ApiFuture<Operation> future =
           siteSearchEngineServiceClient.batchCreateTargetSitesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateTargetSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchCreateTargetSitesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchCreateTargetSitesOperationCallable()
    
    
    public final OperationCallable<BatchCreateTargetSitesRequest,BatchCreateTargetSitesResponse,BatchCreateTargetSiteMetadata> batchCreateTargetSitesOperationCallable()

Creates TargetSite in a batch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       BatchCreateTargetSitesRequest request =
           BatchCreateTargetSitesRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .addAllRequests(new ArrayList<CreateTargetSiteRequest>())
               .build();
       OperationFuture<BatchCreateTargetSitesResponse, BatchCreateTargetSiteMetadata> future =
           siteSearchEngineServiceClient
               .batchCreateTargetSitesOperationCallable()
               .futureCall(request);
       // Do something.
       BatchCreateTargetSitesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchCreateTargetSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchCreateTargetSitesRequest),[BatchCreateTargetSitesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchCreateTargetSitesResponse),[BatchCreateTargetSiteMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchCreateTargetSiteMetadata)>` |   
  
### batchVerifyTargetSitesAsync(BatchVerifyTargetSitesRequest request)
    
    
    public final OperationFuture<BatchVerifyTargetSitesResponse,BatchVerifyTargetSitesMetadata> batchVerifyTargetSitesAsync(BatchVerifyTargetSitesRequest request)

Verify target sites' ownership and validity. This API sends all the target sites under site search engine for verification.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       BatchVerifyTargetSitesRequest request =
           BatchVerifyTargetSitesRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .build();
       BatchVerifyTargetSitesResponse response =
           siteSearchEngineServiceClient.batchVerifyTargetSitesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchVerifyTargetSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchVerifyTargetSitesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchVerifyTargetSitesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchVerifyTargetSitesResponse),[BatchVerifyTargetSitesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchVerifyTargetSitesMetadata)>` |   
  
### batchVerifyTargetSitesCallable()
    
    
    public final UnaryCallable<BatchVerifyTargetSitesRequest,Operation> batchVerifyTargetSitesCallable()

Verify target sites' ownership and validity. This API sends all the target sites under site search engine for verification.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       BatchVerifyTargetSitesRequest request =
           BatchVerifyTargetSitesRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           siteSearchEngineServiceClient.batchVerifyTargetSitesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchVerifyTargetSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchVerifyTargetSitesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchVerifyTargetSitesOperationCallable()
    
    
    public final OperationCallable<BatchVerifyTargetSitesRequest,BatchVerifyTargetSitesResponse,BatchVerifyTargetSitesMetadata> batchVerifyTargetSitesOperationCallable()

Verify target sites' ownership and validity. This API sends all the target sites under site search engine for verification.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       BatchVerifyTargetSitesRequest request =
           BatchVerifyTargetSitesRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .build();
       OperationFuture<BatchVerifyTargetSitesResponse, BatchVerifyTargetSitesMetadata> future =
           siteSearchEngineServiceClient
               .batchVerifyTargetSitesOperationCallable()
               .futureCall(request);
       // Do something.
       BatchVerifyTargetSitesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchVerifyTargetSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchVerifyTargetSitesRequest),[BatchVerifyTargetSitesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchVerifyTargetSitesResponse),[BatchVerifyTargetSitesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.BatchVerifyTargetSitesMetadata)>` |   
  
### close()
    
    
    public final void close()

### createSitemapAsync(@Nullable SiteSearchEngineName parent, Sitemap sitemap)
    
    
    public final OperationFuture<Sitemap,CreateSitemapMetadata> createSitemapAsync(@Nullable SiteSearchEngineName parent, Sitemap sitemap)

Creates a Sitemap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       SiteSearchEngineName parent =
           SiteSearchEngineName.ofProjectLocationDataStoreName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       Sitemap sitemap = Sitemap.newBuilder().build();
       Sitemap response = siteSearchEngineServiceClient.createSitemapAsync(parent, sitemap).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.SiteSearchEngineName`  
Required. Parent resource name of the SiteSearchEngine, such as `projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine`.  
`sitemap` | `[Sitemap](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Sitemap)`  
Required. The Sitemap to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Sitemap](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Sitemap),[CreateSitemapMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateSitemapMetadata)>` |   
  
### createSitemapAsync(CreateSitemapRequest request)
    
    
    public final OperationFuture<Sitemap,CreateSitemapMetadata> createSitemapAsync(CreateSitemapRequest request)

Creates a Sitemap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       CreateSitemapRequest request =
           CreateSitemapRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setSitemap(Sitemap.newBuilder().build())
               .build();
       Sitemap response = siteSearchEngineServiceClient.createSitemapAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSitemapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateSitemapRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Sitemap](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Sitemap),[CreateSitemapMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateSitemapMetadata)>` |   
  
### createSitemapAsync(String parent, Sitemap sitemap)
    
    
    public final OperationFuture<Sitemap,CreateSitemapMetadata> createSitemapAsync(String parent, Sitemap sitemap)

Creates a Sitemap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       String parent =
           SiteSearchEngineName.ofProjectLocationDataStoreName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
               .toString();
       Sitemap sitemap = Sitemap.newBuilder().build();
       Sitemap response = siteSearchEngineServiceClient.createSitemapAsync(parent, sitemap).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent resource name of the SiteSearchEngine, such as `projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine`.  
`sitemap` | `[Sitemap](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Sitemap)`  
Required. The Sitemap to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Sitemap](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Sitemap),[CreateSitemapMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateSitemapMetadata)>` |   
  
### createSitemapCallable()
    
    
    public final UnaryCallable<CreateSitemapRequest,Operation> createSitemapCallable()

Creates a Sitemap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       CreateSitemapRequest request =
           CreateSitemapRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setSitemap(Sitemap.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           siteSearchEngineServiceClient.createSitemapCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSitemapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateSitemapRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSitemapOperationCallable()
    
    
    public final OperationCallable<CreateSitemapRequest,Sitemap,CreateSitemapMetadata> createSitemapOperationCallable()

Creates a Sitemap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       CreateSitemapRequest request =
           CreateSitemapRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setSitemap(Sitemap.newBuilder().build())
               .build();
       OperationFuture<Sitemap, CreateSitemapMetadata> future =
           siteSearchEngineServiceClient.createSitemapOperationCallable().futureCall(request);
       // Do something.
       Sitemap response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateSitemapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateSitemapRequest),[Sitemap](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.Sitemap),[CreateSitemapMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateSitemapMetadata)>` |   
  
### createTargetSiteAsync(@Nullable SiteSearchEngineName parent, TargetSite targetSite)
    
    
    public final OperationFuture<TargetSite,CreateTargetSiteMetadata> createTargetSiteAsync(@Nullable SiteSearchEngineName parent, TargetSite targetSite)

Creates a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       SiteSearchEngineName parent =
           SiteSearchEngineName.ofProjectLocationDataStoreName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       TargetSite targetSite = TargetSite.newBuilder().build();
       TargetSite response =
           siteSearchEngineServiceClient.createTargetSiteAsync(parent, targetSite).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.SiteSearchEngineName`  
Required. Parent resource name of TargetSite, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`.  
`targetSite` | `[TargetSite](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TargetSite)`  
Required. The TargetSite to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TargetSite](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TargetSite),[CreateTargetSiteMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateTargetSiteMetadata)>` |   
  
### createTargetSiteAsync(CreateTargetSiteRequest request)
    
    
    public final OperationFuture<TargetSite,CreateTargetSiteMetadata> createTargetSiteAsync(CreateTargetSiteRequest request)

Creates a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       CreateTargetSiteRequest request =
           CreateTargetSiteRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setTargetSite(TargetSite.newBuilder().build())
               .build();
       TargetSite response = siteSearchEngineServiceClient.createTargetSiteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTargetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateTargetSiteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TargetSite](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TargetSite),[CreateTargetSiteMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateTargetSiteMetadata)>` |   
  
### createTargetSiteAsync(String parent, TargetSite targetSite)
    
    
    public final OperationFuture<TargetSite,CreateTargetSiteMetadata> createTargetSiteAsync(String parent, TargetSite targetSite)

Creates a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       String parent =
           SiteSearchEngineName.ofProjectLocationDataStoreName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
               .toString();
       TargetSite targetSite = TargetSite.newBuilder().build();
       TargetSite response =
           siteSearchEngineServiceClient.createTargetSiteAsync(parent, targetSite).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent resource name of TargetSite, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`.  
`targetSite` | `[TargetSite](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TargetSite)`  
Required. The TargetSite to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TargetSite](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TargetSite),[CreateTargetSiteMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateTargetSiteMetadata)>` |   
  
### createTargetSiteCallable()
    
    
    public final UnaryCallable<CreateTargetSiteRequest,Operation> createTargetSiteCallable()

Creates a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       CreateTargetSiteRequest request =
           CreateTargetSiteRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setTargetSite(TargetSite.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           siteSearchEngineServiceClient.createTargetSiteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTargetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateTargetSiteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createTargetSiteOperationCallable()
    
    
    public final OperationCallable<CreateTargetSiteRequest,TargetSite,CreateTargetSiteMetadata> createTargetSiteOperationCallable()

Creates a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       CreateTargetSiteRequest request =
           CreateTargetSiteRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setTargetSite(TargetSite.newBuilder().build())
               .build();
       OperationFuture<TargetSite, CreateTargetSiteMetadata> future =
           siteSearchEngineServiceClient.createTargetSiteOperationCallable().futureCall(request);
       // Do something.
       TargetSite response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateTargetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateTargetSiteRequest),[TargetSite](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TargetSite),[CreateTargetSiteMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateTargetSiteMetadata)>` |   
  
### deleteSitemapAsync(@Nullable SitemapName name)
    
    
    public final OperationFuture<Empty,DeleteSitemapMetadata> deleteSitemapAsync(@Nullable SitemapName name)

Deletes a Sitemap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       SitemapName name =
           SitemapName.ofProjectLocationDataStoreSitemapName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SITEMAP]");
       siteSearchEngineServiceClient.deleteSitemapAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.SitemapName`  
Required. Full resource name of Sitemap, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/sitemaps/{sitemap}`. If the caller does not have permission to access the Sitemap, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the requested Sitemap does not exist, a NOT_FOUND error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteSitemapMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteSitemapMetadata)>` |   
  
### deleteSitemapAsync(DeleteSitemapRequest request)
    
    
    public final OperationFuture<Empty,DeleteSitemapMetadata> deleteSitemapAsync(DeleteSitemapRequest request)

Deletes a Sitemap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       DeleteSitemapRequest request =
           DeleteSitemapRequest.newBuilder()
               .setName(
                   SitemapName.ofProjectLocationDataStoreSitemapName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SITEMAP]")
                       .toString())
               .build();
       siteSearchEngineServiceClient.deleteSitemapAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSitemapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteSitemapRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteSitemapMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteSitemapMetadata)>` |   
  
### deleteSitemapAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteSitemapMetadata> deleteSitemapAsync(String name)

Deletes a Sitemap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       String name =
           SitemapName.ofProjectLocationDataStoreSitemapName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SITEMAP]")
               .toString();
       siteSearchEngineServiceClient.deleteSitemapAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of Sitemap, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/sitemaps/{sitemap}`. If the caller does not have permission to access the Sitemap, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the requested Sitemap does not exist, a NOT_FOUND error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteSitemapMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteSitemapMetadata)>` |   
  
### deleteSitemapCallable()
    
    
    public final UnaryCallable<DeleteSitemapRequest,Operation> deleteSitemapCallable()

Deletes a Sitemap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       DeleteSitemapRequest request =
           DeleteSitemapRequest.newBuilder()
               .setName(
                   SitemapName.ofProjectLocationDataStoreSitemapName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SITEMAP]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           siteSearchEngineServiceClient.deleteSitemapCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSitemapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteSitemapRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSitemapOperationCallable()
    
    
    public final OperationCallable<DeleteSitemapRequest,Empty,DeleteSitemapMetadata> deleteSitemapOperationCallable()

Deletes a Sitemap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       DeleteSitemapRequest request =
           DeleteSitemapRequest.newBuilder()
               .setName(
                   SitemapName.ofProjectLocationDataStoreSitemapName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[SITEMAP]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteSitemapMetadata> future =
           siteSearchEngineServiceClient.deleteSitemapOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSitemapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteSitemapRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteSitemapMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteSitemapMetadata)>` |   
  
### deleteTargetSiteAsync(@Nullable TargetSiteName name)
    
    
    public final OperationFuture<Empty,DeleteTargetSiteMetadata> deleteTargetSiteAsync(@Nullable TargetSiteName name)

Deletes a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       TargetSiteName name =
           TargetSiteName.ofProjectLocationDataStoreTargetSiteName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[TARGET_SITE]");
       siteSearchEngineServiceClient.deleteTargetSiteAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.TargetSiteName`  
Required. Full resource name of TargetSite, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}`. If the caller does not have permission to access the TargetSite, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the requested TargetSite does not exist, a NOT_FOUND error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteTargetSiteMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteTargetSiteMetadata)>` |   
  
### deleteTargetSiteAsync(DeleteTargetSiteRequest request)
    
    
    public final OperationFuture<Empty,DeleteTargetSiteMetadata> deleteTargetSiteAsync(DeleteTargetSiteRequest request)

Deletes a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       DeleteTargetSiteRequest request =
           DeleteTargetSiteRequest.newBuilder()
               .setName(
                   TargetSiteName.ofProjectLocationDataStoreTargetSiteName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[TARGET_SITE]")
                       .toString())
               .build();
       siteSearchEngineServiceClient.deleteTargetSiteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTargetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteTargetSiteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteTargetSiteMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteTargetSiteMetadata)>` |   
  
### deleteTargetSiteAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteTargetSiteMetadata> deleteTargetSiteAsync(String name)

Deletes a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       String name =
           TargetSiteName.ofProjectLocationDataStoreTargetSiteName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[TARGET_SITE]")
               .toString();
       siteSearchEngineServiceClient.deleteTargetSiteAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of TargetSite, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}`. If the caller does not have permission to access the TargetSite, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the requested TargetSite does not exist, a NOT_FOUND error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteTargetSiteMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteTargetSiteMetadata)>` |   
  
### deleteTargetSiteCallable()
    
    
    public final UnaryCallable<DeleteTargetSiteRequest,Operation> deleteTargetSiteCallable()

Deletes a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       DeleteTargetSiteRequest request =
           DeleteTargetSiteRequest.newBuilder()
               .setName(
                   TargetSiteName.ofProjectLocationDataStoreTargetSiteName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[TARGET_SITE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           siteSearchEngineServiceClient.deleteTargetSiteCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTargetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteTargetSiteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTargetSiteOperationCallable()
    
    
    public final OperationCallable<DeleteTargetSiteRequest,Empty,DeleteTargetSiteMetadata> deleteTargetSiteOperationCallable()

Deletes a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       DeleteTargetSiteRequest request =
           DeleteTargetSiteRequest.newBuilder()
               .setName(
                   TargetSiteName.ofProjectLocationDataStoreTargetSiteName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[TARGET_SITE]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteTargetSiteMetadata> future =
           siteSearchEngineServiceClient.deleteTargetSiteOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTargetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteTargetSiteRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteTargetSiteMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteTargetSiteMetadata)>` |   
  
### disableAdvancedSiteSearchAsync(DisableAdvancedSiteSearchRequest request)
    
    
    public final OperationFuture<DisableAdvancedSiteSearchResponse,DisableAdvancedSiteSearchMetadata> disableAdvancedSiteSearchAsync(DisableAdvancedSiteSearchRequest request)

Downgrade from advanced site search to basic site search.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       DisableAdvancedSiteSearchRequest request =
           DisableAdvancedSiteSearchRequest.newBuilder()
               .setSiteSearchEngine(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .build();
       DisableAdvancedSiteSearchResponse response =
           siteSearchEngineServiceClient.disableAdvancedSiteSearchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DisableAdvancedSiteSearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DisableAdvancedSiteSearchRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DisableAdvancedSiteSearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DisableAdvancedSiteSearchResponse),[DisableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DisableAdvancedSiteSearchMetadata)>` |   
  
### disableAdvancedSiteSearchCallable()
    
    
    public final UnaryCallable<DisableAdvancedSiteSearchRequest,Operation> disableAdvancedSiteSearchCallable()

Downgrade from advanced site search to basic site search.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       DisableAdvancedSiteSearchRequest request =
           DisableAdvancedSiteSearchRequest.newBuilder()
               .setSiteSearchEngine(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           siteSearchEngineServiceClient.disableAdvancedSiteSearchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DisableAdvancedSiteSearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DisableAdvancedSiteSearchRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### disableAdvancedSiteSearchOperationCallable()
    
    
    public final OperationCallable<DisableAdvancedSiteSearchRequest,DisableAdvancedSiteSearchResponse,DisableAdvancedSiteSearchMetadata> disableAdvancedSiteSearchOperationCallable()

Downgrade from advanced site search to basic site search.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       DisableAdvancedSiteSearchRequest request =
           DisableAdvancedSiteSearchRequest.newBuilder()
               .setSiteSearchEngine(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .build();
       OperationFuture<DisableAdvancedSiteSearchResponse, DisableAdvancedSiteSearchMetadata> future =
           siteSearchEngineServiceClient
               .disableAdvancedSiteSearchOperationCallable()
               .futureCall(request);
       // Do something.
       DisableAdvancedSiteSearchResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DisableAdvancedSiteSearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DisableAdvancedSiteSearchRequest),[DisableAdvancedSiteSearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DisableAdvancedSiteSearchResponse),[DisableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DisableAdvancedSiteSearchMetadata)>` |   
  
### enableAdvancedSiteSearchAsync(EnableAdvancedSiteSearchRequest request)
    
    
    public final OperationFuture<EnableAdvancedSiteSearchResponse,EnableAdvancedSiteSearchMetadata> enableAdvancedSiteSearchAsync(EnableAdvancedSiteSearchRequest request)

Upgrade from basic site search to advanced site search.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       EnableAdvancedSiteSearchRequest request =
           EnableAdvancedSiteSearchRequest.newBuilder()
               .setSiteSearchEngine(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .build();
       EnableAdvancedSiteSearchResponse response =
           siteSearchEngineServiceClient.enableAdvancedSiteSearchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EnableAdvancedSiteSearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EnableAdvancedSiteSearchRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EnableAdvancedSiteSearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EnableAdvancedSiteSearchResponse),[EnableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EnableAdvancedSiteSearchMetadata)>` |   
  
### enableAdvancedSiteSearchCallable()
    
    
    public final UnaryCallable<EnableAdvancedSiteSearchRequest,Operation> enableAdvancedSiteSearchCallable()

Upgrade from basic site search to advanced site search.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       EnableAdvancedSiteSearchRequest request =
           EnableAdvancedSiteSearchRequest.newBuilder()
               .setSiteSearchEngine(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           siteSearchEngineServiceClient.enableAdvancedSiteSearchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[EnableAdvancedSiteSearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EnableAdvancedSiteSearchRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### enableAdvancedSiteSearchOperationCallable()
    
    
    public final OperationCallable<EnableAdvancedSiteSearchRequest,EnableAdvancedSiteSearchResponse,EnableAdvancedSiteSearchMetadata> enableAdvancedSiteSearchOperationCallable()

Upgrade from basic site search to advanced site search.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       EnableAdvancedSiteSearchRequest request =
           EnableAdvancedSiteSearchRequest.newBuilder()
               .setSiteSearchEngine(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .build();
       OperationFuture<EnableAdvancedSiteSearchResponse, EnableAdvancedSiteSearchMetadata> future =
           siteSearchEngineServiceClient
               .enableAdvancedSiteSearchOperationCallable()
               .futureCall(request);
       // Do something.
       EnableAdvancedSiteSearchResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[EnableAdvancedSiteSearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EnableAdvancedSiteSearchRequest),[EnableAdvancedSiteSearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EnableAdvancedSiteSearchResponse),[EnableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.EnableAdvancedSiteSearchMetadata)>` |   
  
### fetchDomainVerificationStatus(FetchDomainVerificationStatusRequest request)
    
    
    public final SiteSearchEngineServiceClient.FetchDomainVerificationStatusPagedResponse fetchDomainVerificationStatus(FetchDomainVerificationStatusRequest request)

Returns list of target sites with its domain verification status. This method can only be called under data store with BASIC_SITE_SEARCH state at the moment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       FetchDomainVerificationStatusRequest request =
           FetchDomainVerificationStatusRequest.newBuilder()
               .setSiteSearchEngine(
                   SiteSearchEngineName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (TargetSite element :
           siteSearchEngineServiceClient.fetchDomainVerificationStatus(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchDomainVerificationStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.FetchDomainVerificationStatusRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SiteSearchEngineServiceClient.FetchDomainVerificationStatusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngineServiceClient.FetchDomainVerificationStatusPagedResponse)` |   
  
### fetchDomainVerificationStatusCallable()
    
    
    public final UnaryCallable<FetchDomainVerificationStatusRequest,FetchDomainVerificationStatusResponse> fetchDomainVerificationStatusCallable()

Returns list of target sites with its domain verification status. This method can only be called under data store with BASIC_SITE_SEARCH state at the moment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       FetchDomainVerificationStatusRequest request =
           FetchDomainVerificationStatusRequest.newBuilder()
               .setSiteSearchEngine(
                   SiteSearchEngineName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         FetchDomainVerificationStatusResponse response =
             siteSearchEngineServiceClient.fetchDomainVerificationStatusCallable().call(request);
         for (TargetSite element : response.getTargetSitesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchDomainVerificationStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.FetchDomainVerificationStatusRequest),[FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.FetchDomainVerificationStatusResponse)>` |   
  
### fetchDomainVerificationStatusPagedCallable()
    
    
    public final UnaryCallable<FetchDomainVerificationStatusRequest,SiteSearchEngineServiceClient.FetchDomainVerificationStatusPagedResponse> fetchDomainVerificationStatusPagedCallable()

Returns list of target sites with its domain verification status. This method can only be called under data store with BASIC_SITE_SEARCH state at the moment.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       FetchDomainVerificationStatusRequest request =
           FetchDomainVerificationStatusRequest.newBuilder()
               .setSiteSearchEngine(
                   SiteSearchEngineName.ofProjectLocationCollectionDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<TargetSite> future =
           siteSearchEngineServiceClient
               .fetchDomainVerificationStatusPagedCallable()
               .futureCall(request);
       // Do something.
       for (TargetSite element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchDomainVerificationStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.FetchDomainVerificationStatusRequest),[FetchDomainVerificationStatusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngineServiceClient.FetchDomainVerificationStatusPagedResponse)>` |   
  
### fetchSitemaps(@Nullable SiteSearchEngineName parent)
    
    
    public final FetchSitemapsResponse fetchSitemaps(@Nullable SiteSearchEngineName parent)

Fetch Sitemaps in a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       SiteSearchEngineName parent =
           SiteSearchEngineName.ofProjectLocationDataStoreName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       FetchSitemapsResponse response = siteSearchEngineServiceClient.fetchSitemaps(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.SiteSearchEngineName`  
Required. Parent resource name of the SiteSearchEngine, such as `projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine`.  
**Returns**  
---  
**Type** | **Description**  
`[FetchSitemapsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.FetchSitemapsResponse)` |   
  
### fetchSitemaps(FetchSitemapsRequest request)
    
    
    public final FetchSitemapsResponse fetchSitemaps(FetchSitemapsRequest request)

Fetch Sitemaps in a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       FetchSitemapsRequest request =
           FetchSitemapsRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setMatcher(FetchSitemapsRequest.Matcher.newBuilder().build())
               .build();
       FetchSitemapsResponse response = siteSearchEngineServiceClient.fetchSitemaps(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchSitemapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.FetchSitemapsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FetchSitemapsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.FetchSitemapsResponse)` |   
  
### fetchSitemaps(String parent)
    
    
    public final FetchSitemapsResponse fetchSitemaps(String parent)

Fetch Sitemaps in a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       String parent =
           SiteSearchEngineName.ofProjectLocationDataStoreName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
               .toString();
       FetchSitemapsResponse response = siteSearchEngineServiceClient.fetchSitemaps(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent resource name of the SiteSearchEngine, such as `projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine`.  
**Returns**  
---  
**Type** | **Description**  
`[FetchSitemapsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.FetchSitemapsResponse)` |   
  
### fetchSitemapsCallable()
    
    
    public final UnaryCallable<FetchSitemapsRequest,FetchSitemapsResponse> fetchSitemapsCallable()

Fetch Sitemaps in a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       FetchSitemapsRequest request =
           FetchSitemapsRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setMatcher(FetchSitemapsRequest.Matcher.newBuilder().build())
               .build();
       ApiFuture<FetchSitemapsResponse> future =
           siteSearchEngineServiceClient.fetchSitemapsCallable().futureCall(request);
       // Do something.
       FetchSitemapsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FetchSitemapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.FetchSitemapsRequest),[FetchSitemapsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.FetchSitemapsResponse)>` |   
  
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
    
    
    public final @Nullable SiteSearchEngineServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.SiteSearchEngineServiceSettings` |   
  
### getSiteSearchEngine(@Nullable SiteSearchEngineName name)
    
    
    public final SiteSearchEngine getSiteSearchEngine(@Nullable SiteSearchEngineName name)

Gets the SiteSearchEngine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       SiteSearchEngineName name =
           SiteSearchEngineName.ofProjectLocationDataStoreName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       SiteSearchEngine response = siteSearchEngineServiceClient.getSiteSearchEngine(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.SiteSearchEngineName`  
Required. Resource name of SiteSearchEngine, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`. If the caller does not have permission to access the [SiteSearchEngine], regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[SiteSearchEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngine)` |   
  
### getSiteSearchEngine(GetSiteSearchEngineRequest request)
    
    
    public final SiteSearchEngine getSiteSearchEngine(GetSiteSearchEngineRequest request)

Gets the SiteSearchEngine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       GetSiteSearchEngineRequest request =
           GetSiteSearchEngineRequest.newBuilder()
               .setName(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .build();
       SiteSearchEngine response = siteSearchEngineServiceClient.getSiteSearchEngine(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSiteSearchEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetSiteSearchEngineRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SiteSearchEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngine)` |   
  
### getSiteSearchEngine(String name)
    
    
    public final SiteSearchEngine getSiteSearchEngine(String name)

Gets the SiteSearchEngine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       String name =
           SiteSearchEngineName.ofProjectLocationDataStoreName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
               .toString();
       SiteSearchEngine response = siteSearchEngineServiceClient.getSiteSearchEngine(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of SiteSearchEngine, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`. If the caller does not have permission to access the [SiteSearchEngine], regardless of whether or not it exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[SiteSearchEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngine)` |   
  
### getSiteSearchEngineCallable()
    
    
    public final UnaryCallable<GetSiteSearchEngineRequest,SiteSearchEngine> getSiteSearchEngineCallable()

Gets the SiteSearchEngine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       GetSiteSearchEngineRequest request =
           GetSiteSearchEngineRequest.newBuilder()
               .setName(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .build();
       ApiFuture<SiteSearchEngine> future =
           siteSearchEngineServiceClient.getSiteSearchEngineCallable().futureCall(request);
       // Do something.
       SiteSearchEngine response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSiteSearchEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetSiteSearchEngineRequest),[SiteSearchEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngine)>` |   
  
### getStub()
    
    
    public SiteSearchEngineServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SiteSearchEngineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.SiteSearchEngineServiceStub)` |   
  
### getTargetSite(@Nullable TargetSiteName name)
    
    
    public final TargetSite getTargetSite(@Nullable TargetSiteName name)

Gets a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       TargetSiteName name =
           TargetSiteName.ofProjectLocationDataStoreTargetSiteName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[TARGET_SITE]");
       TargetSite response = siteSearchEngineServiceClient.getTargetSite(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.TargetSiteName`  
Required. Full resource name of TargetSite, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}`. If the caller does not have permission to access the TargetSite, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the requested TargetSite does not exist, a NOT_FOUND error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[TargetSite](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TargetSite)` |   
  
### getTargetSite(GetTargetSiteRequest request)
    
    
    public final TargetSite getTargetSite(GetTargetSiteRequest request)

Gets a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       GetTargetSiteRequest request =
           GetTargetSiteRequest.newBuilder()
               .setName(
                   TargetSiteName.ofProjectLocationDataStoreTargetSiteName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[TARGET_SITE]")
                       .toString())
               .build();
       TargetSite response = siteSearchEngineServiceClient.getTargetSite(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTargetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetTargetSiteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetSite](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TargetSite)` |   
  
### getTargetSite(String name)
    
    
    public final TargetSite getTargetSite(String name)

Gets a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       String name =
           TargetSiteName.ofProjectLocationDataStoreTargetSiteName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[TARGET_SITE]")
               .toString();
       TargetSite response = siteSearchEngineServiceClient.getTargetSite(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of TargetSite, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}`. If the caller does not have permission to access the TargetSite, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the requested TargetSite does not exist, a NOT_FOUND error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[TargetSite](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TargetSite)` |   
  
### getTargetSiteCallable()
    
    
    public final UnaryCallable<GetTargetSiteRequest,TargetSite> getTargetSiteCallable()

Gets a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       GetTargetSiteRequest request =
           GetTargetSiteRequest.newBuilder()
               .setName(
                   TargetSiteName.ofProjectLocationDataStoreTargetSiteName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[TARGET_SITE]")
                       .toString())
               .build();
       ApiFuture<TargetSite> future =
           siteSearchEngineServiceClient.getTargetSiteCallable().futureCall(request);
       // Do something.
       TargetSite response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTargetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetTargetSiteRequest),[TargetSite](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TargetSite)>` |   
  
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
  
### listTargetSites(@Nullable SiteSearchEngineName parent)
    
    
    public final SiteSearchEngineServiceClient.ListTargetSitesPagedResponse listTargetSites(@Nullable SiteSearchEngineName parent)

Gets a list of TargetSites.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       SiteSearchEngineName parent =
           SiteSearchEngineName.ofProjectLocationDataStoreName(
               "[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       for (TargetSite element :
           siteSearchEngineServiceClient.listTargetSites(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.SiteSearchEngineName`  
Required. The parent site search engine resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`. If the caller does not have permission to list TargetSites under this site search engine, regardless of whether or not this branch exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[SiteSearchEngineServiceClient.ListTargetSitesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngineServiceClient.ListTargetSitesPagedResponse)` |   
  
### listTargetSites(ListTargetSitesRequest request)
    
    
    public final SiteSearchEngineServiceClient.ListTargetSitesPagedResponse listTargetSites(ListTargetSitesRequest request)

Gets a list of TargetSites.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       ListTargetSitesRequest request =
           ListTargetSitesRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (TargetSite element :
           siteSearchEngineServiceClient.listTargetSites(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTargetSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListTargetSitesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SiteSearchEngineServiceClient.ListTargetSitesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngineServiceClient.ListTargetSitesPagedResponse)` |   
  
### listTargetSites(String parent)
    
    
    public final SiteSearchEngineServiceClient.ListTargetSitesPagedResponse listTargetSites(String parent)

Gets a list of TargetSites.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       String parent =
           SiteSearchEngineName.ofProjectLocationDataStoreName(
                   "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
               .toString();
       for (TargetSite element :
           siteSearchEngineServiceClient.listTargetSites(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent site search engine resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`. If the caller does not have permission to list TargetSites under this site search engine, regardless of whether or not this branch exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[SiteSearchEngineServiceClient.ListTargetSitesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngineServiceClient.ListTargetSitesPagedResponse)` |   
  
### listTargetSitesCallable()
    
    
    public final UnaryCallable<ListTargetSitesRequest,ListTargetSitesResponse> listTargetSitesCallable()

Gets a list of TargetSites.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       ListTargetSitesRequest request =
           ListTargetSitesRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListTargetSitesResponse response =
             siteSearchEngineServiceClient.listTargetSitesCallable().call(request);
         for (TargetSite element : response.getTargetSitesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTargetSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListTargetSitesRequest),[ListTargetSitesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListTargetSitesResponse)>` |   
  
### listTargetSitesPagedCallable()
    
    
    public final UnaryCallable<ListTargetSitesRequest,SiteSearchEngineServiceClient.ListTargetSitesPagedResponse> listTargetSitesPagedCallable()

Gets a list of TargetSites.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       ListTargetSitesRequest request =
           ListTargetSitesRequest.newBuilder()
               .setParent(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<TargetSite> future =
           siteSearchEngineServiceClient.listTargetSitesPagedCallable().futureCall(request);
       // Do something.
       for (TargetSite element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTargetSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListTargetSitesRequest),[ListTargetSitesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SiteSearchEngineServiceClient.ListTargetSitesPagedResponse)>` |   
  
### recrawlUrisAsync(RecrawlUrisRequest request)
    
    
    public final OperationFuture<RecrawlUrisResponse,RecrawlUrisMetadata> recrawlUrisAsync(RecrawlUrisRequest request)

Request on-demand recrawl for a list of URIs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       RecrawlUrisRequest request =
           RecrawlUrisRequest.newBuilder()
               .setSiteSearchEngine(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .addAllUris(new ArrayList<String>())
               .setSiteCredential("siteCredential-751929602")
               .build();
       RecrawlUrisResponse response = siteSearchEngineServiceClient.recrawlUrisAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RecrawlUrisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.RecrawlUrisRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[RecrawlUrisResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.RecrawlUrisResponse),[RecrawlUrisMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.RecrawlUrisMetadata)>` |   
  
### recrawlUrisCallable()
    
    
    public final UnaryCallable<RecrawlUrisRequest,Operation> recrawlUrisCallable()

Request on-demand recrawl for a list of URIs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       RecrawlUrisRequest request =
           RecrawlUrisRequest.newBuilder()
               .setSiteSearchEngine(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .addAllUris(new ArrayList<String>())
               .setSiteCredential("siteCredential-751929602")
               .build();
       ApiFuture<Operation> future =
           siteSearchEngineServiceClient.recrawlUrisCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RecrawlUrisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.RecrawlUrisRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### recrawlUrisOperationCallable()
    
    
    public final OperationCallable<RecrawlUrisRequest,RecrawlUrisResponse,RecrawlUrisMetadata> recrawlUrisOperationCallable()

Request on-demand recrawl for a list of URIs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       RecrawlUrisRequest request =
           RecrawlUrisRequest.newBuilder()
               .setSiteSearchEngine(
                   SiteSearchEngineName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .addAllUris(new ArrayList<String>())
               .setSiteCredential("siteCredential-751929602")
               .build();
       OperationFuture<RecrawlUrisResponse, RecrawlUrisMetadata> future =
           siteSearchEngineServiceClient.recrawlUrisOperationCallable().futureCall(request);
       // Do something.
       RecrawlUrisResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RecrawlUrisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.RecrawlUrisRequest),[RecrawlUrisResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.RecrawlUrisResponse),[RecrawlUrisMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.RecrawlUrisMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateTargetSiteAsync(TargetSite targetSite)
    
    
    public final OperationFuture<TargetSite,UpdateTargetSiteMetadata> updateTargetSiteAsync(TargetSite targetSite)

Updates a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       TargetSite targetSite = TargetSite.newBuilder().build();
       TargetSite response = siteSearchEngineServiceClient.updateTargetSiteAsync(targetSite).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`targetSite` | `[TargetSite](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TargetSite)`  
Required. The target site to update. If the caller does not have permission to update the TargetSite, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the TargetSite to update does not exist, a NOT_FOUND error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TargetSite](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TargetSite),[UpdateTargetSiteMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateTargetSiteMetadata)>` |   
  
### updateTargetSiteAsync(UpdateTargetSiteRequest request)
    
    
    public final OperationFuture<TargetSite,UpdateTargetSiteMetadata> updateTargetSiteAsync(UpdateTargetSiteRequest request)

Updates a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       UpdateTargetSiteRequest request =
           UpdateTargetSiteRequest.newBuilder()
               .setTargetSite(TargetSite.newBuilder().build())
               .build();
       TargetSite response = siteSearchEngineServiceClient.updateTargetSiteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTargetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateTargetSiteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TargetSite](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TargetSite),[UpdateTargetSiteMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateTargetSiteMetadata)>` |   
  
### updateTargetSiteCallable()
    
    
    public final UnaryCallable<UpdateTargetSiteRequest,Operation> updateTargetSiteCallable()

Updates a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       UpdateTargetSiteRequest request =
           UpdateTargetSiteRequest.newBuilder()
               .setTargetSite(TargetSite.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           siteSearchEngineServiceClient.updateTargetSiteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTargetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateTargetSiteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateTargetSiteOperationCallable()
    
    
    public final OperationCallable<UpdateTargetSiteRequest,TargetSite,UpdateTargetSiteMetadata> updateTargetSiteOperationCallable()

Updates a TargetSite.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SiteSearchEngineServiceClient siteSearchEngineServiceClient =
         SiteSearchEngineServiceClient.create()) {
       UpdateTargetSiteRequest request =
           UpdateTargetSiteRequest.newBuilder()
               .setTargetSite(TargetSite.newBuilder().build())
               .build();
       OperationFuture<TargetSite, UpdateTargetSiteMetadata> future =
           siteSearchEngineServiceClient.updateTargetSiteOperationCallable().futureCall(request);
       // Do something.
       TargetSite response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateTargetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateTargetSiteRequest),[TargetSite](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.TargetSite),[UpdateTargetSiteMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateTargetSiteMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
