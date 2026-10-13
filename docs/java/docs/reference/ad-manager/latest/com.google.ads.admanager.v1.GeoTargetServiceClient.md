---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GeoTargetServiceClient
title: Class GeoTargetServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:44.618283+00:00
---

# Class GeoTargetServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GeoTargetServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GeoTargetServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/GeoTargetServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `GeoTarget` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeoTargetServiceClient geoTargetServiceClient = GeoTargetServiceClient.create()) {
       GeoTargetName name = GeoTargetName.of("[NETWORK_CODE]", "[GEO_TARGET]");
       GeoTarget response = geoTargetServiceClient.getGeoTarget(name);
     }
     

Note: close() needs to be called on the GeoTargetServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetGeoTarget |  Retrieves a `GeoTarget` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getGeoTarget(GetGeoTargetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getGeoTarget(GeoTargetName name) 
  * getGeoTarget(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getGeoTargetCallable() 

  
ListGeoTargets |  Lists `GeoTarget` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGeoTargets(ListGeoTargetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGeoTargets(NetworkName parent) 
  * listGeoTargets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGeoTargetsPagedCallable() 
  * listGeoTargetsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of GeoTargetServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GeoTargetServiceSettings geoTargetServiceSettings =
         GeoTargetServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     GeoTargetServiceClient geoTargetServiceClient =
         GeoTargetServiceClient.create(geoTargetServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GeoTargetServiceSettings geoTargetServiceSettings =
         GeoTargetServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     GeoTargetServiceClient geoTargetServiceClient =
         GeoTargetServiceClient.create(geoTargetServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GeoTargetServiceClient

## Static Methods 

### create()
    
    
    public static final GeoTargetServiceClient create()

Constructs an instance of GeoTargetServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[GeoTargetServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GeoTargetServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GeoTargetServiceSettings settings)
    
    
    public static final GeoTargetServiceClient create(GeoTargetServiceSettings settings)

Constructs an instance of GeoTargetServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GeoTargetServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GeoTargetServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GeoTargetServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GeoTargetServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GeoTargetServiceStub stub)
    
    
    public static final GeoTargetServiceClient create(GeoTargetServiceStub stub)

Constructs an instance of GeoTargetServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(GeoTargetServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GeoTargetServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.GeoTargetServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GeoTargetServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GeoTargetServiceClient)` |   
  
## Constructors 

### GeoTargetServiceClient(GeoTargetServiceSettings settings)
    
    
    protected GeoTargetServiceClient(GeoTargetServiceSettings settings)

Constructs an instance of GeoTargetServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GeoTargetServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GeoTargetServiceSettings)`  
  
  
### GeoTargetServiceClient(GeoTargetServiceStub stub)
    
    
    protected GeoTargetServiceClient(GeoTargetServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GeoTargetServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.GeoTargetServiceStub)`  
  
  
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

### getGeoTarget(@Nullable GeoTargetName name)
    
    
    public final GeoTarget getGeoTarget(@Nullable GeoTargetName name)

Retrieves a `GeoTarget` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeoTargetServiceClient geoTargetServiceClient = GeoTargetServiceClient.create()) {
       GeoTargetName name = GeoTargetName.of("[NETWORK_CODE]", "[GEO_TARGET]");
       GeoTarget response = geoTargetServiceClient.getGeoTarget(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.GeoTargetName`  
Required. The resource name of the GeoTarget. Format: `networks/{network_code}/geoTargets/{geo_target_id}`  
**Returns**  
---  
**Type** | **Description**  
`[GeoTarget](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GeoTarget)` |   
  
### getGeoTarget(GetGeoTargetRequest request)
    
    
    public final GeoTarget getGeoTarget(GetGeoTargetRequest request)

Retrieves a `GeoTarget` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeoTargetServiceClient geoTargetServiceClient = GeoTargetServiceClient.create()) {
       GetGeoTargetRequest request =
           GetGeoTargetRequest.newBuilder()
               .setName(GeoTargetName.of("[NETWORK_CODE]", "[GEO_TARGET]").toString())
               .build();
       GeoTarget response = geoTargetServiceClient.getGeoTarget(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGeoTargetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetGeoTargetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GeoTarget](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GeoTarget)` |   
  
### getGeoTarget(String name)
    
    
    public final GeoTarget getGeoTarget(String name)

Retrieves a `GeoTarget` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeoTargetServiceClient geoTargetServiceClient = GeoTargetServiceClient.create()) {
       String name = GeoTargetName.of("[NETWORK_CODE]", "[GEO_TARGET]").toString();
       GeoTarget response = geoTargetServiceClient.getGeoTarget(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the GeoTarget. Format: `networks/{network_code}/geoTargets/{geo_target_id}`  
**Returns**  
---  
**Type** | **Description**  
`[GeoTarget](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GeoTarget)` |   
  
### getGeoTargetCallable()
    
    
    public final UnaryCallable<GetGeoTargetRequest,GeoTarget> getGeoTargetCallable()

Retrieves a `GeoTarget` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeoTargetServiceClient geoTargetServiceClient = GeoTargetServiceClient.create()) {
       GetGeoTargetRequest request =
           GetGeoTargetRequest.newBuilder()
               .setName(GeoTargetName.of("[NETWORK_CODE]", "[GEO_TARGET]").toString())
               .build();
       ApiFuture<GeoTarget> future =
           geoTargetServiceClient.getGeoTargetCallable().futureCall(request);
       // Do something.
       GeoTarget response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGeoTargetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetGeoTargetRequest),[GeoTarget](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GeoTarget)>` |   
  
### getSettings()
    
    
    public final @Nullable GeoTargetServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.GeoTargetServiceSettings` |   
  
### getStub()
    
    
    public GeoTargetServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[GeoTargetServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.GeoTargetServiceStub)` |   
  
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
  
### listGeoTargets(@Nullable NetworkName parent)
    
    
    public final GeoTargetServiceClient.ListGeoTargetsPagedResponse listGeoTargets(@Nullable NetworkName parent)

Lists `GeoTarget` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeoTargetServiceClient geoTargetServiceClient = GeoTargetServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (GeoTarget element : geoTargetServiceClient.listGeoTargets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of GeoTargets. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[GeoTargetServiceClient.ListGeoTargetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GeoTargetServiceClient.ListGeoTargetsPagedResponse)` |   
  
### listGeoTargets(ListGeoTargetsRequest request)
    
    
    public final GeoTargetServiceClient.ListGeoTargetsPagedResponse listGeoTargets(ListGeoTargetsRequest request)

Lists `GeoTarget` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeoTargetServiceClient geoTargetServiceClient = GeoTargetServiceClient.create()) {
       ListGeoTargetsRequest request =
           ListGeoTargetsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (GeoTarget element : geoTargetServiceClient.listGeoTargets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGeoTargetsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListGeoTargetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GeoTargetServiceClient.ListGeoTargetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GeoTargetServiceClient.ListGeoTargetsPagedResponse)` |   
  
### listGeoTargets(String parent)
    
    
    public final GeoTargetServiceClient.ListGeoTargetsPagedResponse listGeoTargets(String parent)

Lists `GeoTarget` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeoTargetServiceClient geoTargetServiceClient = GeoTargetServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (GeoTarget element : geoTargetServiceClient.listGeoTargets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of GeoTargets. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[GeoTargetServiceClient.ListGeoTargetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GeoTargetServiceClient.ListGeoTargetsPagedResponse)` |   
  
### listGeoTargetsCallable()
    
    
    public final UnaryCallable<ListGeoTargetsRequest,ListGeoTargetsResponse> listGeoTargetsCallable()

Lists `GeoTarget` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeoTargetServiceClient geoTargetServiceClient = GeoTargetServiceClient.create()) {
       ListGeoTargetsRequest request =
           ListGeoTargetsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListGeoTargetsResponse response =
             geoTargetServiceClient.listGeoTargetsCallable().call(request);
         for (GeoTarget element : response.getGeoTargetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGeoTargetsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListGeoTargetsRequest),[ListGeoTargetsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListGeoTargetsResponse)>` |   
  
### listGeoTargetsPagedCallable()
    
    
    public final UnaryCallable<ListGeoTargetsRequest,GeoTargetServiceClient.ListGeoTargetsPagedResponse> listGeoTargetsPagedCallable()

Lists `GeoTarget` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GeoTargetServiceClient geoTargetServiceClient = GeoTargetServiceClient.create()) {
       ListGeoTargetsRequest request =
           ListGeoTargetsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<GeoTarget> future =
           geoTargetServiceClient.listGeoTargetsPagedCallable().futureCall(request);
       // Do something.
       for (GeoTarget element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGeoTargetsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListGeoTargetsRequest),[ListGeoTargetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GeoTargetServiceClient.ListGeoTargetsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
