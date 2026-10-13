---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RichMediaAdsCompanyServiceClient
title: Class RichMediaAdsCompanyServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:09:01.778532+00:00
---

# Class RichMediaAdsCompanyServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RichMediaAdsCompanyServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RichMediaAdsCompanyServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/RichMediaAdsCompanyServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `RichMediaAdsCompany` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RichMediaAdsCompanyServiceClient richMediaAdsCompanyServiceClient =
         RichMediaAdsCompanyServiceClient.create()) {
       RichMediaAdsCompanyName name =
           RichMediaAdsCompanyName.of("[NETWORK_CODE]", "[RICH_MEDIA_ADS_COMPANY]");
       RichMediaAdsCompany response = richMediaAdsCompanyServiceClient.getRichMediaAdsCompany(name);
     }
     

Note: close() needs to be called on the RichMediaAdsCompanyServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetRichMediaAdsCompany |  Retrieves a `RichMediaAdsCompany` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRichMediaAdsCompany(GetRichMediaAdsCompanyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRichMediaAdsCompany(RichMediaAdsCompanyName name) 
  * getRichMediaAdsCompany(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRichMediaAdsCompanyCallable() 

  
ListRichMediaAdsCompanies |  Lists `RichMediaAdsCompany` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRichMediaAdsCompanies(ListRichMediaAdsCompaniesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRichMediaAdsCompanies(NetworkName parent) 
  * listRichMediaAdsCompanies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRichMediaAdsCompaniesPagedCallable() 
  * listRichMediaAdsCompaniesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RichMediaAdsCompanyServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RichMediaAdsCompanyServiceSettings richMediaAdsCompanyServiceSettings =
         RichMediaAdsCompanyServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RichMediaAdsCompanyServiceClient richMediaAdsCompanyServiceClient =
         RichMediaAdsCompanyServiceClient.create(richMediaAdsCompanyServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RichMediaAdsCompanyServiceSettings richMediaAdsCompanyServiceSettings =
         RichMediaAdsCompanyServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     RichMediaAdsCompanyServiceClient richMediaAdsCompanyServiceClient =
         RichMediaAdsCompanyServiceClient.create(richMediaAdsCompanyServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RichMediaAdsCompanyServiceClient

## Static Methods 

### create()
    
    
    public static final RichMediaAdsCompanyServiceClient create()

Constructs an instance of RichMediaAdsCompanyServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RichMediaAdsCompanyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RichMediaAdsCompanyServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RichMediaAdsCompanyServiceSettings settings)
    
    
    public static final RichMediaAdsCompanyServiceClient create(RichMediaAdsCompanyServiceSettings settings)

Constructs an instance of RichMediaAdsCompanyServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RichMediaAdsCompanyServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RichMediaAdsCompanyServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RichMediaAdsCompanyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RichMediaAdsCompanyServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RichMediaAdsCompanyServiceStub stub)
    
    
    public static final RichMediaAdsCompanyServiceClient create(RichMediaAdsCompanyServiceStub stub)

Constructs an instance of RichMediaAdsCompanyServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(RichMediaAdsCompanyServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RichMediaAdsCompanyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.RichMediaAdsCompanyServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RichMediaAdsCompanyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RichMediaAdsCompanyServiceClient)` |   
  
## Constructors 

### RichMediaAdsCompanyServiceClient(RichMediaAdsCompanyServiceSettings settings)
    
    
    protected RichMediaAdsCompanyServiceClient(RichMediaAdsCompanyServiceSettings settings)

Constructs an instance of RichMediaAdsCompanyServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RichMediaAdsCompanyServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RichMediaAdsCompanyServiceSettings)`  
  
  
### RichMediaAdsCompanyServiceClient(RichMediaAdsCompanyServiceStub stub)
    
    
    protected RichMediaAdsCompanyServiceClient(RichMediaAdsCompanyServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RichMediaAdsCompanyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.RichMediaAdsCompanyServiceStub)`  
  
  
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
  
### close()
    
    
    public final void close()

### getRichMediaAdsCompany(@Nullable RichMediaAdsCompanyName name)
    
    
    public final RichMediaAdsCompany getRichMediaAdsCompany(@Nullable RichMediaAdsCompanyName name)

Retrieves a `RichMediaAdsCompany` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RichMediaAdsCompanyServiceClient richMediaAdsCompanyServiceClient =
         RichMediaAdsCompanyServiceClient.create()) {
       RichMediaAdsCompanyName name =
           RichMediaAdsCompanyName.of("[NETWORK_CODE]", "[RICH_MEDIA_ADS_COMPANY]");
       RichMediaAdsCompany response = richMediaAdsCompanyServiceClient.getRichMediaAdsCompany(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.RichMediaAdsCompanyName`  
Required. The resource name of the RichMediaAdsCompany. Format: `networks/{network_code}/richMediaAdsCompanies/{rich_media_ads_company_id}`  
**Returns**  
---  
**Type** | **Description**  
`[RichMediaAdsCompany](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RichMediaAdsCompany)` |   
  
### getRichMediaAdsCompany(GetRichMediaAdsCompanyRequest request)
    
    
    public final RichMediaAdsCompany getRichMediaAdsCompany(GetRichMediaAdsCompanyRequest request)

Retrieves a `RichMediaAdsCompany` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RichMediaAdsCompanyServiceClient richMediaAdsCompanyServiceClient =
         RichMediaAdsCompanyServiceClient.create()) {
       GetRichMediaAdsCompanyRequest request =
           GetRichMediaAdsCompanyRequest.newBuilder()
               .setName(
                   RichMediaAdsCompanyName.of("[NETWORK_CODE]", "[RICH_MEDIA_ADS_COMPANY]")
                       .toString())
               .build();
       RichMediaAdsCompany response =
           richMediaAdsCompanyServiceClient.getRichMediaAdsCompany(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRichMediaAdsCompanyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetRichMediaAdsCompanyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RichMediaAdsCompany](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RichMediaAdsCompany)` |   
  
### getRichMediaAdsCompany(String name)
    
    
    public final RichMediaAdsCompany getRichMediaAdsCompany(String name)

Retrieves a `RichMediaAdsCompany` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RichMediaAdsCompanyServiceClient richMediaAdsCompanyServiceClient =
         RichMediaAdsCompanyServiceClient.create()) {
       String name =
           RichMediaAdsCompanyName.of("[NETWORK_CODE]", "[RICH_MEDIA_ADS_COMPANY]").toString();
       RichMediaAdsCompany response = richMediaAdsCompanyServiceClient.getRichMediaAdsCompany(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the RichMediaAdsCompany. Format: `networks/{network_code}/richMediaAdsCompanies/{rich_media_ads_company_id}`  
**Returns**  
---  
**Type** | **Description**  
`[RichMediaAdsCompany](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RichMediaAdsCompany)` |   
  
### getRichMediaAdsCompanyCallable()
    
    
    public final UnaryCallable<GetRichMediaAdsCompanyRequest,RichMediaAdsCompany> getRichMediaAdsCompanyCallable()

Retrieves a `RichMediaAdsCompany` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RichMediaAdsCompanyServiceClient richMediaAdsCompanyServiceClient =
         RichMediaAdsCompanyServiceClient.create()) {
       GetRichMediaAdsCompanyRequest request =
           GetRichMediaAdsCompanyRequest.newBuilder()
               .setName(
                   RichMediaAdsCompanyName.of("[NETWORK_CODE]", "[RICH_MEDIA_ADS_COMPANY]")
                       .toString())
               .build();
       ApiFuture<RichMediaAdsCompany> future =
           richMediaAdsCompanyServiceClient.getRichMediaAdsCompanyCallable().futureCall(request);
       // Do something.
       RichMediaAdsCompany response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRichMediaAdsCompanyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetRichMediaAdsCompanyRequest),[RichMediaAdsCompany](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RichMediaAdsCompany)>` |   
  
### getSettings()
    
    
    public final @Nullable RichMediaAdsCompanyServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.RichMediaAdsCompanyServiceSettings` |   
  
### getStub()
    
    
    public RichMediaAdsCompanyServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RichMediaAdsCompanyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.RichMediaAdsCompanyServiceStub)` |   
  
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
  
### listRichMediaAdsCompanies(@Nullable NetworkName parent)
    
    
    public final RichMediaAdsCompanyServiceClient.ListRichMediaAdsCompaniesPagedResponse listRichMediaAdsCompanies(@Nullable NetworkName parent)

Lists `RichMediaAdsCompany` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RichMediaAdsCompanyServiceClient richMediaAdsCompanyServiceClient =
         RichMediaAdsCompanyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (RichMediaAdsCompany element :
           richMediaAdsCompanyServiceClient.listRichMediaAdsCompanies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of RichMediaAdsCompanies. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[RichMediaAdsCompanyServiceClient.ListRichMediaAdsCompaniesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RichMediaAdsCompanyServiceClient.ListRichMediaAdsCompaniesPagedResponse)` |   
  
### listRichMediaAdsCompanies(ListRichMediaAdsCompaniesRequest request)
    
    
    public final RichMediaAdsCompanyServiceClient.ListRichMediaAdsCompaniesPagedResponse listRichMediaAdsCompanies(ListRichMediaAdsCompaniesRequest request)

Lists `RichMediaAdsCompany` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RichMediaAdsCompanyServiceClient richMediaAdsCompanyServiceClient =
         RichMediaAdsCompanyServiceClient.create()) {
       ListRichMediaAdsCompaniesRequest request =
           ListRichMediaAdsCompaniesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (RichMediaAdsCompany element :
           richMediaAdsCompanyServiceClient.listRichMediaAdsCompanies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRichMediaAdsCompaniesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListRichMediaAdsCompaniesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RichMediaAdsCompanyServiceClient.ListRichMediaAdsCompaniesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RichMediaAdsCompanyServiceClient.ListRichMediaAdsCompaniesPagedResponse)` |   
  
### listRichMediaAdsCompanies(String parent)
    
    
    public final RichMediaAdsCompanyServiceClient.ListRichMediaAdsCompaniesPagedResponse listRichMediaAdsCompanies(String parent)

Lists `RichMediaAdsCompany` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RichMediaAdsCompanyServiceClient richMediaAdsCompanyServiceClient =
         RichMediaAdsCompanyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (RichMediaAdsCompany element :
           richMediaAdsCompanyServiceClient.listRichMediaAdsCompanies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of RichMediaAdsCompanies. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[RichMediaAdsCompanyServiceClient.ListRichMediaAdsCompaniesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RichMediaAdsCompanyServiceClient.ListRichMediaAdsCompaniesPagedResponse)` |   
  
### listRichMediaAdsCompaniesCallable()
    
    
    public final UnaryCallable<ListRichMediaAdsCompaniesRequest,ListRichMediaAdsCompaniesResponse> listRichMediaAdsCompaniesCallable()

Lists `RichMediaAdsCompany` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RichMediaAdsCompanyServiceClient richMediaAdsCompanyServiceClient =
         RichMediaAdsCompanyServiceClient.create()) {
       ListRichMediaAdsCompaniesRequest request =
           ListRichMediaAdsCompaniesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListRichMediaAdsCompaniesResponse response =
             richMediaAdsCompanyServiceClient.listRichMediaAdsCompaniesCallable().call(request);
         for (RichMediaAdsCompany element : response.getRichMediaAdsCompaniesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRichMediaAdsCompaniesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListRichMediaAdsCompaniesRequest),[ListRichMediaAdsCompaniesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListRichMediaAdsCompaniesResponse)>` |   
  
### listRichMediaAdsCompaniesPagedCallable()
    
    
    public final UnaryCallable<ListRichMediaAdsCompaniesRequest,RichMediaAdsCompanyServiceClient.ListRichMediaAdsCompaniesPagedResponse> listRichMediaAdsCompaniesPagedCallable()

Lists `RichMediaAdsCompany` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RichMediaAdsCompanyServiceClient richMediaAdsCompanyServiceClient =
         RichMediaAdsCompanyServiceClient.create()) {
       ListRichMediaAdsCompaniesRequest request =
           ListRichMediaAdsCompaniesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<RichMediaAdsCompany> future =
           richMediaAdsCompanyServiceClient
               .listRichMediaAdsCompaniesPagedCallable()
               .futureCall(request);
       // Do something.
       for (RichMediaAdsCompany element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRichMediaAdsCompaniesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListRichMediaAdsCompaniesRequest),[ListRichMediaAdsCompaniesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.RichMediaAdsCompanyServiceClient.ListRichMediaAdsCompaniesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
