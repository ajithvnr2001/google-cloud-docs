---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileCarrierServiceClient
title: Class MobileCarrierServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:50.157638+00:00
---

# Class MobileCarrierServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileCarrierServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MobileCarrierServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/MobileCarrierServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `MobileCarrier` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileCarrierServiceClient mobileCarrierServiceClient =
         MobileCarrierServiceClient.create()) {
       MobileCarrierName name = MobileCarrierName.of("[NETWORK_CODE]", "[MOBILE_CARRIER]");
       MobileCarrier response = mobileCarrierServiceClient.getMobileCarrier(name);
     }
     

Note: close() needs to be called on the MobileCarrierServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetMobileCarrier |  Retrieves a `MobileCarrier` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMobileCarrier(GetMobileCarrierRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMobileCarrier(MobileCarrierName name) 
  * getMobileCarrier(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMobileCarrierCallable() 

  
ListMobileCarriers |  Lists `MobileCarrier` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMobileCarriers(ListMobileCarriersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMobileCarriers(NetworkName parent) 
  * listMobileCarriers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMobileCarriersPagedCallable() 
  * listMobileCarriersCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of MobileCarrierServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MobileCarrierServiceSettings mobileCarrierServiceSettings =
         MobileCarrierServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     MobileCarrierServiceClient mobileCarrierServiceClient =
         MobileCarrierServiceClient.create(mobileCarrierServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MobileCarrierServiceSettings mobileCarrierServiceSettings =
         MobileCarrierServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     MobileCarrierServiceClient mobileCarrierServiceClient =
         MobileCarrierServiceClient.create(mobileCarrierServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > MobileCarrierServiceClient

## Static Methods 

### create()
    
    
    public static final MobileCarrierServiceClient create()

Constructs an instance of MobileCarrierServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[MobileCarrierServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileCarrierServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MobileCarrierServiceSettings settings)
    
    
    public static final MobileCarrierServiceClient create(MobileCarrierServiceSettings settings)

Constructs an instance of MobileCarrierServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MobileCarrierServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileCarrierServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MobileCarrierServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileCarrierServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MobileCarrierServiceStub stub)
    
    
    public static final MobileCarrierServiceClient create(MobileCarrierServiceStub stub)

Constructs an instance of MobileCarrierServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(MobileCarrierServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MobileCarrierServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.MobileCarrierServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MobileCarrierServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileCarrierServiceClient)` |   
  
## Constructors 

### MobileCarrierServiceClient(MobileCarrierServiceSettings settings)
    
    
    protected MobileCarrierServiceClient(MobileCarrierServiceSettings settings)

Constructs an instance of MobileCarrierServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MobileCarrierServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileCarrierServiceSettings)`  
  
  
### MobileCarrierServiceClient(MobileCarrierServiceStub stub)
    
    
    protected MobileCarrierServiceClient(MobileCarrierServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MobileCarrierServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.MobileCarrierServiceStub)`  
  
  
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

### getMobileCarrier(@Nullable MobileCarrierName name)
    
    
    public final MobileCarrier getMobileCarrier(@Nullable MobileCarrierName name)

Retrieves a `MobileCarrier` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileCarrierServiceClient mobileCarrierServiceClient =
         MobileCarrierServiceClient.create()) {
       MobileCarrierName name = MobileCarrierName.of("[NETWORK_CODE]", "[MOBILE_CARRIER]");
       MobileCarrier response = mobileCarrierServiceClient.getMobileCarrier(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.MobileCarrierName`  
Required. The resource name of the MobileCarrier. Format: `networks/{network_code}/mobileCarriers/{mobile_carrier_id}`  
**Returns**  
---  
**Type** | **Description**  
`[MobileCarrier](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileCarrier)` |   
  
### getMobileCarrier(GetMobileCarrierRequest request)
    
    
    public final MobileCarrier getMobileCarrier(GetMobileCarrierRequest request)

Retrieves a `MobileCarrier` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileCarrierServiceClient mobileCarrierServiceClient =
         MobileCarrierServiceClient.create()) {
       GetMobileCarrierRequest request =
           GetMobileCarrierRequest.newBuilder()
               .setName(MobileCarrierName.of("[NETWORK_CODE]", "[MOBILE_CARRIER]").toString())
               .build();
       MobileCarrier response = mobileCarrierServiceClient.getMobileCarrier(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMobileCarrierRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetMobileCarrierRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MobileCarrier](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileCarrier)` |   
  
### getMobileCarrier(String name)
    
    
    public final MobileCarrier getMobileCarrier(String name)

Retrieves a `MobileCarrier` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileCarrierServiceClient mobileCarrierServiceClient =
         MobileCarrierServiceClient.create()) {
       String name = MobileCarrierName.of("[NETWORK_CODE]", "[MOBILE_CARRIER]").toString();
       MobileCarrier response = mobileCarrierServiceClient.getMobileCarrier(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the MobileCarrier. Format: `networks/{network_code}/mobileCarriers/{mobile_carrier_id}`  
**Returns**  
---  
**Type** | **Description**  
`[MobileCarrier](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileCarrier)` |   
  
### getMobileCarrierCallable()
    
    
    public final UnaryCallable<GetMobileCarrierRequest,MobileCarrier> getMobileCarrierCallable()

Retrieves a `MobileCarrier` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileCarrierServiceClient mobileCarrierServiceClient =
         MobileCarrierServiceClient.create()) {
       GetMobileCarrierRequest request =
           GetMobileCarrierRequest.newBuilder()
               .setName(MobileCarrierName.of("[NETWORK_CODE]", "[MOBILE_CARRIER]").toString())
               .build();
       ApiFuture<MobileCarrier> future =
           mobileCarrierServiceClient.getMobileCarrierCallable().futureCall(request);
       // Do something.
       MobileCarrier response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMobileCarrierRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetMobileCarrierRequest),[MobileCarrier](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileCarrier)>` |   
  
### getSettings()
    
    
    public final @Nullable MobileCarrierServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.MobileCarrierServiceSettings` |   
  
### getStub()
    
    
    public MobileCarrierServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[MobileCarrierServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.MobileCarrierServiceStub)` |   
  
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
  
### listMobileCarriers(@Nullable NetworkName parent)
    
    
    public final MobileCarrierServiceClient.ListMobileCarriersPagedResponse listMobileCarriers(@Nullable NetworkName parent)

Lists `MobileCarrier` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileCarrierServiceClient mobileCarrierServiceClient =
         MobileCarrierServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (MobileCarrier element :
           mobileCarrierServiceClient.listMobileCarriers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of MobileCarriers. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[MobileCarrierServiceClient.ListMobileCarriersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileCarrierServiceClient.ListMobileCarriersPagedResponse)` |   
  
### listMobileCarriers(ListMobileCarriersRequest request)
    
    
    public final MobileCarrierServiceClient.ListMobileCarriersPagedResponse listMobileCarriers(ListMobileCarriersRequest request)

Lists `MobileCarrier` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileCarrierServiceClient mobileCarrierServiceClient =
         MobileCarrierServiceClient.create()) {
       ListMobileCarriersRequest request =
           ListMobileCarriersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (MobileCarrier element :
           mobileCarrierServiceClient.listMobileCarriers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMobileCarriersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListMobileCarriersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MobileCarrierServiceClient.ListMobileCarriersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileCarrierServiceClient.ListMobileCarriersPagedResponse)` |   
  
### listMobileCarriers(String parent)
    
    
    public final MobileCarrierServiceClient.ListMobileCarriersPagedResponse listMobileCarriers(String parent)

Lists `MobileCarrier` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileCarrierServiceClient mobileCarrierServiceClient =
         MobileCarrierServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (MobileCarrier element :
           mobileCarrierServiceClient.listMobileCarriers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of MobileCarriers. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[MobileCarrierServiceClient.ListMobileCarriersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileCarrierServiceClient.ListMobileCarriersPagedResponse)` |   
  
### listMobileCarriersCallable()
    
    
    public final UnaryCallable<ListMobileCarriersRequest,ListMobileCarriersResponse> listMobileCarriersCallable()

Lists `MobileCarrier` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileCarrierServiceClient mobileCarrierServiceClient =
         MobileCarrierServiceClient.create()) {
       ListMobileCarriersRequest request =
           ListMobileCarriersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListMobileCarriersResponse response =
             mobileCarrierServiceClient.listMobileCarriersCallable().call(request);
         for (MobileCarrier element : response.getMobileCarriersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMobileCarriersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListMobileCarriersRequest),[ListMobileCarriersResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListMobileCarriersResponse)>` |   
  
### listMobileCarriersPagedCallable()
    
    
    public final UnaryCallable<ListMobileCarriersRequest,MobileCarrierServiceClient.ListMobileCarriersPagedResponse> listMobileCarriersPagedCallable()

Lists `MobileCarrier` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MobileCarrierServiceClient mobileCarrierServiceClient =
         MobileCarrierServiceClient.create()) {
       ListMobileCarriersRequest request =
           ListMobileCarriersRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<MobileCarrier> future =
           mobileCarrierServiceClient.listMobileCarriersPagedCallable().futureCall(request);
       // Do something.
       for (MobileCarrier element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMobileCarriersRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListMobileCarriersRequest),[ListMobileCarriersPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MobileCarrierServiceClient.ListMobileCarriersPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
